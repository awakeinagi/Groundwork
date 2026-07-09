---
id: DEC-0234
type: decision
title: GovernanceConfig and a shared RoleResolution service graduate out of CMP-0004 to CMP-0016
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  GovernanceConfig and a shared RoleResolution service graduate out of
  CMP-0004 into new standalone component CMP-0016. RoleResolution evaluates
  role membership plus active time-bounded delegation at explicit governance
  ref and point in time. Both CMP-0004 and CMP-0007 consume it; file schemas
  remain CMP-0001's. Delegation logic implemented exactly once eliminates
  divergence risk and resolves the dependency cycle between gate engine and
  identity.
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
(DEC-0040) was about to exist
twice: CMP-0007
resolves role claims for API/UI callers
(ST-0022
AC3), and the approved `GatePolicyCheck.B-1/B-3` evaluates roles and
delegation itself for PR verdicts. A dependency cycle also arises
(CMP-0004 consumes CMP-0007's attribution block; CMP-0007 would
consume CMP-0004's claims evaluation). The governance file *schemas*
are not in play — they are owned by
CMP-0001
(`SchemaValidator.D-2`), a premise corrected in-session before this
decision was recorded (SES-0045 T9–T10).

## Decision

The `GovernanceConfig` typed value graduates out of
CMP-0004 into a
new standalone component,
CMP-0016,
which also carries a `RoleResolution` service — role membership plus
active time-bounded delegation, evaluated at an explicit governance
ref and point in time. Both
CMP-0004 and
CMP-0007 consume it;
the file schemas remain
CMP-0001's.

## Rationale

Delegation logic implemented exactly once — divergence between the
gate engine's and identity's answers to "who holds this role right
now" is precisely the class of bug the gate engine exists to prevent.
Explicit ref/time parameters keep
DEC-0164's
live-evaluation stance intact. The cycle dissolves: both consumers
point at CMP-0016.

## Alternatives Considered

- **Schemas-only sourcing, both evaluate independently**: no CMP-0004
  amendment, but duplicated delegation logic.
- **RoleResolution homed in CMP-0007**: one fewer CMP, but deepens the
  gate engine's dependency on identity and widens the CMP-0004 rewrite.

## Implications

CMP-0004 is
amended (element moves out; `depends-on` gains CMP-0016 and CMP-0007)
and re-gated, revising
DEC-0162's ten-element,
none-graduated decomposition;
ST-0012 and
ST-0014 add CMP-0016 to
Component Impact.
