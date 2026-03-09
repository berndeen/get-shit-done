# Close CRM — Daily Call Transcript Analysis Workflow

## Development Plan for n8n Automation

---

## Overview

Automated daily workflow that extracts call transcripts from Close CRM, groups them by sales agent, and uses AI to analyse why leads are not qualifying — surfacing actionable patterns per agent.

**Trigger:** Daily at 17:00 CET/CEST
**Stack:** n8n (orchestration) + Close API (data) + Claude API (analysis)
**Output:** Per-agent qualification failure report delivered to Slack/email/Google Sheets

---

## Architecture

```
[Cron Trigger 17:00 CET]
        │
        ▼
[Close API: List Users/Agents]
        │
        ▼
[Close API: Fetch Today's Calls Per Agent]
        │
        ▼
[Filter: Only Calls With Transcripts]
        │
        ▼
[Close API: Fetch Lead Data for Each Call]
        │
        ▼
[Batch by Agent]
        │
        ▼
[Claude API: Analyse Transcripts]
        │
        ▼
[Format Report Per Agent]
        │
        ▼
[Deliver: Slack / Email / Google Sheets]
```

---

## Phase 1 — Close API Setup & Authentication

### 1.1 Create Close API Key
- Go to **Close → Settings → API Keys**
- Generate a dedicated key for this integration (name it `n8n-transcript-analysis`)
- Store it as an n8n credential (HTTP Basic Auth — API key as username, leave password blank)

### 1.2 Configure Close HTTP Credentials in n8n
- **Auth Type:** HTTP Basic Auth
- **Username:** `{CLOSE_API_KEY}`
- **Password:** _(empty)_
- **Base URL:** `https://api.close.com/api/v1/`

---

## Phase 2 — Fetch Agents

### 2.1 n8n Node: HTTP Request — List Users

```
GET https://api.close.com/api/v1/user/
```

**Response fields needed:**
| Field | Purpose |
|---|---|
| `id` | User ID to filter calls |
| `first_name`, `last_name` | Agent name for reporting |
| `email` | Agent identifier |

### 2.2 n8n Node: Filter
- Exclude inactive users or non-sales roles (if applicable)
- Output: Array of active agent objects `[{ id, name, email }]`

---

## Phase 3 — Fetch Today's Call Transcripts Per Agent

### 3.1 n8n Node: Loop Over Agents

For each agent, make the following API call:

```
GET https://api.close.com/api/v1/activity/call/
```

**Query Parameters:**

| Parameter | Value | Purpose |
|---|---|---|
| `user_id` | `{agent.id}` | Filter calls by this agent |
| `date_created__gt` | `{today}T00:00:00+01:00` | Start of day (CET) |
| `date_created__lt` | `{today}T17:00:00+01:00` | Up to trigger time |
| `_fields` | `id,user_id,lead_id,direction,duration,disposition,recording_transcript,date_created,phone,contact_id` | Only fetch needed fields |
| `_limit` | `100` | Per page (paginate if needed) |

### 3.2 Handle Pagination
- Check `has_more` field in response
- If `true`, increment `_skip` by `_limit` and repeat
- Collect all results into a single array per agent

### 3.3 Filter Out Calls Without Transcripts
- Keep only calls where `recording_transcript` is not `null`
- A call without a transcript means recording was disabled or too short

**Important:** The `recording_transcript` field is NOT returned by default. You MUST include it in `_fields` or it will be omitted.

---

## Phase 4 — Enrich With Lead Data

### 4.1 n8n Node: HTTP Request — Fetch Lead Details

For each unique `lead_id` from the calls:

```
GET https://api.close.com/api/v1/lead/{lead_id}/
    ?_fields=id,display_name,status_label,contacts,custom
```

**Fields to extract:**
| Field | Purpose |
|---|---|
| `display_name` | Company/lead name |
| `status_label` | Current lead status (e.g., "Unqualified", "Trial", "Lost") |
| `contacts` | Contact names/titles for context |
| `custom.*` | Any custom fields relevant to qualification (industry, company size, etc.) |

### 4.2 Merge Lead Data Into Call Records
- Attach lead name, status, and custom fields to each call transcript
- This gives the AI context about the lead when analysing the conversation

---

## Phase 5 — AI Analysis With Claude

### 5.1 Claude API Credential in n8n
- **API Key:** Store as n8n credential
- **Model:** `claude-sonnet-4-6` (best balance of speed/cost/quality for batch analysis)
- **Endpoint:** `https://api.anthropic.com/v1/messages`
- **Headers:** `x-api-key: {key}`, `anthropic-version: 2023-06-01`

