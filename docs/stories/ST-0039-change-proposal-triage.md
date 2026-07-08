---
id: ST-0039
type: story
title: Change Proposal triage
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0037]
  impacts: []
  impacted-by: [ST-0034, ST-0037]
cites: [DEC-0044, DEC-0047, DEC-0130]
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
   `implementation-feedback`), and links `relates-to` its target
   artifact, created via the typed `create-change-proposal` mechanical
   operation
   (per [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md),
   [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)).
2. The agent triages each CP into exactly one outcome: trivial changes
   become a mechanical-fix PR citing the CP; substantive changes trigger
   a refinement session with the CP as input; rejected proposals persist
   with recorded triage rationale, recorded via the typed
   `set-cp-triage` mechanical operation
   (per [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md),
   [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)).
3. Jira-drift CPs specifically follow the revert-then-propose flow: the
   projection is restored to canonical content and commented on with an
   explanation before the CP triage runs — the edit is never silently
   discarded
   (per [DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md)).
4. Shared-draft comments captured as CPs
   (per [ST-0037](ST-0037-incremental-synthesis-and-shared-draft.md))
   triage through the same pipeline as any other CP source — no
   special-cased shortcut for synthesis-origin proposals.
5. Triage classification (mechanical / session / rejected) and its
   rationale are recorded on the CP itself via `set-cp-triage`, queryable
   independent of whatever downstream PR or session resulted
   (per [DEC-0130](../decisions/DEC-0130-mechanical-ops-shared-allowlist.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The Jira connector's drift *detection* mechanics
([EP-0005](../epics/EP-0005-connectors-and-identity.md) family); what
counts as "trivial" vs. "substantive" per artifact type (a strategy-pack
policy question, per
[ST-0033](ST-0033-strategy-pack-format-and-plugin-loading.md)); the
mechanical-fix PR construction itself
([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) executes
typed writes).

## Notes for Implementers

Triage classification thresholds are pack-configurable, not hardcoded —
this story owns the CP lifecycle and routing, not the trivial/substantive
judgment call itself.
