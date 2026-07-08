---
id: ST-0009
type: story
title: Hybrid search capabilities beyond v1 — unlinked-neighbor audit, glossary drift, seam clustering
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-07
links:
  derives-from: [EP-0007]
  satisfies: [BG-0001]
  depends-on: []
  impacts: []
  impacted-by: []
cites: [DEC-0119, DEC-0120]
---

# ST-0009: Hybrid Search Capabilities beyond v1

> Deferred to `backlog` at creation (per
> [DEC-0120](../decisions/DEC-0120-v1-scope-and-backlog-capture.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> No trigger subscription — revival is by want. POC evidence from
> [SES-0019](../sessions/SES-0019-semantic-search-hybrid-tooling.md)
> (T13) is summarized inline so revival starts from the tuning
> insights, not from scratch.

## Summary

Three semantic+graph capabilities that tested as promising-but-not-ready
in the
[SES-0019](../sessions/SES-0019-semantic-search-hybrid-tooling.md)
feasibility POCs, to extend the hybrid search tooling
([DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md)) when
revived:

1. **Unlinked-neighbor audit** — surface artifact pairs with high
   semantic similarity but no graph connection: duplicate-story,
   missing-edge, and latent-conflict candidates. *POC evidence:*
   pairwise scoring of 10,289 pairs was instant, but the naive top-10
   was template-similarity noise (sibling refinement sessions at 0.91)
   and false "unlinked" verdicts for CMP↔story pairs connected via
   element `IMPLEMENTS` edges. Tuning needed: treat element-mediated
   paths (`HAS_ELEMENT`/`IMPLEMENTS`) and ≤2-hop paths as connected;
   compare content sections only, excluding shared template sections;
   calibrate per artifact-type pair (unlinked-pair mean similarity was
   0.654 vs linked 0.763 — the distributions overlap heavily).
2. **Glossary-drift detection** — flag sections semantically close to a
   `CONTEXT.md` term that never name it (near-synonym drift, e.g.
   "approval checkpoint" for **Gate**). *POC evidence:* synthetic
   probes hit 2/3, but the corpus scan flagged 129 of 922 chunks
   (~14%), overwhelmingly false positives — discussions legitimately
   not naming the term. Needs a much higher precision bar (e.g.,
   restrict to definition-shaped sentences, or require repeated
   near-miss phrasing) before it's worth agent attention.
3. **Seam-candidate clustering** — cluster semantically similar Design
   Elements across Component Docs to propose seam graduation
   ([SPEC-design-elements](../specs/SPEC-design-elements.md)). *POC
   evidence:* untestable — only
   [CMP-0001](../components/CMP-0001-artifact-store-service.md) exists;
   within-component element similarities ran 0.57–0.81, suggesting
   cross-CMP discrimination will need element-contract-block
   embeddings, not whole-section ones. Revisit when ≥2 CMPs exist.

Explicitly **not** included: trigger matching — rejected with evidence
(per [DEC-0120](../decisions/DEC-0120-v1-scope-and-backlog-capture.md)),
not deferred.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. The unlinked-neighbor audit reports pairs an eng-lead judges ≥50%
   actionable (missing edge, duplicate, or conflict) on the then-current
   corpus, counting element-mediated links as connected (per
   [DEC-0119](../decisions/DEC-0119-hybrid-retrieval-semantics.md),
   [DEC-0120](../decisions/DEC-0120-v1-scope-and-backlog-capture.md)).
2. Glossary-drift detection's false-positive rate is measured and
   below an agreed precision bar before it surfaces to agents (per
   [DEC-0120](../decisions/DEC-0120-v1-scope-and-backlog-capture.md)).
3. Seam clustering runs only when ≥2 CMPs exist and ranks cross-CMP
   element pairs for graduation review (per
   [DEC-0120](../decisions/DEC-0120-v1-scope-and-backlog-capture.md)).

## Component Impact

None yet — this extends the skill's local tooling today; system-side
placement (the [EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
retrieval layer's search API per
[DEC-0067](../decisions/DEC-0067-retrieval-owns-search.md)) is decided
at revival.

## Out of Scope

Trigger matching (rejected, see above); HNSW indexing
([SP-0003](../spikes/SP-0003-hnsw-index-adoption.md)); any change to
the v1 search tool's shipped semantics.

## Notes for Implementers

The throwaway POC scripts referenced in
[SES-0019](../sessions/SES-0019-semantic-search-hybrid-tooling.md) were
scratch artifacts and are not preserved; the measured findings above
are the durable record.
