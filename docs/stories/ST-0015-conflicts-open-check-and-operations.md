---
id: ST-0015
type: story
title: The conflicts-open check and Arbiter conflict operations
status: gated
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0003, ST-0012]
  impacts: [ST-0018]
  impacted-by: [ST-0012]
cites: [DEC-0033, DEC-0034, DEC-0039, DEC-0075, DEC-0143, DEC-0147]
---

# ST-0015: The `conflicts-open` Check and Conflict Operations

## Summary

The operational side of conflict governance: the blocking check that
keeps contested artifacts from merging, the Arbiter's queue, and the
electable timeout-to-default path with its System Decisions.

## Acceptance Criteria

1. The `conflicts-open` required check fails any gate PR whose
   artifact links an unresolved Conflict, and clears only when the
   conflict is resolved by a ratified Decision or explicit withdrawal;
   machine-verified auto-PRs (mechanical writes, System Decisions)
   remain governed by their validators, so recording system facts
   about a contested artifact is never wedged
   (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
   [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
2. Escalated Conflicts surface in the Arbiter's work queue — a derived
   view over open Conflict artifacts — with notifications delivered
   through the notification center
   (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
   [DEC-0147](../decisions/DEC-0147-derived-queue-views.md),
   [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).
3. No conflict resolves by timeout by default: aging conflicts escalate
   in visibility (reminders, dashboard prominence), never in state
   (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md)).
4. The per-artifact timeout-to-default election is expressible in
   artifact frontmatter and tier-1 validated, naming the period and the
   configured default rule
   (per [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
   [DEC-0034](../decisions/DEC-0034-two-tier-validation.md)).
5. When an elected timeout fires, the engine drafts the System Decision
   from the fixed template — citing the election and the default
   rule — and lands it through the auto-PR machinery gated by the
   template-conformance check; the conflict then resolves citing that
   Decision (per [DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md),
   [DEC-0039](../decisions/DEC-0039-conflict-escalation-operations.md),
   [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).

## Component Impact

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — supplies
its conflict-operations and `conflicts-open` contract sections.

## Out of Scope

Mediation content and intent discovery — the session agent mediates;
this story only enforces blocking
([EP-0002](../epics/EP-0002-refinement-session-agent.md), per
[DEC-0005](../decisions/DEC-0005-intent-first-mediation-then-escalation.md));
the conflict-resolution UI surfaces
([EP-0006](../epics/EP-0006-refinement-web-ui.md)).
