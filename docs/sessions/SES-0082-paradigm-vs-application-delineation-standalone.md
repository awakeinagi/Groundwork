---
id: SES-0082
type: session
title: "Paradigm vs application delineation — standalone skills, shared paradigm logic"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude (Fable 5)
transcript-fidelity: verbatim
kind: full
intake: {origin: user, proposed-by: awakeinagi}
overview: >-
  Full grilling session, now closed, delineating the Groundwork
  Paradigm from the Groundwork Application. A consolidated proposal
  was ratified as fifteen accepted decisions (DEC-0420 through
  DEC-0434), followed by four further items (DEC-0435 through
  DEC-0438) and two more selections (DEC-0439, DEC-0440) covering
  engine naming, corpus format-version location, host-identity
  governance mapping, BG-0002's naming, and this repository's own
  adoption stance — twenty-one accepted decisions in all. BG-0001,
  EP-0006, and EP-0008 were amended and re-affirmed per DEC-0267,
  with a mid-process correction restoring the stakeholder-seen
  wording verbatim before the re-affirmation was recorded as the
  content edit plus transcript naming alone. A five-term glossary
  landed in CONTEXT.md, groundwork.yaml and PARITY.md were created.
  Three Ideas were captured: IDEA-0056 (multi-repo code-linkage
  scenario), IDEA-0057 (dogfooding deferred), and IDEA-0058 (BG-0002
  possibly better chartered around the Groundwork Engine itself,
  with the governance- track question recorded inside it rather than
  split into a fourth Idea, answerable only by a future recharter
  session). The decision-recall audit was dispositioned against
  twenty-five ranked candidates, yielding nineteen
  precedent/enrichment links added and no contradictions or re-
  openings. The session closes with the commit to follow as the
  facilitator's own git duty per DEC-0333.
links:

  relates-to: [DEC-0420, DEC-0421, DEC-0422, DEC-0423, DEC-0424, DEC-0425, DEC-0426, DEC-0427, DEC-0428, DEC-0429, DEC-0430, DEC-0431, DEC-0432, DEC-0433, DEC-0434, IDEA-0056, DEC-0435, DEC-0436, DEC-0437, DEC-0438, DEC-0439, DEC-0440, IDEA-0057, IDEA-0058, IDEA-0059]
---

# SES-0082: Paradigm vs application delineation — standalone skills, shared paradigm logic

## Purpose

"Groundwork" currently names two things the corpus does not clearly separate: the Groundwork paradigm (the documentation-first design/doc method itself — gated artifact tree, grilling sessions, decision provenance — delivered as agent skills plus the gw tooling, adoptable standalone in any repo) and the Groundwork application (the centralized team-facing UI for managing the docs corpus that this project is designing and dogfooding the paradigm on). This session takes up the change-intake request to make that delineation explicit in the design documentation, with a hard requirement that the paradigm's agent skills work standalone — using the paradigm must never require hosting or running the application — and to treat the delineation as a standing design constraint (shared implementation of paradigm logic across skill-mode and app-mode, component reuse, DRY) rather than only a documentation reframing.

## Transcript

### T1 (stakeholder, verbatim proposal)

"We need to clearly delineate the use of the Groundwork documentation and design paradigm via agent skills vs the Groundwork application that we are dogfooding with the paradigm. The application is a centralized app to manage the docs across a team from a UI. The skill can be used outside of the application. In both cases, the design/doc paradigm is followed."

### T2 (stakeholder, verbatim addition, same intake)

"People should be able to use the agent skills without it being a requirement to host and run the application as well."

### T3 (facilitator, restatement, DEC-0255)

Restated the intent as: "Groundwork" currently names two things the corpus does not clearly separate — (1) the Groundwork paradigm, the documentation-first design/doc method itself (gated artifact tree, grilling sessions, decision provenance) delivered as agent skills plus the gw tooling, adoptable standalone in any repo; and (2) the Groundwork application, the centralized team-facing UI for managing the docs corpus that this project is designing and dogfooding the paradigm on. The change: make this delineation explicit in the design documentation, with a hard requirement that the skills work standalone — using the paradigm must never require hosting or running the application. The application is an optional, additive layer; both usage modes follow the same paradigm.

### T4 (stakeholder, verbatim confirmation and enrichment)

"Explicit in the corpus and to have the delineation in mind when we're designing the system and the agent skills. We want the system to use the paradigm but we must consider how things will work when using application vs without the application. How can we reuse components across both? How do keep things DRY so we don't have to maintain multiple copies of the paradigm logic? Help me elaborate on these concerns. What else should we be thinking about?"

### T5 (facilitator)

Alignment confirmed with enrichment — the delineation is both a corpus/framing change AND a standing design constraint (single shared implementation of paradigm logic across skill-mode and app-mode; component reuse; DRY). Intake path picked: full grilling session. Locate-first (DEC-0266) tasked in parallel; elaboration of the concern space to follow as the session's first substantive move.

### T6 (facilitator, locate-first findings + elaboration, DEC-0266)

Locate-first reported the delineation is absent and partly contradicted in the corpus. CONTEXT.md's glossary defines "Groundwork" as "a standalone application" and BG-0001 frames the whole system that way; no glossary term exists for the paradigm/method. DEC-0001 (accepted, foundational) states Groundwork is a standalone application and explicitly rejected a skills-first approach — a direct standing contradiction of the new standalone-skills requirement; candidate for narrowing (DEC-0346-style), not supersession, since its gated-refinement core survives. DEC-0338's "sacrificial by design" absorption triggers (method-track pieces retired as the application ships replacements) are in tension with permanent skill-mode; DEC-0346 partially defuses this (pattern permanent, implementation swappable). Supporting precedent: DEC-0263 (skill-only projects reuse governance files), DEC-0326 (only use of "Groundwork documentation paradigm" in the intended sense), DEC-0319 (per-skill install scripts); IDEA-0010 and IDEA-0013 (distribution/paradigm-export) are captured, disposition pending — this session sets their framing. The stakeholder's DRY/shared-implementation concern has no existing artifact; it is net-new.

