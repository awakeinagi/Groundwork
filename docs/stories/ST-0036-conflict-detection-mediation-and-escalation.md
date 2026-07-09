---
id: ST-0036
type: story
title: Conflict detection, mediation, and escalation
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
overview: >-
  Fixed-order flow on contradictory or competing requests: elicit each
  stakeholder's underlying intent first, mediate with informed compromise
  proposals, escalate to CFL artifact if mediation fails. Detection runs at
  three points: within-session contradiction, cross-session contradiction,
  contradiction with accepted Decision. CFL blocks derivative work via
  conflicts-open check; resolves only by ratified Decision or explicit
  withdrawal.
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
   (per DEC-0005).
2. Informed by intent, the agent explains the conflict to the
   stakeholder(s) plainly and offers compromises or alternatives
   (mediation) within the same or a follow-up session
   (per DEC-0005).
3. If mediation fails, the agent opens a `CFL-` artifact capturing both
   intents, the mediation record, and escalates to the configured
   Arbiter's work queue, with notifications via configured channels
   (per DEC-0005,
   DEC-0039).
4. While a `CFL-` is open, the artifacts in tension carry a failing
   `conflicts-open` status check so their PRs cannot merge, and nothing
   new derives from them — enforced as a checkable precondition, not
   just documentation
   (per DEC-0005,
   DEC-0039).
5. Conflict detection runs actively at three trigger points: within a
   single session (an answer contradicts an earlier one), during
   synthesis across sessions (cross-participant contradiction, per
   DEC-0021), and when a
   new answer contradicts an accepted Decision.
6. `CFL-` artifacts do not default into
   DEC-0039's
   per-artifact timeout-to-default election — a Conflict resolves only by
   a ratified Decision or explicit withdrawal, never by inaction; aging
   conflicts escalate in visibility (reminders, dashboards), not in state
   (per DEC-0183).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The `CFL-` artifact's frontmatter schema and gate-blocking mechanics as
enforced by checks (EP-0003
owns check machinery; this story owns when/how the agent detects and
routes into that mechanism); cross-session conflict detection's
integration with the shared draft
(ST-0037).

## Notes for Implementers

Escalation targets the Arbiter role from governance config, not a
hardcoded person — resolve it the same way
ST-0035's Arbiter
notification does.
