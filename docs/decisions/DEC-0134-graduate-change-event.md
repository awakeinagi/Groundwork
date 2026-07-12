---
id: DEC-0134
type: decision
title: ChangeEvent graduates from CMP-0001 to a standalone event-type component
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  ChangeEvent element graduates to CMP-0002, a standalone CMP with
  component-type: event, owned by Canonical Store context and derived from
  EP-0001. It carries the payload schema and the emission/ordering/delivery/
  replay semantics. CMP-0001 depends on it as the emitter; consumer
  components depend on it alone. Consumption by multiple components is
  contract-certain today from approved story citations; graduating at gate
  avoids amputating an element from approved CMP-0001 later.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0023 @ T2-T3"
links:
  derives-from: [SES-0023]
  relates-to: [DEC-0080, DEC-0128, DEC-0126]
---

# DEC-0134: ChangeEvent Graduation

## Context

DEC-0080's graduation rule:
an element consumed by more than one CMP earns its own standalone
component. ST-0008 already
names three future consumer components (Graph Index, governance
staleness sweeps, consolidation invalidation); nested in
CMP-0001, the event
schema would force every consumer to depend on the whole store doc and
inherit its staleness.

## Decision

The `ChangeEvent` element graduates to
CMP-0002, a standalone CMP
with `component-type: event`, owned by the Canonical Store context and
derived from EP-0001.
It carries the payload schema and the emission/ordering/delivery/replay
semantics (DEC-0128 unchanged).
CMP-0001 depends on
it as the emitter; consumer components depend on it alone.

## Rationale

Consumption by multiple components is contract-certain today
(decision-cited in the approved story), not speculative; graduating at
the gate avoids amputating an element from an approved doc later.

## Alternatives Considered

- **Wait for the second consumer CMP to exist** — technically when the
  rule triggers; guarantees staleness churn on approved
  CMP-0001 that
  this gate absorbs for free.

## Implications

With ChangeEvent graduated to CMP-0002, CMP-0001 depends on it only as the emitter, and the future consumer components ST-0008 already names — Graph Index, governance staleness sweeps, consolidation invalidation — depend on CMP-0002 alone rather than on all of CMP-0001, avoiding inheriting the store document's staleness. Graduating at gate time, rather than waiting for the second consumer CMP to materialize, avoids having to amputate the element from an already-approved CMP-0001 later. This graduation review is now a required consideration when designing components in the future, for both the system and the skill. (skeleton restored at SES-0078)
