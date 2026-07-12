---
name: groundwork-design-session
description: Run a Groundwork design session — refine raw product/business ideas into gated, provenance-linked design documentation (Business Goals → Epics → Stories/Spikes → contract-complete Component Docs) through structured grilling interviews. Use this whenever the user wants to start designing a new system or feature, asks to be grilled or interviewed about an idea, wants to turn vague requirements into implementable specs, mentions Groundwork, design docs, business goals, epics, refinement sessions, or asks to continue/resume design work in a project that has a docs/ artifact tree (BG-/EP-/ST-/DEC- files). MANDATORY in any Groundwork-managed project (docs/ artifact tree or Groundwork AGENTS.md marker): invoke it the moment the user proposes ANY change — idea, enhancement, fix, however small — so the change-intake protocol runs; semantic changes there are not made outside a session. Also use it to bootstrap the Groundwork documentation structure in a new or existing repo.
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

The interview technique underneath every session is **grilling** — see
[references/grilling.md](references/grilling.md) for the core technique
and its origin. Grilling sessions run as many rounds as it takes for the
artifact under refinement to be clearly, unambiguously specified; there is
no round limit. It is always better to ask one more question than to stop
short and leave a gap — err on the side of more questions, not fewer.

**Change intake (all modes).** Whenever change intent surfaces in a
Groundwork project — the user mentions an idea/enhancement/fix, or you
notice an issue yourself — run the intake protocol
(§Change intake of
[references/refinement-process.md](references/refinement-process.md)):
todo list at first mention (DEC-0256) → restate & align (DEC-0255) →
path pick (mechanical fix DEC-0253 / idea capture DEC-0258 / expedited
DEC-0254 / full session) → record opens at the verbatim proposal. No
semantic change to the corpus ever happens outside a session (DEC-0252,
hard rule); unauthorized attempts are captured as CPs per the
governance config in `governance/` (DEC-0262, DEC-0263).

**Build intake (DEC-0335, DEC-0345 — the no-arbitrary-builds guard).**
Build intent runs the same intake: nothing executable is built without
a written design presented and approved, however simple — and the
design includes its test plan (which tests validate proper function;
approval covers both). Configuration is never mechanical; when in
doubt, semantic. Tooling/technology decisions require a documented
option survey first, sized to the decision (DEC-0337 — a web search of
official docs recorded in the session suffices for small option
spaces; open questions get a Spike). Grounding through contracts is
first-class (DEC-0336): the sizing yardstick for all of this is the
minimum documentation needed to reconcile the change against original
intent. Approval of an action covers the intent, not the design — an
approved "fix it now" still gets its design presented before
implementation.

## How you touch artifacts: the artifact-librarian (DEC-0324..DEC-0334)

You do not read, search, or write corpus artifacts yourself — **no
agent does** (DEC-0325, facilitator included). Every artifact
interaction is delegated to the `artifact-librarian` project agent:
spawn it with a **task-level intent** — its Sonnet model and effort
are pinned in its frontmatter, which is authoritative (DEC-0329,
DEC-0348); do not pass a spawn-time model param. It plans and executes
the reads/searches/graph queries/typed writes via the
`artifact-interact` skill (its chartered toolbelt, DEC-0327) and
returns a distilled result; ask for verbatim sections when fidelity
matters (gate review, transcript work).

- **Read/search/graph tasks may fan out in parallel, and write tasks
  may too — the gw write path serializes at the apply moment with
  transactional rollback (DEC-0391; DEC-0411..DEC-0416, verified
  SES-0079). Keep order-dependent writes in one batch or explicitly
  sequenced, and at most one turn-appending task per session
  (DEC-0392).**
- The librarian refuses invariant-violating writes and reports the
  sanctioned alternative (DEC-0330); surface refusals to the
  stakeholder like any other tension — never instruct it to work
  around one.
- Git stays with you: the librarian validates and runs the checker on
  request, but you commit (DEC-0333).
- Direct use of `artifact-interact` is sanctioned only under the
  manual-load escape hatch (DEC-0327): the operator explicitly loads
  it, or an agent definition charters it. If that applies to you, its
  SKILL.md documents the CLI.

Intent examples you'll use constantly:

