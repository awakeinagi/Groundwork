# Groundwork Glossary

The ubiquitous language of the Groundwork system. Terms are canonical: docs,
code, UI copy, and agent prompts must use these words with exactly these
meanings. Resolve new or drifting terms here first (see
[SPEC-artifact-common](docs/specs/SPEC-artifact-common.md) for how the glossary
is gated).

## The system

- **Groundwork** — the umbrella name for two delineated deliverables
  (DEC-0420): the Groundwork Paradigm and the Groundwork Application.
  Refers to the system as a whole; use the specific term when precision
  matters.
- **Groundwork Paradigm** — the documentation-first design method itself:
  the gated artifact tree, grilling sessions, decision provenance, and
  integrity rules, delivered as agent skills plus the Groundwork
  Engine's gw CLI. Adoptable standalone in any repository and never
  requires the Application (DEC-0421).
- **Groundwork Application** — the centralized team-facing application
  that manages Groundwork corpora through a UI; an optional superset
  built on the same paradigm. Exactly one instance serves a given
  Groundwork docs repository (DEC-0426, DEC-0438).
- **Groundwork Engine** — the single-sourced implementation of paradigm
  mechanics (DEC-0423): today the gw CLI's internals; target shape a
  library with the CLI and the Application backend as adapters.
- **skill-mode** — using the Groundwork paradigm entirely through an
  agent-chat runtime (Claude Code, GitHub Copilot, Codex, OpenCode, …)
  via the Groundwork skills, no Application/UI; the gw CLI is the
  substrate the skills drive (DEC-0444). The paradigm's core subset
  (DEC-0433).
- **Method Track** — historical name for BG-0002's original governance
  charter (DEC-0338, superseded by DEC-0441); its substance continues
  as the rechartered BG-0002's self-governance outcome (DEC-0442).
- **Canonical Store** — the git-backed markdown repository that is the single
  source of truth for all artifacts. Every other representation (Jira, the
  Graph Index, UI views) is derived from it.
- **Projection** — a derived, non-authoritative representation of canonical
  artifacts in an external system (e.g., the Jira issue mirroring an Epic).
  Edits made to a projection are drift, to be detected and reconciled.
- **Graph Index** — a queryable graph database built from the typed links in
  artifact frontmatter. Derived and rebuildable at any time; never written to
  directly; never a source of truth.
- **Branch Overlay** — the Graph Index's thin per-item-branch view: that
  branch's additions and changes layered over the main base graph, so
  sessions query their drafts in the context of approved reality. Every
  query names its view; results tag nodes with ref and status.
- **Connector** — a pluggable adapter behind a defined API contract for
  *external-system integration*: Jira, codebase hosts (Bitbucket/GitHub),
  auth providers, doc storage. Distinct from a Port, which hosts
  Groundwork's own infrastructure.
- **Work-Management Connector** — the pluggable connector family for
  agile work-management systems, owning projection lifecycle, drift
  capture, and the backlog read feed behind a host-agnostic,
  capability-declaring contract. Jira Data Center is the reference
  adapter; monday.com, OpenProject, and Jira Cloud are future adapters
  against the same contract.
- **Code-Host Connector** — the pluggable connector family for git-hosting
  platforms: fork/branch/PR orchestration, review posting, branch-protection
  and team administration, and allowlisted read-only context access, behind
  a host-agnostic, capability-declaring contract. GitHub (cloud) is the
  reference adapter; Bitbucket Data Center, Bitbucket Cloud, and GitLab are
  future adapters against the same contract.
- **Notifier Connector** — the pluggable connector family for external
  notification delivery: a delivery-pipe protocol that receives a
  resolved channel address and pre-rendered notification payload from
  the notification center (EP-0006) and returns a terminal delivery
  result. Email is the reference adapter; Slack, Teams, and other
  channels are future adapters against the same contract.
- **Capability Manifest** — the structured declaration a connector adapter
  publishes stating which above-minimum operations it supports; a
  documented minimum set is required to run Groundwork at all, and the
  consuming policy compiler adapts to or emulates whatever a manifest
  doesn't declare.
- **Attribution Block** — the structured, service-signed block
  (person-id, PR reference, decision timestamp) carried in the body of
  a program-user review, cryptographically attributing the review to
  the human approver; verified by the `gate-policy` check.
- **Orchestrator App** — the GitHub App registration backing every
  write operation of CMP-0009
  (fork/branch/PR orchestration, review posting, check and
  branch-protection administration, team sync); posts program-user
  reviews under its own bot identity. Structurally distinct from the
  Reader App.
