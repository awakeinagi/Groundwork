---
id: DEC-0512
type: decision
title: "Two-lane story separation for EP-0014's derived work"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T6–T7, T10–T11"
overview: >-
  DEC-0463's implications state EP-0014's stories separate
  governance-rule work from dogfooding-loop work, and a sibling
  sequencing decision gives the governance lane a prerequisite the
  dogfooding lane lacks. This decision makes the two-lane split
  explicit in EP-0014's body: lane A, governance-rule stories,
  sequenced after EP-0010's rule-hosting component doc reaches
  draft; lane B, dogfooding-loop stories, unblocked at derivation;
  plus the bootstrap-circularity spike as a third draft-ahead item.
  Neither lane blocks the other.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0463, DEC-0507]
---

# DEC-0512: Two-lane story separation for EP-0014's derived work

## Context

DEC-0463's implications state that this epic's stories separate governance-rule work from dogfooding-loop work, and the sequencing decision recorded alongside this one gives the governance lane a prerequisite the dogfooding lane lacks.

## Decision

EP-0014's body makes the two-lane split explicit: lane A, governance-rule stories, sequenced after EP-0010's rule-hosting component doc reaches draft; lane B, dogfooding-loop stories, unblocked and free to start at derivation; plus the bootstrap-circularity spike as a third, draft-ahead item. Neither lane blocks the other.

## Rationale

This operationalizes DEC-0463's implication so story derivation does not have to rediscover it, and it gives the sequencing rule a durable place to live.

## Alternatives Considered

Leaving the split to story derivation was rejected because the implication would stay unoperationalized. Explicitly allowing mixed stories was rejected as contradicting DEC-0463's implications for no gain.

## Implications

Story derivation produces two independent lanes plus the spike.
