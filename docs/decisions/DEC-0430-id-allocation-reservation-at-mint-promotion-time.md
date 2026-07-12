---
id: DEC-0430
type: decision
title: "ID allocation: reservation at mint; promotion-time reconciliation only as a documented offline fallback"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T19, T20, T22, T23, T26, T27, T28, T31"
accepted-in: SES-0082
overview: >-
  IDs are allocated at mint time at the mode's serialization point:
  app monotonic counter, git-native first-push-wins reservation ref,
  or unchanged file-sequential solo allocation. Provisional-ID
  promotion-time reconciliation is documented in SP-0018 strictly as
  an offline/disconnected fallback with its costs named (burned ID
  space, alias/rewrite overhead, immutability collision), not built
  unless disconnected minting becomes a real requirement.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0391, SP-0018, DEC-0416]
---

# DEC-0430: ID allocation — reservation at mint; promotion-time reconciliation only as a documented offline fallback

## Context

This was the one item the stakeholder pulled back out of the otherwise-converged consolidated proposal, proposing a develop-branch merge-time ID-reconciliation alternative by CHANGELOG analogy. The facilitator assessed it as breaking on inbound-reference density against closed-content immutability and ran a stakeholder-directed supplementary consultation putting that assessment back to both system-architect instances for a chance to overturn it. Both concurred unanimously.

## Decision

Artifact IDs are allocated at mint time at the operating mode's serialization point: the single application instance's monotonic counter in app-managed repositories, a first-push-wins reservation ref on the canonical remote in skill-only multi-user repositories, and unchanged file-sequential allocation in solo mode. Provisional IDs reconciled at a develop-to-main promotion are documented in SP-0018 strictly as an offline/disconnected fallback with their costs named — burned ID space, alias indirection or transcript rewriting, and collision with the immutability invariants — and are not built unless disconnected minting becomes a real requirement.

## Rationale

Reservation-at-mint keeps IDs permanent and reference-stable from the moment an artifact is created, which is what the corpus's dense inbound-reference model (relates-to, cites, derives-from, all by bare ID) depends on. Promotion-time reconciliation would require every reference minted against a provisional ID to be rewritten or aliased at promotion — a real, ongoing cost against every session that uses it, not a one-time migration cost — and would collide with the closed-content immutability invariant for any provisional ID that got cited before reconciliation.

## Alternatives Considered

The stakeholder's develop-branch merge-time reconciliation proposal (CHANGELOG analogy) was the live alternative and was rejected as primary, on the inbound-reference-density assessment confirmed unanimously by both independently briefed system architects in the supplementary consultation round. It is retained as a documented, named-cost offline fallback in SP-0018 rather than discarded outright, since disconnected minting is a real (if not currently pressing) scenario.

## Implications

SP-0018 must document the fallback with its costs named, not build it. The primary reservation-at-mint model applies across all three operating modes now, including the not-yet-built skill-only multi-user reservation-ref mechanism, which becomes real scope once that mode is implemented.
