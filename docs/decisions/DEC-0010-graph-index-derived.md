---
id: DEC-0010
type: decision
title: A graph database indexes the link graph as a derived, rebuildable projection
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T6-T7, T9"
links:
  derives-from: [SES-0001]
---

# DEC-0010: A graph database indexes the link graph as a derived projection

## Context

The sponsor wants agents to query the cross-reference graph easily (impact
analysis, context retrieval, traceability). Frontmatter links in markdown are
authoritative but slow to traverse at query time.

## Decision

Build a graph database over the typed links — but strictly as a derived
index: rebuilt from the canonical docs at any time, never written to
directly, never a source of truth.

## Rationale

Gets graph-query ergonomics for agents without splitting truth between git
and a database — the same drift problem [DEC-0002](DEC-0002-doc-store-canonical.md)
eliminates for Jira must not be reintroduced internally.

## Alternatives Considered

- **Graph DB as truth**: rejected; splits truth.
- **No index, traverse files**: acceptable at bootstrap scale, degrades as
  the graph grows.

## Implications

The Graph Index is a component with a rebuild contract; choice of graph
engine is deferred behind its interface. Consolidation path analysis
([DEC-0017](DEC-0017-consolidation-memory-layer.md)) and impact analysis
([DEC-0007](DEC-0007-impact-analysis-stale-marks.md)) consume it.
