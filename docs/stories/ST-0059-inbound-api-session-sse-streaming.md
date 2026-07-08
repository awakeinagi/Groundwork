---
id: ST-0059
type: story
title: Inbound API — session SSE streaming with reconnect/resume
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0058, ST-0032]
  impacts: [ST-0043, ST-0044]
  impacted-by: [ST-0057, ST-0032]
cites: [DEC-0182, DEC-0187, DEC-0202, DEC-0207, DEC-0212, DEC-0213]
---

# ST-0059: Inbound API — Session SSE Streaming with Reconnect/Resume

## Summary

The streaming half of the Inbound API
([DEC-0207](../decisions/DEC-0207-inbound-api-rest-sse-split.md)):
Server-Sent Events for
[ST-0032](ST-0032-session-engine-lifecycle-and-contract.md)'s
append-turn output, with automatic reconnect and resume so a network
blip never drops or duplicates a stakeholder's session turns
([DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).

## Acceptance Criteria

1. An SSE endpoint streams append-turn output for an open session; user
   turns are sent as plain POSTs through
   [ST-0058](ST-0058-inbound-api-rest-and-gate-surface.md)'s REST
   routes, not over the SSE channel
   (per [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).
2. The client is built behind a transport-agnostic interface; v1 ships
   the SSE implementation and the abstraction, not a WebSocket
   implementation (per [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).
3. On a dropped connection, the client reconnects automatically with
   backoff and resumes the stream from the last-seen SSE event id
   (`Last-Event-ID`), with no turn dropped or duplicated in the
   rendered conversation
   (per [DEC-0213](../decisions/DEC-0213-sse-reconnect-resume-contract.md)).
4. Streamed events carry enough structure for
   [ST-0043](ST-0043-session-progress-and-lifecycle-shell.md)/[ST-0044](ST-0044-session-conversation-ux.md)
   to render partial agent output incrementally as it's produced, not
   only a completed turn.
5. Every non-2xx response on the SSE endpoint's setup/handshake path
   (e.g. session not found, unauthenticated) follows
   [ST-0058](ST-0058-inbound-api-rest-and-gate-surface.md)'s
   problem+json convention
   (per [DEC-0212](../decisions/DEC-0212-inbound-api-reuses-problem-json.md)).
6. A reconnect-and-resume does not reset or extend the session's
   inactivity clock beyond what the underlying streamed turn already
   does — reconnecting mid-turn is transport recovery, not a new
   activity signal, and never causes the session to auto-close
   mid-turn
   (per [DEC-0182](../decisions/DEC-0182-streaming-turn-resets-inactivity-clock.md)).

## Component Impact

[CMP-0011](../components/CMP-0011-inbound-api.md) — stubbed, contract
pending.

## Out of Scope

- A WebSocket implementation of the transport interface — deferred; the
  interface exists, the implementation doesn't
  (per [DEC-0187](../decisions/DEC-0187-sse-default-pluggable-websocket.md)).
- Non-streaming REST routes —
  [ST-0058](ST-0058-inbound-api-rest-and-gate-surface.md).
- Session engine internals (turn storage, guardrails, distillation) —
  [ST-0032](ST-0032-session-engine-lifecycle-and-contract.md) and
  siblings, [EP-0002](../epics/EP-0002-refinement-session-agent.md).

## Notes for Implementers

`Last-Event-ID` resume relies on the session engine assigning stable,
monotonically ordered event ids per session
([ST-0032](ST-0032-session-engine-lifecycle-and-contract.md)); this
story consumes that ordering, it doesn't define it.
