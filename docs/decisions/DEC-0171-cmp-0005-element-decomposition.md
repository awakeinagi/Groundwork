---
id: DEC-0171
type: decision
title: CMP-0005 decomposes into CodeHostConnector, CapabilityManifest, and HostEvent; no graduation at this time
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T1-T2"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0080, DEC-0129, DEC-0162]
---

# DEC-0171: [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md) Element Decomposition

## Context

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
needed a Design Elements decomposition covering its two approved
stories ([ST-0019](../stories/ST-0019-code-host-connector-protocol.md),
[ST-0023](../stories/ST-0023-read-only-context-access.md)) before its
contract could be drafted, plus — per
[DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)'s
seam-graduation rule — a graduation review of any candidate element.

## Decision

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
decomposes into three elements: `CodeHostConnector` (protocol) —
mirroring [CMP-0003](../components/CMP-0003-app-database-port.md)'s
one-big-protocol-with-lettered-operation-families pattern
([DEC-0129](../decisions/DEC-0129-port-typed-operation-families.md)) —
carrying every operation family (fork/branch/PR orchestration, review
posting, check administration, branch-protection and team
administration, allowlisted reads, permission probe, webhook
subscription); `CapabilityManifest` (value) — the manifest schema
([DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
[DEC-0168](../decisions/DEC-0168-connector-minimum-capability-set.md));
and `HostEvent` (event) — the normalized webhook-event schema
([DEC-0169](../decisions/DEC-0169-connector-push-webhook-delivery.md)).
None graduates to a standalone component now.

## Rationale

A single protocol element keeps the whole capability seam reviewable
as one unit, matching precedent
([CMP-0003](../components/CMP-0003-app-database-port.md)); splitting by
concern (orchestration vs. reviews vs. admin vs. reads) would multiply
elements without a corresponding consumer boundary — every consumer
([CMP-0001](../components/CMP-0001-artifact-store-service.md),
[CMP-0004](../components/CMP-0004-governance-gate-engine.md)) already
consumes named *operations*, not named *sub-protocols*. On graduation:
none of the three elements is consumed by more than one component
outside this seam's own consumers, and none needs independently
versioned conformance apart from the whole protocol's — the graduation
bar [CMP-0002](../components/CMP-0002-change-event.md)/[CMP-0003](../components/CMP-0003-app-database-port.md)
cleared (an actual second consumer) isn't met here; `CapabilityManifest`
and `HostEvent` are consumed externally only through
`CodeHostConnector`'s own API, ordinary component-boundary consumption.

## Alternatives Considered

- **Split into multiple protocol elements by concern** (orchestration,
  reviews, administration, reads) — tighter per-element `Implements`
  lists against [ST-0019](../stories/ST-0019-code-host-connector-protocol.md)
  vs. [ST-0023](../stories/ST-0023-read-only-context-access.md), but
  more elements to cross-reference for no consumer-visible benefit,
  since [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)'s
  granularity test is about seams, not story boundaries alone.

## Implications

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)'s
`## Design Elements` section carries all three element blocks, each
with its own `Implements:` line. A future consumer needing independent
versioning of, say, `CapabilityManifest` alone would revisit this call
then — this decision does not foreclose it.
