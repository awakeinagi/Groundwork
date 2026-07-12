---
id: DEC-0222
type: decision
title: Background Job Execution Runtime owns handler registration; producers register directly
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Background Job Execution Runtime exposes register(job-type, handler) as
  part of its own contract. Each component needing background work calls it
  directly at initialization (e.g., KV-store adapter registers its expiry-sweep
  handler), rather than the Composition Root maintaining a central registry.
  This keeps job registration co-located with the component owning its business
  logic, uncoupling composition from job internals.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0042 @ T1-T2"
links:
  derives-from: [SES-0042]
  relates-to: [DEC-0208, DEC-0214]
  supersedes: []
---

# DEC-0222: Runtime Owns Handler Registration

## Context

CMP-0013
needed a wiring answer for how a `job-type` (open string namespace per
DEC-0214) gets a handler
attached: a registration API this CMP owns and any producer calls
directly, or centralized registration performed by the Composition
Root during process startup.
CMP-0014's Notes
forward-declared this as an open point (the periodic expiry-sweep job
needs to register somewhere).

## Decision

The runtime exposes `register(job-type, handler)` as part of its own
contract. Each component that needs background work calls it directly
at its own initialization — e.g. the KV-store Port's default Adapter
registers its expiry-sweep handler — rather than the Composition Root
maintaining a central registry of every job type in the system.

## Rationale

Keeps a job's registration co-located with the component that owns its
business logic, the same locality principle the port/runtime split
(DEC-0208) already follows: the
runtime provides generic dispatch machinery, not domain knowledge of
what jobs exist. A centralized Composition Root registry would force it
to import every future job-owning module just to wire handlers,
coupling the composition layer to job internals it has no other reason
to know about.

## Alternatives Considered

T1 posed the registration question as `register(job-type, handler)` owned by the runtime and called directly by each producer versus centralized registration performed by the Composition Root at process startup; the centralized alternative was weighed and rejected because it would force the Composition Root to import every future job-owning module just to wire handlers. The stakeholder confirmed the CMP-owned registration recommendation as given (T2). (skeleton restored at SES-0078)

## Implications

Each component that needs background work — e.g. the KV-store Port's default Adapter registering its expiry-sweep handler — must call `register()` directly at its own initialization rather than being wired centrally. This closes the open point CMP-0014's Notes had forward-declared, and keeps job registration co-located with the component owning the business logic rather than coupling the composition layer to job internals it has no other reason to know about. (skeleton restored at SES-0078)
