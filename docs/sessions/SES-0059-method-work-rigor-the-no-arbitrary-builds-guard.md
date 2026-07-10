---
id: SES-0059
type: session
title: Method-work rigor — the no-arbitrary-builds guard
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-09
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude Code (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Change-intake session on the stakeholder proposal that anything
  worked on within a Groundwork project be fully documented, vetted,
  and human-signed-off, after SES-0058's build drifted (the deployed
  artifact-librarian held Write/Edit tools nobody discussed).
  Produced DEC-0335..DEC-0344: the paradigm-level no-arbitrary-
  builds guard with its mechanical floor and build-intent intake;
  grounding-through-contracts as a first-class priority with the
  minimum-reconciliation yardstick; required right-sized research
  before tooling decisions; the BG-0002 method-track charter
  (dogfooding; admission predicate; sacrificial absorption
  triggers); one method epic with two CMPs; the gate-enforced agent-
  contract profile for SPEC-component; the deployed-vs-contracted
  conformance check; the backfill protocol for the SES-0058
  deliverables; the librarian memory-as-preloaded-skill mechanism
  with the ratified tool-surface hot-fix; and IDEA-0011's take-up
  folded into BG-0002; and the test-plan rule (DEC-0345: the
  presented design for anything executable includes which tests will
  validate proper function, and approval covers both). A system-
  architect dual-instance consultation ran and converged after one
  rebuttal round. Mid-session the facilitator repeated the anti-
  pattern (an unpresented hot-fix design, called out by the
  stakeholder) — the corrected sequence (research, option survey,
  approval) is recorded, along with two facilitator-memory lessons.
  A live reconciliation also ran: the write API's batch mode
  diverged from DEC-0314's as-a-unit intent and was fixed under the
  new guard's own path. BG-0002 was drafted and gated; IDEA-0012
  (skill-level contracts) captured. Method- and paradigm-level
  change; no product artifacts change.
links:
  relates-to: [SES-0057, SES-0058, BG-0001, DEC-0252, DEC-0253, DEC-0254, DEC-0006, DEC-0011, DEC-0266, DEC-0314, DEC-0322, DEC-0324, DEC-0325, DEC-0331, DEC-0312, DEC-0292, DEC-0293, DEC-0296, DEC-0323, DEC-0261, DEC-0259, IDEA-0010, IDEA-0011, DEC-0315, DEC-0019]
---

# SES-0059: Method-Work Rigor — the No-Arbitrary-Builds Guard

## Purpose

Run the change-intake protocol on the stakeholder's proposal that
anything worked on within a Groundwork project be fully documented,
vetted, and human-signed-off — at minimum an agile-style Story with
requirements/acceptance criteria — after SES-0058's build (the
artifact-librarian agent and artifact-interact skill, DEC-0324..
DEC-0334) was implemented from a single conversation and drifted: the
deployed agent acquired Write/Edit tools nobody discussed. The session
produced the paradigm-level no-arbitrary-builds guard (sibling of
DEC-0252), the grounding-through-contracts first-class priority, the
required research step, the BG-0002 method-track charter (taking up
IDEA-0011), the agent-contract profile for SPEC-component, the
conformance check, the backfill protocol for the SES-0058 deliverables,
and the librarian memory mechanism (concretizing DEC-0331) with an
in-session hot-fix of the live tool-grant violation of DEC-0312. A
system-architect consultation ran per DEC-0292/DEC-0293/DEC-0323
(dual-instance debate, one rebuttal round). Relates to SES-0057 and
SES-0058 (the precipitating builds), DEC-0253/DEC-0254 (the mechanical
floor and expedited path this extends), DEC-0322 (the build methodology
this formalizes beyond), DEC-0006 (the gate rule extended to method
work), DEC-0011 (component docs as the contract artifact), DEC-0266
(locate-first), IDEA-0010 (distribution seam named, epic deferred to
its take-up), and BG-0001 (the product track BG-0002 parallels).
Method-and-paradigm-level change; no product artifacts change.

