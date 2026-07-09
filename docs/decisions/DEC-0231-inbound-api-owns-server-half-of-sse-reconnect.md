---
id: DEC-0231
type: decision
title: The Inbound API owns the server half of SSE reconnect/resume; the client transport abstraction and reconnect/backoff belong to the Web UI
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Decides that CMP-0011 (backend Inbound API) contracts only the
  server half of SSE reconnect/resume: emit stable, monotonically
  ascending event ids; on reconnect carrying Last-Event-ID, resume
  with no turn dropped or duplicated; return problem+json on
  handshake failures; never treat reconnect as activity signal. The
  client-side transport-agnostic abstraction and automatic
  reconnect-with-backoff are owned by Web UI (EP-0006) and marked
  Out-of-Scope here. The Last-Event-ID standard contract is the clean
  boundary between backend and frontend halves, keeping the backend
  component from owning UI-client behavior.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0044 @ T3"
links:
  derives-from: [SES-0044]
  relates-to: [DEC-0187, DEC-0213, DEC-0207, DEC-0230]
  supersedes: []
---

# DEC-0231: Inbound API Owns the Server Half of SSE Reconnect/Resume

## Context

ST-0059's
Acceptance Criteria mix server-side duties (emit SSE event ids, honor
`Last-Event-ID` on resume — AC3) with client-side ones (automatic
reconnect with backoff, a transport-agnostic client interface — AC2,
AC3). CMP-0011 is the *backend*
Inbound API component; its contract needed a clean stopping line.

## Decision

CMP-0011 contracts the **server
half** of reconnect/resume: emit **stable, monotonically ascending SSE
event ids**; on a reconnect carrying `Last-Event-ID`, **resume the
stream with no turn dropped or duplicated**; return problem+json on
handshake/setup failures
(DEC-0212);
and never treat a reconnect as a new activity signal
(DEC-0182).
The **client-side transport-agnostic abstraction and automatic
reconnect-with-backoff** (ST-0059 AC2 and the backoff schedule of AC3)
are owned by the Web UI (EP-0006,
ST-0043/ST-0044,
which ST-0059
impacts) and are an Out-of-Scope boundary in this component.

## Rationale

Emitting ids and honoring `Last-Event-ID` is server behavior and must be
contracted where the endpoint lives. Reconnect timing, backoff schedule,
and the transport-agnostic client interface are *browser-client*
behavior; putting them in a backend component doc would make it own UI
behavior that EP-0006's stories
are the natural home for. The standard `Last-Event-ID` contract is
precisely the interface between the two halves.

## Alternatives Considered

- **CMP-0011 also specifies the
  client transport abstraction + reconnect/backoff**: rejected — puts all
  of ST-0059
  in one doc at the
  cost of a backend component owning cross-boundary UI-client behavior;
  the front/back split follows the `Last-Event-ID` seam cleanly.

## Implications

CMP-0011's SSE elements contract
only the server obligations and name the client half as an Out-of-Scope
boundary linking EP-0006. The
server-side `Last-Event-ID` resume remains a Constraint, not a Note, per
DEC-0213.
