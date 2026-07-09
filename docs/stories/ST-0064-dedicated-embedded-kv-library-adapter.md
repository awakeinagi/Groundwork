---
id: ST-0064
type: story
title: Dedicated embedded KV-store library adapter (deferred alternate)
status: deferred
release: "backlog"
owner: eng-lead
created: 2026-07-08
overview: >-
  Deferred to backlog. Dedicated embedded KV-store library (e.g.
  diskcache) as alternate Adapter for the KV-store Port—a real option
  but not the v1 default. Documents trade-offs against the default
  (separate storage file, no shared transaction/UnitOfWork scope),
  satisfies expiry contract by whatever mechanism the library provides,
  and passes the conformance suite when built. Per DEC-0204, DEC-0211.
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0062]
  impacts: []
  impacted-by: [ST-0062]
cites: [DEC-0204, DEC-0211]
---

# ST-0064: Dedicated Embedded KV-Store Library Adapter (Deferred Alternate)

## Summary

A dedicated embedded KV library (e.g. `diskcache`) as an alternate
Adapter for the KV-store Port
(ST-0062) — a real option, but not the v1
default, and not built in v1
(per DEC-0204).

## Acceptance Criteria

1. Passes the KV-store Port's conformance suite
   (ST-0062) like any other Adapter, when
   built.
2. Documents its trade-offs against the default (separate storage file
   from the app database, no shared transaction/UnitOfWork scope with
   app-database writes).
3. Satisfies ST-0062's expiry contract
   (`get()` on an expired key returns `not-found`, eventually reclaimed)
   by whatever mechanism the library provides — its own native
   TTL/eviction may substitute for the default adapter's lazy-check-
   plus-sweep mechanism, provided the observable contract holds under
   the conformance suite
   (per DEC-0211).

## Component Impact

None — deferred; no Component Doc work occurs until revived.

## Out of Scope

The app-database-reuse v1 default adapter —
ST-0062.

## Notes for Implementers

Not subscribed to `TRG-0001`/`TRG-0002` — those triggers govern
graduation to *external* adapters, not the choice between two embedded
options. Revive manually if a concrete need surfaces
(per DEC-0204).
