---
id: DEC-0463
type: decision
title: "Dogfooding merges into Self-Governance"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T4, T13"
overview: >-
  SES-0089's epic derivation resolves DEC-0446's deferred
  Dogfooding-vs-Self-governance merge question: the two form a
  mutual feedback loop (dogfooding surfaces governance gaps,
  governance constrains the dogfooding practice) and share the
  Engine-contributor persona and the corpus's own governance state
  as data. Both system-architect consultation instances converged on
  merging them into one epic, Self-Governance & Dogfooding, rather
  than tracking them as separate epics with a permanent mutual edge,
  or folding Dogfooding into Adoption (which DEC-0446 already ruled
  out). The epic's stories will separate governance-rule work from
  dogfooding-loop work internally.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0446, DEC-0442, DEC-0462]
---

# DEC-0463: Dogfooding merges into Self-Governance

## Context

DEC-0446 added Dogfooding to the roster as distinct from Self-governance
and Adoption, and deferred the Dogfooding-vs-Self-governance merge
assessment to epic derivation via the coupling check.

## Decision

Dogfooding and Self-Governance merge into a single epic, Self-Governance
& Dogfooding.

## Rationale

The two form a mutual feedback loop — dogfooding surfaces governance
gaps while governance rules constrain the dogfooding practice — and
persistent mutual coupling signals one epic wearing two IDs. They share
the Engine-contributor persona and the corpus's own governance state as
their data. Both consultation instances converged on the merge.

## Alternatives Considered

Separate epics carrying a documented permanent mutual edge; folding
Dogfooding into Adoption (rejected — DEC-0446 defines Dogfooding as
distinct from Adoption's domain).

## Implications

Resolves DEC-0446's deferred question. The epic's stories separate
governance-rule work from dogfooding-loop work.
