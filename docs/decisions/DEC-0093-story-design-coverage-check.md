---
id: DEC-0093
type: decision
title: Story design coverage — every approved story referenced by an element
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0015 @ T2-T3"
links:
  derives-from: [SES-0015]
  relates-to: [DEC-0092]
---

# DEC-0093: Story design coverage — every approved story referenced by an element

## Context

[DEC-0092](DEC-0092-element-implements-line.md) governs elements that
exist, but alone it leaves "story X is 100% designed" unfalsifiable:
nothing would detect an approved story that no element anywhere picked
up. The reverse direction needs its own check, and its timing matters —
elements do not exist yet when a story passes its gate.

## Decision

Every approved story must be referenced by at least one design
element's Implements line. Enforced at two points:

1. **CMP gate**: a Component Doc cannot pass its gate while any story
   whose Component Impact names that CMP has no referencing element in
   it.
2. **Corpus-wide audit**: the tier-2 suite
   ([ST-0007](../stories/ST-0007-tier2-check-suite.md)) and the gap
   tooling report every approved story with zero referencing elements
   as an uncovered design gap. The audit reports; it does not block
   commits.

This is explicitly **not** a story-gate check.

## Rationale

The coverage check is what makes design completion decidable — the
participant's stated goal. Placing enforcement at the CMP gate matches
when the data can exist: a CMP claiming contract-completeness while a
story it serves has no design surface is exactly the inconsistency the
gate should catch. The non-blocking audit surfaces gaps early without
making story approval impossible before component design starts.

## Alternatives Considered

- **Audit-only**: softer; a CMP could be declared contract-complete
  while a story it claims to serve has no design surface — rejected.
- **No reverse check**: rejected; leaves the metric's denominator
  unverifiable.
- **Story-gate enforcement**: impossible ordering — elements are
  itemized after stories gate.

## Implications

[SPEC-component](../specs/SPEC-component.md) gains the gate rule;
[ST-0007](../stories/ST-0007-tier2-check-suite.md) gains the audit
criterion; the skill's `gaps` tooling reports uncovered approved
stories. A CMP author must account for every story naming their
component before gating.
