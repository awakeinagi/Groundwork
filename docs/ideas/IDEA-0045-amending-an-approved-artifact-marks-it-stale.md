---
id: IDEA-0045
type: idea
title: "Amending an approved artifact marks it stale: approval must re-cover amended content"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  edit-section/delete-section --amend currently leave an approved
  artifact approved, with its original approved-on stamp covering
  content the approver never saw. Proposal to grill: --amend writes
  on an approved artifact automatically transition it to stale
  (forcing the DEC-0267 re-affirmation walk), or at minimum refuse
  without an explicit acknowledgment flag recording why the approval
  should survive the edit. Trade-off to weigh: auto-stale on every
  sanctioned trivial edit may be too aggressive -- a recorded-reason
  escape hatch could balance. Spark context: SP-0016's material
  amendment sat approved until a manual stale-then-reapprove during
  the SES-0073 close-out; the facilitator's first instinct (an
  approved-to-gated transition) was illegal, evidence the lifecycle
  lacks this mechanism. Disposition: pending.
links:
  relates-to: [IDEA-0044]
  derives-from: [SES-0075]
---

# IDEA-0045: Amending an approved artifact marks it stale: approval must re-cover amended content

## The Idea

edit-section/delete-section --amend currently leave an approved artifact approved, with its original approved-on stamp covering content the approver never saw. Proposal to grill: --amend writes on an approved artifact automatically transition it to stale (forcing the DEC-0267 re-affirmation walk), or at minimum refuse without an explicit acknowledgment flag that records why the approval should survive the edit. Trade-off to weigh: auto-stale on every sanctioned trivial edit may be too aggressive -- a recorded-reason escape hatch could balance.

## Spark Context

SP-0016's material amendment sat approved until a manual stale-then-reapprove during the SES-0073 close-out; the facilitator's first instinct (approved-to-gated) was an illegal transition, evidence the lifecycle lacks this mechanism.

## Disposition

Pending.
