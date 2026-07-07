---
name: groundwork-design-session
description: Run a Groundwork design session — refine raw product/business ideas into gated, provenance-linked design documentation (Business Goals → Epics → Stories/Spikes → contract-complete Component Docs) through structured grilling interviews. Use this whenever the user wants to start designing a new system or feature, asks to be grilled or interviewed about an idea, wants to turn vague requirements into implementable specs, mentions Groundwork, design docs, business goals, epics, refinement sessions, or asks to continue/resume design work in a project that has a docs/ artifact tree (BG-/EP-/ST-/DEC- files). Also use it to bootstrap the Groundwork documentation structure in a new or existing repo.
---

# Design Session (Groundwork)

Groundwork is a documentation-first design method: an agent interviews
stakeholders in structured **refinement sessions**, distills their answers
into **Decision records**, and grows a gated artifact tree — Business Goals
→ Epics → Stories/Spikes → **contract-complete Component Docs** an
implementation team (human or agent swarm) can build in parallel. Every
artifact traces to the business intent that motivated it, and every
contract line cites the decision (and conversation) behind it.

You are the facilitator. The user is the stakeholder/sponsor and, usually,
the approver at every gate.

## Step 0 — Assess the project state (always do this first)

Run the bundled status tool from the project root:

```bash
python3 <skill-dir>/scripts/status_report.py .
```

It reports artifact counts by type/status, open items, the refinement
frontier, and a recommended mode. Verify its recommendation yourself:

| Observation | Mode |
|---|---|
| No `docs/` artifact tree and no Groundwork `AGENTS.md` marker | **1 — Bootstrap**, then continue into Mode 2 |
| Structure exists but no approved Business Goal (`BG-*`) | **2 — Begin the design** |
| At least one approved Business Goal exists | **3 — Continue the design** |

If the directory contains an unrelated existing project (code, docs), the
artifact tree lives alongside it — Groundwork manages `docs/`, `CONTEXT.md`,
`AGENTS.md`, and `tools/check_links.py` and touches nothing else. Confirm
with the user before bootstrapping into a non-empty repo.

Before doing any Mode 2 or Mode 3 work, read
[references/groundwork-system.md](references/groundwork-system.md) (the
artifact model and rules) and
[references/refinement-process.md](references/refinement-process.md) (how
to run sessions and gates). Templates for every artifact type are in
[references/templates.md](references/templates.md).

## Mode 1 — Bootstrap a new Groundwork project

