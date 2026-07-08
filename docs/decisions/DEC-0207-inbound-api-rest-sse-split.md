---
id: DEC-0207
type: decision
title: Inbound API splits into a REST/artifact+gate story and a separate SSE session-streaming story
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T1-T2"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0187, DEC-0202, DEC-0198, DEC-0200]
  supersedes: []
---

# DEC-0207: Inbound API Splits into REST and SSE Stories

## Context

[EP-0008](../epics/EP-0008-backend-application-platform.md) named one
Inbound API deliverable (FastAPI, HTTP + SSE). Story derivation needed
to decide whether that is one story or more, per the story-slicing
seam catalog's Data Seam channel variant
([DEC-0198](../decisions/DEC-0198-story-slicing-seam-catalog.md)).

## Decision

The Inbound API is split into two stories:
[ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md) — REST
routes for goal/epic/story/session views and gate actions, and
[ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md) — the
SSE streaming endpoint for the session-engine client
([DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).

## Rationale

The two are independently testable and demoable: REST artifact/gate
routes can be exercised and gated without streaming working, and the
SSE endpoint's event-schema/reconnect contract
([DEC-0213](../decisions/DEC-0213-sse-reconnect-resume-contract.md)) is
a distinct, individually-verifiable concern — the Data Seam's
different-entry-method variant, applied to channel rather than data
type. Keeps each story's Acceptance Criteria list from ballooning past a
tight, individually-testable set
([DEC-0200](../decisions/DEC-0200-no-fixed-story-count.md)).

## Alternatives Considered

- **One combined "Inbound API" story**: rejected — SSE was required
  from day one by [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md),
  but "required from day one" doesn't mean "inseparable"; bundling would
  make the REST routes wait on streaming's reconnect/backoff details
  being settled before either could gate.

## Implications

[ST-0059](../stories/ST-0059-inbound-api-session-sse-streaming.md)
depends-on [ST-0058](../stories/ST-0058-inbound-api-rest-and-gate-surface.md)
(shares the FastAPI app scaffolding) and on
[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)
(the streaming contract it exposes).
