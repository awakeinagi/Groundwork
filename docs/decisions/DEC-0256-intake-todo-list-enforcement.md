---
id: DEC-0256
type: decision
title: The agent materializes the intake workflow as a todo list at first mention of a change
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  The moment change intent is mentioned, the agent creates a minimal todo
  list—restate intention; confirm alignment; start session?—using the
  harness's task/todo tracker. On path confirmation the list expands to
  match the confirmed path (full grilling, expedited per DEC-0254, etc.).
  Agent works the list; steps marked done as complete. Guarantees the
  restate/align steps are tracked and no step silently drops under load.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T3, T10-T11"
links:
  relates-to: [DEC-0410]
  derives-from: [SES-0050]
---

# DEC-0256: Todo-list enforcement of the intake workflow

## Context

Workflow steps that live only in prose get skipped under load. The
stakeholder asked for the intake steps to be tracked explicitly, and
amended the timing from "at session open" to "at first mention."

## Decision

The moment change intent is mentioned, the agent creates a minimal
todo list — *restate intention; confirm alignment; start session?* —
using the harness's task/todo tracker. On path confirmation the list
expands from a standard template matching the confirmed path: the full
grilling flow (grilling topics appended as identified, integrity steps
as fixed items) or the expedited flow. The agent works the list; steps
are marked done as they complete, so no step silently drops.

## Rationale

The same discipline that makes rule-type decisions effective as
checklists (citing a rule is not applying it) applies to the intake
protocol itself. Creating the list before alignment costs nothing when
a discussion ends off-record — three pending items get deleted — and
guarantees the restate/align steps are themselves tracked.

## Alternatives Considered

- **Create at session open only**: misses tracking of the alignment
  loop, the steps most often skipped.
- **Fixed static checklist**: loses the per-session grilling agenda
  that makes the list a working document.

## Implications

The skill's intake playbook and AGENTS.md instruct agents to create
and maintain the list. SES-0050 itself was run this way.
