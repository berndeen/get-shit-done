# Close CRM — Daily Call Transcript Analysis Workflow

## Development Plan for n8n Automation

---

## Overview

Automated daily workflow that extracts call transcripts from Close CRM, groups them by sales agent, and uses AI to identify why leads are not qualifying. Results are pushed to a Google Sheet.

**Trigger:** Daily at 17:00 CET/CEST
**Stack:** n8n (orchestration) + Close API (data) + Claude API (analysis)
**Output:** Google Sheet — one row per unqualified call, grouped by agent

---

## Architecture

```
[Cron Trigger 17:00 CET]
        │
        ▼
[Close API: List Agents]
        │
        ▼
[Close API: Fetch Today's Calls Per Agent]
        │
        ▼
[Filter: Only Calls With Transcripts]
        │
        ▼
[Close API: Fetch Lead Name for Each Call]
        │
        ▼
[Batch Transcripts Per Agent]
        │
        ▼
[Claude API: Why is this lead not qualified?]
        │
        ▼
[Append Rows to Google Sheet]
```

---

## Phase 1 — Credentials & Setup

### 1.1 Close API Key
- Go to **Close → Settings → API Keys**
- Generate a key, name it `n8n-transcript-analysis`
- In n8n: create HTTP Basic Auth credential — API key as username, password blank
- **Base URL:** `https://api.close.com/api/v1/`

### 1.2 Claude API Key
- Get key from **console.anthropic.com**
- In n8n: store as a generic credential or use in HTTP Request header
- **Endpoint:** `https://api.anthropic.com/v1/messages`
- **Headers:** `x-api-key: {key}`, `anthropic-version: 2023-06-01`

### 1.3 Google Sheets
- Create a Google Sheet with this header row:

```
Date | Agent | Lead Name | Not Qualified Reason | Key Quote From Lead
```

- In n8n: connect Google Sheets credential (OAuth2)
- Note the Sheet ID and tab name

---

## Phase 2 — Fetch Agents

### n8n Node: HTTP Request

```
GET https://api.close.com/api/v1/user/
```

**Extract per user:**
- `id` — to filter calls
- `first_name` + `last_name` — for the Agent column

**Filter:** Exclude inactive users or non-sales roles if needed.

---

## Phase 3 — Fetch Today's Calls Per Agent

### n8n Node: Loop Over Agents → HTTP Request

For each agent:

```
GET https://api.close.com/api/v1/activity/call/
```

**Query Parameters:**

| Parameter | Value |
|---|---|
| `user_id` | `{agent.id}` |
| `date_created__gt` | `{today}T00:00:00+01:00` |
| `date_created__lt` | `{today}T17:00:00+01:00` |
| `_fields` | `id,user_id,lead_id,duration,recording_transcript,date_created` |
| `_limit` | `100` |

### Pagination
- If `has_more` is `true`, increment `_skip` by 100 and repeat
- Collect all results per agent

### Filter
- Remove calls where `recording_transcript` is `null`

**Important:** `recording_transcript` is NOT returned by default — it MUST be listed in `_fields`.

---

## Phase 4 — Get Lead Names

### n8n Node: HTTP Request (per unique lead_id)

```
GET https://api.close.com/api/v1/lead/{lead_id}/?_fields=id,display_name
```

Attach `display_name` to each call record. De-duplicate lead_ids first to avoid redundant API calls.

---

## Phase 5 — Claude Analysis

### 5.1 Batch Transcripts Per Agent

Group all calls with transcripts into one payload per agent. This keeps cost low (one API call per agent instead of per call).

### 5.2 HTTP Request to Claude

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "<<PROMPT>>"
    }
  ]
}
```

### 5.3 Prompt

```
You are analysing sales call transcripts for agent {{agent_name}}.

For each call, determine: is this lead qualified or not?

If NOT qualified, provide:
1. The reason why — in plain language, one sentence
2. One direct quote from the lead that shows why they are not qualified

Only include calls where the lead is NOT qualified. Skip qualified leads entirely.

TRANSCRIPTS:

