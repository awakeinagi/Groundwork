---
id: ST-0016
type: story
title: Staleness sweeps and impact analysis
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0006, ST-0008]
  impacts: [ST-0014, ST-0017, ST-0018]
cites: [DEC-0007, DEC-0033, DEC-0038, DEC-0096, DEC-0144, DEC-0145, DEC-0146]
---

# ST-0016: Staleness Sweeps and Impact Analysis

## Summary

The invalidation machinery: detecting that an approved artifact
changed, computing its derived subtree, marking it stale in one
mechanical sweep, and producing the impact report everything downstream
renders.

## Acceptance Criteria

1. On a ChangeEvent indicating a change to an approved artifact, the
   engine computes the affected set via Graph Index queries — the full
   derived subtree plus, for an amended or superseded story, every
   Component Doc with an element whose `Implements:` line references
   it — and marks every approved member stale in one mechanical sweep
   of `mark-stale` operations
   (per [DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md),
   [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
   [DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md),
   [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md),
   [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)).
2. Each sweep produces an impact report: what changed, the affected
   set including in-flight work (open PRs on affected artifacts), the
   specific referencing elements of any component doc staled over an
   Implements edge, and the approvers affected
   (per [DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md),
   [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md),
   [DEC-0096](../decisions/DEC-0096-implements-staleness-propagation.md)).
3. The report is written into affected re-affirmation PR descriptions
   and stored in the event log as telemetry; it is never committed to
   the canonical repo
   (per [DEC-0146](../decisions/DEC-0146-impact-reports-pr-and-log.md),
   [DEC-0144](../decisions/DEC-0144-two-grade-governance-event-log.md)).
4. Sweeps are idempotent under at-least-once event redelivery:
   re-processing the same ChangeEvent produces no duplicate marks or
   reports (per [DEC-0145](../decisions/DEC-0145-event-driven-check-recomputation.md)).
5. Stale state produced here is what blocks: descendants' `gate-policy`
   checks consume it and new derivation from stale artifacts is refused
   until cleared
   (per [DEC-0038](../decisions/DEC-0038-subtree-staleness-reaffirmation.md)).

## Component Impact

[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — supplies
its sweep and impact-analysis contract sections.

## Out of Scope

Clearing staleness — the re-affirmation flow
([ST-0017](ST-0017-reaffirmation-flow-queues.md)); the graph queries
consumed here ([EP-0004](../epics/EP-0004-graph-index.md) owns the
query contract); the `mark-stale` operations themselves
([ST-0006](ST-0006-typed-mechanical-writes.md) — this story is their
invoking side).
