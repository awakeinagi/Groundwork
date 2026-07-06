---
id: SES-0007
type: session
title: EP-0004 refinement — branch overlays, freshness, engine spike, query tiers
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0004, EP-0001, EP-0002]
---

# SES-0007: EP-0004 Refinement Session

## Purpose

Refine [EP-0004](../epics/EP-0004-graph-index.md) (Cross-Reference Graph
Index) to gate-readiness: resolve the branch-awareness question inherited
from the fork-pull model (SES-0003), pin the consistency and query
contracts its now-refined consumers need, and dispose of the twice-deferred
engine choice.

## Transcript

**T1 — Sponsor.** Approved EP-0002. Proceed with the next epic.

**T2 — Agent.** Chose EP-0004 (all three impactors settled). Round 1:
(a) what the index sees under fork-pull (recommended main base + per-item-
branch overlays, view-parameterized queries, ref/status-tagged results);
(b) freshness (recommended session-synchronous overlay writes, async
global propagation, rebuild as the correctness definition); (c) engine
choice — decide vs spike (recommended spike, given self-hosted enterprise
ops burden per DEC-0050); (d) query API shape (recommended named traversals
plus one bounded generic primitive, no engine QL leakage).

**T3 — Sponsor.** (a) Main + branch overlays. (b) Session-sync,
global-async. (c) Spike (SP-0002). (d) Named traversals + bounded
primitive, **plus an advanced query API supporting something like GraphQL,
Cypher, etc.**

**T4 — Agent.** Proposed anchoring the advanced endpoint on a *standard*
language rather than raw engine passthrough, to preserve engine
swappability — openCypher (implemented by Neo4j, KuzuDB, Memgraph, Apache
AGE on Postgres) or GraphQL — making standard-QL support a hard SP-0002
criterion. Round 2: (a) which standard + guards (recommended openCypher,
read-only, depth/time/result guards); (b) index content depth (recommended
metadata-only graph, bodies stay in the store, text search deferred to the
retrieval layer); (c) operational verification of rebuild-correctness
(recommended scheduled rebuild-and-diff with atomic replacement).

**T5 — Sponsor.** (a) openCypher, read-only + guarded. (b) Metadata graph
only. (c) Scheduled rebuild-and-diff.

**T6 — Agent (synthesis).** Distilled DEC-0059–DEC-0064; created SP-0002
(engine selection spike — riding this epic's refinement per the item-branch
pattern, ratified with the epic's approval); rewrote EP-0004 and moved it
to `gated`.

## Decisions Produced

[DEC-0059](../decisions/DEC-0059-main-plus-branch-overlays.md),
[DEC-0060](../decisions/DEC-0060-session-sync-global-async.md),
[DEC-0061](../decisions/DEC-0061-engine-via-spike.md),
[DEC-0062](../decisions/DEC-0062-tiered-query-api.md),
[DEC-0063](../decisions/DEC-0063-metadata-only-graph.md),
[DEC-0064](../decisions/DEC-0064-scheduled-rebuild-diff.md)

## Conflicts Raised

None.