1. Create the skeleton (only what's missing):
   ```
   CONTEXT.md          ← glossary seed (template in references/templates.md)
   AGENTS.md           ← copy assets/AGENTS.md from this skill, verbatim
   tools/check_links.py← copy scripts/check_links.py from this skill
   docs/{goals,epics,stories,spikes,components,sessions,decisions,
         conflicts,change-proposals,consolidations}/   (.gitkeep in each)
   ```
   If the repo already has an `AGENTS.md` or `CLAUDE.md`, don't overwrite —
   append the Groundwork section from the asset instead.
2. If not a git repo, `git init`. Docs being versioned is load-bearing:
   history is the audit trail and IDs are never reused even after deletes.
3. Run `python3 tools/check_links.py` (should pass trivially), commit:
   `"Bootstrap Groundwork documentation structure"`.
4. Proceed directly into Mode 2 — an empty structure has no value until
   the first idea enters refinement. Ask the user for their idea(s) if they
   haven't volunteered one.

The `AGENTS.md` you install is deliberately self-sufficient: it lets any
future agent work in the project correctly *without this skill loaded*.
Keep it in sync if the project's conventions evolve.

## Mode 2 — Begin the design (inception)

Read [references/refinement-process.md](references/refinement-process.md)
in full before starting — it defines the grilling method, session records,
decision distillation, and gates. The short version of the flow:

1. **Ask for the idea.** Get the raw brief in the sponsor's own words —
   problem, who hurts, why now. Don't refine yet; capture it.
2. **Run the inception grilling session.** Dependency-ordered clarifying
   questions, 3–4 per round, each with a recommended answer listed first.
   Challenge vague terms and record them in `CONTEXT.md` as they resolve.
3. **Record `SES-0001`** (turn-numbered transcript) and distill the
   decisions into `DEC-` records, confirming each with the user in plain
   language before marking it accepted.
4. **Draft `BG-0001`** (Business Goal) from the session; set it `gated`
   and ask the user to approve. On approval, record `approved-by`/
   `approved-on` and commit.
5. **Derive draft Epics** from the approved goal, with `impacts`/
   `impacted-by` edges between them, then refine each epic through its own
   session — highest-impact epics first.

Always run `python3 tools/check_links.py` before every commit; commit at
least once per session and once per approval.

## Mode 3 — Continue an existing design

1. Read the status report plus `CONTEXT.md`, the Business Goal(s), and the
   frontier artifacts it lists. Do **not** re-litigate accepted decisions —
   read them and build on them. If something seems wrong, raise it as a
   new session topic; a new decision may supersede an old one, but history
   is never rewritten.
2. Pick the next work item by pipeline order and impact:
   - `gated` artifacts → present to the user for approval first.
   - `stale` artifacts → walk the user through re-affirmation (see the
     staleness section of the process reference).
   - Open conflicts (`CFL-*` not resolved) → these block their artifacts;
     run the mediation/escalation flow.
   - Approved artifacts with no derived work → derive the next layer
     (goal→epics, epic→stories/spikes, stories→component contracts).
   - Among sibling candidates, refine the one whose `impacted-by` list is
     already settled and whose `impacts` list is longest — its decisions
     constrain the most other items.
3. Run the refinement session(s) for the chosen item exactly as in Mode 2:
   session record → confirmed decisions → artifact update → `gated` →
   user approval → commit.
4. The design is *done* when every Component Doc is contract-complete and
   approved: an implementer holding the doc plus its dependencies'
   contracts can build and test the component without asking anyone
   anything. Drive toward that; it is the deliverable the whole process
   exists to produce.

## The local graph index (LadybugDB)

The skill bundles a queryable graph view of the artifact tree —
`scripts/groundwork_graph.py`, an embedded LadybugDB (openCypher) built
from frontmatter links plus Design Element headings. Run it via `uv`,
which installs `ladybug<1.0` into a temporary managed venv from the
script's inline metadata (requires `uv` on PATH):

```bash
uv run <skill-dir>/scripts/groundwork_graph.py --root <project> build
uv run <skill-dir>/scripts/groundwork_graph.py --root <project> <command>
```

Use it whenever a question is really a graph traversal:

| Moment in the process | Command |
|---|---|
| Before superseding a decision or amending an approved artifact — who goes stale? | `impact <ID>` |
| Session prep: why does this artifact exist, on which decisions? | `trace <ID>` |
| Periodic audit: dangling refs, citations of superseded DECs, uncited decisions, frontier | `gaps` |
| Choosing what to refine next among siblings | `order [type]` |
| Element inventory across components (seam-graduation candidates) | `elements [etype]` |
| Percent-complete estimate — design % per story/epic/goal | `progress` |
| Anything else | `query "<openCypher>"` — schema + recipe cookbook in [references/graph-queries.md](references/graph-queries.md) |

Discipline: the graph is a **derived view** — docs stay the source of
truth. After editing artifacts, `sync <file-or-ID>...` (or rebuild:
`build` is cheap). The DB file `.groundwork-graph` is disposable; keep
it gitignored. Graph mutations via `query` are for what-if exploration
only, never a substitute for editing docs.

## Invariants (never break these, in any mode)

- **Checker before commit.** `python3 tools/check_links.py` must pass.
- **Provenance.** Sessions are append-only once closed; accepted decisions
  are immutable (supersede, don't edit); every contract line and
  acceptance criterion cites a `DEC-`.
- **Gates.** Nothing derives from an unapproved parent; approval is the
  user's explicit call, recorded in frontmatter.
- **IDs.** Sequential per prefix, never reused. Check existing files (all
  of `docs/`) for the max before allocating.
- **Glossary.** Use `CONTEXT.md` terms exactly; resolve new or drifting
  terms there the moment they crystallize.

## Reference map

| Need | Read |
|---|---|
| Artifact types, frontmatter, links, statuses, integrity rules | [references/groundwork-system.md](references/groundwork-system.md) |
| How to grill, record sessions, distill decisions, run gates, handle conflicts/staleness, per-stage playbooks | [references/refinement-process.md](references/refinement-process.md) |
| Copy-paste templates for every artifact + CONTEXT.md/README seeds | [references/templates.md](references/templates.md) |
| Graph-index schema, command reference, openCypher recipe cookbook | [references/graph-queries.md](references/graph-queries.md) |
| The standing instructions installed into projects | [assets/AGENTS.md](assets/AGENTS.md) |
