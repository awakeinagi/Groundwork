---
id: ST-0020
type: story
title: Bitbucket Data Center connector
status: gated
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019, SP-0004]
  impacted-by: [ST-0019]
cites: [DEC-0045, DEC-0050, DEC-0079, DEC-0150]
---

# ST-0020: Bitbucket Data Center Connector

## Summary

The v1 reference implementation of the code-host connector protocol:
Bitbucket Data Center, with an honest capability manifest, merge
checks / Code Insights as the required-check surface, reviewer groups
approximating team routing, and Data Center webhooks feeding the
normalized event schema.

## Acceptance Criteria

1. The connector implements the full protocol from
   [ST-0019](ST-0019-code-host-connector-protocol.md) and passes its
   conformance suite (per [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md),
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
2. Its capability manifest declares BBDC's real surface — including the
   absence of native path-scoped reviewer requirements — so the gate
   engine's compiler routes that enforcement through the `gate-policy`
   check rather than assuming host support
   (per [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md),
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
3. Required-check registration and result posting are implemented on
   the surface [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)
   validates (merge checks / Code Insights), honoring the spike's
   findings (per [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md),
   [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)).
4. Team administration maps role projections onto BBDC reviewer groups
   and default reviewers (per [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)).
5. Data Center webhook event families are translated into the
   protocol's normalized event schema with no host-specific payloads
   leaking to consumers (per [DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md),
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
6. Consumer test suites that pass against the local-git fake pass
   against this connector unchanged — the swap-in is the pluggability
   validation (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md),
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Component Impact

[CMP-0006](../components/CMP-0006-bitbucket-data-center-connector.md) —
the whole component.

## Out of Scope

Other hosts ([ST-0028](ST-0028-additional-code-host-connectors.md),
deferred); the protocol itself
([ST-0019](ST-0019-code-host-connector-protocol.md)); Jira Data Center
— a work-management concern
([ST-0025](ST-0025-work-management-projection-lifecycle.md), deferred).
