---
id: SP-0004
type: spike
title: Validate BBDC merge checks / Code Insights as the required-check surface
status: gated
owner: eng-lead
created: 2026-07-08
timebox: 3d
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  relates-to: [ST-0020, ST-0013, ST-0014]
cites: [DEC-0036, DEC-0050, DEC-0141, DEC-0142, DEC-0145, DEC-0150]
---

# SP-0004: BBDC Required-Check Surface Validation

> Drafted during [EP-0005](../epics/EP-0005-connectors-and-identity.md)
> story derivation ([SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md))
> and ratified with that gate bundle (per
> [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md)).

## Question

Do Bitbucket Data Center merge checks / Code Insights suffice as the
required-check surface the gate design assumes — specifically: can the
gate engine register checks that (a) block merge per-PR until they
pass, (b) accept re-reported results when recomputation runs
([DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md))
— **including flipping an already-green check back to failing on an
open PR so it re-blocks merge**, which mid-flight policy recomputation
requires ([DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md))
— and (c) post results as the service/program user with the necessary
permissions — for all five registered checks (`gate-policy`,
`conflicts-open`, the tier-2 suite, the mechanical-diff validator, the
System-Decision template-conformance check, per
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md))?

## Why It Blocks

[ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md) cannot
gate until the answer is known
(per [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md)):
the entire enforcement model routes fine-grained gating through
service-side required checks precisely because BBDC lacks native
path-scoped reviewer requirements
([DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md),
[DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)). If the
check surface can't block merges or accept re-reports, the gate design
needs rework before the connector contract hardens.

## Method

Against a real Bitbucket Data Center instance (matching the target
deployment's major version): register a synthetic required check via
the merge-check and Code Insights APIs; verify per-PR merge blocking,
result re-reporting after state changes — pass→fail un-passing
included (per [DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md))
— program-user permission
requirements, and behavior on force-push/branch update; document API
gaps and workarounds. Findings become decisions.

## Findings

Pending — recorded at spike completion.

## Resulting Decisions

Pending — a completed spike produces at least one decision, even
"assumption confirmed, no change."
