---
id: DEC-0220
type: decision
title: KV-store Port TTL is mandatory on every set() — no permanent keys
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0041 @ T1-T2"
links:
  derives-from: [SES-0041]
  relates-to: [DEC-0203, DEC-0211]
  supersedes: []
---

# DEC-0220: KV-Store TTL Is Mandatory

## Context

[DEC-0203](DEC-0203-queue-kv-ports-added.md) scopes the KV-store Port
to *ephemeral* coordination state and caching. Whether `set()` requires
a TTL, or allows a permanent (no-expiry) key, was undecided going into
contract drafting.

## Decision

`set(namespace, key, value, ttl)` requires a TTL on every call; the
port contract defines no no-expiry variant. A caller wanting permanent
state uses the App Database Port's bookkeeping family instead.

## Rationale

Making TTL mandatory structurally enforces the port's declared
ephemeral-only scope rather than relying on convention — an
implementer cannot accidentally grow a second permanent store behind
this seam. It also keeps the lazy-plus-sweep expiry mechanism
([DEC-0211](DEC-0211-kv-store-lazy-expiry-plus-sweep.md)) universally
applicable: every key is eventually reclaimable, with no carve-out to
special-case.
