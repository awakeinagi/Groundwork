# Groundwork Artifact Templates

Copy-paste starting points. Replace bracketed placeholders; keep required
sections even when brief ("None identified" / "N/A — <reason>" is valid
and auditable; silence is not). Dates absolute. IDs: scan `docs/` for the
prefix's current max before allocating. Body cross-references must be
markdown links `[<ID>](relative/path.md)` — bare IDs in prose fail the
checker; frontmatter values stay bare IDs.

## Contents

[Business Goal](#business-goal-bg) · [Epic](#epic-ep) · [Story](#story-st) ·
[Spike](#spike-sp) · [Component Doc](#component-doc-cmp) ·
[Session](#session-ses) · [Decision](#decision-dec) · [Conflict](#conflict-cfl) ·
[Change Proposal](#change-proposal-cp) · [Consolidation](#consolidation-con) ·
[CONTEXT.md seed](#contextmd-seed) · [README seed](#readme-seed)

## Business Goal (BG)

```markdown
---
id: BG-0001
type: business-goal
title: [Intent in one line]
status: draft
owner: [approver person/role]
sponsor: [named stakeholder who owns the intent]
created: [YYYY-MM-DD]
links:
  derives-from: [SES-0001]
cites: [DEC-0001, DEC-0002]
---

# BG-0001: [Title]

## Problem
[The pain/opportunity in the sponsor's terms — no solution language.]

## Intent
[What the business wants to be true afterward, and why now.]

## Outcomes & Success Criteria
1. [Observable, ideally measurable result] (per [DEC-0001](../decisions/DEC-0001-....md))
2. ...

## Scope
**Releases:** [omit unless the work is release-scoped; labels are SemVer
prefixes; mark the current release]
- `1` (current) — [what this release delivers]
- `2` — [follow-on scope]

**In:** ...
**Out:** ...

## Constraints
- [Regulatory / technical / budget / timeline / organizational]

## Stakeholders & Roles
- **Sponsor:** ...
- **Approvers:** ...

## Conflicts & Tensions
None identified. [or link CFL artifacts]

## Derived Work
- [EP links, maintained as they are created]
```

## Epic (EP)

```markdown
---
id: EP-0001
type: epic
title: [Coherent body of work]
status: draft
owner: [approver role]
created: [YYYY-MM-DD]
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  impacts: []
  impacted-by: []
cites: [DEC-....]
---

# EP-0001: [Title]

## Summary
[What this epic delivers and for whom.]

## Why (Goal Alignment)
[How it advances each linked goal — the argument the gate reviewer checks.]

## Scope
**In:** ...
**Out:** ...

## Domain Context
Bounded context: **[name]**. Terms: [glossary terms used/introduced].

## Interfaces & Contracts to Define
- [API/data/behavior contracts the stories and components will pin down]

## Risks & Open Questions
- [Including candidate spikes]

## Derived Work
None yet — stories/spikes follow gate approval of this epic.
```

## Story (ST)

```markdown
---
id: ST-0001
type: story
title: [Implementable unit]
status: draft            # deferred if out of the current release
# release: "2"           # only when deferred: declared release or backlog
owner: [approver role]
created: [YYYY-MM-DD]
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: []
  impacts: []
  impacted-by: []
cites: [DEC-....]
---

# ST-0001: [Title]

## Summary
[The change, its beneficiary, the value.]

## Acceptance Criteria
1. [Individually testable] (per [DEC-....](../decisions/DEC-....md))
2. ... (per [DEC-....](../decisions/DEC-....md))

## Component Impact
[CMP docs this story builds or modifies (markdown-linked); contract
sections affected. Elements in those CMPs back-reference this story via
`Implements:` lines and may only reference stories whose Component
Impact links their CMP.]

## Out of Scope
[Adjacent work explicitly excluded.]

## Notes for Implementers
[Optional. Context, never a substitute for contracts.]
```

## Spike (SP)

```markdown
---
id: SP-0001
type: spike
title: [Research question]
# status: deferred + release: backlog — for questions that matter later;
# arm a trigger in docs/TRIGGERS.md with the revival condition
status: draft
owner: [role]
created: [YYYY-MM-DD]
timebox: [e.g. 3d]
links:
  derives-from: [EP-0001]   # or [BG-0001] for cross-cutting spikes
  satisfies: [BG-0001]
  relates-to: []            # sibling work whose assumptions are at stake
cites: []
---

# SP-0001: [Title]

## Question
[Phrased so an answer is recognizable.]

## Why It Blocks
[Which assumptions in which artifacts hinge on the answer.]

## Method
1. ...

## Findings
Pending — filled at completion.

## Resulting Decisions
Pending — completion requires ≥1 DEC deriving from this spike.
```

## Component Doc (CMP)

```markdown
---
id: CMP-0001
type: component
title: [Component name]
status: draft
owner: [approver role]
created: [YYYY-MM-DD]
context: [bounded context]
# component-type: protocol  # ONLY on standalone element CMPs (graduated
#                           # seams): entity|value|service|event|protocol
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: []            # other CMPs, contracts-only
cites: [DEC-....]
---

# CMP-0001: [Title]

## Purpose
[What it's for, tied to the goals it satisfies.]

## Ubiquitous Language
[Glossary terms this component's model uses.]

## Design Elements

### [ElementName] (service)

Implements: [ST-....](../stories/ST-....md)   ← mandatory, ≥1 story whose
implementation this element handles; the story's Component Impact must
link this CMP back

[One-line responsibility. Contract kinds per type: entity ⇒ B+D (A only
if boundary-exposed); value ⇒ D; service ⇒ A+B; event ⇒ D+B (delivery
semantics); protocol ⇒ A+B (conformance).]
- [ElementName].B-1: [behavioral guarantee] (per [DEC-....](../decisions/DEC-....md))
- [ElementName].A-1: [operation: signature, request/response schemas —
  inline or referencing a declared value/event element — errors,
  idempotency/ordering] (per [DEC-....](../decisions/DEC-....md))

### [ElementName] (value)

Implements: [ST-....](../stories/ST-....md)

- [ElementName].D-1: [schema, equality/immutability invariants] (per [DEC-....](../decisions/DEC-....md))

## Component Invariants
- C-1: [cross-element guarantee] (per [DEC-....](../decisions/DEC-....md))

## Implementation Guidance

### Constraints
- IG-1: [normative for the reference implementation, e.g. a spike-chosen
  store] (per [DEC-....](../decisions/DEC-....md))

### Notes
- [Advisory, may be stack-specific; never load-bearing — contracts must
  stand without these.]

## Dependencies
- [CMP-....]: consumes [contract sections/items], internals out of bounds.

## Acceptance & Test Expectations
[What a passing implementation must demonstrate. For protocol-type
standalone CMPs: the conformance suite any implementation must pass.]

## Out of Scope
[Especially plausible adjacent behavior an implementer might assume.]
```

## Session (SES)

```markdown
---
id: SES-0001
type: session
title: [What was refined]
status: closed
owner: [participant]
created: [YYYY-MM-DD]
participant: [named person]
participant-role: stakeholder   # | product-owner | eng-lead | ds-lead | arbiter
facilitator: [agent + model]
transcript-fidelity: reconstructed   # | verbatim
links:
  relates-to: [BG-0001]
---

# SES-0001: [Title]

## Purpose
[What the session set out to refine; what was already settled.]

## Transcript
**T1 — [Participant].** [Faithful account of what they said.]
**T2 — Facilitator.** [Questions asked, with the recommendations given.]
**T3 — [Participant].** [Answers, including amendments verbatim in spirit.]
...

## Decisions Produced
[DEC-....](../decisions/DEC-....md), [DEC-....](../decisions/DEC-....md)

## Conflicts Raised
None.
```

## Decision (DEC)

```markdown
---
id: DEC-0001
type: decision
title: [One unambiguous decision, as a statement]
status: accepted        # proposed | accepted | superseded
owner: [decider]
created: [YYYY-MM-DD]
decided-by: [named person]
decided-on: [YYYY-MM-DD]
source-span: "SES-0001 @ T2-T3"
links:
  derives-from: [SES-0001]   # or [SP-....]
  supersedes: []
---

# DEC-0001: [Title]

## Context
[The question that had to be answered, and why it arose.]

## Decision
[One unambiguous statement.]

## Rationale
[Why this option, in the decider's terms.]

## Alternatives Considered
- **[Option]**: [why rejected].

## Implications
[Known consequences for other artifacts.]
```

## Conflict (CFL)

```markdown
---
id: CFL-0001
type: conflict
title: [The tension in one line]
status: open            # open | mediating | escalated | resolved
owner: [arbiter, once escalated]
created: [YYYY-MM-DD]
links:
  relates-to: [BG-0001, BG-0002]   # ALL artifacts in tension
---

# CFL-0001: [Title]

## The Tension
[What contradicts what, stated neutrally.]

## Party Intents
- **[Party A]:** [underlying intent, not just position]
- **[Party B]:** ...

## Mediation Record
[Compromises proposed; each party's response.]

## Resolution
Pending. [At close: outcome, citing the resolving DEC(s) and ratifier.]
```

## Change Proposal (CP)

```markdown
---
id: CP-0001
type: change-proposal
title: [Proposed change in one line]
status: draft
owner: [triager]
created: [YYYY-MM-DD]
source: ui-suggestion      # | jira-drift | implementation-feedback
proposed-by: [person]
triage: pending            # pending | mechanical | session | rejected
links:
  relates-to: [EP-0001]
---

# CP-0001: [Title]

## Proposed Change
[The captured diff/suggestion, verbatim.]

## Context
[Where and how it arose.]

## Triage Outcome
Pending.
```

## Consolidation (CON)

```markdown
---
id: CON-0001
type: consolidation
title: [Neighborhood summarized]
status: fresh              # fresh | stale
owner: [maintainer]
created: [YYYY-MM-DD]
sources:
  - id: BG-0001
    ref: [git sha]
  - id: EP-0001
    ref: [git sha]
audience: session-agent    # | implementation-swarm | human-reviewer
---

# CON-0001: [Title]

## Path Covered
[Which graph traversal this replaces, for whom.]

## Consolidated Content
[Faithful summary; no new claims; load-bearing statements cite artifacts.]

## Omissions
[What was deliberately left out.]
```

## CONTEXT.md seed

```markdown
# [Project] Glossary

The ubiquitous language of this project. Terms are canonical: docs, code,
and conversation must use these words with exactly these meanings. Resolve
new or drifting terms here the moment they crystallize during refinement.
Definitions only — no implementation details.

## Domain terms

- **[Term]** — [precise definition].

## Process terms (Groundwork)

- **Artifact** — any identified document in `docs/`: Business Goal, Epic,
  Story, Spike, Component Doc, Session, Decision, Conflict, Change
  Proposal, Consolidation.
- **Gate** — a human approval checkpoint an artifact passes before the
  next stage may derive from it.
- **Decision (DEC)** — a distilled, attributable decision citing the
  session turns that support it; the unit of provenance.
- **Contract-Complete** — the bar for Component Docs: implementable and
  testable from the doc plus its dependencies' contracts alone.
- **Stale** — approved, but an upstream basis changed; blocks new
  derivation until re-affirmed.
- **Impact Link** — "X impacts Y": refining X shapes decisions in Y;
  reciprocal, same-type; drives refinement order.
```

## README seed

```markdown
# [Project] — Design Documentation

Groundwork-managed design docs: ideas are refined through gated sessions
into Business Goals → Epics → Stories/Spikes → contract-complete Component
Docs. See `AGENTS.md` for how to work in this repo and `CONTEXT.md` for
the project glossary.

Validate the artifact graph:

    python3 tools/check_links.py
```

## Trigger registry (docs/TRIGGERS.md)

```markdown
# Trigger Registry

Watched conditions with subscribed deferred items. Entries:
`## TRG-nnnn (armed|fired|retired)`; one decision-cited subscriber line
per item; a firing cites a decision and revives ALL subscribers; revival
unsubscribes the item from other armed triggers (emptied triggers
retire). Tooling loads **armed** entries only.

## TRG-0001 (armed)
**Condition:** [observable, human-testable statement]
**Subscribers:**
- revive [SP-....](spikes/SP-....md) (per [DEC-....](decisions/DEC-....md))
**Cites:** [DEC-....](decisions/DEC-....md)   ← the arming decision
```
