---
id: DEC-0454
type: decision
title: "Link-vocabulary extension: inspired-by and inspired"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  The closed typed-link vocabulary is extended with a reciprocal
  pair: an artifact inspired by research carries inspired-by naming
  the RSCH, and the Research artifact carries the reciprocal
  inspired list. The pair is permitted on Business Goals, Epics,
  Stories, Spikes, Ideas, and other Research artifacts. This is the
  first extension of the vocabulary defined by DEC-0009 and
  DEC-0026, chosen over overloading relates-to because it preserves
  the causal direction that a piece of work exists because of a
  specific investigation, matching the existing auto-reciprocated
  impacts/impacted-by pattern.
links:
  derives-from: [SES-0086]
  relates-to: [DEC-0009, DEC-0026, DEC-0159, DEC-0248]
---

# DEC-0454: Link-vocabulary extension: inspired-by and inspired

## Context

Grilling round 3 (T9) asked how "inspired by this research" enters the link vocabulary, noting the vocabulary is closed (DEC-0009, DEC-0026). At T10 the stakeholder chose the new reciprocal pair, amending it so IDEAs and other RSCH artifacts can also be inspired-by an RSCH.

## Decision

The closed typed-link vocabulary is extended with a reciprocal pair: an artifact inspired by research carries inspired-by naming the RSCH, and the Research artifact carries the reciprocal inspired list. The pair is permitted on Business Goals, Epics, Stories, Spikes, Ideas, and other Research artifacts. This is the first extension of the vocabulary defined by DEC-0009 and DEC-0026.

## Rationale

Reusing an existing link type like relates-to would lose the directional, causal meaning the stakeholder wanted — that a piece of work exists because of a specific investigation. A reciprocal pair, matching the existing impacts/impacted-by pattern, captures that directionality while staying auto-reciprocated like the other paired link types.

## Alternatives Considered

Overloading relates-to was rejected for losing causal direction. Restricting the pair to design-tree types only (excluding Ideas and other RSCH artifacts) was rejected at T10 — the stakeholder explicitly widened it to cover research inspiring further research or captured ideas.

## Implications

This is precedent for the closed vocabulary being amendable via a decision rather than being permanently fixed; the graph model and gw CLI need to recognize the new pair as auto-reciprocal.
