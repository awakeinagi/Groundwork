---
id: DEC-0460
type: decision
title: "Grilling question cards carry an explicit elaborate option, with a keyword fallback"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0088 @ T4-T8
overview: >-
  Every grilling question card the facilitator presents includes an
  explicit elaboration affordance, no exceptions by question kind.
  Cards with at most two substantive alternatives get a selectable
  option labeled verbatim "Please elaborate on what needs to be
  decided here, include examples where helpful," which expands the
  question with context, rationale, examples, and a compare/contrast
  before re-presenting it. Cards needing three or four substantive
  alternatives drop the listed option and instead end the question
  text with a hint that typing elaborate in the free-text field
  triggers the same behavior, since pre-filling or tab-
  autocompleting the free-text field is unsupported by the harness
  (researched against official Agent SDK docs). Any stakeholder
  answer resembling "I don't understand" or "please explain" is
  treated as the elaboration directive unless the stakeholder states
  specifically what help they need. Decided in SES-0088 (T4-T8),
  confirmed by the stakeholder, mirroring DEC-0074's product-side
  always-present elaborate affordance at the method level.
links:
  relates-to: [DEC-0074, DEC-0461]
  derives-from: [SES-0088]
---

# DEC-0460: Grilling question cards carry an explicit elaborate option, with a keyword fallback

## Context

DEC-0074 (accepted, SES-0010) establishes notes-on-any-choice, always-present free-text, and an always-present selectable elaborate option for the Refinement Web UI product (ST-0044 AC#2, ST-0043, EP-0006). No prior IDEA or session covered the equivalent affordance for facilitator-side harness practice during a grilling session, and question cards are constrained to at most four options, which raised the question of how a standing elaborate option coexists with that cap.

## Decision

Every structured grilling question card the facilitator presents in a session includes an explicit elaboration affordance, with no exceptions by question kind (confirmations included). When a card carries at most two substantive alternatives, it includes a selectable option labeled verbatim "Please elaborate on what needs to be decided here, include examples where helpful"; choosing it has the facilitator expand the question — what is being decided, why it matters now, concrete examples, and a detailed compare/contrast of the alternatives — and then re-present the card. When a question needs three or four substantive alternatives, the listed option is dropped and the question text instead ends with a hint that typing `elaborate` in the free-text field triggers the same behavior; the option survey found that pre-filling or tab-autocompleting the free-text field is unsupported in the harness, making the keyword convention the sanctioned fallback. Any stakeholder answer resembling "I don't understand" or "please explain" is treated as this elaboration directive unless the stakeholder states specifically what help they need.

## Rationale

The stakeholder asked (SES-0088 T5) that the elaborate option be conditional on slot budget, with verbatim wording, applied to every question. Research (SES-0088 T6) into the Agent SDK's user-input, interactive-mode, keybindings, and changelog documentation found no supported mechanism for pre-filling or defaulting the free-text field, so the keyword convention is the only harness-compatible way to preserve the affordance when the option list is full. The stakeholder's SES-0088 T7 amendment tightened the listed-option threshold from "at most three" to "at most two" substantive alternatives, and added the "I don't understand"-style catch that treats an unclear stakeholder answer as an implicit elaborate request.

## Alternatives Considered

Always reserving a slot for the elaborate option regardless of alternative count was rejected because it would force a strict two-alternative maximum, discarding legitimate three- and four-alternative questions. Attempting to pre-fill or tab-autocomplete the free-text field with the elaborate text was investigated and found unsupported by the harness's documented capabilities. Requiring the stakeholder to already know the elaborate phrasing to invoke it (the pre-existing passive rule) was rejected as the very gap this decision closes — it makes the affordance explicit rather than something only a stakeholder aware of the doctrine could use.

## Implications

This mirrors DEC-0074's product-side always-present elaborate affordance at the method level, in live harness practice, and relates to DEC-0074 without superseding it since the two decisions govern different surfaces (product UI vs. facilitator method). The groundwork-design-session skill's refinement-process reference needs its grilling section updated to state the two-alternative listed-option threshold, the keyword fallback for three-to-four-alternative questions, and the "I don't understand"-style elaborate-directive catch.
