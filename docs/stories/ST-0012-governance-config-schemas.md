---
id: ST-0012
type: story
title: Governance configuration schemas and lifecycle
status: gated
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  impacts: [ST-0013, ST-0014, ST-0015, ST-0017]
cites: [DEC-0034, DEC-0037, DEC-0039, DEC-0040, DEC-0046, DEC-0049, DEC-0054,
        DEC-0140]
---

# ST-0012: Governance Configuration Schemas and Lifecycle

## Summary

The governance-as-code surface: schemas, validation, and lifecycle for
the four `governance/` files — who holds which role and decision
rights, how domains route to approvers, what each gate requires, and
which repositories the agent may read — plus the deployment-time
seeding that bootstraps them.

## Acceptance Criteria

1. Published schemas cover the full governance file set:
   `governance/roles.yaml` (role membership, per-role decision rights,
   time-bounded delegation entries), `governance/domains.yaml`
   (domain→approver routing with exclusivity flags),
   `governance/gate-policies.yaml` (per-artifact-type gate policies,
   committee composition, timeout-to-default defaults),
   `governance/repos.yaml` (repository read allowlist with path
   excludes), and `governance/people.yaml` (the person registry —
   stable person-ids that `roles.yaml` membership and provenance
   fields reference)
   (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md),
   [DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md),
   [DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
   [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
   [DEC-0049](../decisions/DEC-0049-repo-read-allowlist.md),
   [DEC-0046](../decisions/DEC-0046-person-registry.md)).
2. Tier-1 validation runs on every PR touching `governance/` and
   blocks malformed configuration with explanations naming file, rule,
   and fix (per [DEC-0034](../decisions/DEC-0034-two-tier-validation.md),
   [DEC-0037](../decisions/DEC-0037-governance-as-code.md)).
3. `governance/` is Arbiter-owned: every change goes through the same
   PR gate as artifacts, and changing approval rights is itself a gated
   change (per [DEC-0037](../decisions/DEC-0037-governance-as-code.md)).
4. A deployment-time init command seeds the founding governance files —
   initial Arbiter and roles from deployment configuration — directly
   into the repository's initial history, before branch protection is
   first compiled (per [DEC-0140](../decisions/DEC-0140-seeded-governance-bootstrap.md)).

## Component Impact

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — supplies
its governance-config schema and validation contract sections.

## Out of Scope

Compiling this configuration onto the host
([ST-0013](ST-0013-policy-compilation-host-provisioning.md)); evaluating
it at gate time ([ST-0014](ST-0014-gate-policy-check.md)); identity and
auth provider linkage ([EP-0005](../epics/EP-0005-connectors-and-identity.md));
the Admin UI editor over these files ([EP-0006](../epics/EP-0006-refinement-web-ui.md),
which edits — never stores — governance state per
[DEC-0037](../decisions/DEC-0037-governance-as-code.md)).

## Notes for Implementers

Decision-rights vocabulary should align with the session engine's
proposal-capture behavior
([DEC-0054](../decisions/DEC-0054-guardrails-authority-limits.md)) — the
rights config this story defines is what
[EP-0002](../epics/EP-0002-refinement-session-agent.md)'s guardrails
consult.
