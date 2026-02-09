# Engagement State Template

Template for `.planning/STATE.md` — the engagement's living memory across sessions.

<template>

```markdown
# Engagement State

## Engagement Reference

See: .planning/PROJECT.md (updated [date])

**Core value:** [One-liner from PROJECT.md Core Value section]
**Current focus:** [Current phase name]

## Current Position

Phase: [X] of [Y] ([Phase name])
Status: [Discovery / Designing / In client review / Approved / Phase complete]
Last activity: [YYYY-MM-DD] — [What happened]

Progress: [░░░░░░░░░░] 0%

## Client Interactions

**Last client touchpoint:** [date] — [What happened: call, review, async feedback]
**Next scheduled:** [date] — [What's planned]
**Awaiting from client:** [Nothing / List of items needed]

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- [Phase X]: [Decision summary]
- [Phase Y]: [Decision summary]

### Client Feedback Themes

[Patterns from client interactions — what they keep coming back to]

- [Theme]: [Context]

### Parking Lot

[Ideas that came up but don't belong in current phase]

- [Idea] — [Which phase it belongs in]

### Blockers/Concerns

[Issues that affect future work]

None yet.

## Session Continuity

Last session: [YYYY-MM-DD]
Stopped at: [Description of last completed action]
Resume with: [What to pick up next]
```

</template>

<purpose>

STATE.md is the engagement's short-term memory spanning all phases and sessions.

**Problem it solves:** When you pick up a client project after a few days (or weeks), you waste time figuring out where you left off, what the client said last, and what's blocking progress.

**Solution:** A single, small file that's:
- Read first when resuming any work
- Updated after every significant action or client interaction
- Contains digest of accumulated context
- Enables instant session restoration

</purpose>

<lifecycle>

**Creation:** After ROADMAP.md is created
- Reference PROJECT.md
- Initialize empty accumulated context sections
- Set position to "Phase 1 Discovery"

**Reading:** First step when resuming work
- Know where you are
- Know what the client last said
- Know what's blocking

**Writing:** After every significant action
- After client calls/reviews: update Client Interactions
- After completing a phase element: update position
- After client feedback: log themes
- After scope discussions: note parking lot items

</lifecycle>

<size_constraint>

Keep STATE.md under 80 lines.

It's a DIGEST, not an archive. If accumulated context grows too large:
- Keep only 3-5 recent decisions (full log in PROJECT.md)
- Keep only active blockers, remove resolved ones
- Summarize client feedback themes, don't log every comment

The goal is "read once, know where we are" — if it takes more than 60 seconds to read, it's too long.

</size_constraint>
