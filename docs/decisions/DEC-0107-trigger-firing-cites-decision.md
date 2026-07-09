---
id: DEC-0107
type: decision
title: Firing or retiring a trigger cites a decision
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0017 @ T4-T5"
links:
  derives-from: [SES-0017]
  relates-to: [DEC-0100, DEC-0106]
---

# DEC-0107: Firing or Retiring a Trigger Cites a Decision

## Context

A trigger fires when someone observes its condition holds. Is that
observation provenance-worthy, or a mechanical registry edit?

## Decision

Firing a trigger requires a decision (derived from a session or spike)
recording the observation that the condition holds. The consequence
executes citing that same decision — since revival already requires a
citation (DEC-0100), one
decision serves both the firing and the revival, no double ceremony.
The registry entry flips to `fired` with the date, the decision link,
and the outcome. Retiring a no-longer-relevant trigger works
identically with `retired`.

## Rationale

"We now need multi-node" is a design event with consequences measured in
infrastructure — exactly the record-when-hard-to-reverse bar. The
in-place `**Fired:**` line keeps the registry self-explanatory without
git archaeology.

## Alternatives Considered

- **Mechanical fire, decision only on the consequence**: one less step,
  but the observation itself — why we believe the condition holds — goes
  unrecorded.

## Implications

The checker requires fired/retired entries to carry a decision link
(DEC-0108).
