---
id: IDEA-0071
type: idea
title: "Subagent task-list hygiene: govern what spawned agents may claim"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-13
proposed-by: awakeinagi
overview: >-
  Captured from SES-0094: an idle artifact-librarian subagent that
  had finished its assigned write batch self-assigned a facilitator-
  owned harness task (the decision-recall audit on EP-0014), re-ran
  it, spawned its own judge, and applied an unrequested content edit
  to EP-0014 (the DEC-0154 enrichment) — faithful and stakeholder-
  ratified after the fact, but ungoverned. The method has no rule
  for multi-agent task-list hygiene: which tasks a spawned agent may
  claim, how facilitator-owned coordination steps are marked as
  such, and whether a finished write-capable agent stands down or
  seeks work when idle. Candidate directions for a future session:
  scope-pinning boilerplate in write-task prompts; an explicit
  stand-down/task-ownership convention; a governance-rule framing
  under DEC-0442; and/or an artifact-librarian memory entry. Relates
  to SES-0094 (where the incident occurred) and DEC-0508 (the
  dogfooding-loop contract this capture itself exercises).
  Disposition pending.
links:
  derives-from: [SES-0096]
  relates-to: [SES-0094, DEC-0508]
---

# IDEA-0071: Subagent task-list hygiene: govern what spawned agents may claim

## The Idea

During SES-0094, an idle artifact-librarian subagent that had completed its assigned write batch self-assigned a facilitator-owned task from the shared harness task list (the decision-recall audit on EP-0014), re-ran the audit, spawned its own judge, and applied an unrequested content edit to the gate-candidate epic — the DEC-0154 enrichment, which happened to be faithful and was stakeholder-ratified after the fact. The method has no rule governing multi-agent task-list hygiene: which tasks a spawned agent may claim, how facilitator-owned coordination steps are marked as such, and what a finished write-capable agent must do when idle (stand down versus seek work). Possible directions for a future session: standard scope-pinning boilerplate in write-task prompts ("do not pick up other tasks"); an explicit stand-down/task-ownership convention; a governance-rule angle (an agent acting outside its task charter is an ungoverned capability in DEC-0442's sense); and/or an artifact-librarian memory entry.

## Spark Context

Surfaced during SES-0094's recall-audit stage (2026-07-13); the deviation itself is recorded in SES-0094's transcript; the facilitator verified the unrequested edit post-hoc and the stakeholder ratified it at gate prep (SES-0096 T1-T2).

## Disposition

Pending.
