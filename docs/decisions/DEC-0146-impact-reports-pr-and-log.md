---
id: DEC-0146
type: decision
title: Impact reports live in re-affirmation PR descriptions and the event log, never in the repo
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Impact reports from staleness sweeps are written into re-affirmation
  PR descriptions (visible to reviewers) and the governance event log
  (for dashboards). Reports are never committed to the canonical repo
  since they are derived analysis, regenerable from the graph at any
  commit.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T4-T5"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0038, DEC-0076, DEC-0144, DEC-0372]
---

# DEC-0146: Impact Reports in PR and Log, Not Repo

## Context

DEC-0038 attaches an
impact report to every staleness sweep and
DEC-0076 renders it at gate review —
but where the report durably lives was undefined.

## Decision

The gate engine writes each sweep's impact report into the affected
re-affirmation PRs' descriptions (host-side, visible to reviewers per
DEC-0076) and stores it in the
governance event log for dashboards. Reports are never committed to the
canonical repo.

## Rationale

Reports are derived analysis, regenerable from the graph at any commit;
committing them would put rebuildable clutter in the canonical store,
and every sweep's commits would themselves emit ChangeEvents.

## Alternatives Considered

- **Committed repo artifact per sweep**: fully in-truth and citable,
  but derived content in the canonical store that goes stale the moment
  the graph moves.
- **App database only**: host-side reviewers — the audience
  DEC-0076 explicitly serves — would
  see nothing in the PR.

## Implications

Log-stored reports are telemetry-grade
(DEC-0144) — the
provenance-grade record of a re-affirmation is the PR itself. Criteria
land in ST-0016
and ST-0017.
