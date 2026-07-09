# Graph Queries — the LadybugDB Graph Index

How to use `scripts/groundwork_graph.py`: the schema, the commands, and
a cookbook of openCypher recipes for questions the canned commands don't
cover. LadybugDB is an embedded, Kuzu-lineage graph database
(openCypher dialect; engine docs at https://docs.ladybugdb.com/).

## Running it

The script carries PEP 723 inline metadata; `uv run` resolves
`ladybug<1.0` + `pyyaml` into a temporary managed venv automatically:

```bash
uv run <skill-dir>/scripts/groundwork_graph.py --root <project> build
uv run <skill-dir>/scripts/groundwork_graph.py --root <project> <command> [args]
```

- The database is a single file, default `<root>/.groundwork-graph`.
  Keep it **gitignored** — it is derived and disposable.
- **Docs are the source of truth.** The graph reflects them; it never
  drives them. After editing artifacts: `sync <file-or-ID>...`, or just
  `build` (a full rebuild takes seconds and also clears stale
  placeholders that `sync` cannot).
- `--json` on any command emits rows as JSON for scripting.
- Every command has `--help`, with detailed descriptions.

## Schema

Node tables:

| Table | Properties | Notes |
|---|---|---|
| `Artifact` | `id` (PK), `type`, `title`, `status`, `owner`, `created`, `path`, `context`, `component_type`, `source_span` | One per doc under `docs/` (specs excluded). Unresolved link targets appear as placeholders with `type = status = 'missing'`. `source_span` is only set on decisions; `context`/`component_type` only on components. |
| `Element` | `key` (PK, `"CMP-nnnn/Name"`), `name`, `etype`, `component`, `complete` | One per `### <Name> (<type>)` heading in a component's Design Elements section. `complete` is the design-complete heuristic: own contract items present, no "Pending" in the block. |

Relationship tables — **direction matters**:

| Table | Direction | Meaning |
|---|---|---|
| `DERIVES {ltype}` | child → parent | `derives-from` and `satisfies` frontmatter links; `ltype` says which. Ancestry = follow outgoing; descendants = follow incoming. |
| `IMPACTS` | X → Y | refining X shapes decisions in Y (`impacted-by` is the same edge read backward; it is stored once, in the `impacts` direction). |
| `DEPENDS_ON` | consumer → dependency | contract consumption between components. |
| `CITES` | artifact → decision | provenance. |
| `SUPERSEDES` | new → old | decision/artifact replacement chains. |
| `CONFLICTS_WITH` | artifact → conflict | open-conflict linkage. |
| `RELATES_TO` | as written | weak association (sessions ↔ artifacts, etc.). |
| `HAS_ELEMENT` | component → element | design-element ownership. |
| `MENTIONS` | referrer → referent | a bare artifact ID in the referrer's body prose (code spans/fenced blocks excluded; DEC-0251). The edge records only that a reference exists — bodies stay in the docs. |
| `IMPLEMENTS` | element → story | the element's `Implements:` line — which stories' implementation it handles. |

## Command reference

| Command | Use at this moment |
|---|---|
| `build` | after many edits, after a `git pull`, or when in doubt |
| `sync PATH\|ID ...` | after editing/deleting a few artifacts |
| `impact ID` | **before** superseding a decision or amending an approved artifact — shows derivation descendants (the would-be-stale set), citers, impact-edge neighbors, dependents |
| `trace ID` | session prep — ancestors to the goal + cited decisions with source-spans |
| `gaps` | periodic audit — unresolved refs, citations of superseded DECs, uncited accepted DECs, approved goals/epics with nothing derived, sessions with no decisions, approved stories no element implements, plus the reciprocity audits (DEC-0251): derived children unlisted in the parent body, dead/missing cites, impact edges without impactor prose, session relates-to targets unmentioned |
| `order [type]` | choosing the next sibling to refine (ready + largest impact fan-out first) |
| `elements [etype]` | reviewing the element model; spotting seam-graduation candidates; per-element implemented stories + completeness |
| `progress` | the design percent-complete rollup — story → epic → goal over `IMPLEMENTS` edges; uncovered stories read 0% |
| `stats` | orientation in an unfamiliar project |
| `query CYPHER` | everything below |

## Cypher cookbook

Prose references with no frontmatter relationship (candidate missing
edges — the inverse of the `gaps` reciprocity audits):

```cypher
MATCH (a:Artifact)-[:MENTIONS]->(b:Artifact)
WHERE NOT EXISTS { MATCH (a)-[:CITES|RELATES_TO|DERIVES|SUPERSEDES|
                            IMPACTS|DEPENDS_ON|CONFLICTS_WITH]->(b) }
  AND NOT EXISTS { MATCH (b)-[:DERIVES|IMPACTS]->(a) }
RETURN a.id, b.id ORDER BY a.id, b.id
```

Approval queue — everything gated, oldest first:

```cypher
MATCH (a:Artifact {status: 'gated'})
RETURN a.id, a.type, a.created, a.title ORDER BY a.created, a.id
```

All stale artifacts (need re-affirmation before anything derives):

```cypher
MATCH (a:Artifact {status: 'stale'}) RETURN a.id, a.type, a.title
```

Every artifact resting on a given decision (pre-supersession check —
same as `impact DEC-0011`, citers view):

```cypher
MATCH (x:Artifact)-[:CITES]->(d:Artifact {id: 'DEC-0011'})
RETURN x.id, x.type, x.status, x.title ORDER BY x.id
```

Decisions produced by a session, with what they shaped:

```cypher
MATCH (d:Artifact {type: 'decision'})-[:DERIVES]->(s:Artifact {id: 'SES-0012'})
OPTIONAL MATCH (x:Artifact)-[:CITES]->(d)
RETURN d.id, d.status, collect(DISTINCT x.id) AS shaped ORDER BY d.id
```

Supersession chain for a decision (what replaced what):

```cypher
MATCH (new:Artifact)-[:SUPERSEDES*1..5]->(old:Artifact {id: 'DEC-0083'})
RETURN new.id, new.status, new.title
```

Approved descendants of an artifact — the exact set the staleness walk
would mark:

```cypher
MATCH (d:Artifact)-[:DERIVES*1..20]->(a:Artifact {id: 'EP-0001'})
WHERE d.status = 'approved'
RETURN DISTINCT d.id, d.type, d.title
```

Which components consume a component's contracts (amend with care):

```cypher
MATCH (c:Artifact)-[:DEPENDS_ON]->(dep:Artifact {id: 'CMP-0002'})
RETURN c.id, c.status, c.title
```

Hop count from any artifact to its goal (path length = derivation depth):

```cypher
MATCH p = (a:Artifact {id: 'ST-0004'})-[:DERIVES*1..20]->(g:Artifact {type: 'business-goal'})
RETURN g.id, length(p) AS hops ORDER BY hops LIMIT 1
```

Components and their element counts by type (model shape at a glance):

```cypher
MATCH (c:Artifact {type: 'component'})-[:HAS_ELEMENT]->(e:Element)
RETURN c.id, e.etype, count(e) AS n ORDER BY c.id, e.etype
```

Which elements implement a story — the story's design surface (what must
be contract-complete before the story counts as designed):

