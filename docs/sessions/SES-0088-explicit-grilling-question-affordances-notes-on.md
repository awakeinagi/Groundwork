---
id: SES-0088
type: session
title: "Explicit grilling-question affordances — notes-on-selection and a selectable elaborate option"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: verbatim
kind: expedited
intake: {origin: user, proposed-by: awakeinagi}
overview: >-
  Expedited method-level change-intake session, closed: the
  stakeholder asked that every text-based alternative in a grilling
  question card carry an explicit notes affordance, and that
  questions with selectable decisions include an explicit selectable
  option reading "Please elaborate on what needs to be decided here,
  include examples where helpful," while keeping the free-text "Type
  Something" field. The facilitator located DEC-0074 (product-side
  precedent) and surveyed Claude Code, GitHub Copilot CLI, and Amp
  question tooling against official docs, finding no pre-fill
  mechanism for the free-text field. The stakeholder chose a
  conditional slot-budget approach, later tightened to a listed-
  option threshold of at most two substantive alternatives, a
  keyword ("elaborate") fallback for three-to-four-alternative
  questions, and an implicit-elaborate catch for "I don't
  understand"-style answers. The session produced two accepted
  decisions, DEC-0460 and DEC-0461, both relating to DEC-0074, and
  rewrote the groundwork-design-session skill's refinement-process
  reference accordingly. A recall audit on both decisions found and
  fixed one missing sibling relates-to link. At close, the inspired-
  ideas check surfaced two candidates, both selected by the
  stakeholder and captured as IDEA-0062 (authoring-time sibling
  cross-link check) and IDEA-0063 (aligning the product-side
  elaborate affordance with DEC-0460).
links:

  relates-to: [DEC-0460, DEC-0461, IDEA-0062, IDEA-0063]
---

# SES-0088: Explicit grilling-question affordances — notes-on-selection and a selectable elaborate option

## Purpose

To refine a stakeholder-proposed change to the grilling text options presented by the facilitator during design sessions: give every text-based alternative in a structured question card an explicit affordance to attach notes, and give questions with selectable decisions an explicit selectable option asking the agent to elaborate on what needs to be decided, while keeping the free-text field.

## Transcript

### T1

(stakeholder, verbatim proposal): "I would like to make some changes to the grilling text options presented by the agent during Sessions. Each text-based alternative given by the facilitator should include the option to add notes. On questions with selectable decisions, please add an option for telling the agent \"Please elaborate on what needs to be decided here, include examples where helpful.\" Keep the \"Type Something\" free-text field."

### T2

(facilitator, restatement): Restated the intention as three parts: (1) every text-based alternative presented in a structured question card should carry the affordance to attach free-text notes to the selection; (2) on questions with selectable decisions, the option list itself should include an explicit selectable choice reading "Please elaborate on what needs to be decided here, include examples where helpful"; (3) the free-text "Type Something" field stays on every question. Noted that the method doctrine already carries a passive "Three affordances on every question" rule (notes / free-text / elaborate) in the groundwork-design-session skill's refinement-process reference since the skill's first commit — this change makes those affordances explicit and visible in the card rather than something the stakeholder must know to invoke. Flagged a design consideration: question cards hold at most 4 options, so a standing elaborate option spends one slot, leaving 2-3 substantive alternatives. Recommended the expedited path.

### T3

(stakeholder, alignment): Confirmed alignment: "Yes, I think we're aligned here. The 'question cards hold at most 4 options' constraint may be a problem. Let's research the Claude Code and Github Copilot docs to understand the exact capabilities of the question tooling for each." Chose the expedited session path.

### T4

