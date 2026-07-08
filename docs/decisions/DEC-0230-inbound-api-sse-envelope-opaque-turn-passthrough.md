---
id: DEC-0230
type: decision
title: The Inbound API SSE contract defines the transport envelope only; session turn/delta content is opaque passthrough owned by the session engine
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0044 @ T2"
links:
  derives-from: [SES-0044]
  relates-to: [DEC-0187, DEC-0207, DEC-0213, DEC-0217, DEC-0231]
  supersedes: []
---

# DEC-0230: SSE Envelope Defined by the API; Turn Content Is Opaque Passthrough

## Context

[ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md)
streams [ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)'s
append-turn output over SSE, and AC4 requires enough structure to render
partial agent output incrementally. Drafting
[CMP-0011](../components/CMP-0011-inbound-api.md) needed to decide
whether the API defines the full turn/delta schema on the wire or only
the SSE transport envelope around it.

## Decision

[CMP-0011](../components/CMP-0011-inbound-api.md) defines an **SSEEvent
value element — the transport envelope only**: the stable event `id`
(the session engine's per-session ordered id, per
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)),
a small **closed set of framing event-types** (e.g. `turn-delta`,
`turn-complete`, `error`), and a `data` field carrying the session
engine's turn/delta structure **verbatim and opaque** — the API frames
and orders it but never parses or re-declares its body. The turn/delta
content schema remains owned by
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)/[EP-0002](../epics/EP-0002-refinement-session-agent.md).

## Rationale

Mirrors the Queue Port's opaque-payload seam
([DEC-0217](../decisions/DEC-0217-queue-job-envelope-opaque-payload.md)):
one owner per schema. If the API re-declared the turn body it would
co-own the session engine's turn model and go stale whenever
[EP-0002](../epics/EP-0002-refinement-session-agent.md)'s turn shape
evolves. Framing + ordering is genuinely the API's concern; turn content
is not.

## Alternatives Considered

- **API defines the full turn/delta schema too**: rejected — more
  self-contained for a client reading only this doc, but creates two
  owners for one schema and a standing drift risk against
  [EP-0002](../epics/EP-0002-refinement-session-agent.md).

## Implications

[CMP-0011](../components/CMP-0011-inbound-api.md) carries an `SSEEvent`
value element (envelope schema + the closed event-type set); the SSE
endpoint service item passes `data` through untouched. `Last-Event-ID`
resume ([DEC-0213](../decisions/DEC-0213-sse-reconnect-resume-contract.md))
keys on the envelope `id`, not on turn content.
