---
id: DEC-0498
type: decision
title: "Fold-back and the pinned template"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  The story that authors SPEC-research must update SPEC-artifact-
  common in the same change: the identity table gains the RSCH
  prefix with docs/research/ as its home, the link vocabulary gains
  the inspired-by and inspired reciprocal pair, and the deferred
  scope statement gains research, so the master specification never
  contradicts the newest type. The historical specification-versus-
  checker drift is out of scope here and queued as an idea. The
  Research template for the design-session skill's templates
  reference is pinned verbatim in this decision's body, and the
  implementing story pastes it unchanged.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0454, DEC-0456, DEC-0458, IDEA-0066]
---

# DEC-0498: Fold-back and the pinned template

## Context

SPEC-artifact-common is the master specification every type must
appear in — its identity table, link vocabulary, and deferred-scope
statement — and it has already drifted once (its enumerated integrity
rules stop at 11 while the checker implements through 26); the RSCH
type needed a concrete plan to land in the master spec without
repeating that drift, plus a single pinned, verbatim template so
every future implementer builds the identical shape.

## Decision

The story that authors SPEC-research must update SPEC-artifact-common
in the same change: the identity table gains the RSCH prefix with
docs/research/ as its home, the link vocabulary gains the inspired-by
and inspired reciprocal pair, and the deferred scope statement gains
research — so the master specification never contradicts the newest
type; the historical specification-versus-checker drift is out of
scope here and queued as an idea. The Research template for the
design-session skill's templates reference is pinned verbatim in this
decision's body, and the implementing story pastes it unchanged.

## Rationale

Same-change fold-back keeps SPEC-artifact-common born in sync with
RSCH specifically, closing the one new drift window entirely within
the control of the story that creates it; the pre-existing
rules-1-through-11 drift is a separate, larger, historical problem
better tracked and fixed on its own rather than blocking this story.
Pinning the template by decision now (rather than leaving it to the
implementing story's judgment) guarantees every consumer — the
implementing story, the design-session skill, and any agent
authoring a Research artifact by hand — builds the exact same shape.

## Alternatives Considered

Batching the RSCH fold-back into the general sync idea was considered
and rejected: it would leave a window, of unknown duration, where
SPEC-artifact-common denies RSCH exists at all. Leaving the template
to be derived ad hoc by the implementing story was considered and
rejected as inviting drift between the spec's prose description and
what actually gets built.

## Implications

The SPEC-research-authoring story's scope explicitly includes the
three named SPEC-artifact-common edits. The pinned template below is
normative; the implementing story pastes it unchanged rather than
re-deriving it.

```
---
id: RSCH-0001
type: research
title: <topic>
status: commissioned          # commissioned | in-progress | concluded | abandoned | deferred
owner: <person-id>
commissioned-by: <person-id>  # create-required
source-mode: seeded           # create-required: provided | seeded | agent-sourced
created: YYYY-MM-DD
overview: >
  <≤250-word self-sufficient summary>
links:
  derives-from: [SES-nnnn]    # create-required: the intake session
  inspired: []                # reciprocal of inspired-by on derived artifacts
  relates-to: []
cites: []                     # cites-sync checked (rule 16)
---

# RSCH-0001 — <topic>

## Inspiration
[What inspired this investigation — who asked, why now; from the intake session.]

## Research Goals
G1. [goal]
G2. [goal]

## Method
[Search strategy; source-admission quality bar; goals-met criteria.]
Stop conditions: [round cap / timebox / diminishing-returns criterion.]

## Source Register
| ID | Title | Reference | Type | Accessed |
|----|-------|-----------|------|----------|
| S1 | [title] | [URL/ISBN/…] | web | YYYY-MM-DD |

## Round 1 — YYYY-MM-DD
### Sources Added
[optional — register entries this round introduced]
### Findings
F1.1 [finding] [S1]
### Business-Goal Applicability
[BG-nnnn: how findings apply / "No applicability found."]
### Goals Assessment
[G1 met (F1.1); G2 unmet — continuing.]
### Open Questions
[optional]
### Next Round Plan
[required iff assessment says continuing: targeted goals, planned queries, source leads]

## Derived Work
None yet.

## Subtopic Files
[required iff docs/research/RSCH-0001/ exists]
- <slug>.md — [one-line description]
```
