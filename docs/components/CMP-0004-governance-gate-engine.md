---
id: CMP-0004
type: component
title: Governance & Gate Engine
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: governance
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [CMP-0001, CMP-0002, CMP-0003]
cites: [DEC-0005, DEC-0007, DEC-0018, DEC-0020, DEC-0028, DEC-0033, DEC-0034,
        DEC-0036, DEC-0037, DEC-0038, DEC-0039, DEC-0040, DEC-0041, DEC-0042,
        DEC-0043, DEC-0045, DEC-0046, DEC-0049, DEC-0050, DEC-0054, DEC-0063,
        DEC-0075, DEC-0079, DEC-0096, DEC-0097, DEC-0102, DEC-0121, DEC-0124,
        DEC-0127, DEC-0130, DEC-0131, DEC-0132, DEC-0136, DEC-0140, DEC-0141,
        DEC-0142, DEC-0143, DEC-0144, DEC-0145, DEC-0146, DEC-0147, DEC-0150,
        DEC-0162, DEC-0163, DEC-0164, DEC-0165, DEC-0172, DEC-0173]
---

# CMP-0004: Governance & Gate Engine

## Purpose

The rules layer of Groundwork: compiles governance-as-code onto host
branch protection, computes the `gate-policy` and `conflicts-open`
required checks, runs staleness sweeps with re-affirmation flows,
operates the Arbiter conflict queue, and emits the governance event log
with its metrics/query API — the component
[EP-0003](../epics/EP-0003-governance-and-gate-engine.md)'s stories
build.

## Ubiquitous Language

Governance-as-Code, Gate, Gate Policy, Approver, Arbiter, Stale,
Impact Analysis, Re-affirmation, Governance Event Log, Item Branch,
Session Worktree, Mechanical Write, Decision Rights — per
[CONTEXT.md](../../CONTEXT.md). No new terms introduced.

## Design Elements

Decomposition per [DEC-0162](../decisions/DEC-0162-cmp-0004-element-decomposition.md):
ten elements, none graduated — the mandatory pre-gate graduation review
([DEC-0136](../decisions/DEC-0136-graduation-review-required.md)) found
no element consumed by more than one CMP or needing independently
versioned conformance. The governance file schemas are owned and
published by [CMP-0001](CMP-0001-artifact-store-service.md)
(`SchemaValidator.D-2`), so no other component needs a standalone
seam onto this one today. All API items resolve against this document's
own value/event elements or against dependency contracts named in
`## Dependencies`, per the schema-resolution rule
([DEC-0089](../decisions/DEC-0089-api-schema-resolution-rule.md)).

### GovernanceConfig (value)

Implements: [ST-0012](../stories/ST-0012-governance-config-schemas.md)

