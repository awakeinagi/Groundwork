---
id: SP-0005
type: spike
title: External secret-store adapter evaluation
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-08
timebox: 3d
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  relates-to: [ST-0021, ST-0022]
cites: [DEC-0152]
---

# SP-0005: External Secret-Store Adapter Evaluation

> Deferred to `backlog` at creation (per
> [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> Subscribed to trigger TRG-0006 — an enterprise deployment mandating
> an external secret store revives it.

## Question

When an enterprise deployment mandates an external secret store, which
adapter target (HashiCorp Vault, cloud KMS, other) best serves the
connector-secrets workload — and how do secrets migrate from the
embedded envelope-encrypted store
([DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md))
without a re-authorization storm for every linked OAuth identity?

## Why It Blocks

Nothing today — that is why it is deferred. On the trigger firing, it
blocks the affected deployment: secrets handling is on the path of
every delegated review
([ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md))
and identity linkage
([ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)).

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
