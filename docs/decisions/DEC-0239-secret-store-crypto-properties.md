---
id: DEC-0239
type: decision
title: Secret-store contract states crypto properties; named v1 algorithms are pinned as Implementation Constraints
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T3-T4"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0152]
---

# DEC-0239: Secret-Store Crypto — Properties in Contract, Defaults in Constraints

## Context

[DEC-0152](DEC-0152-secrets-encrypted-in-app-database.md) requires
envelope encryption with a deployment-provided master key; how
specific the graduated secret store's contract should be about
algorithms was open.

## Decision

[CMP-0015](../components/CMP-0015-secret-store.md)'s contract items
state properties — envelope encryption, AEAD, per-secret data keys,
master key never persisted alongside the data. The named v1 defaults
(AES-256-GCM data keys; master key from environment or key file) are
pinned as decision-cited Implementation Constraints, not contract
items.

## Rationale

Testable without freezing cryptography into the seam; an algorithm
swap is a constraint change, not a contract amendment with a
staleness walk.

## Alternatives Considered

- **Fully named algorithms in the contract**: maximum precision;
  algorithm swaps become contract amendments.
- **Properties only anywhere**: two implementations could choose
  incompatible schemes and fail conformance ambiguously.

## Implications

The conformance expectations test the properties (round-trip,
tamper-detection, key-absence failure), with the constraints defining
the reference implementation's concrete scheme.
