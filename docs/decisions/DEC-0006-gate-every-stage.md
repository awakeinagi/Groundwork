---
id: DEC-0006
type: decision
title: Human approval gates at every pipeline stage
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
overview: >-
  Every artifact passes human approval gate before next stage may derive
  from it: Business Goals→Epics, Epics→Stories/Spikes, Stories→handoff.
  Named approver's sign-off in UI transitions artifact to approved status.
  Each layer of grounding chain is human-ratified — essential quality
  backstop given unsupervised sessions. Slower than continuous review, but
  worth it. Implies gate mechanics need roles/policies and status lifecycle
  includes gated status.
source-span: "SES-0001 @ T4-T5"
links:
  derives-from: [SES-0001]
---

# DEC-0006: Human approval gates at every pipeline stage

## Context

With agents generating artifacts and no facilitator in sessions, the process
needs defined points where humans ratify output before it propagates.

## Decision

Every artifact passes a human approval gate before the next stage may derive
from it: Business Goals before Epics, Epics before Stories/Spikes, Stories
and Component Docs before swarm handoff. A named Approver's sign-off in the
UI transitions the artifact to `approved`.

## Rationale

Each layer of the grounding chain is human-ratified — the essential quality
backstop given unsupervised sessions
(DEC-0003). Slower, and worth it.

## Alternatives Considered

- **Gate goals + final handoff only**: faster, trusts agent mid-layers.
- **Continuous review, no hard gates**: maximum velocity, weakest guarantees.

## Implications

Gate mechanics need roles and policies
(DEC-0020); status lifecycle
includes `gated` ([SPEC-artifact-common](../specs/SPEC-artifact-common.md)).
