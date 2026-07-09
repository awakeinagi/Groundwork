---
id: DEC-0284
type: decision
title: Every artifact carries a frontmatter overview field for progressive disclosure
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T1-T5"
overview: >-
  Every artifact of every type gains a frontmatter overview: field — a
  self-sufficient summary an agent reads before (and often instead of)
  the body. Placement in frontmatter (not a body section or sidecar
  index) makes extraction a cheap YAML parse. This is the method-level
  progressive-disclosure entry point; it is a separate concern from
  EP-0007's application-side retrieval layer, which may later consume it.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0017, DEC-0068]
---

# DEC-0284: Every Artifact Carries a Frontmatter `overview:` Field

## Context

Agents facilitating this project burn a large share of their token
budget reading whole artifact files to discover small pieces of
information (SES-0053 @ T1). Semantic search returns snippets and the
graph tool answers structure questions, but there is no per-artifact
"read this first" layer — the corpus has no progressive disclosure at
read time.

## Decision

Every artifact, of **every type** (goals, epics, stories, spikes,
components, sessions, decisions, conflicts, change proposals, ideas,
consolidations), carries a frontmatter `overview:` field: a
self-sufficient summary an agent reads first to decide whether the
body is needed at all.

## Rationale

Frontmatter placement makes overview extraction a cheap YAML parse —
tooling can emit hundreds of overviews without touching a body.
Uniform coverage across all types means tooling and reading habits
never special-case: sessions and components are the largest wins, but
283 decisions read uniformly is what makes batch triage work. The
concern is method-level and immediate; the application's retrieval
design (DEC-0017's consolidation layer, DEC-0068's recipe resolver)
is a separate concern that may later consume overviews (SES-0053 @
T3).

## Alternatives Considered

- **First body section (`## Overview`)** — nicer to author, but
  extraction requires body parsing and it competes with per-type
  section orders.
- **Generated sidecar index (`docs/OVERVIEWS.md`)** — cheapest read,
  but a derived file that silently drifts and adds a build step.
- **Pipeline artifacts only / size-triggered coverage** — cheaper
  retrofit, but unpredictable presence breaks tooling reliance.

## Implications

[SPEC-artifact-common](../specs/SPEC-artifact-common.md) gains the
field; skill templates and references sync; all existing artifacts
are retrofitted (DEC-0291); presence is checker-enforced (DEC-0287);
content standard per DEC-0286; authority status per DEC-0285.
