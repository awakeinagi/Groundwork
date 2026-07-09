---
id: SES-0019
type: session
title: Semantic search for the skill tooling — DuckDB + vss, hybrid with the graph
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [DEC-0102, DEC-0106, EP-0004, EP-0007, SP-0002]
---

# SES-0019: Semantic Search for the Skill Tooling — DuckDB + vss, Hybrid with the Graph

## Purpose

The participant directed adding semantic search to the facilitation
skill's local tooling using DuckDB + the vss extension, citing
[blog.brunk.io/posts/similarity-search-with-duckdb](https://blog.brunk.io/posts/similarity-search-with-duckdb)
as the technical reference. Already settled going in:
DEC-0102 commits v1 to
embedded DuckDB for the app database and vector/semantic search — this
work dogfoods that decision, the same way the skill's LadybugDB graph
tool dogfoods the embedded graph choice (noted in
SES-0017 T2). `TRG-0003`
in the [trigger registry](../TRIGGERS.md) already watches for vector
search exceeding acceptable latency. The session ran two throwaway
POC investigations against this repository's real corpus before
decisions were confirmed.

## Transcript

**T1 — awakeinagi.** Add semantic search to the agent skill using
DuckDB + the vss extension; read the referenced blog post for details.
Directed that `duckdb` and `duckdb-extensions` be added as requirements
for the skill's script that will handle semantic search.

**T2 — awakeinagi.** Clarified the packaging intent: by installing
`duckdb-extensions`, the script shouldn't have to run `INSTALL vss`
inside DuckDB — only the `LOAD`.

**T3 — facilitator.** Read the blog post (BGE-M3 via FlagEmbedding,
`FLOAT[1024]` column, HNSW index; caveats: experimental HNSW
persistence with WAL-corruption risk, index only used inside a `top_k`
CTE). Verified the packaging empirically: bare `LOAD vss` fails; the
working offline set is **three** packages — `duckdb`,
`duckdb-extensions`, `duckdb-extension-vss` — with
`import_extension("vss")` then `LOAD vss`, no network `INSTALL`.
Opened the session, recapped
DEC-0102 as settled, and
grilled round 1:
(a) where the work lands (recommended skill tooling + decisions
recorded here as dogfood evidence); (b) embedding backend (recommended
model2vec static potion-base-8M over the blog's heavyweight BGE-M3 and
mid-weight sentence-transformers; API embeddings noted as breaking the
offline property); (c) corpus granularity (recommended section-level
chunks); (d) vss usage at ~10³-chunk scale (recommended vss loaded but
no persisted HNSW index — exact brute force, avoiding the experimental
persistence flag).

**T4 — awakeinagi.** Accepted (a) skill tooling + DECs here and (b)
model2vec. Upgraded (c) to **sections plus per-turn transcript rows**
for provenance-grade search. On (d): accepted no-persisted-HNSW and
amended it — "create a deferred spike for HNSW."

**T5 — facilitator.** Round 2: (a) tool shape (recommended a separate
`groundwork_search.py` with its own uv inline dependencies, keeping the
graph script lean); (b) index location (recommended a sibling
`.groundwork-search` DuckDB file, gitignored, derived-view discipline);
(c) freshness (recommended auto-refresh on every search via per-file
content hashes, so the index can never serve stale results); (d) output
and guidance (recommended cite-ready hits — artifact ID, section/turn,
status, score, snippet — plus a SKILL.md row distinguishing
meaning-shaped questions from structure-shaped graph queries).

**T6 — awakeinagi.** Accepted all four recommendations.

**T7 — facilitator.** Played back eight decisions covering the stack,
embeddings, corpus, no-HNSW-plus-spike, tool packaging, freshness, and
output/guidance.

**T8 — awakeinagi.** Interrupted confirmation: "Let's investigate with
a throwaway POC script how we can combine the semantic search with the
graph for maximum effectiveness."

**T9 — facilitator.** Built and ran POC 1 against the real corpus (147
docs → 922 chunks). Results: embedding 0.14 s total, queries ~35 ms
brute-force. Headline: for "which database engine stores the graph and
handles vector search," pure semantic search ranked superseded
DEC-0070 first
and never surfaced DEC-0102
(rank 10) — on a corpus that keeps superseded decisions forever,
semantic search alone actively misleads. One graph hop along
`SUPERSEDES` redirects stale hits to accepted successors. Graph-boosted
re-ranking (1-hop score propagation over cites/derives edges, 0.25
decay) promoted the correct artifact set
(EP-0004,
SES-0017,
SP-0002,
DEC-0102) and demoted
templated boilerplate sections that fooled pure similarity. Subtree scoping via `DERIVES*` worked. Inline provenance
expansion duplicated the graph tool's `trace` — delegated instead.
LadybugDB verified to open `read_only=True` against the live graph.
Revised the playback: search script needs `ladybug` in its
dependencies; output becomes two-tier (boosted artifacts + exact chunk
hits); a new hybrid-retrieval decision.

**T10 — awakeinagi.** Asked for the findings output to the chat, and:
"What are some ways we can combine the semantic search with the graph
search to improve the effectiveness of the agent?"

**T11 — facilitator.** Presented a ranked catalog: (1) current-truth
redirect; (2) graph-boosted ranking; (3) citation-candidate lookup
(`--type decision --status accepted`); (4) unlinked-neighbor audit
(high similarity, no graph path → duplicate/missing-edge/conflict
candidates); (5) prior-art recall over transcript turns; (6)
impact-analysis recall supplement; (7) trigger matching; (8)
glossary-drift detection; (9) seam-candidate clustering across CMPs.

**T12 — awakeinagi.** "Please investigate/test all of these options
and report back on the feasibility."

**T13 — facilitator.** Built and ran POC 2. Verdicts: citation filters
work (right accepted DEC at #1 in 2/3 tests); prior-art recall over
turns 3/3 (found the exact turn where clickable links were first
requested); `similar <ID>` supplement useful with tolerable noise.
Tested poorly: unlinked-neighbor audit (template-similarity noise
dominates; needs tuning — element-mediated links must count as
connected); trigger matching (missed the clearest concurrent-writer
paraphrase at 0.23 — and armed triggers already load into agent context
per DEC-0106); glossary
drift (flagged 14% of chunks, mostly false positives); seam clustering
(untestable — one CMP exists). Arrow bulk insert fixed POC 1's slow
load (25 s → 129 ms). Accidental discovery: the live `.groundwork-graph`
was stale (missing
SES-0018's decisions entirely),
meaning missing
`SUPERSEDES` redirects exactly where they matter most — the search tool
must detect graph staleness and warn. Recommended v1 = tested core +
citation filters + turns filter + `similar <ID>` + staleness warning;
rest to one deferred backlog story.

**T14 — awakeinagi.** (After asking for plain-chat summaries of the
results.) Agreed to both the v1 scope and the single backlog story.
Asked: can pre-filtering be applied to embedding results in DuckDB;
would filtering out stale docs have helped the noisy case; is metadata
needed on the records to allow it?

**T15 — facilitator.** Tested it: pre-filtering is a plain `WHERE`
clause applied before similarity ranking — exact and faster (32 ms vs
45 ms) because brute force has no index to bypass (contrast: `WHERE`
clauses silently bypass vss's HNSW index — another point for no-HNSW).
On the noisy query, `status NOT IN ('superseded','stale')` removed all
three superseded chunks and
DEC-0102 entered the
top-8 (rank 10 → 7).
No new metadata needed — artifact ID, type, and status are already
columns on every chunk row, kept current by auto-refresh. Nuance:
filtering complements but does not replace the redirect — superseded
text is often the best-matching text, and history queries need it. So:
default include-all + annotate + redirect; `--current` flag pre-filters
`superseded`/`stale`.

**T16 — awakeinagi.** "Approved. Let's also add new recipes in the
skill's cookbook reference for using these new capabilities."

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  the semantic search prototyped here at skill scale dogfoods the
  capability owned in the product by EP-0007 (Consolidation Memory
  Layer), the epic responsible for semantic search over artifact
  bodies.

## Decisions Produced

- DEC-0111 —
  semantic search joins the skill tooling on DuckDB + vss, pip-bundled
  extension, dogfooding
  DEC-0102
- DEC-0112 —
  embeddings via model2vec static (potion-base-8M)
- DEC-0113 —
  corpus: section chunks plus per-turn transcript rows, with metadata
  columns
- DEC-0114 — exact
  brute-force search; no persisted HNSW index; experimental persistence
  flag never set
- DEC-0115 —
  SP-0003 deferred spike
  for HNSW adoption, subscribed to `TRG-0003`
- DEC-0116 —
  separate `groundwork_search.py` and gitignored `.groundwork-search`
  index
- DEC-0117 — auto-refresh
  on search; graph-staleness warning
- DEC-0118 —
  two-tier cite-ready output; SKILL.md guidance and cookbook recipes
- DEC-0119 —
  hybrid retrieval semantics (redirect, boost, scoping, filters,
  `--current`, `similar`, dedupe, trace delegation)
- DEC-0120 —
  v1 scope cut; rejected/deferred capabilities captured in
  ST-0009

## Conflicts Raised

None.
