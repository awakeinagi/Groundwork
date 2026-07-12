<!-- groundwork-project: managed by the Groundwork design method -->
# Agent Instructions — Groundwork Design Project

This repository's design documentation is managed with **Groundwork**: a
documentation-first method that refines raw business ideas into gated,
provenance-linked design artifacts, ending in contract-complete Component
Docs an implementation team can build from in parallel. These instructions
are self-sufficient — follow them even if no Groundwork skill/tooling is
loaded.

## The artifact tree

```
CONTEXT.md            glossary (ubiquitous language) — use its terms EXACTLY
tools/check_links.py  graph integrity checker — must pass before every commit
governance/           governance-as-code: people/roles/domains/gate-policies
                      .yaml — who may approve what (solo default: the one
                      operator holds all roles)
docs/
├── goals/       BG-*   Business Goals (root of all traceability)
├── epics/       EP-*   Epics derived from approved goals
├── stories/     ST-*   Stories (acceptance criteria cite decisions)
├── spikes/      SP-*   Research questions (findings become decisions)
├── components/  CMP-*  Contract-complete component specs (the deliverable)
├── sessions/    SES-*  Refinement conversation records (append-only)
├── decisions/   DEC-*  Distilled decisions (the unit of provenance)
├── conflicts/   CFL-*  Contradictory-request records (blocking)
├── change-proposals/ CP-*   Out-of-band + unauthorized-attempt capture
├── ideas/       IDEA-* Raw pre-classification idea captures (work queue)
└── consolidations/   CON-* Derived context summaries (never citable)
```

Pipeline: Idea → Sessions → Business Goal → Epics → Stories/Spikes →
Component Docs. Every stage transition passes a **human approval gate**.

## How agents touch artifacts — the artifact-librarian mandate

**All agents must use the `artifact-librarian` agent to interact with
artifacts, unless the `artifact-interact` skill has been manually
loaded (DEC-0325, DEC-0326, DEC-0327).** Reads, searches, graph
queries, and writes alike: spawn the `artifact-librarian` project
agent (`.claude/agents/artifact-librarian.md`) with a task-level
intent — its Sonnet model and effort are pinned in the agent's
frontmatter, which is authoritative (DEC-0329, DEC-0348); do not pass
a spawn-time model param. It executes the operations through the `artifact-interact`
skill's guardrailed CLI — the sole sanctioned write path (DEC-0312) —
and returns a distilled result (verbatim content on request). Do not
Read/Edit/Write `docs/` artifact files yourself, and do not load
`artifact-interact` because context seems to call for it — the skill
is explicit-load-only. "Manually loaded" means the operator loaded it
by name, or your own agent definition explicitly charters it
(DEC-0328: `overview-writer` and `system-architect` hold such
charters). Read-only librarian tasks may run in parallel; never run
two write-task librarians concurrently (DEC-0332). The librarian never
commits — git stays with you (DEC-0333).

## The no-arbitrary-builds guard (DEC-0335, DEC-0345)

**Nothing is built in this project without a written design presented
to and approved by a human — however simple.** The build-side sibling
of the no-semantic-change-outside-a-session rule: build intent enters
through intake the moment it is uttered (restate → design → approval →
build). The design includes its **test plan** — which tests will run
and what outcome counts as proper function; approval covers both
(DEC-0345). Mechanical floor: only changes that cannot alter runtime
behavior or any contract surface (comments, whitespace, invisible
renames) pass without ceremony; **configuration is never mechanical**
— tool lists, models, permissions, settings, dependencies are semantic
by definition; when in doubt, it's semantic. Before any tooling or
technology decision, survey the option space and document it — a web
search of official docs recorded in the session suffices for small
option spaces; open questions get a Spike (DEC-0337). Alongside
provenance, **grounding through contracts** is first-class (DEC-0336):
everything living in the project carries a written statement of what
it does, what it touches, and how it is configured — before it exists;
the sizing yardstick is the minimum documentation needed to reconcile
a change against original intent.

## Non-negotiable rules

1. **Run the full integrity checker before every commit** (a librarian
   check task; `python3 tools/check_links.py` if you are chartered).
   Never commit red.
2. **Gates.** Never derive downstream work from a parent whose `status`
   is not `approved`. Approval is a human's explicit call; record it as
   `status: approved` + `approved-by:` + `approved-on:` in frontmatter,
   in its own commit.
3. **Immutability.** Closed sessions (`status: closed`) and accepted
   decisions (`status: accepted`) are never edited. New conversation = a
   new `SES-`. Changed mind = a new `DEC-` with `supersedes:` set — then
   mark every artifact citing the old decision `status: stale` and have
   the approver re-affirm or re-refine each. Two sanctioned exceptions,
   neither of which triggers staleness or re-gating: (a)
   reference-formatting edits (converting between reference notations,
   repairing a reference after a rename); (b) cross-reference
   enrichment — adding bare-ID mentions, `cites:` entries, or link
   entries that surface *already-existing* relationships, never
   creating new ones. In closed sessions, enrichment goes in a dated
   `### Post-Close Enrichment` subsection appended at the bottom of
   the Transcript section; transcript turns are never edited.
