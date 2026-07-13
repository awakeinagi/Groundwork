---
id: DEC-0504
type: decision
title: "Method transition principle: pre-change rules govern rule changes"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T4–T5, T10–T11"
overview: >-
  EP-0014's draft carried one open risk, the bootstrap-circularity
  transition rule: what governs a change to the method's own
  governance rules. This decision states the transition principle
  converged on by both system-architect instances in the SES-0094
  consultation: a change to the method or its governance rules is
  gated by the rules accepted before the change, and new rules take
  effect only after approval under the pre-change rules — the
  standard resolution used in self-hosting and self-amending systems
  (an old compiler builds the new one; constitutional amendments
  ratify under the existing procedure). This closes DEC-0442's no-
  ungoverned-capability gap for the method itself and extends
  DEC-0481's specification-first posture. The mechanism behind the
  principle is formalized by the sibling spike-commissioning
  decision; EP-0014's Risks section is updated accordingly.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0442, DEC-0019, DEC-0481, DEC-0505]
---

# DEC-0504: Method transition principle: pre-change rules govern rule changes

## Context

EP-0014's draft carried one named open risk, the bootstrap-circularity transition rule: when a change to the method or its governance rules alters how the method documents or gates itself, something must define which rules govern that change. Both system-architect instances in the SES-0094 advisor consultation converged on the same core answer.

## Decision

A change to the method or its governance rules is gated by the rules that were accepted before the change; the new rules take effect only after the change has been approved under the pre-change rules.

## Rationale

This is the standard resolution in self-hosting and self-amending systems — an old compiler builds the new one, and constitutional amendments are ratified under the existing constitution's procedures. It prevents a change from approving itself under rules it introduces, closing the gap in DEC-0442's no-ungoverned-capability obligation for the method itself, and it extends DEC-0481's specification-first posture: the accepted specification of the method governs until a new one is accepted under it.

## Alternatives Considered

Letting new rules govern their own introduction was rejected because a change could approve itself. Deferring even the principle to the spike was rejected because the first method change to arrive would find no governing rule at all. Resolving the full mechanism in-session was rejected on procedure — the mechanism's details are research-shaped (see the spike decision).

## Implications

The principle is recorded now at epic level; the transition mechanism (transition-window protocol, re-validation policy, genesis documentation, meta-tier placement, test plan) is formalized by the spike commissioned in the sibling decision. EP-0014's Risks section replaces the open risk with references to this decision and the spike.
