---
id: SES-0007
type: session
title: EP-0004 refinement — branch overlays, freshness, engine spike, query tiers
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Refined EP-0004 (Cross-Reference Graph Index) to gate-readiness,
  resolving branch-awareness under fork-pull model and query contracts.
  Settled: main base plus per-item-branch overlays with
  view-parameterized queries, session-synchronous overlay writes and
  asynchronous global propagation with scheduled rebuild-and-diff
  verification, metadata-only graph (bodies stay in store), named
  traversals plus bounded generic query primitive, plus openCypher for
  advanced queries (read-only with depth/time/result guards). Engine
  choice deferred to SP-0002 spike. Produced 6 decisions.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0004, EP-0001, EP-0002]
---

# SES-0007: EP-0004 Refinement Session

## Purpose

Refine EP-0004 (Cross-Reference Graph
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

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  the refined EP-0004 depends on EP-0001 (Artifact Store & Format
  Engine) — the index overlays EP-0001's fork-pull item branches, and
  per the T4–T5 index-content decision artifact bodies stay in
  EP-0001's store.

## Decisions Produced

DEC-0059,
DEC-0060,
DEC-0061,
DEC-0062,
DEC-0063,
DEC-0064

## Conflicts Raised

None.
