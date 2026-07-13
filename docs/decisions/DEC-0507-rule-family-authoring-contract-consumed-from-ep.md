---
id: DEC-0507
type: decision
title: "Rule-family authoring contract consumed from EP-0010; governance-rule stories sequence after it"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T4–T5, T10–T11"
overview: >-
  A rule family — the unit EP-0014 defines policy for — has no
  defined deliverable shape yet; that shape, registration mechanism,
  and policy-configuration schema are deferred to EP-0010's
  component docs per DEC-0486. This decision names the rule-family
  authoring contract as consumed from EP-0010's rule-hosting
  component doc and sequences EP-0014's governance-rule stories
  after that component doc reaches draft completeness, so stories
  are not refined against a guessed contract and reworked later.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0469, DEC-0484, DEC-0486, DEC-0512]
---

# DEC-0507: Rule-family authoring contract consumed from EP-0010; governance-rule stories sequence after it

## Context

EP-0014 defines which governance rules exist and their policy; EP-0010's machinery hosts and runs them per DEC-0469 and DEC-0484. But a rule family has no defined deliverable shape yet — its shape, registration mechanism, and policy-configuration schema are deferred to EP-0010's component docs per DEC-0486 — so governance-rule stories written now would guess at those details.

## Decision

EP-0014's Interfaces section names the rule-family authoring contract — the shape, registration mechanism, and policy-configuration schema of a rule family — as a contract consumed from EP-0010's rule-hosting component doc, and EP-0014's governance-rule stories sequence after that component doc reaches at least draft completeness.

## Rationale

Consumer-driven contract discipline has the consumer name its expectations early while machinery contracts remain EP-0010's domain; co-drafting the contract inside EP-0014 would cross the DEC-0469 boundary and invite a staleness cascade on the just-approved EP-0010. Sequencing prevents acceptance-criteria rework, and the epic is never idle because dogfooding-lane and spike work start immediately.

## Alternatives Considered

Naming the dependency without sequencing was rejected because a rule story refined before the contract exists guesses at registration and configuration details and gets reworked. Co-drafting the authoring contract in this epic was rejected as crossing the DEC-0469 line.

## Implications

Story derivation orders governance-rule stories behind EP-0010's rule-hosting component doc.
