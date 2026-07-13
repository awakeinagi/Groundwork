---
id: SES-0093
type: session
title: "Grilling-card affordances re-grounded in measured AskUserQuestion behavior (expedited)"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-13
kind: expedited
intake: {origin: user, proposed-by: awakeinagi}
participant: awakeinagi
participant-role: stakeholder/operator
facilitator: Claude
transcript-fidelity: reconstructed
overview: >-
  Expedited method-level session that re-grounded the SES-0090
  grilling-affordance decision set in measured AskUserQuestion
  behavior, after in-conversation experiments (2026-07-13). Five
  decisions were produced and accepted (DEC-0499 through DEC-0503):
  a combined "Something else/Please elaborate" preview option,
  layout-dependent free-text channels (notes on preview cards, Other
  on plain cards), a minimum-two-questions rule for preview cards,
  measured preview budget/styling, and a plain-layout rule for
  multi-select questions. DEC-0473 and DEC-0474 were superseded,
  which had rested on the false premise that Other is always
  available on preview cards; DEC-0472's preview-layout mandate
  stands. IDEA-0067 was taken up. The groundwork-design-session
  playbook (references/refinement-process.md) was rewritten to
  match. A Sonnet 5 decision-recall audit ran at close-out: its
  finding that the session narrows DEC-0074's blanket affordance
  guarantee was dispositioned by linking DEC-0074 with a Purpose
  clarification that the product-side guarantee stands unnarrowed. A
  separately reported audit-tooling gap (no provenance edges for the
  considered set in the judge packet) was parked as a new idea. The
  session is closed.
links:
  relates-to: [DEC-0472, DEC-0473, DEC-0474, SES-0088, SES-0090, DEC-0499, DEC-0500, DEC-0501, DEC-0502, DEC-0503, IDEA-0067, DEC-0074]
---

# SES-0093: Grilling-card affordances re-grounded in measured AskUserQuestion behavior (expedited)

## Purpose

This expedited session re-grounds the grilling-card affordance guarantees in empirically measured AskUserQuestion behavior, from experiments the stakeholder and facilitator ran in-conversation on 2026-07-13. The SES-0090 decision set is amended: DEC-0473 and DEC-0474 route their free-text fallbacks through the automatic Other option on the stated premise that Other is always available, but the experiments show preview-layout cards — the very layout DEC-0472 mandates — suppress the Other option entirely. DEC-0472 itself stands. The session supersedes DEC-0473 and DEC-0474 with corrected channels, adds a card-composition rule the experiments surfaced (selection and note are mutually exclusive on single-question cards), and updates the groundwork-design-session skill's preview-budget guidance to measured values. SES-0088 and SES-0090 are the prior affordance sessions this work continues.

IDEA-0067, captured in SES-0092, parked this same change; this session is its take-up.

DEC-0074's product-side guarantee of notes, free-text, and elaboration on every question is not narrowed by this session: the harness limitation that motivated DEC-0501 is specific to Claude Code's AskUserQuestion preview cards, and the product UI remains bound to deliver the full affordance set on every question, including single-question cards.

## Transcript

### T1 (stakeholder)

"There are still some issues with the presentation of grilling questions. I don't want to start a session now, just run some experiments with you. Can you pose some questions to test the capabilities of the AskUserQuestion API vs what I've asked for in the grilling rounds?" Over the conversation the stakeholder directed a battery of experiments — payload round-trips for notes and selections, preview capacity probes, options-column width probes, and a markdown stress test — then asked: "Look at my previous requests (recent) for how to format the questions/responses in the grilling session. What's reasonable?"

### T2 (facilitator)

The facilitator presented the measured capability map: (a) preview-layout cards suppress both option descriptions and the automatic Other option; (b) per-selection notes round-trip intact and note-only submissions are valid answers; (c) on a single-question card, confirming a note submits immediately with no option selected, so a selection with an attached note requires a card of at least two questions; (d) preview panes render a viewport-height window of about 33 post-wrap rows (about 20 is safe across window sizes) and hard-cut the remainder with no scroll affordance; (e) the option-label column is fixed at about 30 characters and cannot be widened; (f) markdown in previews renders headers as bold, styles bold/strikethrough/inline code, syntax-highlights fenced code blocks, draws blockquote bars, and styles links, while tables, task checkboxes, and horizontal rules degrade to raw source. On this evidence the facilitator assessed that DEC-0473 and DEC-0474 rest on a false premise — Other is not always available — and proposed an amendment session to supersede both, add a minimum-two-questions rule for preview cards, and update the skill playbook's budget guidance.

