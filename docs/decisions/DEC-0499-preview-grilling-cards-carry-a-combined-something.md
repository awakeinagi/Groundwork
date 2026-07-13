---
id: DEC-0499
type: decision
title: "Preview grilling cards carry a combined \"Something else/Please elaborate\" option"
status: accepted
owner: awakeinagi
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0093 @ T5, T8"
overview: >-
  Preview-layout grilling cards (DEC-0472) suppress the automatic
  Other option, so DEC-0473's Other-routed elaborate keyword had no
  channel to route through. This decision retires that mechanism and
  gives every preview card a single listed option, labeled
  "Something else/Please elaborate", whose preview text explains
  itself: a note attached to it is a free-text answer or amendment,
  and a blank note is the elaborate directive, expanding the
  question with context, examples, and an alternatives
  compare/contrast. The option supersedes DEC-0473's keyword hint
  and DEC-0460's verbatim label, honors DEC-0074's always-visible
  affordance guarantee, and caps substantive alternatives at three
  per card, splitting genuinely four-way questions across two cards.
links:
  relates-to: [DEC-0472, DEC-0074, DEC-0500, DEC-0501, DEC-0502, DEC-0503]
  derives-from: [SES-0093]
  supersedes: [DEC-0473]
---

# DEC-0499: Preview grilling cards carry a combined "Something else/Please elaborate" option

## Context

DEC-0473 made the automatic Other option the elaborate-keyword channel for three-and-four-alternative grilling cards, on the stated premise that Other is harness-documented as always available. Controlled experiments in this session (2026-07-13) showed that preview-layout cards — the layout DEC-0472 mandates for grilling — suppress the Other option entirely, so the keyword channel did not exist on exactly the cards that needed it. The same experiments showed per-selection notes round-trip reliably and that the returned payload distinguishes a bare selection from a selection with an attached note.

## Decision

Every preview-layout grilling card ends with a listed option labeled "Something else/Please elaborate" whose preview reads verbatim: "Use notes to type your own response or request the agent to provide additional information. A blank notes section implies that you would like the agent to elaborate on the question with examples (where possible)." Selecting it with an attached note is a free-text answer, amendment, or information request. Selecting it with blank notes is the elaborate directive: the facilitator expands the question — what is being decided, why it matters now, concrete examples, and a compare/contrast of the alternatives — and re-presents the card. Any note resembling "I don't understand" or "please explain" is treated as the elaborate directive unless the stakeholder states specifically what help they need. Substantive alternatives cap at three per card; a genuinely four-way question is split across two cards.

## Rationale

A single option slot serves both the free-text and the elaborate affordances. A listed option is discoverable where a keyboard shortcut or a typed keyword is not, honoring DEC-0074's always-visible affordance guarantee at the method level. The option's own preview pane documents how to use it, and the blank-note convention is unambiguous in the returned payload, which carries the selected label with or without a notes suffix.

## Alternatives Considered

Routing the keyword through Other, which is impossible because preview layout suppresses Other. A question-text hint pointing at the n-key notes shortcut, which works but is poorly discoverable and clutters every question. Two separate listed options for free text and elaborate, which costs a second slot and caps substantive alternatives at two.

## Implications

DEC-0460's verbatim elaborate label and DEC-0473's keyword hint are retired everywhere. The groundwork-design-session playbook's three-affordances section is rewritten to match. The thirty-one-character label wraps to two rows in the fixed option column, which is cosmetic only.
