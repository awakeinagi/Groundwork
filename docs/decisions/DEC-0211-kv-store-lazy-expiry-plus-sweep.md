---
id: DEC-0211
type: decision
title: KV-store Port v1 expiry is lazy-on-read plus a best-effort periodic sweep
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0039 @ T3-T4"
links:
  derives-from: [SES-0039]
  relates-to: [DEC-0203, DEC-0204]
  supersedes: []
---

# DEC-0211: KV-Store Expiry — Lazy Plus Periodic Sweep

## Context

DEC-0203 scoped the
KV-store Port to coordination state plus general-purpose caching, both
of which need TTL support; the expiry mechanism itself was undecided
going into story derivation.

## Decision

`get()` on an expired key returns `not-found` immediately (lazy check,
no separate expiry pass needed for correctness), and a best-effort
periodic sweep job — itself the first concrete job running on the new
async runtime
(ST-0061) —
reclaims expired rows so storage doesn't grow unbounded from keys that
are set and never read again.

## Rationale

Lazy expiry alone is correct but leaves storage growth unbounded for
write-heavy, read-rarely keys (a plausible profile for rate-limiting
counters); a periodic sweep bounds that without adding a second storage
mechanism — it's a job the Queue/runtime story already provides a home
for, at zero new infrastructure cost consistent with the v1 embedded
posture (DEC-0102).

## Alternatives Considered

- **Lazy only, no sweep**: simplest, but unbounded storage growth from
  unread expired keys is a real operational risk for a caching use case.
- **Active sweep only, no lazy check**: rejected — a key read between
  sweep intervals but past its TTL would incorrectly appear live.

## Implications

ST-0062's Acceptance Criteria
require both mechanisms; the sweep job is a concrete demonstration of
ST-0061's
runtime and is named in that story's Notes.
