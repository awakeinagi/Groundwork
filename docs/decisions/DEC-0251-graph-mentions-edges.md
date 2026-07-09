---
id: DEC-0251
type: decision
title: The graph index gains MENTIONS edges and reciprocity audits
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0049 @ T3-T4, T8-T11"
links:
  derives-from: [SES-0049]
  relates-to: [DEC-0063, DEC-0092, DEC-0242, DEC-0246, DEC-0247,
               DEC-0249, DEC-0250]
---

# DEC-0251: Graph MENTIONS Edges and Reciprocity Audits

## Context

The stakeholder asked to use the graph to find reciprocity gaps ("the
items themselves say they derive from BG-0001 but BG-0001's Derived
Work section doesn't list them"). The graph index carries frontmatter
edges only; body bare-ID mentions are not indexed — which is exactly
why no reciprocity asymmetry was queryable and the sweep had to be a
one-off script.

## Decision

`groundwork_graph.py` indexes every bare artifact ID in body prose
(code spans and fenced blocks excluded, notation per DEC-0242) as a
`MENTIONS` edge from the containing artifact to the referenced one.
The `gaps` command gains reciprocity audits mirroring the checker
rules: children unlisted in their parent's body (DEC-0246),
dead/missing cites (DEC-0247), impactor edges without impactor prose
(DEC-0249), and session relates-to targets unmentioned (DEC-0250).

Division of labor is unchanged: `check_links.py` is the blocking
enforcement surface; the graph is the derived exploration surface —
`MENTIONS` makes every future reciprocity question a two-line Cypher
query instead of a bespoke script.

This respects DEC-0063's boundary (bodies stay in the store): a
`MENTIONS` edge records only that a reference exists, never body
content — the same body-derived-edge shape the `IMPLEMENTS` edge
(DEC-0092's Implements lines) already exercises.

## Rationale

The gap class was invisible precisely because prose references lived
outside every queryable view. Indexing them closes the blind spot for
ad-hoc questions the canned rules don't cover (e.g. "which artifacts
mention X without any frontmatter edge to it?").

## Alternatives Considered

- **Index only, no gaps extension**: leaves the audits as cookbook
  recipes someone must remember to run.
- **Checker only, no graph change**: enforcement without
  explorability; the next novel asymmetry needs another one-off
  script.

## Implications

Graph schema documentation (references/graph-queries.md) gains the
`MENTIONS` table and recipe entries; `build`/`sync` parse bodies the
same way the checker does, keeping the two surfaces consistent.
