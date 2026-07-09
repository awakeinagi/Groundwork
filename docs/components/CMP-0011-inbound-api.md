---
id: CMP-0011
type: component
title: Inbound API
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  FastAPI/ASGI HTTP+SSE surface serving the Web UI. Non-streaming REST
  routes for artifact reads with provenance, gate actions, conflict reads,
  notification reads/writes, and governance metrics (fixed named endpoints,
  no generic query language). SSE endpoint for session-engine turns with
  Last-Event-ID reconnect/resume, emitting stable monotonically-ascending
  event IDs. All responses application/problem+json per RFC 9457. Computes
  nothing itself — fronts CMP-0001, CMP-0004, and ST-0018. Four elements:
  ApiApplication, ProblemType, RestSurface, SessionSseEndpoint.
context: platform
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0010, CMP-0004, CMP-0001]
cites: [DEC-0001, DEC-0018, DEC-0042, DEC-0085, DEC-0127, DEC-0132, DEC-0133,
        DEC-0163, DEC-0182, DEC-0187, DEC-0202, DEC-0207, DEC-0212, DEC-0213,
        DEC-0226, DEC-0227, DEC-0229, DEC-0230, DEC-0231]
---

# CMP-0011: Inbound API

## Purpose

The FastAPI/ASGI HTTP+SSE surface serving the Web UI
(EP-0006): non-streaming REST
routes for artifact reads with provenance drill-down, gate actions,
conflict reads, notification reads/writes, and governance metrics
(ST-0058),
plus SSE streaming of session-engine turns with `Last-Event-ID`
reconnect/resume
(ST-0059)
(DEC-0202,
DEC-0207). It
computes nothing itself — it fronts the Governance & Gate Engine, the
Canonical Store, and the session engine, translating transport and
errors only. The surface exists because Groundwork ships as a
standalone application whose stakeholders work through a web UI, not
a terminal (per DEC-0001).

## Ubiquitous Language

Port, Adapter, Participant, Session — per
[CONTEXT.md](../../CONTEXT.md). Standards used verbatim, not redefined:
**problem+json** (RFC 9457 error body, per
DEC-0127) and
**SSE** (Server-Sent Events, the v1 streaming transport, per
DEC-0187).

## Design Elements

### ApiApplication (service)

Implements: ST-0058,
ST-0059

- `ApiApplication.A-1` — the FastAPI/ASGI application object; its
  lifespan hook invokes
  CMP-0010's
  `CompositionRoot.A-2` (`startup()`/`shutdown()`) rather than
  orchestrating bring-up itself, and receives its dependencies by
  constructor injection from the `ApplicationContainer` (per
  DEC-0202,
  DEC-0227).
- `ApiApplication.B-1` — every route requires an authenticated
  Participant, resolved through
  ST-0022's
  provider contract; an unauthenticated request receives a `401`
  `application/problem+json` response with the `identity-required`
  problem type (per
  ST-0058 AC2,
  DEC-0212).
- `ApiApplication.B-2` — every non-2xx response, on every route, is
  `application/problem+json` per RFC 9457 with a stable `type` URI per
  failure class and tier-1 field-level errors in an `errors[]` extension
  member where applicable — reusing
  DEC-0127's model
  rather than a new envelope (per
  DEC-0212).
- `ApiApplication.B-3` — the whole route surface is published as a
  maintained **OpenAPI** document, the authoritative language-neutral
  wire contract; the `A-*` route items below fix behavior, calls, and
  failure classes, while exact paths, verbs, and success-body schemas
  resolve to that document (per
  DEC-0229,
  DEC-0018).

### ProblemType (value)

Implements: ST-0058,
ST-0059

- `ProblemType.D-1` — schema: the RFC 9457 problem+json body — `type`
  (stable URI), `title`, `status`, `detail`, `instance`, plus an
  `errors[]` extension member carrying tier-1 field-level errors where
  applicable (per
  DEC-0127,
  DEC-0212).
- `ProblemType.D-2` — the v1 Inbound-API problem-type vocabulary is a
  named, **extensible** set scoped to this surface — including at least
  `identity-required` (401), `gate-already-approved`, and
  `session-not-found`, alongside the not-found / conflict / validation
  classes each route group raises; a new surface adds types without
  changing the envelope (per
  DEC-0212).

### RestSurface (service)

Implements: ST-0058

- `RestSurface.A-1` — artifact reads: read a Business Goal / Epic /
  Story / Spike with full content and provenance drill-down; success
  schema resolves to the OpenAPI document (`ApiApplication.B-3`), errors
  to `ProblemType`. Reads come from the Canonical Store
  (CMP-0001 `StorageService.A-1`),
  never a duplicated projection (per
  ST-0058
  AC1/AC4).
