---
id: CMP-0003
type: component
title: App Database Port
status: gated
owner: eng-lead
created: 2026-07-08
context: canonical-store
component-type: protocol
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
cites: [DEC-0077, DEC-0080, DEC-0102, DEC-0103, DEC-0121, DEC-0122, DEC-0124,
        DEC-0125, DEC-0129, DEC-0135]
---

# CMP-0003: App Database Port

> Standalone `protocol`-type component, graduated out of
> [CMP-0001](CMP-0001-artifact-store-service.md) per
> [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md) under
> the [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)
> rule: independently versioned conformance. The pattern for all four
> infrastructure ports of
> [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md).

## Purpose

The infrastructure seam for the Canonical Store's
relational/transactional workload: the contract any app-database
Adapter must satisfy, and the conformance suite that defines Adapter
validity. Consumers program against this contract; engines adapt to it.

## Ubiquitous Language

Port, Adapter, Mechanical Write, Canonical Store — per
[CONTEXT.md](../../CONTEXT.md). No new terms introduced.

## Design Elements

### AppDatabasePort (protocol)

Implements: [ST-0010](../stories/ST-0010-app-database-port.md),
[ST-0008](../stories/ST-0008-change-event-stream.md)

- `AppDatabasePort.A-1` — `begin() → UnitOfWork` with atomic
  commit/rollback across all operations enlisted in it (per [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `AppDatabasePort.A-2` — outbox family: `outbox.append(events[],
  uow)`; `outbox.claim(batch-size) → leased events`;
  `outbox.ack(lease)` / `outbox.nack(lease)` for the dispatcher's retry
  loop. Event payloads conform to
  [CMP-0002](CMP-0002-change-event.md) (per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md), [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `AppDatabasePort.A-3` — bookkeeping family:
  `bookkeeping.put/get/delete(namespace, key, document)` for
  operational records (worktree state, branch metadata, retry
  counters); no ID-counter surface exists on the port (per [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md),
  [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md)).
- `AppDatabasePort.B-1` — atomicity: outbox append and the write's
  bookkeeping commit or roll back together within one UnitOfWork
  (per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md), [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `AppDatabasePort.B-2` — no SQL crosses the seam; Adapters implement
  semantics, not a dialect; Adapter selection is deployment
  configuration only (per [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md), [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `AppDatabasePort.B-3` — conformance: the shared suite exercises every
  operation family, including UnitOfWork atomicity under failure
  injection; passing it is the definition of a valid Adapter
  (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).

## Component Invariants

- `C-1` — all state behind the port is derived state: rebuildable from
  the fork's refs, never a source of truth (per [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md), [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md)).

## Implementation Guidance

### Constraints

- `IG-1` — v1 ships the DuckDB Adapter only; second storage adapters
  arrive with the graduation evaluation
  ([SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md))
  (per [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md), [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)).
- `IG-2` — the conformance suite is published with the port contract
  and runs against any Adapter without modification (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).

### Notes

- DuckDB's single-writer character matches the v1 single-process
  constraint; the Adapter should not simulate concurrency the engine
  does not have.

## Dependencies

- [CMP-0002](CMP-0002-change-event.md) — outbox rows carry ChangeEvent
  payloads; this port consumes only its schema (`ChangeEvent.D-1`).

## Acceptance & Test Expectations

1. The conformance suite passes with the v1 DuckDB Adapter
   (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md), [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
2. Atomicity under failure injection: a crash between bookkeeping write
   and outbox append leaves no half-committed unit of work
   (per [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md), [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).

## Out of Scope

Boundary statements (per [DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)):

- The other three infrastructure ports — vector store and embedding
  ([EP-0007](../epics/EP-0007-consolidation-memory-layer.md)), graph
  store ([EP-0004](../epics/EP-0004-graph-index.md)) — arrive as their
  own protocol CMPs per [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md).
- Artifact-ID allocation state — excluded from the port; rescan-on-boot
  is the sole mechanism (per [DEC-0125](../decisions/DEC-0125-port-counters-exclude-id-allocation.md), [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)).
- Dispatcher scheduling and retry policy — the consumer's concern
  ([CMP-0001](CMP-0001-artifact-store-service.md)).
