---
id: DEC-0368
type: decision
title: "SP-0014 produced no differential evidence for a reactive substrate"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-11
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-11
source-span: "SP-0014 findings; SES-0069 @ T12-T17"
overview: >-
  SP-0014's rulebase exercised ActiveGraph only as a passive typed
  store: the SP-0013 projection loaded cleanly and expressiveness
  was never a constraint, but the 24-rule catalog fired as one batch
  behavior running plain graph queries, exercising none of the
  runtime's distinctive reactive, replay, or fork machinery. The
  spike therefore produces no differential evidence for a reactive
  graph runtime over a thin owned implementation of the same rule
  concepts. On the DEC-0354/DEC-0356 substrate-evaluation axis, the
  deferred DEC-0356 option survey must weigh SP-0016's hook-loop-
  economics evidence and SP-0017's fork-and-diff evidence, not this
  spike's -- recorded in SP-0014's Findings feasibility assessment
  (SES-0069 T16, stakeholder-directed inclusion at T17). Claiming
  ActiveGraph feasibility as a demonstrated benefit was considered
  and rejected as overclaiming: batch structural checking
  demonstrably does not need a reactive runtime. Implication:
  ActiveGraph earns adoption only if SP-0016/SP-0017 show the
  reactive/fork machinery paying for itself; SP-0014's data caveat
  (100% interface edges, leaving build-order/serialization/coupling
  rules unmeasured) carries forward into both of those spikes'
  evaluation.
links:
  derives-from: [SP-0014]
  relates-to: [DEC-0354, DEC-0356, SP-0013, SP-0016, SP-0017, DEC-0374, DEC-0375, DEC-0387]
cites: [DEC-0354, DEC-0356]
---

# DEC-0368: SP-0014 produced no differential evidence for a reactive substrate

## Context

The spike program evaluates ActiveGraph as candidate substrate (DEC-0354, DEC-0356); SP-0014 is the structural-rule-precision leg.

## Decision

SP-0014 exercised ActiveGraph only as a passive typed store: the projection loaded cleanly and expressiveness was never a constraint, but the rulebase fired as one batch behavior running plain graph queries, exercising none of the runtime's distinctive reactive, replay, or fork machinery. The spike therefore produces no differential evidence for a reactive graph runtime over a thin owned implementation of the same rule concepts; on that axis the DEC-0356 option survey must weigh SP-0016's (hook-loop economics) and SP-0017's (fork-and-diff) evidence, not this spike's.

## Rationale

Recorded in SP-0014's Findings feasibility assessment (SES-0069 T16, stakeholder-directed inclusion at T17).

## Alternatives Considered

Claiming ActiveGraph feasibility as demonstrated benefit — rejected as overclaiming; batch structural checking demonstrably does not need a reactive runtime.

## Implications

ActiveGraph earns adoption only if SP-0016/SP-0017 show the reactive/fork machinery paying for itself; the data caveat (100% interface edges leaving build-order/serialization/coupling rules unmeasured) carries into both.
