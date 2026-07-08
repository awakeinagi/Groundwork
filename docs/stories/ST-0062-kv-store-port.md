---
id: ST-0062
type: story
title: KV-store port — protocol contract, conformance suite, app-database-reuse adapter
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0010]
  impacts: [ST-0057, ST-0064]
  impacted-by: []
cites: [DEC-0121, DEC-0122, DEC-0129, DEC-0203, DEC-0204, DEC-0211]
---

# ST-0062: KV-Store Port — Protocol Contract, Conformance Suite, App-Database-Reuse Adapter

## Summary

The infrastructure seam for ephemeral coordination state and
general-purpose caching: the KV-store Port defined as a Protocol design
element, its conformance test suite, and the v1 default adapter that
reuses the App Database Port rather than adding new deployment surface
([DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)).

## Acceptance Criteria

1. The KV-store Port is defined as a Protocol design element covering
   `get` / `set` / `delete` with TTL support, scoped to ephemeral
   coordination state (rate limiting, single-writer coordination locks,
   connection/session bookkeeping) and general-purpose caching (e.g.
   avoiding recomputation of graph query results)
   (per [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md),
   [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
2. Consumers program against the port contract only
   (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)); the
   concrete Adapter is selected by deployment configuration
   (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
   [ST-0057](ST-0057-composition-root.md)).
3. A shared conformance test suite ships with the port; passing it is
   the definition of a valid Adapter
   (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
   [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)).
4. v1 ships a default Adapter that reuses the same DuckDB engine
   instance as the App Database Port's adapter
   ([ST-0010](ST-0010-app-database-port.md)) — its own KV table, zero
   new deployment surface — the same co-located-engine relationship
   already established between the app-database and vector-store
   ports (one DuckDB engine, separate Port contracts); it does not
   route through `AppDatabasePort`'s `bookkeeping` operation family or
   any other consumer-facing operation of that port, and no SQL
   crosses this port's own seam either
   (per [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md),
   [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
   [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)),
   and it passes the conformance suite.
5. Expiry is lazy-on-read (`get()` on an expired key returns
   `not-found` immediately) plus a best-effort periodic sweep job
   running on the async runtime
   ([ST-0061](ST-0061-background-job-execution-runtime.md))
   (per [DEC-0211](../decisions/DEC-0211-kv-store-lazy-expiry-plus-sweep.md)).

## Component Impact

[CMP-0014](../components/CMP-0014-kv-store-port.md) — stubbed as its
own standalone `protocol`-type Component Doc, mirroring
[CMP-0003](../components/CMP-0003-app-database-port.md)'s pattern
(per [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)),
contract pending.

## Out of Scope

- The dedicated embedded KV-store library adapter alternate — deferred
  ([ST-0064](ST-0064-dedicated-embedded-kv-library-adapter.md)).
- Further use cases beyond coordination state and caching — tracked by
  a deferred spike
  ([SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md)), not
  scoped here.
- External adapters — deferred, evaluated by
  [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md).
- The periodic sweep runtime mechanics themselves —
  [ST-0061](ST-0061-background-job-execution-runtime.md); this story
  only requires that a sweep exists and reclaims expired rows.

## Notes for Implementers

TTL granularity and the sweep interval are implementation choices, not
load-bearing contract items — the contract only requires "expired
means unreadable via `get()`, and eventually reclaimed."