Facilitator then elaborated the concern space: (1) the corpus format (markdown artifact tree + git) as the strongest DRY lever — if specified and versioned as THE contract, mixed-mode teams, app-down degradation, and zero-migration adoption/exit follow by construction; (2) paradigm logic lives at three layers that DRY differently — mechanics (already centralized in the gw CLI; the app backend should consume the same engine, never reimplement), process knowledge (currently prose in skill files; duplication risk — may need to become data/spec both surfaces load), governance config (already solved, DEC-0263); (3) concurrency as the meeting point — the app as "another writer against the same git corpus" keeps reuse high, whereas an app-private database as source of truth would fork the paradigm's storage semantics (most consequential fork to guard against); (4) an explicit parity/asymmetry matrix (shared semantics vs app-only team features vs skill-only terminal facilitation); (5) version-skew story (corpus-format version, engine version, stale installed skills vs newer app); (6) conformance testing, distribution (IDEA-0010/IDEA-0013), and whether this repo deliberately stays skill-mode-only as the dogfood of the standalone path. Recommended a discretionary system-architect dual-instance consultation before decision distillation.

### T7 (stakeholder, verbatim)

"Yes, let's consult the architects. But it is recommended that both of them read the docs on agent skills (agentskills.io and Claude's docs https://code.claude.com/docs/en/agents) to get a clear picture of what's possible. Maybe it would be better to spawn a research agent (inherit your model) first to compile all of the information and then share the same source material with both architects so they're working with the same information."

### T8 (facilitator)

Ratified. A research agent (inheriting the facilitator's model per the stakeholder's instruction) is compiling a shared briefing packet from agentskills.io and the Claude Code agents/skills docs, with per-claim citations. The identical packet will be provided to both system-architect instances (record-grounded and best-practice-independent) per the DEC-0293 debate protocol, so both argue from the same source material. Consultation question: how to deliver the paradigm both as standalone skills and inside the centralized application while keeping paradigm logic single-sourced.

### T9 (facilitator, research packet delivered)

The research agent compiled the shared agent-skills briefing packet from agentskills.io (specification, using-scripts, best-practices pages) and the official Claude Code docs (agents, sub-agents, skills, plugins, discover-plugins), roughly 2400 words with per-section citations. Key verified facts: a skill is a directory of SKILL.md (YAML frontmatter plus Markdown body) plus optional scripts/references/assets — instructions and files, not a hosted service; three-stage progressive disclosure (metadata at roughly 100 tokens always loaded, body under 5k tokens on activation, bundled resources on demand); bundled scripts execute without entering context and may self-declare dependencies (PEP723/uv, npx, deno, bun); the open spec defines no versioning, distribution, or service semantics — those are Claude-Code-specific (plugins via .claude-plugin/plugin.json, marketplaces, version-bump-or-git-SHA update semantics, bin/ executables, hooks); Claude Code extensions (dynamic context injection, context:fork, skills preload) do not travel to other hosts; subagents are .md files with first-class tool restriction and model pinning; skills can bundle and invoke CLI tools, so shared logic can live in a CLI or library a skill wraps and an app backend calls. Unverified items were marked (client list page is JS-rendered; deeper plugin-reference pages were not fetched). The identical packet was given to both architect instances.

### T10 (system-architect, record-grounded instance, DEC-0293 opening position)

Recommends library-first with adapter shells: the gw engine refactored into a Python library (artifact CRUD with the DEC-0391 lock model, ID allocation, graph sync, checker, governance evaluation per DEC-0263, format validation), with the gw CLI and the BG-0001 app backend both thin in-process adapters over it (hexagonal ports-and-adapters; no service, since a service would violate the no-hosting requirement; no subprocess CLI calls from the app). Git-backed markdown remains the sole primary store for both modes; the app's database is strictly a derived, read-optimized projection rebuilt from the canonical file tree; the app's write path goes through the library to files under the DEC-0391 lock. Process knowledge (grilling/intake/gate playbooks, currently prose in skill files) should be extracted into structured machine-readable definitions both modes consume — flagged as the hardest problem, ungrilled, needing its own DEC-0335 intake plus a DEC-0336 boundary ruling on whether execution-driving process definitions fall within BG-0002's admission predicate. Recommends a deliberate documented asymmetry, skill-mode as the core subset and the app as the superset ("if you can do X in skill-mode, you can do X in the app with the same corpus outcome"), maintained as a parity-matrix fitness function. Version skew is governed by the corpus format as a slow-moving backward-compatible contract (format-version marker; additive-only evolution; breaking changes need a migration tool and a DEC). Distribution via the IDEA-0010 plugin with explicit versioning bundling skills, agents, gw CLI, process definitions, governance seeds (DEC-0263), and install scripts (DEC-0319); consumers track rather than fork, with customization via process-definition overrides. Proposes record reconciliations: DEC-0001 narrowed rather than superseded (its business-users-need-a-UI rationale stands; standalone delivery is additive); DEC-0338/DEC-0346 absorption triggers reinterpreted so they retire specific subagent implementations, never skill-mode itself, with the library and CLI adapter persisting (a TRIGGERS.md text repair). Notes library extraction likely needs an EP-0009 scope amendment or its own epic.

### T11 (system-architect, best-practice-independent instance, DEC-0293 opening position)

Independently recommends the same four-component decomposition: a groundwork-core library with no I/O opinions and an abstract corpus port, the gw CLI as its first consumer with a git-filesystem adapter, an agent-skill package wrapping the CLI, and an app backend importing the library directly. Shares the record-grounded instance's positions on corpus format as a versioned consumer-driven contract, a structured playbook format with prose and UI as generated views (decidable parts structured, judgmental facilitation stays prose), a parity matrix, and three-dimensional version management (format version as the compatibility contract; skills declare compatibility; explicit plugin versioning, never per-commit auto-update), plugin distribution bundling the CLI in bin/, and portable-spec authoring with a generic fallback for non-Claude-Code hosts. Its sole material divergence: recommends the app NOT be a second writer on the git corpus — app-private PostgreSQL as runtime storage with import/export roundtrip fidelity enforced by CI, arguing exclusive data ownership, git-as-database impedance mismatch for multi-user web apps, and a portable-vs-ephemeral feature classification.

