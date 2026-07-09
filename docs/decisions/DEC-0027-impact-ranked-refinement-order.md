---
id: DEC-0027
type: decision
title: Refinement order is decided by ranking over the impact graph
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Refinement order among same-level artifacts determined by ranking algorithm
  over impact graph developed through research spike SP-0001; until spike
  concludes, ordering is human judgment informed by raw impact edges; encoding
  logic as validated algorithm makes prioritization reproducible and explainable.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0002 @ T1-T2"
links:
  derives-from: [SES-0002]
---

# DEC-0027: Refinement order decided by ranking over the impact graph

## Context

With impact links in place (DEC-0026),
the question "which sibling do we refine first?" becomes answerable from the
graph — but not trivially: real impact graphs contain cycles (the initial
epic set already has EP-0001↔EP-0003 and EP-0002↔EP-0006), so simple
topological ordering fails.

## Decision

Refinement order among same-level artifacts is determined by a ranking
algorithm over the impact graph. The algorithm is developed through a
dedicated research spike (SP-0001).
Until the spike concludes, ordering is human judgment informed by the raw
impact edges.

## Rationale

Encoding the ordering logic as an explicit, spike-validated algorithm makes
prioritization reproducible and explainable — the same property the rest of
Groundwork demands of requirements. Guessing at an algorithm now (PageRank
variant? cycle condensation + topo sort? weighted out-degree?) would bake in
an unvalidated choice at a load-bearing spot.

## Alternatives Considered

- **Manual ordering forever**: doesn't scale past a handful of items and
  hides its reasoning.
- **Pick an algorithm without a spike**: cheap now, expensive to unwind once
  refinement queues depend on it.

## Implications

SP-0001 is created deriving directly from BG-0001;
[SPEC-spike](../specs/SPEC-spike.md) is relaxed to allow cross-cutting,
process-level spikes to derive from a Business Goal (not only an Epic),
since refinement ordering is a goal-level concern that exists before any
epic is approved — a spec change produced by dogfooding.
