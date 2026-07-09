# The Groundwork Documentation System

Self-contained reference: the artifact model, file conventions, link
graph, status lifecycles, and integrity rules. This is the *what*; the
companion [refinement-process.md](refinement-process.md) is the *how*.

## Contents

1. [The pipeline](#the-pipeline)
2. [Repository layout](#repository-layout)
3. [Identity and files](#identity-and-files)
4. [Common frontmatter and typed links](#common-frontmatter-and-typed-links)
5. [Status lifecycles](#status-lifecycles)
6. [Artifact catalog](#artifact-catalog) (one section per type)
7. [Integrity rules](#integrity-rules)
8. [Operating modes](#operating-modes)

## The pipeline

```
Idea ─▶ Refinement Sessions ─▶ Business Goal ─▶ Epics ─▶ Stories/Spikes ─▶ Component Docs ─▶ implementation
             (SES)                 (BG)           (EP)       (ST/SP)           (CMP)
               │                    ▲              ▲            ▲                ▲
               └── Decisions (DEC) ─┴──────────────┴────────────┴────────────────┘
                    every artifact cites the decisions that shaped it
```

Each stage transition passes a human **approval gate**. The end product is
a set of **contract-complete Component Docs**: an implementer holding one
(plus the interface contracts of its dependencies, not their internals)
can implement and test the component without asking anyone anything. The
whole system exists to produce those docs while keeping them provably
aligned with the business intent at the root.

Three properties make the system work; protect them above all:

- **Provenance**: raw conversation → distilled Decision → cited by
  requirements/contracts. "Why does this contract say X?" is always
  answerable, down to who said what and when.
- **Gates**: nothing derives from an unapproved parent, so every layer of
  the tree is human-ratified.
- **Traceability**: typed links make the tree machine-walkable — impact
  analysis, staleness, and refinement ordering all ride the link graph.

## Repository layout

```
CONTEXT.md               glossary — the project's ubiquitous language
AGENTS.md                standing instructions for agents (Groundwork marker)
tools/check_links.py     graph integrity checker — run before every commit
governance/              governance-as-code (DEC-0263): roles.yaml,
                         domains.yaml, gate-policies.yaml, people.yaml —
                         seeded solo at bootstrap, edited via normal commits
docs/
├── goals/               Business Goals        BG-*
├── epics/               Epics                 EP-*
├── stories/             Stories               ST-*
├── spikes/              Spikes                SP-*
├── components/          Component Docs        CMP-*
├── sessions/            Session records       SES-*
├── decisions/           Decision records      DEC-*
├── conflicts/           Conflicts             CFL-*
├── change-proposals/    Change Proposals      CP-*
├── ideas/               Ideas                 IDEA-*
└── consolidations/      Consolidations        CON-*
```

## Identity and files

- Every artifact has an immutable ID: `<PREFIX>-<4-digit zero-padded n>`
  (e.g. `EP-0003`). Numbers are sequential per prefix and **never reused**,
  even after deletion. To allocate, scan all of `docs/` for the current
  max of that prefix.
- Filename: `<ID>-<kebab-case-slug>.md`. The slug may change; the ID may not.
- One artifact per file: markdown body + YAML frontmatter.
- Dates are absolute (`2026-07-06`), never relative.

## Common frontmatter and typed links

```yaml
---
id: EP-0002
type: epic          # business-goal | epic | story | spike | component |
                    # session | decision | conflict | change-proposal |
                    # idea | consolidation
title: Short descriptive title
status: draft
owner: <person or role accountable for the gate>
created: 2026-07-06
overview: >-        # REQUIRED on every artifact (DEC-0284): self-sufficient
  ...               # plain prose, max 250 words — read first, body on demand
links:
  derives-from: [BG-0001]   # immediate parent(s) in the pipeline
  satisfies: [BG-0001]      # business goal(s) ultimately served
  depends-on: []            # artifacts this one requires (e.g. CMP contracts)
  conflicts-with: []        # open conflicts (paired with a CFL artifact)
  supersedes: []            # earlier artifact(s) this replaces
  relates-to: []            # weak association (context, not derivation)
  impacts: []               # same-type siblings whose decisions this
                            # artifact's refinement will shape
  impacted-by: []           # inverse of impacts
cites: [DEC-0004, DEC-0009] # decisions that shaped this artifact
---
```

Rules:

- Link values are bare artifact IDs; the vocabulary above is **closed** —
  no invented link types. Empty lists may be omitted.
- Frontmatter links are the authoritative relationships; the frontmatter
  is what tools read. In body prose, cross-references to artifacts are
  **bare IDs** (`EP-0003`, `DEC-0152`; citation clauses `(per DEC-0152,
  DEC-0239)`) — navigational rendering is a viewer concern, no graph
  semantics in prose. Every bare ID outside code spans/fenced blocks
  must resolve to an existing artifact, and an inline markdown link
  targeting an artifact file is an integrity violation the checker
  reports. Markdown links remain for non-artifact files (CONTEXT.md,
  specs, code) and URLs.
- **Impact links**: "X impacts Y" means decisions recorded while refining
  X are expected to constrain, shape, or invalidate decisions in Y. They
  connect *same-type* artifacts only, and both endpoints record the
  relationship (`impacts` on X, `impacted-by` on Y) — the checker enforces
  reciprocity. Impact graphs may legitimately contain cycles; refinement
  ordering among siblings is judged over this graph (refine items whose
  impactors are settled and whose impact fan-out is largest, first).
- `cites` is the provenance field: any artifact whose content rests on a
  decision cites its `DEC-` ID.
- **The `overview:` field** (DEC-0284..DEC-0288) is the
  progressive-disclosure entry point: self-sufficient plain prose, max
  250 words, bare IDs allowed, no markdown — what the artifact is, its
  core content/outcome, and its disposition. It is **derived,
  non-normative** content (like consolidations): never citable as
  provenance, body wins on conflict, freely regenerable — so adding or
  regenerating one on a closed session or accepted decision violates no
  immutability rule. Any edit that changes an artifact's meaning updates
  its overview in the same edit; gate prep confirms faithfulness.
  Presence and the cap are checker-enforced.

## Status lifecycles

Standard lifecycle (goals, epics, stories, spikes, components):

```
draft ─▶ in-refinement ─▶ gated ─▶ approved ─▶ (stale ⇄ approved)
                                       │
                                       ├─▶ superseded
                                       └─▶ archived

any active status ─▶ deferred ─▶ draft   (stories, epics & spikes)
```

- `draft` — generated/authored, not yet in active refinement.
- `in-refinement` — under active session work.
- `gated` — refinement complete, awaiting the approver's sign-off.
- `approved` — human-ratified; may feed the next stage. Record
  `approved-by:` and `approved-on:` in frontmatter at this transition.
- `stale` — an upstream basis changed after approval; blocks new
  downstream derivation until re-affirmed back to `approved`.
- `superseded`/`archived` — terminal; a superseding artifact links back
  with `supersedes`.
- `deferred` — stories, epics, and spikes only: captured but
  intentionally out of the current release. Entered from any active status; while deferred the
  artifact cannot pass a gate and nothing derives from it. Revival always
  lands at `draft` — content, citations, and links are retained, but the
  gate is re-earned in current context. Deferral and revival each cite a
  decision.

**Release scoping.** Stories, epics, and spikes may carry a `release:`
frontmatter field: reserved `backlog` ("wanted, no target yet") or a prefix of a
SemVer 2.0.0 version core — `MAJOR`, `MAJOR.MINOR`, or
`MAJOR.MINOR.PATCH` (e.g. `1`, `1.2`, `1.2.3`; numeric identifiers, no
leading zeroes, no `v` prefix, no pre-release/build metadata; quote the
value so YAML keeps it a string). A partial value is a scope ("somewhere
in the 1.x.x line"), narrowable mechanically; *moving* an item between
releases cites a decision. Absence of the field = current release. An
epic's label defaults its derived stories and spikes; either may
override. Labels
must exactly match a release declared in the governing Business Goal's
Scope section (`**Releases:**` list, current release marked `(current)`),
or be `backlog`. Non-current effective release ⇔ `deferred`. Deferred
stories leave the design-% denominators and coverage warnings; the
status report lists them grouped by release, SemVer precedence order,
`backlog` last.

**Trigger registry.** `docs/TRIGGERS.md` (not an artifact — no
frontmatter, no artifact ID) tracks watched conditions with subscribed
deferred items: entries under strict headings
`## TRG-nnnn (armed|fired|retired)` with `**Condition:**` (observable,
human-testable), `**Subscribers:**` (one line per subscription:
action verb + bare-ID target + that subscription's own
`(per DEC)` citation — one condition, many watchers, each individually
attributable), `**Cites:**` (the arming decision), and — once
fired/retired — `**Fired:**`/`**Retired:**` with date, decision link,
and outcome. TRG IDs are sequential, never reused; entries are never
deleted. Firing requires a decision recording the observation and
**revives all subscribers** (the one decision serves the firing and
every revival). Lifecycle invariants: armed triggers subscribe only
`deferred` artifacts (≥1, checker-enforced — so a revived item cannot
be revived again); when an item leaves `deferred`, its subscriber lines
are removed from all other armed triggers in the same change, citing
the same reviving decision; an armed trigger emptied this way
auto-retires. Tooling loads **armed entries only** into agent context;
the status report lists them; a release-declaration amendment to a
Business Goal must review the registry.

Reduced lifecycles:

- **Session**: `open → closed`. Closed sessions are immutable — follow-up
  conversation is a *new* session.
- **Decision**: `proposed → accepted → superseded`. Accepted decisions are
  immutable; changing course means a new decision with `supersedes` set.
- **Conflict**: `open → mediating → escalated → resolved`.
- **Change Proposal**: triage states `pending → mechanical | session | rejected`.
- **Idea**: `captured → taken-up | declined`. Ideas pass no gates and
  nothing derives from them except their take-up intake session.
- **Consolidation**: `fresh | stale` (derived artifacts, mechanically
  invalidated when any source changes).

## Artifact catalog

### Business Goal (BG) — `docs/goals/`
The foundational statement of a refined business intent; root of the
traceability graph. Sections: **Problem** (in the sponsor's terms, no
solution language), **Current State & Gap** (what exists today and the
specific capability gap that lets the problem persist — distinct from
Problem's human/business pain and from System Context's build-vs-reuse
question), **Intent**, **System Context** (boundary-only, C4-Level-1/2
inspired: what's being built, who uses it and how, where it lives, the
trigger/output contract, existing-vs-new for the system's own parts,
existing systems needing change, external dependencies — plus a
mandatory Context Diagram and an optional Process Flow diagram, both
Mermaid; see [goal-grilling-questions.md](goal-grilling-questions.md)),
**Illustrative Scenario** (non-binding: a happy-path walkthrough, plus
any bad paths that surfaced naturally — full edge-case enumeration is
deferred to Epic/Story refinement), **Outcomes & Success Criteria**
(each citing a decision, ideally metric-shaped), **Scope** (in/out; if
the work is release-scoped, also a `**Releases:**` list — one item per
release, value in a code span, current release marked `(current)` —
which release labels validate against), **Constraints** (including an
explicit compliance/data-residency check, answered even when "none
identified"), **Stakeholders & Roles**, **Conflicts & Tensions**,
**Derived Work**. A goal must be `approved` before epics derive from it.
Solution design does not belong here — System Context stays
boundary-only (what, not how); internal mechanics are Epic/Component
territory. Frontmatter extras: `sponsor:`.

### Epic (EP) — `docs/epics/`
A coherent body of work derived from an approved goal. Sections:
**Summary**, **Why (Goal Alignment)** — the argument a gate reviewer
checks, **Scope** (in/out), **Domain Context** (bounded context + glossary
terms it introduced), **Interfaces & Contracts to Define**, **Risks & Open
Questions** (including candidate spikes), **Derived Work**. Must be
`approved` before stories/spikes derive.

### Story (ST) — `docs/stories/`
An implementable unit derived from an approved epic. Sections: **Summary**,
**Acceptance Criteria** — numbered, individually testable, **each ending
with `(per DEC-nnnn)`** (a criterion no decision supports means: refine
more, never invent provenance), **Component Impact** (which CMPs it
builds or modifies — the story-side forward declaration that component
design elements later back-reference via `Implements:` lines), **Out of
Scope** (future-work entries must exist as, and link, deferred
stories/spikes; boundary statements link the owning artifact —
permanent denials are never backlogged), **Notes for Implementers** (optional context, never a
substitute for contracts). Amending or superseding an approved story
stales every CMP with an element that implements it. Out-of-release
stories are `deferred` with a `release:` label (see Release scoping in
the status section, above).

### Spike (SP) — `docs/spikes/`
A research unit: a question that must be answered before sibling work can
be trusted. Sections: **Question** (phrased so an answer is recognizable),
**Why It Blocks**, **Method**, **Findings** (at completion), **Resulting
Decisions**. Frontmatter extras: `timebox:`. A completed spike must
produce ≥1 Decision (deriving from the spike) — even "assumption
confirmed, no change." Cross-cutting process-level spikes may derive
directly from a Business Goal.

### Component Doc (CMP) — `docs/components/`
The contract-complete spec of one system component, aligned with a
DDD-style bounded context — **the deliverable**. A component comprises
typed **design elements** (see below). Sections: **Purpose**,
**Ubiquitous Language** (every model term glossary-resolved), **Design
Elements** (each element declared `### <ElementName> (<type>)`, followed
directly by a mandated `Implements:` line naming ≥1 story as markdown
links, and carrying its own contract block with element-scoped item IDs
like `StorageService.B-3`; kinds `B` behavior / `A` API / `D` data;
schemas in language-neutral form), **Component Invariants** (cross-element
guarantees, `C-<n>`), **Implementation Guidance** (two subsections:
**Constraints** `IG-<n>` — normative for the reference implementation,
decision-cited; **Notes** — advisory, may be stack-specific, never
load-bearing: contracts must stand without them), **Dependencies** (which
contract sections/items of each `depends-on` component are consumed —
internals are out of bounds), **Acceptance & Test Expectations**, **Out
of Scope** (especially plausible adjacent behavior an implementer might
assume). Out of Scope entries follow a differentiated rule: an entry that is really *future work* must exist as a deferred story/spike and be linked from the entry (prose-only future work is a review-time smell); a *boundary statement* links the owning artifact if one exists and never mints a deferred artifact. **Every contract item — element items, invariants, and
Constraints — cites at least one decision**; uncited items block the
gate (Notes are exempt). Frontmatter extras: `context:` (bounded context
name); `component-type:` only on standalone element CMPs (see
graduation, below). Drafts may carry `Pending — …` sections; the gate
requires completeness.

**Design elements.** The element-type taxonomy is a **closed set of
five** — extended only by an accepted decision and spec change:

- **entity** — identity that persists across state changes; lifecycle;
  mutable state.
- **value** — immutable, attribute-defined; equality by value.
- **service** — stateless capability exposing operations.
- **event** — schema'd payload crossing a boundary, with
  emission/ordering/delivery semantics.
- **protocol** — a capability seam: the contract an implementation must
  satisfy.

Each type mandates contract kinds, checkable at the gate: entity ⇒ full
behavior contract (identity semantics, lifecycle states, transitions,
domain-operation semantics) + data contract, with an API contract
required only when its operations are exposed at the component boundary;
value ⇒ data contract; service ⇒ API + behavior; event ⇒ schema +
delivery semantics; protocol ⇒ API + conformance expectations.
**Schema-resolution rule**: every request/response schema in an API item
is defined inline or resolves to a declared value/event element —
dangling type references block the gate. The `### Name (type)` headings
are the single machine-readable source of truth (no frontmatter element
list). **Implements lines**: every element declares, directly under its
heading, the story or stories whose implementation it handles
(`Implements: ST-nnnn`, ≥1, resolvable — missing or empty is a
gate-blocker; an element no story motivates means refine or cut). An
element may only reference a story whose Component Impact links this
CMP; a CMP cannot gate while a story naming it has no referencing
element; approved stories with zero referencing elements anywhere are
audit-reported design gaps. These edges power the design and
implementation percent-complete rollups (story → epic → goal,
equal-weighted; implementation status stays projection-side — e.g. the
issue tracker — never in the docs). Private helper elements list the
stories of the element they support; graduated seam CMPs reference the
stories that birthed the seam. Common constructs are modeled as *compositions*, not new types:
a repository = protocol + stored entity/value schemas; a workflow/saga =
service with a state-machine behavior contract + events (+ a process
entity); a policy = value (the rule schema) + the service that evaluates
it. **Seam graduation**: an element consumed by more than one CMP, or
needing independently versioned conformance, graduates to its own
standalone CMP with `component-type: <type>` in frontmatter.

### Session (SES) — `docs/sessions/`
The record of one 1:1 refinement conversation. Sections: **Purpose**,
**Transcript** — turn-numbered (`T1`, `T2`, …) so decisions can cite spans;
this is the raw record, faithful to what was actually said, never
summarized in place (fidelity `verbatim` when captured live;
`reconstructed` when written up from an agent conversation — say which),
**Decisions Produced**, **Conflicts Raised**. Frontmatter extras:
`participant:`, `participant-role:`, `facilitator:` (agent + model),
`transcript-fidelity:`. Append-only; corrections happen in later turns or
later sessions. Multi-stakeholder input = separate 1:1 sessions that the
facilitator synthesizes, never shared sessions.

### Decision (DEC) — `docs/decisions/`
The unit of provenance: one distilled, attributable decision. Sections:
**Context** (the question that had to be answered), **Decision** (one
unambiguous statement — if it takes more than a short paragraph it is
several decisions), **Rationale**, **Alternatives Considered**,
**Implications**. Frontmatter extras: `decided-by:`, `decided-on:`,
`source-span: "SES-0001 @ T4-T6"` (turns that actually support it; for
spikes, `"SP-0002 findings"`). `derives-from` must point at a session or
spike. Record decisions that are hard to reverse, surprising without
context, or genuine trade-offs; routine clarifications live in artifact
bodies instead.

### Conflict (CFL) — `docs/conflicts/`
A first-class record of contradictory or competing requests. Sections:
**The Tension** (stated neutrally), **Party Intents** (the underlying
intent behind each position — discovered before mediating), **Mediation
Record** (compromises proposed, responses), **Resolution** (citing the
decision(s) that resolved it). While unresolved, the artifacts in tension
link `conflicts-with: [CFL-…]`, cannot pass a gate, and nothing new may
derive from them. Frontmatter extras: `escalated-to:` once escalated.

### Change Proposal (CP) — `docs/change-proposals/`
A captured change proposal awaiting triage or ratification, created in
exactly two situations (DEC-0262): (1) **out-of-band** intent — an edit
made elsewhere, a reviewer suggestion, implementation feedback, input
queued while another session runs; (2) an **unauthorized change
attempt** — a change instructed by someone whose decision rights
(governance config) don't cover it; the change does not proceed, and
the CP captures the attempt verbatim awaiting the authority holder(s).
The CP is the artifact form of an out-of-authority proposal requiring
ratification. A live instruction by an authorized user needs no CP —
the intake session record is the capture. Sections: **Proposed
Change**, **Context**, **Triage Outcome** (mechanical fix / refinement
session / rejected-with-rationale). Frontmatter extras: `source:`
(`ui-suggestion | jira-drift | implementation-feedback |
unauthorized-attempt`), `proposed-by:`, `triage:`. CPs never modify
their target directly; the fix or session does, citing the CP.

### Idea (IDEA) — `docs/ideas/`
A pre-classification capture of raw change intent (DEC-0258) — too raw
to know whether it is goal-, epic-, story-, spike-, or component-shaped.
The moment intent's level *is* clear, capture it as a deferred
story/spike instead (DEC-0259); Ideas never carry `release:` labels or
trigger subscriptions. Captured mid-session under the focus-artifact
test (DEC-0260), or via an idea-capture micro-session (a session record
with zero linked decisions is valid; one may batch several ideas). The
spawning session cross-references every Idea it produces (`relates-to`
+ body mention). Captured Ideas are the project's brain-dump work
queue (DEC-0261): the status report lists them, and each take-up runs
the change-intake protocol as its own new session — never an extension
of the session that spawned it. Sections: **The Idea** (verbatim),
**Spark Context**, **Disposition** (pending → names the take-up
session, or decline rationale + decider). Frontmatter extras:
`proposed-by:`; `derives-from` points at the spawning session when
there is one. Statuses: `captured → taken-up | declined`.

### Consolidation (CON) — `docs/consolidations/`
A derived summary of a frequently-needed neighborhood of the graph (e.g.
"BG-0001 + its epics + key decisions"), used to load context efficiently.
Sections: **Path Covered**, **Consolidated Content** (faithful, no new
claims, load-bearing statements carry citations), **Omissions**.
Frontmatter extras: `sources:` (each pinned to a git ref). Stale the
moment any source changes; never citable as provenance; always
regenerable. Optional — valuable once the graph outgrows comfortable
re-reading.

## Integrity rules

Enforced by `tools/check_links.py` (bundled with this skill; installed
into projects at bootstrap):

1. IDs are unique; frontmatter `id` matches the filename prefix; type
   matches prefix.
2. Every linked or cited ID resolves to an existing artifact.
3. Every epic/story/spike/component traces to ≥1 Business Goal through
   `derives-from`/`satisfies` chains.
4. Every decision `derives-from` a session or spike.
5. No `approved` artifact links `conflicts-with` an unresolved conflict.
6. Impact links are reciprocal and same-type.
7. Component design elements use the closed type enum; element names are
   unique within a doc.
8. Body cross-references are bare artifact IDs that resolve to existing
   artifacts; inline markdown links targeting artifact files are
   violations; remaining relative links (non-artifact files) must
   resolve.
9. Every element heading is directly followed by an `Implements:` line
   naming ≥1 resolvable story whose Component Impact links the CMP back;
   approved stories no element implements are reported as design-coverage
   warnings.
10. `deferred` status and `release:` fields appear only on
    stories/epics/spikes; `release:` values are `backlog` or SemVer
    prefixes exactly matching a declared release; deferred ⇔ non-current
    effective release. Elements implementing only deferred stories are
    audit warnings.
11. The trigger registry (`docs/TRIGGERS.md`) is well-formed: valid
    headings, unique TRG IDs, required fields per status, resolvable
    links, decision link on every fired/retired entry, decision-cited
    subscriber lines, and armed triggers subscribing only deferred
    artifacts (≥1).
12. **Derived-work completeness** (DEC-0246): every artifact whose
    `derives-from` names a goal or epic is referenced by bare ID in
    that parent's body (the Derived Work section, normally).
13. **Cites/prose synchronization** (DEC-0247), on goals, epics,
    stories, spikes, and components — both directions: no dead cites
    (a `cites:` DEC the body never references) and no missing cites
    (a body-referenced DEC absent from `cites:` and links). `cites:`
    is the complete considered set.
14. **Impactor-side impact prose** (DEC-0249): an artifact carrying an
    `impacts` edge references each target in its body — the impactor
    explains how it shapes the impactee. The impactee carries no prose
    obligation.
15. **Session mention completeness** (DEC-0250): every artifact in a
    session's `relates-to` is referenced in the session body — at
    write time in the Purpose section; retroactively via a Post-Close
    Enrichment entry.
16. **Overview presence, cap, and resolution** (DEC-0284, DEC-0286,
    DEC-0287): every artifact's frontmatter contains a non-empty
    `overview:` of at most 250 words whose bare artifact IDs all
    resolve (DEC-0242 extended to the overview surface). Faithfulness
    is process-enforced (DEC-0288), not checker territory.

Beyond the checker, the human-enforced rules: closed sessions and accepted
decisions are immutable; acceptance criteria and contract items cite
decisions; glossary terms are used exactly; staleness propagates
story→CMP over Implements references.

Immutability has one sanctioned carve-out — **cross-reference
enrichment** (DEC-0248, extending DEC-0091): adding bare-ID mentions,
`cites:` entries, or link entries that surface *already-existing*
relationships never alters recorded meaning and does not trigger
staleness or re-gating. In closed sessions such additions go in a dated
`### Post-Close Enrichment` subsection appended at the bottom of the
Transcript section; transcript turns are testimony and are never
edited. Enrichment never *creates* relationships — only surfaces ones
the frontmatter or graph already records.

## Operating modes

**Manual mode (default — what this skill runs):** a single branch;
lifecycle state lives in the `status` frontmatter field; the user approves
gates in conversation and the agent records `approved-by`/`approved-on`;
every session and every approval is a commit; git history is the audit
trail.

**Branch/PR mode (optional, for teams on a git host):** each artifact
under refinement gets an item branch carrying the item plus its sessions
and decisions; opening the branch opens a PR to main; **PR approval is the
gate** and merge = approved, so main holds only ratified artifacts;
post-merge changes reuse the branch with a new PR. Adopt this only when
the team actually reviews PRs; the artifact model is identical either way.
