---
id: DEC-0086
type: decision
title: Taxonomy, obligations, and patterns live in a dedicated SPEC-design-elements
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T8-T9"
links:
  derives-from: [SES-0012]
---

# DEC-0086: SPEC-design-elements as the Normative Home

## Context

The new normative content — type definitions, typed obligations, the
seam-graduation rule, element-declaration syntax, element-first layout
rules, and the modeling-patterns catalog — needed a home. Inlining it
all would roughly triple SPEC-component.

## Decision

A dedicated [SPEC-design-elements](../specs/SPEC-design-elements.md)
holds the taxonomy, obligations, graduation rule, declaration syntax,
item-ID scheme, and patterns catalog. SPEC-component references it and
keeps only the doc-structure rules (required sections, Implementation
Guidance, gate checks). The five type names become glossary terms in
[CONTEXT.md](../../CONTEXT.md).

## Rationale

One spec per concern keeps SPEC-component readable at authoring time and
gives the patterns catalog room to grow without crowding gate-checkable
rules; glossary entries keep the type names enforceable everywhere.

## Alternatives Considered

- **Extend SPEC-component + glossary**: one read path, but the spec
  triples and guidance sits among gate rules.
- **Rules in spec, patterns in a non-normative guidance doc**: cleanest
  normative/advisory divide, but two new places to keep in sync with the
  type definitions.

## Implications

[ST-0001](../stories/ST-0001-tier1-schema-suite.md)'s "schema per SPEC document" criterion now covers the new spec's
enum asset; SPEC-component slims to structure + references.
