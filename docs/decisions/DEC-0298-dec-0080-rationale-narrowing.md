---
id: DEC-0298
type: decision
title: DEC-0080's rationale narrows — the component gate ratifies coherence; the build-and-test unit is the work package
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T5-T7"
overview: >-
  Clarifying decision narrowing one sentence of DEC-0080's rationale:
  the component is "the unit whose gate ratifies a coherent design,"
  no longer "the unit an implementer can build and test
  independently." The build-and-test unit is now the work package
  (DEC-0300) under the dual-granularity model (DEC-0297). DEC-0080's
  decision — nested elements with seam graduation — and its full
  alternatives analysis stand unchanged. Narrowing, not supersession:
  DEC-0080's citers receive consistency review, no staleness walk.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0080, DEC-0297, DEC-0300]
---

# DEC-0298: Narrowing of DEC-0080's Rationale

## Context

DEC-0080 anchored implementability at the component ("a lone value or
schema doc fails that test") while rejecting one-doc-per-element.
DEC-0297 moves the dispatch atom to the element; without this
clarification the record would contradict itself.

## Decision

DEC-0080's rationale sentence anchoring "the unit an implementer can
build and test independently" at the component **narrows to**: the
component is "the unit whose gate ratifies a coherent design." The
build-and-test unit is the work package (DEC-0300). DEC-0080's
decision — nested elements by default, standalone CMPs on seam
graduation — and its alternatives analysis are untouched.

## Rationale

The gate-explosion and coherent-ratification arguments of DEC-0080
were always about approval economics, not dispatch; naming that
precisely lets the element-atom model coexist with the component
gate.

## Alternatives Considered

- **Full supersession of DEC-0080** — discards a still-correct
  decision to change one sentence; rejected.
- **Leave the contradiction implicit** — rule-type decisions fail
  silently; rejected.

## Implications

Consistency review of DEC-0080's citers; SPEC-component language
updated where it echoes the narrowed sentence.