4. **IDs.** `PREFIX-nnnn`, sequential per prefix, **never reused** (even
   after deletion). Scan all of `docs/` for the current max before
   allocating. Filename = `ID-kebab-slug.md`.
5. **Provenance.** Every acceptance criterion and every contract item in
   a Component Doc ends with a citation `(per DEC-nnnn)` — bare IDs,
   comma-separated when several apply. A claim no decision
   supports means more refinement is needed — never invent a citation.
   Decisions carry `source-span: "SES-nnnn @ Tx-Ty"` pointing at
   transcript turns that actually support them. On goals, epics,
   stories, spikes, and components, `cites:` and body prose stay
   synchronized in both directions: every cited DEC appears in the
   prose, and every DEC the prose references is in `cites:` (or a
   frontmatter link). `cites:` IS the considered set.
6. **Typed links only** in frontmatter `links:` — `derives-from`,
   `satisfies`, `depends-on`, `conflicts-with`, `supersedes`,
   `relates-to`, `impacts`, `impacted-by` (the last two: same-type,
   reciprocal on both endpoints). Decision citations go in top-level
   `cites:`. In body prose, cross-references to artifacts are **bare
   IDs** (`DEC-0152`, `CMP-0009`) — an inline markdown link targeting
   an artifact file fails the checker, and every bare ID must resolve
   to an existing artifact. Links are still used for non-artifact
   files (CONTEXT.md, specs, code) and URLs. Frontmatter stays bare
   IDs and remains what tools read. Humans browse the rendered,
   navigable docs via `python3 tools/serve_docs.py` →
   `docs/human_docs.html`. Edges also carry prose obligations, checked
   before every commit: a goal/epic's body references every artifact
   deriving from it — update the parent's Derived Work in the same
   edit that creates the child; an artifact with an `impacts` edge
   explains each impact in its own body — the impactor explains, the
   impactee stays silent; a session's body references every
   `relates-to` target.
7. **Glossary.** When a new or ambiguous term comes up, resolve it in
   `CONTEXT.md` immediately and use it exactly thereafter.
8. **Conflicts block.** Artifacts linked to an unresolved `CFL-` cannot
   pass gates and nothing derives from them until the conflict resolves
   via an accepted decision.
9. **Component Docs are element-first.** A CMP's contracts live under
   `## Design Elements`: each element is declared `### <Name> (<type>)`
   with `<type>` from the closed set `entity | value | service | event |
   protocol`, directly followed by a mandated `Implements:` line naming
   ≥1 story by bare ID whose implementation the element handles,
   and carries element-scoped contract items (`<Name>.B-1` behavior,
   `.A-1` API, `.D-1` data). Implements references must agree with each
   story's Component Impact; a CMP cannot gate while a story naming it
   has no referencing element; amending or superseding an approved story
   stales every CMP whose elements implement it (element-scoped impact). Types mandate contract kinds
   (entity ⇒ behavior+data, API only if boundary-exposed; value ⇒ data;
   service ⇒ API+behavior; event ⇒ schema+delivery semantics; protocol ⇒
   API+conformance). API request/response schemas resolve inline or to a
   declared value/event element. Cross-element guarantees go in
   `## Component Invariants` (`C-n`); stack commitments in
   `## Implementation Guidance` as decision-cited Constraints (`IG-n`),
   with advisory Notes never load-bearing. An element consumed by more
   than one CMP graduates to its own CMP with `component-type:` set.
10. **Overviews.** Every artifact carries a frontmatter `overview:` —
    self-sufficient plain prose, max 250 words, bare IDs allowed (all
    must resolve), no markdown (per DEC-0284, DEC-0286; presence, cap,
    and resolution checker-enforced per DEC-0287). It is derived,
    non-normative content: never citable as provenance, body wins on
    conflict, freely regenerable — adding or refreshing one on a
    closed session or accepted decision violates no immutability rule
    (per DEC-0285). Any edit that changes an artifact's meaning
    updates its overview in the same edit; gate prep confirms
    faithfulness (per DEC-0288).

## How design changes are made — change intake

**No semantic change to this corpus is made outside a recorded session
(DEC-0252). Hard rule, no waiver — including for users with full
authority.** Discussion that changes nothing may stay off the record;
the moment a change is instructed, run intake:

1. **First mention → todo list (DEC-0256, DEC-0410).** Create a
   minimal tracked list — *restate intention; confirm alignment; start
   session?* — in whichever task/todo tool the harness exposes (e.g.
   TodoWrite or the Task tools TaskCreate/TaskUpdate; a visible
   in-conversation checklist only when none exists), expanding it to
   the confirmed path's steps once aligned.
