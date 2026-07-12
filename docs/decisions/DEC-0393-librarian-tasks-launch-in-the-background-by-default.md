---
id: DEC-0393
type: decision
title: "Librarian tasks launch in the background by default; the facilitator blocks only where the next turn depends on the result"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0076 @ T4-T5, T22-T23"
overview: >-
  Read, search, graph, and — once the DEC-0391 concurrent-apply
  build ships — write tasks launch in the background by default; the
  facilitator continues the session and folds results in on arrival,
  blocking only when the immediate next step consumes the output. No
  barrier machinery is needed: every task reports actually applied
  outcomes, so the existing truthful-turns rule (assert only landed
  outcomes) suffices. Decided at SES-0076; resolves IDEA-0030.
links:
  derives-from: [SES-0076]
  relates-to: [DEC-0391, DEC-0394]
---
# DEC-0393: Librarian tasks launch in the background by default; the facilitator blocks only where the next turn depends on the result

## Context

SES-0076 asked how librarian tasks should be dispatched relative to the flow of the conversation (skeleton restored at SES-0077).

## Decision

Read, search, graph, and — once the concurrent-apply build ships — write tasks launch in the background by default. The facilitator continues the session and folds results in on arrival, blocking only when the immediate next step consumes the output.

## Rationale

No barrier machinery is needed: every task reports actually applied outcomes, so the existing truthful-turns rule — assert only landed outcomes — suffices.

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

This resolves IDEA-0030.
