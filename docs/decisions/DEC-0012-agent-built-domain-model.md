---
id: DEC-0012
type: decision
title: The agent builds the domain model during refinement
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Agent builds the domain model during refinement by challenging vague terms,
  proposing precise canonical terms, and recording definitions in glossaries
  so bounded contexts and component boundaries emerge from stakeholder-
  validated language continuously rather than as one-time modeling.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T6-T7"
links:
  derives-from: [SES-0001]
---

# DEC-0012: The agent builds the domain model during refinement

## Context

Component boundaries are to align with DDD-style business objects, but no
formal domain model or ubiquitous language exists in the organization today.

## Decision

Every refinement session doubles as domain modeling: the agent challenges
vague or overloaded terms, proposes precise canonical terms, records
definitions in per-context glossaries (CONTEXT.md style), and lets bounded
contexts — and therefore component boundaries — emerge from that language.
The glossary is a first-class, gated artifact.

## Rationale

Terminology drift is a root cause of the vague-requirements problem; making
the glossary an enforced byproduct of refinement attacks it continuously
rather than as a one-time modeling exercise.

## Alternatives Considered

- **Formal model exists**: it doesn't.
- **Seed from codebase mining**: viable enrichment later; not a substitute
  for stakeholder-validated language.

## Implications

The session agent needs glossary-challenge behavior (à la the
domain-modeling skill); Component Docs must resolve every model term against
the glossary ([SPEC-component](../specs/SPEC-component.md)).
