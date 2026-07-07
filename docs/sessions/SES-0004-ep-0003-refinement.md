---
id: SES-0004
type: session
title: EP-0003 refinement — policy enforcement, governance config, staleness ops
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0003, EP-0001]
---

# SES-0004: [EP-0003](../epics/EP-0003-governance-and-gate-engine.md) Refinement Session

## Purpose

Refine [EP-0003](../epics/EP-0003-governance-and-gate-engine.md)
(Governance & Gate Engine) to gate-readiness, reconciling it with the
fork-pull PR-gating model settled in
[SES-0003](SES-0003-ep-0001-refinement.md): how gate policies are enforced
on the code host, where governance configuration lives, staleness and
conflict operations, delegation, queue ordering, and reporting.

## Transcript

**T1 — Sponsor.** Approved [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md). Proceed to the next epic, agent's
choice.

**T2 — Agent.** Recorded [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) approval. Chose [EP-0003](../epics/EP-0003-governance-and-gate-engine.md) by the interim
impact-ranking logic ([DEC-0027](../decisions/DEC-0027-impact-ranked-refinement-order.md)):
its only impactor ([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)) is settled and it impacts four siblings,
including [EP-0005](../epics/EP-0005-connectors-and-identity.md) whose refinement needs [EP-0003](../epics/EP-0003-governance-and-gate-engine.md)'s decisions. Round 1:
(a) policy enforcement given hosts can't express domain-conditional
approvers (recommended host base + service-computed `gate-policy` status
check); (b) governance config home (recommended governance-as-code in the
canonical repo); (c) staleness spread/blocking/clearing (recommended
subtree mark + re-affirmation); (d) conflict escalation operations
(recommended Arbiter queue + blocking check, no auto-timeout).

**T3 — Sponsor.** (a) Host base + service check. (b) Governance-as-code.
(c) Subtree mark + re-affirm to clear. (d) Option 1 (queue + blocking
check, no auto-timeout) as the default, but allow election of option 2
(timeout to a configured default resolution) on a per-artifact basis.

**T4 — Agent.** Round 2: (a) approver unavailability (recommended
role-pool default + explicit time-bounded delegation in governance
config); (b) re-affirmation queue ordering after staleness sweeps
(recommended impact-ranked queue in the UI — the [SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md) algorithm ordering
refinement also orders re-affirmation); (c) reporting responsibility
(recommended [EP-0003](../epics/EP-0003-governance-and-gate-engine.md) emits a governance event log + metrics API, [EP-0006](../epics/EP-0006-refinement-web-ui.md)
renders dashboards).

**T5 — Sponsor.** All three as recommended.

**T6 — Agent (synthesis).** Distilled [DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md)–[DEC-0042](../decisions/DEC-0042-governance-reporting-split.md), rewrote [EP-0003](../epics/EP-0003-governance-and-gate-engine.md)
accordingly, and moved it to `gated` awaiting sponsor sign-off. Noted for
[EP-0005](../epics/EP-0005-connectors-and-identity.md)'s refinement: host review-semantics variance (Bitbucket vs GitHub)
now matters to gate compilation, and the connector must support team/
required-check administration.

## Decisions Produced

[DEC-0036](../decisions/DEC-0036-host-base-plus-service-gate-check.md),
[DEC-0037](../decisions/DEC-0037-governance-as-code.md),
[DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
[DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
[DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
[DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md),
[DEC-0042](../decisions/DEC-0042-governance-reporting-split.md)

## Conflicts Raised

None.