### T3 (stakeholder)

The stakeholder confirmed: "Yes", and subsequently instructed "This can be expedited."

### T4 (facilitator)

The facilitator played back a four-decision amendment set (elaborate keyword and free-text guarantee re-pointed at the notes channel, a minimum-two-questions rule for preview cards, and a measured preview budget) and relayed the locate-first results: the staleness cascade is minimal — no living approved artifact bakes in the false premise except DEC-0473 and DEC-0474 themselves — and IDEA-0067, captured in SES-0092, already parked this same change, making this session its take-up.

### T5 (stakeholder)

The stakeholder instructed "This can be expedited", then asked whether a free-text response works on preview cards; the facilitator confirmed the notes channel round-trips and note-only submissions are valid. The stakeholder then proposed an always-present listed "Something else" option carrying a note, and upgraded it in a second amendment to a single combined option: "Or even better, two birds with one stone: 'Something else/Please elaborate'", with the option's preview reading verbatim: "Use notes to type your own response or request the agent to provide additional information. A blank notes section implies that you would like the agent to elaborate on the question with examples (where possible)."

### T6 (stakeholder)

The stakeholder asked: "Should we also include an explicit decision about using non-preview type for multi-select responses?" The facilitator agreed it must be its own decision — superseding DEC-0473 would otherwise orphan the elaborate guarantee on plain multi-select cards — and proposed the multi-select affordance story (descriptions carry per-option prose, Other is the free-text and elaborate-keyword channel).

### T7 (facilitator)

At the stakeholder's request ("Let's confirm one more time that multi-select doesn't work for preview type"), the facilitator sent a live probe card with multiSelect enabled and both descriptions and previews on every option. Screenshot-verified result: the card silently dropped to plain layout — previews discarded without error, descriptions rendered, checkboxes worked including on the inline "Type something" option, and no notes affordance appeared. The multi-select decision gained an explicit rule that previews are never attached to multi-select questions.

### T8 (stakeholder)

The stakeholder confirmed the full five-decision set: "Confirmed. Thanks for the help debugging this!"

### T9 (facilitator)

Close-out, recording executed outcomes. The five decisions were recorded as accepted (DEC-0499 through DEC-0503), DEC-0473 and DEC-0474 flipped to superseded via the supersession machinery with their body text untouched, and IDEA-0067 transitioned to taken-up. The groundwork-design-session playbook (references/refinement-process.md) was rewritten in three places — the small-rounds bullet, the preview-layout bullet, and the affordances bullet — citing DEC-0499 through DEC-0503; the retired Other-based keyword routing and the two-to-eight-line preview guidance were removed. Consistency sweep findings were dispositioned: EP-0006, ST-0043, and ST-0044 cite DEC-0074 and were reviewed with no action required — they implement the product-side UX guarantee and nowhere assert the false premise about the Other option; an optional follow-up pass may confirm their affordance descriptions against the corrected channel story. The decision-recall audit ran with a Sonnet 5 judge; its single finding — that the session narrows DEC-0074's blanket guarantee — was dispositioned by linking DEC-0074 with a Purpose clarification that the product-side guarantee stands unnarrowed, the harness limitation being specific to the method-level card mirror that DEC-0501 works around. The judge's separately reported contract gap in the audit packet (no provenance edges for the considered set) was parked as IDEA-0069, per the focus-artifact test.

## Decisions Produced

DEC-0499 — Preview grilling cards carry a combined "Something else/Please elaborate" option
DEC-0500 — Free-text channels are layout-dependent: notes on preview cards, Other on plain cards
DEC-0501 — Preview grilling cards always carry at least two questions
DEC-0502 — Preview budget and styling follow measured harness behavior
DEC-0503 — Multi-select questions use plain layout; previews are never attached to them

## Conflicts Raised

None.
