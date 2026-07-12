# Semantic Search & Decision-Recall Audit

Companion to [SKILL.md](../SKILL.md)'s search section: recipes and the
audit protocol. The tool is the `search` family of the artifact-interact
skill's unified CLI:

```bash
python3 .claude/skills/artifact-interact/scripts/gw.py --root <project> search <subcommand> [args]
```

Its DuckDB index (`.groundwork-search`) is a derived view — docs stay
the source of truth; the index reconciles itself with the docs on every
run.

> **Who runs these commands (DEC-0324..DEC-0327).** The commands below
> are executed by the `artifact-librarian` agent (or another agent that
> explicitly charters the artifact-interact skill per DEC-0327) — never
> by the facilitator directly. Facilitators pass the *intent* to the
> librarian ("have we discussed X?", "run the recall audit on ST-0004")
> rather than running commands themselves.

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

1. Task the librarian with the recall audit on the artifact (it runs
   `audit <ID-or-file> [--k 15] [--output PATH]`) — this ranks accepted
   decisions relevant to the artifact but absent from its considered
   set (frontmatter cites + inline references, superseded-redirected),
   and emits a JSON judge packet, which the librarian returns to you.
   The packet is self-sufficient (DEC-0405): it carries the audited
   artifact's id, title, overview, and full body, candidate overviews
   and similarity scores, and the judge instructions — no out-of-band
   artifact handoff is needed. Prefer `--output` so the packet never
   shares a stream with warnings or progress output.
2. Spawn a judge subagent with the packet, always on a **Sonnet 5**
   model — never Opus-class. The packet's instructions make the judge
   confirm `artifact.id` matches its assignment before judging (a
   mismatch is reported, not judged — catches orchestration-layer
   packet swaps, IDEA-0027):
   - list ≤ 15 → **one** Sonnet 5 judge; fork (inherits session
     context) when the facilitator itself runs Sonnet 5, otherwise a
     fresh Sonnet 5 agent fed the packet. **Pin the model
     explicitly**: on the Agent call pass `model: sonnet` — a fresh
     subagent given only a `subagent_type` (e.g. `general-purpose`) and
     no `model` override *inherits the facilitator's model*, so on an
     Opus-class facilitator the judge silently runs Opus unless you set
     it. Verify if unsure (the subagent transcript's turns should read
     `claude-sonnet-5`).
   - list > 15 → shard into batches of ~8 across Sonnet 5 agents, each
     batch judged comparatively; a batch of one is forbidden —
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
