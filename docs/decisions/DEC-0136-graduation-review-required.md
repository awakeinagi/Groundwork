---
id: DEC-0136
type: decision
title: An explicit element-graduation review is a required step before any component doc gates
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Before any Component Doc is set gated, the facilitator must run explicit
  graduation review: every design element checked against DEC-0080 criteria
  (consumed by more than one CMP or needing independently versioned
  conformance), outcome recorded in gating session. The review is named step
  in SPEC-component and facilitation skill's component playbook; the graph
  tool's element-inventory command provides mechanical aid. Rule-type
  decisions fail silently when merely cited; operationalizing them as
  checklists at the stage they govern is the fix.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0023 @ T3-T4"
links:
  derives-from: [SES-0023]
  relates-to: [DEC-0080, DEC-0134, DEC-0135, DEC-0371]
---

# DEC-0136: Required Graduation Review at Component Gates

## Context

CMP-0001 reached
its gate with two elements that already satisfied
DEC-0080's graduation
criteria; the rule was cited in the draft but never applied
element-by-element. The participant caught it at the gate and directed
that the review become mandatory — for the system being designed and
for the facilitation skill
(SES-0023 T3).

## Decision

Before any Component Doc is set `gated`, the facilitator must run an
**explicit graduation review**: every design element is checked against
the DEC-0080 criteria
(consumed by more than one CMP — actual or contract-certain — or
needing independently versioned conformance), and the outcome is
recorded in the gating session. The review is a named step in
[SPEC-component](../specs/SPEC-component.md)'s rules and in the
facilitation skill's component playbook; the graph tool's
element-inventory command is the mechanical aid for spotting
candidates.

## Rationale

Rule-type decisions fail silently when they are merely *cited*: the
fix is operationalizing them as checklists at the stage they govern.
Retrieval (semantic search) surfaces decisions an author does not know
about; it does not fix failure-to-apply a decision already in hand —
only a required step does.

## Alternatives Considered

- **Rely on semantic search surfacing the decision** — it was already
  cited and in context; surfacing was not the failure mode.
- **A mechanical tier-2 check** — "consumed by more than one CMP" is
  partially detectable, but contract-certain future consumption is
  human judgment; a checker rule would false-negative exactly the
  interesting cases.

## Implications

[SPEC-component](../specs/SPEC-component.md) gains the rule; the
design-session skill's playbook gains the step (synced to the vendored
and installed copies). First execution:
DEC-0134/DEC-0135.
