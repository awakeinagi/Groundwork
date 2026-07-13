---
id: DEC-0509
type: decision
title: "Check-time enforcement posture for governance rules"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T6–T7, T10–T11"
overview: >-
  DEC-0442 requires governance obligations to be mechanically
  checked, leaving open whether enforcement is gate/check-time only
  or also continuous (CI/pre-commit). This decision states EP-0014's
  enforcement posture at epic level as check-time — governance rules
  run as check-time rule families per DEC-0475, reporting at gate
  prep and explicit check runs, never blocking writes — while
  deferring whether the same rule families additionally run
  continuously to a story-level decision.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0475, DEC-0442, DEC-0484]
---

# DEC-0509: Check-time enforcement posture for governance rules

## Context

DEC-0442 requires governance obligations to be mechanically checked, which could mean checked at gate or check time, or enforced continuously (CI or pre-commit) between gates. DEC-0475 already draws the enforcement line: only self-trust invariants enforce at write time; everything else runs as check-time rule families.

## Decision

EP-0014 states its enforcement posture at epic level as check-time: governance rules run as check-time rule families per DEC-0475, reporting at gate prep and explicit check runs and never blocking writes. Whether the same rule families additionally run continuously is a story-level decision, deferred.

## Rationale

Fitness-function-style continuous enforcement belongs where quality scenarios are concrete, which is story level; DEC-0484's substrate-neutral hosting supports adding it later without epic rework. Committing now would bind stories to CI integration and a warn-versus-fail noise policy before any rule exists.

## Alternatives Considered

Committing to continuous enforcement as an epic-level quality goal now was rejected as premature. Ruling out continuous enforcement permanently was rejected because it forecloses a cheap option the substrate already supports.

## Implications

EP-0014's Risks & Open Questions section carries the deferred story-level question explicitly.
