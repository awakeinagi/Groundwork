---
id: EP-0008
type: epic
title: Backend Application Platform
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0006]
  impacted-by: [EP-0001, EP-0002, EP-0003, EP-0004, EP-0005, EP-0006, EP-0007]
cites: [DEC-0001, DEC-0018, DEC-0121, DEC-0122, DEC-0102, DEC-0124, DEC-0187,
        DEC-0201, DEC-0202, DEC-0203, DEC-0204, DEC-0205]
---

# EP-0008: Backend Application Platform

## Summary

The composition/runtime layer that assembles Groundwork's domain engines
([EP-0001](EP-0001-artifact-store-and-format-engine.md)..[EP-0004](EP-0004-graph-index.md),
[EP-0007](EP-0007-consolidation-memory-layer.md)) and integration layer
([EP-0005](EP-0005-connectors-and-identity.md)) into one running v1
application, and exposes it to the UI channel
([EP-0006](EP-0006-refinement-web-ui.md)): the Composition Root (binding
Port contracts to concrete Adapters at startup, from deployment
configuration), the inbound API surface (FastAPI, ASGI, SSE per
[DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)),
and two new infrastructure ports — Queue and KV-store — extending the
Port family
([DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)). Identified
as a gap in the original epic derivation
([SES-0035](../sessions/SES-0035-goal-template-redesign.md)
retrospective); this epic closes it.

## Why (Goal Alignment)

[BG-0001](../goals/BG-0001-groundwork.md)'s Intent names "a standalone
application" with backend services as one of three deliverables
([DEC-0001](../decisions/DEC-0001-standalone-application.md)) — this is
that deliverable's owning epic.
[BG-0001](../goals/BG-0001-groundwork.md)'s System Context (per
[DEC-0190](../decisions/DEC-0190-system-context-bg-section.md)) already
states the v1 process/deployment shape (single-process, single-writer,
until `TRG-0001`/`TRG-0002` fire) and the trigger/output contract this
epic implements. Outcome 4 (parallel implementability) depends on
component docs being contract-complete — this epic's Composition Root
and API contracts are the stable seam the UI
([EP-0006](EP-0006-refinement-web-ui.md)) and the engine/connector
components build against, instead of each other's internals.

## Scope

**In:**
- **Composition Root**: binds the six Port contracts (app database,
  vector store, embedding, graph store, Queue, KV-store) to concrete
  Adapters at process startup, from deployment configuration
  ([DEC-0201](../decisions/DEC-0201-composition-root-split.md),
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)). For the
  four pre-existing ports, it selects among the already-decided v1
  adapters: embedded LadybugDB (graph) and DuckDB (app database, vector
  search) ([DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)), and
  the local-model or REST-client embedding adapter
  ([DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
- **Inbound API**: a FastAPI/ASGI application serving the Web UI's
  HTTP + SSE needs
  ([DEC-0202](../decisions/DEC-0202-fastapi-selected.md),
  [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).
- **Queue Port**: contract plus v1 default adapter — durable,
  app-database-backed
  ([DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md),
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
- **KV-store Port**: contract plus v1 default adapter — reuses the
  app-database Port
  ([DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md),
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
- **Runtime/async execution model**: in-process asyncio background
  tasks running against the Queue Port — no external broker for v1.

**Out:**
- Port *contracts* for app database, vector store, embedding, graph
  store — owned by
  [EP-0001](EP-0001-artifact-store-and-format-engine.md)/[EP-0004](EP-0004-graph-index.md)/[EP-0007](EP-0007-consolidation-memory-layer.md)
  ([DEC-0201](../decisions/DEC-0201-composition-root-split.md)); this
  epic only wires them.
- The Web UI itself — [EP-0006](EP-0006-refinement-web-ui.md).
- Connector/identity logic —
  [EP-0005](EP-0005-connectors-and-identity.md); this epic's API surface
  calls into it, never reimplements it.
- Governance/gate logic —
  [EP-0003](EP-0003-governance-and-gate-engine.md); the API enforces
  gates by calling into it.
- External Queue/KV-store adapters (Celery/RQ, AWS SQS, Redis, etc.) —
  deferred behind `TRG-0001`/`TRG-0002`
  ([SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md),
  [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md)).
- Additional KV-store use cases beyond the baseline coordination-state
  and general-caching scope — deferred
  ([SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md)).
- The ephemeral in-memory Queue adapter and the dedicated embedded
  KV-library adapter — deferred/backlog alternates
  ([DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)),
  not built in v1.

## Domain Context

Bounded context: **Platform**. New term: Composition Root (per
[CONTEXT.md](../../CONTEXT.md)). Extends existing terms: Port, Adapter —
now six Ports, not four
([DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)).

## Interfaces & Contracts to Define

- **Composition Root startup/config schema**: how deployment
  configuration selects which Adapter binds to each of the six Ports.
- **Inbound API contract**: the FastAPI route surface serving
  [EP-0006](EP-0006-refinement-web-ui.md)'s needs (goal/epic/story/
  session views, gate actions) and SSE streaming endpoints for the
  session-engine client
  ([DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).
- **Queue Port contract**: enqueue / consume / ack / retry semantics,
  plus a conformance test suite every adapter (the v1 default and any
  future one) must pass.
- **KV-store Port contract**: get / set / delete, with TTL support for
  the caching use case, plus its own conformance test suite — following
  every existing Port's pattern
  ([DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).

## Risks & Open Questions

- External Queue adapter choice →
  [SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md)
  (AWS SQS evaluation), deferred, triggers `TRG-0001`/`TRG-0002`.
- External KV-store adapter choice →
  [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md),
  deferred, triggers `TRG-0001`/`TRG-0002`.
- Further KV-store use cases beyond the two scoped now →
  [SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md), deferred.
- Composition Root config schema format (structured file, environment
  variables, or both) — open; resolve at story derivation.

## Derived Work

Draft-ahead spikes, ratified by this epic's approval (per the Gates and
approvals draft-ahead rule):
- [SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md) — AWS
  SQS adapter evaluation for the Queue Port, deferred/backlog, triggers
  `TRG-0001`/`TRG-0002`.
- [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md) —
  external KV-store adapter evaluation, deferred/backlog, triggers
  `TRG-0001`/`TRG-0002`.
- [SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md) —
  KV-store additional use-case discovery, deferred/backlog.

Stories, derived via [SES-0039](../sessions/SES-0039-ep-0008-story-derivation.md):
- [ST-0057](../stories/ST-0057-composition-root.md) — Composition Root,
  config-driven Port/Adapter binding.
- [ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md) —
  Inbound API, artifact/session/gate REST surface.
- [ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md) —
  Inbound API, session SSE streaming with reconnect/resume.
- [ST-0060](../stories/ST-0060-queue-port.md) — Queue Port, contract +
  conformance suite + durable adapter.
- [ST-0061](../stories/ST-0061-background-job-execution-runtime.md) —
  in-process asyncio background job execution runtime.
- [ST-0062](../stories/ST-0062-kv-store-port.md) — KV-store Port,
  contract + conformance suite + app-database-reuse adapter.
- [ST-0063](../stories/ST-0063-ephemeral-in-memory-queue-adapter.md) —
  ephemeral in-memory Queue adapter, deferred/backlog.
- [ST-0064](../stories/ST-0064-dedicated-embedded-kv-library-adapter.md) —
  dedicated embedded KV-store library adapter, deferred/backlog.
