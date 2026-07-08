---
id: DEC-0134
type: decision
title: ChangeEvent graduates from CMP-0001 to a standalone event-type component
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0023 @ T2-T3"
links:
  derives-from: [SES-0023]
  relates-to: [DEC-0080, DEC-0128, DEC-0126]
---

# DEC-0134: ChangeEvent Graduation

## Context

[DEC-0080](DEC-0080-hybrid-component-granularity.md)'s graduation rule:
an element consumed by more than one CMP earns its own standalone
component. [ST-0008](../stories/ST-0008-change-event-stream.md) already
names three future consumer components (Graph Index, governance
staleness sweeps, consolidation invalidation); nested in
[CMP-0001](../components/CMP-0001-artifact-store-service.md), the event
schema would force every consumer to depend on the whole store doc and
inherit its staleness.

## Decision

The `ChangeEvent` element graduates to
[CMP-0002](../components/CMP-0002-change-event.md), a standalone CMP
with `component-type: event`, owned by the Canonical Store context and
derived from [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md).
It carries the payload schema and the emission/ordering/delivery/replay
semantics ([DEC-0128](DEC-0128-change-event-closed-schema.md) unchanged).
[CMP-0001](../components/CMP-0001-artifact-store-service.md) depends on
it as the emitter; consumer components depend on it alone.

## Rationale

Consumption by multiple components is contract-certain today
(decision-cited in the approved story), not speculative; graduating at
the gate avoids amputating an element from an approved doc later.

## Alternatives Considered

- **Wait for the second consumer CMP to exist** — technically when the
  rule triggers; guarantees staleness churn on approved
  [CMP-0001](../components/CMP-0001-artifact-store-service.md) that
  this gate absorbs for free.
