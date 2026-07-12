---
id: DEC-0220
type: decision
title: KV-store Port TTL is mandatory on every set() — no permanent keys
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  set(namespace, key, value, ttl) requires a TTL on every call; the KvStorePort
  contract defines no no-expiry variant. Mandatory TTL structurally enforces
  the port's ephemeral-only scope, preventing implementers from accidentally
  growing a second permanent store. It also keeps lazy-plus-sweep expiry
  universally applicable since every key is eventually reclaimable.
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

DEC-0203 scopes the KV-store Port
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
(DEC-0211) universally
applicable: every key is eventually reclaimable, with no carve-out to
special-case.

## Alternatives Considered

The facilitator's Round 1 question set (T1) framed the TTL requirement as a binary choice between making TTL mandatory on every `set()` call and leaving it optional so that no-TTL keys could live forever; the optional, permanent-key path was weighed and set aside because it would let the port drift into a second permanent store, undermining the ephemeral-only scope DEC-0203 established. The stakeholder confirmed the mandatory-TTL recommendation as given (T2), settling the point with no further alternative raised. (skeleton restored at SES-0078)

## Implications

Every caller of `set()` must supply an explicit TTL, and the contract provides no way to create a key that never expires; a caller that needs permanent state must instead use the App Database Port's bookkeeping family. This also means the lazy-plus-sweep expiry mechanism (DEC-0211) can apply uniformly to every key in the store, since none are exempt from eventual reclamation. (skeleton restored at SES-0078)
