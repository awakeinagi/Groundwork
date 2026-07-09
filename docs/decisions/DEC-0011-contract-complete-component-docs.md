---
id: DEC-0011
type: decision
title: Component docs are contract-complete, with crawlable provenance as fallback
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
overview: >-
  Component Doc must be contract-complete: implementer with doc plus
  dependency interface contracts (not internals) can implement and test.
  Behavior, data, API contracts itemized and tied to discussions/decisions
  that produced them, so agents crawl cross-references for context when
  needed. Full self-containment pursued iteratively; quality software is
  priority so fallback stays sanctioned. Prevents divergence risk across
  parallel agents while crawl keeps missing detail from becoming wrong
  guess. Formalized in SPEC-component.
source-span: "SES-0001 @ T6-T7"
links:
  derives-from: [SES-0001]
---

# DEC-0011: Component docs are contract-complete, with crawlable fallback

## Context

Component docs are handed to a swarm of parallel implementation agents.
"Self-contained" needed a testable definition — it is the definition of done
for the whole documentation pipeline.

## Decision

A Component Doc must be contract-complete: an implementer holding the doc
plus the interface contracts of its dependencies (not their internals) can
implement and test the component. Behavior, data, and API contracts are
itemized and tied to the documented Q&A/discussions/decisions that produced
them, so implementation agents can crawl cross-references for additional
context when needed. Full self-containment is pursued iteratively; it should
ideally be unnecessary to crawl — but quality software is the top priority,
so the fallback stays sanctioned.

## Rationale

Contract-completeness prevents the divergence risk of each parallel agent
re-interpreting shared upstream docs, while the provenance crawl keeps a
missing detail from becoming a wrong guess.

## Alternatives Considered

- **Context-complete** (doc + ancestor chain as input): divergence risk
  across parallel agents.
- **Repo-aware** (assume codebase exploration): makes self-containment
  aspirational from the start.

## Implications

Formalized in [SPEC-component](../specs/SPEC-component.md): every contract
item cites Decisions; uncited items block the gate. Implementer escalations
for missing context are documentation defects to feed back into refinement
([SPEC-handoff-manifest](../specs/SPEC-handoff-manifest.md)).
