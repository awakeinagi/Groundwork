---
id: DEC-0179
type: decision
title: Eval harness requires an authored seed benchmark corpus before it can gate anything
status: accepted
owner: ds-lead
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0033 @ T2-T3"
links:
  derives-from: [SES-0033]
  supersedes: []
---

# DEC-0179: Eval Harness Requires an Authored Seed Benchmark Corpus Before It Can Gate Anything

## Context

EP-0002's Risks flagged
that grilling-quality and guardrail benchmarks need scenarios to judge
against, and none exist before the first production session. Left
unresolved, the harness would ship toothless — unable to gate pack
changes or model swaps (DEC-0058) —
until enough real sessions accumulated.

## Decision

A hand-authored seed benchmark corpus (covering goal-refinement,
epic-refinement, story-refinement, conflict-mediation, and CP-triage
scenarios) is a v1 acceptance criterion of the evaluation harness story:
the harness must not pass pack changes or model swaps until the seed
corpus exists and is exercised.

## Rationale

Gating power on day one matters more than corpus size — a small,
deliberately designed seed corpus gives the harness teeth immediately;
organic growth from production sessions supplements it later but cannot
be the only source or the harness is unusable at launch.

## Alternatives Considered

- **Grows organically, no seed requirement**: leaves the harness unable
  to gate anything until real sessions accumulate — exactly when pack
  changes are most likely (early iteration) and least protected.
- **Separate spike on corpus methodology**: the scenario shape (one per
  strategy-pack phase) is already implied by DEC-0053's
  phase list; a spike would re-derive what's already decided.

## Implications

ST-0041's acceptance criteria
require the seed corpus as a deliverable, not a stretch goal.
