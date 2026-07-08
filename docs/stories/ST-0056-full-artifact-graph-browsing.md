---
id: ST-0056
type: story
title: Full artifact and graph browsing across all types
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0006]
  satisfies: [BG-0001]
  depends-on: [ST-0045]
cites: [DEC-0009, DEC-0010, DEC-0073, DEC-0100, DEC-0101, DEC-0119, DEC-0133]
---

# ST-0056: Full Artifact and Graph Browsing Across All Types

> Deferred to release `2` at creation (per
> [DEC-0073](../decisions/DEC-0073-v1-ui-surfaces.md), the v1 surface
> subset; the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)/[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)). No
> trigger subscription — revival is release-2 planning.

## Summary

Generalizes [ST-0045](ST-0045-goal-artifact-view.md)'s artifact view
from Business Goals to every artifact type, plus a graph browser over
the derived graph index (per
[DEC-0010](../decisions/DEC-0010-graph-index-derived.md)) for exploring
the full design tree — impact, trace, and order queries rendered
visually rather than run via the CLI graph tool.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. [ST-0045](ST-0045-goal-artifact-view.md)'s renderer works for every
   artifact type (epic, story, spike, component, session, decision,
   conflict, change proposal), not just Business Goals.
2. A graph browser visualizes typed-link traversal (`impact`, `trace`,
   `order` equivalents) over the read-only derived index
   (per [DEC-0010](../decisions/DEC-0010-graph-index-derived.md)),
   rendering the closed link-type vocabulary over stable frontmatter IDs
   (per [DEC-0009](../decisions/DEC-0009-typed-links-stable-ids.md)).

## Component Impact

None — deferred.

## Out of Scope

The graph index and its query API themselves
([EP-0004](../epics/EP-0004-graph-index.md)); this story only renders
what the graph API already exposes.

## Notes for Implementers

Generalize, don't rewrite — [ST-0045](ST-0045-goal-artifact-view.md)'s
renderer should already be artifact-type-agnostic in its core; this
story is mostly wiring plus the graph visualization itself. The browser
should expose the same deferred/backlog discovery surface the status
report already provides, not a separate one
(per [DEC-0101](../decisions/DEC-0101-deferred-out-of-metrics.md)), and
any search entry point should honor the CLI search tool's established
semantics — superseded-decision redirect, subtree scoping, metadata
pre-filters — rather than diverge from it
(per [DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md)).
