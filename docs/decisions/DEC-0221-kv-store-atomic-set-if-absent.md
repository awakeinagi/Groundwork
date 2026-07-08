---
id: DEC-0221
type: decision
title: KV-store Port adds an atomic set-if-absent operation for coordination locks
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0041 @ T1-T2"
links:
  derives-from: [SES-0041]
  relates-to: [DEC-0203, DEC-0139]
  supersedes: []
---

# DEC-0221: KV-Store Port Adds Atomic Set-If-Absent

## Context

[ST-0062](../stories/ST-0062-kv-store-port.md)'s scope names
"single-writer coordination locks" as a use case, but a plain
`get()`-then-`set()` composition races: two callers can both observe
"absent" before either writes, both believing they acquired the lock.
A minimal `get`/`set`/`delete` surface cannot deliver the use case the
story's own scope names.

## Decision

The `KvStorePort` contract adds an atomic operation:
`set-if-absent(namespace, key, value, ttl) → acquired: bool`. It
succeeds and returns `true` only if no live (non-expired) value exists
at that key; otherwise it returns `false` without modifying the
existing value.

## Rationale

This is the minimal primitive that makes lock acquisition
race-free without pulling in a heavier mechanism (e.g. requiring
callers to use the App Database Port's UnitOfWork for what is meant to
be lightweight coordination state). It follows the same "typed
operation family, no caller-composed race" discipline the App Database
Port already established for its own atomicity guarantees
([DEC-0139](DEC-0139-port-operation-failure-semantics.md)).
