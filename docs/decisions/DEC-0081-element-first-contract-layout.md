---
id: DEC-0081
type: decision
title: Element-first contract layout with element-scoped item IDs
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T3-T5"
links:
  derives-from: [SES-0012]
---

# DEC-0081: Element-First Contract Layout

## Context

With multiple design elements inside one CMP, the sponsor asked how the
behavior/data/API contracts stay manageable — the three global contract
sections scatter each element's contract across the doc.

## Decision

Inside a CMP, the Design Elements section iterates elements; each
element carries its own contract block with element-scoped item IDs
(e.g. `StorageService.B-3`, kinds B = behavior, A = API, D = data). A
Component Invariants section (`C-<n>` items) holds cross-element
guarantees. This replaces the three global Behavior/API/Data Contract
sections of the original SPEC-component.

## Rationale

Contracts stay local to what they describe — directly answering the
manageability concern that motivated one-CMP-per-element — while one
gate still ratifies a coherent whole. Element-scoped IDs keep decision
citations and staleness precise at the same resolution a per-element doc
would give.

## Alternatives Considered

- **Global sections, element-tagged items**: preserves the current SPEC
  shape, but each element's contract remains scattered across three
  sections.

## Implications

[SPEC-component](../specs/SPEC-component.md) restructured;
[SPEC-design-elements](../specs/SPEC-design-elements.md) defines the ID
scheme; ST-0007 checks item-ID well-formedness and uniqueness. CMP-0001
(draft) restructured to the new layout.
