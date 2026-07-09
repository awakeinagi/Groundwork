---
id: EP-0008
type: epic
title: Backend Application Platform
status: gated
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  The backend platform layer assembling Groundwork's domain engines and
  integration layer into one running v1 application and exposing it to
  the UI. Includes the Composition Root binding six Port contracts to
  concrete Adapters from deployment configuration, the inbound API
  surface using FastAPI/ASGI/SSE, and two new infrastructure ports —
  Queue and KV-store — extending the Port family. Identified as a
  missing piece during SES-0035 retrospective.
  Amended per SES-0056/DEC-0305: Inbound API exposes the manifest 
  trigger endpoint only; no manifest domain logic. Gated pending 
  re-approval.
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0006]
  impacted-by: [EP-0001, EP-0002, EP-0003, EP-0004, EP-0005, EP-0006, EP-0007]
cites: [DEC-0001, DEC-0018, DEC-0121, DEC-0122, DEC-0102, DEC-0124, DEC-0187,
        DEC-0190, DEC-0201, DEC-0202, DEC-0203, DEC-0204, DEC-0205, DEC-0305]
---

# EP-0008: Backend Application Platform

## Summary

The composition/runtime layer that assembles Groundwork's domain engines
(EP-0001..EP-0004,
EP-0007) and integration layer
(EP-0005) into one running v1
application, and exposes it to the UI channel
(EP-0006): the Composition Root (binding
Port contracts to concrete Adapters at startup, from deployment
configuration), the inbound API surface (FastAPI, ASGI, SSE per
DEC-0187),
and two new infrastructure ports — Queue and KV-store — extending the
Port family
(DEC-0121). Identified
as a gap in the original epic derivation
(SES-0035
retrospective); this epic closes it.

## Why (Goal Alignment)

BG-0001's Intent names "a standalone
application" with backend services as one of three deliverables
(DEC-0001) — this is
that deliverable's owning epic.
BG-0001's System Context (per
DEC-0190) already
states the v1 process/deployment shape (single-process, single-writer,
until `TRG-0001`/`TRG-0002` fire) and the trigger/output contract this
epic implements. Outcome 4 (parallel implementability) depends on
component docs being contract-complete — this epic's Composition Root
and API contracts are the stable seam the UI
(EP-0006) and the engine/connector
components build against, instead of each other's internals.

## Scope

**In:**
- **Manifest trigger endpoint** (DEC-0305): the Inbound API exposes
  the endpoint that triggers Handoff Manifest generation; generation,
  validation, and write are EP-0001's, topology EP-0004's — no manifest
  domain logic lives here (DEC-0201).
- **Composition Root**: binds the six Port contracts (app database,
  vector store, embedding, graph store, Queue, KV-store) to concrete
  Adapters at process startup, from deployment configuration
  (DEC-0201,
  DEC-0122). For the
  four pre-existing ports, it selects among the already-decided v1
  adapters: embedded LadybugDB (graph) and DuckDB (app database, vector
  search) (DEC-0102), and
  the local-model or REST-client embedding adapter
  (DEC-0124).
- **Inbound API**: a FastAPI/ASGI application serving the Web UI's
  HTTP + SSE needs
  (DEC-0202,
  DEC-0187), in Python per the reference-implementation stack
  (DEC-0018).
- **Queue Port**: contract plus v1 default adapter — durable,
  app-database-backed
  (DEC-0203,
  DEC-0204).
- **KV-store Port**: contract plus v1 default adapter — reuses the
  app-database Port
  (DEC-0203,
  DEC-0204).
- **Runtime/async execution model**: in-process asyncio background
  tasks running against the Queue Port — no external broker for v1.

**Out:**
- Port *contracts* for app database, vector store, embedding, graph
  store — owned by
  EP-0001/EP-0004/EP-0007
  (DEC-0201); this
  epic only wires them.
- The Web UI itself — EP-0006.
- Connector/identity logic —
  EP-0005; this epic's API surface
  calls into it, never reimplements it.
- Governance/gate logic —
  EP-0003; the API enforces
  gates by calling into it.
- External Queue/KV-store adapters (Celery/RQ, AWS SQS, Redis, etc.) —
  deferred behind `TRG-0001`/`TRG-0002`
  (SP-0009,
  SP-0010, per
  DEC-0205).
- Additional KV-store use cases beyond the baseline coordination-state
  and general-caching scope — deferred
  (SP-0011).
- The ephemeral in-memory Queue adapter and the dedicated embedded
  KV-library adapter — deferred/backlog alternates
  (DEC-0204),
  not built in v1.

## Domain Context

Bounded context: **Platform**. New term: Composition Root (per
[CONTEXT.md](../../CONTEXT.md)). Extends existing terms: Port, Adapter —
now six Ports, not four
(DEC-0203).

## Interfaces & Contracts to Define

- **Composition Root startup/config schema**: how deployment
  configuration selects which Adapter binds to each of the six Ports.
- **Inbound API contract**: the FastAPI route surface serving
  EP-0006's needs (goal/epic/story/
  session views, gate actions) and SSE streaming endpoints for the
  session-engine client
  (DEC-0187).
- **Queue Port contract**: enqueue / consume / ack / retry semantics,
  plus a conformance test suite every adapter (the v1 default and any
  future one) must pass.
- **KV-store Port contract**: get / set / delete, with TTL support for
  the caching use case, plus its own conformance test suite — following
  every existing Port's pattern
  (DEC-0122).

## Risks & Open Questions

- External Queue adapter choice →
  SP-0009
  (AWS SQS evaluation), deferred, triggers `TRG-0001`/`TRG-0002`.
- External KV-store adapter choice →
  SP-0010,
  deferred, triggers `TRG-0001`/`TRG-0002`.
- Further KV-store use cases beyond the two scoped now →
  SP-0011, deferred.
- Composition Root config schema format (structured file, environment
  variables, or both) — open; resolve at story derivation.

## Derived Work

Draft-ahead spikes, ratified by this epic's approval (per the Gates and
approvals draft-ahead rule):
- SP-0009 — AWS
  SQS adapter evaluation for the Queue Port, deferred/backlog, triggers
  `TRG-0001`/`TRG-0002`.
- SP-0010 —
  external KV-store adapter evaluation, deferred/backlog, triggers
  `TRG-0001`/`TRG-0002`.
- SP-0011 —
  KV-store additional use-case discovery, deferred/backlog.

Stories, derived via SES-0039:
- ST-0057 — Composition Root,
  config-driven Port/Adapter binding.
- ST-0058 —
  Inbound API, artifact/session/gate REST surface.
- ST-0059 —
  Inbound API, session SSE streaming with reconnect/resume.
- ST-0060 — Queue Port, contract +
  conformance suite + durable adapter.
- ST-0061 —
  in-process asyncio background job execution runtime.
- ST-0062 — KV-store Port,
  contract + conformance suite + app-database-reuse adapter.
- ST-0063 —
  ephemeral in-memory Queue adapter, deferred/backlog.
- ST-0064 —
  dedicated embedded KV-store library adapter, deferred/backlog.

Components, contract-completed from the stories above:
- CMP-0010 — Composition Root
- CMP-0011 — Inbound API
- CMP-0012 — Queue Port
- CMP-0013 — Background Job Execution Runtime
- CMP-0014 — KV-Store Port