### T12 (facilitator, rebuttal round 1 relay and outcome)

Each instance received the other's position with targeted pressure points. Independent instance verdict: amend — concedes git-primary for v1 (the verified DEC-0391 lock model, the single-writer v1 charter with armed scale triggers, low write frequency, and the mixed-mode-team scenario dissolve its objections; its own import/export model would have created a dual-write sync problem strictly harder than the one it avoided). It holds that the corpus-access port abstraction must be ratified now as architectural insurance making git-primary reversible, and newly surfaces that the git remote/sync topology (canonical repo hosting, serializing laptop-clone pushes against app writes) is outside the local lock's jurisdiction and must be an explicit v1 commitment; flags projection-rebuild latency and real-time co-editing as design points. Record-grounded instance verdict: amend — git-primary holds, but acknowledges the same DEC-0391 scope gap (local lock only); the fix is extending the coordination layer, not adding a second data store — the app is architecturally another git client (pull, write under lock, push, retry-on-conflict optimistic concurrency; version tokens force re-reads on rebased sections). Proposes SP-0018 as the vehicle for the multi-machine coordination design, scoped to v1 single-instance (TRG-0001 armed for multi-node); steelmans git-primary's honest costs (no sub-file real-time co-editing, mitigated by flush-on-save; cross-machine locks deferred to TRG-0001; large-corpus git scaling addressed via shallow/sparse options; backup via git hosting). Convergence was reached after one round; no second rebuttal round was needed. The converged proposal goes to the stakeholder for ratification.

### T13 (stakeholder, responding to the converged architecture proposal's flagged question on git remote/sync topology)

"For (1), I think what it may look like is the app has a local repo like any other user. The remote becomes the consensus location with ground truth role and authorization configs per user. PRs are the mechnism for approval. But how do we manage that from the app? How do we manage that in the case of a bunch of users in a project only using the agent skills? Additionally, I would like to add that if a team uses the app for a repo, there would only be one instance of the app for the repo that everyone works through."

### T14 (facilitator, analysis of the stakeholder's topology proposal, distilled)

Restated the proposed topology: the git remote is the canonical consensus store; the app is one instance per repo, holding its own clone like any other git client; all app users work through that single instance; per-user authorization lives at the remote; PRs are the approval mechanism. Noted what the single-instance constraint buys: all app-mediated writes serialize through the one instance's DEC-0391 local lock, so the app-side concurrency story reduces to the already-verified model, and the remote-coordination problem reduces to standard multi-clone git (app clone plus skill-mode users' clones against one remote). Flagged the design forks this opens, to be grilled: (1) PR granularity — recommended branch-per-session with the PR opened at session close, since the session is the paradigm's atomic semantic unit (DEC-0252) and the checker validates whole-tree consistency; (2) which act constitutes THE approval — recommended the in-corpus frontmatter approval remain the paradigm's portable record (the paradigm core must not hard-depend on a git host — PRs are a host feature, not git itself), with PR merge plus branch protection as the team-mode enforcement layer that guarantees only authorized approvers can land gated changes; PR-based approval becomes a governance-selected policy (team mode) rather than paradigm core, and solo god-mode keeps direct commit; (3) governance-to-host mapping — governance-as-code YAML should be the source that projects into host-side branch protection and review requirements (derived, one direction), not a second hand-maintained auth config; (4) app-side mechanics — the app integrates via a git-host application installation with per-user OAuth identities so approvals and merges are attributed to real users; the app renders PRs in paradigm terms (artifacts, decisions, gates, not raw diffs); (5) skill-only teams run the same protocol without the app — the facilitator agent branches per session, pushes, opens the PR via the host CLI, the gw checker runs in CI as a required status check, branch protection encodes approver authority, and review/merge happens on the host or via the approver's own agent session; (6) a newly concrete problem — sequential per-prefix ID allocation collides across parallel session branches (two branches both allocating the same next DEC or SES ID); candidate solutions (remote ref reservation, merge-time renumbering, app-as-allocator-when-present with git-native fallback) belong in SP-0018, which both architects already named as the vehicle for the multi-machine coordination design. Grilling questions on forks 1, 2, and the single-instance constraint's implications were put to the stakeholder along with these recommendations.

### T15 (stakeholder, verbatim)

"I like your recommendations. But let's run them by the architects for one more round of debate."

### T16 (facilitator, rebuttal round 2 relay, final per the DEC-0293 two-round cap)

Relayed rebuttal round 2 (final, per the DEC-0293 two-round cap) to both architect instances: the stakeholder's topology (remote as canonical consensus with per-user authorization; app holds a local clone like any other user; PRs as the approval mechanism; NEW constraint — exactly one app instance per repo that all app users work through) plus facilitator recommendations R1 (branch-per-session, PR at session close), R2 (frontmatter approval as the portable record, PR merge plus branch protection as team-mode enforcement, solo god-mode keeps direct commit), R3 (governance YAML projects one-way into host branch protection), and the deferral of ID-allocation to SP-0018. Both instances were instructed to attack, not rubber-stamp, with named pressure points (long-lived/stale session branches, shared-surface merge conflicts, mid-session approval visibility, approver-vs-merger mismatch, approved-but-unmerged limbo, bare git remotes without PR features, single-instance SPOF, ID collisions under parallel branches).

### T17 (stakeholder, via the /ponytail skill invocation, verbatim)

"As a senior engineer do you have any suggestions?"

### T18 (facilitator, senior-engineer/YAGNI lens, in response)

