---
id: DEC-0297
type: decision
title: Dual-granularity implementation model — element is the dispatch atom, component the gate unit
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0056 @ T1-T7"
overview: >-
  Design elements are the terminal specification and dispatch atoms of
  implementation: terminal (no further breakdown), all sibling
  dependencies declared (the "no unspecified dependencies" criterion),
  and empty-context implementable via a generated work-package bundle
  (DEC-0300). The component doc remains the gate, coherence, and
  assembly unit — DEC-0080's decision stands (its rationale narrowed
  by DEC-0298). The three atomicity properties are gate-checked
  obligations (DEC-0303), not assumed facts: the dual-instance
  consultation showed today's elements carry prose-only sibling
  dependencies (e.g. CMP-0001 StorageService running SchemaValidator,
  delegating to MechanicalWriteService), so atomicity must be earned
  per element, not declared globally. The name "design element" is
  kept for the design-time construct.
links:
  derives-from: [SES-0056]
  relates-to: [DEC-0080, DEC-0011, DEC-0298, DEC-0300, DEC-0303]
---

# DEC-0297: Dual-Granularity Implementation Model

## Context

The stakeholder proposed treating design elements as the atomic units
of implementation handoff (SES-0056 T1). The dual-instance
system-architect consultation found the direction sound but the
as-stated claims conflated three roles (work assignment, contract
completeness, integration verification) and the "no internal
dependencies" premise false against today's corpus.

## Decision

Design elements are the **terminal specification and dispatch atoms**
of implementation:

- **terminal** — an element needs no further breakdown;
- **declared dependencies** — every dependency on another element is
  a named, typed contract-item reference (DEC-0299); "atomic" means
  *no unspecified dependencies*, not no dependencies;
- **empty-context implementable** — via the generated work-package
  bundle (DEC-0300) under the DEC-0304 semantics.

The component doc remains the **gate, coherence, and assembly unit**.
Contract-completeness ratification and integration verification stay
at component grain (DEC-0301). All three atomicity properties are
gate-checked obligations per DEC-0303.

## Rationale

Small assignment units suit empty-context agents, but larger
contract-ownership and assembly units prevent the
parallel-pieces-pass/whole-fails integration gap. Splitting dispatch
granularity from ratification granularity repeats the record's own
successful DEC-0080/DEC-0081 move one level down.

## Alternatives Considered

- **Full element atomization** (element = contract, gate, and handoff
  unit) — orphans component invariants and acceptance suites; revives
  DEC-0080's rejected alternative; rejected.
- **Status quo + informational element inventory** — exports
  decomposition intelligence to the orchestrator; fails the
  stakeholder's intent; rejected.

## Implications

Elements gain Uses: lines (DEC-0299); the manifest moves to work
packages (DEC-0300); gate reviews gain atomicity checks (DEC-0303);
"design element" is retained as the design-time name.
