---
id: DEC-0004
type: decision
title: Pipeline handles new goals only, with existing-context awareness
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
overview: >-
  Only goals entering the pipeline fresh are refined through Groundwork.
  Agent must nevertheless be aware of existing systems, backlog, and
  codebases as context when refining new goals — to detect overlap and
  conflict. Retroactive ingestion of existing backlog is low-leverage;
  awareness of existing work captures most conflict-detection value without
  that cost. Implies context feeds required and conflict detection must
  compare new goals against artifacts never through Groundwork.
source-span: "SES-0001 @ T2-T3"
links:
  derives-from: [SES-0001]
---

# DEC-0004: Pipeline handles new goals only, with existing-context awareness

## Context

Groundwork could be purely greenfield, could retroactively ingest the
existing Jira backlog and legacy docs into its hierarchy, or could handle
only new goals while staying aware of the existing world.

## Decision

Only goals entering the pipeline fresh are refined through Groundwork. The
agent must nevertheless be aware of existing systems, backlog, and codebases
as context when refining new goals — to detect overlap and conflict.

## Rationale

Retroactive normalization of an existing backlog is a large, low-leverage
project; awareness (not ownership) of existing work captures most of the
conflict-detection value.

## Alternatives Considered

- **Pure greenfield**: ignores real overlap/conflict with in-flight work.
- **Ingest existing backlog**: significant ingestion and normalization work
  before any new-goal value ships.

## Implications

Context feeds are required (DEC-0016);
conflict detection must compare new goals against artifacts that never went
through Groundwork.
