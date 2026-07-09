---
id: ST-0039
type: story
title: Change Proposal triage
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0037]
  impacts: [ST-0055]
  impacted-by: [ST-0034, ST-0037]
cites: [DEC-0044, DEC-0047, DEC-0130, DEC-0277, DEC-0278]
---

# ST-0039: Change Proposal Triage

## Summary

The classification step every captured-outside-refinement change runs
through — Jira drift, shared-draft comments, implementation feedback —
sorted into a mechanical fix, a refinement session, or an audited
rejection, always preserving the proposal verbatim.

## Acceptance Criteria

1. A `CP-` artifact captures the proposed change verbatim, its proposer
   (person-id), its source (`jira-drift` | `ui-suggestion` |
   `implementation-feedback` | `unauthorized-attempt`), and links
   `relates-to` its target artifact, created via the typed
   `create-change-proposal` mechanical operation
   (per DEC-0047,
   DEC-0130,
   DEC-0278).
2. The agent triages each CP into exactly one outcome: trivial changes
   become a mechanical-fix PR citing the CP; substantive changes open an
   intake-opened refinement session carrying the CP verbatim as its
   proposal (`origin: cp`); rejected proposals persist with recorded
   triage rationale, recorded via the typed `set-cp-triage` mechanical
   operation
   (per DEC-0047,
   DEC-0130,
   DEC-0277).
3. Jira-drift CPs specifically follow the revert-then-propose flow: the
   projection is restored to canonical content and commented on with an
   explanation before the CP triage runs — the edit is never silently
   discarded
   (per DEC-0044).
4. Shared-draft comments captured as CPs
   (per ST-0037)
   triage through the same pipeline as any other CP source — no
   special-cased shortcut for synthesis-origin proposals.
5. Triage classification (mechanical / session / rejected) and its
   rationale are recorded on the CP itself via `set-cp-triage`, queryable
   independent of whatever downstream PR or session resulted
   (per DEC-0130).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Impact Notes

AC2's intake routing defines the shape ST-0055's triage views render at
revival — its "session" action opens an intake-opened session from the
CP — the ST-0039 → ST-0055 impact edge (per DEC-0277).

## Out of Scope

The Jira connector's drift *detection* mechanics
(EP-0005 family); what
counts as "trivial" vs. "substantive" per artifact type (a strategy-pack
policy question, per
ST-0033); the
mechanical-fix PR construction itself
(EP-0001 executes
typed writes).

## Notes for Implementers

Triage classification thresholds are pack-configurable, not hardcoded —
this story owns the CP lifecycle and routing, not the trivial/substantive
judgment call itself.

CPs with source `unauthorized-attempt` are created by the intake
authority check (ST-0035, per
DEC-0278), not by
triage — they arrive in this pipeline as any other pending CP awaiting
the authority holder(s).
