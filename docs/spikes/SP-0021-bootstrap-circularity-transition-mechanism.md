---
id: SP-0021
type: spike
title: "Bootstrap-circularity transition mechanism"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  This spike formalizes the mechanism behind DEC-0504's transition
  principle — a change to the method or its governance rules is
  gated by the rules accepted before the change, new rules taking
  effect only after approval under the old ones. It answers five
  research questions: what governs the transition window between a
  method change's proposal and its approval; the re-validation
  policy for already-approved artifacts when rules change; whether
  the transition rule lives in the session protocol or a meta rule
  family on the Engine-hosted checker; how the DEC-0019-era genesis
  bootstrap is documented once as the degenerate base case; and the
  DEC-0345 test plan demonstrating the mechanism functions. Drafted
  during EP-0014's refinement session (SES-0094) as draft-ahead work
  per DEC-0505 and ratified by the epic's own approval, it runs as
  the next refinement target after EP-0014's approval, before story
  derivation, since its findings shape governance-rule stories'
  acceptance criteria and it consumes nothing from EP-0010's
  component docs.
links:
  derives-from: [EP-0014]
  relates-to: [DEC-0504, DEC-0505, DEC-0337, DEC-0345, DEC-0480, DEC-0481, DEC-0483, DEC-0019]
cites: [DEC-0504, DEC-0505, DEC-0337, DEC-0345, DEC-0480, DEC-0481, DEC-0483, DEC-0019, DEC-0484, DEC-0252]
---

# SP-0021: Bootstrap-circularity transition mechanism

## Question

What is the mechanism behind the transition principle (DEC-0504) — a change to the method or its governance rules is gated by the rules accepted before the change, and new rules take effect only after approval under the old ones? Specifically: (1) what governs during the transition window between a method change's proposal and its approval under the pre-change rules, and how that window reconciles with DEC-0252's hard rule that semantic changes to a Groundwork corpus happen only inside recorded sessions? (2) when rules change, what happens to already-approved artifacts — grandfathered, re-validated at next gate, or re-validated corpus-wide? (3) does the transition rule live in the session protocol or as a meta rule family on the Engine-hosted checker — a placement question reasoned against DEC-0484's definition of a rule family as Engine-owned rule code with declarative committed configuration, substrate-neutral, and itself constrained by DEC-0252's session-only rule? (4) how is the genesis base case — the DEC-0019-era bootstrap that predates any governing ruleset — documented once as the degenerate base case? (5) what is the test plan (DEC-0345) demonstrating the mechanism functions?

If question 3 resolves toward a meta rule family on the Engine-hosted checker, the transition mechanism would land in EP-0010-hosted machinery and this spike's no-EP-0010-dependency sequencing claim (DEC-0505) would need revisiting in its findings.

## Why It Blocks

EP-0014's governance-rule stories need the transition mechanism settled before their acceptance criteria can name how a rule change is proposed, gated, and rolled out without the method approving its own amendment under rules it just introduced. Without this spike, any story touching governance-rule authoring or amendment would guess at the transition-window protocol and the re-validation policy, and would likely be reworked once the mechanism is formalized.

## Method

Literature grounding in self-hosting and self-amending systems (compiler bootstrapping, constitutional amendment procedures) per DEC-0337's research-sizing; a design pass over the two building blocks already in the record (DEC-0480's version pinning, DEC-0481's specification-first posture, DEC-0483's corpus SemVer marker) to assemble a candidate protocol; a decision on session-protocol versus meta-rule-family placement,; one-time genesis documentation of the DEC-0019-era bootstrap as the degenerate base case; and a DEC-0345-conformant test plan for the assembled mechanism, drafted for stakeholder review.

## Findings

Not yet run. This spike was drafted during EP-0014's refinement session (SES-0094) as draft-ahead work and is ratified by the epic's approval; it runs as the next refinement target after EP-0014's approval, before story derivation, since its findings shape governance-rule stories' acceptance criteria and it consumes nothing from EP-0010's component docs (DEC-0505).

## Resulting Decisions

Done when: findings are recorded as decisions. None recorded yet.
