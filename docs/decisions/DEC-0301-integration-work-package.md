---
id: DEC-0301
type: decision
title: Every component contributes an integration work package owning invariants and acceptance verification
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T5-T7"
overview: >-
  Every component contributes one generated integration work package
  to the manifest, depending on all of the component's element work
  packages and sequencing after lifted implementation dependencies
  (DEC-0309). Its charter: verify the component's C-n invariants and
  its Acceptance & Test Expectations — the whole-component guarantees
  no single element owns (e.g. CMP-0001's OpenAPI conformance,
  hermetic orchestration suite, replay convergence). Closes the
  integration-ownership vacuum both consultation instances ranked as
  the top risk of element-grain dispatch: 53 leaves with no assembler.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0297, DEC-0300, DEC-0309]
---

# DEC-0301: Integration Work Package

## Context

If elements dispatch individually, component invariants (`C-n`) and
whole-component Acceptance & Test Expectations have no implementing
element — the classic parallel-pieces-pass/whole-fails gap. Both
consultation instances ranked this the top risk.

## Decision

Every component contributes one generated **integration work
package** to the manifest:

- depends on all the component's element work packages, sequencing
  after lifted `implementation` dependencies (DEC-0309);
- charter: verify the component's `C-n` invariants and its
  Acceptance & Test Expectations sections;
- generated like all work packages (DEC-0300), never authored.

## Rationale

Integration ownership must be explicit in the dispatch plan itself;
assigning it to the component that ratified those guarantees keeps
verification where the contract semantics live.

## Alternatives Considered

- **No integration unit** (element packages only) — integration gap;
  rejected.
- **One system-wide integration task** — big-bang integration shape;
  rejected in favor of per-component packages plus slice acceptance
  (DEC-0302).

## Implications

Manifest schema carries two package kinds; component Acceptance
sections become the integration package's charter and should be
written to be executable against assembled elements.
