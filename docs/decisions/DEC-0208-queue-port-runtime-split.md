---
id: DEC-0208
type: decision
title: Queue Port splits into a port-contract+adapter story and a separate async-runtime-consumer story
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T1-T2"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0203, DEC-0121, DEC-0122, DEC-0198]
  supersedes: []
---

# DEC-0208: Queue Port Splits from Its Runtime Consumer

## Context

[EP-0008](../epics/EP-0008-backend-application-platform.md) scoped both
the Queue Port (contract + v1 adapter) and the "runtime/async execution
model" (in-process asyncio background tasks running against it) as one
Scope bullet. This project already has a directly analogous precedent:
[ST-0010](../stories/ST-0010-app-database-port.md) (App Database Port
contract + DuckDB adapter) is a separate story from
[ST-0008](../stories/ST-0008-change-event-stream.md) (the dispatcher
that consumes it).

## Decision

The Queue Port splits into
[ST-0060](../stories/ST-0060-queue-port.md) — the Protocol contract,
conformance suite, and v1 durable app-database-backed adapter — and
[ST-0061](../stories/ST-0061-background-job-execution-runtime.md) — the
in-process asyncio runtime that enqueues, consumes, acknowledges, and
retries jobs against it.

## Rationale

Mirrors the project's own established seam
(port-contract-and-adapter vs. the consumer that rides it) rather than
inventing a new one. A Queue Port with no consumer isn't independently
demoable, but the contract's conformance suite is verifiable on its own
before any runtime consumes it — exactly [ST-0010](../stories/ST-0010-app-database-port.md)'s
shape.

## Alternatives Considered

- **Bundle into one story**: considered, since neither half is fully
  "valuable" alone by INVEST's letter — rejected in favor of consistency
  with this project's own precedent, which already answered this exact
  question for the app-database Port.

## Implications

[ST-0061](../stories/ST-0061-background-job-execution-runtime.md)
depends-on [ST-0060](../stories/ST-0060-queue-port.md).
[ST-0063](../stories/ST-0063-ephemeral-in-memory-queue-adapter.md) (the
deferred ephemeral adapter) is impacted-by
[ST-0060](../stories/ST-0060-queue-port.md)'s contract, not the runtime.