Suggested the session's decisions be phrased as standing constraints, not build mandates — constraints are free forever, mandates create work queues with zero current consumers. Specifically: (1) structured process-definition extraction is the proposal's biggest premature-build risk — a DSL with no consumer until the app's facilitation engine exists; keep prose canonical and extract when that work starts, gate checklists first; (2) library extraction should not be scheduled now — record "no paradigm logic outside the engine" and extract when the first non-CLI consumer appears; (3) governance-to-host projection tooling waits for the first real multi-user team — the host's native branch protection plus CODEOWNERS plus required CI already is the enforcement layer; (4) the ID-collision fix can be a one-liner (first-push-wins reservation ref on the remote) rather than a three-option study; (5) the parity matrix is a markdown table in a doc, not automation. None of this changes the converged architecture — it only sequences when things get built.

### T19 (system-architect, best-practice-independent instance, round-2 verdicts, distilled)

R1 endorse with caveats — trunk-based-development wisdom about short-lived branches targets fast-moving codebases and is weak here, but two rules are required before ratification: long-lived sessions rebase at defined points (or checkpoint-merge past a threshold), and cross-session-referenced artifacts must be merged to main first (foundational sessions close before dependents open); mid-session approvals staying invisible until close is correct, avoiding phantom dependencies on unmerged state. R2 endorse with one required CI rule — frontmatter approved-by must match someone with merge authority, else the dual record is a liability rather than defense-in-depth; approved-but-unmerged is a non-problem (approval frontmatter only exists on the branch; abandoned branch equals abandoned approval). R3 amend — governance policy carries an explicit enforcement-level field (full, basic, or solo) and the checker warns when policy demands enforcement the host capability cannot provide. Single-instance endorse as v1 — resolves its round-1 multi-writer concern (one instance, one clone, the verified lock covers all app writes); SPOF is proportionate for a documentation system since CLI users keep working during outages; pre-armed trigger for multi-instance if outages block teams. ID-allocation deferral object — under R1, two concurrent users minting the same sequential ID is the default day-one outcome; proposes team-mode app-owned allocation (one instance, one monotonic counter) now, a spike for harder cases later.

### T20 (system-architect, record-grounded instance, round-2 verdicts, distilled)

