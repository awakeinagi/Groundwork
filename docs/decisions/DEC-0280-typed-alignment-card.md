---
id: DEC-0280
type: decision
title: A typed alignment card carries the restate-and-align loop in the session payload contract
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0280 constrains the session payload contract to gain a fourth card
  type, the alignment card: the agent's restatement of the intake intent
  with confirm/amend actions, where amendment loops back to a fresh
  restatement turn mirroring decision-playback correction. A confirmed
  alignment card is the typed turn DEC-0273's alignment-before-grilling
  invariant keys on, making alignment confirmation machine-legible and
  recorded.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T8-T9"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0051, DEC-0074]
---

# DEC-0280: The typed alignment card

## Context

ST-0044's typed turn payloads are question-card, decision-playback,
and elaboration-request/response (DEC-0074). The restate-and-align
loop needs alignment confirmation to be machine-legible: the path pick
hangs on it, the transcript must show intent being corrected, and
DEC-0273's alignment-before-grilling invariant needs something
concrete to key on.

## Decision

The session payload contract gains a fourth card type, the **alignment
card**: the agent's restatement of the intake intent rendered with
confirm / amend actions. An amendment loops back to a fresh
restatement turn — mirroring how a decision-playback correction
reopens the topic rather than editing the record. A confirmed
alignment card is the typed turn the engine's intake invariant keys
on.

## Rationale

Free chat would make "alignment confirmed" an LLM inference over
prose, not a recorded act — weaker than what the paradigm gives a
skill-mode agent today. Reusing the decision-playback card would
conflate confirming a distilled decision (post-grilling) with aligning
on intent (pre-grilling), forcing downstream distillation and the eval
harness to disambiguate by position.

## Alternatives Considered

- **Free chat suffices**: nothing for the invariant to enforce
  against.
- **Reuse decision-playback**: same mechanics, conflated semantics.

## Implications

ST-0044 gains the card's acceptance criterion; the EP-0006→EP-0002
typed-payload contract grows by one card type; ST-0032's
alignment-before-grilling invariant (DEC-0273) references the typed
turn.
