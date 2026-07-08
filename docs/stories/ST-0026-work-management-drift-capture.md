---
id: ST-0026
type: story
title: Work-management drift capture and change proposals
status: deferred
release: "2"
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0025]
  impacted-by: [ST-0025]
cites: [DEC-0033, DEC-0044, DEC-0047, DEC-0048, DEC-0148]
---

# ST-0026: Work-Management Drift Capture and Change Proposals

> Deferred to release `2` at creation (per
> [DEC-0148](../decisions/DEC-0148-work-management-stories-release-2.md),
> the deferral citation per
> [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md)).
> No trigger subscription — revival is release-2 planning.

## Summary

Drift, treated as input rather than error: direct edits to
canonical-owned projection fields are detected with before/after
capture, promptly reverted toward canon, preserved verbatim as Change
Proposal artifacts, and answered with a respectful redirection comment.

## Acceptance Criteria

Indicative until revival re-refines this story (deferred stories cannot
pass a gate):

1. A direct edit to a canonical-owned projection field is detected
   with the edit's before/after content captured from the host's
   webhook/event payloads
   (per [DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md)).
2. The projection is promptly restored to canonical content, and the
   editor's diff is captured as a Change Proposal
   (source `jira-drift`, proposer resolved to a person-id) routed to
   the item's refinement flow
   (per [DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md),
   [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)).
3. The CP artifact is filed through the typed write path the connector
   is allowed — never a direct canonical edit
   (per [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md),
   [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
4. The issue receives a comment explaining the revert with links to
   the canonical doc and the captured proposal
   (per [DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md)).
5. Edits to workflow-owned fields are telemetry, never drift — no
   revert, no CP
   (per [DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md)).

## Component Impact

None yet — lands in the work-management connector component stubbed at
revival (see [ST-0025](ST-0025-work-management-projection-lifecycle.md)).

## Out of Scope

CP *triage* — the session agent's job
([EP-0002](../epics/EP-0002-refinement-session-agent.md), per
[DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md));
UI-suggestion and implementation-feedback CP sources
([EP-0006](../epics/EP-0006-refinement-web-ui.md) and the Handoff
boundary respectively).
