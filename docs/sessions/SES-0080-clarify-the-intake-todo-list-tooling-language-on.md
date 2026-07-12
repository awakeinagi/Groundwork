---
id: SES-0080
type: session
title: "Clarify the intake todo-list tooling language on the DEC-0256 instruction surfaces"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
kind: expedited
intake: {origin: user, proposed-by: awakeinagi}
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Expedited take-up session (DEC-0254) clarifying the intake todo-
  list tooling language on the surfaces that carry DEC-0256's
  requirement. Triggered when a 2026-07-12 change intake found the
  facilitator, working in a harness exposing the Task tools
  (TaskCreate/TaskUpdate) rather than TodoWrite, falling back to an
  in-message checklist because the groundwork-design-session skill's
  refinement-process reference, its AGENTS.md asset, and the project
  AGENTS.md all compress DEC-0256's requirement to "create a minimal
  todo list" -- language that reads as naming one specific tool,
  even though DEC-0256 itself already says the list is kept "using
  the harness's task/todo tracker." Stakeholder awakeinagi confirmed
  the proposed fix and its wording verbatim. The session produced
  DEC-0410 (accepted), then closed after the facilitator applied the
  confirmed wording directly to all three instruction surfaces
  (outside docs/, beyond the DEC-0312 write-API boundary) and ran a
  decision-recall audit on DEC-0410: one finding disposed by
  grounding its Implications claim with a relates-to link to
  DEC-0312, the remaining fourteen candidates adjacent-no-action.
  DEC-0256 itself remains unchanged.
links:
  relates-to: [DEC-0256, DEC-0410]
---

# SES-0080: Clarify the intake todo-list tooling language on the DEC-0256 instruction surfaces

## Purpose

DEC-0254 authorizes expedited method-level take-up sessions for process gaps discovered mid-work. This session clarifies the tooling language that carries DEC-0256's intake todo-list requirement, after a 2026-07-12 change intake where the facilitator, working in a harness that exposes the Task tools (TaskCreate/TaskUpdate) rather than TodoWrite, fell back to an in-message checklist because none of the instruction surfaces named the Task tools as a valid tracker.

## Transcript

T1 (stakeholder awakeinagi, verbatim; context — the facilitator had kept the intake todo list as in-message text after not finding a TodoWrite tool, and the stakeholder pointed at the Task tools): "You don't have TodoWrite but you do have Task tools", followed in the next turn by: "It seems like the skill instructions were confusing for the todo list. In this session, let's improve that language so it's clear you can use Task tools."

T2 (facilitator restatement and root cause): DEC-0256 itself is already tool-agnostic — its Decision says the list is kept "using the harness's task/todo tracker." The confusion is downstream: three instruction surfaces (the groundwork-design-session skill's references/refinement-process.md intake step 1, the skill's assets/AGENTS.md intake step 1, and the project AGENTS.md intake step 1) compressed this to "create a minimal todo list", which reads as assuming one specific tool. Proposed fix: clarify on all three surfaces that the list is kept in whichever task/todo tool the harness session exposes (e.g. TodoWrite, or the Task tools TaskCreate/TaskUpdate), with a visible in-conversation checklist as fallback when no tracker tool exists. Presentation-only clarification; DEC-0256 is unchanged, not superseded.

T3 (stakeholder awakeinagi, verbatim): "Confirmed."

T4 (facilitator): Applied the confirmed language to all three instruction surfaces — the groundwork-design-session skill's references/refinement-process.md intake step 1, its assets/AGENTS.md intake step 1, and the project AGENTS.md intake step 1 — each now naming the capability level (whichever task/todo tool the harness exposes, e.g. TodoWrite or the Task tools TaskCreate/TaskUpdate, with a visible in-conversation checklist only when none exists) and citing DEC-0256 and DEC-0410. Direct facilitator edits are sanctioned for these files because they live outside docs/, beyond the DEC-0312 write-API boundary.

T5 (facilitator): Decision-recall audit on DEC-0410: 15 candidates, judged by a Sonnet 5 judge; one finding — the Implications' write-API-boundary claim rests on DEC-0312, uncited. Disposition: DEC-0312 linked/cited from DEC-0410 in-session. Remaining 14 candidates adjacent-no-action. Consistency sweep earlier returned one citer (ST-0033), reviewed non-actionable; terms clean.

T6 (facilitator, closing summary): Expedited session complete: DEC-0410 accepted, three surfaces edited in sync, audit dispositioned. Classification confirmed: method-level presentation clarification, no artifact-tree impact beyond DEC-0410/DEC-0256 links.

## Decisions Produced

DEC-0410 (accepted) clarifies the intake todo-list tooling language on the three DEC-0256 instruction surfaces.

## Conflicts Raised

None.