R1 amend with three recorded constraints — (1) shared append surfaces (CONTEXT.md, TRIGGERS.md, SPECs) will merge-conflict across parallel sessions; a structured-markdown conflict strategy is a design constraint and the checker must run on the post-merge result in CI, not just the branch; (2) cross-session derivation binds to main-branch state ("only approved artifacts feed the next stage" means approved-on-main), with dependent sessions sequenced or explicitly branch-chained; (3) rebase-before-PR with post-rebase re-validation is a mandatory session-close step. R2 endorse — architecturally clean; merger-vs-approver handled by projected branch protection or a CI fallback check; approved-but-unmerged is just an abandoned branch (main is ground truth, no new checker rule); DEC-0136 graduation is orthogonal. R3 amend — the degraded mode must be named: bare git (today's baseline — agent discipline per DEC-0326 plus post-commit checker; DEC-0263 solo god-mode is this level), basic host (PR-required), full host (API-projected protection); enforcement follows host-capability level. Single-instance endorse — BG-0001 System Context already specifies v1 as single-process single-writer with TRG-0001 armed for multi-node; exact alignment, no record conflict. ID-allocation deferral object — ratifying R1 without an ID strategy ratifies a known-broken workflow; options: (a) app-held monotonic counter with a git-ref/remote-lockfile fallback for skill-mode (simplest, fits single-instance), (b) merge-time renumbering (rejected — breaks in-branch citations), (c) session-scoped IDs normalized at merge (skill-mode fallback only). Either decide ID allocation with R1 or defer R1 itself.

### T21 (facilitator, debate closed, consolidated proposal)

The two instances converged on every item — R1 ratifiable with the union of their constraints (shared-surface conflict strategy plus CI-on-merge-result; derivation binds to main with sequencing/chaining; mandatory rebase and re-validation at PR; mid-session approvals visible only at merge), R2 ratifiable with the approver-merger match enforced (branch protection at full capability, CI check otherwise), R3 ratifiable with a three-level host-capability/enforcement-level field in governance policy where bare-git/solo is the honored baseline not a failure mode, single-app-instance-per-repo ratifiable as v1 topology aligned with BG-0001/TRG-0001, and — the debate's one hard correction to the facilitator — ID allocation must be decided in this session, not spiked: consolidated recommendation is app-as-allocator in app-managed repos plus a git-native first-push-wins reservation ref for skill-only multi-user repos, solo mode unchanged, with SP-0018 detailing mechanics and edge cases (offline allocation, retry semantics) rather than choosing the model. The consolidated proposal, restated through the T18 constraints-not-mandates lens, was put to the stakeholder for ratification.

### T22 (stakeholder, responding to the consolidated proposal's ID-allocation item, verbatim)

"What if we use the equivalent of a develop branch? Changes are proposed there and PR is merged, but when changes go to main IDs, etc. are reconciled. Similar to what has to happen with a CHANGELOG file before the next version is known."

### T23 (facilitator, analysis, distilled)

Identified the stakeholder's proposal as the merge-time-normalization family — the grounded architect's option (c), provisional/session-scoped IDs normalized at a serialization point — with the normalization point moved to a develop-to-main promotion. Named its core insight: sequential IDs require exactly one serialization point, and the only real question is when — at mint time (the reservation-ref model: the remote serializes, final IDs land immediately, no rewrites ever, but requires connectivity at mint) versus at promotion time (provisional IDs need no coordination, fully offline-friendly minting, but require a reconciliation rewrite at promotion). Flagged where the CHANGELOG analogy breaks: a changelog's Unreleased section has no inbound references, while Groundwork IDs are dense reference targets from the moment they are minted — bare-ID cross-references in body prose (DEC-0242), frontmatter links, session transcripts, and commit messages all cite an ID immediately, so promotion-time reconciliation would have to mechanically rewrite all of them, including CLOSED session transcripts and accepted decisions, colliding with the append-only and immutability invariants and weakening verbatim-transcript trust (post-close content hashes would change), while git history would retain dead provisional IDs in the audit trail regardless. Noted the two concerns are separable: a develop branch as an integration/QA buffer is orthogonal to ID reconciliation — a team can adopt a develop branch without renumbering, and the reservation-ref model works with or without one. Recommended keeping first-push-wins reservation (final IDs at mint) as the primary model, and documenting provisional-IDs-with-promotion-reconciliation in SP-0018 as an explicit offline fallback mode only if disconnected minting turns out to be a real requirement. Put a grilling question to the stakeholder: is offline/disconnected session work — minting artifacts with no reachable remote — a scenario the design must serve?

### T24 (stakeholder, verbatim)

"Approach the architects again with the previous consolidated proposal as the standing winner but mention my changelog analogy and see if they think it's worth considering. I think you're right in your assessment but let's see if we get any new insights."

### T25 (facilitator, supplementary consultation, distilled)

Ran the stakeholder-directed supplementary consultation as a focused question to both architect instances, distinct from the closed two-round DEC-0293 debate, with the T21 consolidated proposal standing as the winner throughout. Each instance received: the stakeholder's verbatim T22 develop-branch/CHANGELOG proposal, the facilitator's T23 assessment (the analogy breaks on inbound-reference density; promotion-time reconciliation would rewrite closed transcripts and accepted decisions against the append-only and immutability invariants; develop-as-integration-buffer is separable from ID reconciliation; offline/uncoordinated minting is the reconciliation model's one unique win), and an explicit invitation to overturn the assessment. Each was asked to answer verdict-first — ADOPT, DOCUMENT-AS-FALLBACK, or REJECT — with four specific probes: reconciliation designs that never touch closed content (alias/redirect maps, or session-close-time ID assignment that shrinks the provisional window); whether the record's append-only and immutability invariants make reconciliation harder or easier than the T23 assessment judged; industry precedents for late ID binding; and whether a develop-to-main promotion step carries an ID-independent batching or release benefit (corpus releases, format-version stamping at promotion) worth capturing separately from the ID-allocation question.

### T26 (system-architect, best-practice-independent instance, supplementary verdict, distilled)

DOCUMENT-AS-FALLBACK — the facilitator's assessment is correct and nearly complete. Partial mitigations examined and found insufficient: session-close ID assignment shrinks but does not eliminate the provisional window (within-session cross-references still use provisional IDs; any cross-session reference to a provisional ID reintroduces the corpus-wide rewrite); alias/redirect mapping avoids mutating closed content but creates a permanent, monotonically growing indirection layer every ID-processing tool inherits — a usability regression where prose IDs stop matching files. Industry precedent: distributed systems that solve late ID binding well (Fossil content hashes, Jira server-receipt assignment, UUIDs/CRDTs, git SHAs vs server-assigned PR numbers) all do it by NOT using sequential IDs for distributed minting — sequential IDs and distributed minting are fundamentally in tension, and the proven pattern separates the distributed identifier from the sequential one, which is exactly what reservation-at-mint does. Independent finding: the develop-branch topology has real ID-independent value as corpus RELEASE semantics — batch sessions, run the full checker across combined changes, stamp a corpus format version, promote to main as a coherent validated snapshot consumer projects can pin — worth capturing as a governance-topology option separate from ID allocation.

### T27 (system-architect, record-grounded instance, supplementary verdict, distilled)

DOCUMENT-AS-FALLBACK — the facilitator's assessment if anything UNDERSTATES the difficulty. All three no-rewrite reconciliation routes are blocked by the record: (a) session-close assignment fails because decisions cross-reference each other mid-session (e.g., DEC-0346 citing DEC-0338 from the same session arc) — no window exists where IDs lack inbound references; (b) alias files add permanent indirection the bare-ID prose convention (DEC-0242) cannot pass through — unstructured "per DEC-0418" prose refs hit no resolver today, so alias-awareness is a permanent tax on every tool for a temporary problem; (c) session-scoped provisional prefixes leave either a rewritten historical transcript or two ID forms coexisting permanently. Three additional record constraints the facilitator had not cited: SPEC-artifact-common declares every artifact ID immutable (reconciliation by definition mutates it) and IDs never reused even for deletions (provisional numbers are burned permanently), and SPEC-decision makes accepted decisions immutable including their in-content ID; commit messages carrying IDs cannot be rewritten without force-push. Concurs the develop→main topology is independently valuable standard release engineering (stable consumer snapshots, format-version stamping at promotion, integration-checking before release, batched rather than per-session consumer churn) and should be captured in SP-0018 as a separate concern.

### T28 (facilitator, supplementary consultation closed, final consolidated position)

Unanimous DOCUMENT-AS-FALLBACK. The ID-allocation item of the consolidated proposal is finalized as: reservation-at-mint is the primary model (the single app instance allocates in app-managed repos; a git-native first-push-wins reservation ref serves skill-only multi-user repos; solo mode unchanged); provisional-IDs-with-promotion-reconciliation is documented in SP-0018 strictly as the offline/disconnected fallback with its costs named (burned ID space, alias indirection or transcript rewriting, collision with the immutability invariants); and — the supplementary round's genuinely new capture, credited to the stakeholder's CHANGELOG intuition — the develop→main branch topology is recorded as an independently valuable, optional corpus-release governance pattern (batched validated snapshots, format-version stamping at promotion) separable from ID allocation, to be captured in SP-0018's scope as its own concern. The complete consolidated proposal (delineation and naming; single-sourced paradigm logic; git-primary storage with ratified corpus-access port; remote-as-consensus topology with one app instance per repo; branch-per-session PR protocol with its three constraints; frontmatter-record/merge-enforcement approval with enforcement levels; ID allocation as above; deliberately-deferred items recorded as constraints not build mandates) now awaits stakeholder ratification in full.

### T29 (stakeholder, verbatim)

OK please give me a detailed explanation of the final ratification package. Explain how will work in detail for 3 cases: 1) Users running sessions in the app via the UI 2) A single god-mode user like I am using it today 3) Multiple users only using the agent skills, no app. Give me examples and flow diagrams of what each scenario looks like.

