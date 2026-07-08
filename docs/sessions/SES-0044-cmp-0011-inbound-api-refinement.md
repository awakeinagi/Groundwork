---
id: SES-0044
type: session
title: CMP-0011 Inbound API — component contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
participant: awakeinagi@gmail.com
links:
  relates-to: [CMP-0011, EP-0008, ST-0058, ST-0059]
---

# SES-0044: Inbound API — Contract Refinement

## Purpose

Make [CMP-0011](../components/CMP-0011-inbound-api.md) contract-complete
against approved stories
[ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md)
(REST/artifact/gate) and
[ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md) (SSE
streaming). Everything the two stories settle (FastAPI/ASGI, the route
groups, problem+json reuse, auth on every route, SSE reconnect/resume
via `Last-Event-ID`, inactivity-clock neutrality) was recapped as
settled and not re-litigated; three genuinely open contract-shaping
questions were grilled.

## Transcript

**T1 — Route-surface granularity: how concrete should the route contract
be inside the Component Doc, given
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)
requires a language-neutral spec?**

Facilitator recommended: contract the **behavioral endpoint groups**
(artifact reads, gate actions, conflict reads, notifications, governance
metrics, session SSE) as items — behavior, auth, the component each
calls, its problem+json failure classes — and name a **maintained
OpenAPI document as the authoritative wire contract** for exact
paths/verbs/schemas (satisfying
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
Alternative: enumerate every path+verb+schema inline (rejected —
duplicates OpenAPI, drift with no source of truth between them).

Participant: selected the recommended behavioral-groups + OpenAPI-wire-
contract option. →
[DEC-0229](../decisions/DEC-0229-inbound-api-behavioral-groups-openapi-wire-contract.md).

**T2 — SSE event seam: what does the API define about the event payload
vs. the session engine's turn content?**

Facilitator recommended: the API defines the **transport envelope only**
— an `SSEEvent` value with the stable event `id` (from
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)'s
ordering), a small closed set of framing event-types (`turn-delta`,
`turn-complete`, `error`), and a `data` field carrying the session
engine's turn/delta structure **opaque** — mirroring the Queue Port's
opaque-payload seam
([DEC-0217](../decisions/DEC-0217-queue-job-envelope-opaque-payload.md)).
Turn content schema stays owned by
[EP-0002](../epics/EP-0002-refinement-session-agent.md). Alternative:
API defines the full turn/delta schema too (rejected — two owners for
one schema; drift when
[EP-0002](../epics/EP-0002-refinement-session-agent.md)'s turn shape
evolves).

Participant: selected the recommended envelope-only + opaque-passthrough
option. →
[DEC-0230](../decisions/DEC-0230-inbound-api-sse-envelope-opaque-turn-passthrough.md).

**T3 — Reconnect split:
[ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md)'s ACs
mix server duties (emit event ids, honor `Last-Event-ID`) and client
duties (auto-reconnect with backoff, transport-agnostic abstraction).
Where does [CMP-0011](../components/CMP-0011-inbound-api.md)'s contract
stop?**

Facilitator recommended:
[CMP-0011](../components/CMP-0011-inbound-api.md) owns the **server
half** — stable ascending event ids, `Last-Event-ID` resume with no
gap/dupe, problem+json on handshake failures, inactivity-clock
neutrality — while the **client-side transport abstraction +
reconnect/backoff** is owned by the Web UI
([EP-0006](../epics/EP-0006-refinement-web-ui.md),
[ST-0043](../stories/ST-0043-session-progress-and-lifecycle-shell.md)/[ST-0044](../stories/ST-0044-session-conversation-ux.md),
which [ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md)
impacts) and is an Out-of-Scope boundary here. Alternative:
[CMP-0011](../components/CMP-0011-inbound-api.md) also specifies the
client abstraction + reconnect (rejected — a backend component owning
browser-client behavior; the front/back split follows the
`Last-Event-ID` seam cleanly).

