---
id: IDEA-0056
type: idea
title: "Multi-repo topology: code-only repositories linked back to the governing Groundwork docs repo"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  Captures the stakeholder's SES-0082 T35 clarification of DEC-0426
  (one application instance per Groundwork docs repo): the software
  built from a Groundwork corpus may itself be spread across
  multiple code-only repositories, distinct from the single governed
  docs repo, with that code needing to link back to the Groundwork
  repo. Open territory: the code-to-corpus linkage mechanism,
  provenance from implementation to contracts/decisions, whether
  paradigm enforcement (checker, gates, governance) reaches into
  code-only repos, how Handoff Manifests and implementation-facing
  artifacts relate to multi-repo layouts, and the application
  instance's scope when one corpus governs several code repos.
  Flagged as a more complicated scenario for a future session — on
  the radar, not scheduled.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0426]
---

# IDEA-0056: Multi-repo topology: code-only repositories linked back to the governing Groundwork docs repo

## The Idea

The stakeholder's raw idea, captured at SES-0082 T35: the software built from a Groundwork corpus may be spread across multiple "code-only" repositories, while the Groundwork docs repo remains the single governed corpus (one application instance per docs repo, DEC-0426). That code would need to be linked back to the Groundwork repo. Open territory for a future session includes: the linkage mechanism from code repos back to the corpus (provenance from implementation to contracts and decisions), whether/how the paradigm's enforcement (checker, gates, governance) reaches into code-only repos, how the Handoff Manifest and implementation-facing artifacts relate to multi-repo layouts, and what the application instance's scope is when one corpus governs several code repos. Flagged by the stakeholder as a more complicated scenario to flesh out in a future session — on the radar, not scheduled.

## Spark Context

Raised mid-session at SES-0082 T35, as a clarification to the just-ratified DEC-0426 (team topology: one application instance per repository). The stakeholder wanted the "one instance per repository" reading pinned to the Groundwork docs repo specifically, and flagged the multi-repo (code-only repos linked back to the docs repo) scenario as out of scope for this session but worth tracking.

## Disposition

Pending.
