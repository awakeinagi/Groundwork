---
id: DEC-0207
type: decision
title: Inbound API splits into a REST/artifact+gate story and a separate SSE session-streaming story
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Inbound API splits into two stories: ST-0058 (REST routes for goal/
  epic/story/session views and gate actions) and ST-0059 (SSE streaming
  endpoint for session-engine client). Independently testable and
  demoable via Data Seam's different-entry-method variant applied to
  channel. Keeps each story's Acceptance Criteria list tight rather than
  waiting on streaming's reconnect/backoff details. ST-0059 depends-on
  ST-0058 and ST-0032. Status accepted.
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

EP-0008 named one
Inbound API deliverable (FastAPI, HTTP + SSE). Story derivation needed
to decide whether that is one story or more, per the story-slicing
seam catalog's Data Seam channel variant
(DEC-0198).

## Decision

The Inbound API is split into two stories:
ST-0058 — REST
routes for goal/epic/story/session views and gate actions, and
ST-0059 — the
SSE streaming endpoint for the session-engine client
(DEC-0187).

## Rationale

The two are independently testable and demoable: REST artifact/gate
routes can be exercised and gated without streaming working, and the
SSE endpoint's event-schema/reconnect contract
(DEC-0213) is
a distinct, individually-verifiable concern — the Data Seam's
different-entry-method variant, applied to channel rather than data
type. Keeps each story's Acceptance Criteria list from ballooning past a
tight, individually-testable set
(DEC-0200).

## Alternatives Considered

- **One combined "Inbound API" story**: rejected — SSE was required
  from day one by DEC-0187,
  but "required from day one" doesn't mean "inseparable"; bundling would
  make the REST routes wait on streaming's reconnect/backoff details
  being settled before either could gate.

## Implications

ST-0059
depends-on ST-0058
(shares the FastAPI app scaffolding) and on
ST-0032
(the streaming contract it exposes).
