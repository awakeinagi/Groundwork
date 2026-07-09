---
id: SP-0005
type: spike
title: External secret-store adapter evaluation
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
overview: >-
  Question: when an enterprise deployment mandates an external secret
  store, which adapter (Vault, cloud KMS, other) best serves the
  connector-secrets workload, and how do secrets migrate from embedded
  envelope encryption without a re-authorization storm? Blocks no current
  work; on trigger firing, it blocks deployments that require external
  secrets (secrets handle every delegated review and identity linkage).
  Method surveys deployment's approved services, prototypes storage seam
  against leading candidate, measures token re-encryption and movement
  without user action, recommends adapter boundary. Deferred to backlog;
  revived by TRG-0006. Findings pending.
timebox: 3d
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  relates-to: [ST-0021, ST-0022]
cites: [DEC-0100, DEC-0152]
---

# SP-0005: External Secret-Store Adapter Evaluation

> Deferred to `backlog` at creation (per
> DEC-0152,
> the deferral citation per
> DEC-0100).
> Subscribed to trigger TRG-0006 — an enterprise deployment mandating
> an external secret store revives it.

## Question

When an enterprise deployment mandates an external secret store, which
adapter target (HashiCorp Vault, cloud KMS, other) best serves the
connector-secrets workload — and how do secrets migrate from the
embedded envelope-encrypted store
(DEC-0152)
without a re-authorization storm for every linked OAuth identity?

## Why It Blocks

Nothing today — that is why it is deferred. On the trigger firing, it
blocks the affected deployment: secrets handling is on the path of
every delegated review
(ST-0021)
and identity linkage
(ST-0022).

## Method

Survey the mandating deployment's approved secret-store services;
prototype the storage seam against the leading candidate; measure
whether existing tokens can be re-encrypted and moved without user
action; recommend the adapter boundary (extend the app-database
envelope scheme vs. a dedicated secrets port).

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — a completed spike produces at least one decision, even
"assumption confirmed, no change."
