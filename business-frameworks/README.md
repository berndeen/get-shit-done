# Business Frameworks — GSD Methodology Adapted

A structured framework for designing complete business systems: lead intake, marketing sequences, sales processes, delivery lanes, and content strategy.

Built on the [Get Shit Done](../README.md) methodology — same workflow, adapted for business framework design instead of software engineering.

## Who This Is For

Consultants and strategists who design end-to-end business systems for clients. If you map journeys from lead intake to marketing to sales to delivery to content — this is your operating system for that work.

## The Workflow

Same GSD cycle, different domain:

```
1. Discovery    → Deep questioning until you fully understand the client's business
2. Research     → Audit existing assets, analyze market, identify gaps
3. Define       → Lock in deliverables with clear success criteria
4. Roadmap      → Phase the engagement (intake → marketing → sales → delivery → content)
5. Per Phase:
   a. Discuss   → Capture client preferences and constraints for this phase
   b. Design    → Create the frameworks, models, and SOPs
   c. Review    → Client reviews and approves
   d. Verify    → Does this actually achieve the phase goal?
6. Integrate    → Connect all pieces into one coherent system
7. Handoff      → Client can run it without you
```

## Templates

| Template | What It Does | When to Use |
|----------|-------------|-------------|
| [PROJECT.md](templates/PROJECT.md) | Client brief — business, audience, goals, constraints | Start of every engagement |
| [REQUIREMENTS.md](templates/REQUIREMENTS.md) | Checkable deliverables per phase | After discovery, before roadmap |
| [ROADMAP.md](templates/ROADMAP.md) | Phased engagement plan with success criteria | After deliverables are defined |
| [STATE.md](templates/STATE.md) | Where you are, what's decided, what's blocking | Updated continuously |
| [CONTEXT.md](templates/CONTEXT.md) | Phase-specific preferences and decisions | Before designing each phase |
| [RESEARCH.md](templates/RESEARCH.md) | Market analysis, asset audit, gap analysis | During discovery |

## How to Start a New Client Engagement

1. **Create a folder** for the client: `clients/[client-name]/.planning/`
2. **Copy the templates** you need into `.planning/`
3. **Start with PROJECT.md** — fill it out during your discovery call
4. **Run RESEARCH.md** — audit what they have, what's working, what's broken
5. **Define REQUIREMENTS.md** — lock in what "done" looks like
6. **Build ROADMAP.md** — phase the work based on dependencies
7. **For each phase**, fill out CONTEXT.md before designing
8. **Keep STATE.md updated** — your future self will thank you

## Default Phase Structure

Most client engagements follow this sequence (adapt as needed):

```
Phase 1: Discovery & Lead Intake
    └── Where do leads come from? Where do they go?

Phase 2: Marketing Engine
    └── How do we nurture cold leads into warm prospects?
        └── depends on: knowing lead sources (Phase 1)

Phase 3: Sales Process
    └── How do we convert warm prospects into paying clients?
        └── depends on: marketing handoff point (Phase 2)

Phase 4: Delivery Lanes
    └── How does the client get what they paid for?
        └── depends on: knowing what's promised (Phase 3)

Phase 5: Content Strategy
    └── What content feeds the top of the funnel?
        └── depends on: knowing the audience and what converts (Phases 1-3)

Phase 6: Integration & Handoff
    └── Does it all connect? Can the client run it?
        └── depends on: everything above
```

## Adapting for Different Client Types

**Service businesses** (agencies, consultants): Heavy on delivery lanes, sales may be referral-based.

**Product businesses** (e-commerce, SaaS): Heavy on marketing engine, delivery may be simple.

**Creators / personal brands**: Heavy on content strategy, sales may be automated.

**B2B**: Heavy on sales process, longer cycles, content focused on authority.

Not every client needs all 6 phases. Some need 3. Some need 8. The templates adapt.

## Key Principles

1. **Audit before you design** — never throw away what's working
2. **Phase boundaries are real** — don't design everything at once
3. **Outcomes over tasks** — "team can qualify a lead in 2 minutes" beats "create a spreadsheet"
4. **Manual first, automate later** — build the process before buying the tool
5. **The client has to run it** — if they can't operate it without you, you haven't finished
