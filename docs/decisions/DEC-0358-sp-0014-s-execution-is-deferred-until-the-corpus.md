---
id: DEC-0358
type: decision
title: "SP-0014's execution is deferred until the corpus-wide Uses: backfill completes"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-10
source-span: "SES-0064 @ T22"
overview: >-
  SP-0013's findings (approved spike) found zero typed Uses: lines
  anywhere in the 16 approved CMPs: the DEC-0299/DEC-0306/DEC-0309
  typed-dependency mechanism is SPEC-mandated but corpus-absent,
  leaving only 26 untyped component depends-on edges as structural
  dependency data. SP-0014 (structural design-rule precision)
  depends on that typed data to fire dependency-cycle, stability-
  direction, and build-order rules meaningfully -- without it,
  roughly half its planned rulebase has no data to fire against. At
  SES-0064 T22 the stakeholder chose, over proceeding now with a
  reduced rulebase that skips the data-dependent rules, to defer
  SP-0014's execution entirely until the Uses: backfill (captured as
  an Idea at this session) is taken up and completed. SP-0014 gains
  a body note recording this precondition. Relates to DEC-0299 and
  DEC-0309 (the typed-edge mechanism whose absence forced the
  choice) and to SP-0013's findings as the evidentiary basis.
links:
  derives-from: [SES-0064]
  relates-to: [DEC-0299, DEC-0309, SP-0013]
---

## Context

SP-0013 (approved, executed by a sandboxed executor subagent per SES-0064 T19-T20) found that despite DEC-0299's mandated typed `Uses:` line (interface | implementation | test), extended to test doubles by DEC-0306 and lifted to component grain by DEC-0309, zero `Uses:` lines exist anywhere across the 16 approved CMPs. The mechanism is SPEC-mandated but corpus-absent: the docs predate the mandate, were never backfilled, and `tools/check_links.py` does not flag the gap. SP-0014 (structural design-rule precision) is the next spike in the EP-0009 program; roughly half its planned rulebase (dependency-cycle, stability-direction, build-order rules) requires the typed element-grain edges DEC-0309 makes the source of truth for component-level `depends-on`. Without them that half of the rulebase has no data to fire against.

## Decision

SP-0014's execution is deferred until the corpus-wide `Uses:` backfill (captured as an Idea at this session) is taken up and completed. SP-0014 does not proceed with a reduced rulebase in the interim.

## Rationale

At SES-0064 T22 the stakeholder was presented the choice between a reduced rulebase (dropping or stubbing the edge-dependent rules so SP-0014 could proceed now) and full deferral until the backfill lands, and selected the latter: SP-0014's evidentiary value depends on exercising the complete rulebase DEC-0354's program specified, and firing a partial rulebase against absent data would produce a distorted read on rule precision rather than genuine evidence.

## Alternatives Considered

A reduced rulebase proceeding now with only the DEC-independent structural rules (orphaned interfaces, citation integrity, mandatory-contract-kind completeness) was rejected: it would understate SP-0014's evidentiary value for the executable-design-knowledge approach (DEC-0354) and could not exercise the dependency-cycle/stability-direction/build-order half of the planned rulebase at all.

## Implications

SP-0014 gains a body note recording this precondition, citing this decision. The corpus-wide `Uses:` backfill is captured as an Idea and, per DEC-0267, its eventual take-up must run the full amendment cascade since it modifies approved CMPs. SP-0016 and SP-0017, both impacted-by SP-0014, remain queued behind it.
