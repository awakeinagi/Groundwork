---
id: DEC-0051
type: decision
title: Distilled decisions are confirmed in-session before acceptance
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  At natural checkpoints (topic close, session end) the agent plays back
  proposed decisions in plain language and the participant confirms or corrects
  while present. Confirmed decisions commit to the item branch as accepted, with
  the confirmation exchange itself in the transcript; the item's PR gate remains
  final ratification. This catches distillation errors at the source by the only
  person who knows what they meant, making the confirmation exchange part of the
  provenance chain. Sessions auto-closed for inactivity commit only confirmed
  decisions; the rest stay proposed (DEC-0057).
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T2-T3"
links:
  derives-from: [SES-0006]
---

# DEC-0051: In-session confirmation of distilled decisions

## Context

The distillation-faithfulness risk: a Decision record may state something
the participant didn't quite mean, and the PR approver is often not the
person whose words were distilled.

## Decision

At natural checkpoints (topic close, session end) the agent plays back
proposed Decisions in plain language and the participant confirms or
corrects while present. Confirmed DECs commit to the item branch as
`accepted`, with the confirmation exchange itself in the transcript; the
item's PR gate remains final ratification.

## Rationale

Distillation errors are caught at the source by the only person who knows
what they meant; the confirmation becomes part of the provenance chain.

## Alternatives Considered

- **Gate review only**: misreadings survive until a contract dispute.
- **Async confirmation window**: pipeline waits on inbox archaeology.

## Implications

Playback checkpoints are strategy-pack behavior
(DEC-0053); sessions auto-closed
for inactivity commit only confirmed DECs, the rest staying `proposed`
(DEC-0057).
