---
id: DEC-0237
type: decision
title: CMP-0007 owns the OAuth host-identity linking flow end-to-end
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T3-T4"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0043, DEC-0046, DEC-0174]
---

# DEC-0237: Identity-Owned OAuth Linking

## Context

[ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md)
AC6 requires an expired/revoked OAuth token to fail a review post
with a re-authorization prompt; someone must own the linking dance
(authorize URL, callback exchange, token storage).
[CMP-0009](../components/CMP-0009-github-connector.md) already
declares token issuance and OAuth linkage out of scope as "identity's
concern" ([DEC-0174](DEC-0174-github-connector-identity-architecture.md)).

## Decision

[CMP-0007](../components/CMP-0007-identity-and-access.md) owns the
flow end-to-end: `begin_link(person-id, host) → authorize-url` and
`complete_link(state, callback-params)` finishing the exchange and
storing the token in the secret store
([CMP-0015](../components/CMP-0015-secret-store.md)).
[CMP-0011](../components/CMP-0011-inbound-api.md) exposes the HTTP
callback route and delegates immediately.

## Rationale

Matches the boundary the approved connector already drew; host-OAuth
specifics stay out of the generic API component.

## Alternatives Considered

- **[CMP-0011](../components/CMP-0011-inbound-api.md) drives the flow, [CMP-0007](../components/CMP-0007-identity-and-access.md) stores the result**: fewer
  hops, but leaks host-OAuth mechanics into the API layer.

## Implications

The `HostIdentityLink` entity carries the linking lifecycle; [CMP-0011](../components/CMP-0011-inbound-api.md)
gains no OAuth logic beyond the delegating route it already models.
