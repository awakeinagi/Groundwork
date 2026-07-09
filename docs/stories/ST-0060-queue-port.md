---
id: ST-0060
type: story
title: Queue port — protocol contract, conformance suite, durable adapter
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0010]
  impacts: [ST-0057, ST-0061, ST-0063]
  impacted-by: []
cites: [DEC-0121, DEC-0122, DEC-0129, DEC-0135, DEC-0152, DEC-0203, DEC-0204,
        DEC-0208, DEC-0210, DEC-0139]
---

# ST-0060: Queue Port — Protocol Contract, Conformance Suite, Durable Adapter

## Summary

The infrastructure seam for background/async job execution: the Queue
Port defined as a Protocol design element, its conformance test suite,
and the v1 durable app-database-backed adapter — so enqueued work rides
a config-swappable contract instead of an engine API
(DEC-0203).

## Acceptance Criteria

1. The Queue Port is defined as a Protocol design element covering
   enqueue / consume / acknowledge / retry operations for
   background/async job execution, as typed operation families with no
   SQL crossing the seam — the same discipline the App Database Port
   already established
   (per DEC-0203,
   DEC-0121,
   DEC-0129).
2. Consumers program against the port contract only; no consumer
   references an engine API directly
   (per DEC-0121).
3. The concrete Adapter is selected by deployment configuration
   (per DEC-0122,
   ST-0057).
4. A shared conformance test suite ships with the port; passing it is
   the definition of a valid Adapter, for bundled and future adapters
   alike (per DEC-0122,
   DEC-0203).
5. v1 ships a durable adapter — a queue table riding the App Database
   Port (ST-0010) — so jobs survive a
   process restart, and it passes the conformance suite
   (per DEC-0204).
6. Failure semantics mirror the App Database Port's outbox pattern:
   bounded retries per job; `stale-lease` typed errors on ack/nack of an
   expired or unknown lease, with the job remaining/becoming claimable
   again; dead-letter parking after a configurable maximum of failed
   deliveries, visible through the port's bookkeeping surface and never
   silently dropped; at-least-once delivery with idempotent consumers
   (per DEC-0210,
   DEC-0139).
7. Job payloads never embed secret material (API keys, tokens); a job
   needing a secret carries a reference (e.g. a connector/person id)
   and resolves the actual value at execution time, consistent with
   secrets living envelope-encrypted in the app database rather than
   scattered across job payloads
   (per DEC-0152).

## Component Impact

CMP-0012 — approved, its own
standalone `protocol`-type Component Doc, mirroring
CMP-0003's pattern
(per DEC-0203,
DEC-0135).

## Out of Scope

- The in-process runtime that consumes this port —
  ST-0061 (split per
  DEC-0208).
- The ephemeral in-memory adapter alternate — deferred
  (ST-0063).
- External adapters (AWS SQS, etc.) — deferred, evaluated by
  SP-0009.

## Notes for Implementers

Write the conformance suite against the contract first, including
failure injection for stale-lease and dead-letter paths, then make the
durable adapter pass it — the same discipline
ST-0010 already established.
