---
id: DEC-0472
type: decision
title: "Grilling cards use preview layout with consequence-sketch previews"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Every grilling question card uses the AskUserQuestion preview
  layout: each substantive option carries a preview whose content is
  a consequence sketch — a concrete illustration of what choosing
  that option means, never a restatement of the option label. The
  elaborate option's preview lists what the expansion will cover.
  Because the harness supports previews only on single-select
  questions, grilling questions are phrased single-select wherever
  feasible; when a question is genuinely multi-select, the card
  drops to plain layout and its question text discloses that per-
  choice notes are unavailable and caveats route through Other.
  Decided in SES-0090 (T4-T9), confirmed by the stakeholder, and is
  a precondition for DEC-0460 and DEC-0461's same-session
  supersession, both of which relied on preview layout for their
  notes and keyword-fallback guarantees. Relates to DEC-0074's
  product-side affordance guarantee at the method level.
links:
  derives-from: [SES-0090]
  relates-to: [DEC-0074]
---

# DEC-0472: Grilling cards use preview layout with consequence-sketch previews

## Context

DEC-0460 and DEC-0461 (SES-0088) established that grilling question cards carry an explicit elaborate option and treat notes-on-selection and free-text as first-class affordances, but both decisions assumed the harness's plain question-card layout and pointed keyword fallbacks and custom answers at "the free-text field." The stakeholder asked (SES-0090 T1) that grilling rounds instead use the AskUserQuestion preview layout, with the automatic "Other" option carrying free-text. The T5 option survey found previews are single-select only, that any card with a preview switches the whole card to a side-by-side layout, and that the harness ties per-selection notes to that same preview layout — leaving open what preview content grilling options should carry and how a genuinely multi-select question is handled.

## Decision

Every grilling question card uses the AskUserQuestion preview layout: each substantive option carries a preview whose content is a consequence sketch — a concrete illustration of what choosing that option means (an example, mock, or resulting state, roughly two to eight lines), never a restatement of the option label. The elaborate option's preview lists what the expansion will cover. Because the harness supports previews only on single-select questions, grilling questions are phrased single-select wherever feasible; when a question is genuinely multi-select, the card drops to plain layout and its question text states that per-choice notes are unavailable and caveats route through Other — the affordance loss is disclosed, never silent.

## Rationale

The stakeholder's T1 proposal and T7 selection both favored preview layout as the default, and the T5 survey confirmed previews are the only way to expose per-selection notes in this harness, making preview layout a precondition for DEC-0461's notes channel rather than an independent stylistic choice. Requiring a consequence sketch (T7, Q3) rather than a bare restatement of the option label makes previews carry decision-relevant information instead of empty affordance. Disclosing the affordance loss on multi-select cards, rather than silently dropping notes, keeps the facilitator's practice honest about what a given card can and cannot offer.

## Alternatives Considered

Minimal token previews (a short label duplicating the option text) were considered and rejected at T7 as adding UI complexity without adding decision-relevant content. A structured mini-compare preview (a table-like breakdown per option) was considered and rejected as heavier than needed for most grilling questions, though nothing forbids using one where a question warrants it. Banning multiSelect grilling questions outright, or silently falling back to plain layout without disclosure, were both considered against the multi-select tension (T6 Q1) and rejected in favor of the single-select-first rule with a stated, disclosed plain-layout fallback.

## Implications

This decision is a precondition for DEC-0460 and DEC-0461's supersession: both are being replaced in the same session (SES-0090) to point their keyword-fallback and free-text guarantees at "Other" under this preview-layout requirement rather than at the inline free-text field, which this session's T5 survey found may not reliably survive in preview mode. The groundwork-design-session skill's refinement-process reference needs its grilling section updated to state the preview-layout requirement, the consequence-sketch preview content rule, and the disclosed multi-select fallback.
