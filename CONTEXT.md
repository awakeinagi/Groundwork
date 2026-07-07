# Groundwork Glossary

The ubiquitous language of the Groundwork system. Terms are canonical: docs,
code, UI copy, and agent prompts must use these words with exactly these
meanings. Resolve new or drifting terms here first (see
[SPEC-artifact-common](docs/specs/SPEC-artifact-common.md) for how the glossary
is gated).

## The system

- **Groundwork** — this system: a standalone application that refines business
  ideas into contract-complete Component Docs through gated, agent-facilitated
  refinement, with full provenance from implementation detail back to business
  intent.
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
- **Connector** — a pluggable adapter behind a defined API contract: Jira,
  codebase hosts (Bitbucket/GitHub), auth providers, doc storage.
- **Handoff Manifest** — the machine-readable package (component docs,
  contracts, dependency order) that Groundwork emits for an implementation
  swarm. Groundwork's southern boundary.
- **Implementation Swarm** — the set of AI agents and/or developers that build
  components from Component Docs. Out of Groundwork's scope; consumes the
  Handoff Manifest.

## Artifacts

- **Artifact** — any identified, versioned document in the Canonical Store:
  Business Goal, Epic, Story, Spike, Component Doc, Session, Decision,
  Conflict, Consolidation.
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
- **Conflict (CFL)** — a first-class record of contradictory or competing
  requests, linking the artifacts in tension. Blocks downstream generation
  until resolved.
- **Consolidation (CON)** — curated, derived reference material summarizing a
  frequently traveled path of the artifact graph, maintained for agent
  retrieval efficiency and invalidated when its sources change.
- **Participant Profile** — opt-in, per-person interaction memory (pacing,
  preferences, questions already covered) that improves repeat sessions;
  owned by its subject, who can read, edit, and delete it via the UI; never
  a home for org facts, which belong in artifacts.
- **Change Proposal (CP)** — a captured change proposed from outside the
  refinement pipeline (Jira drift, UI suggestion, implementation feedback),
  preserved verbatim and triaged by the agent into a mechanical fix, a
  refinement session, or an audited rejection.

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

## Roles

- **Stakeholder** — a business participant who initiates ideas and answers
  refinement questions.
- **Product Owner** — approves Business Goals and Epics.
- **Engineering Lead / Data Science Lead** — refine and approve Stories,
  Spikes, and Component Docs.
- **Arbiter** — the person (often an Admin, product lead, or scrum master) to
  whom unresolved Conflicts escalate; assigns and overrides Approvers.
