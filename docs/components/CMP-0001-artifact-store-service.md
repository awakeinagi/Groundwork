---
id: CMP-0001
type: component
title: Artifact Store Service
status: draft
owner: eng-lead
created: 2026-07-06
context: canonical-store
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
cites: [DEC-0028, DEC-0029, DEC-0030, DEC-0031, DEC-0033, DEC-0034, DEC-0035]
---

# CMP-0001: Artifact Store Service

> Draft stub, birthed by [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md).
> Contract sections are filled in as the epic's stories (ST-0001–ST-0008)
> refine and settle their designs; this component is gate-eligible only
> when contract-complete per
> [DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md).

## Purpose

The single write authority over the Canonical Store: owns the fork-pull
git model, validates every write, allocates IDs, orchestrates item
branches, session worktrees, and gate PRs, executes typed mechanical
writes, and emits the change-event stream every other component consumes.

## Ubiquitous Language

Canonical Store, Artifact, Item Branch, Session Worktree, Mechanical
Write, Gate — per [CONTEXT.md](../../CONTEXT.md). No new terms introduced.

## Behavior Contract

Pending — itemized from ST-0002/ST-0003/ST-0004/ST-0005/ST-0006 as they
refine. Anchors already decided: single write authority
(per [DEC-0029](../decisions/DEC-0029-api-writes-git-reads.md)); branch/PR
lifecycle (per [DEC-0028](../decisions/DEC-0028-fork-pull-pr-gating.md));
worktree concurrency (per [DEC-0030](../decisions/DEC-0030-session-worktrees-branch-merge.md));
mechanical-write inexpressibility of content diffs
(per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md));
append-only sessions (per [DEC-0035](../decisions/DEC-0035-store-enforced-append-only-transcripts.md)).

## API Contract

Pending — OpenAPI authored in ST-0002; mechanical operations in ST-0006;
branch/PR operations in ST-0003 (per
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md),
language-neutral).

## Data Contract

Pending — owned state: the fork (git), ID counters (ST-0005 design),
event outbox (ST-0008 design). The repository remains rebuild-sufficient.

## Dependencies

- Code-host connector contract (EP-0005 / future CMP) — fork, branch, PR,
  review, protection operations; consumed per its capability manifest
  (per [DEC-0045](../decisions/DEC-0045-capability-declaring-connectors.md)).

## Acceptance & Test Expectations

Pending — assembled from story acceptance criteria; must include the
tier-2 check suite (ST-0007) passing against this repo's bootstrap corpus.

## Out of Scope

Gate policy logic (Governance engine); graph queries (Graph Index);
retrieval (Memory layer); any UI.
