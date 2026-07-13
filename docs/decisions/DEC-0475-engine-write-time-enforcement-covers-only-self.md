---
id: DEC-0475
type: decision
title: "Engine write-time enforcement covers only self-trust invariants; all other rules run as check-time rule families"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T4-T5"
overview: >-
  The Engine's contract needed a principled boundary between what it
  mechanically enforces at write time and what runs as check-time
  rule reporting. This decision draws that line at self-trust: the
  Engine enforces only invariants whose violation would corrupt its
  own operations (ID uniqueness, schema validity, link integrity,
  gate-state legality, graph consistency); everything else,
  governance rules included, runs as a checker rule family, with
  content-quality rules warning rather than blocking. Both advisor
  instances converged on this independently, avoiding both release-
  coupling every rule to the Engine and letting the Engine persist
  self-corrupting corpora.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0469, DEC-0471, DEC-0423, DEC-0484]
---

# DEC-0475: Engine write-time enforcement covers only self-trust invariants; all other rules run as check-time rule families

## Context

EP-0010 carried the open question of which paradigm rules the Engine mechanically enforces and which remain convention in the skill layer.

## Decision

The Engine enforces at write time only the invariants whose violation would leave the corpus in a state the Engine's own operations cannot trust: ID uniqueness, schema validity, link referential integrity, gate-state transition legality, and graph consistency. Every other paradigm rule, governance rules included, runs as a checker rule family that reports violations at check time, and content-quality rules warn rather than block. The boundary test: if a violation would make graph sync, semantic search, or gate logic produce wrong results, enforce it at write time; otherwise report it at check time.

## Rationale

Both advisor instances converged on this principle independently. Enforcing too much at write time couples every rule family's evolution to Engine releases, against DEC-0471's evolving-model posture; enforcing too little lets the Engine persist corpora that corrupt its own operations. DEC-0469's split between rule policy (EP-0014) and hosting machinery (EP-0010) already implies rule families are pluggable definitions rather than kernel invariants.

## Alternatives Considered

Enforcing all rules at write time was rejected as rigid and release-coupled. Check-time-only enforcement was rejected because the Engine could then persist corpora that corrupt its own operations.

## Implications

The write API's guardrails and the checker's rule families become two contract surfaces with a principled boundary, and EP-0014 authors rule families against the check-time surface.
