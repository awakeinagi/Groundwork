---
id: DEC-0375
type: decision
title: "Reactive-substrate marginal-cost advantage is conditional; loop safety needs idempotence or budget caps (SP-0016, addressing DEC-0368)"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-11
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-11
source-span: "SES-0071"
overview: >-
  Differential reactive-substrate evidence that DEC-0368 recorded as
  missing. Over ActiveGraph 1.9.0: (1) Marginal cost -- self-scoped
  delta behaviors that read the triggering event's payload achieve
  corpus-independent ~0.1 ms per edit (~140x cheaper than the full
  batch checker at 16 components); the built-in Cypher pattern
  subscriptions re-scan the whole graph on every firing (the v0.7
  matcher ignores the triggering event) and are no cheaper than the
  batch checker at scale -- they provide selective firing, not
  incremental matching. (2) Loop safety -- idempotent mutate-on-
  match rules converge to a fixpoint even on dependency cycles; an
  unguarded cyclic cascade is non-terminating, and only
  ActiveGraph's budget={max_events} cap halts it (validated load-
  bearing). Implication: a reactive adoption of Groundwork's checker
  would require delta-scoped rule implementations plus idempotence-
  or-budget guards, not naive pattern subscriptions. Throwaway
  (DEC-0351); adoption via DEC-0337/DEC-0335 only; no kill bar
  (DEC-0355).
links:
  relates-to: [DEC-0368, DEC-0354, DEC-0351, DEC-0355, DEC-0374, DEC-0387]
  derives-from: [SES-0071]
---

# Reactive-substrate marginal-cost advantage is conditional; loop safety needs idempotence or budget caps (SP-0016, addressing DEC-0368)

## Context

DEC-0368 recorded that SP-0014 produced no differential evidence for a reactive substrate over a thin owned implementation, and left the question open for SP-0016 and SP-0017 to resolve. SP-0016's conditional stretch phase, run over ActiveGraph 1.9.0 with a throwaway build (DEC-0351), targets that gap directly: reactive marginal cost versus the batch checker, and loop safety under cascades.

## Decision

Marginal-cost evidence: self-scoped delta behaviors that read the triggering event's payload achieve corpus-independent per-edit cost (~0.1 ms, flat across 2/4/8/16-component corpora) -- roughly 140x cheaper than the full batch checker at 16 components (~19.8 ms rules-only, before the ~0.5s of corpus parsing the live hook adds). ActiveGraph's built-in Cypher pattern subscriptions do NOT deliver this: their matcher re-scans the whole graph on every firing (the triggering event is unused in 1.9.0's `PatternMatcher.matches`), so they grow with corpus size and reach batch-checker cost by 16 components -- they provide selective firing, not incremental matching.

Loop-safety evidence: idempotent mutate-on-match behaviors (mark a dependent stale only if not already stale) converge to a fixpoint on every topology tested, including cycles -- chain(100 nodes) settles in 100 firings, tree(127) in 127, cycle(50) in 51, each node firing once. An unguarded (non-idempotent) behavior on a cycle is genuinely non-terminating; only ActiveGraph's `budget={max_events}` cap halts it, deterministically and proportional to the cap. The budget cap is therefore load-bearing whenever idempotence is not guaranteed.

## Rationale

SES-0071 Turn 10 (marginal-cost experiment, `scratchpad/sp0016/reactive_experiment.py`) and Turn 11 (cascade/fixpoint experiment, `scratchpad/sp0016/cascade_experiment.py`) -- both throwaway, reusing SP-0014's projector. Root cause of the pattern-subscription result confirmed directly in ActiveGraph 1.9.0 source (`activegraph/runtime/patterns.py`, `PatternMatcher.matches`).

## Alternatives Considered

Concluding the reactive substrate is unconditionally cheaper was rejected as overclaiming -- the built-in pattern-subscription path measured is NOT cheaper at scale; only self-scoped, delta-reading behaviors are. Concluding cascades are always safe without guards was rejected -- an unguarded cyclic cascade is non-terminating absent a budget cap or idempotence.

## Implications

A reactive adoption of Groundwork's checker would require delta-scoped rule implementations (not naive Cypher pattern subscriptions) plus either idempotent rule design or an enforced budget cap. This is throwaway evidence (DEC-0351); adoption proceeds only through the ordinary DEC-0337 option survey followed by DEC-0335 design intake, with no kill bar attached to this descriptive result (DEC-0355).
