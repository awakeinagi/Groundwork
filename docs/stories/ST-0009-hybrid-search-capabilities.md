---
id: ST-0009
type: story
title: Hybrid search capabilities beyond v1 — unlinked-neighbor audit, glossary drift, seam clustering
status: deferred
release: backlog
owner: eng-lead
created: 2026-07-07
overview: >-
  Extends hybrid search tooling with three semantic plus graph capabilities
  tested as promising-but-not-ready in SES-0019 POCs: (1) unlinked-neighbor
  audit surfacing artifact pairs with high semantic similarity but no graph
  connection (duplicate-story, missing-edge, conflict candidates); tuning
  needed for element-mediated paths and content-only comparison. (2)
  Glossary-drift detection flagging sections semantically close to CONTEXT.md
  terms that never name them; false-positive rate too high, needs precision
  bar. (3) Seam-candidate clustering for proposing element seam graduation
  across Component Docs; untestable with single CMP, needs element-contract
  embeddings. Deferred to backlog with no trigger subscription; revival by
  want. POC evidence captured inline for tuning at revival.
links:
  derives-from: [EP-0007]
  satisfies: [BG-0001]
  depends-on: []
  impacts: []
  impacted-by: []
cites: [DEC-0067, DEC-0100, DEC-0119, DEC-0120]
---

# ST-0009: Hybrid Search Capabilities beyond v1

> Deferred to `backlog` at creation (per
> DEC-0120,
> the deferral citation per
> DEC-0100).
> No trigger subscription — revival is by want. POC evidence from
> SES-0019
> (T13) is summarized inline so revival starts from the tuning
> insights, not from scratch.

## Summary

Three semantic+graph capabilities that tested as promising-but-not-ready
in the
SES-0019
feasibility POCs, to extend the hybrid search tooling
(DEC-0119) when
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
   CMP-0001 exists;
   within-component element similarities ran 0.57–0.81, suggesting
   cross-CMP discrimination will need element-contract-block
   embeddings, not whole-section ones. Revisit when ≥2 CMPs exist.

Explicitly **not** included: trigger matching — rejected with evidence
(per DEC-0120),
not deferred.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. The unlinked-neighbor audit reports pairs an eng-lead judges ≥50%
   actionable (missing edge, duplicate, or conflict) on the then-current
   corpus, counting element-mediated links as connected (per
   DEC-0119,
   DEC-0120).
2. Glossary-drift detection's false-positive rate is measured and
   below an agreed precision bar before it surfaces to agents (per
   DEC-0120).
3. Seam clustering runs only when ≥2 CMPs exist and ranks cross-CMP
   element pairs for graduation review (per
   DEC-0120).

## Component Impact

None yet — this extends the skill's local tooling today; system-side
placement (the EP-0007
retrieval layer's search API per
DEC-0067) is decided
at revival.

## Out of Scope

Trigger matching (rejected, see above); HNSW indexing
(SP-0003); any change to
the v1 search tool's shipped semantics.

## Notes for Implementers

The throwaway POC scripts referenced in
SES-0019 were
scratch artifacts and are not preserved; the measured findings above
are the durable record.
