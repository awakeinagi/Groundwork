---
id: ST-0016
type: story
title: Staleness sweeps and impact analysis
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
owner: eng-lead
created: 2026-07-08
overview: >-
  Invalidation machinery: detecting approved artifact changes, computing
  their derived subtree, marking all approved members stale in one
  mechanical sweep, and producing impact reports captured in re-affirmation
  PRs and stored as telemetry. Sweeps are idempotent under at-least-once
  redelivery.
links:
  derives-from: [EP-0003]
  satisfies: [BG-0001]
  depends-on: [ST-0006, ST-0008]
  impacts: [ST-0014, ST-0017, ST-0018]
  impacted-by: [ST-0032]
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
   (per DEC-0007,
   DEC-0038,
   DEC-0096,
   DEC-0033,
   DEC-0145).
2. Each sweep produces an impact report: what changed, the affected
   set including in-flight work (open PRs on affected artifacts), the
   specific referencing elements of any component doc staled over an
   Implements edge, and the approvers affected
   (per DEC-0007,
   DEC-0038,
   DEC-0096).
3. The report is written into affected re-affirmation PR descriptions
   and stored in the event log (ST-0018) as telemetry; it is never
   committed to the canonical repo
   (per DEC-0146,
   DEC-0144).
4. Sweeps are idempotent under at-least-once event redelivery:
   re-processing the same ChangeEvent produces no duplicate marks or
   reports (per DEC-0145).
5. Stale state produced here is what blocks: descendants' `gate-policy`
   checks (ST-0014) consume it and new derivation from stale artifacts
   is refused until cleared
   (per DEC-0038).

## Component Impact

CMP-0004 — supplies
its sweep and impact-analysis contract sections.

## Out of Scope

Clearing staleness — the re-affirmation flow
(ST-0017); the graph queries
consumed here (EP-0004 owns the
query contract); the `mark-stale` operations themselves
(ST-0006 — this story is their
invoking side).
