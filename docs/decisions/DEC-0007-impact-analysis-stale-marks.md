---
id: DEC-0007
type: decision
title: Upstream changes trigger impact analysis and stale marks
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T4-T5"
links:
  derives-from: [SES-0001]
---

# DEC-0007: Upstream changes trigger impact analysis and stale marks

## Context

An approved Business Goal will sometimes change (pivot, new constraint) after
a tree of epics, stories, and component docs — possibly mid-implementation —
has been derived from it.

## Decision

When an approved artifact changes, the agent walks the cross-reference graph,
marks affected descendants `stale`, produces an impact report (including
in-flight work), and queues targeted re-refinement sessions. Approved-but-
stale artifacts block new downstream generation until re-ratified.

## Rationale

Preserves human refinements and in-flight state (unlike regeneration) while
guaranteeing nothing new is built on an invalidated basis (unlike manual
propagation).

## Alternatives Considered

- **Full downstream regeneration**: clean lineage, destroys manual work.
- **Manual propagation**: humans decide everything; misses the tail.

## Implications

Requires the typed link graph ([DEC-0009](DEC-0009-typed-links-stable-ids.md))
and Graph Index ([DEC-0010](DEC-0010-graph-index-derived.md)). The same
mechanism serves superseded Decisions and spike findings
([DEC-0023](DEC-0023-spike-findings-become-decisions.md)) and Consolidation
freshness ([DEC-0017](DEC-0017-consolidation-memory-layer.md)).
