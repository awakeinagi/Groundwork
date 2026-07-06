---
id: EP-0003
type: epic
title: Governance & Gate Engine
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0001, EP-0004, EP-0005, EP-0006]
  impacted-by: [EP-0001]
cites: [DEC-0006, DEC-0007, DEC-0020, DEC-0026, DEC-0028, DEC-0032, DEC-0036,
        DEC-0037, DEC-0038, DEC-0039, DEC-0040, DEC-0041, DEC-0042]
---

# EP-0003: Governance & Gate Engine

## Summary

The rules layer: roles, gate policies, approvals, and change propagation.
Compiles declarative governance configuration onto code-host branch
protection, computes the `gate-policy` and `conflicts-open` required checks
that make PR merges meaningful, runs staleness sweeps with re-affirmation
flows, operates the Arbiter conflict queue, and emits the governance event
log.

## Why (Goal Alignment)

BG-0001 outcome 3 (human-ratified layers) is this epic
([DEC-0006](../decisions/DEC-0006-gate-every-stage.md),
[DEC-0020](../decisions/DEC-0020-configurable-gate-policies.md)) — realized
under the fork-pull model as PR gating
([DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md)). The staleness
machinery ([DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md),
[DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)) keeps
the traceability graph honest as intent evolves — alignment maintained over
time, not just at creation.

## Scope

**In** (refined at [SES-0004](../sessions/SES-0004-ep-0003-refinement.md)):

- **Policy enforcement** ([DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)):
  coarse rules compiled to host branch protection (artifact-type directory →
  reviewer group, approval counts for committees); rich rules
  (domain-conditional approvers, quorum composition, ancestor staleness,
  open conflicts) computed as the required `gate-policy` status check.
- **Governance-as-code** ([DEC-0037](../decisions/DEC-0037-governance-as-code.md)):
  `governance/roles.yaml`, `domains.yaml`, `gate-policies.yaml` in the
  canonical repo, PR-gated with the Arbiter as owner; the gate engine
  recompiles host protections on change; host teams are projections of
  `roles.yaml`.
- **Staleness** ([DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)):
  full-subtree mechanical sweeps with attached impact reports; stale
  ancestors fail descendants' `gate-policy` checks and block new
  derivation; cleared by lightweight re-affirmation PRs, escalating to full
  re-refinement only on rejection.
- **Conflict operations** ([DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)):
  Arbiter work queue with notifications; `conflicts-open` blocking check;
  no auto-timeout by default, per-artifact election of timeout-to-default
  with system Decisions recording auto-resolutions.
- **Delegation** ([DEC-0040](../decisions/DEC-0040-role-pool-delegation.md)):
  role-pool approval by default (domain mapping = routing preference);
  explicit time-bounded delegation entries for exclusivity.
- **Queueing** ([DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md)):
  per-approver work queues ordered by impact rank (SP-0001's algorithm;
  human judgment until it lands), batched notifications.
- **Observability** ([DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)):
  governance event log + language-neutral metrics/query API.

**Out:** identity/auth itself (EP-0005); the approval and dashboard UI
(EP-0006, per [DEC-0032](../decisions/DEC-0032-ui-wraps-pr-gate.md) and
[DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)); conflict
mediation content (EP-0002 — this epic enforces blocking; the agent
mediates); commit construction (EP-0001 executes mechanical writes this
epic requests).

## Domain Context

Bounded context: **Governance**. Terms: Gate, Gate Policy, Approver,
Arbiter, Impact Analysis, Stale, Re-affirmation — per
[CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Governance config schemas**: roles, domains (with exclusivity flags),
  gate policies (including committee composition and timeout elections) —
  tier-1 validated ([DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
- **Policy compilation contract**: governance config → host
  branch-protection settings, via EP-0005's team/required-check
  administration operations.
- **`gate-policy` / `conflicts-open` check contracts**: inputs (PR, graph
  state, governance config) → pass/fail with human-readable explanation.
- **Impact-analysis contract**: changed artifact → affected set + impact
  report (consumes EP-0004 graph queries; requests EP-0001 mechanical
  writes).
- **Re-affirmation flow contract**: stale artifact → re-affirm PR →
  cleared/rejected.
- **Metrics/query API**: governance event log access for EP-0006
  dashboards.

## Risks & Open Questions

- Mid-flight policy changes: recomputing open PRs' checks when
  `roles.yaml`/`gate-policies.yaml` change — recomputation semantics at
  story level.
- Host review-semantics variance (Bitbucket vs GitHub approval/dismissal
  behavior) — pinned during EP-0005 refinement (impact edge EP-0003→EP-0005).
- Bootstrap: initial Arbiter and roles at deployment, before governance
  files exist to gate their own creation.

## Derived Work

None yet — stories/spikes follow gate approval of this epic.
