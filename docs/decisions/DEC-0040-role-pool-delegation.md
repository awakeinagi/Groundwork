---
id: DEC-0040
type: decision
title: Role-pool approval by default; explicit time-bounded delegation for exclusivity
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0004 @ T4-T5"
links:
  derives-from: [SES-0004]
---

# DEC-0040: Role-pool default + explicit delegation

## Context

Domain mappings name preferred approvers; queues must not stall when the
named person is unavailable.

## Decision

By default, any member of the required role's pool satisfies a gate — the
domain mapping expresses a *preferred* approver, not an exclusive one
(host teams already match the pool, per
[DEC-0036](DEC-0036-host-base-plus-service-gate-check.md)). Where
exclusivity matters, governance config supports explicit, time-bounded
delegation entries (person → delegate), edited via the same PR flow
([DEC-0037](DEC-0037-governance-as-code.md)).

## Rationale

No new mechanism for the common case; auditable exceptions for the rare
one; vacations never become Arbiter chores.

## Alternatives Considered

- **Strict named approver + Arbiter reassignment**: queues stall by
  default.
- **Auto-escalate after wait**: adds timers and makes approval rights
  time-dependent.

## Implications

The `gate-policy` check treats domain preference as routing (whose queue it
lands in), not as a merge requirement, unless an exclusivity flag is set in
the gate policy.
