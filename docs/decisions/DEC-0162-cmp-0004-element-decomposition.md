---
id: DEC-0162
type: decision
title: CMP-0004 decomposes into ten nested Design Elements; no graduation at this time
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0029 @ T1-T4"
links:
  derives-from: [SES-0029]
  relates-to: [DEC-0080, DEC-0134, DEC-0135, DEC-0136, DEC-0163, DEC-0164,
               DEC-0165]
---

# DEC-0162: Governance & Gate Engine Element Decomposition

## Context

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) (Governance
& Gate Engine) needed a Design Elements decomposition covering its
seven approved stories
([ST-0012](../stories/ST-0012-governance-config-schemas.md)–[ST-0018](../stories/ST-0018-governance-event-log-metrics.md))
before its contract could be drafted, and — per
[DEC-0080](DEC-0080-hybrid-component-granularity.md)'s seam-graduation
rule and [DEC-0136](DEC-0136-graduation-review-required.md)'s mandatory
pre-gate graduation review — a decision on whether any element should
split into a standalone component rather than nest.

## Decision

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) decomposes
into ten Design Elements, one per story concern: `GovernanceConfig`
(value) and `GovernanceInit`(service) for
[ST-0012](../stories/ST-0012-governance-config-schemas.md);
`PolicyCompiler`(service) for
[ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md);
`GatePolicyCheck`(service) for
[ST-0014](../stories/ST-0014-gate-policy-check.md); `ConflictGate`
(service) for
[ST-0015](../stories/ST-0015-conflicts-open-check-and-operations.md);
`StalenessSweepService`(service) and `ImpactReport`(value) for
[ST-0016](../stories/ST-0016-staleness-sweep-impact-analysis.md);
`ReaffirmationService`(service) for
[ST-0017](../stories/ST-0017-reaffirmation-flow-queues.md);
`GovernanceEvent`(event) and `GovernanceEventLog`(service) for
[ST-0018](../stories/ST-0018-governance-event-log-metrics.md). All ten
stay nested inside
[CMP-0004](../components/CMP-0004-governance-gate-engine.md); none
graduates to a standalone component now.

## Rationale

Mirrors [CMP-0001](../components/CMP-0001-artifact-store-service.md)'s
one-service-per-capability granularity, keeping each story's contract
independently reviewable. On graduation: the only plausible seam is
`GovernanceConfig`, since
[ST-0012](../stories/ST-0012-governance-config-schemas.md)'s
implementer notes flag
[EP-0002](../epics/EP-0002-refinement-session-agent.md)'s future
session guardrails as a second consumer of the decision-rights portion
— but the governance file schemas are already owned and published by
[CMP-0001](../components/CMP-0001-artifact-store-service.md)
(`SchemaValidator.D-2`), so a future session-agent component can read
`governance/roles.yaml` directly via `StorageService.A-1` against that
published schema without depending on
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) at all.
`GovernanceEvent` and `ImpactReport` are consumed externally only
through `GovernanceEventLog`'s API — ordinary component-boundary
consumption, not a shared seam. This matches the precedent set when
[CMP-0002](../components/CMP-0002-change-event.md)/[CMP-0003](../components/CMP-0003-app-database-port.md)
graduated out of
[CMP-0001](../components/CMP-0001-artifact-store-service.md)
([DEC-0134](DEC-0134-graduate-change-event.md),
[DEC-0135](DEC-0135-graduate-app-database-port.md)): graduation follows
an actual second consumer, not a forecast one.

## Alternatives Considered

- **Coarser decomposition** (one `GovernanceEngine` service covering
  compile+check+sweep+reaffirm, plus the three data elements) — rejected
  as less parallelizable for implementers and a worse match to the
  story boundaries already approved.
- **Graduate `GovernanceConfig` now, forward-declared** (mirroring
  [DEC-0132](DEC-0132-connector-consumption-forward-declared.md)'s
  pattern for the code-host connector) — rejected: that decision
  forward-declares consumption of a contract that must exist regardless
  (every host interaction crosses it); here the config-reading
  capability already exists on
  [CMP-0001](../components/CMP-0001-artifact-store-service.md) and
  needs no new seam to be reached.

## Implications

[CMP-0004](../components/CMP-0004-governance-gate-engine.md)'s
`## Design Elements` section carries all ten element blocks. If
[EP-0002](../epics/EP-0002-refinement-session-agent.md)'s refinement
later makes governance decision-rights an actual, contract-level
[CMP-0004](../components/CMP-0004-governance-gate-engine.md)
dependency (rather than a raw file read), that graduation call is
revisited then — this decision does not foreclose it.
