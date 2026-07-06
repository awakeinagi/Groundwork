# Groundwork — Agent Handoff / Context Dump

> Throwaway continuation document, written 2026-07-06. Purpose: give an agent
> with EMPTY context everything needed to continue building Groundwork from
> the current state. Not a canonical artifact — do not link it into the doc
> graph; delete or regenerate at will. The canonical truth is the repo itself;
> where this file and the repo disagree, the repo wins.

## 1. What Groundwork is

Groundwork is a **standalone application** (Python backend + Claude Agent
SDK; TypeScript frontend) in which an AI agent conducts **unsupervised 1:1
refinement sessions** with business stakeholders, product owners, and
eng/data-science leads, turning raw business ideas into a gated hierarchy:

```
Idea → Sessions (SES) → Business Goal (BG) → Epics (EP) → Stories/Spikes (ST/SP)
     → contract-complete Component Docs (CMP) → Handoff Manifest → implementation swarm
```

**The docs are the product** — swarm orchestration is out of scope
(DEC-0014). Every artifact carries provenance: raw transcript → Decision
(DEC) → cited by contracts/criteria. Human approval gates sit at every stage.
The core pain being solved: poorly defined, vague, or contradictory business
requests.

This repository is simultaneously (a) the specification of Groundwork and
(b) its first Canonical Store — **full dogfood** (DEC-0019): the system was
designed through its own process, and every design conversation with the
sponsor is recorded as a session artifact with distilled decisions.

## 2. Current state (as of last commit)

- **BG-0001 approved.** All seven epics **approved** (EP-0001..EP-0007,
  sponsor sign-off 2026-07-06). 96 artifacts, graph validates clean.
- **SP-0001** (impact-ranking algorithm) — `draft`, derives from BG-0001,
  not yet executed. **SP-0002** (graph + search engine selection) —
  `approved`, 7-day timebox, not yet executed.
- **76 decisions** (DEC-0001..0076), all `accepted`. **10 sessions**
  (SES-0001..0010), all `closed`, all `transcript-fidelity: reconstructed`
  (pre-application bootstrap; app-hosted sessions must be `verbatim`).
- No stories, components, conflicts, change-proposals, or consolidations
  exist yet (directories hold `.gitkeep`).
- **No application code exists.** Only docs, specs, and `tools/check_links.py`.
- Next free IDs: BG-0002, EP-0008, ST-0001, SP-0003, CMP-0001, SES-0011,
  DEC-0077, CFL-0001, CON-0001, CP-0001.

## 3. Repo layout & conventions

```
CONTEXT.md            glossary (ubiquitous language) — use its terms EXACTLY
README.md             overview + core rules
docs/specs/           format specs per artifact type (SPEC-artifact-common first)
docs/goals|epics|stories|spikes|components|sessions|decisions|conflicts|
     change-proposals|consolidations/
tools/check_links.py  graph integrity checker — RUN BEFORE EVERY COMMIT
HANDOFF.md            this file (untracked, throwaway)
```

Artifact = markdown + YAML frontmatter. Immutable IDs `PREFIX-nnnn`,
filename `ID-slug.md`. Typed links in frontmatter (closed vocabulary):
`derives-from, satisfies, depends-on, conflicts-with, supersedes,
relates-to, impacts, impacted-by`, plus top-level `cites: [DEC-...]`.
`impacts`/`impacted-by` are same-type, reciprocal (checker-enforced), and
mean "decisions made refining X constrain decisions in Y" — used to rank
refinement order (DEC-0026/0027). Status lifecycle:
`draft → in-refinement → gated → approved → (stale ⇄) / superseded / archived`.
Decisions: `proposed | accepted | superseded`, immutable once accepted;
change = new DEC with `supersedes`.

**Commit conventions used so far** (bootstrap simulates the future PR flow):
`git -c user.name="cognizac" -c user.email="awakeinagi@gmail.com" commit`,
message ends with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
Approval = edit frontmatter (`status: approved`, `approved-by:
awakeinagi@gmail.com`, `approved-on: <date>`), commit
`"Approve EP-XXXX (sponsor sign-off, <date>)"`.

## 4. The working process (how to continue correctly)

The sponsor (awakeinagi@gmail.com — tech-side lead; org is Python-native;
hosts on **Bitbucket Data Center**, Jira assumed Data Center) expects the
**grilling method**: dependency-ordered clarifying questions, ~3-4 per
round via structured multi-choice with a **recommended answer listed first**,
free-text always honored. He frequently amends recommendations — treat
notes as design input and record them faithfully.

For every design exchange:
1. Open/record a **new SES artifact** (sessions are closed+immutable;
   follow-ups are new sessions) with turn-numbered reconstructed transcript.
2. Distill **DEC records** (one decision each: Context / Decision /
   Rationale / Alternatives Considered / Implications; `source-span:
   "SES-nnnn @ Tx-Ty"`; `decided-by: awakeinagi@gmail.com`).
3. Update the affected artifact (scope, cites, edges), the glossary
   (CONTEXT.md) for new terms, and specs/checker if the taxonomy changes.
