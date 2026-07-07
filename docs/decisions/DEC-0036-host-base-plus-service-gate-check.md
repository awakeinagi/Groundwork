---
id: DEC-0036
type: decision
title: Gate policies enforce via host branch protection plus a service-computed check
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T2-T3"
links:
  derives-from: [SES-0004]
---

# DEC-0036: Host branch protection + service `gate-policy` check

## Context

PR approval is the gate ([DEC-0028](DEC-0028-fork-pull-pr-gating.md)), but
code hosts natively express only approval counts and path-based reviewer
rules — not policies like "a DS Lead must approve any story touching a DS
domain" ([DEC-0020](DEC-0020-configurable-gate-policies.md)).

## Decision

Two enforcement layers. Coarse rules compile to host branch protection:
artifact-type directories map to reviewer groups CODEOWNERS-style
(`docs/goals/**` → product-owners) with minimum approval counts for
committee gates. Everything richer — domain-conditional approvers, role
verification, quorum composition — is computed by the gate engine and
reported as a required `gate-policy` status check that blocks merge.

## Rationale

The host provides tamper-resistance (its reviewer machinery cannot be
bypassed by a service bug); the service provides expressiveness the host
lacks. Neither alone suffices.

## Alternatives Considered

- **Host-native only**: committee composition by distinct roles exceeds
  host vocabulary; policies would be dumbed down to fit.
- **Service-only**: single point of compromise; host machinery unused.

## Implications

The gate engine compiles `gate-policies.yaml`
([DEC-0037](DEC-0037-governance-as-code.md)) into branch-protection
settings via the code-host connector — requiring team and required-check
administration operations in the [EP-0005](../epics/EP-0005-connectors-and-identity.md) contract. Host review-semantics
variance (Bitbucket vs GitHub) becomes an [EP-0005](../epics/EP-0005-connectors-and-identity.md) refinement concern.
