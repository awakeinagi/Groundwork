---
id: DEC-0068
type: decision
title: A deterministic recipe resolver assembles session context bundles
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0008 @ T2-T3"
links:
  derives-from: [SES-0008]
---

# DEC-0068: The recipe resolver

## Context

Strategy packs declare context recipes with token budgets
([DEC-0056](DEC-0056-context-recipes-in-packs.md)); something must turn a
recipe plus a task into an actual context window.

## Decision

The retrieval layer exposes `resolve(recipe, task) → bundle`: required
graph paths fetched (via EP-0004), fresh consolidations substituted where
they cover a path, search filling content gaps, everything ranked and
truncated to the token budget by the recipe's priority order. Every bundle
element carries source refs and freshness metadata. Resolution is
deterministic for a given (recipe, task, repo-ref, index-state) — agents
use on-demand graph/search tools mid-session for follow-ups.

## Rationale

One well-tested assembly brain beats every pack reimplementing ranking and
truncation; determinism makes context assembly debuggable and evaluable
(the DEC-0058 harness can regression-test bundles).

## Alternatives Considered

- **Primitives only**: divergent quality, duplicated logic across packs.
- **Agentic retrieval**: LLM latency and cost on every session start,
  weaker reproducibility.

## Implications

The resolver contract (recipe schema in, bundle schema out) is EP-0007's
primary language-neutral interface; on-demand regeneration
([DEC-0066](DEC-0066-debounced-on-demand-regeneration.md)) is invoked
inside resolution when a covering consolidation is stale.
