---
id: CMP-0003
type: component
title: App Database Port
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Standalone protocol-type component, graduated from CMP-0001 per
  DEC-0135. Defines the infrastructure seam for relational/transactional
  workload behind the Canonical Store. Operations: UnitOfWork begin/commit,
  outbox append/claim/ack/nack for change-event emission, bookkeeping
  put/get/delete for derived state (branch metadata, worktree state, retry
  counters). No ID-counter state exposed; all state derived and
  rebuildable. DuckDB adapter in v1. Conformance suite published with
  contract.
context: canonical-store
component-type: protocol
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
cites: [DEC-0077, DEC-0080, DEC-0102, DEC-0103, DEC-0121, DEC-0122, DEC-0124,
        DEC-0125, DEC-0129, DEC-0131, DEC-0133, DEC-0135, DEC-0139]
---

# CMP-0003: App Database Port

> Standalone `protocol`-type component, graduated out of
> CMP-0001 per
> DEC-0135 under
> the DEC-0080
> rule: independently versioned conformance. The pattern for all four
> infrastructure ports of
> DEC-0121.

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

Implements: ST-0010,
ST-0008

- `AppDatabasePort.A-1` — `begin() → UnitOfWork` with atomic
  commit/rollback across all operations enlisted in it; typed error
  conditions: `unavailable`, `uow-closed` (operations on a committed or
  rolled-back unit) (per DEC-0129, DEC-0139).
- `AppDatabasePort.A-2` — outbox family: `outbox.append(events[],
  uow)`; `outbox.claim(batch-size) → leased events`;
  `outbox.ack(lease)` / `outbox.nack(lease)` for the dispatcher's retry
  loop. Event payloads conform to
  CMP-0002; typed error conditions:
  `stale-lease` (expired or unknown lease on ack/nack), `uow-closed`
  on append (per DEC-0103, DEC-0129, DEC-0139).
- `AppDatabasePort.A-3` — bookkeeping family:
  `bookkeeping.put/get/delete(namespace, key, document)` for
  operational records (worktree state, branch metadata, retry
  counters); no ID-counter surface exists on the port; typed error
  conditions: `not-found` on get/delete of an absent key (per DEC-0129,
  DEC-0125, DEC-0139).
- `AppDatabasePort.B-1` — atomicity: outbox append and the write's
  bookkeeping commit or roll back together within one UnitOfWork
  (per DEC-0103, DEC-0129).
- `AppDatabasePort.B-2` — no SQL crosses the seam; Adapters implement
  semantics, not a dialect; Adapter selection is deployment
  configuration only (per DEC-0129, DEC-0122).
- `AppDatabasePort.B-3` — conformance: the shared suite exercises every
  operation family, including UnitOfWork atomicity under failure
  injection; passing it is the definition of a valid Adapter
  (per DEC-0122).
- `AppDatabasePort.B-4` — stale-lease safety: `ack`/`nack` with an
  expired or unknown lease fails with `stale-lease` and the event
  remains (or becomes again) claimable — safe under at-least-once
  delivery because consumers are idempotent per
  CMP-0002's delivery contract
  (per DEC-0139).
- `AppDatabasePort.B-5` — dead-lettering: after a configurable maximum
  of failed deliveries an event parks in a dead-letter state, visible
  through the bookkeeping surface and never silently dropped;
  replay-from-git remains the ultimate recovery path
  (per DEC-0139, DEC-0103).
- `AppDatabasePort.B-6` — crash atomicity: a crash at any point inside
  a UnitOfWork leaves no partially visible state after restart;
  exercised by the conformance suite's failure injection
  (per DEC-0139, DEC-0129).

## Component Invariants

- `C-1` — all state behind the port is derived state: rebuildable from
  the fork's refs, never a source of truth (per DEC-0131, DEC-0103).

## Implementation Guidance

### Constraints

- `IG-1` — v1 ships the DuckDB Adapter only; second storage adapters
  arrive with the graduation evaluation
  (SP-0002)
  (per DEC-0124, DEC-0102).
- `IG-2` — the conformance suite is published with the port contract
  and runs against any Adapter without modification (per DEC-0122).

### Notes

- DuckDB's single-writer character matches the v1 single-process
  constraint; the Adapter should not simulate concurrency the engine
  does not have.

## Dependencies

- CMP-0002 — outbox rows carry ChangeEvent
  payloads; this port consumes only its schema (`ChangeEvent.D-1`).

## Acceptance & Test Expectations

1. The conformance suite passes with the v1 DuckDB Adapter
   (per DEC-0122, DEC-0124).
2. Atomicity under failure injection: a crash between bookkeeping write
   and outbox append leaves no half-committed unit of work
   (per DEC-0103, DEC-0129).
3. Failure-path conformance: stale-lease rejection with the event
   re-claimable, dead-letter parking after retry exhaustion, and every
   enumerated typed error condition are exercised by the suite
   (per DEC-0139).

## Out of Scope

Boundary statements (per DEC-0133):

- The other three infrastructure ports — vector store and embedding
  (EP-0007), graph
  store (EP-0004) — arrive as their
  own protocol CMPs per DEC-0135.
- Artifact-ID allocation state — excluded from the port; rescan-on-boot
  is the sole mechanism (per DEC-0125, DEC-0077).
- Dispatcher scheduling and retry policy — the consumer's concern
  (CMP-0001).
