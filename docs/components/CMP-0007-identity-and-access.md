---
id: CMP-0007
type: component
title: Identity & Access
status: draft
owner: eng-lead
created: 2026-07-08
context: integration
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0003, CMP-0005]
---

# CMP-0007: Identity & Access

## Purpose

Who anyone is, and how the system acts for them: the pluggable
auth-provider protocol with the v1 email/OIDC provider
([DEC-0024](../decisions/DEC-0024-pluggable-auth.md)), person-id
resolution and role claims from the person registry
([DEC-0046](../decisions/DEC-0046-person-registry.md)), OAuth
host-identity linkage over the encrypted secret store
([DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)),
and delegated-review posting with the signed attribution block
([DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md),
[DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition follows story approval
([ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md),
[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)).
The attribution-block schema is a known graduation candidate — consumed
by [CMP-0004](CMP-0004-governance-gate-engine.md) for verification
(per [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

Consumes [CMP-0003](CMP-0003-app-database-port.md) (encrypted secret
storage, per [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md))
and [CMP-0005](CMP-0005-code-host-connector-protocol.md) (review
posting operations); exact consumed sections declared at contract time.

## Pending — Acceptance & Test Expectations

## Pending — Out of Scope
