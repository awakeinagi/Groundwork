---
id: DEC-0087
type: decision
title: Element declarations are parseable body headings; no frontmatter mirror
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T9-T11"
links:
  derives-from: [SES-0012]
---

# DEC-0087: Parseable Element Headings, No Frontmatter Mirror

## Context

The graph index, schema suite, check suite, and Handoff Manifest all
need to see a component's elements, not just prose. The sponsor asked
whether a frontmatter elements list *in addition to* body headings would
help or just add noise.

## Decision

Element declarations use the body-heading convention
`### <ElementName> (<type>)` inside the Design Elements section as the
single source of truth. The checker parses headings and validates types
against the closed enum. Machine consumers query element nodes via the
Graph Index. No frontmatter mirror.

## Rationale

Every real consumer parses the body anyway: the check suite must
validate obligations, item IDs, and citations that live in body
sections; the Graph Index is the sanctioned derived home for queryable
structure (DEC-0010); the Handoff
Manifest is compiled by tooling. A mirror would serve only a
hypothetical YAML-only consumer while costing dual maintenance on every
element change and adding mirror-drift as a new failure mode.

## Alternatives Considered

- **Body headings + frontmatter mirror**: cheap YAML read path, rejected
  as duplication inside a single file in a system whose core discipline
  is one source of truth with derived views. Revisitable as a mechanical
  spec change if a YAML-only consumer ever materializes.

## Implications

Heading grammar in [SPEC-design-elements](../specs/SPEC-design-elements.md);
ST-0007 parses and validates headings; EP-0004 story derivation must
include exposing element nodes (name, type, owning CMP, contract items)
in the Graph Index.