- "Status report for <root>: counts, open items, frontier, recommended mode."
- "Locate-first for this proposal: search + graph-trace <topic>; return the affected artifacts with overviews."
- "Record these N decisions (payloads follow) with cites and links; then consistency sweep + terms on the new IDs."
- "Run the recall audit on <ID>; return the candidate list and judge packet."
- "Close SES-nnnn: append these turns, set status closed, update overview; run the full checker and report."

## Step 0 — Assess the project state (always do this first)

1. **Verify the interaction surface is installed** (DEC-0326):
   the `artifact-librarian` agent (`.claude/agents/artifact-librarian.md`)
   and the `artifact-interact` skill (project-local
   `.claude/skills/artifact-interact/`, or user scope) must both exist.
   If either is missing, stop and tell the user to run
   `install.sh --project <repo>` from a Groundwork repo's
   `.claude/skills/artifact-interact/` directory. Do not improvise
   direct artifact access instead.
2. **Task the librarian with a status report.** Verify its recommended
   mode yourself:

| Observation | Mode |
|---|---|
| No `docs/` artifact tree and no Groundwork `AGENTS.md` marker | **1 — Bootstrap**, then continue into Mode 2 |
| Structure exists but no approved Business Goal (`BG-*`) | **2 — Begin the design** |
| At least one approved Business Goal exists | **3 — Continue the design** |

