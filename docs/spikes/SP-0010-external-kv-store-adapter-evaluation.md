---
id: SP-0010
type: spike
title: External KV-store adapter evaluation
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
overview: >-
  Question: when TRG-0001 or TRG-0002 fires, which external KV-store
  adapter (Redis/ElastiCache, Memcached, other) best serves coordination
  state and caching, and how does data migrate from embedded,
  app-database-backed KV table? Blocks no current work; on trigger
  firing, it blocks multi-node deployment (coordination and locks must
  be shared across instances) and any caching-dependent story. Method
  establishes which trigger fired and its demands, prototypes KV-store
  Port contract (get/set/delete/TTL) against leading candidate,
  verifies cross-instance coordination correctness, evaluates operational
  overhead and cost against alternatives, defines migration path for
  existing coordination/cache state and rollback. Deferred to backlog;
  revived by TRG-0001 or TRG-0002. Findings pending.
timebox: 3d
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  relates-to: [SP-0009]
cites: [DEC-0023, DEC-0100, DEC-0204, DEC-0205]
---

# SP-0010: External KV-Store Adapter Evaluation

> Deferred to `backlog` at creation (per
> DEC-0205,
> the deferral citation per
> DEC-0100).
> Subscribed to triggers `TRG-0001` and `TRG-0002` — either firing
> revives it.

## Question

When `TRG-0001` or `TRG-0002` fires, which external KV-store adapter
(Redis/ElastiCache, Memcached, other) best serves the coordination-state
and caching workload — and how does data migrate from the embedded,
app-database-backed KV table
(DEC-0204)?

## Why It Blocks

Nothing today — that is why it is deferred. On a trigger firing, it
blocks multi-node deployment (coordination state and locks must be
shared across instances, which an embedded single-writer KV table cannot
do) and any caching-dependent story.

## Method

1. Establish which trigger fired and what it demands.
2. Prototype the KV-store Port contract (get / set / delete / TTL)
   against the leading candidate; verify cross-instance coordination
   correctness specifically (locks, not just cache hits/misses).
3. Evaluate operational overhead and cost against alternatives.
4. Define the migration path for existing coordination/cache state and
   the rollback story.
5. Record the adapter choice and migration plan as Decisions, per
   DEC-0023.

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — at minimum: the adapter choice and the migration approach.
