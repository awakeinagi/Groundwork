---
id: ST-0017
type: story
title: Re-affirmation flow and impact-ranked approver queues
status: gated
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0003, ST-0012, ST-0016]
  impacts: [ST-0018]
  impacted-by: [ST-0012, ST-0016]
  relates-to: [SP-0001]
cites: [DEC-0028, DEC-0033, DEC-0038, DEC-0041, DEC-0075, DEC-0146, DEC-0147]
---

# ST-0017: Re-affirmation Flow and Approver Queues

## Summary

How staleness clears: the lightweight re-affirmation PR, escalation to
full re-refinement on rejection, and the impact-ranked derived queues
that tell each approver what to clear first.

## Acceptance Criteria

1. A stale artifact gets a re-affirmation PR — a reuse of its item
   branch and gate-PR machinery — carrying the upstream diff and the
   impact report in its description; approval clears the mark via the
   `clear-stale` mechanical operation
   (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
   [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md),
   [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md),
   [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)).
2. Rejecting a re-affirmation routes the artifact to full
   re-refinement — a new session — and the rejection is recorded in the
   governance event log
   (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)).
3. Each approver's work queue is a derived view — computed at read time
   from stale artifacts, open gate PRs, governance routing, and
   delegations — ordered by impact rank, with human judgment over raw
   impact edges serving until [SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md)'s
   algorithm lands
   (per [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md),
   [DEC-0147](../decisions/DEC-0147-derived-queue-views.md)).
4. Queue notifications are batched per user preference and delivered
   through the notification center
   (per [DEC-0041](../decisions/DEC-0041-impact-ranked-reaffirmation-queue.md),
   [DEC-0075](../decisions/DEC-0075-notification-center-connectors.md)).

## Component Impact

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — supplies
its re-affirmation and queue contract sections.

## Out of Scope

The ranking algorithm itself — open research in
[SP-0001](../spikes/SP-0001-impact-ranking-algorithm.md); queue and
review UI surfaces ([EP-0006](../epics/EP-0006-refinement-web-ui.md),
including the semantic gate diff rendering per
[DEC-0076](../decisions/DEC-0076-semantic-gate-diff.md)); notification
delivery adapters ([EP-0005](../epics/EP-0005-connectors-and-identity.md)).
