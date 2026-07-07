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
        DEC-0049, DEC-0050]
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
- **Jira connector**: projection created on first merge to main; split
  field ownership — content canonical-owned, workflow Jira-owned syncing in
  as telemetry ([DEC-0048](../decisions/DEC-0048-project-on-approval-field-ownership.md));
  drift detection with before/after capture; revert + Change Proposal
  creation ([DEC-0044](../decisions/DEC-0044-drift-revert-capture-proposal.md),
  [DEC-0047](../decisions/DEC-0047-change-proposal-artifact.md)); editor
  redirection comments.
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
  minimum capability set (CMP-level).
- **Jira connector contract**: projection operations, field-ownership map,
  drift events with diffs, telemetry sync.
- **Auth provider contract**: authenticate → auth subject; person-id
  resolution against the registry; role claims for [EP-0003](EP-0003-governance-and-gate-engine.md).
- **Person registry schema**: `governance/people.yaml` (tier-1 validated).
- **CP creation operation**: the typed write connectors use to file
  proposals ([DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).

## Risks & Open Questions

- BBDC gaps: no native path-scoped reviewer requirements — the
  `gate-policy` check carries more enforcement weight; validate that merge
  checks / Code Insights suffice as the required-check surface
  ([DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)) —
  candidate spike.
- Jira Data Center assumed (self-hosted Atlassian stack); confirm flavor
  and webhook/event capabilities for drift diffs during story refinement.
- Program-user attribution format: the cryptographic attribution scheme
  ([DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md))
  needs story-level design.
- Bootstrap-period identities: migrating email-based `decided-by`/`owner`
  values to person-ids once the registry exists
  ([DEC-0046](../decisions/DEC-0046-person-registry.md) implication).

## Derived Work

None yet — stories/spikes follow gate approval of this epic.