### T30 (facilitator, distilled)

Walked the stakeholder through the final ratification package as three concrete operating scenarios with named-actor examples and flow diagrams: (1) team-via-app — one app instance per repo holding its own clone, per-user host OAuth identities, app-counter ID allocation, branch-per-session with app-driven rebase/checker/PR at close, approver reviewing in paradigm-rendered UI, merge under projected branch protection with CI gw-check, projections refreshed from main; (2) solo god-mode — today's baseline: direct-to-main commits, file-sequential IDs (single writer), frontmatter-only approval, agent discipline + checker as the honored solo/bare enforcement level, zero-migration path to the other scenarios; (3) multi-user skill-only — per-user clones with the skills plugin, first-push-wins reservation refs for IDs, branch-per-session with rebase+re-check+PR at close via host CLI, approval enforced by branch protection/CI approver-match at basic capability degrading to agent discipline on bare remotes, derivation binding to main. Emphasized the parity core identical across all three (corpus format, engine semantics, checker, approval record, governance file) making the scenarios freely interchangeable states of the same repo rather than different products.

### T31 (stakeholder, verbatim)

Ratified. Please log the decisions. But I have a few more things to discuss before we close.

### T32 (facilitator)

Ratification recorded. The consolidated proposal is distilled into the decision records listed in this session's Decisions Produced section, each accepted on the strength of the T31 ratification. The session remains open for the stakeholder's further topics; the closing machinery (recall audit, corpus edits with their cascade, checker, commit) runs at session close.

### T33 (stakeholder, verbatim)

"Based on this discussion, I think we need: 1) Make sure our artifacts' frontmatter supports multiple approvals 2) Define configs for approver groups by artifact type (BG type assigned a group of approvers, EP a group of potentially different users, ST, etc.), approver groups by artifact ID i.e. a group for `EP-0123`, etc. 3) For the multi-user, skills-only scenario, a push button way to update the IDs on conflict (someone got changes in before you and now you need to increment the IDs for your artifacts)"

### T34 (facilitator, analysis and recommended shapes, distilled)

All three extend the ratified package without contradiction.

(1) Multiple approvals: recommended an additive `approvals:` list in frontmatter (entries of by/on/optional role), legal under the DEC-0425 additive-evolution contract; the legacy approved-by/approved-on pair stays valid and reads as an approvals-list of one, so no migration; the checker validates the list against governance policy; solo mode unaffected.

(2) Approver groups: recommended a governance-as-code schema extension (DEC-0263 lineage) — named groups defined once, per-type gate policies mapping artifact types to groups, per-artifact-ID overrides with ID-specific beating type-level; at full enforcement groups project into host required-reviewer config (DEC-0429), at basic a CI check counts frontmatter approvals against policy, at solo everything resolves to the operator unchanged. Open call put to the stakeholder: quorum semantics — recommended each policy entry declares `require: any | all | k`, defaulting to `any` (today's single-approver behavior; nothing tightens until a team opts in).

(3) Push-button ID renumbering: recommended a `gw renumber` recovery tool scoped strictly to unmerged branch content — detects branch-minted IDs colliding with main after a rebase, reserves fresh IDs through the normal DEC-0430 reservation mechanism, rewrites references only within the branch's own diff (including its not-yet-published session transcript), re-runs the checker. Distinguished from the rejected promotion-time reconciliation: renumbering unpublished branch content violates no immutability invariant (analogous to rebasing unpushed commits); hard rule proposed — the tool never touches anything already on main. Positioned as the recovery complement to DEC-0430's prevention (reservation-at-mint).

The three shapes, including the `any` quorum default and the never-touches-main rule, await stakeholder confirmation before distillation.

### T35 (stakeholder, verbatim)

And I want to add a clarification for "one application instance per repository"; I mean one application instance per Groundwork docs repo. The software built from the Groundwork docs could be spread across multiple "code-only" repos; though that code would need to be linked back to the Groundwork repo. This is a more complicated scenario that we should flesh out in a future session. But let's put it on the radar.

### T36 (facilitator, scoping)

The clarification is recorded as follows. DEC-0426 is accepted and immutable; its text is not amended. In DEC-0426, "repository" means the Groundwork docs repository (the corpus repo) — the single application instance serves the corpus, and this reading is consistent with the decision's context (the instance holds a clone of the corpus and participates as a git client against the corpus's canonical remote). The larger scenario the stakeholder raises — implementation code spread across multiple code-only repositories, each linked back to the governing Groundwork docs repo — is genuinely new design territory (cross-repo linkage, provenance from code back to contracts, possibly per-code-repo tooling) and is parked on the radar as a captured Idea per DEC-0258/DEC-0260 rather than extending this session; the Idea is cross-referenced below as IDEA-0056. A small clarifying decision pinning the "repository = Groundwork docs repo" reading to DEC-0426 was proposed to the stakeholder for confirmation alongside the three pending items from T33/T34.

### T37 (stakeholder, verbatim)

"Confirmed. And just to add more color, I clarified that the app is tied to the Groundwork repo because we could be managing a larger project with many apps, libraries, etc. that all fall under the larger projects umbrella."

### T38 (facilitator)

Confirmation recorded for the four T34/T36 items; each is distilled below as an accepted decision. The stakeholder's added color — one umbrella project may comprise many apps and libraries in their own repositories, all governed by the single Groundwork docs repo its application instance serves — is folded into the DEC-0426 clarifying decision and enriches IDEA-0056's context.

### T39 (facilitator)