```cypher
MATCH (e:Element)-[:IMPLEMENTS]->(s:Artifact {id: 'ST-0002'})
RETURN e.component, e.name, e.etype, e.complete
```

Stories a component's elements implement, with coverage counts (compare
against the stories whose Component Impact names the CMP):

```cypher
MATCH (c:Artifact {id: 'CMP-0001'})-[:HAS_ELEMENT]->(e:Element)-[:IMPLEMENTS]->(s:Artifact)
RETURN s.id, s.status, collect(e.name) AS by_elements ORDER BY s.id
```

CMPs that would go stale if a story changed (the DEC-0096 walk):

```cypher
MATCH (e:Element)-[:IMPLEMENTS]->(s:Artifact {id: 'ST-0008'})
MATCH (c:Artifact)-[:HAS_ELEMENT]->(e)
RETURN DISTINCT c.id, c.status, collect(e.name) AS via_elements
```

Sessions that touched a given artifact (its conversational history):

```cypher
MATCH (s:Artifact {type: 'session'})-[:RELATES_TO]->(a:Artifact {id: 'CMP-0001'})
RETURN s.id, s.created, s.title ORDER BY s.created
```

Decisions with no surviving influence — accepted, cited by nothing,
superseding nothing (candidates for a fold-in or a review):

```cypher
MATCH (d:Artifact {type: 'decision', status: 'accepted'})
OPTIONAL MATCH (x:Artifact)-[:CITES]->(d)
OPTIONAL MATCH (d)-[:SUPERSEDES]->(o:Artifact)
WITH d, count(x) AS citers, count(o) AS sups
WHERE citers = 0 AND sups = 0
RETURN d.id, d.title
```

## What-if exploration

To ask "what would the impact be **if** X impacted Y" without touching
real state, work on a copy of the derived DB:

```bash
cp .groundwork-graph /tmp/whatif.db
uv run .../groundwork_graph.py --db /tmp/whatif.db query \
  "MATCH (a:Artifact {id:'EP-0002'}), (b:Artifact {id:'EP-0006'})
   MERGE (a)-[:IMPACTS]->(b)"
uv run .../groundwork_graph.py --db /tmp/whatif.db impact EP-0002
```

Never mutate the real DB to represent hypothetical design: rebuild
(`build`) resets everything to what the docs say.

## Dialect notes (Kuzu-lineage quirks)

- Variable-length patterns need explicit bounds: `-[:DERIVES*1..20]->`.
- `collect()` over zero rows returns NULL, not `[]` — guard consumers.
- `MERGE ... ON CREATE SET ...` is supported; plain `SET` after `MERGE`
  applies on both create and match.
- The `query` command takes one literal Cypher string; there is no CLI
  parameter binding — interpolate values into the string.
