---
id: DEC-0486
type: decision
title: "Five contract shapes settle at EP-0010's gate; remaining surfaces defer downstream"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T4-T5"
overview: >-
  EP-0010's draft listed eight interfaces/contracts to define,
  needing a decision on which settle at the epic gate. This decision
  settles five at the gate — kernel operation catalog, schema
  contract shape and compatibility rules, schema-
  versioning/migration contract, rule-family hosting contract,
  single-session concurrency invariants — and defers per-type schema
  details, port specifics, and instrumentation points downstream,
  with the compliance definition due before EP-0013's stories begin.
links:
  relates-to: [DEC-0476, DEC-0485]
  derives-from: [SES-0091]
---

# DEC-0486: Five contract shapes settle at EP-0010's gate; remaining surfaces defer downstream

## Context

EP-0010's draft listed eight interfaces and contracts to define, and the epic needed to decide which are epic-level decisions and which defer.

## Decision

Five contract shapes settle at EP-0010's gate: the kernel operation catalog, the artifact-model schema contract shape with its compatibility rules, the schema-versioning and migration contract, the rule-family hosting contract, and the single-session concurrency invariant model. The remaining surfaces defer: per-type schema details, port interface specifics, and instrumentation points to component docs, while the compliance definition emerges from EP-0010's stories and is due before EP-0013's stories begin rather than at this gate.

## Rationale

Epic level settles what would force rework across sibling epics if wrong; the deferred surfaces have downstream consumers that tolerate late definition. The advisor debate converged here after the record-grounded instance conceded the concurrency write path to epic level.

## Alternatives Considered

Settling all eight at the gate was rejected as premature fine granularity. Settling only three was rejected because EP-0015 cannot design without concurrency entitlements.

## Implications

EP-0010's Interfaces & Contracts section records a disposition per surface, and the compliance definition's due date becomes a cross-epic ordering constraint against EP-0013.