- **Reader App** — the read-only GitHub App registration backing
  CMP-0009's
  allowlisted context reads, installed only on allowlisted
  repositories. Never shares a credential with the Orchestrator App.
- **Port** — a Protocol-typed seam for a swappable infrastructure
  capability that hosts Groundwork's own state or computation. The six
  Ports: app database, vector store, embedding, graph store, Queue,
  KV-store. Consumers program against the Port contract, never an
  engine API.
- **Adapter** — a concrete implementation of one Port (e.g. DuckDB,
  LadybugDB, a local embedding model, a REST embedding client), selected
  by deployment configuration and valid only if it passes the Port's
  conformance test suite.
- **Composition Root** — the single place, owned by
  EP-0008, where
  Port contracts are bound to concrete Adapters at process startup, from
  deployment configuration. Every other engine programs against Port
  contracts only; only the Composition Root knows which Adapters are
  actually wired in.
- **Secret Store** — the single component holding secret material at
  rest: envelope-encrypted storage for connector and service secrets
  (OAuth tokens, signing keys, webhook secrets) in the app database,
  with the master key from deployment configuration, never persisted
  with the data.
- **Session Token** — the opaque, revocable handle Identity & Access
  issues after authentication; carries no claims — session state lives
  server-side, and role claims are resolved fresh per request.
- **Role Claims** — the resolved answer to "which roles does this
  person hold at this moment": direct role memberships plus roles held
  through an active time-bounded delegation window, evaluated at an
  explicit governance ref and point in time.
- **Handoff Manifest** — the machine-readable package Groundwork emits
  at its southern boundary: ordered Slices referencing Work Packages,
  with typed dependency order, pinned to a canonical-ref. Generated and
  written by the Artifact Store (DEC-0305), topology supplied by the
  Graph Index.
- **Implementation Swarm** — the set of AI agents and/or developers that
  build the system from Work Packages. Dispatched and verified by the
  Swarm Orchestrator; consumes the Handoff Manifest.
