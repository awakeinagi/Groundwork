---
id: DEC-0147
type: decision
title: Approver and Arbiter queues are derived views with no persisted queue truth
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Queues are computed views: membership and order derived at read time
  from graph state (stale artifacts, open conflicts, open gate PRs),
  governance configuration (routing, delegations), and impact rank.
  No queue truth is persisted. Read-state and snooze preferences are
  UI-side per-user only.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T4-T5"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0039, DEC-0041, DEC-0131]
---

# DEC-0147: Derived Queue Views

## Context

The impact-ranked re-affirmation queues
(DEC-0041) and the
Arbiter conflict queue
(DEC-0039) needed a state
model.

## Decision

Queues are computed views: membership and order are derived at read
time from graph state (stale artifacts, open conflicts, open gate PRs),
governance configuration (routing, delegations), and impact rank. No
queue truth is persisted. Read-state and snooze niceties are UI-side
per-user preferences, never queue truth.

## Rationale

Nothing to drift from the graph it mirrors, rebuild-trivial under
DEC-0131's discipline, and
ordering updates the moment impact edges change.

## Alternatives Considered

- **Persisted queue entities** with lifecycle: enables assignment
  history but must answer the rebuild question for every field and can
  contradict the graph.
- **Derived membership + persisted annotation overlay**
  (claimed-by/snoozed-until): more moving parts, only warranted if
  claiming is a v1 requirement — it is not.

## Implications

Queue endpoints are pure queries over the Graph Index and governance
config; queue history for metrics comes from telemetry-grade events
(DEC-0144), not queue
state. Criteria land in
ST-0017.
