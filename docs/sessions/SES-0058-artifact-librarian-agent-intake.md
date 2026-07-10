---
id: SES-0058
type: session
title: The artifact-librarian agent — delegated artifact interaction for all agents
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-09
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude Code (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Change-intake session on the stakeholder proposal to design an
  agent that the default agent calls as a subagent any time it needs
  to interact with artifacts. Produced DEC-0324..DEC-0334: the
  artifact-librarian project agent — task-level intent contract,
  distilled results with verbatim-on-request; delegation mandatory
  for ALL artifact interaction (reads included) by ALL agents,
  facilitator included, extending DEC-0312's sole-path stance a layer
  up; enforcement via a standing instruction (AGENTS.md + project
  memory, installed at design-session startup in every
  Groundwork-paradigm project) plus a deliberately non-self-
  triggering artifact-interact skill, superseding DEC-0321; a
  manual-load escape hatch where agent-definition loads count as
  manual; recharters of overview-writer (typed update-overview op)
  and system-architect (explicit read-only charter); Sonnet-class
  model doubly pinned; refuse-and-report refusal semantics; stateless
  per task with a persistent behavioral learning memory (stakeholder
  amendment); parallel reads with serialized writes; caller-owned
  commits; and shipping as one deliverable with the artifact-interact
  skill inside the DEC-0322 build loop. System-architect consultation
  offered per DEC-0323 and declined. Mid-session the stakeholder
  surfaced that SES-0057's skill was never built — captured as
  IDEA-0011 (method build obligations invisible to the work queue).
  Close carried a stakeholder sequencing instruction: implement the
  skill and agent before committing anything. Method-level change; no
  product artifacts (BG/EP/ST/CMP) change.
links:
  relates-to: [SES-0057, DEC-0310, DEC-0312, DEC-0313, DEC-0318,
               DEC-0319, DEC-0320, DEC-0321, DEC-0322, DEC-0323,
               DEC-0291, DEC-0292, DEC-0260, DEC-0261,
               IDEA-0010, IDEA-0011]
---

# SES-0058: The artifact-librarian Agent

## Purpose

Run the change-intake protocol on the stakeholder's proposal to
design an agent that the default agent calls as a subagent whenever
it needs to interact with artifacts. The session sits directly on
SES-0057's foundation — the artifact-interact skill owning all
artifact tooling (DEC-0310), its write API as sole write path
(DEC-0312), the full-lifecycle operation surface (DEC-0313), and the
build/packaging decisions (DEC-0318, DEC-0319, DEC-0320, DEC-0322) —
and supersedes DEC-0321 (facilitator Step-0 load). Agent precedents:
overview-writer (DEC-0291) and system-architect (DEC-0292); the
consultation offer follows DEC-0323. Touches IDEA-0010 (the eventual
plugin bundles this agent too) and captures IDEA-0011. Method-level
change; no product artifacts change.

## Transcript

**T1 — Stakeholder.** Verbatim proposal: "I want to design an agent
that the default agent will call (as a subagent) any time it needs
to interact with artifacts."

**T2 — Facilitator.** Restatement: a new project agent (like
system-architect and overview-writer) that the default agent — the
facilitator, or any main-loop agent in the project — delegates to
whenever it needs to interact with corpus artifacts: reads, searches,
graph queries, writes through the artifact-interact API; keeping tool
output and corpus content out of the main context. Located it as the
natural next step after SES-0057; noted the DEC-0321 tension (Step-0
load vs delegation) and the IDEA-0010 connection. Classification
hypothesis: method-level, full grilling session. Asked to open.

**T3 — Stakeholder.** "yes, open the session."

**T4 — Facilitator.** Session open. Locate-first (DEC-0266): graph
rebuilt; material discovery — the artifact-interact skill decided in
SES-0057 has not been built (`.claude/skills/` empty; the DEC-0322
build loop never ran), so agent and skill specs can co-evolve. Round
1 (recommendations first): (a) callers — all agents including the
facilitator, vs only non-facilitator agents, vs facilitator-writes-
only; (b) granularity — task-level intent (recommended) vs
operation-level proxy vs both; (c) binding force — writes-mandatory/
reads-discretionary (recommended) vs everything-mandatory vs
advisory; (d) per DEC-0323, offered a system-architect advisor
consultation (session is architecture-shaped).

**T5 — Stakeholder.** (a) All agents, facilitator included. (b)
Task-level intent. (c) Everything mandatory — the agent is the sole
sanctioned way to touch artifacts at all, exceeding the facilitator's
recommendation. (d) Consultation declined (recorded per DEC-0323).

**T6 — Facilitator.** Read-back; surfaced the two tensions
everything-mandatory creates: DEC-0321 cannot stand as written, and
the existing specialized agents (system-architect reads the corpus;
overview-writer edits overviews; recall-audit judges read packets)
touch artifacts directly and cannot delegate — subagents cannot spawn
subagents. Round 2: (a) skill home — supersede DEC-0321, skill
becomes the agent's toolbelt (recommended) vs both-load vs keep; (b)
mandate boundary for specialized agents — charter-scoped access
(recommended) vs facilitator pre-packaging vs reads-free/writes-
chartered; (c) model — Sonnet-class (recommended) vs Haiku vs
inherit; (d) result contract — distilled + verbatim-on-request
(recommended) vs distilled-only vs structured raw.

**T7 — Stakeholder.** (a) Skill becomes the agent's toolbelt;
supersede DEC-0321. (b) Custom answer replacing the offered options,
verbatim: "Part of the startup process of the groundwork-design-
session skill is to add a project-level memory that all agents must
use the artifact agent to interact with artifacts unless the
artifact-interact skill as been manually loaded; we will disable the
ability for the artifact-interact skill to automatically load from
context." (c) Sonnet-class. (d) Distilled + verbatim-on-request.

**T8 — Facilitator.** Read-back of T7's enforcement mechanism
(standing instruction at startup + non-self-triggering skill + manual
load as escape hatch); noted it resolves the mechanism but leaves the
specialized-agent edge open, since overview-writer and
system-architect use raw Read/Edit without loading the skill at all.
Round 3: (a) does "manually loaded" extend to agent definitions —
yes, definition counts (recommended) vs operator-only vs
reads-chartered/writes-never-direct; (b) name — artifact-librarian
(recommended) vs artifact-interactor vs archivist; (c) refusal
semantics — refuse-and-report (recommended) vs adapt-within-
sanctioned-ops vs latitude flag; (d) packaging — one deliverable with
the skill in the DEC-0322 loop (recommended) vs separate follow-on
build.

**T9 — Stakeholder.** All four recommendations: definition counts as
manual load (overview-writer rechartered to the typed op;
system-architect chartered read-only); name artifact-librarian;
refuse and report; one deliverable with the skill.

**T10 — Facilitator.** Read-back. Round 4: (a) statefulness —
stateless fresh-per-task (recommended) vs continuable; (b)
concurrency — parallel reads, serialized writes (recommended) vs
fully serialized vs API-locked; (c) commits — caller commits
(recommended) vs librarian-commits-on-request; (d) home of the
standing instruction — AGENTS.md Groundwork section (recommended) vs
AGENTS.md + facilitator memory vs CLAUDE.md.

**T11 — Stakeholder.** (a) Stateless per task, amended: "but also
able to use memory to refine behavior through experience and
interaction with the user." (b) Parallel reads, serialized writes.
(c) Caller commits. (d) Amended: "AGENTS.md + project-level memory
for all project using the Groundwork documentation paradigm (outside
of the Groundwork application repo)" — i.e. every consumer project
gets both surfaces at bootstrap/startup.

**T12 — Stakeholder** (mid-turn). "Why didn't we create the
artifact-interact skill in the previous session? That seems like a
surfaced gap in our design-session workflow."

**T13 — Facilitator.** Answer: by design in part — sessions produce
decisions, and DEC-0322 deliberately deferred construction to a
skill-creator build loop; but the tracking gap is real — ratified
method-tooling build obligations appear nowhere in the status
report's work queue, and the unbuilt skill was only discovered by
direct inspection. Restated the gap and proposed IDEA capture per
the focus-artifact test (DEC-0260: different artifact, park it).
Presented the full decision playback (the eleven decisions recorded
as DEC-0324..DEC-0334), confirmed classification (method-level; no
product artifacts change; DEC-0321 superseded; DEC-0322 scope
amended in spirit), and ran the DEC-0261 inspired-ideas check with
the gap as candidate (a).

**T14 — Stakeholder.** "I want to handle implementation of both the
agent and the skill before we commit anything." No corrections to
the playback — taken as confirmation of the eleven decisions, plus a
sequencing instruction: build the artifact-interact skill and the
artifact-librarian agent first; commit only after.

**T15 — Facilitator.** Close. Decisions recorded as
DEC-0324..DEC-0334; IDEA-0011 captured for the build-visibility gap
(restatement aligned, no correction raised at T14); the sequencing
instruction accepted — session records and the DEC-0322/DEC-0334
build land in the working tree together, with the checker run and
commits deferred to the end of the build per the stakeholder's
instruction. Consistency sweeps and the decision-recall audit run
before commit as always.

## Session Close

- **Classification (confirmed):** method-level tooling change; no
  product artifacts (BG/EP/ST/CMP) change.
- **Supersession:** DEC-0321 superseded by DEC-0326.
- **Amendments in spirit:** DEC-0322's build scope (agent joins the
  loop, DEC-0334; description pass inverts to non-triggering,
  DEC-0326); DEC-0319's install contract (installs the agent too,
  DEC-0334); DEC-0291/DEC-0292 agent charters (DEC-0328).