- **Swarm Orchestrator** — the v1 deliverable (DEC-0308, superseding
  DEC-0014's exclusion) that consumes the Handoff Manifest, dispatches
  implementation agents per Slice ordering and lifted implementation
  edges, verifies acceptance, and reports results. Feedback-loop
  ingestion into the corpus remains out of v1 scope.
- **Work Package** — the generated dispatch unit of implementation
  (DEC-0300): one or more design elements' contract blocks plus the
  transitive closure of referenced contract items, applicable component
  invariants/IG constraints, a glossary slice, and a Shared Preamble
  reference. Never hand-authored; same canonical-ref ⇒ identical
  bundles. An element stands alone iff it carries self-contained
  implementable A/B items; otherwise it rides with its
  enforcing/consuming element.
- **Integration Work Package** — the per-component generated work
  package (DEC-0301) that depends on the component's element work
  packages and verifies its C-n invariants and Acceptance & Test
  Expectations.
- **Shared Preamble** — the single generated document of swarm-wide
  cross-cutting context (reference stack, error model, repo
  conventions) referenced by every work-package bundle instead of
  duplicated into each (DEC-0300).
- **Slice (SL)** — a first-class artifact (DEC-0302, SPEC-slice): a
  named, owned vertical subset of work packages forming one end-to-end
  behavior, carrying the acceptance-criteria block that is the durable
  home of end-to-end test expectations. Referenced by the manifest in
  ordered sequence, walking skeleton first. Slices reference work
  packages across components; they never regroup components
  (DEC-0307).
- **Empty Context** — the implementing agent's starting state
  (DEC-0304): no conversational history; only its work-package bundle
  plus the Shared Preamble. Crawling the corpus pinned at
  canonical-ref remains sanctioned (DEC-0011).
- **Lifted Edge** — a coarse-grained dependency edge derived from
  fine-grained ones (DEC-0309): a component's depends-on is the exact
  projection of its members' cross-component Uses: targets, typed
  strongest-member-wins (implementation > interface > test). At epic
  boundaries lifting is reported, never enforced.
- **Closure Axis** — the single shared reason-for-change a component's
  elements are grouped around (DEC-0307, Common Closure Principle):
  changes of that kind stay inside the component (e.g. CMP-0001/the
  storage model, CMP-0009/GitHub's API surface, CMP-0004/governance
  semantics).

## Artifacts

- **Artifact** — any identified, versioned document in the Canonical Store:
  Business Goal, Epic, Story, Spike, Component Doc, Session, Decision,
  Conflict, Change Proposal, Idea, Research, Consolidation.
- **Business Goal (BG)** — the foundational statement of a refined business
  intent: problem, intent, outcomes, scope, constraints. Root of the
  traceability graph.
- **Epic (EP)** — a coherent body of work derived from a Business Goal,
  refined with product owners and engineering/data-science leads.
- **Story (ST)** — an implementable unit of work derived from an Epic, with
  acceptance criteria citing Decisions.
- **Spike (SP)** — a research unit derived from an Epic. Its findings are
  recorded as Decision records, which drive impact analysis on siblings.
- **Component Doc (CMP)** — a contract-complete specification of a system
  component (aligned with DDD-style bounded contexts) handed to the
  Implementation Swarm.
- **Session (SES)** — an append-only record of a 1:1 refinement conversation
  between the agent and one participant. The raw material Decisions distill.
- **Decision (DEC)** — a distilled, attributable decision: context, choice,
  rationale, alternatives, source (Session or Spike). The unit of provenance.
- **System Decision** — a Decision the gate engine authors from a fixed
  template to record an automated outcome (e.g., a timeout-to-default
  conflict resolution), citing the election and default rule that
  authorized it; lands through the auto-PR path under a
  template-conformance check, never through a mechanical write.
- **Conflict (CFL)** — a first-class record of contradictory or competing
  requests, linking the artifacts in tension. Blocks downstream generation
  until resolved.
- **Consolidation (CON)** — curated, derived reference material summarizing a
  frequently traveled path of the artifact graph, maintained for agent
  retrieval efficiency and invalidated when its sources change.
- **Overview** — the derived, non-normative frontmatter summary every
  artifact carries (self-sufficient plain prose, max 250 words): the
  progressive-disclosure entry point read before — often instead of — the
  body. Never citable as provenance; the body wins on conflict; kept
  faithful in the same edit whenever meaning changes.
- **Participant Profile** — opt-in, per-person interaction memory (pacing,
  preferences, questions already covered) that improves repeat sessions;
  owned by its subject, who can read, edit, and delete it via the UI; never
  a home for org facts, which belong in artifacts.
- **Change Proposal (CP)** — a captured change proposal awaiting triage or
  ratification: either out-of-band intent (Jira drift, UI suggestion,
  implementation feedback) or an unauthorized change attempt — a change
  instructed by someone whose Decision Rights don't cover it. Preserved
  verbatim and triaged into a mechanical fix, a refinement session, or an
  audited rejection; the artifact form of an out-of-authority proposal
  requiring ratification.
- **Idea (IDEA)** — a pre-classification capture of raw change intent —
  too raw to know which artifact level it lands at. Captured verbatim in
  seconds (mid-session under the Focus-Artifact Test, or via an
  idea-capture micro-session), it joins the work queue until an intake
  session takes it up or it is declined with rationale. Never gated,
  never release-labeled; classified intent defers as a Story/Spike
  instead.
- **Research (RSCH)** — a free-standing deep investigation into a topic
  drawn from any source class (web search, books, videos, or others),
  distinct from a Spike (which derives from an Epic to answer a
  design-tree question) and from an Idea (raw pre-classification capture
  versus RSCH's post-investigation, analyzed evidence). Lives in
  `docs/research/` as one canonical main file (frontmatter, overview,
  status, links, research goals, compiled findings, and Business-Goal
  applicability analysis) plus optional subtopic write-ups: plain
  markdown files under the artifact's own directory
  (`docs/research/RSCH-nnnn/`), owned by and referenced from the main
  file, without their own IDs or frontmatter. Statuses: commissioned,
  in-progress, concluded, abandoned, deferred. Ungated; reopenable from
  concluded back to in-progress, with each round recorded in its own
  timestamped, append-only section (DEC-0447, DEC-0448). A commissioned
  or in-progress RSCH may enter deferred and revives to its prior
  status, mirroring the deferred semantics DEC-0104 already gives
  stories, epics, and spikes; abandoned remains terminal (DEC-0458).
- **Source Register** — the per-Research-artifact list of sources
  (title, reference or URL, source type, date accessed) that every
  finding must cite from (DEC-0452).
- **Source Mode** — the recorded choice governing how a Research
  effort's sources are gathered: a stakeholder-supplied complete list,
  a stakeholder-supplied seed list the agent expands, or sources the
  agent finds on its own (DEC-0451).
- **Research Round** — a Research artifact's timestamped, append-only
  record of one investigation pass (initial or reopened); earlier
  rounds are never rewritten (DEC-0448).
- **Commissioned** — the initial status of a Research artifact opened
  at intake to be investigated, as opposed to one created post-hoc
  directly at `concluded` for research that already happened
  (DEC-0448).

## Design elements

The typed constituents of Component Docs (see
[SPEC-design-elements](docs/specs/SPEC-design-elements.md)). The five type
names below are reserved words when used as element types.

- **Design Element** — a named, typed constituent of a Component Doc's
  contract, declared as `### <Name> (<type>)` in the doc's Design Elements
  section and carrying its own contract block.
- **Element Type** — the closed classification of Design Elements: Entity,
  Value, Service, Event, Protocol. Extended only by an accepted Decision
  and spec change.
- **Entity** — an element type: a domain concept with persistent identity,
  lifecycle, and mutable state; identity survives state changes.
- **Value** — an element type: an immutable, attribute-defined item;
  equality by value; no identity or lifecycle.
- **Service** — an element type: a stateless capability exposing
  operations; owns no state beyond what its contracts declare.
- **Event** — an element type: a schema'd payload crossing a boundary,
  with defined emission, ordering, and delivery semantics.
- **Protocol** — an element type: a capability seam — the contract an
  implementation must satisfy, defined independently of any
  implementation.
- **Implements** — the directed relationship *Design Element ⇒ Story*: the
  element handles (part of) the implementation the story calls for.
  Declared on the mandated `Implements:` line under each element heading;
  the word is reserved for this direction (a Story *builds or modifies* a
  Component Doc, never "implements" it).
- **Uses** — the directed, typed relationship *Design Element ⇒ Design
  Element* (DEC-0299): every dependency on another element is declared
  on the mandated `Uses:` line as a named contract item with an
  edge-type qualifier from the closed set `interface` (contract-only;
  non-serializing — consumer builds against stubs from the referenced
  items, which ship in its bundle; the default), `implementation`
  (requires the built artifact; the only qualifier constraining
  build-order), `test` (needed only at test execution; targets must be
  owned test-double elements, DEC-0306). "Atomic" means no
  *unspecified* dependencies, not no dependencies (DEC-0297).
- **Design-Complete** — the property of a Design Element whose typed
  contract obligations are fully met with no pending content; the unit the
  design percent-complete metric counts. A Story is design-complete when
  every element implementing it is design-complete.
- **Seam** — a Design Element consumed across component boundaries
  (consumed by more than one CMP, or independently versioned); seams
  graduate to standalone Component Docs carrying a `component-type`.
- **Component Invariant** — a numbered guarantee spanning multiple
  elements of one component (`C-<n>` items).
- **Implementation Constraint** — a normative, Decision-cited commitment
  binding the reference implementation (`IG-<n>` items in a CMP's
  Implementation Guidance section).
- **Implementation Note** — an advisory, possibly stack-specific hint in
  a CMP's Implementation Guidance section; never load-bearing — contracts
  must stand without it.

## Process

- **Refinement Session** — a 1:1 Q&A conversation in which the agent sharpens
  a participant's request through clarifying questions. Unsupervised: no
  technical facilitator is present.
- **Change Intake** — the mandatory protocol by which change intent enters
  a Groundwork project: restate-and-align loop, then a session (full or
  expedited), a mechanical fix, or idea capture. No semantic change to the
  corpus happens outside a session; off-record discussion producing no
  change is always allowed.
- **Mechanical Fix** — a change with zero semantic content (typo,
  formatting, reference repair) that alters no meaning and touches no
  contract line, decision text, status, approval field, or link
  semantics. Exempt from the session requirement; git history is its
  audit trail. When in doubt, a change is semantic, not mechanical.
- **Expedited Session** — a single-round intake session for small
  semantic changes: proposal restated, confirmed once, recorded.
  Compresses grilling only — every integrity step (distillation,
  consistency checks, recall audit, staleness cascade, checker) still
  runs.
- **Focus-Artifact Test** — the mid-session rule for tangents: a thought
  that changes the artifact under refinement is grilled now; one
  requiring a different artifact is parked (as an Idea, or a deferred
  Story/Spike when its level is already clear) and the session
  continues.
- **Synthesis** — the agent's merging of perspectives from multiple 1:1
  Sessions into a single artifact, surfacing cross-participant Conflicts.
- **Strategy Pack** — a versioned, plugin-like bundle (prompts, skills,
  tools, policies, context recipe) defining how the agent conducts one kind
  of session; PR-gated, model-agnostic, recorded in each session's
  provenance.
- **Decision Rights** — the governance-configured scope of decisions a
  role may accept in-session; statements outside a participant's rights are
  captured as proposals requiring ratification by the right holder.
- **Gate** — a human approval checkpoint an artifact must pass before it may
  feed the next pipeline stage.
- **Gate Policy** — the configured rule for who approves a gate: a fixed
  role-to-gate mapping or a committee requiring multiple roles.
- **Approver** — the named person whose sign-off passes a gate.
- **Contract-Complete** — the required property of a Component Doc: an
  implementer holding the doc plus the interface contracts of its dependencies
  (not their internals) can implement and test the component. Behavior, data,
  and API contracts are itemized and cite the Decisions behind them.
- **Impact Analysis** — walking the Graph Index from a changed artifact to
  find affected descendants (including in-flight work) and mark them Stale.
- **Stale** — status of an artifact whose upstream basis changed after
  approval. Stale artifacts block new downstream generation until re-ratified.
- **Re-affirmation** — the lightweight clearing of a Stale mark: the
  approver reviews the upstream diff plus impact report and re-approves via
  a small PR; full re-refinement happens only if re-affirmation is rejected.
- **Governance-as-Code** — the rule that roles, domain→approver mappings,
  and gate policies live as versioned, PR-gated files under `governance/`
  in the Canonical Store; host teams and branch protections are projections
  compiled from them.
- **Governance Event Log** — the gate engine's record of governance
  events (gate transitions, sweeps, conflict lifecycle, check activity)
  in two truth grades: provenance-grade entries mirror facts already
  landed in git or host history and reconverge on rebuild;
  telemetry-grade entries are dashboard-authoritative, lossy on rebuild,
  and never citable as provenance.
- **Drift** — divergence between a Projection and its canonical artifact
  (e.g., a direct Jira edit), detected by sync and reconciled toward canon.
- **Item Branch** — the git branch dedicated to one artifact's refinement,
  carrying the item plus its sessions and decisions; its PR to upstream main
  is the artifact's Gate, and merging it is approval.
- **Session Worktree** — the isolated git worktree in which one user
  session's changes accumulate before merging into the Item Branch (or a
  user-suffixed branch when versions diverge).
- **Mechanical Write** — a metadata-only or append-only mutation (stale
  mark, jira-key, transcript turn, counter) expressible solely as a typed
  storage-service operation; records a system fact and bypasses the human
  gate under machine verification, never carrying design content.
- **Provenance Chain** — Transcript → Decision → citation: the traceable path
  from any contract line back to who said what, when, and why.
- **Impact Link** — a directional, reciprocal link between same-type
  artifacts: "X impacts Y" means decisions recorded while refining X are
  expected to constrain, shape, or invalidate decisions in Y. Recorded as
  `impacts` on X and `impacted-by` on Y; the basis for ranking refinement
  order among siblings.
- **Inspired-by / Inspired** — a reciprocal link pair: an artifact
  inspired by a Research artifact carries `inspired-by` naming the RSCH,
  which carries the reciprocal `inspired` list. Permitted on Business
  Goals, Epics, Stories, Spikes, Ideas, and other Research artifacts;
  the first extension of the closed typed-link vocabulary (DEC-0009,
  DEC-0026) beyond its original set (DEC-0454).
- **Release** — a named scope of delivery declared in a Business Goal's
  Scope section, labeled by a Semantic Versioning prefix (`1`, `1.2`,
  `1.2.3`). A partial label is a scope, not a version: `1` means
  "somewhere in the 1.x.x line". Stories and Epics target a Release via
  the `release:` frontmatter field; absence means the current Release.
- **Deferred** — status of a Story, Epic, or Spike captured but
  intentionally out of the current Release. Deferred artifacts cannot pass a Gate and
  nothing derives from them; revival always lands at `draft`, re-earning
  the gate in current context. Deferral and revival each cite a Decision.
- **Backlog** — the reserved Release label for work that is wanted but has
  no target Release yet. Always valid without declaration; sorts after
  all named Releases.
- **Trigger** — a watched, human-testable condition in the tracked
  registry (`docs/TRIGGERS.md`) whose firing revives deferred work or
  starts new work. Statuses: armed (watched; the only entries loaded
  into agent context), fired, retired. Firing or retiring cites a
  Decision.
- **Artifact Interaction Surface** — the mandatory delegation surface
  (the artifact-librarian agent plus the artifact-interact skill)
  through which all agents interact with Groundwork corpora
  (DEC-0324/DEC-0325).

## Roles

- **Stakeholder** — a business participant who initiates ideas and answers
  refinement questions.
- **Product Owner** — approves Business Goals and Epics.
- **Engineering Lead / Data Science Lead** — refine and approve Stories,
  Spikes, and Component Docs.
- **Arbiter** — the person (often an Admin, product lead, or scrum master) to
  whom unresolved Conflicts escalate; assigns and overrides Approvers.