Close-out grilling round one (mechanics). Four questions, each with a recommendation. (1) What is the glossary-canonical name for the DEC-0423 single-sourced engine? Recommended: "Groundwork Engine". (2) How is BG-0001's conflating "standalone application" framing handled at close-out, given the DEC-0267 cascade obligations? Recommended: a minimal narrowing edit, with cascade and re-affirmation handled in-session; BG-0002 left untouched. (3) What disposition mode applies to the thirty-five consistency-sweep-flagged citers? Recommended: bulk review with batch approval. (4) Does close-out create the initial DEC-0433 parity-matrix document? Recommended: create a minimal stub now.

### T40 (stakeholder, structured answers, selections verbatim)

"Groundwork Engine (Recommended)"; "Minimal narrowing edit (Recommended)" for BG-0001 with cascade and re-affirmation in-session, BG-0002 untouched; "Bulk review, batch approval (Recommended)" for the sweep-flagged citers; "Create minimal stub now (Recommended)" for the parity matrix.

Stakeholder aside (verbatim): "Sorry I should have said another grilling round within this same session"

### T41 (facilitator)

Grilling round two (open ambiguities). Four questions, each with a recommendation. (1) Where does the DEC-0425-mandated corpus format-version marker live? Recommended: a root manifest file. (2) How are governance-keyed people, given team-mode enforcement, matched to git-host identities? Recommended: email plus a host-identity map. (3) Does BG-0002's "Method Track" name still fit under the new Paradigm/Application glossary? Recommended: keep the name. (4) Does this repository adopt the Application when it exists, or stay skill-mode-only as the standalone dogfood? Recommended: defer until the app exists.

### T42 (stakeholder, structured answers, selections verbatim)

"Root manifest file (Recommended)"; "Email + host-identity map (Recommended)"; "Keep the name (Recommended)"; "Defer until the app exists (Recommended)".

### T43 (facilitator)

Round-two distillation. Two selections are decisions, recorded below as accepted on the T42 confirmations. Two are dispositions: BG-0002's "Method Track" name is kept — the glossary defines Paradigm, Application, and Method Track as three distinct terms and no BG-0002 edit occurs; the dogfooding stance for this repository is deliberately deferred until the Application exists and is captured as an Idea so it stays on the radar. Close-out now commences: bulk citer review, recall audit, the mandated corpus edits (CONTEXT.md glossary, BG-0001 minimal narrowing with cascade, TRIGGERS.md repair per DEC-0422, parity-matrix stub, root manifest), checker, and commit.

### T44 (stakeholder, verbatim)

"Approved. Do we need any new goals or epics based on what we worked on this session?"

### T45 (facilitator)

Batch approval recorded. Sweep dispositions per the bulk review: thirteen citers CONSISTENT as reviewed — CMP-0010 and ST-0057 (correctly scoped "Groundwork's standalone application"), CMP-0011 and ST-0058 ("ships as" delivery rationale), EP-0009 and SP-0013 through SP-0017 (DEC-0336 cited only for its sizing yardstick), BG-0002's DEC-0263 and DEC-0336 citations (text already matches the new decisions), CMP-0004, CMP-0008, CMP-0015 (DEC-0136 cited for element graduation, unrelated to DEC-0428). BG-0002 and EP-0009 confirmed needing no edit under DEC-0422 — both already carry the implementations-not-pattern trigger language from DEC-0346. BG-0001 takes the minimal narrowing edit at its three conflating passages, with EP-0006's echoing sentence and EP-0008's quoted Intent fragment aligned in the same batch so the DEC-0267 cascade completes in-session. Structural assessment for the stakeholder's question delivered in-conversation: no new goals or epics — by this session's own decisions the deferred tracks create their homes when their consumers appear, with SP-0018's grown scope and a possible future team-mode epic noted.

### T46 (stakeholder, verbatim)

"Reaffirmed"

### T47 (facilitator)

