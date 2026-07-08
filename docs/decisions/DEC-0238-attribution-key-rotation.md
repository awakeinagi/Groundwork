---
id: DEC-0238
type: decision
title: The attribution block carries a key_id; deployment config holds the ordered active public-key list
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T3-T4"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0153]
---

# DEC-0238: Attribution Key Rotation via key_id

## Context

[DEC-0153](DEC-0153-service-signed-attribution-block.md) fixed the
signed attribution block with a single service key and its public key
in deployment configuration, leaving rotation (compromise, policy)
unaddressed.

## Decision

The attribution-block schema carries a `key_id`; deployment
configuration holds an ordered list of active public keys keyed by
id. The verifier ([CMP-0004](../components/CMP-0004-governance-gate-engine.md))
verifies against the key matching the block's `key_id`. Rotation: add
the new key to the list, re-key the signer, retire the old key once
open PRs drain.

## Rationale

Cheap now, painful to retrofit; rotating without it invalidates
attribution on every open PR.

## Alternatives Considered

- **Single key, rotation = re-deployment**: simpler schema; open PRs
  need re-review on every rotation.

## Implications

Narrows [DEC-0153](DEC-0153-service-signed-attribution-block.md)'s
"the public key is deployment configuration" to a keyed list; the
schema published by [CMP-0007](../components/CMP-0007-identity-and-access.md)
and consumed by the gate engine includes `key_id` from v1.
