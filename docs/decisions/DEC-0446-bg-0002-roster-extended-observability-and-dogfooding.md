---
id: DEC-0446
type: decision
title: "BG-0002 roster extended: Observability and Dogfooding"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0085 T24, T27"
overview: >-
  DEC-0443's anticipated derived-work roster gains two topics,
  bringing it to fifteen: Observability — visibility into the
  Engine's operation and the corpus's health (audit trails, agent-
  interaction telemetry, gate/checker metrics, session analytics);
  and Dogfooding — the Groundwork project's own use of the paradigm
  to develop the Engine, distinct from Adoption (people using
  Groundwork on their own projects) and from Self-governance
  (compliance outcomes). Whether Dogfooding stays standalone or
  merges with Self-governance is assessed at epic derivation via the
  coupling check. Both are anticipation, not derivation: each epic
  derives only through its own refinement session, per DEC-0443's
  original mechanism.
links:
  derives-from: [SES-0085]
  relates-to: [DEC-0443, BG-0002]
---

# DEC-0446: BG-0002 roster extended: Observability and Dogfooding

## Context

At T24 the stakeholder asked to add an Epic for observability under BG-0002 if not already captured; the facilitator confirmed at T25 that observability was not on DEC-0443's thirteen-topic roster. At the T27 gate ratification the stakeholder approved the observability wording as proposed and also asked to add Dogfooding as a topic, describing it as a core feature of the Engine refinement process — by people working on the Groundwork project itself, not people using Groundwork on their own projects.

## Decision

DEC-0443's anticipated derived-work roster gains two topics, bringing it to fifteen. Observability — visibility into the Engine's operation and the corpus's health: audit trails, agent-interaction telemetry, gate/checker metrics, session analytics. Dogfooding — the Groundwork project's own use of the paradigm to develop the Engine: contributors refine Groundwork by working through Groundwork itself, and what that practice surfaces feeds Engine refinement; this is by people working on the Groundwork project itself, not people using Groundwork on their own projects (Adoption's domain), and is distinct from Self-governance's compliance outcomes.

## Rationale

Dogfooding is deliberately kept distinct from two neighboring roster topics rather than folded into either: Adoption concerns people applying Groundwork to their own projects, while Dogfooding concerns the Groundwork project's own contributors using the paradigm on itself; Self-governance concerns compliance outcomes, while Dogfooding concerns the development practice that surfaces Engine refinements. Whether Dogfooding stays standalone or merges with Self-governance is assessed at epic derivation via the coupling check, the same mechanism DEC-0443 relies on for every roster item. Like the rest of the roster, both new topics are anticipation, not derivation: each epic derives only through its own refinement session.

## Alternatives Considered

Folding Dogfooding into Self-governance at this stage was considered, since both concern the project's internal practice, but was deferred to the epic-derivation coupling check rather than decided here — consistent with how DEC-0443 treated its own close-topic folds (corpus-format versioning, team governance configuration) as assessments for the roster's original round, not as prejudged mergers.

## Implications

Both Observability and Dogfooding derive only through their own refinement sessions, exactly as the other thirteen roster topics do; the roster addition itself creates no epic and re-scopes no existing one, including EP-0009.
