---
id: DEC-0017
type: decision
title: A consolidation memory layer keeps agent retrieval lean and fresh
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Consolidation memory layer maintains curated reference material on frequently
  traveled artifact graph paths, pinned to source git refs; stale consolidations
  regenerated or retired mechanically, never served; kept non-citable to
  preserve provenance chain integrity.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T9"
links:
  derives-from: [SES-0001]
---

# DEC-0017: A consolidation memory layer for agent retrieval

## Context

Crawling the full artifact graph for every agent task would overwhelm context
windows with superfluous information; retrieval must be fast and concise.
But any summarization risks going stale as the design evolves.

## Decision

Maintain curated/consolidated reference material along frequently traveled
paths of the artifact graph — a memory system for the agent. Consolidations
are derived artifacts pinned to the git refs of their sources; any source
change invalidates them mechanically. Stale consolidations are never served;
they are regenerated or retired. Nothing may cite a Consolidation as
provenance.

## Rationale

Gets the context-window economy of summaries with a freshness guarantee that
requires no judgment: ref mismatch = stale. Keeping consolidations
non-citable preserves the provenance chain's integrity
(DEC-0015).

## Alternatives Considered

- **No memory layer, always crawl**: context bloat and slow retrieval.
- **Manually curated context packs**: authoring and staleness burden on
  humans.

## Implications

Formalized in [SPEC-consolidation](../specs/SPEC-consolidation.md). Requires
graph-path usage analysis (DEC-0010) to
know which paths are hot, and a maintenance process for regeneration.
