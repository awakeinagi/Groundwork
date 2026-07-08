---
id: ST-0013
type: story
title: Policy compilation and host provisioning
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0012]
  impacts: [ST-0014]
  impacted-by: [ST-0012]
cites: [DEC-0033, DEC-0036, DEC-0037, DEC-0045, DEC-0046, DEC-0079,
        DEC-0140, DEC-0142, DEC-0143, DEC-0172]
---

# ST-0013: Policy Compilation and Host Provisioning

## Summary

The compiler from governance-as-code to host reality: branch
protection, reviewer-group teams, and the required-check catalog —
recompiled on every governance change, with the gate engine as the sole
writer of what blocks merge.

## Acceptance Criteria

1. Coarse rules compile to host branch protection: artifact-type
   directories map to reviewer groups with minimum approval counts for
   committee gates (per [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
2. Host teams are projections of `governance/roles.yaml`, created and
   synced via the connector's team-administration operations — never
   edited host-side as truth; team membership references stable
   person-ids from `governance/people.yaml`, with host-username
   resolution staying connector-side
   (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
   [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md),
   [DEC-0046](../decisions/DEC-0046-person-registry.md)).
3. The gate engine registers every required check — `gate-policy`,
   `conflicts-open`, the tier-2 suite, the mechanical-diff validator,
   and the System-Decision template-conformance check — and is the
   single writer and reconciler of branch-protection settings
   (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md),
   [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md),
   [DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md)).
4. Merging any change under `governance/` triggers recompilation, and
   drift between compiled settings and governance files reconciles
   toward the files (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
   [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
5. The first compilation after the seeded init commit locks gating in
   behind the founding configuration, leaving no empty-governance
   special case in any evaluator
   (per [DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)).
6. All host interactions go through the code-host connector contract
   and respect its capability manifest; v1 target is GitHub (cloud)
   (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
   [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)).
7. The full compilation and provisioning suite passes hermetically
   against the local-git fake connector
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).

## Component Impact

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — supplies
its compilation and host-provisioning contract sections.

## Out of Scope

The connector implementation and its team/required-check administration
operations themselves ([EP-0005](../epics/EP-0005-connectors-and-identity.md),
consumption binding per
[DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md));
evaluating the compiled policy at gate time
([ST-0014](ST-0014-gate-policy-check.md)); posting tier-2 and
mechanical-diff results, which stays with
[CMP-0001](../components/CMP-0001-artifact-store-service.md)
(per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
