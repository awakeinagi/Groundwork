---
id: EP-0005
type: epic
title: Connectors & Identity
status: stale
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001, EP-0003]
  impacts: [EP-0001, EP-0002, EP-0006]
  impacted-by: [EP-0001, EP-0003]
cites: [DEC-0002, DEC-0013, DEC-0016, DEC-0024, DEC-0026, DEC-0028, DEC-0032,
        DEC-0036, DEC-0043, DEC-0044, DEC-0045, DEC-0046, DEC-0047, DEC-0048,
        DEC-0049, DEC-0050, DEC-0075, DEC-0132, DEC-0142, DEC-0148, DEC-0149,
        DEC-0150, DEC-0151, DEC-0152, DEC-0153, DEC-0154, DEC-0155, DEC-0156]
---

# EP-0005: Connectors & Identity

## Summary

The pluggable boundary adapters: the code-host connector (fork/branch/PR
orchestration, delegated reviews, branch-protection and team
administration, read-only context access), the Jira connector (projection
sync, drift capture, workflow telemetry), and identity (auth providers,
the person registry, OAuth linkage). Each sits behind a capability-declaring
contract so implementations are swappable; v1 targets Bitbucket Data Center.

## Why (Goal Alignment)

[BG-0001](../goals/BG-0001-groundwork.md) outcome 5 (sync without drift) is the Jira connector
([DEC-0002](../decisions/DEC-0002-doc-store-canonical.md),
[DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md)); the
PR gate itself now runs through the code-host connector
([DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md),
[DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md)); the agent's
existing-context awareness rides its read operations
([DEC-0016](../decisions/DEC-0016-agent-context-feeds.md),
[DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)).

## Scope

**In** (refined at [SES-0005](../sessions/SES-0005-ep-0005-refinement.md)):

- **Code-host connector** ([DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)):
  operations for fork/branch/worktree push, PR open/merge/review-state,
  review posting (per-user OAuth and program-user paths, per
  [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)),
  branch-protection and team/required-check administration (consumed by
  [EP-0003](EP-0003-governance-and-gate-engine.md)'s policy compiler), read-only browse/search filtered by the
  `governance/repos.yaml` allowlist ([DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md)),
  and a capability manifest with a documented minimum set. v1
  implementation: **Bitbucket Data Center**
  ([DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)).
- **Work-management connector** (generalized from "Jira connector" per
  [DEC-0155](../decisions/DEC-0155-pluggable-work-management-connector.md);
  release-2 scoped per
  [DEC-0148](../decisions/DEC-0148-work-management-stories-release-2.md)):
  host-agnostic contract with Jira Data Center as reference adapter;
  projection created on first merge to main; split
  field ownership — content canonical-owned, workflow Jira-owned read as
  projection-side telemetry ([DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md),
  [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md));
  drift detection with before/after capture; revert + Change Proposal
  creation ([DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md),
  [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)); editor
  redirection comments; the agent's backlog read feed
  ([DEC-0016](../decisions/DEC-0016-agent-context-feeds.md)).
- **Notifier connector** (added per
  [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)/[DEC-0149](../decisions/DEC-0149-notifier-story-under-ep-0005.md),
  amendment re-affirmed with the story-derivation gate): the delivery
  contract under the in-app notification center, plus the v1 email
  adapter.
- **Identity**: pluggable auth providers
  ([DEC-0024](../decisions/DEC-0024-pluggable-auth.md));
  `governance/people.yaml` person registry with stable person-ids
  ([DEC-0046](../decisions/DEC-0046-person-registry.md)); per-user OAuth
  host-identity linkage (tokens in the service secret store, never the
  repo); role-claims resolution for the gate engine.

**Out:** gate policy logic ([EP-0003](EP-0003-governance-and-gate-engine.md) — this epic executes its compilation
requests); CP triage ([EP-0002](EP-0002-refinement-session-agent.md) — the agent triages what this epic captures);
what the agent does with read context ([EP-0002](EP-0002-refinement-session-agent.md)); writing to codebases
(out entirely, per [DEC-0014](../decisions/DEC-0014-docs-are-the-product.md)).

## Domain Context

Bounded context: **Integration**. Terms: Connector, Projection, Drift,
Change Proposal — per [CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Code-host connector contract** + capability manifest schema + the
  minimum capability set (CMP-level) — bound by
  [CMP-0001](../components/CMP-0001-artifact-store-service.md)'s
  forward-declared consumption list
  ([DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md))
  and the gate engine's registration/administration operations
  ([DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
- **Work-management connector contract**: projection operations,
  field-ownership map, drift events with diffs, backlog read,
  projection-side telemetry
  ([DEC-0155](../decisions/DEC-0155-pluggable-work-management-connector.md),
  [DEC-0151](../decisions/DEC-0151-workflow-telemetry-projection-side.md)).
- **Notifier connector contract**: delivery operations, capability
  manifest, channel preferences
  ([DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
- **Auth provider contract**: authenticate → auth subject; person-id
  resolution against the registry; role claims for [EP-0003](EP-0003-governance-and-gate-engine.md).
- **Person registry schema**: `governance/people.yaml` (tier-1 validated;
  schema owned by [ST-0012](../stories/ST-0012-governance-config-schemas.md)).
- **Attribution block schema**: the service-signed program-user review
  attribution ([DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).
- **CP creation operation**: the typed write connectors use to file
  proposals ([DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).

## Risks & Open Questions

All four recorded risks were resolved at story derivation
([SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md)):

- BBDC required-check surface → spike
  [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)
  ([DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md));
  [ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md)
  cannot gate before its findings land.
- Jira flavor → confirmed Data Center, generalized to a pluggable
  work-management contract
  ([DEC-0155](../decisions/DEC-0155-pluggable-work-management-connector.md));
  DC webhook/event validation happens when the release-2 stories revive.
- Program-user attribution → service-signed attribution block
  ([DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).
- Bootstrap identity migration → criterion 5 of
  [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md).

## Derived Work

Derived at [SES-0026](../sessions/SES-0026-ep-0005-story-derivation.md):

- Current release:
  [ST-0019](../stories/ST-0019-code-host-connector-protocol.md) (connector
  protocol & capability manifest),
  [ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md) (BBDC
  connector),
  [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md)
  (delegated reviews & attribution),
  [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)
  (identity & person resolution),
  [ST-0023](../stories/ST-0023-read-only-context-access.md) (read-only
  context access),
  [ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md)
  (notifier contract & email adapter);
  spike [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md).
- Release 2 (deferred per
  [DEC-0148](../decisions/DEC-0148-work-management-stories-release-2.md)):
  [ST-0025](../stories/ST-0025-work-management-projection-lifecycle.md),
  [ST-0026](../stories/ST-0026-work-management-drift-capture.md),
  [ST-0027](../stories/ST-0027-work-management-backlog-read-feed.md).
- Backlog, trigger-subscribed (per
  [DEC-0156](../decisions/DEC-0156-future-connector-families-deferred.md),
  [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)):
  [ST-0028](../stories/ST-0028-additional-code-host-connectors.md),
  [ST-0029](../stories/ST-0029-additional-notifier-adapters.md),
  [ST-0030](../stories/ST-0030-additional-work-management-connectors.md);
  spike [SP-0005](../spikes/SP-0005-external-secret-store-adapter.md).
- Component stubs:
  [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md),
  [CMP-0006](../components/CMP-0006-bitbucket-data-center-connector.md),
  [CMP-0007](../components/CMP-0007-identity-and-access.md),
  [CMP-0008](../components/CMP-0008-notification-delivery.md).
