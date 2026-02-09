# Deliverables Template

Template for `.planning/REQUIREMENTS.md` — checkable deliverables that define "done" for a client engagement.

<template>

```markdown
# Deliverables: [Client / Company Name]

**Defined:** [date]
**Core Value:** [from PROJECT.md]

## v1 Deliverables

Deliverables for initial engagement. Each maps to roadmap phases.

### Lead Intake

- [ ] **LEAD-01**: Lead capture mechanism defined (form, landing page, DM flow, etc.)
- [ ] **LEAD-02**: Lead qualification criteria documented (who's a fit, who's not)
- [ ] **LEAD-03**: Lead routing logic mapped (where do leads go after capture)
- [ ] **LEAD-04**: Lead tracking system configured (CRM, spreadsheet, etc.)

### Marketing Sequences

- [ ] **MKTG-01**: Welcome/nurture email sequence mapped (triggers, timing, content briefs)
- [ ] **MKTG-02**: Segmentation logic defined (who gets what, based on what signals)
- [ ] **MKTG-03**: Re-engagement sequence for cold leads designed
- [ ] **MKTG-04**: Marketing-to-sales handoff criteria defined

### Sales Process

- [ ] **SALE-01**: Sales conversation framework documented (discovery → pitch → close)
- [ ] **SALE-02**: Objection handling playbook created
- [ ] **SALE-03**: Proposal/pricing structure templated
- [ ] **SALE-04**: Follow-up cadence defined (timing, channels, escalation)
- [ ] **SALE-05**: CRM pipeline stages mapped to actual sales steps

### Delivery Process

- [ ] **DLVR-01**: Client onboarding flow documented (welcome → kickoff → first milestone)
- [ ] **DLVR-02**: Delivery lanes mapped (who does what, when, in what order)
- [ ] **DLVR-03**: Milestone/checkpoint structure defined
- [ ] **DLVR-04**: Client communication cadence set (updates, reviews, approvals)
- [ ] **DLVR-05**: Handoff points between team members documented

### Content Strategy

- [ ] **CONT-01**: Content pillars defined (themes, topics, angles)
- [ ] **CONT-02**: Content calendar framework created (frequency, channels, formats)
- [ ] **CONT-03**: Content-to-funnel mapping documented (which content feeds which stage)
- [ ] **CONT-04**: Repurposing workflow designed (one piece → multiple formats)

### [Category]

- [ ] **[CAT]-01**: [Deliverable description]
- [ ] **[CAT]-02**: [Deliverable description]

## v2 Deliverables

Deferred to future engagement or follow-up. Tracked but not in current roadmap.

### [Category]

- **[CAT]-01**: [Deliverable description]
- **[CAT]-02**: [Deliverable description]

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Deliverable | Reason |
|-------------|--------|
| [Deliverable] | [Why excluded] |
| [Deliverable] | [Why excluded] |

## Traceability

Which phases cover which deliverables. Updated during roadmap creation.

| Deliverable | Phase | Status |
|-------------|-------|--------|
| LEAD-01 | Phase 1 | Pending |
| LEAD-02 | Phase 1 | Pending |
| MKTG-01 | Phase 2 | Pending |
| SALE-01 | Phase 3 | Pending |
| DLVR-01 | Phase 4 | Pending |
| CONT-01 | Phase 5 | Pending |
| [ID] | Phase [N] | Pending |

**Coverage:**
- v1 deliverables: [X] total
- Mapped to phases: [Y]
- Unmapped: [Z]

---
*Deliverables defined: [date]*
*Last updated: [date] after [trigger]*
```

</template>

<guidelines>

**Deliverable Format:**
- ID: `[CATEGORY]-[NUMBER]` (LEAD-01, MKTG-02, SALE-03, DLVR-04, CONT-05)
- Description: Outcome-focused, verifiable, atomic
- Checkbox: Only for v1 deliverables (v2 are not yet actionable)

**Categories:**
- Adapt to the client's actual business system
- Common: Lead Intake, Marketing Sequences, Sales Process, Delivery Process, Content Strategy, Retention, Referrals, Operations, Team SOPs, Analytics/Reporting
- Not every client needs every category — use what fits

**v1 vs v2:**
- v1: Committed scope, will be in roadmap phases
- v2: Acknowledged but deferred, not in current roadmap
- Moving v2 to v1 requires roadmap update