### 5.2 n8n Node: Batch Transcripts Per Agent

Group all transcript data per agent into a single payload to reduce API calls and give the model full context of the agent's day.

### 5.3 n8n Node: HTTP Request — Claude Analysis

**For each agent batch, send one prompt:**

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "<<PROMPT BELOW>>"
    }
  ]
}
```

### 5.4 Analysis Prompt Template

```
You are a sales call analyst. Below are today's call transcripts for agent
{{agent_name}}. Each transcript includes the lead name, lead status, and the
full conversation.

Analyse each call and identify:

1. **Qualification Outcome**: Was the lead qualified or not qualified?
2. **Disqualification Reasons**: If not qualified, categorise the reason using
   ONLY these categories:
   - BUDGET: Lead cannot afford or has no budget allocated
   - AUTHORITY: Spoke to wrong person / no decision-making power
   - NEED: No clear need or pain point for our product
   - TIMELINE: No urgency / not buying anytime soon
   - FIT: Product/service mismatch (wrong industry, size, use case)
   - COMPETITOR: Already using or committed to a competitor
   - NO_SHOW: Lead did not engage / very short call with no substance
   - OTHER: Does not fit above categories (explain briefly)
3. **Key Objections**: Quote the specific objection from the lead (1-2 sentences max)
4. **Agent Handling**: Brief assessment of how the agent handled the objection
   (effective / needs improvement / missed opportunity)
5. **Suggested Improvement**: One actionable suggestion for the agent

After analysing each call, provide:

## Agent Summary for {{agent_name}}
- Total calls today: X
- Qualified: X
- Not qualified: X
- Top 3 disqualification reasons (ranked by frequency)
- Overall pattern: [1-2 sentence summary of recurring issues]
- Priority coaching point: [single most impactful improvement]

---

TRANSCRIPTS:

