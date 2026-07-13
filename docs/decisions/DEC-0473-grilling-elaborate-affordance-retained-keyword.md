---
id: DEC-0473
type: decision
title: "Grilling elaborate affordance retained; keyword fallback routes through Other"
status: superseded
superseded-by: [DEC-0499]
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0090 @ T4-T9"
overview: >-
  Every structured grilling question card the facilitator presents
  includes an explicit elaboration affordance, unchanged in
  substance from DEC-0460 (verbatim label, two-alternative listed-
  option threshold, the 'I don't understand' catch). Only the
  keyword-fallback channel for three-and-four-alternative cards
  changes: it now routes through the automatic Other option rather
  than 'the free-text field,' because DEC-0472 makes preview layout
  the default for grilling cards and the T5 option survey found the
  inline free-text field is not reliably present in preview mode,
  while Other is harness-documented as always available. Decided in
  SES-0090 (T4-T9), confirmed by the stakeholder, superseding
  DEC-0460 and relating to DEC-0472's preview-layout precondition
  and to DEC-0074's product-side elaborate affordance.
links:
  relates-to: [DEC-0074, DEC-0472]
  derives-from: [SES-0090]
  supersedes: [DEC-0460]
---

# DEC-0473: Grilling elaborate affordance retained; keyword fallback routes through Other

## Context

DEC-0460 (SES-0088) established that grilling question cards carry an explicit elaborate option, with a keyword fallback pointed at "the free-text field" for cards with three or four substantive alternatives. SES-0090 requires grilling cards to use the AskUserQuestion preview layout (DEC-0472), and the T5 option survey found the inline "Type something" free-text field may not reliably be present once a card carries previews, leaving the automatic "Other" option as the only affordance the harness guarantees regardless of layout. DEC-0460's keyword-fallback wording needed to be updated to match.

## Decision

Every structured grilling question card the facilitator presents in a session includes an explicit elaboration affordance, with no exceptions by question kind (confirmations included). When a card carries at most two substantive alternatives, it includes a selectable option labeled verbatim "Please elaborate on what needs to be decided here, include examples where helpful"; choosing it has the facilitator expand the question — what is being decided, why it matters now, concrete examples, and a detailed compare/contrast of the alternatives — and then re-present the card. When a question needs three or four substantive alternatives, the listed option is dropped and the question text instead ends with a hint that choosing Other and typing `elaborate` triggers the same behavior; with grilling cards in preview layout (DEC-0472) the inline free-text field is not reliably present, so the automatic Other option — not the inline field — is the sanctioned keyword channel. Any stakeholder answer resembling "I don't understand" or "please explain" is treated as this elaboration directive unless the stakeholder states specifically what help they need.

## Rationale

The elaborate affordance itself is unchanged from DEC-0460 — the stakeholder's SES-0090 T7/T9 ratification kept the verbatim label, the two-alternative listed-option threshold, and the "I don't understand" catch as-is. Only the keyword-fallback channel changes, and only because DEC-0472 makes preview layout the default: the T5 survey found no doc-backed guarantee that the inline free-text field survives in preview mode, while the automatic Other option is harness-documented as always available regardless of layout, making it the only reliable keyword channel once cards carry previews.

## Alternatives Considered

Leaving the fallback wording pointed at "the free-text field" was rejected because DEC-0472's preview-layout requirement puts that field's presence in doubt; retaining stale wording would describe a channel that may not exist. Dropping the keyword-fallback affordance entirely for three-and-four-alternative cards was not raised and would contradict DEC-0460's no-exceptions-by-question-kind guarantee, which this decision preserves. Amending DEC-0460 in place rather than superseding it was rejected because DEC-0460 is an accepted decision; amendment of accepted decisions is refused by the write API, and supersession is the sanctioned repair (DEC-0267).

## Implications

This decision supersedes DEC-0460 in full; ratified citers of DEC-0460 should be reviewed for staleness against the new Other-routed keyword-fallback wording. It relates to DEC-0472 (the preview-layout precondition this fallback change depends on) and to DEC-0074 (the product-side always-present elaborate affordance this decision continues to mirror at the method level). The groundwork-design-session skill's refinement-process reference needs its grilling section's keyword-fallback wording updated from "the free-text field" to "Other."