- `GovernanceConfig.D-1` — the parsed, typed representation of the five
  `governance/` files (`roles.yaml`, `domains.yaml`,
  `gate-policies.yaml`, `repos.yaml`, `people.yaml`) at a resolving git
  ref; schema shape is exactly
  [CMP-0001](CMP-0001-artifact-store-service.md)'s published
  `SchemaValidator.D-2` assets — this element defines no schema of its
  own, only the in-memory value every other element in this component
  reads. Equality by value at a given ref; never persisted
  independently of git (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
  [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
- `GovernanceConfig.D-2` — role membership entries carry stable
  person-ids from `people.yaml` and optional time-bounded delegation
  windows; domain entries carry an approver-routing target and an
  optional exclusivity flag; gate-policy entries carry per-artifact-type
  committee composition and a timeout-to-default default rule
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
  [DEC-0020](../decisions/DEC-0020-configurable-gate-policies.md),
  [DEC-0046](../decisions/DEC-0046-person-registry.md)).

### GovernanceInit (service)

Implements: [ST-0012](../stories/ST-0012-governance-config-schemas.md)

- `GovernanceInit.A-1` — `init(deployment-config) → {commit-sha}`.
  Writes the founding `governance/` files — initial Arbiter and role
  assignments taken from deployment configuration — directly into the
  repository's initial history, before `PolicyCompiler` first runs
  (per [DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)).
- `GovernanceInit.B-1` — one-time bootstrap: this operation runs
  exactly once, before the first `PolicyCompiler.A-2` provisioning
  call; after it, no evaluator anywhere carries an empty-governance
  special case (per [DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)).

### PolicyCompiler (service)

Implements: [ST-0013](../stories/ST-0013-policy-compilation-host-provisioning.md)

- `PolicyCompiler.A-1` — `compile(governance-ref) →
  {branch-protection-plan, team-sync-plan, required-checks[]}`. Pure
  translation from `GovernanceConfig` at the given ref to a host-neutral
  plan: directory→reviewer-group mappings with minimum approval counts,
  team membership by person-id, and the required-check catalog
  (per [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
- `PolicyCompiler.A-2` — `provision(plan) → ok |
  problem(host-provisioning-failed)`. Applies a compiled plan to the
  host via the code-host connector's branch-protection and
  team-administration operations; host-username resolution for
  person-ids stays connector-side
  (per [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md),
  [DEC-0046](../decisions/DEC-0046-person-registry.md),
  [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
- `PolicyCompiler.B-1` — host teams are projections of
  `GovernanceConfig` role membership, created and synced through the
  connector's team-administration operations only — never edited
  host-side as truth (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md)).
- `PolicyCompiler.B-2` — registers every required check —
  `gate-policy`, `conflicts-open`, the tier-2 suite, the
  mechanical-diff validator, and the System-Decision template-
  conformance check — and is the single writer and reconciler of
  branch-protection settings; no other component registers a required
  check (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md),
  [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md),
  [DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md)).
- `PolicyCompiler.B-3` — a merge under `governance/` triggers
  `compile` + `provision` again; drift between compiled host settings
  and `GovernanceConfig` reconciles toward the files
  (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
  [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
- `PolicyCompiler.B-4` — the first `provision` call after
  `GovernanceInit.A-1`'s commit locks gating in behind the founding
  configuration (per [DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)).
- `PolicyCompiler.B-5` — all host interactions go through the
  code-host connector contract and respect its capability manifest; v1
  target is GitHub (cloud)
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
  [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md)).

### GatePolicyCheck (service)

Implements: [ST-0014](../stories/ST-0014-gate-policy-check.md)

- `GatePolicyCheck.A-1` — `evaluate(pr-ref) →
  {verdict: pass|fail, explanation, missing[]}`. Reads
  `GovernanceConfig` at the PR's target-branch ref, PR review state (via
  the code-host connector), staleness state (via
  [CMP-0001](CMP-0001-artifact-store-service.md)'s `StorageService`
  and forward-declared Graph Index queries), and open-conflict state,
  fresh on every call — no cached intermediate
  (per [DEC-0164](../decisions/DEC-0164-gate-policy-check-live-evaluation.md)).
- `GatePolicyCheck.B-1` — evaluates the rich policy layer: domain-
  conditional approvers, role verification against `GovernanceConfig`,
  and committee quorum composition by distinct roles
  (per [DEC-0020](../decisions/DEC-0020-configurable-gate-policies.md),
  [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
- `GatePolicyCheck.B-2` — fails while any ancestor of the PR's artifact
  is stale; passes only once every stale ancestor has cleared
  (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)).
- `GatePolicyCheck.B-3` — any pool member of the required role
  satisfies a gate by default; domain preference affects routing only,
  unless the policy sets an exclusivity flag, in which case only the
  named approver or their active time-bounded delegate passes
  (per [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md)).
- `GatePolicyCheck.B-4` — reviews posted by a program user pass only
  with verified human attribution
  (per [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
- `GatePolicyCheck.B-5` — every verdict carries a human-readable
  explanation naming the governing policy and the satisfying facts, and
  on failure, exactly what is missing
  (per [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)).
- `GatePolicyCheck.B-6` — verdicts recompute idempotently on relevant
  ChangeEvents and host webhooks, with a periodic reconciliation sweep
  re-verifying all open PRs as the backstop
  (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)).
- `GatePolicyCheck.B-7` — merging a governance change bulk-
  recomputes this check on every open PR under the new policy; existing
  host reviews stand as facts re-evaluated against it
  (per [DEC-0141](../decisions/DEC-0141-midflight-policy-recompute.md)).
- `GatePolicyCheck.B-8` — on the machine-verified path — program-user
  auto-PRs for mechanical writes and System Decisions — the check
  passes with program-user approval when the corresponding validator
  (mechanical-diff or template-conformance) passes; machine
  verification substitutes for role-pool approval on exactly these PRs
  and no others (per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md),
  [DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md)).

### ConflictGate (service)

Implements: [ST-0015](../stories/ST-0015-conflicts-open-check-and-operations.md)

- `ConflictGate.A-1` — `evaluate(pr-ref) → {verdict: pass|fail,
  explanation}` — the `conflicts-open` required check. Fails any gate
  PR whose artifact links an unresolved Conflict; clears only when the
  conflict is resolved by a ratified Decision or explicit withdrawal.
  Machine-verified auto-PRs (mechanical writes, System Decisions) remain
  governed by their own validators, never blocked here
  (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
  [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `ConflictGate.A-2` — `escalate(conflict-id) → {queue-entry}`. Surfaces
  an unresolved Conflict to the Arbiter's derived work queue and fires a
  notification through the notification center
  (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
  [DEC-0147](../decisions/DEC-0147-derived-queue-views.md),
  [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
- `ConflictGate.A-3` — `resolve(conflict-id, decision-ref) → ok |
  problem(decision-not-ratifying)`. Records that the conflict resolves
  citing the given ratified Decision or an explicit withdrawal
  (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
  [DEC-0165](../decisions/DEC-0165-conflict-gate-operation-surface.md)).
- `ConflictGate.A-4` — `override-approver(gate-ref, new-approver) →
  ok`. Arbiter reassignment of a gate's approver, independent of
  conflict state (per [DEC-0165](../decisions/DEC-0165-conflict-gate-operation-surface.md)).
- `ConflictGate.B-1` — no conflict resolves by timeout by default:
  aging conflicts escalate in visibility (reminders, dashboard
  prominence), never in state
  (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)).
- `ConflictGate.B-2` — the per-artifact timeout-to-default election is
  expressed in artifact frontmatter (naming the period and the
  configured default rule) and tier-1 validated by
  [CMP-0001](CMP-0001-artifact-store-service.md); it is not a service
  operation of this element
  (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
  [DEC-0034](../decisions/DEC-0034-two-tier-validation.md),
  [DEC-0165](../decisions/DEC-0165-conflict-gate-operation-surface.md)).
- `ConflictGate.B-3` — when an elected timeout fires, this element
  drafts the System Decision from the fixed template — citing the
  election and the default rule — and lands it through the auto-PR
  machinery gated by the template-conformance check; the conflict then
  resolves citing that Decision
  (per [DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md),
  [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
  [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).

### StalenessSweepService (service)

Implements: [ST-0016](../stories/ST-0016-staleness-sweep-impact-analysis.md)

- `StalenessSweepService.A-1` — `sweep(change-event) → {affected:
  ArtifactId[], report: ImpactReport}`. Invoked on a ChangeEvent
  indicating a change to an approved artifact.
- `StalenessSweepService.B-1` — computes the affected set via
  forward-declared Graph Index queries — the full derived subtree plus,
  for an amended or superseded story, every Component Doc with an
  element whose `Implements:` line references it — and marks every
  approved member stale in one mechanical sweep of `mark-stale`
  operations — the `mark-stale` member of
  [CMP-0001](CMP-0001-artifact-store-service.md)'s
  `MechanicalWriteService.A-1..A-8` closed operation set
  (per [DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md),
  [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
  [DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md),
  [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `StalenessSweepService.B-2` — idempotent under at-least-once
  ChangeEvent redelivery: re-processing the same event produces no
  duplicate marks or reports
  (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)).
- `StalenessSweepService.B-3` — stale state produced here is what
  blocks: `GatePolicyCheck.B-2` consumes it, and new derivation from a
  stale artifact is refused until cleared
  (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)).

### ImpactReport (value)

Implements: [ST-0016](../stories/ST-0016-staleness-sweep-impact-analysis.md)

- `ImpactReport.D-1` — schema: what changed (source artifact + diff
  ref), the affected set including in-flight work (open PRs on
  affected artifacts), the specific referencing elements of any
  Component Doc staled over an `Implements` edge, and the approvers
  affected (per [DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md),
  [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
  [DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md)).
- `ImpactReport.D-2` — never committed to the canonical repository:
  written into affected re-affirmation PR descriptions and stored in
  `GovernanceEventLog` as telemetry-grade data only
  (per [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md),
  [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md)).

### ReaffirmationService (service)

Implements: [ST-0017](../stories/ST-0017-reaffirmation-flow-queues.md)

- `ReaffirmationService.A-1` — `open-reaffirmation(artifact-id) →
  {item-branch, pr-ref}`. Reuses the artifact's existing item branch and
  gate-PR machinery ([CMP-0001](CMP-0001-artifact-store-service.md)
  `BranchOrchestrator.A-2`), carrying the upstream diff and the
  `ImpactReport` in the PR description
  (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
  [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md),
  [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md)).
- `ReaffirmationService.A-2` — `get-approver-queue(approver-id) →
  {entries: QueueEntry[]}`. A derived view — computed at read time from
  stale artifacts, open gate PRs, governance routing, and delegations —
  ordered by impact rank
  (per [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md),
  [DEC-0147](../decisions/DEC-0147-derived-queue-views.md)).
- `ReaffirmationService.B-1` — approving a re-affirmation PR clears the
  mark via the `clear-stale` member of
  [CMP-0001](CMP-0001-artifact-store-service.md)'s
  `MechanicalWriteService.A-1..A-8` closed operation set
  (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
  [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `ReaffirmationService.B-2` — rejecting a re-affirmation routes the
  artifact to full re-refinement (a new session); the rejection is
  recorded in `GovernanceEventLog`
  (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)).
- `ReaffirmationService.B-3` — queue ordering uses human-judgment
  impact-edge ranking until
  [SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md)'s algorithm
  lands; no persisted queue truth exists — recomputed on every read
  (per [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md),
  [DEC-0147](../decisions/DEC-0147-derived-queue-views.md)).
- `ReaffirmationService.B-4` — queue notifications are batched per user
  preference and delivered through the notification center
  (per [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md),
  [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).

### GovernanceEvent (event)

Implements: [ST-0018](../stories/ST-0018-governance-event-log-metrics.md)

- `GovernanceEvent.D-1` — envelope: `event-id`, `event-type` (closed
  enum: `gate-transition`, `staleness-sweep`, `staleness-clear`,
  `reaffirm-outcome`, `conflict-lifecycle`, `check-registration`,
  `check-recomputation`, `system-decision-auto-resolution`), `grade`
  (`provenance` | `telemetry`), `timestamp`, `artifact-ref`, `payload`
  (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
  [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md)).
- `GovernanceEvent.B-1` — emission and ordering: per-artifact ordering,
  at-least-once delivery, consistent with
  [CMP-0002](CMP-0002-change-event.md)'s emission semantics.
  Provenance-grade events emit only after the fact they mirror has
  landed in git or host history; telemetry-grade events emit at the
  time of the operation they describe
  (per [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md)).

### GovernanceEventLog (service)

Implements: [ST-0018](../stories/ST-0018-governance-event-log-metrics.md)

- `GovernanceEventLog.A-1` — `get-approval-latency(range) → {p50, p90,
  samples[]}` (per [DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)).
- `GovernanceEventLog.A-2` — `get-stale-counts(range) → {by-type,
  by-age-bucket}` (per [DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)).
- `GovernanceEventLog.A-3` — `get-conflict-aging(range) → {open[],
  resolved[], age-histogram}` (per [DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)).
- `GovernanceEventLog.A-4` — `get-gate-throughput(range) → {merged,
  rejected, pending}` (per [DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)).
- `GovernanceEventLog.A-5` — `search-events(filter) → {events:
  GovernanceEvent[]}`, answering only from provenance-grade events
  (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
  [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md),
  [DEC-0163](../decisions/DEC-0163-governance-metrics-api-named-endpoints.md)).
- `GovernanceEventLog.B-1` — accepts a `GovernanceEvent` from every
  other element in this contract on its governance-relevant
  transitions (gate transitions, sweeps and clears, re-affirmation
  outcomes, conflict lifecycle, check registrations and
  recomputations, System-Decision auto-resolutions); this intake path
  is internal to the component, not a boundary-crossing API item
  (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md),
  [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md)).
- `GovernanceEventLog.B-2` — persists behind the App Database Port
  ([CMP-0003](CMP-0003-app-database-port.md)); no consumer or engine
  code touches a database engine API directly
  (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
  [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)).
- `GovernanceEventLog.B-3` — every event's declared grade governs its
  rebuild behavior: provenance-grade entries reconverge on rebuild from
  git and host history; telemetry-grade entries are dashboard-
  authoritative, lossy on rebuild, and never citable as provenance
  (per [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md)).
- `GovernanceEventLog.B-4` — the four named metric endpoints
  (`A-1`..`A-4`) may draw on both grades for aggregate counts;
  `search-events` (`A-5`) answers only from provenance-grade events
  (per [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)).

## Component Invariants

- `C-1` — **Governance is Arbiter-gated**: every change to a
  `governance/` file goes through the same item-branch/gate-PR flow as
  any artifact, and changing approval rights is itself a gated change —
  no direct-write path to `governance/` exists outside
  [CMP-0001](CMP-0001-artifact-store-service.md)'s gated write surface
  (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md)).
- `C-2` — **Single required-check registrant**: `PolicyCompiler` is the
  only writer and reconciler of what the host requires to merge; no
  other component in the system registers a required check
  (per [DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)).
- `C-3` — **No stale or contested merge**: no artifact with a stale
  ancestor, and no artifact linking an unresolved Conflict, can pass its
  gate — enforced by `GatePolicyCheck.B-2` and `ConflictGate.A-1`
  respectively, except on the machine-verified auto-PR path, which both
  checks explicitly exempt
  (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
  [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
  [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
- `C-4` — **Provenance/telemetry separation**: a telemetry-grade
  `GovernanceEvent` is never returned by a provenance query, and no
  design-content claim in this component is truth-bearing anywhere but
  a provenance-grade event or the canonical repo itself
  (per [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md),
  [DEC-0131](../decisions/DEC-0131-rebuild-sufficiency-invariant.md)).
- `C-5` — **No persisted queue truth**: the Arbiter queue and every
  approver queue are computed at read time; no code path writes queue
  membership or order to storage
  (per [DEC-0147](../decisions/DEC-0147-derived-queue-views.md)).

## Implementation Guidance

### Constraints

- `IG-1` — v1 code-host target is GitHub (cloud) via the connector
  contract; nothing in this component may depend on GitHub-specific
  behavior (per [DEC-0172](../decisions/DEC-0172-github-v1-bbdc-deferred.md),
  [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).
  `PolicyCompiler.B-2`/`B-5` rely on GitHub's Checks API /
  required-status-checks to host every required check this component
  registers (`gate-policy`, `conflicts-open`, the tier-2 suite, the
  mechanical-diff validator, the template-conformance check); GitHub's
  documented support for per-PR blocking, re-reporting, and un-passing
  an already-green check is what makes this a settled assumption rather
  than an open spike question here
  (per [DEC-0173](../decisions/DEC-0173-check-admin-no-longer-provisional.md)).
  The equivalent question for the now-deferred Bitbucket Data Center
  adapter remains
  [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)'s to
  answer, on revival
  (per [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md)).
- `IG-2` — `GovernanceEventLog` persists behind the App Database Port
  ([CMP-0003](CMP-0003-app-database-port.md)); v1 adapter is DuckDB
  (per [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
  [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
  [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
- `IG-3` — `ReaffirmationService.A-2`'s queue ordering is a
  human-judgment impact-edge heuristic until
  [SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md) lands a
  ranking algorithm; do not build a bespoke ranking model here
  (per [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md)).
- `IG-4` — the reference implementation is Python; the OpenAPI contract
  and schema assets are the deliverables of record and must stand
  language-neutral, published in the same shared OpenAPI document as
  [CMP-0001](CMP-0001-artifact-store-service.md)
  (per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
- `IG-5` — every non-2xx API response (`PolicyCompiler.A-2`,
  `ConflictGate.A-3`, and every other `problem(...)`-returning item in
  this contract) uses the RFC 9457 problem+json model with typed
  problem URIs, matching
  [CMP-0001](CMP-0001-artifact-store-service.md)'s error convention
  (per [DEC-0127](../decisions/DEC-0127-problem-json-error-model.md)).

### Notes

- Build and test every connector-consuming element (`PolicyCompiler`,
  `GatePolicyCheck`, `ConflictGate`) against the local-git fake
  connector first, per
  [CMP-0001](CMP-0001-artifact-store-service.md)'s established pattern
  (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).
- `GovernanceEvent` is a distinct schema from
  [CMP-0002](CMP-0002-change-event.md)'s `ChangeEvent` — don't collapse
  them or invent a second delivery mechanism; this component both
  consumes ChangeEvents (to trigger sweeps and recomputation) and emits
  GovernanceEvents (to record what it did).
- `StalenessSweepService.B-1`'s subtree computation and
  `ReaffirmationService.A-2`'s queue view both depend on Graph Index
  queries that do not yet have a contract — see `## Dependencies`.
  Build against a stub query interface first; bind for real once
  [EP-0004](../epics/EP-0004-graph-index.md) is refined.

## Dependencies

- [CMP-0001](CMP-0001-artifact-store-service.md) — consumed sections:
  `StorageService.A-1`/`A-2` (reading and writing `governance/` files
  and artifact frontmatter), the `mark-stale`/`clear-stale` members of
  `MechanicalWriteService.A-1..A-8`, `BranchOrchestrator.A-1`/`A-2`
  (item-branch and gate-PR reuse for re-affirmation),
  `SchemaValidator.D-2` (governance file schema assets).
- [CMP-0002](CMP-0002-change-event.md) — the ChangeEvent stream this
  component subscribes to for sweep and check-recomputation triggers;
  consumed sections: payload schema and emission semantics
  (`ChangeEvent.D-1`, `ChangeEvent.B-1`).
- [CMP-0003](CMP-0003-app-database-port.md) — the app database port
  `GovernanceEventLog` persists behind; consumed sections: all
  operation families and the atomicity guarantee
  (`AppDatabasePort.A-1..A-3`, `AppDatabasePort.B-1`).
- **Code-host connector contract** ([EP-0005](../epics/EP-0005-connectors-and-identity.md);
  future standalone `protocol`-type CMP per
  [DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md)) —
  consumption forward-declared per
  [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
  binding on [EP-0005](../epics/EP-0005-connectors-and-identity.md)'s
  refinement. Operations consumed: branch-protection administration;
  team creation/sync; required-check registration; check-run result
  posting; PR review-state reads; permission probe. All consumed per
  the capability manifest; hermetic testing via the local-git fake
  connector (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md),
  [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).
- **Graph Index queries** ([EP-0004](../epics/EP-0004-graph-index.md),
  not yet a standalone CMP) — consumption forward-declared, binding on
  [EP-0004](../epics/EP-0004-graph-index.md)'s refinement. Operations
  consumed: derived-subtree traversal from a changed artifact;
  reverse `Implements`-edge lookup for Component Doc elements
  (per [DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md)).
  Query results carry frontmatter metadata only, never artifact bodies
  (per [DEC-0063](../decisions/DEC-0063-metadata-only-graph.md)):
  `StalenessSweepService` and `ReaffirmationService` fetch any body
  content they need (e.g. for an `ImpactReport`'s human-readable
  description) via
  [CMP-0001](CMP-0001-artifact-store-service.md)'s `StorageService`,
  never by assuming the graph query returns it.
- **Notification center / notifier connectors**
  ([EP-0005](../epics/EP-0005-connectors-and-identity.md)/[EP-0006](../epics/EP-0006-refinement-web-ui.md),
  not yet a standalone CMP) — consumption forward-declared. Operations
  consumed: batched notification delivery for queue updates and
  conflict escalations
  (per [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).

## Acceptance & Test Expectations

1. OpenAPI conformance suite runs against this component's published
   contract items, sharing the document
   [CMP-0001](CMP-0001-artifact-store-service.md) publishes to
   (per [DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md)).
2. The full compilation, provisioning, and check suite passes
   hermetically against the local-git fake connector
   (per [DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)).
3. `GatePolicyCheck` regression suite exercises domain-conditional
   approvers, committee quorum, staleness blocking, exclusivity
   routing, and program-user attribution scenarios against fixture
   `GovernanceConfig` values.
4. Sweep idempotency: replaying the same ChangeEvent through
   `StalenessSweepService` produces no duplicate `mark-stale` operations
   and no duplicate `ImpactReport`.
5. Two-grade log conformance: a log rebuilt from git plus host history
   reconverges on every provenance-grade `GovernanceEvent`; telemetry-
   grade events are verified absent from `search-events` results.
6. Queue derivation: `ReaffirmationService.A-2` and `ConflictGate`'s
   Arbiter queue recompute correctly from fixture graph state with no
   backing queue table in the app database.

## Out of Scope

Boundary statements (per [DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md),
each linking its owning artifact where one exists):

- **No connector implementation** — the code-host connector protocol
  and its GitHub adapter (v1) are
  [EP-0005](../epics/EP-0005-connectors-and-identity.md)'s
  ([CMP-0005](CMP-0005-code-host-connector-protocol.md)/[CMP-0009](CMP-0009-github-connector.md);
  the deferred Bitbucket Data Center adapter is
  [CMP-0006](CMP-0006-bitbucket-data-center-connector.md)).
  This component only consumes the contract.
- **No notification adapter implementation** — delivery mechanics
  (email, future channels) belong to
  [EP-0005](../epics/EP-0005-connectors-and-identity.md)'s notifier
  connectors and [EP-0006](../epics/EP-0006-refinement-web-ui.md)'s
  notification center; this component only calls the delivery
  operation.
- **No dashboard rendering** — `GovernanceEventLog`'s metrics API is
  consumed, never rendered, here
  ([EP-0006](../epics/EP-0006-refinement-web-ui.md), per
  [DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)).
- **No graph query engine** — subtree traversal and `Implements`-edge
  lookup are consumed, not implemented, here
  ([EP-0004](../epics/EP-0004-graph-index.md)).
- **No impact-ranking algorithm** — queue ordering is a placeholder
  heuristic until [SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md)
  lands; this component must not grow its own ranking research.
- **No mediation or intent discovery** — the session agent mediates
  conflicts before they escalate; this component only enforces blocking
  and operates the post-escalation queue
  ([EP-0002](../epics/EP-0002-refinement-session-agent.md), per
  [DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md)).
- **No governance config UI editor** — the Admin UI edits, never
  stores, governance state
  ([EP-0006](../epics/EP-0006-refinement-web-ui.md), per
  [DEC-0037](../decisions/DEC-0037-governance-as-code.md)).
- **No identity/auth provider logic** — person-id resolution and
  host-username mapping beyond consuming `people.yaml` values belong to
  [EP-0005](../epics/EP-0005-connectors-and-identity.md)'s Identity &
  Access ([CMP-0007](CMP-0007-identity-and-access.md)).
