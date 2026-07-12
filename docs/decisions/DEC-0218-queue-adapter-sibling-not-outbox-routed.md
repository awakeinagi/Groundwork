---
id: DEC-0218
type: decision
title: Queue Port's durable adapter is a sibling adapter on the co-located DuckDB engine, not routed through AppDatabasePort operations
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Queue Port's v1 durable adapter is a sibling adapter on the co-located
  DuckDB engine, not routed through AppDatabasePort operations. DEC-0210's
  "reuses the outbox pattern" refers to the retry/dead-letter/stale-lease
  semantics, not implementation on top of AppDatabasePort.A-2. Consistent
  with KV-store Port precedent: one engine instance, separate Port contracts,
  zero cross-port operation consumption.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0040 @ T3-T4"
links:
  derives-from: [SES-0040]
  relates-to: [DEC-0210, DEC-0129, DEC-0121]
  supersedes: []
---

# DEC-0218: Queue Adapter Is a Sibling on the Co-Located Engine

## Context

ST-0060 AC5 describes the v1
durable adapter as "a queue table riding the App Database Port" —
ambiguous between routing through `AppDatabasePort`'s outbox/
bookkeeping operations as its storage mechanism, or a sibling adapter
with its own table on the same co-located DuckDB engine instance. This
is the identical layering ambiguity
SES-0039 already
resolved for the KV-store Port
(ST-0062).

## Decision

The Queue Port's v1 durable adapter is a sibling adapter: its own
queue table on the same co-located DuckDB engine instance the App
Database Port's adapter uses, consuming none of
`AppDatabasePort`'s operation families. `DEC-0210`'s "reuses the outbox
pattern" means the *retry/dead-letter/stale-lease semantics* are
mirrored, not that the Queue adapter is implemented on top of
`AppDatabasePort.A-2`'s outbox operations. No SQL crosses the Queue
Port's own seam either
(per DEC-0129).

## Rationale

Consistent with the KV-store Port precedent settled in the same
refinement thread: one DuckDB engine instance, separate Port contracts,
zero cross-port operation consumption
(DEC-0121). Routing through
`AppDatabasePort`'s outbox family would couple Queue Port's conformance
to App Database Port internals and blur which port's conformance suite
is actually being exercised — the same reasoning that settled the
KV-store case.

## Alternatives Considered

At T3, the facilitator surfaced a layering ambiguity in ST-0060 AC5's description of the v1 durable adapter as "a queue table riding the App Database Port," posing two readings as alternatives: routing through `AppDatabasePort`'s outbox/bookkeeping operations as the storage mechanism, versus a sibling adapter with its own table on the same co-located DuckDB engine, consuming no `AppDatabasePort` operations. The facilitator recommended the sibling-adapter reading for consistency with the KV-store Port precedent just settled in the same refinement thread (SES-0039, ST-0062), and the stakeholder confirmed that recommendation at T4. (skeleton restored at SES-0078)

## Implications

The Queue Port's durable adapter consumes none of `AppDatabasePort`'s operation families; DEC-0210's phrase "reuses the outbox pattern" is clarified to mean only that the retry/dead-letter/stale-lease semantics are mirrored, not that the adapter is implemented on top of `AppDatabasePort.A-2`. No SQL crosses the Queue Port's own seam either, per DEC-0129, and this keeps the two ports' conformance suites cleanly separated rather than coupling Queue Port conformance to App Database Port internals. (skeleton restored at SES-0078)
