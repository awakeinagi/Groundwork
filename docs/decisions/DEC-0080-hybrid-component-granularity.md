---
id: DEC-0080
type: decision
title: Hybrid CMP granularity — nested design elements, seam elements graduate
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0012 @ T3-T5"
links:
  derives-from: [SES-0012]
---

# DEC-0080: Hybrid CMP Granularity

## Context

The proposed element types (entity, value, service, event, protocol) are
class/function-scale, while CMP docs are bounded-context-scale. The
sponsor asked whether one CMP per element would manage contracts more
cleanly than multi-element CMPs.

## Decision

Component Docs stay bounded-context-scale and contain typed design
elements. An element consumed across component boundaries graduates to
its own standalone CMP. Graduation rule: more than one consuming CMP, or
independently versioned conformance. Standalone element CMPs carry their
element type in frontmatter (`component-type:`).

## Rationale

The CMP is anchored to DEC-0011's
gate test — the unit an implementer can build *and* test independently.
A lone value or schema doc fails that test, and one-CMP-per-element
means ~10–15 gates per component, piecemeal approvals that can ratify
incoherent combinations, and internals promoted to published artifacts
against the contracts-not-internals rule. Seams (protocols, shared event
schemas, shared value kernels) genuinely have independent consumers,
versioning, and conformance tests, so they earn their own gate.

## Alternatives Considered

- **One CMP per element**: cleanest per-doc contracts, but gate
  explosion, incoherent piecemeal approval, internals published, and the
  Handoff Manifest must reassemble elements into buildable work units.
- **Nested only**: simplest rule, but cross-component seams get owned by
  one side's doc, blurring who governs the seam.

## Implications

CMP-0001's anticipated connector contract becomes a standalone
`protocol`-type CMP under EP-0005. [SPEC-component](../specs/SPEC-component.md)
gains the `component-type:` frontmatter field;
[SPEC-design-elements](../specs/SPEC-design-elements.md) records the
graduation rule. ST-0001 validates the new field tier-1.
