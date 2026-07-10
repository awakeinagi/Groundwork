---
id: SES-0057
type: session
title: Extract artifact tooling into the standalone artifact-interact skill
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-09
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude Code (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Change-intake session on the stakeholder proposal to break the
  artifact parsing/reading abilities out of the groundwork-design-session
  skill into a standalone artifact-interact skill exposing a
  guardrailed script API for reading and writing artifacts, aimed at
  minimizing context bloat and maximizing agent efficiency. Grilling
  expanded the scope from "read tooling + parsing" to the full
  artifact toolbelt: every artifact-touching script (read, new typed
  write API, parsing core, semantic search, graph, consistency,
  coupling, status report, checker/viewer sources) moves;
  groundwork-design-session becomes pure method and mandatorily loads
  artifact-interact at Step 0. Produced DEC-0310..DEC-0323: the
  extraction and roster; SPEC-driven Groundwork specificity; the
  write API as sole sanctioned write path (dogfooding DEC-0029 and
  DEC-0033); the full-lifecycle v1 operation surface; CLI subcommands
  plus JSON batch apply; per-op invariant validation with targeted
  re-checks; a unified CLI redesign superseding DEC-0289; layered
  stdlib-core/opt-in-heavy dependencies; project-local .claude/skills
  as the canonical git-tracked skill home retiring .agents/skills;
  per-skill install scripts; a one-shot reference cutover; building
  the skill under the skill-creator methodology; and, closing a
  recall-audit contract gap on DEC-0292, discretionary
  system-architect consultation at method-level sessions. Prior art
  DEC-0116 is narrowed in part (DEC-0138 recognized as its operative
  narrowing). System-architect consultation was offered and declined.
  The close captured IDEA-0010 (plugin packaging for the skills and
  agents).
  No product artifacts (BG/EP/ST/CMP) change.
links:
  relates-to: [DEC-0289, DEC-0029, DEC-0033, DEC-0116, SES-0053,
               IDEA-0010]
---

# SES-0057: Extract Artifact Tooling into the artifact-interact Skill

## Purpose

Run the change-intake protocol on the stakeholder's proposal to break
the artifact parsing/reading abilities out of the
groundwork-design-session skill into a separate skill,
`artifact-interact`, exposing a guardrailed script API for agents to
read and write artifacts — stated goals: minimize context bloat,
maximize agent efficiency when working with artifacts. Method-level
change: it touches the skill's tooling architecture, the concise-read
prior art from SES-0053 (DEC-0289, superseded here; DEC-0116, narrowed
here), and dogfoods the product's write-authority principles (DEC-0029,
DEC-0033) into the method tooling. No product artifacts change.

## Transcript

**T1 — Stakeholder.** Verbatim proposal (session-opening
instruction): "I want to break out the artifact parsing/reading
abilities from the groundwork-design-session skill onto its own
separate skill artifact-interact. This new skill will use scripts to
define a guardrailed API for agents to interact with artifacts (read,
write) with stated goals of minimizing context bloat and allowing the
maximizing an agent's efficiency of working with artifacts."

**T2 — Facilitator.** Restatement: a new standalone skill
`artifact-interact` takes the artifact parsing and reading
capabilities (the DEC-0289 concise-read tool plus the frontmatter/
structure parsing other bundled scripts re-implement) and adds a
guardrailed, script-delivered API covering read *and* write — today
writes are freehand Edit/Write calls whose correctness rests on agent
discipline; a scripted write path could enforce the invariants
mechanically. Goals: minimize context bloat; maximize agent
efficiency. Flagged for grilling: extraction scope, write-API
surface, Groundwork-specific vs general, and how the change lands in
the corpus. Asked whether to open a session.

**T3 — Stakeholder.** Aligned — open a full grilling session (chose
the recommended option over expedited, correction, or idea capture).

**T4 — Facilitator.** Locate-first findings (per DEC-0266): the
change sits at method level. Read-side ancestry is SES-0053's
progressive-disclosure work — DEC-0289 (stdlib read tool with eight
affordances, homed in the design-session skill) and DEC-0284..DEC-0288,
DEC-0290. The write side has a product-side mirror: CMP-0001 is the
product's single write authority under DEC-0029 (all writes via the
storage API) and DEC-0033 (mechanical writes are typed operations,
never arbitrary diffs) — the proposal dogfoods that architecture into
the method tooling. DEC-0116 (search as a separate script with its
own index) is adjacent prior art. docs/specs/ (16 SPEC documents) is
the natural normative basis for a guardrailed API. Affected-set
hypothesis: method DECs plus the two skills; no product BG/EP/ST/CMP
changes.

