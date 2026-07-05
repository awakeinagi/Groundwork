---
id: EP-0007
type: epic
title: Consolidation Memory Layer
status: draft
owner: ds-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0004]
  impacted-by: [EP-0001, EP-0002, EP-0004]
cites: [DEC-0017, DEC-0026]
---

# EP-0007: Consolidation Memory Layer

## Summary

Groundwork's agent memory: curated Consolidation artifacts summarizing
frequently traveled paths of the artifact graph, served to agents in place
of multi-artifact crawls, with mechanical freshness invalidation (source git
refs pinned; any source change marks the consolidation stale) and a
maintenance process that regenerates or retires stale ones.

## Why (Goal Alignment)

Refinement and implementation agents need existing context
([DEC-0016](../decisions/DEC-0016-agent-context-feeds.md)) without
overwhelming their context windows — the sponsor's explicit concern at
SES-0001 T9. Consolidations deliver retrieval economy while the freshness
rule keeps summaries from silently diverging from evolving design
([DEC-0017](../decisions/DEC-0017-consolidation-memory-layer.md)).

## Scope

**In:** consolidation generation (agent-produced, per
[SPEC-consolidation](../specs/SPEC-consolidation.md)); placement policy
driven by graph path-usage telemetry (EP-0004); freshness tracking against
source refs; regeneration/retirement maintenance loop; serving interface
("give me fresh context for task X" → consolidations + gap-filling artifact
reads); inclusion of fresh consolidations in Handoff Manifests.

**Out:** the graph statistics themselves (EP-0004); provenance — nothing
cites a Consolidation ([SPEC-consolidation](../specs/SPEC-consolidation.md)).

## Domain Context

Bounded context: **Memory**. Terms: Consolidation, fresh/stale — per
[CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Retrieval contract**: task descriptor → ranked fresh context bundle
  within a token budget.
- **Maintenance contract**: stale-consolidation queue, regeneration
  triggers, retirement criteria.

## Risks & Open Questions

- Regeneration cost vs. churn: hot paths under active refinement invalidate
  constantly — debounce/batching policy needed; candidate spike.
- Measuring whether consolidations actually improve agent output vs. direct
  crawling — evaluation design.

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
