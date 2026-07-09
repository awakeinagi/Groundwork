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
docs/
├── goals/       BG-*   Business Goals (root of all traceability)
├── epics/       EP-*   Epics derived from approved goals
├── stories/     ST-*   Stories (acceptance criteria cite decisions)
├── spikes/      SP-*   Research questions (findings become decisions)
├── components/  CMP-*  Contract-complete component specs (the deliverable)
├── sessions/    SES-*  Refinement conversation records (append-only)
├── decisions/   DEC-*  Distilled decisions (the unit of provenance)
├── conflicts/   CFL-*  Contradictory-request records (blocking)
├── change-proposals/ CP-*   Out-of-band change capture
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

## How design changes are made

All design content changes flow through **refinement sessions** with a
human, not unilateral edits:

1. Interview the stakeholder about the artifact being refined — focused
   clarifying questions in small rounds, each with your recommended
   answer stated first. Read existing decisions before asking; never
   re-litigate what an accepted DEC settles.
2. Play back the decisions you intend to record and get confirmation
   in-conversation before marking them accepted.
3. Record the session (`SES-`, turn-numbered transcript, faithful to what
   was actually said), the decisions (`DEC-`, one decision each), and the
   artifact updates (content + `cites` + links) together.
4. Set the refined artifact to `status: gated` and ask the approver.
5. Checker, then commit (session + decisions + artifact in one commit;
   approval as its own commit: `Approve <ID> (<approver>, <date>)`).

Mechanical, non-design edits (fixing a broken link, adding a reciprocal
edge, status bookkeeping) may be made directly — they must never change
design meaning.

## Status lifecycle

`draft → in-refinement → gated → approved` (then `stale ⇄ approved`, or
`superseded`/`archived`). Sessions: `open → closed`. Decisions:
`proposed → accepted → superseded`. Conflicts: `open → mediating →
escalated → resolved`.

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
