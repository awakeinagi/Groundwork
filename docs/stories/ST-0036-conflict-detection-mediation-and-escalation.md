---
id: ST-0036
type: story
title: Conflict detection, mediation, and escalation
status: gated
owner: ds-lead
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0034]
  impacts: [ST-0037]
  impacted-by: [ST-0032, ST-0034]
cites: [DEC-0005, DEC-0021, DEC-0039, DEC-0183]
---

# ST-0036: Conflict Detection, Mediation, and Escalation

## Summary

The fixed-order flow the agent runs on contradictory or competing
requests: understand each party's underlying intent first, mediate with
informed compromise proposals, and — only if mediation fails — escalate
to a documented `CFL-` artifact that blocks downstream generation from
the artifacts in tension until resolved.

## Acceptance Criteria

1. On detecting a conflict, the agent first elicits each stakeholder's
   underlying intent (not just their stated position) before proposing
   anything
   (per [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)).
2. Informed by intent, the agent explains the conflict to the
   stakeholder(s) plainly and offers compromises or alternatives
   (mediation) within the same or a follow-up session
   (per [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)).
3. If mediation fails, the agent opens a `CFL-` artifact capturing both
   intents, the mediation record, and escalates to the configured
   Arbiter's work queue, with notifications via configured channels
   (per [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md),
   [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)).
4. While a `CFL-` is open, the artifacts in tension carry a failing
   `conflicts-open` status check so their PRs cannot merge, and nothing
   new derives from them — enforced as a checkable precondition, not
   just documentation
   (per [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md),
   [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)).
5. Conflict detection runs actively at three trigger points: within a
   single session (an answer contradicts an earlier one), during
   synthesis across sessions (cross-participant contradiction, per
   [DEC-0021](../decisions/DEC-0021-one-on-one-sessions.md)), and when a
   new answer contradicts an accepted Decision.
6. `CFL-` artifacts do not default into
   [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)'s
   per-artifact timeout-to-default election — a Conflict resolves only by
   a ratified Decision or explicit withdrawal, never by inaction; aging
   conflicts escalate in visibility (reminders, dashboards), not in state
   (per [DEC-0183](../decisions/DEC-0183-conflicts-no-default-timeout-election.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The `CFL-` artifact's frontmatter schema and gate-blocking mechanics as
enforced by checks ([EP-0003](../epics/EP-0003-governance-and-gate-engine.md)
owns check machinery; this story owns when/how the agent detects and
routes into that mechanism); cross-session conflict detection's
integration with the shared draft
([ST-0037](ST-0037-incremental-synthesis-and-shared-draft.md)).

## Notes for Implementers

Escalation targets the Arbiter role from governance config, not a
hardcoded person — resolve it the same way
[ST-0035](ST-0035-guardrails-and-authority-limits.md)'s Arbiter
notification does.
