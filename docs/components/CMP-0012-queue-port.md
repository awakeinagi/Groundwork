---
id: CMP-0012
type: component
title: Queue Port
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: platform
component-type: protocol
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: []
cites: [DEC-0121, DEC-0122, DEC-0129, DEC-0135, DEC-0139, DEC-0152,
        DEC-0203, DEC-0204, DEC-0205, DEC-0206, DEC-0208, DEC-0210,
        DEC-0214, DEC-0215, DEC-0216, DEC-0217, DEC-0218]
---

# CMP-0012: Queue Port

> Standalone `protocol`-type component, mirroring
> [CMP-0003](CMP-0003-app-database-port.md)'s pattern per
> [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md)
> and extending the Port family per
> [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md).

## Purpose

The infrastructure seam for background/async job execution: the
contract any Queue Adapter must satisfy — enqueue / consume /
acknowledge / retry — plus the conformance suite that defines Adapter
validity. Consumers (the background job execution runtime,
[CMP-0013](CMP-0013-background-job-execution-runtime.md)) program
against this contract; adapters conform to it
([ST-0060](../stories/ST-0060-queue-port.md)).

## Ubiquitous Language

Port, Adapter — per [CONTEXT.md](../../CONTEXT.md). New terms: **Job**
(a unit of background work carrying a `job-type` and opaque payload),
**Lease** (a claim's time-bounded ownership of a job, mirroring the
App Database Port's outbox lease).

## Design Elements

### QueuePort (protocol)

Implements: [ST-0060](../stories/ST-0060-queue-port.md),
[ST-0061](../stories/ST-0061-background-job-execution-runtime.md)

- `QueuePort.A-1` — `enqueue(job-type, payload) → JobId`. `job-type` is
  an open string namespace — any value is accepted; the port does not
  validate it against a registry (per
  [DEC-0214](../decisions/DEC-0214-queue-job-type-open-namespace.md)).
  Typed error conditions: none beyond payload-shape validation
  (`Job.D-1`) (per
  [DEC-0217](../decisions/DEC-0217-queue-job-envelope-opaque-payload.md)).
- `QueuePort.A-2` — consume family: `claim(batch-size) → leased Job[]`;
  `ack(lease)`; `nack(lease, [reason])` for retry. Typed error
  conditions: `stale-lease` (expired or unknown lease on ack/nack),
  mirroring the App Database Port's outbox leasing discipline (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md),
  [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `QueuePort.A-3` — `status(job-id) → JobStatus | problem(not-found)`.
  Exposes current job state (`queued | running | retrying |
  dead-lettered`) so job progress is queryable, not only inferable from
  logs (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md)).
  No redrive/requeue operation exists on the port in v1 — dead-lettered
  jobs are visible via this operation only (per
  [DEC-0215](../decisions/DEC-0215-queue-dead-letter-terminal-v1.md)).
- `QueuePort.B-1` — consumers program against the port contract only;
  no consumer references an engine API directly (per
  [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
- `QueuePort.B-2` — no SQL crosses the seam; Adapters implement
  semantics, not a dialect; Adapter selection is deployment
  configuration only (per
  [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md),
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `QueuePort.B-3` — conformance: the shared suite exercises every
  operation family, including stale-lease and dead-letter failure
  injection; passing it is the definition of a valid Adapter (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `QueuePort.B-4` — stale-lease safety: `ack`/`nack` with an expired or
  unknown lease fails with `stale-lease` and the job remains (or
  becomes again) claimable — safe under at-least-once delivery because
  consumers are idempotent (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md),
  [DEC-0139](../decisions/DEC-0139-port-operation-failure-semantics.md)).
- `QueuePort.B-5` — dead-lettering: after a single deployment-wide
  configurable maximum of failed deliveries a job parks in a
  `dead-lettered` state, visible through `QueuePort.A-3` and never
  silently dropped; no port-level recovery operation exists in v1 (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md),
  [DEC-0215](../decisions/DEC-0215-queue-dead-letter-terminal-v1.md),
  [DEC-0216](../decisions/DEC-0216-queue-retry-bound-deployment-default.md)).
- `QueuePort.B-6` — delivery: at-least-once, with no ordering guarantee
  across jobs (including jobs of the same `job-type`); consumers are
  idempotent by contract (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md)).

### Job (value)

Implements: [ST-0060](../stories/ST-0060-queue-port.md)

- `Job.D-1` — schema: `job-id` (uuid), `job-type` (open string, per
  [DEC-0214](../decisions/DEC-0214-queue-job-type-open-namespace.md)),
  `payload` (opaque JSON document, uninterpreted by the port —
  meaningful only to the runtime's registered handler for that
  `job-type`), `attempt-count` (int), `enqueued-at` (timestamp);
  equality by value; immutable except for `attempt-count`, which the
  port increments on each claim (per
  [DEC-0217](../decisions/DEC-0217-queue-job-envelope-opaque-payload.md)).
- `Job.D-2` — `payload` never embeds secret material (API keys,
  tokens); a job needing a secret carries a reference (e.g. a
  connector/person id) resolved at execution time, consistent with
  secrets living envelope-encrypted in the app database rather than
  scattered across job payloads (per
  [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)).

### JobStatus (value)

Implements: [ST-0060](../stories/ST-0060-queue-port.md),
[ST-0061](../stories/ST-0061-background-job-execution-runtime.md)

- `JobStatus.D-1` — closed enum: `queued | running | retrying |
  dead-lettered`; queryable via `QueuePort.A-3` (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md)).

## Component Invariants

- `C-1` — at-least-once delivery only: no operation of this port ever
  promises exactly-once or cross-job ordering (per
  [DEC-0210](../decisions/DEC-0210-queue-port-outbox-pattern-reuse.md)).
- `C-2` — durability across a process restart is an Adapter-level
  property, not a port-level guarantee: the v1 durable Adapter provides
  it, but the contract does not require every Adapter to (per
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).

## Implementation Guidance

### Constraints

- `IG-1` — v1 ships a single durable Adapter only: a queue table on the
  same co-located DuckDB engine instance the App Database Port's
  adapter uses, as a sibling adapter — it consumes none of
  `AppDatabasePort`'s operation families and no SQL crosses this port's
  own seam either (per
  [DEC-0218](../decisions/DEC-0218-queue-adapter-sibling-not-outbox-routed.md),
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
- `IG-2` — the max-retry bound is a single deployment-wide configured
  value, set via the Composition Root's deployment configuration; no
  per-job override exists in `enqueue` (per
  [DEC-0216](../decisions/DEC-0216-queue-retry-bound-deployment-default.md),
  [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)).
- `IG-3` — the conformance suite is published with the port and runs
  against any Adapter without modification, including stale-lease and
  dead-letter failure injection (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).

### Notes

- Lease duration is an Adapter-level tuning knob, not a contract item —
  the contract only requires that an expired lease yields `stale-lease`
  on `ack`/`nack`.
- The ephemeral in-memory Adapter (deferred,
  [ST-0063](../stories/ST-0063-ephemeral-in-memory-queue-adapter.md))
  would satisfy this contract without `C-2`'s durability — a future
  conformance run, not a v1 obligation.

## Dependencies

None — this contract is a leaf. The v1 durable Adapter is a sibling
adapter on the same co-located DuckDB engine the App Database Port's
adapter uses, but consumes none of its contract sections (per
[DEC-0218](../decisions/DEC-0218-queue-adapter-sibling-not-outbox-routed.md)).

## Acceptance & Test Expectations

1. The conformance suite passes with the v1 durable Adapter (per
   [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
2. Failure-path conformance: stale-lease rejection with the job
   re-claimable, dead-letter parking after retry exhaustion with no
   port-level recovery path, and every enumerated typed error
   condition are exercised by the suite (per
   [DEC-0139](../decisions/DEC-0139-port-operation-failure-semantics.md),
   [DEC-0215](../decisions/DEC-0215-queue-dead-letter-terminal-v1.md)).
3. Durability: a process restart does not lose jobs queued or claimed
   against the v1 durable Adapter (per
   [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).

## Out of Scope

Boundary statements (per
[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)):

- The in-process runtime that consumes this port (claim/execute/ack
  dispatch loop, job-handler registration) —
  [CMP-0013](CMP-0013-background-job-execution-runtime.md), per the
  port/runtime story split
  ([DEC-0208](../decisions/DEC-0208-queue-port-runtime-split.md)).
- The ephemeral in-memory Adapter alternate — deferred
  ([ST-0063](../stories/ST-0063-ephemeral-in-memory-queue-adapter.md)).
- External Adapters (AWS SQS, etc.) — deferred behind
  `TRG-0001`/`TRG-0002`, evaluated by
  [SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md)
  (per
  [DEC-0205](../decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md)).
- Dead-letter redrive/recovery — no port operation exists for it in v1
  (per
  [DEC-0215](../decisions/DEC-0215-queue-dead-letter-terminal-v1.md));
  an operator-side or future gated addition, not tracked as a deferred
  artifact since no concrete need has surfaced yet.
- Per-job-type payload schema validation — the port treats `payload` as
  opaque; type-specific validation is the registered handler's concern
  ([CMP-0013](CMP-0013-background-job-execution-runtime.md)).
