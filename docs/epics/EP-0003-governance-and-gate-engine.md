---
id: EP-0003
type: epic
title: Governance & Gate Engine
status: draft
owner: eng-lead
created: 2026-07-05
links:
  derives-from: [BG-0001]
  satisfies: [BG-0001]
  depends-on: [EP-0001]
cites: [DEC-0006, DEC-0007, DEC-0020]
---

# EP-0003: Governance & Gate Engine

## Summary

The rules layer: roles, gate policies, approvals, and change propagation.
Enforces that every artifact passes its human gate before the next stage
derives from it, supports both fixed role→gate mapping and committee gates,
and runs impact analysis that marks descendants stale when approved
artifacts change.

## Why (Goal Alignment)

BG-0001 outcome 3 (human-ratified layers) is this epic
([DEC-0006](../decisions/DEC-0006-gate-every-stage.md),
[DEC-0020](../decisions/DEC-0020-configurable-gate-policies.md)). The
staleness machinery ([DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md))
is what keeps the traceability graph honest as intent evolves — alignment is
maintained over time, not just at creation.

## Scope

**In:** role model (Stakeholder, Product Owner, Eng Lead, DS Lead, Arbiter);
gate policy configuration per artifact type (single-role and committee);
approver auto-assignment per domain/team mapping with Arbiter override;
approval/rejection flows and their audit trail; impact analysis over the
graph (via EP-0004) on artifact change and Decision supersession; stale
marking and re-ratification flow; downstream-generation blocking for stale
and conflict-linked artifacts.

**Out:** identity/auth itself (EP-0005); the approval UI (EP-0006); conflict
mediation content (EP-0002 — this epic enforces the blocking, the agent does
the mediating).

## Domain Context

Bounded context: **Governance**. Terms: Gate, Gate Policy, Approver,
Arbiter, Impact Analysis, Stale — per [CONTEXT.md](../../CONTEXT.md).

## Interfaces & Contracts to Define

- **Gate policy schema**: declarative configuration mapping artifact types →
  approval requirements.
- **Approval API**: request, sign-off, rejection with reasons, committee
  quorum evaluation.
- **Impact-analysis contract**: changed-artifact → affected-set + impact
  report, consumed by re-refinement queueing.

## Risks & Open Questions

- Stale semantics for in-flight implementation work (component already
  handed off): how the impact report reaches consumers of an emitted
  Handoff Manifest — candidate spike.
- Approval delegation and vacation coverage — policy question for the
  refinement session on this epic.

## Derived Work

None yet — stories/spikes follow refinement and approval of this epic.
