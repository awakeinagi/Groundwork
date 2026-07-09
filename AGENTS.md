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
                      .yaml — who may approve what (per DEC-0037, DEC-0263;
                      solo default: the one operator holds all roles)
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

## Non-negotiable rules

1. **Run `python3 tools/check_links.py` before every commit.** Never
   commit red.
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
   repairing a reference after a rename) change no meaning and are
   permitted (per DEC-0091, applied by DEC-0243); (b) cross-reference
   enrichment — adding bare-ID mentions, `cites:` entries, or link
   entries that surface *already-existing* relationships, never
   creating new ones (per DEC-0248). In closed sessions, enrichment
   goes in a dated `### Post-Close Enrichment` subsection appended at
   the bottom of the Transcript section; transcript turns are never
   edited.
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
   synchronized in both directions (per DEC-0247): every cited DEC
   appears in the prose, and every DEC the prose references is in
   `cites:` (or a frontmatter link). `cites:` IS the considered set.
6. **Typed links only** in frontmatter `links:` — `derives-from`,
   `satisfies`, `depends-on`, `conflicts-with`, `supersedes`,
   `relates-to`, `impacts`, `impacted-by` (the last two: same-type,
   reciprocal on both endpoints). Decision citations go in top-level
   `cites:`. In body prose, cross-references to artifacts are **bare
   IDs** (`DEC-0152`, `CMP-0009`) — an inline markdown link targeting
   an artifact file fails the checker, and every bare ID must resolve
   to an existing artifact (per DEC-0242). Links are still used for
   non-artifact files (CONTEXT.md, specs, code) and URLs. Frontmatter
   stays bare IDs and remains what tools read; humans browse via
   `python3 tools/serve_docs.py` → `docs/human_docs.html` (per
   DEC-0244, DEC-0245). Edges also carry prose obligations, checked
   before every commit: a goal/epic's body references every artifact
   deriving from it — update the parent's Derived Work in the same
   edit that creates the child (per DEC-0246); an artifact with an
   `impacts` edge explains each impact in its own body — the impactor
   explains, the impactee stays silent (per DEC-0249); a session's
   body references every `relates-to` target (per DEC-0250).
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

## How design changes are made — change intake

**No semantic change to this corpus is made outside a recorded session
(per DEC-0252). Hard rule, no waiver — including for users with full
authority.** Discussion that changes nothing may stay off the record;
the moment a change is instructed, run intake:

1. **First mention → todo list (per DEC-0256).** Create a minimal
   tracked list — *restate intention; confirm alignment; start
   session?* — expanding it to the confirmed path's steps once aligned.
2. **Restate & align (per DEC-0255).** Restate the proposal's
   *intention*; clarifications loop back to restatement until the
   proposer confirms. Agent-noticed issues enter the same way, roles
   reversed: you propose, the user disposes (per DEC-0257).
3. **Authority check (per DEC-0262, DEC-0264).** Resolve the operator
   against `governance/people.yaml` (git identity, honor system) and
   the gate policies. An instruction outside the instructor's rights
   does not proceed — capture it verbatim as a CP
   (`source: unauthorized-attempt`) awaiting the authority holder(s).
4. **Pick the path:**
   - **Mechanical fix (per DEC-0253)** — zero semantic content (typo,
     formatting, reference repair; no contract line, decision text,
     status, approval field, or link semantics touched): commit
     directly, descriptive message, no session. When in doubt, it's
     semantic.
   - **Idea capture (per DEC-0258)** — record IDEA artifact(s) verbatim
     in a micro-session (zero linked decisions is valid).
   - **Expedited session (per DEC-0254)** — small semantic change: one
     round; every integrity step still runs.
   - **Full grilling session** — everything else: focused clarifying
     questions in small rounds, recommended answer stated first; read
     existing decisions before asking; never re-litigate what an
     accepted DEC settles.
5. **The session record opens at the verbatim proposal** (T1), then
   the restatement and alignment loop (per DEC-0255). Locate affected
   artifacts up front (search + graph) and keep a working hypothesis
   of the change's artifact level(s) through grilling (per DEC-0266).
6. **Mid-session tangents — focus-artifact test (per DEC-0260):**
   changes the artifact under refinement → grill now; needs a
   different artifact → park as an IDEA (level unclear) or deferred
   ST/SP (level clear, per DEC-0259) and continue. Cross-reference
   spawned Ideas from the session. Captured Ideas are the work queue
   (per DEC-0261): each take-up is its own new intake session, never
   an extension.
7. **Modifying approved artifacts:** superseding DECs, the staleness
   walk, and re-affirmation all complete inside the session
   (per DEC-0267) — never leave the corpus mid-cascade.
8. **Close:** detailed summary + inspired-ideas check; play back the
   decisions you intend to record and get confirmation before marking
   them accepted; record the session (`SES-`, turn-numbered,
   faithful), decisions (`DEC-`, one each), and artifact updates
   together; `status: gated` → ask the approver. Checker, then commit
   (session + decisions + artifacts in one commit; approval as its own
   commit: `Approve <ID> (<approver>, <date>)`).

Multi-party governance without the Groundwork application is
git-mediated and asynchronous (per DEC-0265): each authority holder
triages/ratifies/approves in their own sessions; committee gates
collect sign-offs across commits/PRs. Local identity is declared and
honor-system (per DEC-0264) — provenance, not tamper-proofing.

## Status lifecycle

`draft → in-refinement → gated → approved` (then `stale ⇄ approved`, or
`superseded`/`archived`). Sessions: `open → closed`. Decisions:
`proposed → accepted → superseded`. Conflicts: `open → mediating →
escalated → resolved`. Change proposals: triage `pending → mechanical |
session | rejected`. Ideas: `captured → taken-up | declined` — never
gated, never release-labeled; take-up runs intake as a new session (per
DEC-0258, DEC-0261).

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

## Orientation for a fresh agent

1. Read `CONTEXT.md`, then the Business Goal(s) in `docs/goals/`.
2. Check state: artifacts with `status: gated` await approval; `stale`
   await re-affirmation; open `CFL-` files block their artifacts; approved
   artifacts with an empty "Derived Work" section are the frontier.
3. The design is done when every Component Doc is `approved` and
   contract-complete: an implementer could build and test it from the doc
   plus its dependencies' contracts alone, without asking anyone anything.