4. Maintain impact edges reciprocally; new cross-epic requirements = new
   edge + note that live operation would queue a re-affirmation.
5. `python3 tools/check_links.py` → commit.
6. Move refined items to `gated`; the sponsor approves with a short message
   ("Approved. Let's move on."); then record approval as in §3.

## 5. Decision architecture — the settled design (by area)

**Truth & storage (EP-0001, approved):** git-backed markdown canonical
(DEC-0002/0008). **Fork-pull model** (DEC-0028): app owns a fork; one item
branch per artifact carrying the item + its sessions/decisions; opening the
branch opens a PR to upstream main; **PR approval IS the gate**; post-merge
changes reuse the branch with a new PR; main holds only approved versions.
Worktree per user session; sole version merges to the item branch, divergent
versions get user-suffixed branches (DEC-0030). All writes via storage API,
read-only git sanctioned for consumers (DEC-0029). ID allocation via
service lock (DEC-0031). **Mechanical writes** (stale marks, jira-status,
transcript appends, counters) are typed service operations only — the LLM
agent holds NO git credentials; arbitrary diffs are inexpressible; where
branch protection forbids direct pushes, auto-PRs approved by a program
user gated by a deterministic mechanical-diff CI check (DEC-0033).
Two-tier validation: schema+links on every write to any branch;
completeness (required sections, citations, reciprocity, no open conflicts)
as required PR checks (DEC-0034). Session transcripts append-only at the
API level (DEC-0035).

**Governance (EP-0003, approved):** gates at every stage (DEC-0006), fixed
role-map AND committee policies (DEC-0020). Enforcement = host branch
protection (dir→reviewer-group, approval counts) + a service-computed
`gate-policy` required check for anything richer (DEC-0036). **Governance-
as-code**: `governance/roles.yaml|domains.yaml|gate-policies.yaml|
people.yaml|repos.yaml` in the repo, PR-gated, Arbiter-owned (DEC-0037/
0046/0049). Staleness: full-subtree mechanical sweep; stale ancestors fail
descendants' gate checks; cleared by lightweight **re-affirmation** PRs
(DEC-0007/0038). Conflicts: intent-first mediation → escalation with
documented Conflict artifact; Arbiter queue + `conflicts-open` blocking
check; no auto-timeout by default, timeout-to-default electable per
artifact (DEC-0005/0039). Role-pool approval + time-bounded delegation
(DEC-0040). Re-affirm queues impact-ranked (DEC-0041). Gate engine emits
event log + metrics API; UI renders dashboards (DEC-0042). Roles:
Stakeholder, Product Owner, Eng Lead, DS Lead, Arbiter. Decision-rights
config extends roles.yaml (DEC-0054).

**Connectors & identity (EP-0005, approved):** capability-declaring
connector contracts with a documented minimum set; gate compiler emulates
missing host features (DEC-0045). v1 host = **Bitbucket Data Center only**
(DEC-0050 — no native path-scoped reviewers, so `gate-policy` check carries
more weight; merge checks/Code Insights are the check surface). Reviews
post as the approver via per-user OAuth; program-user fallback with
verified attribution for seatless roles (DEC-0043). UI wraps the PR —
approvers never leave Groundwork (DEC-0032). Jira: projection on approval
only; content fields canonical-owned, workflow fields Jira-owned syncing in
as telemetry (DEC-0048/0013); drift → revert + capture as **Change
Proposal** (CP artifact, DEC-0044/0047) triaged by the agent (mechanical
fix / session / rejected). Person registry `people.yaml` with stable
person-ids; bootstrap artifacts use emails — migration pending (DEC-0046).
Repo read allowlist `repos.yaml` (DEC-0049). Pluggable auth (DEC-0024).

**Session agent (EP-0002, approved) — the v1 centerpiece:** unsupervised
1:1 sessions (DEC-0003/0021). **Strategy packs as plugins** — versioned
bundles of prompts/skills/tools/policies per session type, PR-gated,
LLM-swappable, recorded in session provenance (DEC-0053). Raw transcripts
ARE the stored record; distillation regenerable from raw (DEC-0052).
In-session confirmation playback before DECs become accepted (DEC-0051).
Guardrails: pack-defined unproductive-pattern handling; decision rights;
input-as-data injection hygiene (DEC-0054). Incremental synthesis on each
session close with shared visible draft, comments → CPs (DEC-0055).
Declarative context recipes in packs with token budgets (DEC-0056).
Lifecycle: open across pauses, inactivity auto-close with partial
distillation, resume = new session (DEC-0057). Evaluation harness in scope:
faithfulness judging, grilling benchmarks, guardrail tests — gates pack
changes and LLM swaps; periodic drift audits (DEC-0058).

**Graph index (EP-0004, approved):** derived, rebuildable, never truth
(DEC-0010). **Main + per-item-branch overlays**, view-parameterized
queries, ref/status-tagged results (DEC-0059). Session-sync/global-async
freshness; correct ≡ rebuild output (DEC-0060). Three query tiers: named
traversals; bounded generic primitive; **read-only guarded openCypher**
(DEC-0062). Metadata-only nodes; bodies from the store (DEC-0063).
Nightly rebuild-and-diff with atomic replacement (DEC-0064). Engine chosen
by SP-0002 (KuzuDB vs Postgres+AGE vs Neo4j; openCypher support is a hard
criterion) (DEC-0061).