{{#each calls}}
---
Call: {{lead_name}}
Duration: {{duration}} seconds

{{#each recording_transcript.utterances}}
[{{speaker_side}}] {{speaker_label}}: {{text}}
{{/each}}
---
{{/each}}

Respond ONLY with valid JSON, no other text:
[
  {
    "lead_name": "string",
    "reason": "string — plain language, one sentence explaining why not qualified",
    "key_quote": "string — one direct quote from the lead"
  }
]

If all leads are qualified, return an empty array: []
```

### 5.4 Model Choice
- **Default:** `claude-sonnet-4-6` — fast, accurate, good value
- **Budget option:** `claude-haiku-4-5` — ~10x cheaper, still handles this well
- **Alternative:** GPT-4o works too — the prompt is model-agnostic

---

## Phase 6 — Push to Google Sheet

### n8n Node: Google Sheets — Append Rows

Parse Claude's JSON response and append one row per unqualified lead:

| Date | Agent | Lead Name | Not Qualified Reason | Key Quote From Lead |
|---|---|---|---|---|
| `{today}` | `{agent_name}` | From Claude JSON `lead_name` | From Claude JSON `reason` | From Claude JSON `key_quote` |

If Claude returns an empty array (all qualified), write nothing for that agent — or optionally append a single row: `{date} | {agent} | — | All leads qualified today | —`

---

## Phase 7 — Error Handling

| Scenario | How to Handle |
|---|---|
| **Rate limiting (Close)** | 60 req/min — add 1s delay between calls per agent |
| **Rate limiting (Claude)** | n8n retry on error: 3 retries, 5s wait |
| **No calls today** | Skip agent, no rows written |
| **No transcripts** | Skip agent, no rows written |
| **50+ calls for one agent** | Split into batches of 20 transcripts per Claude request, merge results |
| **Claude returns invalid JSON** | Log error, retry once, flag in sheet as "Analysis failed" |

---

## n8n Workflow Node Summary

| # | Node Type | Name | Purpose |
|---|---|---|---|
| 1 | Cron | `Daily 17:00 CET` | Trigger |
| 2 | HTTP Request | `Get Agents` | `GET /user/` |
| 3 | Function | `Filter Active Agents` | Remove non-sales users |
| 4 | Split In Batches | `Loop Agents` | One iteration per agent |
| 5 | HTTP Request | `Get Calls` | `GET /activity/call/?user_id=...&_fields=recording_transcript,...` |
| 6 | IF | `Has More Pages?` | Pagination loop |
| 7 | Function | `Filter Has Transcript` | Drop calls without transcripts |
| 8 | HTTP Request | `Get Lead Name` | `GET /lead/{id}/?_fields=display_name` |
| 9 | Function | `Build Claude Payload` | Merge transcripts + lead names into prompt |
| 10 | HTTP Request | `Claude Analysis` | `POST /v1/messages` |
| 11 | Function | `Parse Response` | Extract JSON array from Claude |
| 12 | Google Sheets | `Append Rows` | Write results to sheet |
| 13 | NoOp | `Error Handler` | Catch failures, notify |

---

## Configuration Variables

```
CLOSE_API_KEY=         # Close CRM API key
CLAUDE_API_KEY=        # Anthropic API key
TIMEZONE=Europe/Berlin # Or Europe/Amsterdam, Europe/Paris, etc.
GOOGLE_SHEET_ID=       # Target spreadsheet ID
GOOGLE_SHEET_TAB=      # Tab name (e.g., "DQ Analysis")
```

---

## Cost Estimate

- Average transcript: ~500-1500 tokens
- 20 calls per agent batch: ~10,000-30,000 input tokens
- **Per agent per day:** ~$0.03-0.10 (Sonnet) or ~$0.003-0.01 (Haiku)
- 5 agents = ~$0.15-0.50/day with Sonnet

---

## Testing Checklist

- [ ] Close API key authenticates
- [ ] Agent list returns correct users
- [ ] Calls endpoint returns `recording_transcript` when requested in `_fields`
- [ ] Pagination works for agents with 100+ calls
- [ ] Lead names resolve correctly
- [ ] Claude returns valid JSON matching expected structure
- [ ] Empty array returned when all leads are qualified
- [ ] Google Sheet rows appear with correct columns
- [ ] Cron fires at 17:00 CET (verify DST handling for CEST)
- [ ] Full run completes within ~10 minutes
