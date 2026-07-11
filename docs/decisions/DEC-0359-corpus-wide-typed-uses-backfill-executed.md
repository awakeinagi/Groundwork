---
id: DEC-0359
type: decision
title: "Corpus-wide typed Uses: backfill executed"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0066 @ T16-T17"
overview: >-
  IDEA-0025 taken up: all 53 elements across the 15 conforming CMPs
  now carry typed Uses: lines -- 71 edges, 100% (interface), 20
  explicit Uses: none -- derived by the ratified three-pass
  methodology (extract all element references incl. intra-component
  from contract prose with the 26 untyped depends-on edges as
  completeness map; classify by the could-build-against-contract-
  alone test; reconcile cross-component projection mechanically per
  DEC-0309 both directions). Conventions ratified: explicit
  qualifiers on every edge (checker accepts SPEC-default omission);
  bare-element targets where prose names no contract item;
  MechanicalWriteService item numbering by list order. Zero
  (implementation) edges -- SP-0014's build-order/serialization
  rules are therefore vacuously satisfied. Zero (test) edges written
  (DEC-0306 requires owned test-double elements, none exist); three
  promotion candidates flagged: CMP-0005's local-git fake connector,
  CMP-0008's in-memory fake adapter, CMP-0009's conformance-parity
  tie to CMP-0005's fake. Two edges target A-3/A-4 of the
  MechanicalWriteService range disputed by IDEA-0026, inside its
  undisputed portion; IDEA-0026 inherits the affected-edge note.
links:
  derives-from: [SES-0066]
  relates-to: [DEC-0299, DEC-0306, DEC-0309, DEC-0358, SP-0013, IDEA-0025]
---

## Context

SP-0013's projection found zero typed `Uses:` lines anywhere across the 16 approved CMPs despite the DEC-0299/DEC-0306/DEC-0309 mandate. IDEA-0025 proposed backfilling them and arming checker enforcement in the same take-up. SES-0066 took up IDEA-0025 and executed the backfill: 53 elements across the 15 conforming CMPs (CMP-0006 carved out as a non-conforming draft stub) needed classified, typed `Uses:` edges.

## Decision

The corpus-wide typed `Uses:` backfill is executed. All 53 elements across the 15 conforming CMPs now carry typed `Uses:` lines: 71 edges, 100% `(interface)`, and 20 explicit `Uses: none` declarations. The edges were derived by the ratified three-pass methodology: (1) extract all element references, including intra-component ones, from contract-item prose, using the corpus's 26 pre-existing untyped `depends-on` edges as a completeness map only, never as source of truth; (2) classify each edge by the "could a team build this element to completion given only the provider's contract" test — yes = `(interface)`, no = `(implementation)`; (3) reconcile the cross-component subset mechanically against frontmatter `depends-on` per DEC-0309, in both directions.

Ratified conventions: every edge carries an explicit qualifier for documentary clarity, even though the checker accepts qualifier omission as the SPEC-default `(interface)`; targets that name an element without naming a specific contract item are written as bare-element edges rather than inventing an item; `MechanicalWriteService`'s disputed item range is numbered by list order for edge-targeting purposes, corroborated by CMP-0001's own "MechanicalWriteService.A-1/A-2" append-turn/close-session delegation cite.

Zero `(implementation)` edges resulted — the stakeholder explicitly acknowledged this means SP-0014's build-order/serialization rules are vacuously satisfied against this data. Zero `(test)` edges were written: DEC-0306 requires a `(test)` edge to target an owned, specified test-double element, and none exist yet in the corpus. Three promotion candidates are flagged for future DEC-0306 promotion work, not written this backfill: CMP-0005's local-git fake connector, CMP-0008's in-memory fake adapter, and CMP-0009's conformance-parity tie to CMP-0005's fake.

Two written edges target the `MechanicalWriteService` item range disputed by IDEA-0026 (CMP-0001 gives A-1..A-10, CMP-0004 gives A-1..A-8): `StalenessSweepService` and `ReaffirmationService` (both in CMP-0004) target members A-3/A-4, inside the undisputed portion of the range in both variants. IDEA-0026 inherits this affected-edge note as part of its own resolution.

IDEA-0025 is set to `taken-up`, this session (SES-0066) being its take-up intake.

## Rationale

The mandate (DEC-0299/DEC-0306/DEC-0309) was fully specified in SPEC-design-elements; the gap was purely unexecuted backfill, not a design defect. Executing it now, via a system-architect-ratified derivation methodology with explicit stakeholder disposition of the qualifier distribution and every escalation, closes the corpus's largest outstanding SPEC-compliance gap and gives SP-0014 real (if `(implementation)`-vacuous) typed edge data to fire against.

## Alternatives Considered

A partial or CMP-by-CMP incremental backfill was implicitly rejected in favor of a single batched session: the mandate is corpus-wide and SP-0014 is blocked on completion, not partial progress (DEC-0358). Force-typing ambiguous edges rather than escalating them to the stakeholder was rejected by the ratified methodology, which requires every ambiguous or `(implementation)`-candidate edge to be walked individually.

## Implications

SP-0014's DEC-0358 precondition is satisfied (decision 7, this session). IDEA-0026's contract-item-range dispute inherits the two-edge affected list noted above. The three flagged `(test)`-promotion candidates remain open work, not committed to by this decision. tools/check_links.py rule 20 (decision 2, this session) now enforces the mandate going forward against this corpus state.