{{#each calls}}
### Call {{@index + 1}}: {{lead_name}} (Status: {{lead_status}})
- Direction: {{direction}}
- Duration: {{duration}} seconds
- Disposition: {{disposition}}

**Transcript:**
{{#each recording_transcript.utterances}}
[{{speaker_side}}] {{speaker_label}}: {{text}}
{{/each}}

**Call Summary:** {{recording_transcript.summary_text}}

---
{{/each}}

Respond in valid JSON matching this structure:
{
  "agent": "string",
  "date": "string",
  "total_calls": number,
  "qualified_count": number,
  "not_qualified_count": number,
  "calls": [
    {
      "lead_name": "string",
      "qualified": boolean,
      "disqualification_reason": "BUDGET|AUTHORITY|NEED|TIMELINE|FIT|COMPETITOR|NO_SHOW|OTHER|null",
      "reason_detail": "string",
      "key_objection": "string",
      "agent_handling": "effective|needs_improvement|missed_opportunity",
      "suggestion": "string"
    }
  ],
  "top_disqualification_reasons": ["string"],
  "overall_pattern": "string",
  "priority_coaching_point": "string"
}
```

### 5.5 Why Claude Over ChatGPT for This Use Case
- Better at structured JSON output with complex prompts
- Stronger at nuanced conversation analysis
- `claude-sonnet-4-6` is fast and cost-effective for batch processing
- If cost is a concern, `claude-haiku-4-5` can handle this at ~10x lower cost with slightly less nuance
- ChatGPT (GPT-4o) is a viable alternative — the prompt is model-agnostic

---

## Phase 6 — Report Delivery

### Option A: Slack Report

**n8n Node: Slack — Send Message**

Format the JSON response into a readable Slack message per agent:

```
📊 Daily Call Analysis — {{agent_name}} — {{date}}

Calls: {{total_calls}} | ✅ Qualified: {{qualified_count}} | ❌ Not Qualified: {{not_qualified_count}}

Top Disqualification Reasons:
1. {{top_reasons[0]}}
2. {{top_reasons[1]}}
3. {{top_reasons[2]}}

🎯 Priority Coaching Point:
{{priority_coaching_point}}

Pattern: {{overall_pattern}}
```

### Option B: Google Sheets Log

Append a row per call per agent with columns:
`Date | Agent | Lead | Qualified | DQ Reason | Objection | Handling | Suggestion`

This creates a historical dataset for trend analysis over time.

### Option C: Email Digest

Single email with all agents' summaries to sales manager(s).

---

## Phase 7 — Error Handling & Edge Cases

### 7.1 Rate Limiting
- Close API: 60 req/min — add **1-second delay** between agent call fetches
- Claude API: Handle 429 responses with exponential backoff
- n8n has built-in retry on error — enable with 3 retries, 5s wait

### 7.2 No Calls Today
- If an agent has zero calls, skip analysis — include a note in the report: "No calls recorded today"

### 7.3 Empty Transcripts
- Some calls may have `recording_transcript: null` (recording disabled, very short calls)
- Filter these out before sending to Claude

### 7.4 Large Volume Handling
- If an agent has 50+ calls, split into batches of 15-20 calls per Claude request to stay within token limits
- Merge results after all batches complete

### 7.5 Token Budget
- Average transcript: ~500-1500 tokens
- 20 calls per batch: ~10,000-30,000 input tokens
- Claude Sonnet output: ~2,000-4,000 tokens per batch
- **Estimated cost per agent per day:** ~$0.03-0.10 (Sonnet) or ~$0.003-0.01 (Haiku)

---

## n8n Workflow Node Summary

| # | Node Type | Name | Purpose |
|---|---|---|---|
| 1 | Cron | `Daily 17:00 CET` | Trigger workflow |
| 2 | HTTP Request | `Get Agents` | `GET /user/` |
| 3 | Function | `Filter Active Agents` | Remove inactive/non-sales |
| 4 | Split In Batches | `Loop Agents` | Iterate per agent |
| 5 | HTTP Request | `Get Agent Calls` | `GET /activity/call/?user_id=...&_fields=recording_transcript,...` |
| 6 | IF | `Has More Pages?` | Pagination loop |
| 7 | Function | `Filter Calls With Transcripts` | Remove null transcripts |
| 8 | HTTP Request | `Get Lead Details` | `GET /lead/{id}/` for each unique lead |
| 9 | Function | `Merge Lead + Call Data` | Combine into analysis payload |
| 10 | HTTP Request | `Claude Analysis` | `POST /v1/messages` with prompt |
| 11 | Function | `Parse Claude Response` | Extract JSON from response |
| 12 | Function | `Format Report` | Build Slack/email/Sheets output |
| 13 | Slack/Email/Sheets | `Deliver Report` | Send to chosen destination(s) |
| 14 | NoOp | `Error Handler` | Catch and notify on failures |

---

## Configuration Variables (Set as n8n Environment Variables)

```
CLOSE_API_KEY=         # Close CRM API key
CLAUDE_API_KEY=        # Anthropic API key
TIMEZONE=Europe/Berlin # Or Europe/Amsterdam, Europe/Paris, etc.
TRIGGER_HOUR=17        # 5 PM
SLACK_CHANNEL=#sales-insights  # Delivery channel
REPORT_EMAIL=manager@company.com
GOOGLE_SHEET_ID=       # If using Sheets delivery
```

---

## Customisation Points

The automation expert should adjust these based on your needs:

1. **Disqualification categories** (Phase 5.4) — edit the list in the prompt to match your sales process
2. **Custom fields** (Phase 4.1) — add any Close custom fields relevant to qualification
3. **Delivery channel** (Phase 6) — pick Slack, email, Sheets, or all three
4. **Model choice** — start with `claude-sonnet-4-6`, switch to Haiku for cost savings or Opus for deeper analysis
5. **Trigger time** — adjust cron to match your team's end-of-day

---

## Estimated Build Time

| Phase | Effort |
|---|---|
| Phase 1: API Setup | 30 min |
| Phase 2: Fetch Agents | 30 min |
| Phase 3: Fetch Calls + Pagination | 1-2 hours |
| Phase 4: Lead Enrichment | 1 hour |
| Phase 5: Claude Prompt + Integration | 1-2 hours |
| Phase 6: Report Delivery | 1 hour |
| Phase 7: Error Handling + Testing | 1-2 hours |
| **Total** | **5-8 hours** |

---

## Testing Checklist

- [ ] API key authenticates successfully against Close
- [ ] User list returns correct agents
- [ ] Calls endpoint returns data with `recording_transcript` populated
- [ ] Pagination works when agent has >100 calls
- [ ] Calls without transcripts are filtered out
- [ ] Lead enrichment returns status and custom fields
- [ ] Claude prompt returns valid JSON
- [ ] JSON parsing handles edge cases (no calls, all qualified, etc.)
- [ ] Slack/email/Sheets output is formatted correctly
- [ ] Cron triggers at correct CET/CEST time (check DST handling)
- [ ] Rate limiting doesn't cause failures with multiple agents
- [ ] Full end-to-end run completes within reasonable time (<10 min)