- `RestSurface.A-2` — gate actions: approve / request-changes, calling
  into the Governance & Gate Engine
  (CMP-0004) and driving the host
  PR through the connector — never reimplementing gate logic; a
  disallowed transition surfaces as a `ProblemType` (e.g.
  `gate-already-approved`) (per
  ST-0058
  AC1/AC4).
- `RestSurface.A-3` — conflict reads: read conflict state for an
  artifact (per
  ST-0058 AC1,
  serving ST-0047).
- `RestSurface.A-4` — notification reads/writes: list notifications,
  update read/unread state, and write preferences for the authenticated
  Participant (per
  ST-0058 AC1,
  serving ST-0048).
- `RestSurface.A-5` — governance metrics: expose
  ST-0018's
  existing metrics/query API over HTTP as **fixed named endpoints** —
  never a generic query language at the HTTP boundary — computing
  nothing itself (per
  ST-0058 AC5,
  DEC-0163,
  DEC-0042).
- `RestSurface.B-1` — front, don't reimplement: gate actions call
  CMP-0004, artifact reads call
  CMP-0001, and metrics front
  ST-0018; this
  surface holds no gate, artifact, or metric computation of its own (per
  ST-0058 AC4,
  DEC-0042).
- `RestSurface.B-2` — the metrics endpoints translate
  ST-0018's own
  error signaling into this surface's problem+json vocabulary rather
  than assuming it already speaks RFC 9457 (per
  ST-0058
  Notes,
  DEC-0127).

### SessionSseEndpoint (service)

Implements: ST-0059

- `SessionSseEndpoint.A-1` — an SSE endpoint streams append-turn output
  for an open session as `SSEEvent` frames; the stakeholder's own turns
  are sent as plain POSTs through `RestSurface`, not over the SSE
  channel (per
  ST-0059 AC1,
  DEC-0187).
- `SessionSseEndpoint.B-1` — emits stable, **monotonically ascending**
  SSE event ids (the session engine's per-session ordered id, consumed
  from ST-0032);
  on a reconnect carrying `Last-Event-ID`, resumes the stream with **no
  turn dropped or duplicated** (per
  ST-0059 AC3,
  DEC-0213).
- `SessionSseEndpoint.B-2` — carries the session engine's turn/delta
  structure through as the `SSEEvent.data` field, **opaque** — it frames
  and orders, never parses the turn body — while the envelope's
  `event`-type (`turn-delta`/`turn-complete`) gives the UI enough
  structure to render partial agent output incrementally, not only a
  completed turn (per
  ST-0059 AC4,
  DEC-0230).
- `SessionSseEndpoint.B-3` — every non-2xx on the setup/handshake path
  (session not found, unauthenticated) follows the same problem+json
  convention as the REST surface (per
  ST-0059 AC5,
  DEC-0212).
- `SessionSseEndpoint.B-4` — a reconnect-and-resume is transport
  recovery, not a new activity signal: it neither resets nor extends the
  session's inactivity clock beyond what the underlying streamed turn
  already does, and never causes the session to auto-close mid-turn (per
  ST-0059 AC6,
  DEC-0182).

### SSEEvent (value)

Implements: ST-0059

