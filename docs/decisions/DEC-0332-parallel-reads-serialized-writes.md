---
id: DEC-0332
type: decision
title: Librarian concurrency — parallel read spawns, serialized write tasks
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T10-T11"
overview: >-
  Callers may fan out read/search/graph librarian tasks in parallel
  freely — no shared-state hazard, and cheap parallel gathering (e.g.
  overviews for a gate packet) is a real win. Write-task librarians
  are serialized: at most one at a time, caller-enforced. The hazard
  is concrete: typed creates allocate sequential IDs and several
  operations do reciprocity bookkeeping across files; two concurrent
  writers could collide on both. This matches the project's existing
  parallel-agent discipline (no whole-tree operations in parallel
  same-tree subagents) and the single-writer reality of the corpus.
  Whether the write API additionally takes a repository lock as
  defense-in-depth is build territory under the DEC-0322/DEC-0334
  loop — the caller-level rule stands regardless, so correctness
  never rests on the lock alone.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0324, DEC-0313, DEC-0322]
---

# DEC-0332: Parallel Reads, Serialized Writes

## Context

With every artifact interaction a librarian spawn (DEC-0325), callers
will want fan-outs. Typed creates allocate sequential IDs and
reciprocity bookkeeping touches multiple files — parallel writers can
collide.

## Decision

Read-only librarian tasks (reads, searches, graph queries) may run in
parallel without limit. Write-task librarians are serialized: a
caller runs at most one at a time and waits for its result before
dispatching the next.

## Rationale

Reads are hazard-free and parallel gathering is where fan-out pays.
Serializing writes at the caller keeps correctness independent of any
API-level locking, which remains an open build choice.

## Alternatives Considered

- **Fully serialized** — forfeits cheap read fan-outs for no safety
  gain; rejected.
- **API-locked, caller-free** — puts an unscoped hard requirement on
  the skill build and makes correctness invisible to callers;
  rejected as the primary mechanism (allowed as defense-in-depth).

## Implications

The AGENTS.md instruction and the librarian definition both state the
rule. The build loop decides whether the API also locks.