## Transcript

**T1 — Stakeholder.** Verbatim proposal: "This reveals a major flaw in
our process. Though not part of the Groundwork application itself, this
agent and skill were part of the overall project. But unlike the rest
of the system that we're designing, and carefully analyzing toward the
final goal of implementation. For this agent and the skill, we kind of
just winged it based on a single conversation. I would like to propose
that anything worked on within a Groundwork project should be fully
documented, vetted, and signed off on by a human. For this librarian
agent, we didn't document any core features, capabilities, contracts,
etc. Which is why we see the agent getting granted tools we didn't
discuss. I want to come up with a way to handle situations like this.
There should at the very least be a Story (an agile-style user story)
explaining why we need this and listing out all of the
requirements/ACs to know when the work is complete or when there are
still gaps in the implementation. Let's begin a grilling session to
discuss. Do you think we need an Implementation artifact to document
the implementation design?"

**T2 — Facilitator.** Restatement: method-level work was designed and
built from one conversation while product work gets requirements,
contracts, gates, sign-off — and the gap showed immediately as an
undiscussed tool grant on the deployed librarian. Direct answer to the
Implementation-artifact question: recommend NO new type — the Story is
already the requirements/AC artifact and the Component Doc is already
the implementation-design artifact (contract-complete, element-typed,
gated, DEC-0011); a CMP's contract would have enumerated the tool
surface and the gate would have caught the drift. The real gap:
method work has no home in the tree (integrity rule 3 traces
everything to a Business Goal). Proposed grilling toward a
method-track Business Goal. Locate-first (DEC-0266) dispatched as an
artifact-librarian read task — the SES-0058 mandate binding the
facilitator too.

**T3 — Facilitator.** Locate-first results (librarian task): the
sign-off machinery exists but is product-scoped — DEC-0006 gates,
ST-0007 traceability checks, DEC-0093/DEC-0194 coverage discipline all
stop at the BG→EP→ST/SP→CMP tree; method tooling is governed only by
DEC-0322's build methodology (evals and review, but no requirements
artifact, no ACs, no gate); IDEA-0011 already names the tracking gap;
no implementation-design artifact type exists other than the CMP.
Round 1 presented: scope of the mandate, ontology home, backfill of
the as-built, architect-consultation offer (DEC-0323).

**T4 — Stakeholder.** Clarifying question before answering: "But,
which Epic would this supposed story(s) live under?"

