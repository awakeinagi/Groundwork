---
id: SES-0090
type: session
title: "Grilling rounds use preview-layout cards; Other as the free-text channel"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-13
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: verbatim
kind: expedited
intake: {origin: user, proposed-by: awakeinagi}
overview: >-
  Expedited method-level change-intake session, now closed: the
  stakeholder asked that every grilling-round question card use the
  preview layout, with the automatic "Other" option serving as the
  free-text channel for custom answers. The facilitator's T2
  restatement mis-cited its preview/notes findings as coming from
  "SES-0088/SES-0089"; T4 corrects this — SES-0089 is the unrelated
  BG-0002 epic-derivation session, and the findings originated in
  facilitator working memory, substantiated fresh at T5 by a
  documentation-based option survey. The session settled three
  tensions: a single-select-first rule with a disclosed plain-layout
  fallback for genuinely multi-select grilling questions;
  superseding DEC-0460 and DEC-0461 to point their free-text
  guarantees at Other, layered on a new preview-layout decision; and
  a consequence-sketch rule for preview content. The stakeholder
  ratified all three options (T7, T9), producing DEC-0472 (preview
  layout with consequence-sketch previews), DEC-0473 (supersedes
  DEC-0460), and DEC-0474 (supersedes DEC-0461). Post-ratification
  consistency checks (T10) found DEC-0074's ratified citers already
  tracked under IDEA-0063 and no stale ratified citers of DEC-0460
  or DEC-0461. The decision-recall audit (T11) over the three new
  decisions found zero content-relevant gaps. T12 corroborated the
  preview free-text-suppression observation against GitHub issue
  #27348. T13 applied all three decisions to the groundwork-design-
  session skill's grilling-process reference. The stakeholder closed
  the session with no new ideas to capture (T15).
links:
  relates-to: [SES-0088, DEC-0460, DEC-0461, DEC-0472, DEC-0473, DEC-0474]
---

# SES-0090: Grilling rounds use preview-layout cards; Other as the free-text channel

## Purpose

To refine a stakeholder-proposed change requiring every grilling-round question card to use the preview layout, and to establish the automatic "Other" option as the sanctioned free-text channel now that the inline free-text field may not survive in that layout — reconciling this with DEC-0460 and DEC-0461 from SES-0088.

## Transcript

### T1

(stakeholder, verbatim proposal): "I'd like the grilling rounds to use preview-layout cards. The Other choice can serve as the option where a user writes a custom response with free-text."

### T2

(facilitator, restatement): Restated the intent as: every grilling-round AskUserQuestion card should use the preview layout (each substantive option carries a preview field) rather than the plain layout, because the notes affordance only exists on preview-layout cards (SES-0088/SES-0089 findings); and since the inline "Type something" free-text field may vanish in preview mode, the automatic "Other" option becomes the sanctioned free-text channel — custom answers and the elaborate keyword route through it. Surfaced three tensions for the session to settle: (1) previews are only supported on single-select questions, so multiSelect grilling cards would either lose the notes affordance or need rephrasing as single-select — a rule is needed; (2) DEC-0460 and DEC-0461's wording ("the free-text field is never suppressed"; keyword-elaborate fallback pointing at "the free-text field") needs amending or superseding to point at "Other," plus the new preview-layout requirement on top; (3) a rule is needed for what preview content on grilling options contains, including for the verbatim "Please elaborate…" option. Recommended the expedited path (DEC-0254).

### T3

(stakeholder): Confirmed alignment with the restatement: "Yes open the expedited session."

### T4

(facilitator, correction to T2): "Correction: T2's citation '(SES-0088/SES-0089 findings)' is wrong. Corpus SES-0089 is the unrelated epic-derivation session for BG-0002, and SES-0088 documents no preview-layout findings. The preview/notes/field-vanish observations originated in the facilitator's working memory from the 2026-07-12 conversation that produced SES-0088, mis-attributed there to 'SES-0089'. They are substantiated fresh in this session by the option survey at T5."

### T5

(facilitator, option survey, DEC-0337 sizing: harness documentation, in-session): "Claude Code's AskUserQuestion tool documentation states: (a) previews are supported only on single-select questions, not multiSelect; (b) when any option has a preview, the UI switches to a side-by-side layout with the option list on the left and preview on the right; (c) the answer-annotations channel is described as 'notes on preview selections,' tying per-selection notes to preview layout; (d) users are always able to select 'Other' to provide custom text input. First-hand observation, not doc-backed: the inline 'Type something' free-text field may vanish in preview mode."