- **Ideas:** IDEA-0011 captured (method build obligations invisible
  to the work queue), parked per DEC-0260; inspired-ideas check run
  per DEC-0261. IDEA-0010 noted: the plugin would bundle the
  librarian as well.
- **Recall audit:** one finding — DEC-0260/DEC-0261 applied by name
  but uncited; fixed in place before close. Remaining candidates
  judged noise; no contract gap.
- **System-architect consultation:** offered (DEC-0323), declined at
  T5.
- **Execution note:** per T14, implementation of the
  artifact-interact skill and artifact-librarian agent proceeds
  before any commit; commits follow the completed build and passing
  checker.

## Decisions Produced

- DEC-0324 — create the artifact-librarian agent; task-level intent;
  distilled + verbatim-on-request results
- DEC-0325 — delegation mandatory for all artifact interaction, all
  agents
- DEC-0326 — enforcement: standing instruction at startup +
  non-self-triggering skill; supersedes DEC-0321
- DEC-0327 — manual-load escape hatch; agent-definition loads count
- DEC-0328 — recharter overview-writer and system-architect
- DEC-0329 — Sonnet-class model, doubly pinned
- DEC-0330 — refuse-and-report refusal semantics
- DEC-0331 — stateless per task with persistent behavioral memory
- DEC-0332 — parallel reads, serialized writes
- DEC-0333 — caller commits; librarian never touches git
- DEC-0334 — one deliverable with the artifact-interact skill

## Conflicts Raised

None.