**T5 — Stakeholder.** Out-of-band instruction during session setup:
use the skill-creator skill when creating the artifact-interact skill
(invoked /skill-creator with that directive).

**T6 — Facilitator.** Round 1 (recommended options first): (a) what
moves — recommended read tool + parsing core + new write API, with
search/graph/consistency/status staying; (b) write-API authority —
recommended sole sanctioned write path mirroring DEC-0029/DEC-0033;
(c) Groundwork-specific SPEC-driven vs generic toolkit — recommended
Groundwork-specific; (d) convene the system-architect advisor
consultation (architecture-shaped session, discretionary at method
level) — recommended yes.

**T7 — Stakeholder.** (a) Read tool + parsing core + new write API
(recommended). (b) Answered with a question: "How will the agent call
the typed operations from the skill scripts?" (c) Groundwork-specific,
SPEC-driven (recommended). (d) No — skip the architect consultation
for this session.

**T8 — Facilitator.** Elaboration on invocation mechanics: agents
call typed operations through the Bash tool as CLI subcommands (the
groundwork_read.py pattern, extended to writes) — e.g. `create` with
ID allocation, `append-turn` with stdin payloads, `set-status` with
transition validation, `edit-section` with `--from-file`. The script,
not the agent, owns the dangerous parts: validate before touching
disk (SPEC conformance, transition legality, immutability — editing
an accepted DEC returns an error naming the sanctioned `supersede`
alternative), perform mechanical bookkeeping atomically (ID
allocation, reciprocal impact edges, slugs, approval stamping),
return a compact diff. Long content via stdin or `--from-file`, never
shell-quoted arguments. Named the alternative convention — a single
`apply` command taking a JSON operation document, more
machine-checkable and batchable — and that the two compose. Re-asked
the write-authority question plus the convention choice.

**T9 — Stakeholder.** Write authority: sole sanctioned write path
(recommended). Convention: CLI subcommands plus a JSON batch `apply`
(recommended).

**T10 — Facilitator.** Round 2: (a) v1 operation surface —
recommended the full lifecycle set (create, append-turn, edit-section,
set-status, add-link/add-cite, supersede, update-overview) since a
sole-path stance needs near-complete coverage to be honest; (b)
validation depth — recommended per-op invariants + targeted re-checks
of touched artifacts, full checker staying the pre-commit gate; (c)
how scripts remaining in design-session consume the parsing core that
moves — recommended import via sibling-skill path; (d) read side —
recommended move-as-is, extend later.

**T11 — Stakeholder.** (a) Full lifecycle set — *and* move the graph
and semantic-search scripts currently on the groundwork-design-session
skill as well. (b) Per-op invariants + targeted checks (recommended).
(c) Scope amendment superseding the T7 split: "All artifact related
abilities will now live on this skill and its scripts.
groundwork-design-session should reference this skill in its SKILL.md
as an autoload." (d) Redesign the read side during the move.

**T12 — Facilitator.** Round 3 on the amended scope: (a) exact
roster — recommended everything that touches artifacts (read, write,
parsing, search, graph, consistency, coupling, status_report, plus
ownership of the check_links.py/serve_docs.py sources bootstrap
installs), leaving design-session with zero scripts; (b) redesign
shape — recommended one unified CLI with subcommand families
(read/write/search/graph/check), uniform --root/--json conventions;
(c) autoload semantics — recommended a mandatory load at design-session
Step 0 (hard dependency, no duplicated command docs); (d) cutover —
recommended one-shot with all references updated, no shims.

**T13 — Stakeholder.** (a) Everything that touches artifacts
(recommended). (b) One unified CLI with subcommand families + JSON
mode (recommended). (c) Mandatory load at Step 0 (recommended). (d)
One-shot cutover updating all references — and additionally: "copy
all .agents/skills into .claude/skills local to the project so they
can be tracked by git."

**T14 — Facilitator.** Round 4: (a) which skill home is canonical
after that copy, and does .agents/skills survive — recommended
project-local .claude/skills as the canonical git-tracked source of
truth (Claude Code loads it natively), ~/.claude/skills demoted to a
personal convenience install, .agents/skills retired; (b) dependency
handling in the unified CLI — recommended layering: stdlib
read/write/check families always work via python3, search/graph
families carry inline uv metadata and load their engines only when
invoked.