**Out of Scope:**
- Explicit exclusions with reasoning
- Prevents "why didn't you include X?" later
- Common exclusions: implementation (vs. framework design), hiring, tool migration, ad management

**Traceability:**
- Empty initially, populated during roadmap creation
- Each deliverable maps to exactly one phase
- Unmapped deliverables = roadmap gap

**Status Values:**
- Pending: Not started
- In Progress: Phase is active
- Complete: Deliverable verified with client
- Blocked: Waiting on client input or external factor

</guidelines>

<evolution>

**After each phase completes:**
1. Mark covered deliverables as Complete
2. Update traceability status
3. Note any deliverables that changed scope

**After roadmap updates:**
1. Verify all v1 deliverables still mapped
2. Add new deliverables if scope expanded
3. Move deliverables to v2/out of scope if descoped

**Deliverable completion criteria:**
- Deliverable is "Complete" when:
  - Framework/model/document is created
  - Client has reviewed and approved
  - Handoff documentation exists (client can use it without you)

</evolution>

<example>

```markdown
# Deliverables: GrowthCo Consulting

**Defined:** 2026-02-09
**Core Value:** A repeatable system that turns LinkedIn content into booked discovery calls without founder dependency

## v1 Deliverables

### Lead Intake

- [ ] **LEAD-01**: LinkedIn lead magnet funnel mapped (post → DM → lead capture)
- [ ] **LEAD-02**: Lead qualification scorecard (fit, budget, urgency)
- [ ] **LEAD-03**: CRM setup guide with custom fields and automation triggers

### Marketing Sequences

- [ ] **MKTG-01**: 7-email welcome sequence (content briefs + timing)
- [ ] **MKTG-02**: Segment-based nurture tracks (3 segments based on pain point)
- [ ] **MKTG-03**: Re-engagement sequence for 30-day inactive leads

### Sales Process

- [ ] **SALE-01**: Discovery call script with qualification framework
- [ ] **SALE-02**: Proposal template with 3 pricing tiers
- [ ] **SALE-03**: Follow-up sequence (post-call → decision → close)

### Delivery Process

- [ ] **DLVR-01**: Client onboarding checklist (day 1 → day 7)
- [ ] **DLVR-02**: 3-lane delivery board (Strategy, Execution, Review)
- [ ] **DLVR-03**: Weekly client update template
- [ ] **DLVR-04**: Project completion and handoff SOP

### Content Strategy

- [ ] **CONT-01**: 4 content pillars with 10 topic angles each
- [ ] **CONT-02**: Weekly content calendar (LinkedIn + email)
- [ ] **CONT-03**: Content-to-funnel map (awareness → consideration → decision)

## v2 Deliverables

### Retention

- **RETN-01**: Client satisfaction survey and NPS tracking
- **RETN-02**: Upsell/cross-sell trigger framework

### Referrals

- **REFR-01**: Referral program structure
- **REFR-02**: Case study creation SOP

## Out of Scope

| Deliverable | Reason |
|-------------|--------|
| Running paid ads | Client wants organic-first, ads in phase 2 engagement |
| Hiring/team building | Not in scope — focus on systems, not staffing |
| Tool migration | Client staying on current CRM for now |
| Copywriting | Frameworks and briefs, not finished copy |

## Traceability

| Deliverable | Phase | Status |
|-------------|-------|--------|
| LEAD-01 | Phase 1 | Pending |
| LEAD-02 | Phase 1 | Pending |
| LEAD-03 | Phase 1 | Pending |
| MKTG-01 | Phase 2 | Pending |
| MKTG-02 | Phase 2 | Pending |
| MKTG-03 | Phase 2 | Pending |
| SALE-01 | Phase 3 | Pending |
| SALE-02 | Phase 3 | Pending |
| SALE-03 | Phase 3 | Pending |
| DLVR-01 | Phase 4 | Pending |
| DLVR-02 | Phase 4 | Pending |
| DLVR-03 | Phase 4 | Pending |
| DLVR-04 | Phase 4 | Pending |
| CONT-01 | Phase 5 | Pending |
| CONT-02 | Phase 5 | Pending |
| CONT-03 | Phase 5 | Pending |

**Coverage:**
- v1 deliverables: 16 total
- Mapped to phases: 16
- Unmapped: 0

---
*Deliverables defined: 2026-02-09*
*Last updated: 2026-02-09 after initial definition*
```

</example>