2. **Restate & align (DEC-0255).** Restate the proposal's *intention*;
   clarifications loop back to restatement until the proposer confirms.
   Agent-noticed issues enter the same way, roles reversed: you
   propose, the user disposes (DEC-0257).
3. **Authority check (DEC-0262, DEC-0264).** Resolve the operator
   against `governance/people.yaml` (git identity, honor system) and
   the gate policies. An instruction outside the instructor's rights
   does not proceed — capture it verbatim as a CP
   (`source: unauthorized-attempt`) awaiting the authority holder(s).
4. **Pick the path:**
   - **Mechanical fix (DEC-0253)** — zero semantic content (typo,
     formatting, reference repair; no contract line, decision text,
     status, approval field, or link semantics touched): commit
     directly, descriptive message, no session. When in doubt, it's
     semantic.
   - **Idea capture (DEC-0258)** — record IDEA artifact(s) verbatim in
     a micro-session (zero linked decisions is valid).
   - **Expedited session (DEC-0254)** — small semantic change: one
     round; every integrity step still runs.
   - **Full grilling session** — everything else: focused clarifying
     questions in small rounds, recommended answer stated first; read
     existing decisions before asking; never re-litigate what an
     accepted DEC settles.
5. **The session record opens at the verbatim proposal** (T1), then
   the restatement and alignment loop (DEC-0255). Locate affected
   artifacts up front (search + graph) and keep a working hypothesis
   of the change's artifact level(s) through grilling (DEC-0266).
6. **Mid-session tangents — focus-artifact test (DEC-0260):** changes
   the artifact under refinement → grill now; needs a different
   artifact → park as an IDEA (level unclear) or deferred ST/SP (level
   clear, DEC-0259) and continue. Cross-reference spawned Ideas from
   the session. Captured Ideas are the work queue (DEC-0261): each
   take-up is its own new intake session, never an extension.
7. **Modifying approved artifacts:** superseding DECs, the staleness
   walk, and re-affirmation all complete inside the session
   (DEC-0267) — never leave the corpus mid-cascade.
8. **Close:** detailed summary + inspired-ideas check; play back the
   decisions you intend to record and get confirmation before marking
   them accepted; record the session (`SES-`, turn-numbered,
   faithful), decisions (`DEC-`, one each), and artifact updates
   together; `status: gated` → ask the approver. Checker, then commit
   (session + decisions + artifacts in one commit; approval as its own
   commit: `Approve <ID> (<approver>, <date>)`).

Multi-party governance without the Groundwork application is
git-mediated and asynchronous (DEC-0265): each authority holder
triages/ratifies/approves in their own sessions; committee gates
collect sign-offs across commits/PRs. Local identity is declared and
honor-system (DEC-0264) — provenance, not tamper-proofing.

## Status lifecycle

`draft → in-refinement → gated → approved` (then `stale ⇄ approved`, or
`superseded`/`archived`). Sessions: `open → closed`. Decisions:
`proposed → accepted → superseded`. Conflicts: `open → mediating →
escalated → resolved`. Change proposals: triage `pending → mechanical |
session | rejected`. Ideas: `captured → taken-up | declined` — never
gated, never release-labeled; take-up runs intake as a new session.

Stories, epics, and spikes may additionally be `deferred` — out of the
current release, carrying a `release:` label (a SemVer prefix declared
in the Business Goal's `**Releases:**` list, or `backlog`). Deferred
items pass no gates and derive nothing; revival re-enters at `draft`.
Deferral and revival each cite a decision. Revival conditions are armed
as triggers in `docs/TRIGGERS.md` (`## TRG-nnnn (armed|fired|retired)`
entries; decision-cited subscriber lines, one condition serving many
items). Firing cites a decision and revives ALL subscribers; a revived
item is unsubscribed from every other armed trigger in the same change
(armed triggers may only subscribe deferred items — checker-enforced),
and emptied triggers retire. Review armed triggers when scope or
releases are re-planned.

## Reading discipline — progressive disclosure

Read overviews first; ask for bodies only when the overview says the
detail is there (per DEC-0284, DEC-0289). Librarian read tasks serve
concise reads without whole-file loads: overviews (batch, or
type/status filtered), outlines, sections, design elements, contract
items, transcript turn spans, glossary terms, and citers. Search and
graph results already include overviews (per DEC-0290) — a hit list is
often enough to answer without any file read. Ask for verbatim
sections only when fidelity matters (gate review, transcript work).

## Orientation for a fresh agent

1. Read `CONTEXT.md`, then the Business Goal(s) in `docs/goals/` —
   overviews first, bodies as needed (see Reading discipline).
2. Check state: artifacts with `status: gated` await approval; `stale`
   await re-affirmation; open `CFL-` files block their artifacts; approved
   artifacts with an empty "Derived Work" section are the frontier.
3. The design is done when every Component Doc is `approved` and
   contract-complete: an implementer could build and test it from the doc
   plus its dependencies' contracts alone, without asking anyone anything.
