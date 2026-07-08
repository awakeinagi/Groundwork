---
id: DEC-0153
type: decision
title: Program-user reviews carry a service-signed attribution block that gate-policy verifies
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T4-T5"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0043, DEC-0046]
---

# DEC-0153: Service-Signed Attribution Block

## Context

[DEC-0043](DEC-0043-oauth-reviews-program-user-fallback.md) requires
program-user reviews to carry the human approver's identity
"cryptographically attributed", with the `gate-policy` check verifying
it — the concrete scheme was left as story-level design and flagged as
an open question on
[EP-0005](../epics/EP-0005-connectors-and-identity.md).

## Decision

The review body carries a structured **attribution block** — person-id,
PR reference, decision timestamp — signed by a service-held asymmetric
key (Ed25519-class). The public key is deployment configuration; the
private key lives in the secret store
([DEC-0152](DEC-0152-secrets-encrypted-in-app-database.md)). The
`gate-policy` check verifies the signature and that the person-id
resolves in `governance/people.yaml`
([DEC-0046](DEC-0046-person-registry.md)) to a holder of the required
role.

## Rationale

Forgery requires the service's private key, not merely Bitbucket
access; asymmetric signing means the verifying check holds only the
public key, so verification capability never implies forging
capability.

## Alternatives Considered

- **HMAC with a shared secret**: simpler crypto, but anything that can
  verify can also forge.
- **Unsigned block + event-log cross-check**: no key management, but the
  governance event log's telemetry grade
  ([DEC-0144](DEC-0144-two-grade-governance-event-log.md)) is too weak
  an enforcement anchor.

## Implications

The block schema is a contract item of the identity component consumed
by the gate engine ([CMP-0004](../components/CMP-0004-governance-gate-engine.md))
— a cross-component seam to check at graduation review.
