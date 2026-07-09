---
id: DEC-0305
type: decision
title: Handoff Manifest ownership — EP-0001 generates and writes, EP-0004 supplies topology, EP-0008 exposes the endpoint
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T8-T9"
overview: >-
  EP-0001 owns the Handoff Manifest and work-package bundle
  generation, validation, and write — they are generated store
  artifacts pinned to a canonical-ref. EP-0004 supplies the
  graph-derived topology (typed element DAG, lifted edges, topo-sort)
  via a declared dependency. EP-0008 exposes the trigger endpoint
  only. Resolves the ownership half of SES-0055 finding 1 (critical:
  manifest emission unowned) captured in IDEA-0006; the DEC-0194
  coverage-pass rerun remains queued there. Joint dual-instance
  consultation recommendation, revising the SES-0055 T8 facilitator
  recommendation (EP-0004 assembles): with bundles and preamble in
  the picture, the manifest family is store-artifact-shaped —
  reproducible projections written under store validation — while the
  topology competence stays with the graph.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0300, DEC-0302, IDEA-0006, EP-0001, EP-0004, EP-0008]
---

# DEC-0305: Manifest Ownership

## Context

SES-0055 found manifest emission unowned (critical). The SES-0056
work-package model materially increased manifest complexity, forcing
ownership to be settled before the new machinery could be assigned.

## Decision

- **EP-0001** owns generation, validation, and write of the Handoff
  Manifest, work-package bundles, and Shared Preamble — generated
  store artifacts pinned to a `canonical-ref`.
- **EP-0004** supplies the graph-derived topology (typed element DAG,
  lifted edges, topological ordering) via a declared dependency.
- **EP-0008** exposes the trigger endpoint only.

## Rationale

Same-ref-same-output reproducibility and all-writes-through-the-store
(DEC-0008 family) make the manifest family store artifacts; graph
competence stays where traversal contracts live (DEC-0062); the
composition root stays thin (DEC-0201).

## Alternatives Considered

- **EP-0004 assembles** (SES-0055 T8 facilitator recommendation) —
  stretches a derived read index into an emitter; revised.
- **EP-0008 composes** — domain logic in the composition root against
  DEC-0201; rejected.

## Implications

EP-0001/EP-0004/EP-0008 scope amendments (gated); manifest-emission
stories derive under EP-0001; IDEA-0006 narrows to the DEC-0194
coverage-pass rerun.
