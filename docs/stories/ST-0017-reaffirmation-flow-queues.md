---
id: ST-0017
type: story
title: Re-affirmation flow and impact-ranked approver queues
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
owner: eng-lead
created: 2026-07-08
overview: >-
  How staleness clears: lightweight re-affirmation PR reusing the item
  branch and gate machinery, carrying upstream diff and impact report.
  Approval clears via `clear-stale` operation; rejection escalates to
  full re-refinement session. Impact-ranked queues guide each approver's
  priority ordering.
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0003, ST-0012, ST-0016]
  impacts: [ST-0018]
  impacted-by: [ST-0012, ST-0016, ST-0032]
  relates-to: [SP-0001]
cites: [DEC-0028, DEC-0033, DEC-0038, DEC-0041, DEC-0075, DEC-0076, DEC-0146,
        DEC-0147]
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
   (per DEC-0038,
   DEC-0028,
   DEC-0146,
   DEC-0033).
2. Rejecting a re-affirmation routes the artifact to full
   re-refinement — a new session — and the rejection is recorded in the
   governance event log (ST-0018)
   (per DEC-0038).
3. Each approver's work queue is a derived view — computed at read time
   from stale artifacts, open gate PRs, governance routing, and
   delegations — ordered by impact rank, with human judgment over raw
   impact edges serving until SP-0001's
   algorithm lands
   (per DEC-0041,
   DEC-0147).
4. Queue notifications are batched per user preference and delivered
   through the notification center
   (per DEC-0041,
   DEC-0075).

## Component Impact

CMP-0004 — supplies
its re-affirmation and queue contract sections.

## Out of Scope

The ranking algorithm itself — open research in
SP-0001; queue and
review UI surfaces (EP-0006,
including the semantic gate diff rendering per
DEC-0076); notification
delivery adapters (EP-0005).