**Memory/retrieval (EP-0007, approved):** consolidations = derived,
non-citable summaries of graph paths; static catalog + telemetry-driven
placement (DEC-0065); instant staleness, debounced + on-demand regeneration
(DEC-0066). Retrieval layer owns full-text + semantic search (embedding-
version pinned, swap = re-embed; powers conflict-similarity detection)
(DEC-0067). **Recipe resolver**: deterministic `resolve(recipe, task) →
bundle` within token budget, citations + freshness proof per element
(DEC-0068). No human gate on consolidations — automated no-new-claims
checks block serving (DEC-0069); humans can **flag from the UI → instant
quarantine → disposition; confirmed misses feed the eval corpus**
(DEC-0072). Search infra evaluated in extended SP-0002 (DEC-0070).
**Participant profiles**: supported, strictly opt-in, subject-readable/
editable/deletable via UI, stored outside the canonical store; org facts
never in profiles (DEC-0071).

**Web UI (EP-0006, approved):** v1 = session experience + goal view with
provenance drill-down + goal gate + minimal conflict view (DEC-0073).
**Structured-hybrid sessions**: question cards (recommended-first) +
decision-playback cards + progress panel; guaranteed affordances — notes on
any choice, free-text always, "elaborate" option (agent expands with
examples/compare-contrast) (DEC-0074). Requires typed turn payloads in the
session-engine contract (realizes EP-0006→EP-0002 edge — land in EP-0002
stories). In-app notification center + notifier connectors, email first
(DEC-0075). Semantic gate diff + agent change summary + impact report; raw
diff one click away (DEC-0076).

**Cross-cutting:** Python backend / TS frontend, all specs language-
agnostic for rebuildability (DEC-0018). v1 vertical slice = goal refinement
end-to-end (DEC-0022). Spike findings become DECs (DEC-0023). Handoff
manifest = southern API (SPEC-handoff-manifest). Impact links + ranking
(DEC-0026/0027, SP-0001 — includes investigating **provisional bounding
decisions**: subject-to-change guesses on impacted items to bound the
impactor, reconcile later).

## 6. Impact graph (epics, X impacts Y)

```
EP-0001 → 2,3,4,5,6,7     EP-0002 → 3,4,6,7     EP-0003 → 1,4,5,6
EP-0004 → 7               EP-0005 → 1,2,6       EP-0006 → 2
EP-0007 → 6
Cycles: 1↔3, 1↔5, 2↔6 (why SP-0001 exists — no clean topo order)
```

## 7. Agreed next steps (in rough priority)

1. **Derive EP-0001 stories** (storage API contract, branch/PR
   orchestration, tier-1 JSON Schemas, mechanical-write ops, counter
   durability, worktree lifecycle) — first stories of the project; follow
   SPEC-story (acceptance criteria each citing a DEC).
2. **Execute SP-0002** (graph + search engine selection) — findings become
   DECs deriving from SP-0002.
3. **Execute SP-0001** (impact-ranking algorithm + provisional bounds).
4. EP-0002 stories, incl. typed turn payloads (from DEC-0074), strategy-pack
   format spec, eval harness + benchmark corpus bootstrap.
5. Component docs (CMP) begin to crystallize from stories — the
   contract-complete deliverable (SPEC-component: every contract item cites
   a DEC; uncited = gate blocker).

## 8. Open threads / known debts

- Email→person-id migration once `governance/people.yaml` exists (DEC-0046).
- Confirm Jira Data Center flavor + webhook/event capabilities (EP-0005 risk).
- BBDC required-check surface validation (merge checks / Code Insights) —
  candidate spike.
- Counter durability + distributed lock for multi-node (DEC-0031 implication).
- Mid-flight policy-change recomputation semantics (EP-0003 risk).
- Benchmark corpus must be authored before production sessions exist
  (EP-0002 risk); judge model must differ from session model.
- Bootstrap gap: initial Arbiter/roles before governance files exist to
  gate their own creation (EP-0003 risk).
- SP-0001 objective must serve both refinement ordering and re-affirmation
  queues (DEC-0027 + DEC-0041).
- Profile schema + retention policy needs privacy review (DEC-0071).

## 9. Sponsor interaction profile (observed, this bootstrap)

Approves with short messages; engages deeply with recommended options and
frequently upgrades them (fork-pull model, plugin packs, opt-in profiles,
consolidation flagging, elaborate-affordance). Values: provenance,
regenerability from raw records, structural safeguards over trust,
opt-in/user-owned personal data, git-native mechanisms, pluggability with
contract-level standards (openCypher). Expects the agent to surface
tensions honestly (e.g., redundant inverse links, approval spam, host
variance) and propose resolutions. Persistent memory for this project
exists at `~/.claude/projects/-home-cognizac-Projects-project-documentation-system/memory/`.
