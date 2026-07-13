---
id: DEC-0501
type: decision
title: "Preview grilling cards always carry at least two questions"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0093 @ T2, T4, T8"
overview: >-
  Experiments in this session showed a single-question preview-
  layout grilling card forces a choice between selecting an option
  and attaching a free-text note: confirming a note with no
  selection submits the card immediately, and the two cannot
  combine. A card of two or more questions gains a Submit tab that
  allows a stakeholder to select an option, return to its tab,
  attach a note, and submit both together. This decision requires
  every preview-layout card the facilitator sends to carry at least
  two questions, adding a genuine rider question when a grilling
  round has only one substantive question, and has the preceding
  chat message teach the select-then-annotate-then-submit sequence.
links:
  relates-to: [DEC-0472, DEC-0499, DEC-0500, DEC-0502]
  derives-from: [SES-0093]
---

# DEC-0501: Preview grilling cards always carry at least two questions

## Context

This session's experiments showed that on a single-question card, confirming a note submits the card immediately with no option selected — selection and note are mutually exclusive. On a card of two or more questions, which gains an explicit Submit tab, a stakeholder can select an option, navigate back to its tab, attach a note, and submit both together.

## Decision

The facilitator never sends a single-question preview-layout card. Every preview card carries at least two questions; when a grilling round has only one substantive question, a genuinely useful rider question — scheduling, scope, priority, or similar — is added. The chat message preceding the card teaches the sequence: select an answer (Enter advances), answer the remaining questions, arrow back to the earlier tab, press n, type the note, press Enter, then Submit.

## Rationale

A selection with an attached caveat is the answer shape grilling most wants to support, and it is only reachable on multi-question cards.

## Alternatives Considered

Accepting that single-question cards force a choice between an option and free text, which loses the caveat channel. Padding cards with throwaway questions, rejected because rider questions must be genuine — a padding question wastes stakeholder attention.

## Implications

Grilling rounds already batch questions, so the rule costs little; card authoring assumes two to four questions per card.
