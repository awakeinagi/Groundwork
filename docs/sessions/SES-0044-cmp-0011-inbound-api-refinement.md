---
id: SES-0044
type: session
title: CMP-0011 Inbound API — component contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  SES-0044 refined the CMP-0011 Inbound API component contract against
  approved stories ST-0058 and ST-0059, grilling three open questions:
  route-surface granularity (decided: behavioral endpoint groups with
  OpenAPI as authoritative wire contract), SSE event seam (decided: API
  defines transport envelope only, opaque passthrough), and SSE
  reconnect/resume ownership (decided: CMP-0011 owns server half only).
  Produced DEC-0229, DEC-0230, DEC-0231. Status closed.
participant: awakeinagi@gmail.com
links:
  relates-to: [CMP-0011, EP-0008, ST-0058, ST-0059]
---

# SES-0044: Inbound API — Contract Refinement

## Purpose

Make CMP-0011 contract-complete
against approved stories
ST-0058
(REST/artifact/gate) and
ST-0059 (SSE
streaming). Everything the two stories settle (FastAPI/ASGI, the route
groups, problem+json reuse, auth on every route, SSE reconnect/resume
via `Last-Event-ID`, inactivity-clock neutrality) was recapped as
settled and not re-litigated; three genuinely open contract-shaping
questions were grilled.

## Transcript

**T1 — Route-surface granularity: how concrete should the route contract
be inside the Component Doc, given
DEC-0018
requires a language-neutral spec?**

Facilitator recommended: contract the **behavioral endpoint groups**
(artifact reads, gate actions, conflict reads, notifications, governance
metrics, session SSE) as items — behavior, auth, the component each
calls, its problem+json failure classes — and name a **maintained
OpenAPI document as the authoritative wire contract** for exact
paths/verbs/schemas (satisfying
DEC-0018).
Alternative: enumerate every path+verb+schema inline (rejected —
duplicates OpenAPI, drift with no source of truth between them).

Participant: selected the recommended behavioral-groups + OpenAPI-wire-
contract option. →
DEC-0229.

**T2 — SSE event seam: what does the API define about the event payload
vs. the session engine's turn content?**

Facilitator recommended: the API defines the **transport envelope only**
— an `SSEEvent` value with the stable event `id` (from
ST-0032's
ordering), a small closed set of framing event-types (`turn-delta`,
`turn-complete`, `error`), and a `data` field carrying the session
engine's turn/delta structure **opaque** — mirroring the Queue Port's
opaque-payload seam
(DEC-0217).
Turn content schema stays owned by
EP-0002. Alternative:
API defines the full turn/delta schema too (rejected — two owners for
one schema; drift when
EP-0002's turn shape
evolves).

Participant: selected the recommended envelope-only + opaque-passthrough
option. →
DEC-0230.

**T3 — Reconnect split:
ST-0059's ACs
mix server duties (emit event ids, honor `Last-Event-ID`) and client
duties (auto-reconnect with backoff, transport-agnostic abstraction).
Where does CMP-0011's contract
stop?**

Facilitator recommended:
CMP-0011 owns the **server
half** — stable ascending event ids, `Last-Event-ID` resume with no
gap/dupe, problem+json on handshake failures, inactivity-clock
neutrality — while the **client-side transport abstraction +
reconnect/backoff** is owned by the Web UI
(EP-0006,
ST-0043/ST-0044,
which ST-0059
impacts) and is an Out-of-Scope boundary here. Alternative:
CMP-0011 also specifies the
client abstraction + reconnect (rejected — a backend component owning
browser-client behavior; the front/back split follows the
`Last-Event-ID` seam cleanly).

Participant: selected the recommended server-half-only option. →
DEC-0231.

**T4 — Confirm decisions.** Facilitator played back
DEC-0229/DEC-0230/DEC-0231
in plain language; participant confirmed all three as recorded.
Facilitator confirmed the remaining ACs (auth resolution via
ST-0022,
metrics fronting per
DEC-0163/DEC-0042,
the fixed-named-endpoints constraint) are already settled by the two
stories and fold into the doc without new DECs.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  this session refined CMP-0011, a component of the Backend
  Application Platform epic EP-0008.

## Decisions Produced

- DEC-0229
  — behavioral endpoint groups in the doc; OpenAPI is the authoritative
  wire contract.
- DEC-0230
  — SSE transport envelope defined by the API; turn/delta content is
  opaque passthrough.
- DEC-0231
  — Inbound API owns the server half of SSE reconnect/resume; client
  abstraction belongs to
  EP-0006.

## Post-Session Steps

- Consistency `sweep`/`terms` over
  DEC-0229..DEC-0231
  (run jointly with
  SES-0043's
  DECs): no contradictions; the `Last-Event-ID` cluster cross-links
  tightened
  (DEC-0230↔DEC-0231,
  DEC-0230→DEC-0213).
- Graduation review (required before gating): checked all five elements
  — `ApiApplication`/`RestSurface`/`SessionSseEndpoint` are own-service;
  `ProblemType` is Inbound-API-scoped
  (DEC-0212
  deliberately chose per-surface vocabularies over one shared element);
  `SSEEvent` has a single consumer (the Web UI consumes the API
  contract, not the element). No element is consumed by a second CMP or
  needs independently versioned conformance. **Outcome: no graduation.**
- Decision-recall audit on
  CMP-0011: Sonnet 5 judge over
  the 15-candidate packet. **Findings addressed:** (1) added
  DEC-0085 at
  `IG-3`, whose "Constraint, not a Note" elevation directly invokes that
  decision's Constraints-vs-Notes distinction; (2) provenance fix — the
  frontmatter `cites` was missing
  DEC-0226,
  referenced inline in Dependencies; added. Remaining candidates judged
  noise (internals of fronted components
  CMP-0011 disclaims
  reimplementing).
- CMP-0011 drafted
  contract-complete and set `gated`.
