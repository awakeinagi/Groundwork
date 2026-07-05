---
id: EP-0004
type: epic
title: Cross-Reference Graph Index
status: draft
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0007]
  impacted-by: [EP-0001, EP-0002, EP-0003]
cites: [DEC-0009, DEC-0010, DEC-0026]
---

# EP-0004: Cross-Reference Graph Index

## Summary

A queryable graph database built from the typed links and citations in
artifact frontmatter — strictly a derived, rebuildable projection of the
canonical store. Serves traversal queries to agents (context retrieval),
the gate engine (impact analysis), and the UI (traceability navigation).

## Why (Goal Alignment)

The cross-reference system is BG-0001's alignment backbone; the Graph Index
is what makes it efficiently navigable for agents at scale
([DEC-0010](../decisions/DEC-0010-graph-index-derived.md)) without
compromising the single-source-of-truth rule
([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md)).

## Scope

**In:** graph construction from frontmatter (`derives-from`, `satisfies`,
`depends-on`, `conflicts-with`, `supersedes`, `relates-to`, `cites`);
incremental updates from the store's change-event stream; full rebuild from
scratch (the invariant that proves derived-ness); query API — ancestors/
descendants, trace-to-goal, cited-by, conflict neighborhoods, dependency
topology for the Handoff Manifest; path-usage statistics feeding
consolidation placement (EP-0007).

**Out:** choosing what to do with query results (callers' concern); the
canonical link data itself (EP-0001 validates and owns it).

## Domain Context

Bounded context: **Graph Index**. Terms: Graph Index, Provenance Chain,
typed link vocabulary — per [CONTEXT.md](../../CONTEXT.md) and
[SPEC-artifact-common](../specs/SPEC-artifact-common.md).

## Interfaces & Contracts to Define

- **Graph query API**: language-neutral contract; the specific graph engine
  (Neo4j, embedded, etc.) is an implementation detail behind it — engine
  choice deferred, per SES-0001 synthesis (T14).
- **Rebuild contract**: `rebuild(canonical-ref) → index`, deterministic.
- **Path-usage telemetry schema**: consumed by EP-0007.

## Risks & Open Questions

- Graph engine selection — explicitly deferred; candidate spike when this
  epic is refined.
- Index freshness guarantees relative to the event stream (read-after-write
  for agents mid-session).

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
