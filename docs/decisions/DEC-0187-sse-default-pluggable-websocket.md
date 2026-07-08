---
id: DEC-0187
type: decision
title: SSE is the default streaming transport, behind a client abstraction that also supports WebSockets
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0034 @ T2-T3"
links:
  derives-from: [SES-0034]
  relates-to: [DEC-0184]
  supersedes: []
---

# DEC-0187: SSE Default, Pluggable WebSocket Support

## Context

[ST-0032](../stories/ST-0032-session-engine-lifecycle-and-contract.md)
AC5 requires turn append to be streaming-capable so a consuming UI can
render partial agent output as it's produced. The v1 package needs a
concrete transport assumption, but the sponsor also wants room for
bidirectional needs (presence, typing indicators) without a later
transport migration.

## Decision

The package's session-engine client defaults to Server-Sent Events for
streaming agent output, with user turns sent as plain POSTs. The client
is built behind a transport-agnostic interface so a deployment can swap
in a WebSocket implementation without changing component APIs; v1 ships
the SSE implementation and the abstraction, not a WebSocket
implementation.

## Rationale

SSE fits append-turn's actual v1 shape (one-way agent-output streaming,
simple POSTs for user turns) with the least infrastructure — plain HTTP,
works through most proxies/CDNs, no connection-lifecycle/reconnect
machinery to build. Hiding it behind a swappable client interface
captures the sponsor's bidirectional-future intent without paying
WebSocket's infrastructure cost in v1.

## Alternatives Considered

- **WebSockets from the start**: bidirectional from day one, but v1 has
  no bidirectional requirement — the infrastructure (connection
  lifecycle, reconnect/backoff) would be unused complexity.
- **Leave the transport as an implementer detail**: fails to give the
  component-doc contract a concrete shape to define (event schema,
  reconnect/backoff behavior, partial-turn rendering contract).

## Implications

Component docs for this bounded context must define the transport
interface (the swap point) and the SSE implementation's event schema as
part of the package's contract; a future WebSocket implementation is a
new, additive implementation of the same interface, not a breaking
change.