Participant: selected the recommended server-half-only option. →
[DEC-0231](../decisions/DEC-0231-inbound-api-owns-server-half-of-sse-reconnect.md).

**T4 — Confirm decisions.** Facilitator played back
[DEC-0229](../decisions/DEC-0229-inbound-api-behavioral-groups-openapi-wire-contract.md)/[DEC-0230](../decisions/DEC-0230-inbound-api-sse-envelope-opaque-turn-passthrough.md)/[DEC-0231](../decisions/DEC-0231-inbound-api-owns-server-half-of-sse-reconnect.md)
in plain language; participant confirmed all three as recorded.
Facilitator confirmed the remaining ACs (auth resolution via
[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md),
metrics fronting per
[DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)/[DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
the fixed-named-endpoints constraint) are already settled by the two
stories and fold into the doc without new DECs.

## Decisions Produced

- [DEC-0229](../decisions/DEC-0229-inbound-api-behavioral-groups-openapi-wire-contract.md)
  — behavioral endpoint groups in the doc; OpenAPI is the authoritative
  wire contract.
- [DEC-0230](../decisions/DEC-0230-inbound-api-sse-envelope-opaque-turn-passthrough.md)
  — SSE transport envelope defined by the API; turn/delta content is
  opaque passthrough.
- [DEC-0231](../decisions/DEC-0231-inbound-api-owns-server-half-of-sse-reconnect.md)
  — Inbound API owns the server half of SSE reconnect/resume; client
  abstraction belongs to
  [EP-0006](../epics/EP-0006-refinement-web-ui.md).

## Post-Session Steps

- Consistency `sweep`/`terms` over
  [DEC-0229](../decisions/DEC-0229-inbound-api-behavioral-groups-openapi-wire-contract.md)..[DEC-0231](../decisions/DEC-0231-inbound-api-owns-server-half-of-sse-reconnect.md)
  (run jointly with
  [SES-0043](../sessions/SES-0043-cmp-0010-composition-root-refinement.md)'s
  DECs): no contradictions; the `Last-Event-ID` cluster cross-links
  tightened
  ([DEC-0230](../decisions/DEC-0230-inbound-api-sse-envelope-opaque-turn-passthrough.md)↔[DEC-0231](../decisions/DEC-0231-inbound-api-owns-server-half-of-sse-reconnect.md),
  [DEC-0230](../decisions/DEC-0230-inbound-api-sse-envelope-opaque-turn-passthrough.md)→[DEC-0213](../decisions/DEC-0213-sse-reconnect-resume-contract.md)).
- Graduation review (required before gating): checked all five elements
  — `ApiApplication`/`RestSurface`/`SessionSseEndpoint` are own-service;
  `ProblemType` is Inbound-API-scoped
  ([DEC-0212](../decisions/DEC-0212-inbound-api-reuses-problem-json.md)
  deliberately chose per-surface vocabularies over one shared element);
  `SSEEvent` has a single consumer (the Web UI consumes the API
  contract, not the element). No element is consumed by a second CMP or
  needs independently versioned conformance. **Outcome: no graduation.**
- Decision-recall audit on
  [CMP-0011](../components/CMP-0011-inbound-api.md): Sonnet 5 judge over
  the 15-candidate packet. **Findings addressed:** (1) added
  [DEC-0085](../decisions/DEC-0085-implementation-guidance-split.md) at
  `IG-3`, whose "Constraint, not a Note" elevation directly invokes that
  decision's Constraints-vs-Notes distinction; (2) provenance fix — the
  frontmatter `cites` was missing
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md),
  referenced inline in Dependencies; added. Remaining candidates judged
  noise (internals of fronted components
  [CMP-0011](../components/CMP-0011-inbound-api.md) disclaims
  reimplementing).
- [CMP-0011](../components/CMP-0011-inbound-api.md) drafted
  contract-complete and set `gated`.
