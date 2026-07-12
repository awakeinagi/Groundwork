---
id: DEC-0420
type: decision
title: "Groundwork names two delineated deliverables: the Paradigm and the Application"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T1-T5, T21, T31"
accepted-in: SES-0082
overview: >-
  Groundwork covers two delineated deliverables: the Paradigm (the
  documentation-first design method — gated artifact tree, grilling
  sessions, decision provenance, integrity rules — delivered as
  agent skills plus gw tooling, adoptable standalone) and the
  Application (the optional centralized team-facing UI built on the
  same paradigm). Corpus artifacts and CONTEXT.md must be
  unambiguous about which term they name.
links:
  derives-from: [SES-0082]
  relates-to: [BG-0001, BG-0002, DEC-0001, DEC-0326]
---

# DEC-0420: Groundwork names two delineated deliverables: the Paradigm and the Application

## Context

The term "Groundwork" had been used loosely across the corpus to mean both a design method and a product. SES-0082 was opened to settle whether these are one thing or two, and, if two, how the corpus names and separates them so artifacts and the glossary stop being ambiguous about which one they describe.

## Decision

The term Groundwork covers two distinct, delineated deliverables. The Groundwork Paradigm is the documentation-first design method itself — the gated artifact tree, grilling sessions, decision provenance, and integrity rules — delivered as agent skills plus the gw tooling and adoptable standalone in any repository. The Groundwork Application is the centralized team-facing application that manages Groundwork corpora through a UI; it is an optional superset built on the same paradigm. Corpus artifacts and glossary entries must be unambiguous about which of the two they name; CONTEXT.md carries both terms.

## Rationale

Naming the split explicitly resolves the ambiguity at its source rather than patching individual artifacts case by case: every future reference can be checked against a single authoritative distinction instead of inferred from context. It also matches the two deliverables' actual dependency direction — the paradigm stands alone, the application depends on it — so the naming mirrors the architecture rather than fighting it.

## Alternatives Considered

Continuing to use "Groundwork" as a single undifferentiated term was rejected: it had already produced confusion across DEC-0001 and DEC-0326 about whether "the product" meant the method or the hosted UI. Renaming one of the two deliverables to a wholly different brand was considered and set aside — both are legitimately "Groundwork," just at different scopes, and a shared root term keeps that relationship visible.

## Implications

CONTEXT.md is updated to carry both terms with their definitions. Future artifacts and glossary entries must state explicitly which of the two they mean when the distinction matters. This decision is the foundation the rest of SES-0082's decisions (paradigm/application boundary, engine single-sourcing, distribution) build on.