- `SSEEvent.D-1` — schema (the SSE transport envelope): `id` (the
  session engine's stable, per-session ordered id, from
  ST-0032),
  `event` (closed set: `turn-delta | turn-complete | error`), and `data`
  (the session engine's turn/delta JSON, carried **verbatim and opaque**).
  Equality by value (per
  DEC-0230,
  DEC-0187).
- `SSEEvent.D-2` — the `id` ordering is **consumed, not defined here**:
  the session engine assigns it
  (ST-0032),
  and `Last-Event-ID` resume keys on it (per
  DEC-0213,
  DEC-0230).

## Component Invariants

- `C-1` — every non-2xx response on every route (REST and the SSE
  handshake) is `application/problem+json`; no route emits a bare or
  ad-hoc error body (per
  DEC-0212,
  DEC-0127).
- `C-2` — the API computes no governance, gate, or artifact result
  itself: it fronts CMP-0004,
  CMP-0001, and
  ST-0018's
  metrics API, translating only transport and errors (per
  ST-0058
  AC4/AC5,
  DEC-0042).
- `C-3` — the SSE stream neither drops nor duplicates a turn across a
  `Last-Event-ID` reconnect (per
  DEC-0213).

## Implementation Guidance

### Constraints

- `IG-1` — the framework is FastAPI on ASGI (per
  DEC-0202).
- `IG-2` — the route surface is published as a maintained OpenAPI
  document — the authoritative language-neutral wire contract; success-
  body schemas resolve to it (per
  DEC-0229,
  DEC-0018).
- `IG-3` — `Last-Event-ID`-based resume is normative for the reference
  implementation, a Constraint and not a Note — deliberately elevated per
  the Constraints-vs-Notes distinction (per
  DEC-0213,
  DEC-0085).
- `IG-4` — v1 ships the SSE transport only; a WebSocket implementation
  of the client transport interface is deferred (the interface lives
  client-side in EP-0006, the
  implementation does not ship in v1) (per
  DEC-0187).

### Notes

- Exact route paths, OpenAPI `operationId`s, and the server-tolerated
  bounds on a reconnect gap are implementation choices within the
  contract above.
- ST-0018's
  metrics API predates
  DEC-0127's
  citation set; front it defensively (`RestSurface.B-2`) rather than
  assuming it already emits problem+json.

## Dependencies

- CMP-0010 — consumed:
  `CompositionRoot.A-2` (`startup()`/`shutdown()`), invoked from the ASGI
  lifespan, and the `ApplicationContainer` from which this component's
  dependencies are constructor-injected (per
  DEC-0227,
  DEC-0226).
- CMP-0004 — consumed: the gate
  evaluation surface (`GatePolicyCheck.A-1`) for gate actions and the
  conflict surface (`ConflictGate.A-1` evaluate) for conflict reads; the
  API drives these, never reimplements gate/conflict logic.
- CMP-0001 — consumed:
  `StorageService.A-1` (`read(artifact-id, [ref]) → {document,
  provenance}`) for artifact reads with provenance drill-down.
- Forward-declared (per
  DEC-0132):
  the identity-provider contract from
  ST-0022
  (owned by CMP-0007) resolving the
  Participant on every route; and
  ST-0032's
  append-turn stream and stable per-session event-id ordering, consumed
  by `SessionSseEndpoint`.

## Acceptance & Test Expectations

1. REST surface: an artifact read returns full content and provenance
   from CMP-0001; a gate approve
   drives its verdict through
   CMP-0004; conflict and
   notification reads/writes serve the authenticated Participant (per
   ST-0058
   AC1/AC4).
2. Auth + errors: an unauthenticated request to any route returns `401`
   `application/problem+json`, and every non-2xx across the REST and
   SSE-handshake paths is RFC 9457 problem+json with a stable `type` from
   the Inbound-API vocabulary (per
   ST-0058
   AC2/AC3,
   ST-0059 AC5,
   DEC-0212).
3. Metrics fronting: governance metrics endpoints return
   ST-0018's
   metrics over fixed named HTTP endpoints — no generic query language at
   the boundary — computing nothing themselves (per
   ST-0058 AC5,
   DEC-0163).
4. SSE streaming + resume: an open session streams
   `turn-delta`/`turn-complete` `SSEEvent`s; killing the connection and
   reconnecting with `Last-Event-ID` resumes with no turn dropped or
   duplicated in the rendered conversation (per
   ST-0059
   AC1/AC3/AC4,
   DEC-0213).
5. Inactivity neutrality: a mid-turn reconnect does not reset or extend
   the inactivity clock and never auto-closes the session mid-turn (per
   ST-0059 AC6,
   DEC-0182).
6. OpenAPI: the full served route surface is published as a maintained
   OpenAPI document matching the routes actually served (per
   ST-0058 AC6,
   DEC-0229).

## Out of Scope

Boundary statements (per
DEC-0133):

- The SSE **client** transport-agnostic abstraction and automatic
  reconnect-with-backoff — owned by the Web UI
  (EP-0006,
  ST-0043/ST-0044);
  this component owns only the server half (stable ids, `Last-Event-ID`
  resume) (per
  DEC-0231).
- A WebSocket implementation of the transport interface — the client
  interface is EP-0006's and the
  implementation is deferred; not this backend component's work at all
  (per
  DEC-0187).
- Gate / governance / conflict decision *logic* —
  EP-0003/CMP-0004;
  the API only calls into it.
- Connector logic (code host, work management, notifier) —
  EP-0005; the API calls
  connectors, never reimplements them.
- The UI itself — rendering and client-side state —
  EP-0006.
- Governance metrics *computation* —
  ST-0018; this
  component only exposes it over HTTP (per
  DEC-0042).
- Session-engine internals (turn storage, guardrails, distillation, and
  the event-id *assignment*) —
  ST-0032
  and EP-0002; the SSE
  endpoint consumes the ordering, it does not define it (per
  DEC-0230).