### T6

(facilitator): "Presented the expedited round as three preview-layout cards, practicing the proposal itself: Q1 — rule for genuinely multi-select grilling questions (options: single-select first with stated plain fallback; ban multiSelect; allow plain multiSelect silently); Q2 — shape of the decision-record change given DEC-0461's 'never suppressed' guarantee is contradicted in preview mode (options: supersede DEC-0460 and DEC-0461 plus a new preview DEC; layer one new DEC on top; elaborate); Q3 — required preview content (options: consequence sketch; minimal token previews; structured mini-compare). Each card carried consequence-sketch previews; keyword-elaborate hints routed through Other."

### T7

(stakeholder): "Chose the recommended option on all three cards: Q1 single-select first with stated plain fallback; Q2 supersede DEC-0460 and DEC-0461 and add the preview-layout decision; Q3 consequence-sketch previews."

### T8

(facilitator): "Presented the three distilled decision payloads in plain language for ratification, including the supersession consequences and the T4/T5 session-record additions."

### T9

(stakeholder): "Confirmed: record all three decisions as accepted."

### T10

(facilitator, consistency + cascade dispositions): "Consistency checks after distillation (DEC-0157/DEC-0158): the sweep over DEC-0472..DEC-0474 surfaced DEC-0074's three ratified citers — EP-0006, ST-0043, ST-0044 — via the new relates-to edges. Disposition: this is the known product-vs-method alignment gap already queued as IDEA-0063; no action in this session, and IDEA-0063 should target DEC-0473's post-supersession wording when taken up. The terms check returned zero hits. The DEC-0267 impact walk found no ratified citers of DEC-0460 or DEC-0461, so nothing went stale; EP-0012 (draft) cites both as illustrative precedent only, and IDEA-0062/IDEA-0063 relate to them as accurate historical provenance — all left untouched."

### T11

(facilitator, recall audit outcome): "Decision-recall audit over DEC-0472..DEC-0474: 39 ranked candidates, sharded into five Sonnet 5 judge batches of seven to eight. Zero candidates judged content-relevant. DEC-0337 was judged compliance evidence rather than a gap (the T5 option survey is exactly what it requires), and DEC-0193 shares only grilling vocabulary (question content versus card mechanics). Outcome recorded: nothing to add."

### T12

(facilitator, corroboration note): "Corroboration for T5's first-hand observation: GitHub issue #27348 independently reports preview mode suppressing the inline free-text field. Additionally noted from the same research: previews hard-truncate long content with no scroll, which motivates DEC-0472's two-to-eight-line consequence-sketch sizing."

### T13

(facilitator, single-sourced method edit): "Applied the ratified decisions to the groundwork-design-session skill's references/refinement-process.md grilling section: a new preview-layout bullet (DEC-0472); the three-affordances header now cites DEC-0472..DEC-0474 as superseding DEC-0460/DEC-0461; the keyword hint now reads 'choose Other and type `elaborate`' (DEC-0473); and the free-text guarantee now names the automatic Other option (DEC-0474). Facilitator working memory was updated with the corrected attribution from T4."

### T14

(facilitator): "Presented the closing summary — decisions ratified, sweep and cascade dispositions, audit outcome, corroboration, skill edit — and ran the inspired-ideas check (DEC-0261), noting the in-flight SES-0089 work is excluded from this session's commit."

### T15

(stakeholder): "No new ideas to capture; close SES-0090 and commit."

## Decisions Produced

Three decisions were ratified in this session (T7-T9):

- DEC-0472 establishes that every grilling question card uses the AskUserQuestion preview layout with consequence-sketch previews, phrased single-select wherever feasible, with a disclosed plain-layout fallback for genuinely multi-select questions.
- DEC-0473 supersedes DEC-0460: the elaborate affordance is unchanged, but its keyword fallback for three-and-four-alternative cards now routes through the automatic Other option rather than "the free-text field," since DEC-0472's preview layout is not guaranteed to keep that field present.
- DEC-0474 supersedes DEC-0461: notes-on-selection remains a first-class channel, now understood as a preview-layout feature, and Other replaces the inline free-text field as the guaranteed custom-answer channel, retiring the "never suppressed" guarantee the T5 survey found unsupported in preview mode.

## Conflicts Raised

None.
