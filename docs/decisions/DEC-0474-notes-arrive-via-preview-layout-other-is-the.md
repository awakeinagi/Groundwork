---
id: DEC-0474
type: decision
title: "Notes arrive via preview layout; Other is the guaranteed free-text channel"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0090 @ T4-T9"
overview: >-
  The facilitator's first-class treatment of notes-on-selection is
  unchanged from DEC-0461, but the guaranteed free-text channel
  changes from the inline 'Type something' field to the automatic
  Other option. Preview-layout cards (DEC-0472) are what expose per-
  selection notes at all (the harness documents its answer-
  annotations channel as 'notes on preview selections'), and the T5
  option survey found the inline field may vanish in preview mode,
  retiring DEC-0461's never-suppressed guarantee about it; Other is
  harness-documented as always available and takes over as the
  guaranteed channel. Harness fallbacks for tools lacking native
  notes or structured cards (GitHub Copilot CLI, Amp) are unchanged.
  Decided in SES-0090 (T4-T9), confirmed by the stakeholder,
  superseding DEC-0461 and relating to DEC-0472's preview-layout
  precondition and to DEC-0074's product-side affordance set.
links:
  relates-to: [DEC-0074, DEC-0472]
  derives-from: [SES-0090]
  supersedes: [DEC-0461]
---

# DEC-0474: Notes arrive via preview layout; Other is the guaranteed free-text channel

## Context

DEC-0461 (SES-0088) established notes-on-selection and free-text as first-class grilling affordances, stating the automatic free-text field is "never suppressed" and pointing keyword fallbacks at that same field. SES-0090's T5 option survey found the harness ties per-selection notes specifically to preview-layout cards (the answer-annotations channel is documented as "notes on preview selections"), and that the inline "Type something" field may vanish once a card carries previews — directly contradicting DEC-0461's never-suppressed guarantee now that DEC-0472 makes preview layout the default for grilling cards.

## Decision

The facilitator treats the harness's native notes-on-selection as a first-class channel: free-text notes attached to any chosen option are design input — amendments, caveats, and upgrades to the chosen option — never noise. In Claude Code, per-selection notes are a preview-layout feature (the harness documents its answer-annotations channel as "notes on preview selections"), which is why grilling cards carry previews (DEC-0472). The guaranteed free-text affordance is the automatic "Other" option, which the harness documents as always available; a custom answer through Other is always as valid as a listed option. The inline "Type something" field is not relied upon — first-hand observation recorded in SES-0090 is that it may vanish in preview mode, retiring the superseded guarantee that it is never suppressed. On harnesses without native per-selection notes (GitHub Copilot CLI's ask_user) or without structured question cards at all (stock Amp), the elaborate keyword and whatever free-text channel exists substitute for the missing affordances.

## Rationale

DEC-0461's first-class-notes-channel principle is unchanged and reaffirmed by the stakeholder's SES-0090 T7/T9 ratification. What changes is which affordance is documented as guaranteed: the T5 survey found the harness's own documentation ties notes to preview layout and offers no guarantee about the inline free-text field's presence under previews, while it does document Other as always selectable. Downgrading the inline field from a stated guarantee to an unrelied-upon first-hand observation, and promoting Other to the guaranteed channel, keeps the decision's claims within what the harness actually documents rather than what was previously assumed.

## Alternatives Considered

Keeping "the free-text field is never suppressed" as written was rejected because it is contradicted by preview-mode behavior once DEC-0472 makes preview layout the default — retaining it would leave an accepted decision asserting something the facilitator has observed to be false. Treating the inline field's possible disappearance as disqualifying for preview layout altogether (staying on plain layout to preserve the old guarantee) was rejected at T7 in favor of preview layout, since preview layout is what makes notes-on-selection possible at all — the very affordance this decision protects. Amending DEC-0461 in place was rejected for the same reason as DEC-0460's supersession: accepted decisions are immutable, and supersession is the sanctioned repair (DEC-0267).

## Implications

This decision supersedes DEC-0461 in full; ratified citers of DEC-0461 should be reviewed for staleness against the retired never-suppressed guarantee. It relates to DEC-0472 (the preview-layout precondition notes now depend on) and to DEC-0074 (the product-side affordance set this decision continues to mirror at the method level). The groundwork-design-session skill's refinement-process reference needs its grilling section updated to drop the "free-text field is never suppressed" claim and state Other as the guaranteed free-text channel, with the inline field noted only as an unrelied-upon convenience.
