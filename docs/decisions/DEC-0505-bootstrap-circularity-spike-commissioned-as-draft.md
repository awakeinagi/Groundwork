---
id: DEC-0505
type: decision
title: "Bootstrap-circularity spike commissioned as draft-ahead work"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T4–T5, T8–T9, T10–T11"
overview: >-
  EP-0014's transition principle settles which rules govern a method
  change, but the mechanism — transition-window protocol, re-
  validation policy, meta-tier placement, genesis documentation,
  test plan — is research-shaped, per DEC-0337 and DEC-0345. This
  decision commissions a spike, drafted in this session as draft-
  ahead work under EP-0014's gate bundle and ratified by the epic's
  approval, to formalize that mechanism. The spike runs as the next
  refinement target after EP-0014's approval, before story
  derivation, since its findings shape governance-rule stories'
  acceptance criteria and it consumes nothing from EP-0010's
  component docs.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0337, DEC-0345, DEC-0480, DEC-0481, DEC-0483, DEC-0019, DEC-0504]
---

# DEC-0505: Bootstrap-circularity spike commissioned as draft-ahead work

## Context

The transition principle settles which rules govern a method change, but the mechanism details are research-shaped: the record holds building blocks (DEC-0480's version pinning, DEC-0481's specification-first posture, DEC-0483's corpus SemVer marker) but no assembled self-amendment protocol. DEC-0337 sizes research to the decision and DEC-0345 requires a test plan with any design.

## Decision

A spike is commissioned, drafted in this session as draft-ahead work under EP-0014's gate bundle and ratified by the epic's approval, to formalize the transition mechanism: the transition-window protocol (what governs between a method change's proposal and its approval); the re-validation policy for already-approved artifacts when rules change; whether the transition rule lives in the session protocol or as a meta rule family on the checker; one-time documentation of the genesis base case (the DEC-0019-era bootstrap); and the test plan for the mechanism.

## Rationale

The stakeholder ratified the record-grounded architect's position: decide the principle now, spike the mechanism. The mechanism warrants investigation before commitment per DEC-0337, and its test plan needs research-grounded specification per DEC-0345. Re-validation policy is included in the spike's scope because it is the same temporal-version question as the transition rule.

## Alternatives Considered

Resolving the full mechanism in-session was rejected because it commits protocol details without the research pass DEC-0337 sizes for foundational choices. Deferring both principle and mechanism to the spike was rejected because the epic would gate with its named risk unresolved.

## Implications

The spike runs as the next refinement target after EP-0014's approval, before story derivation, because its findings shape governance-rule stories' acceptance criteria and it consumes nothing from EP-0010's component docs. It is listed in EP-0014's Derived Work with its draft-ahead status noted explicitly.
