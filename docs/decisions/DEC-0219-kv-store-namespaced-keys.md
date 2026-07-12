---
id: DEC-0219
type: decision
title: KV-store Port keys are (namespace, key) pairs, mirroring AppDatabasePort's bookkeeping shape
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Every KvStorePort operation addresses a (namespace, key) pair, mirroring
  AppDatabasePort.A-3's bookkeeping family shape (namespace, key, document).
  This keeps the two ports' typed operation families consistent and gives each
  unrelated consumer (rate limiter, lock, cache) a collision-free namespace
  without inventing per-caller prefixing conventions.
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

## Alternatives Considered

The facilitator's Round 1 question set posed a flat `key` string as the alternative to a `(namespace, key)` pair for KvStorePort. The `(namespace, key)` recommendation was given instead so that the port's unrelated scoped consumers — rate limiting, coordination locks, and caching — cannot collide on key names, and the stakeholder confirmed the recommendation as given. (skeleton restored at SES-0078)

## Implications

Mirroring `AppDatabasePort.A-3`'s bookkeeping family shape (`namespace, key, document`) keeps the two ports' typed operation families consistent with one another. Each unrelated consumer of the KV-store Port — rate limiter, lock, cache — gets a collision-free namespace without needing to invent its own per-caller prefixing convention. (skeleton restored at SES-0078)
