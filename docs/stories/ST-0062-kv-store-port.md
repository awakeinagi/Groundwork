---
id: ST-0062
type: story
title: KV-store port — protocol contract, conformance suite, app-database-reuse adapter
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Infrastructure seam for ephemeral coordination state and
  general-purpose caching: KV-store Port defined as a Protocol design
  element with conformance test suite and v1 default adapter reusing the
  App Database Port, supporting get/set/delete with TTL via
  lazy-on-read plus best-effort periodic sweep job, zero new deployment
  surface. Per DEC-0121, DEC-0122, DEC-0129, DEC-0203, DEC-0204,
  DEC-0211.
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
(DEC-0203).

## Acceptance Criteria

1. The KV-store Port is defined as a Protocol design element covering
   `get` / `set` / `delete` with TTL support, scoped to ephemeral
   coordination state (rate limiting, single-writer coordination locks,
   connection/session bookkeeping) and general-purpose caching (e.g.
   avoiding recomputation of graph query results)
   (per DEC-0203,
   DEC-0121).
2. Consumers program against the port contract only
   (per DEC-0121); the
   concrete Adapter is selected by deployment configuration
   (per DEC-0122,
   ST-0057).
3. A shared conformance test suite ships with the port; passing it is
   the definition of a valid Adapter
   (per DEC-0122,
   DEC-0203).
4. v1 ships a default Adapter that reuses the same DuckDB engine
   instance as the App Database Port's adapter
   (ST-0010) — its own KV table, zero
   new deployment surface — the same co-located-engine relationship
   already established between the app-database and vector-store
   ports (one DuckDB engine, separate Port contracts); it does not
   route through `AppDatabasePort`'s `bookkeeping` operation family or
   any other consumer-facing operation of that port, and no SQL
   crosses this port's own seam either
   (per DEC-0204,
   DEC-0121,
   DEC-0129),
   and it passes the conformance suite.
5. Expiry is lazy-on-read (`get()` on an expired key returns
   `not-found` immediately) plus a best-effort periodic sweep job
   running on the async runtime
   (ST-0061)
   (per DEC-0211).

## Component Impact

CMP-0014 — approved, its
own standalone `protocol`-type Component Doc, mirroring
CMP-0003's pattern
(per DEC-0203).

## Out of Scope

- The dedicated embedded KV-store library adapter alternate — deferred
  (ST-0064).
- Further use cases beyond coordination state and caching — tracked by
  a deferred spike
  (SP-0011), not
  scoped here.
- External adapters — deferred, evaluated by
  SP-0010.
- The periodic sweep runtime mechanics themselves —
  ST-0061; this story
  only requires that a sweep exists and reclaims expired rows.

## Notes for Implementers

TTL granularity and the sweep interval are implementation choices, not
load-bearing contract items — the contract only requires "expired
means unreadable via `get()`, and eventually reclaimed."