If the directory contains an unrelated existing project (code, docs), the
artifact tree lives alongside it — Groundwork manages `docs/`, `CONTEXT.md`,
`AGENTS.md`, and `tools/` (`check_links.py`, `serve_docs.py`) and touches
nothing else. Confirm with the user before bootstrapping into a non-empty
repo.

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
   tools/check_links.py← from the artifact-interact skill's scripts/
   tools/serve_docs.py ← from the artifact-interact skill's scripts/
   docs/human_docs.html← from the artifact-interact skill's assets/
   governance/         ← seed people/roles/domains/gate-policies.yaml with
                         solo god-mode defaults (templates.md §Governance
                         seeds; DEC-0263 — all roles → the operator)
   docs/{goals,epics,stories,spikes,components,sessions,decisions,
         conflicts,change-proposals,ideas,consolidations}/  (.gitkeep each)
   ```
   `docs/human_docs.html` + `serve_docs.py` are the human browsing
   surface: rendered markdown, clickable bare-ID cross-references,
   backlinks, and (when served via `serve_docs.py`) semantic + graph
   search over the corpus. Cross-references in artifact bodies are bare
   IDs; this viewer, not stored links, carries human navigation.
   If the repo already has an `AGENTS.md` or `CLAUDE.md`, don't overwrite —
   append the Groundwork section from the asset instead.
2. **Install the interaction surface and its mandate** (DEC-0326):
   install the `artifact-interact` skill + `artifact-librarian` agent
   into the project (`install.sh --project`), and ensure the standing
   instruction is present in BOTH surfaces — the AGENTS.md Groundwork
   section (the asset carries it) AND project-level memory: *all agents
   must use the artifact-librarian to interact with artifacts, unless
   the artifact-interact skill has been manually loaded.* On every
   later invocation, re-verify both; re-add if missing. This applies to
   every project using the Groundwork paradigm, not just the Groundwork
   application repo.
3. If not a git repo, `git init`. Docs being versioned is load-bearing:
   history is the audit trail and IDs are never reused even after deletes.
4. Have the librarian run the full checker (should pass trivially), commit:
   `"Bootstrap Groundwork documentation structure"`.
5. Proceed directly into Mode 2 — an empty structure has no value until
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
   Use [references/goal-grilling-questions.md](references/goal-grilling-questions.md)
   as the question bank — organized by BG section and tagged by confidence
   tier (High/Medium/Low); don't skip Low-tier questions, just expect
   their answers to be provisional. Challenge vague terms and record them
   in `CONTEXT.md` as they resolve. Keep going as many rounds as it takes
   to reach shared understanding — there is no round cap.
3. **Record `SES-0001`** (turn-numbered transcript) and distill the
   decisions into `DEC-` records — all via librarian write tasks —
   confirming each with the user in plain language before marking it
   accepted.
4. **Draft `BG-0001`** (Business Goal) from the session; set it `gated`
   and ask the user to approve. On approval, record `approved-by`/
   `approved-on` and commit.
5. **Derive draft Epics** from the approved goal, with `impacts`/
   `impacted-by` edges between them, then refine each epic through its own
   session — highest-impact epics first.

Always have the librarian run the full checker before every commit;
commit at least once per session and once per approval.

## Mode 3 — Continue an existing design

1. Read the status report plus `CONTEXT.md`, the Business Goal(s), and the
   frontier artifacts it lists (librarian read tasks; overviews first).
   Do **not** re-litigate accepted decisions —
   read them and build on them. If something seems wrong, raise it as a
   new session topic; a new decision may supersede an old one, but history
   is never rewritten.
2. Pick the next work item by pipeline order and impact:
   - `gated` artifacts → present to the user for approval first.
   - `stale` artifacts → walk the user through re-affirmation (see the
     staleness section of the process reference).
   - Open conflicts (`CFL-*` not resolved) → these block their artifacts;
     run the mediation/escalation flow.
   - Untriaged change proposals and captured Ideas (`IDEA-*`) → triage
     CPs; offer intake sessions for queued Ideas (DEC-0261) — the
     project's brain-dump work queue.
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

## Semantic search & the decision-recall audit

Route **meaning-shaped** questions to librarian search tasks (have we
discussed X? which decision covers Y? is this new artifact a
duplicate?) and **structure-shaped** questions to librarian graph tasks
(what depends on X? why does Y exist?). Read tasks parallelize freely
(DEC-0391).

**Decision-recall audit (required stage step).** After drafting or
materially amending an artifact — and again at gate prep — task the
librarian with the recall audit on the artifact: it returns the ranked
candidates and the judge context packet. Spawn a judge subagent with
that packet, always on a **Sonnet 5** model (fork when the facilitator
itself runs Sonnet 5, else a fresh Sonnet 5 agent — spawn it with the
Agent tool's **`model: sonnet` override set explicitly**; a subagent
with no `model` inherits the facilitator's model, which when the
facilitator is Opus-class is exactly the forbidden case) — one judge
for lists ≤15; shard into ~8-candidate batches beyond that; **never
one candidate per agent** (isolated relevance judges over-flag).
Address findings in-session; "Nothing to add" is a valid outcome worth
recording. The audit catches *content-relevant* decisions missing from
context; *rule-type* decisions (e.g. seam graduation) still need their
explicit checklists — the two mechanisms are complements. Recipes in
[references/semantic-search.md](references/semantic-search.md).

**Consistency checks at distillation (required — DEC-0157/DEC-0158).**
Immediately after recording new decisions, include in the librarian's
write task: run the consistency `sweep` and `terms` checks over the new
DEC IDs. `sweep` catches partial supersessions: an accepted decision
named in `relates-to`/`supersedes` gets its ratified citers listed for
consistency review (narrowing decisions never fire the staleness walk).
`terms` catches contract-identifier overlap: ratified artifacts sharing
rare code-span identifiers (containment-matched), flagging unlinked
co-occurrences. Review hits in-session; record dispositions like audit
findings. Protocol details in
[references/refinement-process.md](references/refinement-process.md)
§Distilling decisions.

**Cross-sibling coupling check at epic and story derivation (required —
DEC-0196, DEC-0199).** Right after a draft sibling set's impact edges
are drawn, and before refining any of them in depth, task the librarian
with the coupling check over the sibling IDs (story/spike sets under an
epic use the story variant; the default groups epics by goal). It flags
*mutual* (bidirectional) `impacts` coupling between siblings — a signal
the split may have followed a technical-layer seam instead of a real
one — while treating one-directional fan-out as informational only
(expected from foundational/substrate epics; not a finding). Seam
catalogs and split-vs-merge guidance in
[references/epic-slicing-seams.md](references/epic-slicing-seams.md) and
[references/story-slicing-seams.md](references/story-slicing-seams.md).

**System-architect consultation at EP/ST/CMP (required —
DEC-0292..DEC-0296).** Epic, story/spike, and component refinement
sessions open with an **advisor** consultation of the
`system-architect` project agent (`.claude/agents/system-architect.md`,
knowledge in the `system-architecture-bp` skill), and their gate prep
includes a **reviewer** consultation — at component gate prep it runs
before the DEC-0136 graduation review. Discretionary at BG level and at
method-level sessions (DEC-0323). Every consultation is a dual-instance
debate (record-grounded vs best-practice-independent, ≤2 rebuttal
rounds; model and effort pinned in the agent's frontmatter, DEC-0348); the verdict
is a proposal the stakeholder ratifies, recorded as attributed
transcript turns with inline dispositions. The system-architect holds
an explicit read-only corpus charter (DEC-0328). Protocol details in
[references/refinement-process.md](references/refinement-process.md)
§System-architect consultation.

## Concise reads & progressive disclosure

Every artifact carries a frontmatter `overview:` (max 250 words,
derived/non-normative — body wins; DEC-0284..DEC-0288). Librarian read
tasks serve overviews, outlines, sections, elements, contract items,
turn spans, glossary terms, and citers — ask for overviews first, and
for bodies only when an overview says the detail is there. Search and
graph results include overviews by default (DEC-0290) — a hit list
frequently answers the question with zero file reads. When an edit
changes an artifact's meaning, the same write task updates its
overview (DEC-0288).

## The graph index (structure-shaped questions)

The librarian's graph tasks answer traversals:

| Moment in the process | Ask the librarian for |
|---|---|
| Before superseding a decision or amending an approved artifact — who goes stale? | impact walk of the ID |
| Session prep: why does this artifact exist, on which decisions? | provenance trace of the ID |
| Periodic audit: dangling refs, citations of superseded DECs, uncited decisions, frontier, reciprocity gaps | the gaps report |
| Choosing what to refine next among siblings | refinement order (optionally by type) |
| Element inventory across components (seam-graduation candidates) | the elements inventory |
| Percent-complete estimate | design % per story/epic/goal |
| Anything else | an openCypher query — recipes in [references/graph-queries.md](references/graph-queries.md) |

The graph is a **derived view** — docs stay the source of truth; the
librarian keeps it synced around its own writes. Graph mutations are
for what-if exploration only, never a substitute for editing docs.

## Invariants (never break these, in any mode)

- **Checker before commit.** The full integrity suite must pass (a
  librarian check task) before every commit.
- **Provenance.** Sessions are append-only once closed; accepted decisions
  are immutable (supersede, don't edit); every contract line and
  acceptance criterion cites a `DEC-`.
- **Gates.** Nothing derives from an unapproved parent; approval is the
  user's explicit call, recorded in frontmatter.
- **IDs.** Sequential per prefix, never reused — the write API allocates;
  never hand-pick an ID.
- **Glossary.** Use `CONTEXT.md` terms exactly; resolve new or drifting
  terms there the moment they crystallize.
- **Delegation (DEC-0325).** All artifact interaction goes through the
  artifact-librarian; direct tooling only under the DEC-0327 escape
  hatch.

## Reference map

| Need | Read |
|---|---|
| Artifact types, frontmatter, links, statuses, integrity rules | [references/groundwork-system.md](references/groundwork-system.md) |
| The grilling technique itself, and its origin | [references/grilling.md](references/grilling.md) |
| How to grill, record sessions, distill decisions, run gates, handle conflicts/staleness, per-stage playbooks | [references/refinement-process.md](references/refinement-process.md) |
| The curated goal-level (BG) question bank, tiered by confidence/volatility | [references/goal-grilling-questions.md](references/goal-grilling-questions.md) |
| Epic-slicing seams, vertical-vs-horizontal slicing, split-vs-merge guidance, the coupling check | [references/epic-slicing-seams.md](references/epic-slicing-seams.md) |
| Story-slicing seams, INVEST-grounded split-vs-merge guidance, the coupling check | [references/story-slicing-seams.md](references/story-slicing-seams.md) |
| Copy-paste templates for every artifact + CONTEXT.md/README seeds | [references/templates.md](references/templates.md) |
| Graph-index schema, openCypher recipe cookbook | [references/graph-queries.md](references/graph-queries.md) |
| Recall-audit recipes and judge protocol | [references/semantic-search.md](references/semantic-search.md) |
| The standing instructions installed into projects | [assets/AGENTS.md](assets/AGENTS.md) |
| The artifact toolbelt itself (librarian/chartered use only) | the `artifact-interact` skill |
