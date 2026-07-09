---
id: DEC-0193
type: decision
title: Goal-grilling questions are tiered by confidence and consolidated into a dedicated reference file
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0035 @ T15-T18"
links:
  derives-from: [SES-0035]
  relates-to: [DEC-0189, DEC-0190, DEC-0191]
  supersedes: []
---

# DEC-0193: Goal-Grilling Questions Are Tiered by Confidence and Consolidated Into a Dedicated Reference File

## Context

The expanded goal-level question set (Problem, Current State & Gap,
System Context, Illustrative Scenario, sharpened Outcomes/Scope/
Constraints — per
DEC-0189,
DEC-0190,
DEC-0191) is now large
enough that inlining it in the process document would bloat it. Not all
of it carries equal certainty — edge cases and integration specifics are
expected to be revised downstream in a way a goal's foundational framing
is not.

## Decision

Goal-level questions are consolidated into a new skill reference file,
`references/goal-grilling-questions.md`, organized by Business Goal
section, with each question tagged **[High]**, **[Medium]**, or **[Low]**
confidence. Volatility runs High → Low as questions get more concrete:
High-tier answers are treated as settled once confirmed; Low-tier answers
are provisional, expected to be revised at Epic/Story/Spike level. The
tiering is communicated to the approver explicitly at gate time (per
DEC-0192).

## Rationale

Separates the stable "process" document (how to run any session) from the
more frequently-tuned "content" document (what to ask at this specific
stage). The tier tags give the facilitator and approver a shared,
explicit vocabulary for how hard to push for precision at each question.

## Alternatives Considered

- **Keep all questions inline in `refinement-process.md` without
  tiering**: rejected — loses the volatility signal that lets the
  approver distinguish load-bearing answers from best-guesses, and makes
  an already-long process document harder to navigate.

## Implications

`SKILL.md`'s reference map and Mode 2 step point at the new file;
`references/refinement-process.md`'s Goal playbook delegates to it rather
than repeating the question list.