Re-affirmation stamped on BG-0001, EP-0006, and EP-0008 per DEC-0267 (the narrowing amendments of this session's batch). The decision-recall audit now runs as the final required stage step; its findings and dispositions will be recorded before close.

### T48 (facilitator)

Process correction recorded. After the stakeholder's T46 re-affirmation,
a librarian task instructed only to stamp the re-affirmation
additionally re-edited BG-0001, EP-0006, and EP-0008, leaving
on-disk wording the stakeholder had never seen. The facilitator
detected the discrepancy, and the re-affirmed wording of all three
artifacts has been restored verbatim; the re-affirmation therefore
attaches to the text now on disk. The DEC-0267 re-affirmation record
convention is confirmed as: no status transition, the sanctioned
content edit itself, plus the session transcript naming the
re-affirmation (T46-T48).

### T49 (stakeholder, verbatim)

"Approved"

### T50 (facilitator)

Recall-audit findings and dispositions recorded. Three Sonnet 5 judge shards evaluated the twenty-five ranked candidates; seventeen were judged embedding noise and eight material. Dispositions, approved by the stakeholder at T49: (1) DEC-0265 — the pre-existing git-mediated, PR-carried, frontmatter-recorded multi-party governance model for skill-only mode; DEC-0427 and DEC-0428 FORMALIZE and extend DEC-0265's model rather than duplicating it, and now carry relates-to links to it. (2) DEC-0310 — the artifact-interact-owns-tooling / design-session-as-pure-method split is the direct architectural precedent that DEC-0423's single-sourced engine and DEC-0432's process-knowledge deferral formalize; links added from DEC-0423, DEC-0432, DEC-0433. (3) DEC-0036's two-layer enforcement model (host branch protection plus service-computed checks) is prior art for DEC-0429/DEC-0436; links added. (4) DEC-0234 — the approver-group and identity-mapping configuration of DEC-0436/DEC-0440 likely belongs in or beside CMP-0016's existing RoleResolution service when built; recorded as a design pointer, links added. (5) DEC-0174 — CMP-0009's GitHub-App identity pattern is working prior art for the application instance's host-identity design; links added from DEC-0426, DEC-0428, DEC-0440. (6) DEC-0416 with DEC-0394 — the session's reliance on "the verified DEC-0391 lock model" now traces to DEC-0416 (the verifying decision); links added from DEC-0424, DEC-0427, DEC-0430; DEC-0394's interim single-writer rule noted as the constraint those decisions' multi-writer topology must retire on its own terms. (7) DEC-0172 — GitHub Cloud is the ratified v1 code host grounding DEC-0429/DEC-0440's host abstractions; links added. (8) DEC-0315 — per-write targeted validation with the full checker at gate/commit level is the existing validation architecture behind DEC-0423's engine and DEC-0429's CI clause; links added. Audit outcome: no contradictions, nothing re-opened; all eight are precedent/enrichment links.

### T51 (stakeholder, verbatim)

"This dogfooding exercise has been very helpful in refining the trajectory for Groundwork. Looking back, I feel like I jumped the gun a bit in deciding for a full application from the start. I'm really seeing the benefit of the agents and skills working with methodology. The application itself really is mostly a presentation layer around the Groundwork Engine. Toward that realization, I'm starting to think that BG-0002 may be better suited to track the development and refinement of the Groundwork Engine itself as the core technology to work on, even if an application with a UI may have its own merits. Since BG-0002 is still relatively new, I think it might not be too hard to change its focus. What are your thoughts?"

### T52 (facilitator)

Per DEC-0261, this inspired idea does not extend the closing session; it is captured verbatim as IDEA-0058 and joins the work queue for its own intake session. Facilitator's assessment given in-conversation: the session's own decisions already point this direction — DEC-0423 made the Engine the architectural center; DEC-0433 made skill-mode the core subset; DEC-0421 and DEC-0422 completed BG-0002's drift from sacrificial scaffolding toward permanent first-class delivery — so re-chartering BG-0002 as the Engine's home is the logical continuation of an existing trajectory rather than a reversal, but it is a material amendment to an approved goal, requiring its own full session with locate-first, an impact walk over BG-0002's derived tree (EP-0009, the SP-0013 through SP-0018 spikes, and the many decisions citing it), a decision on where the current governance-track function lives (recommended: subsumed as the recharted goal's self-governance concern, keeping the dogfooding), and possibly a discretionary BG-level architect consultation. The eventual implication that BG-0001 rescopes toward "presentation and team layer on the Engine" is noted as a further, separate step not to be bundled.

### T53 (stakeholder, verbatim)

"Yes. But should we track the governance-track (your #2) as an idea as well?"

### T54 (facilitator)

Answered: no separate Idea — the governance-track question (where BG-0002's current charter function lives after a recharter) is already recorded as a named open question inside IDEA-0058's body and is only answerable by the recharter session itself; splitting it out would create a fragment with no independent take-up path. Should that session close without resolving it, it parks as its own artifact per DEC-0260 at that time. With the stakeholder's confirmation, the session closes: twenty-one accepted decisions (DEC-0420..DEC-0440), BG-0001/EP-0006/EP-0008 amended and re-affirmed (DEC-0267), the five-term glossary landed in CONTEXT.md, groundwork.yaml and PARITY.md created, three Ideas captured (IDEA-0056, IDEA-0057, IDEA-0058), the recall audit dispositioned with nineteen precedent links, and the commit to follow as the facilitator's git duty (DEC-0333).

### Post-Close Enrichment (2026-07-12)

Post-Close Enrichment (2026-07-12): cross-referenced to IDEA-0059 (harden write tasks against librarian overreach), captured at SES-0084 from the overreach incident recorded at this session's T48.

## Decisions Produced

Ratified at T31 and logged as fifteen accepted decisions distilling the consolidated proposal:

- DEC-0420 — Groundwork names two delineated deliverables: the Paradigm and the Application.
- DEC-0421 — Standalone use of the paradigm never requires the application (narrows DEC-0001).
- DEC-0422 — Absorption triggers retire implementations, never skill-mode delivery (extends DEC-0346).
- DEC-0423 — Paradigm logic is single-sourced in one engine, extraction deferred to first non-CLI consumer.
- DEC-0424 — Git-backed markdown is the sole primary store in every mode.
- DEC-0425 — The corpus format is a versioned, backward-compatible contract.
- DEC-0426 — Team topology: canonical remote, one application instance per repository.
- DEC-0427 — Collaboration protocol: branch-per-session with a pull request at session close.
- DEC-0428 — Approval: frontmatter is the record; merge under branch protection is team-mode enforcement.
- DEC-0429 — Governance declares an enforcement level and projects one-way into host configuration.
- DEC-0430 — ID allocation: reservation at mint; promotion-time reconciliation only as a documented offline fallback.
- DEC-0431 — Develop-branch promotion is an optional corpus-release pattern, independent of ID allocation.
- DEC-0432 — Process-knowledge structuring is deferred until the application's facilitation is built.
- DEC-0433 — Skill-mode is the paradigm's core subset; parity is tracked in a maintained matrix.
- DEC-0434 — Distribution decisions remain with IDEA-0010 and IDEA-0013 take-up, framed by this delineation.

Confirmed at T37 and logged as four further accepted decisions extending the ratified package:

- DEC-0435 — Artifact frontmatter supports multiple approvals via an additive approvals list.
- DEC-0436 — Approver groups are governance configuration: named groups, per-type policies, per-ID overrides, declared quorum.
- DEC-0437 — gw renumber: push-button ID-collision recovery scoped to unmerged branch content.
- DEC-0438 — In DEC-0426, repository means the Groundwork docs repository.

Confirmed at T42, round two, and logged as two further accepted decisions:

- DEC-0439 — The corpus format version lives in a root manifest file.
- DEC-0440 — Governance keys people by email, with per-host identity mappings.

Also at T42, the dogfooding stance for this repository (adopt the Application when it exists, or stay skill-mode-only) was deliberately deferred and captured as IDEA-0057 rather than decided now.

## Conflicts Raised

None.
