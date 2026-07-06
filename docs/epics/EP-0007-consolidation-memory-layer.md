---
id: EP-0007
type: epic
title: Consolidation Memory Layer
status: gated
owner: ds-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0004]
  impacts: [EP-0006]
  impacted-by: [EP-0001, EP-0002, EP-0004]
cites: [DEC-0017, DEC-0026, DEC-0056, DEC-0063, DEC-0065, DEC-0066, DEC-0067,
        DEC-0068, DEC-0069, DEC-0070, DEC-0071, DEC-0072]
---

# EP-0007: Consolidation Memory Layer

## Summary

Groundwork's retrieval and memory layer: consolidations along catalogued
and telemetry-discovered graph paths, full-text and semantic search over
artifact bodies, a deterministic recipe resolver that assembles
budget-bounded context bundles for sessions, automated faithfulness
checking, and opt-in, user-owned participant profiles.

## Why (Goal Alignment)

Refinement and implementation agents need existing context
([DEC-0016](../decisions/DEC-0016-agent-context-feeds.md)) without
overwhelming their windows — the sponsor's explicit concern behind
[DEC-0017](../decisions/DEC-0017-consolidation-memory-layer.md). Semantic
search additionally powers cross-goal conflict detection
([DEC-0067](../decisions/DEC-0067-retrieval-owns-search.md)) — BG-0001
outcome 2 — and profiles improve the session experience the whole system
rides on ([DEC-0071](../decisions/DEC-0071-opt-in-participant-profiles.md)).

## Scope

**In** (refined at [SES-0008](../sessions/SES-0008-ep-0007-refinement.md)):

- **Placement** ([DEC-0065](../decisions/DEC-0065-catalog-plus-telemetry-placement.md)):
  static always-on catalog (per-goal neighborhood, per-epic bundle,
  glossary-per-context) as repo configuration; telemetry-driven additions
  and retirements from EP-0004's path-usage statistics; explicit human
  requests.
- **Freshness & churn** ([DEC-0066](../decisions/DEC-0066-debounced-on-demand-regeneration.md)):
  instant staleness (never served stale); debounced regeneration
  (quiet-window / max-wait) plus on-demand rebuild at request time.
- **Search** ([DEC-0067](../decisions/DEC-0067-retrieval-owns-search.md)):
  full-text + embedding-based semantic search over bodies; derived and
  rebuildable; embedding-model version pinned, swap = re-embed batch.
- **Serving** ([DEC-0068](../decisions/DEC-0068-recipe-resolver.md)):
  `resolve(recipe, task) → bundle` — deterministic assembly of graph
  paths, fresh consolidations, and search results, ranked and truncated to
  the token budget, every element carrying source refs and freshness
  metadata.
- **Quality** ([DEC-0069](../decisions/DEC-0069-automated-faithfulness-checks.md)):
  no human gate; automated no-new-claims faithfulness checks block serving
  on failure; periodic judge sampling.
- **Human review & flagging** ([DEC-0072](../decisions/DEC-0072-consolidation-review-flagging.md)):
  consolidations browsable in the UI with source refs, freshness state,
  and check history; any user's flag quarantines immediately (never
  served; resolver falls back to sources) pending disposition —
  regenerate, fix sources, or correct the checker; confirmed misses feed
  the evaluation corpus as regression cases.
- **Participant profiles** ([DEC-0071](../decisions/DEC-0071-opt-in-participant-profiles.md)):
  opt-in per user; readable and editable by the subject via the UI; stored
  per-person outside the canonical artifact store; served as bundle
  elements. Org facts never live in profiles — they belong in artifacts.

**Out:** graph structure queries (EP-0004 — this layer composes them); the
profile/consent UI itself (EP-0006, via the new EP-0007→EP-0006 impact
edge); search/vector engine choice until the extended SP-0002 concludes
([DEC-0070](../decisions/DEC-0070-extend-sp-0002-search-infra.md));
provenance citation of consolidations (forbidden — [SPEC-consolidation](../specs/SPEC-consolidation.md)).

## Domain Context

Bounded context: **Memory**. Terms: Consolidation, fresh/stale,
Participant Profile — per [CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Recipe resolver contract**: recipe schema in ([DEC-0056](../decisions/DEC-0056-context-recipes-in-packs.md)),
  bundle schema out — EP-0007's primary language-neutral interface.
- **Search API**: full-text + semantic query operations with ref-pinned
  results; embedding-version metadata.
- **Catalog schema**: the static consolidation catalog as repo
  configuration.
- **Faithfulness-check contract**: generation → pass/blocked with report.
- **Flag/quarantine contract**: flag → quarantine → disposition
  (regenerate | fix-sources | correct-checker), with eval-corpus feedback.
- **Profile store contract**: per-person CRUD with consent state, subject
  read/edit access, serving projection into bundles.

## Risks & Open Questions

- Search/vector infrastructure — extended [SP-0002](../spikes/SP-0002-graph-engine-selection.md).
- Consolidation effectiveness measurement (do bundles beat raw crawls?) —
  evaluation design shared with the DEC-0058 harness.
- Profile schema and retention policy (what may a profile contain; how
  long) — story-level, with privacy review.
- Embedding re-index cost at corpus scale on model swap — measure in
  SP-0002.

## Derived Work

None yet — stories/spikes follow gate approval of this epic (SP-0002 is
shared with EP-0004).
