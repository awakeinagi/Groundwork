---
id: DEC-0234
type: decision
title: GovernanceConfig and a shared RoleResolution service graduate out of CMP-0004 to CMP-0016
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T2, T5-T6, T9-T10"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0162, DEC-0040, DEC-0164, DEC-0136]
---

# DEC-0234: Graduate GovernanceConfig + RoleResolution

## Context

Role-membership and delegation-window evaluation
([DEC-0040](DEC-0040-role-pool-delegation.md)) was about to exist
twice: [CMP-0007](../components/CMP-0007-identity-and-access.md)
resolves role claims for API/UI callers
([ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)
AC3), and the approved `GatePolicyCheck.B-1/B-3` evaluates roles and
delegation itself for PR verdicts. A dependency cycle also arises
([CMP-0004](../components/CMP-0004-governance-gate-engine.md) consumes [CMP-0007](../components/CMP-0007-identity-and-access.md)'s attribution block; [CMP-0007](../components/CMP-0007-identity-and-access.md) would
consume [CMP-0004](../components/CMP-0004-governance-gate-engine.md)'s claims evaluation). The governance file *schemas*
are not in play — they are owned by
[CMP-0001](../components/CMP-0001-artifact-store-service.md)
(`SchemaValidator.D-2`), a premise corrected in-session before this
decision was recorded ([SES-0045](../sessions/SES-0045-cmp-0007-identity-refinement.md) T9–T10).

## Decision

The `GovernanceConfig` typed value graduates out of
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) into a
new standalone component,
[CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md),
which also carries a `RoleResolution` service — role membership plus
active time-bounded delegation, evaluated at an explicit governance
ref and point in time. Both
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) and
[CMP-0007](../components/CMP-0007-identity-and-access.md) consume it;
the file schemas remain
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s.

## Rationale

Delegation logic implemented exactly once — divergence between the
gate engine's and identity's answers to "who holds this role right
now" is precisely the class of bug the gate engine exists to prevent.
Explicit ref/time parameters keep
[DEC-0164](DEC-0164-gate-policy-check-live-evaluation.md)'s
live-evaluation stance intact. The cycle dissolves: both consumers
point at [CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md).

## Alternatives Considered

- **Schemas-only sourcing, both evaluate independently**: no [CMP-0004](../components/CMP-0004-governance-gate-engine.md)
  amendment, but duplicated delegation logic.
- **RoleResolution homed in [CMP-0007](../components/CMP-0007-identity-and-access.md)**: one fewer CMP, but deepens the
  gate engine's dependency on identity and widens the [CMP-0004](../components/CMP-0004-governance-gate-engine.md) rewrite.

## Implications

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) is
amended (element moves out; `depends-on` gains [CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md) and [CMP-0007](../components/CMP-0007-identity-and-access.md))
and re-gated, revising
[DEC-0162](DEC-0162-cmp-0004-element-decomposition.md)'s ten-element,
none-graduated decomposition;
[ST-0012](../stories/ST-0012-governance-config-schemas.md) and
[ST-0014](../stories/ST-0014-gate-policy-check.md) add [CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md) to
Component Impact.
