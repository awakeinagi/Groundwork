---
id: DEC-0084
type: decision
title: Spec includes a modeling-patterns catalog composing the five types
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T7"
links:
  derives-from: [SES-0012]
---

# DEC-0084: Modeling-Patterns Catalog

## Context

Candidate extra types — repository/store, workflow/process, policy/rule —
were rejected from the taxonomy ([DEC-0082](DEC-0082-closed-element-type-taxonomy.md))
because each models as a composition of the five types. The sponsor
amended the recommendation: that modeling knowledge must not be lost.

## Decision

The design-elements spec includes a patterns catalog showing how common
system constructs are modeled as compositions of the five element types,
naming for each pattern the required sub-elements that keep the
composition independently buildable-and-testable (per
[DEC-0011](DEC-0011-contract-complete-component-docs.md)). Initial
patterns: repository/store, workflow/process (saga), policy/rule. The
catalog is guidance for CMP authors, not additional gate rules; it grows
as new constructs recur.

## Rationale

Sponsor amendment (SES-0012 @ T7): a closed taxonomy only works if
authors are shown how to express the constructs the rejected types would
have named — otherwise pressure to reopen the enum returns with the
first repository.

## Alternatives Considered

- **Taxonomy-only spec**: leaner, but leaves each author to rediscover
  the compositions, inconsistently.

## Implications

Catalog section in
[SPEC-design-elements](../specs/SPEC-design-elements.md); future recurring
constructs are added there via mechanical spec edits rather than enum
changes.
