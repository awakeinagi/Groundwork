---
id: CMP-0014
type: component
title: KV-Store Port
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
cites: [DEC-0121, DEC-0122, DEC-0129, DEC-0135, DEC-0139, DEC-0203,
        DEC-0204, DEC-0205, DEC-0211, DEC-0219, DEC-0220, DEC-0221]
---

# CMP-0014: KV-Store Port

> Standalone `protocol`-type component, mirroring
> [CMP-0003](CMP-0003-app-database-port.md)'s pattern per
> [DEC-0135](../decisions/DEC-0135-graduate-app-database-port.md)
> and extending the Port family per
> [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md).

## Purpose

The infrastructure seam for ephemeral coordination state and
general-purpose caching: the contract any KV-store Adapter must
satisfy — `get`/`set`/`delete`/`set-if-absent`, all TTL-scoped — plus
the conformance suite that defines Adapter validity. v1 ships a default
Adapter reusing the App Database Port's DuckDB engine instance
([ST-0062](../stories/ST-0062-kv-store-port.md)).

## Ubiquitous Language

Port, Adapter — per [CONTEXT.md](../../CONTEXT.md). No new terms
introduced; `namespace`/`key` reuse the shape
`AppDatabasePort.A-3`'s bookkeeping family already established.

## Design Elements

### KvStorePort (protocol)

Implements: [ST-0062](../stories/ST-0062-kv-store-port.md)

- `KvStorePort.A-1` — `get(namespace, key) → value |
  problem(not-found)`. Returns `not-found` immediately for an expired
  key — lazy expiry, no separate pass required for correctness (per
  [DEC-0211](../decisions/DEC-0211-kv-store-lazy-expiry-plus-sweep.md),
  [DEC-0219](../decisions/DEC-0219-kv-store-namespaced-keys.md)).
- `KvStorePort.A-2` — `set(namespace, key, value, ttl)`. `ttl` is a
  required parameter — no no-expiry variant exists (per
  [DEC-0220](../decisions/DEC-0220-kv-store-ttl-mandatory.md)).
  Overwrites any existing (live or expired) value at that key.
- `KvStorePort.A-3` — `delete(namespace, key)`. Idempotent: deleting an
  absent or already-expired key is not an error.
- `KvStorePort.A-4` — `set-if-absent(namespace, key, value, ttl) →
  acquired: bool`. Atomic: succeeds and returns `true` only if no live
  (non-expired) value exists at that key; otherwise returns `false`
  without modifying the existing value. The primitive that makes
  single-writer coordination locks race-free (per
  [DEC-0221](../decisions/DEC-0221-kv-store-atomic-set-if-absent.md)).
- `KvStorePort.B-1` — consumers program against the port contract
  only; no consumer references an engine API directly (per
  [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
- `KvStorePort.B-2` — no SQL crosses the seam; Adapter selection is
  deployment configuration only (per
  [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md),
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `KvStorePort.B-3` — conformance: the shared suite exercises every
  operation family, including `set-if-absent` under concurrent
  contention and expiry behavior at the TTL boundary; passing it is
  the definition of a valid Adapter (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `KvStorePort.B-4` — expiry: `get()` on an expired key returns
  `not-found` immediately (lazy check); a best-effort periodic sweep
  job reclaims expired rows so storage doesn't grow unbounded from
  write-heavy, read-rarely keys — the sweep is best-effort, not a
  correctness requirement (per
  [DEC-0211](../decisions/DEC-0211-kv-store-lazy-expiry-plus-sweep.md)).
- `KvStorePort.B-5` — every key is TTL-scoped; the port defines no
  mechanism for a permanent key. A consumer needing permanent state
  uses the App Database Port instead (per
  [DEC-0220](../decisions/DEC-0220-kv-store-ttl-mandatory.md)).

## Component Invariants

- `C-1` — atomicity of `set-if-absent`: under concurrent callers
  racing the same `(namespace, key)`, exactly one call observes
  `acquired: true` for any given live-value window (per
  [DEC-0221](../decisions/DEC-0221-kv-store-atomic-set-if-absent.md)).
- `C-2` — no cross-key ordering or transactional guarantee spans
  multiple keys; each operation is scoped to exactly one `(namespace,
  key)` (per
  [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).

## Implementation Guidance

### Constraints

- `IG-1` — v1 ships a single default Adapter: its own table on the
  same co-located DuckDB engine instance the App Database Port's
  adapter uses, as a sibling adapter — it consumes none of
  `AppDatabasePort`'s operation families and no SQL crosses this
  port's own seam either (per
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md),
  [DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)).
- `IG-2` — the conformance suite is published with the port and runs
  against any Adapter without modification, including `set-if-absent`
  contention and TTL-boundary expiry behavior (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).

### Notes

- Sweep interval and TTL granularity are implementation choices, not
  load-bearing contract items — the contract only requires "expired
  means unreadable via `get()`, and eventually reclaimed" (per
  [DEC-0211](../decisions/DEC-0211-kv-store-lazy-expiry-plus-sweep.md)).
- The periodic expiry sweep runs as a named job on the background job
  execution runtime
  ([CMP-0013](CMP-0013-background-job-execution-runtime.md)): the
  v1 default Adapter registers its sweep handler via
  `JobRuntime.A-1` at its own startup (per
  [DEC-0222](../decisions/DEC-0222-runtime-owns-handler-registration.md));
  this port's own contract does not depend on that runtime.

## Dependencies

None — this contract is a leaf. The v1 default Adapter is a sibling
adapter on the same co-located DuckDB engine the App Database Port's
adapter uses, but consumes none of its contract sections (per
[DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).

## Acceptance & Test Expectations

1. The conformance suite passes with the v1 default Adapter (per
   [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
2. Concurrency conformance: `set-if-absent` under concurrent contention
   on the same `(namespace, key)` yields exactly one `acquired: true`
   (per
   [DEC-0221](../decisions/DEC-0221-kv-store-atomic-set-if-absent.md)).
3. Expiry conformance: `get()` on an expired key returns `not-found`
   immediately, independent of whether the periodic sweep has run yet
   (per
   [DEC-0211](../decisions/DEC-0211-kv-store-lazy-expiry-plus-sweep.md)).

## Out of Scope

Boundary statements (per
[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)):

- The dedicated embedded KV-store library Adapter alternate — deferred
  ([ST-0064](../stories/ST-0064-dedicated-embedded-kv-library-adapter.md)).
- Further use cases beyond coordination state and caching — tracked by
  a deferred spike
  ([SP-0011](../spikes/SP-0011-kv-store-use-case-discovery.md)).
- External Adapters — deferred behind `TRG-0001`/`TRG-0002`, evaluated
  by
  [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md)
  (per
  [DEC-0205](../decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md)).
- The periodic sweep job's runtime mechanics (dispatch loop, handler
  registration) —
  [CMP-0013](CMP-0013-background-job-execution-runtime.md); this port
  only requires that a sweep exists and reclaims expired rows.
- Permanent (non-expiring) storage — out of scope by design
  ([DEC-0220](../decisions/DEC-0220-kv-store-ttl-mandatory.md)); use
  the App Database Port
  ([CMP-0003](CMP-0003-app-database-port.md)) instead.
