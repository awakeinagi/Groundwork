---
id: DEC-0432
type: decision
title: "Process-knowledge structuring is deferred until the application's facilitation is built"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T10, T11, T18, T21, T31"
accepted-in: SES-0082
overview: >-
  Grilling playbooks, the intake protocol, and gate criteria remain
  canonical as prose in the skills. Structuring into machine-
  readable definitions is deferred until the application's
  facilitation engine is actually being built, extracting only
  decidable parts (gate checklists first); judgment-laden
  facilitation stays prose. DEC-0336's boundary ruling on BG-0002's
  admission predicate travels with that future work.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0336, BG-0002, DEC-0310]
---

# DEC-0432: Process-knowledge structuring is deferred until the application's facilitation is built

## Context

The converged architecture proposal included a fourth component — structured process definitions — alongside the engine, CLI adapter, and application backend. SES-0082 needed to decide when the paradigm's process knowledge (grilling playbooks, intake protocol, gate criteria) actually needs to move out of prose skills into structured, machine-readable form, and to reconcile that with DEC-0336's existing boundary ruling on BG-0002's admission predicate.

## Decision

The paradigm's process knowledge — grilling playbooks, the intake protocol, and gate criteria — remains canonical as prose in the skills. Extraction into structured, machine-readable definitions is deferred until the application's facilitation engine is actually being built, and then extracts only the decidable parts, gate checklists first, while judgment-laden facilitation stays prose. The DEC-0336 boundary ruling on whether such definitions fall under BG-0002's admission predicate travels with that future work.

## Rationale

This follows the same deferred-extraction discipline as DEC-D's engine and DEC-J's projection tooling: structuring process knowledge has no real consumer until an application facilitation engine exists to consume it, so building it now would be speculative. Splitting "decidable parts" (gate checklists) from "judgment-laden facilitation" (grilling technique) up front avoids a false-precision trap — some of this knowledge genuinely resists structured encoding and should stay prose even after extraction begins.

## Alternatives Considered

Structuring all process knowledge now, ahead of the application, was rejected as premature — mirroring DEC-D's engine-extraction reasoning. Structuring nothing ever, keeping everything permanently as prose even once an application facilitation engine exists, was rejected — gate checklists in particular are genuinely decidable and would benefit a facilitation engine that needs machine-checkable criteria.

## Implications

No structuring work is chartered by this decision. DEC-0336's boundary ruling remains the live reference for whether future structured-definition work counts as BG-0002 scope; it is not re-litigated here. When the application's facilitation engine work eventually starts, gate checklists should be the first extraction target.
