# Phase Context Template

Template for `.planning/phases/XX-name/{phase}-CONTEXT.md` — captures implementation decisions for a phase.

**Purpose:** Document decisions and preferences before designing the phase deliverables. This captures HOW things should be built within this phase's scope.

**Key principle:** Categories are NOT predefined. They emerge from what was actually discussed for THIS phase. A lead intake phase has different sections than a delivery lanes phase.

---

<template>

```markdown
# Phase [X]: [Name] - Context

**Gathered:** [date]
**Status:** Ready for design

<domain>
## Phase Boundary

[Clear statement of what this phase delivers — the scope anchor. This comes from ROADMAP.md and is fixed. Discussion clarifies implementation within this boundary.]

</domain>

<decisions>
## Implementation Decisions

### [Area 1 that was discussed]
- [Specific decision made]
- [Another decision if applicable]

### [Area 2 that was discussed]
- [Specific decision made]

### [Area 3 that was discussed]
- [Specific decision made]

### Open / Flexible
[Areas where client said "you decide" or "whatever you think is best" — you have creative freedom here]

</decisions>

<specifics>
## Specific References

[Any particular references, examples, or "I want it like X" moments from discussion. Competitor references, specific tools, existing materials to model after.]

[If none: "No specific requirements — open to best practices"]

</specifics>

<deferred>
## Deferred Ideas

[Ideas that came up during discussion but belong in other phases. Captured here so they're not lost, but explicitly out of scope for this phase.]

[If none: "None — discussion stayed within phase scope"]

</deferred>

---

*Phase: XX-name*
*Context gathered: [date]*
```

</template>

<good_examples>

**Example 1: Lead Intake Phase**

```markdown
# Phase 1: Lead Intake - Context

**Gathered:** 2026-02-09
**Status:** Ready for design

<domain>
## Phase Boundary

Map every way a lead enters the business, define qualification criteria, and design routing logic. Marketing sequences and nurture are Phase 2.

</domain>

<decisions>
## Implementation Decisions

### Lead sources
- Primary: LinkedIn (organic posts + DMs)
- Secondary: Website contact form, referrals
- Future (not now): Paid ads, podcast guest appearances
- Track source on every lead for attribution

### Qualification approach
- Simple scorecard, not complex automation
- 3 criteria: Budget fit, timeline, decision-maker
- Binary: qualified or nurture — no complex scoring tiers

### CRM setup
- Using HubSpot (free tier for now)
- Custom fields: source, score, segment, last touch
- Pipeline stages must match actual steps, not default HubSpot stages

### Intake form
- Keep it short — name, email, one qualifying question
- No phone number required (reduces friction)
- Auto-tag by source

### Open / Flexible
- Exact form tool (Typeform, native HubSpot, etc.)
- Automation sequences within CRM
- Dashboard layout

</decisions>

<specifics>
## Specific References

- "I like how Alex Hormozi talks about qualifying on ability to pay, not just interest"
- Client currently has leads in a spreadsheet — we need to migrate ~200 contacts
- They already have a LinkedIn following of 12k — warm audience exists

</specifics>

<deferred>
## Deferred Ideas

- Email nurture sequences — Phase 2
- Lead magnet creation — Phase 5 (Content Strategy)
- Referral program — v2 engagement

</deferred>

---

*Phase: 01-lead-intake*
*Context gathered: 2026-02-09*
```

**Example 2: Delivery Lanes Phase**

```markdown
# Phase 4: Delivery Lanes - Context

**Gathered:** 2026-02-09
**Status:** Ready for design

<domain>
## Phase Boundary

Map the client fulfillment process from signed contract to project completion. Includes onboarding, delivery workflow, communication, and handoffs. Retention and upsells are a future phase.

</domain>

<decisions>
## Implementation Decisions

### Delivery model
- 3 lanes: Strategy (founder), Execution (team), Review (founder + client)
- Strategy lane produces briefs → Execution lane produces deliverables → Review lane approves
- Weekly sprint rhythm, not waterfall

### Onboarding
- Day 0: Welcome email + intake questionnaire
- Day 1-2: Internal kickoff (team reviews intake, assigns work)
- Day 3: Client kickoff call (45 min)
- Day 7: First deliverable due

### Communication cadence
- Weekly async update (Loom video, 3-5 min)
- Bi-weekly live check-in (30 min)
- Slack channel for async questions (response within 24h)
- No email for project work — keep everything in one place

### Project management
- Using ClickUp (client already pays for it)
- Board view for delivery lanes
- Client gets view-only access to their board
- Internal tasks not visible to client

### Open / Flexible
- Exact ClickUp template structure
- Internal team assignment process
- QA checklist format

</decisions>

<specifics>
## Specific References

- "I don't want clients Slacking me at 10pm — need boundaries"
- Current pain: founder does everything, team waits for instructions
- Goal: team can run a sprint without founder being bottleneck

</specifics>

<deferred>
## Deferred Ideas

- Client satisfaction survey at project end — Phase 6
- Capacity planning for multiple concurrent clients — v2
- SOPs for common deliverable types — Phase 5 overlap

</deferred>

---

*Phase: 04-delivery-lanes*
*Context gathered: 2026-02-09*
```

</good_examples>

<guidelines>

**This template captures DECISIONS for the design process.**

The output should answer: "What are the constraints and preferences for designing this phase's deliverables?"

**Good content (concrete decisions):**
- "3 lanes: Strategy, Execution, Review"
- "Weekly async update via Loom, bi-weekly live call"
- "Simple scorecard, not complex automation"
- "Using HubSpot free tier — must work within its limits"

**Bad content (too vague):**
- "Should be a good experience"
- "Professional and clean"
- "Easy for the team to use"
- "Best practices"

**After creation:**
- File lives in phase directory: `.planning/phases/XX-name/{phase}-CONTEXT.md`
- Used as input when designing the actual frameworks and models
- Prevents going back to the client to re-ask things they already told you

</guidelines>
