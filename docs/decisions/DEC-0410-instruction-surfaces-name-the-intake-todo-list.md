---
id: DEC-0410
type: decision
title: "Instruction surfaces name the intake todo-list requirement at the tool-capability level, not a specific tool"
status: accepted
accepted-in: SES-0080
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0080 @ T1-T3
overview: >-
  Clarifies the tooling language on the three surfaces that carry
  DEC-0256's intake todo-list requirement -- the groundwork-design-
  session skill's refinement-process reference, its AGENTS.md asset,
  and the project AGENTS.md -- after a 2026-07-12 change intake
  showed the compressed phrase "create a minimal todo list" reading
  as naming one specific tool (TodoWrite) in a harness that instead
  exposes the Task tools (TaskCreate/TaskUpdate). DEC-0256's own
  Decision already ties the requirement to "the harness's task/todo
  tracker" at the capability level; only the downstream instruction
  phrasing lagged. This decision states that the three surfaces
  should name the requirement at the tool-capability level
  explicitly -- whichever task/todo tool the harness session
  exposes, falling back to a visible in-conversation checklist only
  when none exists -- without superseding or otherwise altering
  DEC-0256 itself. Stakeholder awakeinagi confirmed the proposed
  wording verbatim in SES-0080.
links:
  derives-from: [SES-0080]
  relates-to: [DEC-0256, DEC-0312]
---

# DEC-0410: Instruction surfaces name the intake todo-list requirement at the tool-capability level, not a specific tool

## Context

During a 2026-07-12 change intake the facilitator, working in a harness that exposes the Task tools (TaskCreate/TaskUpdate) rather than TodoWrite, fell back to an in-message checklist because the instruction surfaces compress DEC-0256's requirement to "create a minimal todo list", which reads as naming a specific tool. DEC-0256's own Decision already says the list is kept using the harness's task/todo tracker.

## Decision

The instruction surfaces that carry DEC-0256's intake todo-list step -- the groundwork-design-session skill's refinement-process reference, the AGENTS.md asset that skill installs, and this project's AGENTS.md -- state explicitly that the list is kept in whichever task/todo tool the harness session exposes (for example TodoWrite, or the Task tools TaskCreate/TaskUpdate), falling back to a visible in-conversation checklist only when the session exposes no tracker tool. This is a presentation clarification of DEC-0256, not a change to it.

## Rationale

Instruction text that names or implies a single concrete tool dangles in harnesses that expose a different tracker; naming the requirement at the capability level keeps the intake list enforceable everywhere.

## Alternatives Considered

Superseding DEC-0256 to enumerate concrete tools was rejected -- the decision is already capability-level; only its downstream phrasing lagged. Leaving the language as-is and relying on agent inference was rejected after it demonstrably failed in this session.

## Implications

The facilitator edits the three instruction surfaces directly (they live outside docs/, beyond the write API); the skill asset and the installed project AGENTS.md stay in sync per the skill's own sync rule.
