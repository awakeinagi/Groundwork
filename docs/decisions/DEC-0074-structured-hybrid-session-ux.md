---
id: DEC-0074
type: decision
title: Sessions use a structured-hybrid UX with notes, free-text, and elaboration on every question
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0010 @ T2-T3"
links:
  derives-from: [SES-0010]
---

# DEC-0074: Structured-hybrid session UX

## Context

The session experience could be pure chat or structured. This bootstrap
itself was conducted with structured question cards (options,
recommended-first, free-text override) — a validated pattern.

## Decision

The session is a conversation stream mixing free chat with typed
interaction cards: **question cards** and **decision-playback cards**
(DEC-0051), plus a
persistent progress panel (settled / open / parked). Every question card
guarantees three affordances: (1) users can attach **notes/clarifications
to any predetermined choice**; (2) a **free-text response** option is
always present; (3) an **"elaborate" option** is always present — choosing
it has the agent expand the question with examples of the different
options and more detailed comparisons and contrasts before the user
answers.

## Rationale

Structured cards make recommendations visible and answers precise; the
three guaranteed affordances keep structure from ever boxing a participant
in — annotated choices captured verbatim are exactly what distillation
needs, and elaboration-on-demand serves participants who need more context
without burdening those who don't.

## Alternatives Considered

- **Pure chat**: option comparison and confirmation ergonomics degrade;
  busy stakeholders skim.
- **Form-first wizard**: kills the adaptive conversational dynamic.

## Implications

The session-engine contract (EP-0002) needs typed turn payloads —
question-card, decision-playback, elaboration-request/response — realizing
the EP-0006→EP-0002 impact edge; recorded as a story-level contract
elaboration within EP-0002's approved scope (in live operation this would
queue an EP-0002 re-affirmation). Choice annotations land in the raw
transcript (DEC-0052)
and are citable by distillation. Elaboration behavior is strategy-pack
content (DEC-0053).
