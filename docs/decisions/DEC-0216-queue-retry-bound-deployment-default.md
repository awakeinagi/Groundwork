---
id: DEC-0216
type: decision
title: Queue Port retry bound is a single deployment-wide default, not a per-job override
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  The Queue Port's retry bound is a single deployment-wide configured value
  (set via Composition Root), not overridable per job at enqueue time. This
  matches App Database Port precedent, which exposes no per-operation retry
  override either — retry policy is adapter/deployment configuration, not a
  per-call parameter.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0040 @ T1-T2"
links:
  derives-from: [SES-0040]
  relates-to: [DEC-0210, DEC-0139, DEC-0206]
  supersedes: []
---

# DEC-0216: Queue Retry Bound Is a Single Deployment-Wide Default

## Context

DEC-0210 established
"bounded retries per job" but left open whether the bound is one
deployment-wide configured value or overridable per job at enqueue
time.

## Decision

v1 defines a single deployment-wide max-retry value, set via the
Composition Root's deployment configuration
(DEC-0206); `enqueue()`
carries no per-job retry-bound parameter.

## Rationale

Matches the App Database Port precedent
(CMP-0003), which
exposes no per-operation retry override either — retry policy is
adapter/deployment configuration, not a per-call parameter. No cited
Acceptance Criterion in
ST-0060 or
ST-0061
calls for per-job tuning; a single default keeps the contract simplest
and can be extended later if a real job type needs a different bound.

## Alternatives Considered

The facilitator's Round 1 question set posed a per-job override of the retry bound at enqueue time as the alternative to a single deployment-wide default. The single-default recommendation was given instead because it matches the App Database Port precedent (CMP-0003), which exposes no per-operation retry override either, and because no cited Acceptance Criterion in ST-0060 or ST-0061 calls for per-job tuning; the stakeholder confirmed the recommendation as given. (skeleton restored at SES-0078)

## Implications

With retry policy set as adapter/deployment configuration via the Composition Root (DEC-0206), `enqueue()` carries no per-job retry-bound parameter, which keeps the contract at its simplest. The decision leaves room to extend the contract later if a real job type is found to need a different bound. (skeleton restored at SES-0078)