(facilitator): Presented research findings. Locate-first: DEC-0074 (accepted, SES-0010) already establishes notes-on-any-choice, always-present free-text, and an always-present selectable elaborate option — but for the Refinement Web UI product (ST-0044 AC#2, ST-0043, EP-0006); no prior IDEAs or sessions cover facilitator-side practice, so this change harmonizes harness practice with the product promise and relates to DEC-0074 rather than superseding it. Tooling survey (DEC-0337-sized, official docs): Claude Code AskUserQuestion — 1-4 questions per call, 2-4 options per question, automatic "Type something" free-text, native per-selection notes (empirically confirmed in this session), no built-in elaborate affordance (it must spend an option slot). GitHub Copilot CLI ask_user — single/multi-select with a freeform option and markdown questions, no documented per-selection notes, no documented option cap. Amp — no built-in question tool; plugin-provided select only (example plugin: single-select, 2-5 options). Asked three design questions: slot budget under the 4-option cap, wording of the elaborate option, and which questions get it.

### T5

(stakeholder, verbatim answers to the three design questions): Slot budget: "Conditional (Option 2). In the case where we have to fallback to the user using free-text, could we set the default (tab autocomplete?) for the free-text field to the \"Please elaborate\" text? Is that possible?" Wording: "Verbatim as label (Recommended)". Scope: "Every question, no exceptions".

### T6

(facilitator): Researched the pre-fill question against official docs (Agent SDK user-input, interactive-mode, keybindings, changelog): pre-filling, defaulting, or tab-autocompleting text into the free-text field is not supported — docs are silent on any such mechanism. Proposed the keyword-convention fallback: when the elaborate option is dropped, the question text ends with a hint that typing `elaborate` in the free-text field triggers the same behavior. Presented two decision drafts (standing elaborate option with conditional escape; notes and free-text as stated affordances with harness fallbacks) plus the exact method-text change to the grilling section of the groundwork-design-session skill's refinement-process reference.

### T7

(stakeholder, verbatim): "Confirmed. But when 3 alternatives need to be presented only include the free-text option (change from <= 3). If a user say anything similar to \"I don't understand\", \"Please explain\", etc., assume the \"Please elaborate on what needs to be decided here, include examples where helpful\" directive unless the user has explicit instructions for the help that they need."

### T8

(facilitator): Incorporated both amendments into the decisions: the listed elaborate option appears only on cards with at most two substantive alternatives (three or four substantive alternatives -> keyword fallback), and any stakeholder answer resembling "I don't understand" or "please explain" is treated as the elaborate directive unless they state specifically what help they need.

### T9

(facilitator): Ran the decision-recall audit on DEC-0460 and DEC-0461 (15 candidates each; two independent Sonnet 5 judges). One confirmed finding, now fixed in-session: the sibling decisions lacked a mutual relates-to link — both cited only DEC-0074 despite forming one coherent doctrine born in the same session; the mutual links were added. All other candidates were judged topical noise; closest near-miss was DEC-0410 (tool-capability-level language precedent), judged compatible rather than in tension since DEC-0461 deliberately catalogs multiple harnesses with fallbacks. Both judges independently reported the same contract gap, parked as an inspired-idea candidate rather than extending this session: same-session sibling decisions sharing a citation target escape the DEC-0157 relates-to sweep (the sweep walks citers of already-named relations, so it has no edge between un-cross-linked siblings) — an authoring-time same-session sibling cross-link check would close the gap.

### T10 (facilitator)

Presented the closing summary: expedited method-level classification confirmed; DEC-0460 and DEC-0461 recorded accepted and mutually linked, relating to DEC-0074; the grilling section of the groundwork-design-session skill's refinement-process reference rewritten accordingly and in force immediately; sweep/terms clean; recall audit produced one finding (missing sibling link), fixed in-session; full checker passing. Ran the inspired-ideas check, offering two candidates: the same-session sibling cross-link check (from both audit judges) and product-side copy alignment with ST-0044/DEC-0074.

### T11 (stakeholder)

Selected both inspired-idea candidates for capture: "Sibling cross-link check" and "Product copy alignment". No further ideas offered.

### T12 (facilitator)

Captured both as IDEA artifacts (IDEA-0062, IDEA-0063), cross-referenced from this session; session closed.

## Decisions Produced

DEC-0460 (grilling question cards carry an explicit elaborate option, with a keyword fallback) and DEC-0461 (notes-on-selection and free-text are stated grilling affordances, with harness fallbacks), both accepted in this session and relating to DEC-0074.

## Conflicts Raised

None.