**T5 — Facilitator.** Answer: none of EP-0001..EP-0008 can honestly
host it — they derive from BG-0001, the product goal, and method
stories don't advance its outcomes; forcing them in would corrupt
traceability. Hence the method track needs its own root: BG-0002, with
method epics beneath (first: an artifact-interaction-surface epic
where the backfill lands; later e.g. distribution/packaging where
IDEA-0010's plugin would dock). Noted the two-track relationship:
BG-0001's application will eventually absorb the manual tooling —
a reason for clean separation now. Round 1 re-presented with the
epic layer explicit.

**T6 — Stakeholder.** Round 1 answers. Scope (custom answer):
"Dogfooding was a stated goal for this project. But, it feels like
we've dropped the ball. I agree with the creation of a new BG. Let's
also bring in the software architects so we can hear their opinions."
Ontology: BG-0002 + method epics + standard ST/CMP. Backfill: backfill
and gate against as-built. Architect consultation: yes, consult now.

**T7 — Facilitator.** Read-back; scope boundary held open for the
architects. DEC-0293 dual-instance debate launched (record-grounded
instance with a packet of the relevant accepted DECs; best-practice-
independent instance with the abstract situation only; strongest model
passed explicitly at both spawns per DEC-0292).

**T8 — Stakeholder** (mid-turn, while the debate ran). "The most
important thing is that we guard against any project building things
arbitrarily."

**T9 — Facilitator.** Acknowledged as the session's center of gravity:
a paradigm-level guard — the build-side sibling of DEC-0252 — *no
construction outside a gated artifact*, enforced by standing
instruction in every Groundwork-paradigm project, with a build-intent
intake path so "let's build X" routes to a Story before code exists.
BG-0002 becomes this repo's instance of the universal rule, not the
rule itself. Carried into the rebuttal round.

**T10 — System-architect consultation** (summarized per DEC-0296;
dual-instance debate, one rebuttal round, convergent verdict). Opening
positions agreed on fundamentals (second root sound with junk-drawer
guards; intent-first backfill; closed-world tool enumeration;
continuous conformance checking) and differed on epic count (three
seams vs one epic) and on whether agents need a distinct contract
element type. After one rebuttal round: best-practice instance
conceded to ONE epic + two CMPs (a runtime-config epic cannot gate
independently — by its own seam-rent test) while retaining that
runtime/capability configuration is a distinct CONTRACT concern with a
mandatory gate-enforced section; record-grounded instance conceded the
gate-checkable agent contract profile (as a SPEC-component
`component-type: agent` extension rather than a new element type,
honoring DEC-0311's anti-generality stance; revisit trigger if the
agent population grows past three) and the explicit breaking-change
list (tool grants, model class, memory scope ⇒ re-gate; DEC-0322
eval-loop build details ⇒ compatible); both placed the stakeholder's
T8 guard rule ABOVE BG-0002 in the process layer (BG-0002 cites it as
a constraint); both refined the excess-grant stance to "scoped memory
write clause in the contract + the blanket grant is a nonconformance
finding requiring stakeholder disposition"; both endorsed
strangler-shaped backfill starting with the tool-grant slice, with
adversarial gate scenarios and an independent reviewer. The
record-grounded instance flagged an interim risk: the deployed
librarian's Write/Edit grant violated DEC-0312 live, worth a
hot-fix-now stakeholder call.

**T11 — Facilitator.** Joint verdict presented as a proposal
(seven points) with Round-2 calls: ratify verdict, hot-fix now vs at
gate, scope predicate, IDEA-0011 disposition. The live-grant risk was
also surfaced standalone.

**T12 — Stakeholder.** Rejected the presentation and sharpened the
substance: "This is a whole bunch of jargon but not a lot of
substance." Additions: Groundwork needs additional FIRST-CLASS
priorities (similar to provenance) — documented behavior and/or data
contracts for everything living in the project; the tool choices
should have been specified and documented; we under-grilled the agent
and skill; research into available options was in order and should be
a core part of the flow; the handed-off work drifted because it wasn't
specified clearly enough, and Groundwork is supposed to prevent
exactly that — to "work" on "ground"ing the agents handling
implementation. The questions that were never asked: Why did we need
this agent? What was it supposed to accomplish? How does it accomplish
that? What are the configuration options for an agent? How should this
agent be configured? Inspiration: the superpowers brainstorming skill
(fetched from source in-session), specifically its anti-pattern —
"This Is Too Simple To Need A Design": every project goes through the
process; a todo list, a single-function utility, a config change — all
of them; the design can be short but MUST be presented and approved.

**T13 — Facilitator.** Plain-language root cause, owned: SES-0058
decided behaviors but never wrote the configuration contract; the
facilitator chose the agent definition's fields silently while writing
the file — including a `memory` setting never discussed — and nobody
could catch the drift because no document said what the tool list
should be. "We specified intent but not configuration, and unspecified
configuration is where drift lives." The stakeholder's three additions
restated concretely; feedback recorded to facilitator memory
(plain language over jargon). Round presented: contracts first-class,
research required, no-simplicity-exception rule, hot-fix timing.

**T14 — Stakeholder.** Contracts: "Yes, first-class priorities where
possible. For prose edits, the session and the decision records are
sufficient. But we should always ask ourselves, what is minimum amount
of specification/design documentation that I will need to reconcile
this change against the original intent." Research: "Yes. Require,
sized to the decision. But research could be as simple as a web search
to look up documentation (e.g. on configuring an agent, what each
config option handles, what's relevant for fulfilling the proposal?)"
No-exceptions rule: "We need to be clear on what is meant by
'zero-semantic-content'." Live fix: fix now.

**T15 — Facilitator.** Hot-fix executed (expedited step): removed the
undiscussed `memory: project` field and scoped an interim notes-file
memory; committed. Presented the mechanical-floor definition: a build
change is mechanical only if it cannot change runtime behavior or any
contract surface (comments, whitespace, invisible renames);
configuration is NEVER mechanical; when in doubt, semantic. Presented
the remaining calls.

**T16 — Stakeholder.** "You just made another arbitrary decision."

**T17 — Facilitator.** Conceded precisely: the T14 approval covered
the intent (fix now), not the fix's design — the interim memory
mechanism was invented and committed without presenting options, and
the root cause ("memory: project pulled in Write/Edit") was asserted
without verification. The anti-pattern, mid-session. Feedback recorded
to facilitator memory (approval covers intent, not design). The
skipped research step then ran (documentation lookup): VERIFIED —
`memory:` auto-enables Read/Write/Edit regardless of the `tools:`
list; full agent frontmatter field inventory obtained, including three
fields that implicitly expand capability (`memory`, `mcpServers`,
`tools: Agent(...)`) and the `disallowedTools` denylist; no
harness-managed memory scope offers a narrower grant. Option survey
presented: (1) harness memory with the documented full grant, (2) the
committed Bash-scoped notes file, (3) memory as a preloaded skill
(automatic recall via the `skills:` field + the same narrow Bash-scoped
write, git-tracked), (4) operator-curated memory.

**T18 — Stakeholder.** Confirmed the agent should update its own
memory and asked which available option best fits the session's
revealed needs; on the survey, approved option 3 — memory as a
preloaded skill. Separately challenged the interim design's file
location: "Are you sure it's safe to put this 'memory' scratch file at
.claude/agents/artifact-librarian.notes.md. How will the Claude apps
distinguish between it and an agent *.md file?" — a real defect
(the harness scans .claude/agents/*.md as agent definitions),
validated and already mooted by the approved design
(.claude/skills/artifact-librarian-memory/SKILL.md). Implementation of
the approved design executed and committed: memory skill created,
librarian definition amended, install script ships the memory skill
without overwriting accumulated copies.

**T19 — Stakeholder.** Final calls: build rule adopted WITH the
mechanical floor; the structural plan confirmed (BG-0002 with the
reconciliation yardstick, one epic + two CMPs, agent-contract
checklist in SPEC-component including the implicit-grant fields,
automated conformance check, backfill starting with the librarian tool
surface); IDEA-0011 folded into BG-0002 and taken up by this session.

**T20 — Facilitator.** Decision playback (ten decisions, plain
language) and the DEC-0261 inspired-ideas check; candidate offered:
skill-level contracts (skills' scripts run with the loading agent's
permissions — implicit capability surface beyond the agent checklist).

**T21 — Stakeholder.** Playback confirmed without corrections; the
skill-contracts thought captured: "Yes, you can add that as an idea or
a spike."

**T22 — Facilitator.** While dispatching the recording batch to the
librarian, a build defect surfaced and was brought to the stakeholder
per the just-ratified guard instead of being silently fixed: the write
API's batch mode re-validates each file immediately after each
operation, so mutually-referencing record sets (session ↔ decisions ↔
goal — what every session close produces) cannot be recorded; DEC-0314
had ratified batches as "validated and applied as a unit", making this
a reconciliation case under the DEC-0336 yardstick. Short design
presented: defer per-file re-validation to the end of the batch,
single-operation behavior unchanged; alternatives (opt-in flag;
placeholder-then-edit workarounds) laid out.

**T23 — Stakeholder.** Approved the deferred-validation fix.

**T24 — Stakeholder** (mid-dispatch refinement). "Another refinement.
Before implementing anything executable, make a plan for which tests
will be run to validate proper function."

**T25 — Facilitator.** Recorded as DEC-0345: the presented design for
anything executable includes its test plan, and approval covers both.
Honest note entered: the T23 fix was verified on the scratch corpus
(mutually-referencing create cycle; single-op validation regression
check), but those tests were chosen after approval — DEC-0345 closes
exactly that residual going forward.

**T26 — Facilitator.** Close. IDEA-0012 captured (level unclear until
the contract-checklist work exists → Idea per the DEC-0259 boundary).
Decisions recorded as DEC-0335..DEC-0345; BG-0002 drafted and gated
for stakeholder approval; IDEA-0011 marked taken-up with disposition
pointing here. All writes executed through the artifact-librarian per
DEC-0325. Consistency sweeps, recall audit, checker, and commits
follow before the session record is final.

### Post-Close Enrichment (2026-07-09)

Recall-audit dispositions: DEC-0019 surfaced as the founding
dogfooding decision T6 invoked — linked from DEC-0338, cited by
BG-0002's Problem; DEC-0315 recognized as the per-operation
re-validation design that collided with DEC-0314's as-a-unit intent
in the T22 reconciliation — linked from this session; DEC-0336's
"alongside provenance" traces to DEC-0015 — linked. Remaining
candidates judged noise or already carried (DEC-0326, DEC-0319
verified carried by existing citations).

## Session Close

- **Classification (confirmed):** paradigm- and method-level change;
  no product artifacts (BG-0001 tree) change. New root BG-0002 gated,
  awaiting approval.
- **Produced:** DEC-0335..DEC-0345; BG-0002 (gated); IDEA-0012
  (captured); IDEA-0011 → taken-up (disposition: this session and
  BG-0002).
- **In-session reconciliation (T22-T23):** the write API's batch mode
  diverged from DEC-0314's as-a-unit intent; fixed under the DEC-0335
  path (design presented, approved, scratch-verified).
- **System-architect consultation:** offered and accepted; DEC-0293
  dual-instance debate, one rebuttal round; verdict ratified at T19
  with stakeholder amendments from T12/T14 woven in (DEC-0296
  dispositions inline in T11..T19).
- **In-session remediations:** librarian tool-surface hot-fix
  (undiscussed `memory: project` removed; root cause verified against
  documentation); memory mechanism ratified and implemented as the
  artifact-librarian-memory preloaded skill (DEC-0343).
- **Process lessons recorded to facilitator memory:** plain language
  over jargon; approval covers intent, not design.
- **Follow-on obligations (visible per BG-0002's own criterion):**
  SPEC-component agent-profile amendment (DEC-0340), conformance check
  (DEC-0341), EP + backfill Stories/CMPs derivation after BG-0002
  approval (DEC-0339, DEC-0342), standing-instruction installation for
  the guard rule (DEC-0335).

## Decisions Produced

- DEC-0335 — the no-arbitrary-builds guard rule, mechanical floor,
  build-intent intake, standing-instruction enforcement
- DEC-0336 — grounding-through-contracts as a first-class priority,
  with the minimum-reconciliation yardstick
- DEC-0337 — required research, sized to the decision, before
  build/tooling decisions
- DEC-0338 — charter BG-0002, the method track (outcomes, non-goals,
  admission predicate, absorption triggers)
- DEC-0339 — one method epic (artifact interaction surface) with two
  CMPs; distribution seam named, epic deferred to IDEA-0010 take-up
- DEC-0340 — agent-contract profile in SPEC-component, gate-enforced,
  with breaking-change list
- DEC-0341 — automated deployed-vs-contracted conformance check in the
  checker suite
- DEC-0342 — the backfill protocol for the SES-0058 deliverables
- DEC-0343 — librarian memory as a preloaded skill; tool-surface
  hot-fix ratified
- DEC-0344 — IDEA-0011 taken up; fix folded into BG-0002
- DEC-0345 — a test plan precedes any executable implementation;
  approval covers design and test plan together

## Conflicts Raised

None.
