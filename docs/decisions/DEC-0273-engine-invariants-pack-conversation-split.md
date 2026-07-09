---
id: DEC-0273
type: decision
title: The application splits intake into engine-enforced invariants and pack-defined conversation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0273 constrains the application's intake implementation to split
  the paradigm's change-intake protocol into two layers: the session
  engine enforces hard invariants (intake-opened sessions begin at
  verbatim proposal, authority check runs at open, grilling requires
  typed alignment confirmation, modified-artifacts sessions cannot close
  until staleness cascade is marked); the conversational protocol
  (restatement quality, alignment loop phrasing, locate-first steps, path
  recommendation) is strategy-pack content, improvable through the gated
  pack pipeline.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T4-T5"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0252, DEC-0053]
---

# DEC-0273: Engine invariants, pack conversation

## Context

IDEA-0001 asks the application to embody the paradigm's change-intake
protocol (SES-0050). The protocol has two natures: hard invariants
(the record opens at the verbatim proposal, the authority check gates
open, the session rule has no waiver) and conversational behavior (the
restate-and-align loop, locate-first exploration, path
recommendation). Where does each live?

## Decision

The session engine's contract enforces the invariants that must never
be bypassable: intake-opened sessions begin their transcript at the
verbatim proposal, the authority check runs at open, grilling does not
begin before a typed alignment confirmation exists, and a session that
modified approved artifacts cannot close until the staleness cascade
is marked (DEC-0279). The conversational protocol — restatement
quality, the alignment loop's phrasing, locate-first steps, the path
recommendation — is strategy-pack content (DEC-0275), improvable
through the PR-gated, eval-gated pack pipeline.

## Rationale

DEC-0252 is a hard rule; structural enforcement beats tested policy
for a provenance guarantee. Grilling style has always been pack
territory (DEC-0053) — baking conversational policy into engine code
would make every intake-quality improvement an engine release.

## Alternatives Considered

- **All in packs**: maximally configurable, but a pack edit could then
  waive the no-waiver rule — exactly what DEC-0252 rejects.
- **All in engine**: non-bypassable end to end, but cuts against
  DEC-0053's whole design for conversational behavior.

## Implications

ST-0032 carries the invariant amendments; ST-0033's pack set gains the
change-intake pack (DEC-0275); the alignment invariant keys on the
typed alignment card (DEC-0280).