**T15 — Stakeholder.** (a) .claude/skills canonical, retire
.agents/skills — and add an install script to each skill allowing
users to install it locally and globally (home folder), including the
option to install the repo's .claude/skills globally. (b) Layered
dependencies (recommended).

**T16 — Facilitator.** Twelve-item read-back for in-session
confirmation: (1) artifact-interact owns all artifact abilities,
design-session becomes pure method; (2) Groundwork-specific,
SPEC-driven; (3) write API is the sole sanctioned write path; (4)
full-lifecycle v1 op surface; (5) CLI subcommands + JSON batch apply;
(6) per-op invariants + targeted checks; (7) unified-CLI redesign
superseding DEC-0289's framing with affordance intent carried
forward; (8) layered dependencies; (9) .claude/skills canonical,
.agents/skills retired, per-skill install scripts (facilitator's
interpretation flagged for correction); (10) one-shot cutover; (11)
mandatory Step-0 load; (12) build under skill-creator.

**T17 — Stakeholder.** Confirmed — all twelve.

**T18 — Facilitator.** Session-close inspired-ideas check (DEC-0261),
after presenting the close summary, the recall-audit dispositions,
and the DEC-0323 gap closure.

**T19 — Stakeholder.** Verbatim: "I want to create a plugin for
these skills and custom agents to use them" — captured as IDEA-0010
for the work queue; not an extension of this session.

## Session Close

Consistency machinery (per DEC-0157 sweep and DEC-0158 terms): sweep
flagged the ratified citers of DEC-0029
and DEC-0033 (CMP-0001, EP-0001, ST-0002, ST-0006, and the gate/
identity stories) for review against DEC-0312 — disposition: no
change needed; DEC-0312 extends the product's write-authority
principle into method tooling and alters no product contract. terms
flagged serve_docs.py co-occurrence with DEC-0244/DEC-0245 —
disposition: no change needed; those decisions specify the viewer's
behavior and bootstrap installation, not which skill hosts its
sources. Checker green (pre-existing coverage warnings only).

Determined: DEC-0310..DEC-0322 distilled and confirmed at T16-T17;
DEC-0289 superseded by DEC-0316; DEC-0116 narrowed by DEC-0310/
DEC-0316 (separate-script aspect) with its own-index aspect intact —
reviewed under the consistency sweep. Recall-audit findings applied
as cross-reference enrichment (DEC-0248): DEC-0130 (shared
allowlist asset between typed operations and validator) surfaced as
prior art on DEC-0315; DEC-0138 recognized as the operative
narrowing of DEC-0116 that the unified CLI's search family actually
inherits, cited on DEC-0317. The audit's contract-gap finding —
DEC-0292 defines no consultation policy for method-level sessions —
closed by recording DEC-0323 (discretionary at method level, offer
recorded), ratified by the stakeholder in-session. Classification confirmed:
method-level tooling change; no product artifacts touched; no
staleness cascade (DEC-0289's only citers are DEC-0290, immutable,
and SES-0053, closed). Follow-on queue: build the artifact-interact
skill under the skill-creator methodology (DEC-0322) executing the
cutover decisions (DEC-0310, DEC-0316..DEC-0321), including the
.claude/skills migration and .agents/skills retirement; update
facilitator memory (vendored-copy sync rule becomes obsolete at
cutover). Inspired-ideas check captured IDEA-0010 (package the
skills and custom agents as a plugin, T19) into the work queue.

## Decisions Produced

- DEC-0310 — artifact-interact owns all artifact-touching tooling;
  groundwork-design-session becomes pure method
- DEC-0311 — artifact-interact is Groundwork-specific and SPEC-driven
- DEC-0312 — the write API is the sole sanctioned write path
- DEC-0313 — v1 write surface is the full lifecycle operation set
- DEC-0314 — calling convention: CLI subcommands plus JSON batch apply
- DEC-0315 — per-operation invariant validation with targeted re-checks
- DEC-0316 — one unified CLI with subcommand families and JSON mode
  (supersedes DEC-0289)
- DEC-0317 — layered dependencies: stdlib core, opt-in heavy families
- DEC-0318 — project-local .claude/skills is the canonical skill home;
  .agents/skills retired
- DEC-0319 — every skill ships an install script for local and global
  installs
- DEC-0320 — one-shot cutover with all references updated
- DEC-0321 — groundwork-design-session mandatorily loads
  artifact-interact at Step 0
- DEC-0322 — artifact-interact is built under the skill-creator
  methodology
- DEC-0323 — system-architect consultation is discretionary at
  method-level sessions (closes the recall-audit contract gap)

## Conflicts Raised

None.
