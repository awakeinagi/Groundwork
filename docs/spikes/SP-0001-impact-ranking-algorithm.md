---
id: SP-0001
type: spike
title: Ranking algorithm for impact-based refinement ordering
status: draft
owner: ds-lead
created: 2026-07-05
timebox: 3d
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  relates-to: [EP-0001, EP-0002, EP-0003, EP-0004, EP-0005, EP-0006, EP-0007]
cites: [DEC-0026, DEC-0027]
---

# SP-0001: Ranking Algorithm for Impact-Based Refinement Ordering

## Question

Given a set of same-level artifacts and their directional impact links
([DEC-0026](../decisions/DEC-0026-directional-impact-links.md)), what
algorithm produces a refinement order that minimizes decision rework — i.e.,
maximizes the chance that when we refine an artifact, the decisions it is
impacted by have already been made? The answer must be well-defined in the
presence of cycles, since real impact graphs contain them (the current epic
set has EP-0001↔EP-0003 and EP-0002↔EP-0006).

## Why It Blocks

Refinement ordering is the first scheduling decision Groundwork makes at
every level — goals, epics, stories, spikes — and it recurs every time
impact edges change or new siblings appear. Until this spike concludes,
ordering is human judgment informed by raw edges
([DEC-0027](../decisions/DEC-0027-impact-ranked-refinement-order.md)), which
does not scale and hides its reasoning. The Governance engine's
re-refinement queueing ([EP-0003](../epics/EP-0003-governance-and-gate-engine.md))
and the Graph Index's query contract ([EP-0004](../epics/EP-0004-graph-index.md))
both have interfaces shaped by whatever the algorithm needs.

## Method

1. Formalize the objective: define "decision rework" cost over an ordering
   of a directed graph with cycles, and what ties mean.
2. Evaluate candidate approaches against that objective on the real EP-0001–
   EP-0007 graph plus synthetic graphs (larger, denser, cyclic):
   - condensation of strongly connected components + topological sort of the
     DAG of SCCs, with an intra-SCC tie-break rule (cycle members refined
     iteratively or jointly);
   - eigenvector/PageRank-style centrality on impact edges (rank = how much
     your decisions propagate);
   - weighted out-degree minus in-degree heuristics;
   - minimum feedback arc set orderings (minimize edges pointing backward
     in the refinement sequence).
3. Investigate **provisional bounding decisions** (sponsor guidance,
   SES-0003 @ T1): rather than strictly ordering refinement, impacted items
   may first receive "subject to change" decisions or best guesses — made by
   the agent, humans, or both — that provide guidance and boundaries for
   refining the item that impacts them, with reconciliation once the
   impactor's real decisions land. Assess: whether this needs a
   `provisional` decision status, how reconciliation interacts with the
   staleness machinery ([DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md)),
   and whether provisional bounds change what the ranking algorithm should
   optimize (e.g., cycles become tractable by bounding one direction).
4. Consider extensions the data model may need: edge weights (impact
   strength), partial refinement (an artifact revisited after its impactors
   settle), and incremental re-ranking when edges change.
5. Prototype the front-runner and run it on the current epic graph; sanity-
   check the output against human judgment.

## Findings

Pending — filled at completion.

## Resulting Decisions

Pending — per [SPEC-spike](../specs/SPEC-spike.md), completion requires at
least one Decision record deriving from this spike (the chosen algorithm,
plus any data-model extensions such as edge weights).
