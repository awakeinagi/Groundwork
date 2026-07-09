---
id: EP-0003
type: epic
title: Governance & Gate Engine
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-06
owner: eng-lead
created: 2026-07-05
overview: >-
  EP-0003 delivers the Governance & Gate Engine that enforces human
  ratification through the fork-pull model: compiles declarative
  governance configuration (roles, domains, gate policies) onto code-host
  branch protection and computed gate-policy and conflicts-open required
  checks; runs staleness sweeps with re-affirmation flows; operates the
  Arbiter conflict queue; and emits governance event logs. Gate policies
  are refined through DEC-0006, DEC-0020, DEC-0036-0042. Approved
  2026-07-06.
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
  impacts: [EP-0001, EP-0004, EP-0005, EP-0006, EP-0008]
  impacted-by: [EP-0001, EP-0002]
cites: [DEC-0006, DEC-0007, DEC-0020, DEC-0026, DEC-0028, DEC-0032, DEC-0034,
        DEC-0036, DEC-0037, DEC-0038, DEC-0039, DEC-0040, DEC-0041, DEC-0042]
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
(DEC-0006,
DEC-0020) — realized
under the fork-pull model as PR gating
(DEC-0028). The staleness
machinery (DEC-0007,
DEC-0038) keeps
the traceability graph honest as intent evolves — alignment maintained over
time, not just at creation.

## Scope

**In** (refined at SES-0004):

- **Policy enforcement** (DEC-0036):
  coarse rules compiled to host branch protection (artifact-type directory →
  reviewer group, approval counts for committees); rich rules
  (domain-conditional approvers, quorum composition, ancestor staleness,
  open conflicts) computed as the required `gate-policy` status check.
- **Governance-as-code** (DEC-0037):
  `governance/roles.yaml`, `domains.yaml`, `gate-policies.yaml` in the
  canonical repo, PR-gated with the Arbiter as owner; the gate engine
  recompiles host protections on change; host teams are projections of
  `roles.yaml`.
- **Staleness** (DEC-0038):
  full-subtree mechanical sweeps with attached impact reports; stale
  ancestors fail descendants' `gate-policy` checks and block new
  derivation; cleared by lightweight re-affirmation PRs, escalating to full
  re-refinement only on rejection.
- **Conflict operations** (DEC-0039):
  Arbiter work queue with notifications; `conflicts-open` blocking check;
  no auto-timeout by default, per-artifact election of timeout-to-default
  with system Decisions recording auto-resolutions.
- **Delegation** (DEC-0040):
  role-pool approval by default (domain mapping = routing preference);
  explicit time-bounded delegation entries for exclusivity.
- **Queueing** (DEC-0041):
  per-approver work queues ordered by impact rank (SP-0001's algorithm;
  human judgment until it lands), batched notifications.
- **Observability** (DEC-0042):
  governance event log + language-neutral metrics/query API.

**Out:** identity/auth itself (EP-0005); the approval and dashboard UI
(EP-0006, per DEC-0032 and
DEC-0042); conflict
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
  tier-1 validated (DEC-0034).
- **Policy compilation contract**: governance config → host
  branch-protection settings, via EP-0005's team/required-check
  administration operations.
- **`gate-policy` / `conflicts-open` check contracts**: inputs (PR, graph
  state, governance config) → pass/fail with human-readable explanation.
  EP-0008's inbound API enforces gates by calling into these checks, so
  their contract shape constrains the platform's gate-action endpoints
  (the EP-0003→EP-0008 impact edge).
- **Impact-analysis contract**: changed artifact → affected set + impact
  report (consumes EP-0004 graph queries; requests EP-0001 mechanical
  writes). The affected set is computed over the directional impact
  links (DEC-0026).
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

Derived at SES-0025:

- CMP-0004 —
  Governance & Gate Engine (stub; contract-completed by the stories
  below)
- ST-0012 —
  Governance configuration schemas and lifecycle
- ST-0013 —
  Policy compilation and host provisioning
- ST-0014 — The `gate-policy`
  required check
- ST-0015 —
  The `conflicts-open` check and conflict operations
- ST-0016 —
  Staleness sweeps and impact analysis
- ST-0017 —
  Re-affirmation flow and approver queues
- ST-0018 —
  Governance event log and metrics API

Post-derivation additions:

- SES-0029 — component refinement of CMP-0004 (element decomposition
  and contract shape)
- CMP-0016 — Governance Config & Role Resolution (component, graduated
  out of CMP-0004)
