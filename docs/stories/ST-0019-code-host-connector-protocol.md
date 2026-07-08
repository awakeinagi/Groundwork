---
id: ST-0019
type: story
title: Code-host connector protocol and capability manifest
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  impacts: [ST-0020, ST-0021, ST-0023, ST-0024, ST-0025, ST-0031]
cites: [DEC-0028, DEC-0032, DEC-0036, DEC-0043, DEC-0045, DEC-0049, DEC-0079,
        DEC-0132, DEC-0142, DEC-0145, DEC-0150]
---

# ST-0019: Code-Host Connector Protocol and Capability Manifest

## Summary

The host-agnostic seam every host interaction crosses: the code-host
connector protocol's operation families, its capability manifest schema
with the documented minimum capability set, the normalized webhook
event schema, and the conformance suite that qualifies any adapter —
satisfying the consumption lists the artifact store and gate engine
have already forward-declared.

## Acceptance Criteria

1. The protocol defines every operation family the boundary needs:
   fork provisioning; branch create/delete and push; PR open, merge,
   and review-state; review posting on both the delegated-OAuth and
   program-user paths; check-run result posting; required-check
   registration; branch-protection administration; team
   administration; read-only browse/search; permission probe; and
   webhook/event subscription
   (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md),
   [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md),
   [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
   [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md),
   [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).
2. [CMP-0001](../components/CMP-0001-artifact-store-service.md)'s
   forward-declared consumption list — fork provisioning, branch
   create/delete, PR open/merge/review-state, check-run result
   posting, permission probe — is satisfied operation-for-operation,
   or a conflict is raised
   (per [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)).
3. The gate engine's operations — required-check registration,
   branch-protection write and reconcile, team administration — are
   defined as [CMP-0004](../components/CMP-0004-governance-gate-engine.md)
   consumes them, keeping registration distinct from result posting
   (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md),
   [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
4. Each connector declares a capability manifest against a published
   schema; a documented minimum capability set states what a host must
   support to run Groundwork at all, and every operation above the
   minimum is marked so the gate engine's compiler can adapt or emulate
   (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
5. Host webhooks surface through the protocol as a normalized event
   schema (PR state, review, push, check events) that downstream
   consumers subscribe to without host-specific parsing
   (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md),
   [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
6. A protocol conformance suite qualifies any adapter; the local-git
   fake connector passes it in full — manifest included — and remains
   the hermetic CI double for every consumer
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).

## Component Impact

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md) —
supplies the protocol's operation contracts, manifest schema, event
schema, and conformance expectations.

## Out of Scope

Adapter implementations — the GitHub connector, v1
([ST-0031](ST-0031-github-connector.md), per
[DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)) and the
Bitbucket Data Center connector, deferred
([ST-0020](ST-0020-bitbucket-data-center-connector.md)); allowlist
*enforcement* and citation format for reads
([ST-0023](ST-0023-read-only-context-access.md)); token handling and
attribution signing
([ST-0021](ST-0021-delegated-reviews-and-attribution.md)); connectors
for additional hosts
([ST-0028](ST-0028-additional-code-host-connectors.md), deferred);
writing to codebases — permanently out for the whole system
(per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).

## Notes for Implementers

The fake connector predates this story
([ST-0003](ST-0003-item-branch-pr-orchestration.md) ships it); this
story owns the protocol spec and conformance suite the fake must
track — expect to adjust the fake, never the contract, when they
disagree.

Do not harden the check-administration operation family (registration,
result posting) before
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)'s findings
land — if BBDC cannot express the assumed semantics, the protocol
shape, not just the adapter, may need rework
(per [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md)).
