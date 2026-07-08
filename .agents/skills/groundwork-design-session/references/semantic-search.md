# Semantic Search & Decision-Recall Audit

Companion to [SKILL.md](../SKILL.md)'s search section: recipes and the
audit protocol. The tool is `scripts/groundwork_search.py`; its DuckDB
index (`.groundwork-search`) is a derived view — docs stay the source
of truth; the index reconciles itself with the docs on every run.

## Search recipes

| Question | Command |
|---|---|
| Have we discussed X before? (prior-art in conversations) | `search "X" --turns` |
| Which accepted decision covers Y? | `search "Y" --type decision --status accepted` |
| Is this idea already decided/current? | `search "..." --current` (excludes superseded/stale) |
| Anything like this inside one epic's subtree? | `search "..." --within EP-0001` |
| Is this new artifact a duplicate? | `similar <ID>` before minting |
| Raw similarity without link-boost | add `--no-boost` |

Hits on superseded decisions always carry a `superseded_by` redirect to
the accepted successor. Scores are rank-signals only — static
embeddings compress the range; never threshold on absolute score.

## The decision-recall audit (required stage step)

**When:** after drafting or materially amending any artifact, and again
at gate prep.

**Mechanics:**

1. `audit <ID-or-file> [--k 15]` — ranks accepted decisions relevant to
   the artifact but absent from its considered set (frontmatter cites +
   inline references, superseded-redirected), and emits a JSON judge
   packet including instructions.
2. Spawn a judge subagent with the packet (plus the artifact text if
   the judge lacks session context):
   - list ≤ 15 → **one** Opus-class judge; fork (inherits session
     context) when the facilitator runs on an Opus-class model,
     otherwise a fresh Opus agent fed the packet + artifact.
   - list > 15 → shard into batches of ~8 across Sonnet-class agents,
     each batch judged comparatively; a batch of one is forbidden —
     isolated relevance judges over-flag (acquiescence bias).
3. The judge reports at most 4 findings (ID, why relevant, where to
   consider it) or exactly "Nothing to add." plus the closest
   near-miss; contract gaps noticed en route are reported separately.
4. Address findings in the session before gating; "Nothing to add" is
   a valid outcome and worth a line in the session record.

**Limits (measured):** on a held-out benchmark (hide an artifact's
citations, ask where each ranks among non-cited decisions) a 15-item
list catches a missing decision ~60% of the time per stage — stages
compound. The audit catches *content-relevant* misses only: a rule-type
decision that governs document *structure* (e.g. seam graduation) has
no lexical footprint in a document that violates it and will not
surface — such decisions need explicit checklists at the stage they
govern (see the graduation review in
[refinement-process.md](refinement-process.md)). The two mechanisms
are complements; neither substitutes for the other.
