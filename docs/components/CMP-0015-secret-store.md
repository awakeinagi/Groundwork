---
id: CMP-0015
type: component
title: Secret Store
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Standalone service component, graduated from CMP-0007 per DEC-0232
  (consumed by CMP-0007 and CMP-0009). Single place secret material lives
  at rest: envelope-encrypted storage in app database behind CMP-0003.
  Operations: put, get, delete with namespace/key scoping. Envelope
  encryption: each secret encrypted with own data key under AEAD; data
  keys wrapped by deployment master key. Master key never persisted with
  data. No secret values in logs or error output. Copied database useless
  without master key; tampered ciphertext yields decryption-failed,
  never silent corruption.
context: integration
component-type: service
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [CMP-0003]
cites: [DEC-0136, DEC-0152, DEC-0232, DEC-0239]
---

# CMP-0015: Secret Store

> Standalone `service`-type component, graduated out of
> CMP-0007's draft per
> DEC-0232 under the
> DEC-0136 rule:
> consumed by more than one CMP —
> CMP-0007 (OAuth tokens, the
> attribution signing key) and
> CMP-0009 (per-installation webhook
> signing secrets, its `IG-5`); the master key is handed in by
> CMP-0010 at startup.

## Purpose

The single place secret material lives at rest: envelope-encrypted
storage for connector and service secrets in the app database, behind
the App Database Port, with the master key from deployment
configuration
(per DEC-0152).

## Ubiquitous Language

Secret Store, Port, Adapter — per [CONTEXT.md](../../CONTEXT.md).

## Design Elements

### SecretStore (service)

Implements: ST-0021,
ST-0022

- `SecretStore.A-1` — `put(namespace, key, secret) → ok`: stores or
  replaces (replacement supports credential rotation) the secret
  envelope-encrypted; typed error: `encryption-unavailable` (no master
  key loaded)
  (per DEC-0152,
  DEC-0232).
- `SecretStore.A-2` — `get(namespace, key) → secret`; typed errors:
  `not-found`, `decryption-failed` (absent/wrong master key or
  tampered ciphertext — never partial plaintext)
  (per DEC-0152,
  DEC-0239).
- `SecretStore.A-3` — `delete(namespace, key) → ok`; typed error:
  `not-found`
  (per DEC-0152).
- `SecretStore.B-1` — envelope encryption: each secret is encrypted
  with its own data key under an AEAD scheme; data keys are wrapped by
  the deployment master key; the master key comes from deployment
  configuration and is never persisted with the data
  (per DEC-0152,
  DEC-0239).
- `SecretStore.B-2` — persistence goes exclusively through the App
  Database Port's bookkeeping family
  (CMP-0003, `AppDatabasePort.A-3`);
  only ciphertext crosses the port
  (per DEC-0152).
- `SecretStore.B-3` — secret values never appear in logs, error
  messages, traces, or any enumeration surface
  (per DEC-0152).
- `SecretStore.B-4` — a copied database file is useless without the
  deployment master key; tampered ciphertext or a wrong key yields
  `decryption-failed`, never silent corruption
  (per DEC-0152,
  DEC-0239).

## Component Invariants

- `C-1` — no consumer holds secret material at rest anywhere but this
  store: not in the repo, not in governance files, not in plain
  app-database rows
  (per DEC-0152).

## Implementation Guidance

### Constraints

- `IG-1` — v1 reference scheme: AES-256-GCM data keys; master key
  read from environment variable or key file
  (per DEC-0239,
  DEC-0152).
- `IG-2` — the master key is loaded once at startup by the Composition
  Root (CMP-0010, its `IG-3`) and
  handed to this component; no other component reads the key source
  (per DEC-0152).

### Notes

- Namespacing convention: one namespace per consuming concern (e.g.
  `oauth-tokens`, `signing-keys`, `webhook-secrets`) keeps blast radius
  and future per-namespace policies tractable.

## Dependencies

- CMP-0003 — consumed sections:
  `AppDatabasePort.A-1` (UnitOfWork) and `AppDatabasePort.A-3`
  (bookkeeping put/get/delete).

## Acceptance & Test Expectations

1. Round-trip: `put` then `get` returns the secret across process
   restart (per DEC-0152).
2. Key absence: with no master key configured, `put` fails
   `encryption-unavailable` and `get` fails `decryption-failed`; no
   plaintext path exists
   (per DEC-0239).
3. Tamper detection: modified ciphertext rows fail `decryption-failed`
   (per DEC-0239).
4. At-rest inspection: a dump of the underlying database contains no
   plaintext secret material
   (per DEC-0152).
5. Hygiene: log/error output captured across the suite contains no
   secret values (per DEC-0152).

## Out of Scope

- An external vault / KMS adapter — deferred, evaluated by
  SP-0005 behind
  trigger `TRG-0006`
  (per DEC-0152).
- Master-key rotation and re-encryption tooling — an operational
  concern weighed together with the vault adapter in
  SP-0005.
- Which secrets exist and when they rotate — the consumers' contracts
  (CMP-0007,
  CMP-0009).
- Deployment-configuration values that are not secrets (feature flags,
  mappings) — the Composition Root's config surface
  (CMP-0010).
