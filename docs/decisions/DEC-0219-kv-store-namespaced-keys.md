---
id: DEC-0219
type: decision
title: KV-store Port keys are (namespace, key) pairs, mirroring AppDatabasePort's bookkeeping shape
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0041 @ T1-T2"
links:
  derives-from: [SES-0041]
  relates-to: [DEC-0129, DEC-0203]
  supersedes: []
---

# DEC-0219: KV-Store Keys Are Namespaced

## Context

CMP-0014 needed a key
shape before its `get`/`set`/`delete` operations could be specified: a
flat key string, or a `(namespace, key)` pair. The port's scoped use
cases — rate limiting, coordination locks, connection/session
bookkeeping, general-purpose caching — are unrelated consumers that
could otherwise collide on key names.

## Decision

Every `KvStorePort` operation addresses a `(namespace, key)` pair, not
a flat key — mirroring `AppDatabasePort.A-3`'s bookkeeping family
shape (`namespace, key, document`).

## Rationale

Reusing an already-established shape keeps the two ports' typed
operation families consistent
(DEC-0129) and gives each
consumer (rate limiter, lock, cache) a collision-free namespace without
inventing a new prefixing convention per caller.
