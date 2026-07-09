---
id: DEC-0267
type: decision
title: Changes modifying approved artifacts fire the supersession and staleness machinery inside the intake session
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0267 constrains intake sessions handling modifications to
  approved artifacts to complete the cascade before close: superseding
  decisions are recorded, the staleness walk runs, affected descendants
  go stale, and re-affirmation is presented to the approver, all within
  the session. Net-new changes skip this and derive artifacts under
  existing gates. The corpus is never left mid-cascade at session close.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T18-T19"
links:
  derives-from: [SES-0050]
---

# DEC-0267: The cascade completes before the session closes

## Context

Intake handles both net-new work and modifications to approved
artifacts. For modifications, when do supersession, the staleness
walk, and re-affirmation run?

## Decision

Inside the intake session: superseding DECs are recorded, the
staleness walk runs (graph `impact`), affected approved descendants go
`stale`, and re-affirmation is presented to the approver — all before
the session closes. The corpus is never left mid-cascade at close.
Net-new changes skip this; the session derives new artifacts under
existing gates. Intake adds an entry point, not new change semantics.

## Rationale

A "cascade later" queue is a queue of forgotten inconsistencies; the
existing staleness rules assume the walk happens with the change.
Where re-affirmation genuinely needs an absent approver (multi-party,
DEC-0265), the stale marks themselves are the durable record — the
session still closes with the cascade *marked*, never unwalked.

## Alternatives Considered

- **Session proposes, cascade as follow-up**: shorter sessions, corpus
  inconsistent between close and cascade, follow-ups forgotten.

## Implications

Expedited sessions (DEC-0254) include the cascade when they modify
approved artifacts. The intake playbook sequences it before the
closing summary.
