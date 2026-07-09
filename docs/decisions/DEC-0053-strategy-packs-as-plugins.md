---
id: DEC-0053
type: decision
title: Grilling methodology ships as versioned, plugin-like strategy packs
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Grilling methodology ships as versioned, plugin-like strategy packs: bundles
  of prompts, skills, tools, and policies per artifact type and phase
  (goal-refinement, epic-refinement, story-refinement, conflict-mediation,
  CP-triage), stored in the canonical repo and PR-gated like governance. Packs
  are model-agnostic at the core, with the underlying LLM swappable while
  functionality is maintained; the session frontmatter records which pack version
  and model conducted it. This makes methodology provenance and an improvable
  asset, refined through the same gated process as everything else, with model
  swaps decoupled from methodology changes.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T2-T3"
links:
  derives-from: [SES-0006]
---

# DEC-0053: Strategy packs as plugin bundles

## Context

The grilling methodology — question taxonomies, dependency ordering,
recommended-answer discipline, stopping criteria — needs a home that is
reviewable, versioned, and independent of both the service release cycle
and the underlying model.

## Decision

Methodology ships as **strategy packs treated like plugins**: versioned
bundles of prompts, skills, tools, and policies, per artifact type and
phase (goal-refinement, epic-refinement, story-refinement,
conflict-mediation, CP-triage), stored in the canonical repo and PR-gated
like governance. Packs are model-agnostic at the core, with the underlying
LLM swappable while functionality is maintained; the session frontmatter
records which pack version (and model) conducted it.

## Rationale

Methodology becomes provenance and an improvable asset: refined over time
through the same gated process as everything else, with model swaps
decoupled from methodology changes — the sponsor's plugin framing.

## Alternatives Considered

- **Embedded in service code**: methodology changes need releases; review
  buried in code diffs.
- **Freeform agent judgment**: zero reproducibility; nothing to improve
  deliberately.

## Implications

A pack format spec (bundle layout, `pack.yaml` schema, skill/tool
declaration) becomes an EP-0002 contract deliverable; pack changes and LLM
swaps are gated by the evaluation harness
(DEC-0058); context recipes live in the
pack (DEC-0056).
