---
id: DEC-0140
type: decision
title: Governance bootstraps via a seeded init commit before protection is compiled
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T2-T3"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0037]
---

# DEC-0140: Seeded Governance Bootstrap

## Context

Governance-as-code ([DEC-0037](DEC-0037-governance-as-code.md)) makes
`governance/` PR-gated with the Arbiter as owner — but at deployment
time no governance files exist to gate their own creation, and no
Arbiter exists to approve them ([EP-0003](../epics/EP-0003-governance-and-gate-engine.md)'s
recorded bootstrap risk).

## Decision

A deployment-time init command writes the founding governance files —
the initial Arbiter and role assignments, taken from deployment
configuration — directly into the repository's initial history, before
branch protection is first compiled. The first policy compilation then
locks gating in behind them. The founding state is the first commit of
the audit trail.

## Rationale

The chicken-and-egg is resolved by sequencing, not by a standing
exception: once the door is locked there is no special case left in the
policy evaluator for an attacker to reach. The founding configuration
is exactly as auditable as everything after it.

## Alternatives Considered

- **Host-admin out-of-band PR**: keeps everything PR-shaped but depends
  on host permissions outside Groundwork's model, and the founding
  approval is checked by no policy.
- **Self-ratifying first PR**: a `gate-policy` special case for the
  empty-governance state is a permanent hole reachable by deleting
  `roles.yaml`.

## Implications

The init flow ships with the governance config story
([ST-0012](../stories/ST-0012-governance-config-schemas.md)); the
lock-behind sequencing is a compilation-story criterion
([ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md)).
