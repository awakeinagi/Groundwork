---
id: DEC-0461
type: decision
title: "Notes-on-selection and free-text are stated grilling affordances, with harness fallbacks"
status: superseded
superseded-by: [DEC-0474]
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0088 @ T4-T8
overview: >-
  The facilitator treats the harness's native notes-on-selection as
  a first-class channel: free-text notes attached to any chosen
  option are design input, never noise. The automatic free-text
  field ("Type something") is never suppressed and is always as
  valid an answer as a listed option. On harnesses lacking native
  per-selection notes (GitHub Copilot CLI's ask_user) or lacking
  structured question cards at all (stock Amp), the elaborate
  keyword and the free-text field substitute for the missing
  affordances. Records the SES-0088 option survey: Claude Code
  AskUserQuestion (1-4 questions per call, 2-4 options, automatic
  free-text, native per-selection notes, no pre-fill), GitHub
  Copilot CLI ask_user (single/multi-select, freeform option, no
  documented notes), and Amp (plugin-provided select only). Decided
  in SES-0088 (T4-T8), confirmed by the stakeholder, mirroring
  DEC-0074's product-side always-present affordances at the method
  level.
links:
  relates-to: [DEC-0074, DEC-0460]
  derives-from: [SES-0088]
---

# DEC-0461: Notes-on-selection and free-text are stated grilling affordances, with harness fallbacks

## Context

The groundwork-design-session skill's refinement-process reference has long carried a passive "three affordances on every question" rule (notes, free-text, elaborate), but nothing made notes-on-selection and the automatic free-text field explicit, stated practice — a stakeholder had to already know the doctrine to rely on them. The tooling survey in SES-0088 also found that not every harness supports these affordances natively, raising the question of what substitutes when they are missing.

## Decision

The facilitator treats the harness's native notes-on-selection as a first-class channel: free-text notes attached to any chosen option are design input — amendments, caveats, and upgrades to the chosen option — never noise. The automatic free-text field ("Type something") is never suppressed, and a free-text answer is always as valid as a listed option. On harnesses without native per-selection notes (GitHub Copilot CLI's ask_user) or without structured question cards at all (stock Amp), the elaborate keyword and the free-text field substitute for the missing affordances. The supporting option survey, recorded in SES-0088: Claude Code AskUserQuestion allows 1-4 questions per call and 2-4 options per question, with automatic free-text and native per-selection notes but no pre-fill mechanism; GitHub Copilot CLI ask_user offers single/multi-select with a freeform option and no documented notes; Amp offers plugin-provided selection only.

## Rationale

Making these affordances stated rather than passive matches the stakeholder's T7 confirmation that every question, no exceptions, carries the full affordance set, and closes the same locate-first gap DEC-0074 already closed on the product side: the doctrine existed but was not visible in practice. Naming harness fallbacks explicitly (elaborate keyword, free-text) keeps the affordance set intact even where a given tool lacks native notes or structured cards, rather than silently degrading when the facilitator runs on a different tool.

## Alternatives Considered

Leaving the affordances passive (unstated, relying on the facilitator's prior knowledge of the doctrine) was rejected as the status quo gap this decision closes. Requiring a uniform question-tooling capability across all harnesses before stating the rule was rejected as impractical — the survey found real capability differences (Claude Code, GitHub Copilot CLI, Amp) that the method needs to accommodate rather than wait out.

## Implications

This mirrors DEC-0074's product-side always-present affordances at the method level, in live harness practice, and relates to DEC-0074 without superseding it since the two decisions govern different surfaces (product UI vs. facilitator method). The groundwork-design-session skill's refinement-process reference needs its grilling section updated to state notes-on-selection and free-text as first-class channels and to name the harness-specific fallbacks.
