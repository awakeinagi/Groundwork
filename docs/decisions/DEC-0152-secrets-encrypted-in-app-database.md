---
id: DEC-0152
type: decision
title: Connector secrets live envelope-encrypted in the app database; an external vault is a triggered future adapter
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0026 @ T4-T5"
links:
  derives-from: [SES-0026]
  relates-to: [DEC-0046, DEC-0102, DEC-0121]
---

# DEC-0152: Secrets Encrypted in the App Database

## Context

Per-user OAuth tokens belong in "the service secret store, never the
repo" (DEC-0046), but the v1 embedded
stack (DEC-0102) defines no secret
store, and DEC-0121 requires
consumers to program against ports.

## Decision

Connector secrets (OAuth tokens, host credentials, the attribution
signing key) are stored envelope-encrypted at rest in the app database,
accessed through the App Database Port
(CMP-0003); the master
key comes from deployment configuration (environment or key file) and
is never persisted alongside the data. An external vault (HashiCorp
Vault, cloud KMS) becomes a future adapter, evaluated by the deferred
spike SP-0005,
which arms trigger TRG-0006 (enterprise secret-store mandate) — the
sponsor's amendment to the facilitator's recommendation.

## Rationale

Zero extra infrastructure, honoring
DEC-0102's ops-burden stance; envelope
encryption keeps a copied database file useless without the deployment
key; the trigger keeps the enterprise-mandate path watched instead of
forgotten.

## Alternatives Considered

- **A fifth infrastructure port for secrets now**: cleaner seam, but a
  port and conformance suite for one v1 consumer.
- **OS keyring / permissions-locked file**: awkward for server
  deployments; a second stateful store to back up.
- **External vault in v1**: contradicts the zero-external-infrastructure
  stance.

## Implications

ST-0021 and
ST-0022
build against the encrypted store;
SP-0005 is
deferred `backlog` citing this decision; TRG-0006 is armed citing this
decision.
