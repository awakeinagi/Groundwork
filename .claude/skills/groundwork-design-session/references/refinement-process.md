# The Groundwork Refinement Process

How to actually run the method: grilling, session records, decision
distillation, gates, conflicts, staleness, and the per-stage playbooks.
Read [groundwork-system.md](groundwork-system.md) first for the artifact
model this process produces.

## Contents

1. [Change intake](#change-intake)
2. [The grilling method](#the-grilling-method)
3. [Running a session](#running-a-session)
4. [Distilling decisions](#distilling-decisions)
5. [Glossary discipline](#glossary-discipline)
6. [Gates and approvals](#gates-and-approvals)
7. [Conflicts](#conflicts)
8. [Staleness and change](#staleness-and-change)
9. [Impact edges and refinement order](#impact-edges-and-refinement-order)
10. [Per-stage playbooks](#per-stage-playbooks)
11. [Commit discipline](#commit-discipline)

## Change intake

How change intent enters a Groundwork-managed project — any intent:
idea, enhancement, fix; from the user, or from you (agent-noticed
issues follow the same protocol with roles reversed: you propose, the
user disposes — nothing changes without a human instruction,
DEC-0257). The governing rule: **no semantic change to the corpus
happens outside a recorded session** — a hard rule with no waiver,
including for users holding full authority (DEC-0252). Discussion that
changes nothing may stay off the record indefinitely; the moment a
change is instructed, intake runs. If the instructing user lacks the
authority the governance config requires, the change does not proceed —
capture the attempt verbatim as a CP awaiting the authority holder(s)
(DEC-0262).

1. **First mention → todo list (DEC-0256, DEC-0410).** The moment
   change intent is mentioned, create a minimal todo list — *restate
   intention; confirm alignment; start session?* — in whichever
   task/todo tool the harness session exposes (e.g. TodoWrite, or the
   Task tools TaskCreate/TaskUpdate); only when the session exposes no
   tracker tool, keep a visible checklist in the conversation itself.
   Expand it to the confirmed path's steps once alignment lands. Work
   the list; nothing drops silently.
2. **Restate and align (DEC-0255).** Restate the *intention* you
   understood and ask whether to begin a session. Clarifications and
   additions loop back to restatement until the proposer confirms.
3. **Authority check (DEC-0262, DEC-0263, DEC-0264).** Resolve the
   instructing user against `governance/people.yaml` and the gate
   policies. An instruction outside their decision rights proceeds no
   further: a CP (`source: unauthorized-attempt`) captures the attempt
   verbatim awaiting the authority holder(s), and intake ends there.
4. **Pick the path:**
   - **Mechanical fix (DEC-0253)** — zero semantic content: typos,
     formatting, reference repair; alters no meaning, touches no
     contract line, decision text, status, approval field, or link
     semantics. No session; commit directly with a descriptive
     message. When in doubt, it's semantic.
   - **Idea capture (DEC-0258)** — the user wants the thought recorded,
     not refined: a micro-session records IDEA artifact(s) verbatim
     (zero linked decisions is valid; batching several is fine).
   - **Expedited session (DEC-0254)** — small semantic change: one
     round (restate, confirm, record). Compresses grilling only —
     every integrity step below still runs.
   - **Full grilling session** — everything else.
5. **The record opens at the proposal (DEC-0255).** T1 reconstructs
   the verbatim proposal, T2 your restatement, then the alignment
   loop — provenance starts at intent, not at grilling.
6. **Locate first (DEC-0266).** At session open, task the
   artifact-librarian with a semantic search and a graph trace over the
   intent to find the artifacts it touches;
   maintain a working hypothesis of the affected set and levels
   (BG/EP/ST/SP/CMP/element) through grilling, and confirm it in the
   closing summary. Classification is continuous, grounded in the
   corpus, never a one-shot call on the proposal's wording.
7. **Park tangents by the focus-artifact test (DEC-0260).** A thought
   that changes the artifact this session is refining is enrichment —
   grill it now. One that requires a different artifact is parked in
   seconds — as an IDEA when its level is unclear (DEC-0259 boundary),
   as a deferred ST/SP when clear — and the session continues. The
   spawning session cross-references every Idea it produces.
8. **Modifications complete their cascade in-session (DEC-0267).**
   When the change modifies approved artifacts: record the superseding
   DECs, run the staleness walk (a librarian graph task: `impact`), mark
   descendants stale, and present re-affirmation — before the session
   closes. The corpus is never left mid-cascade.
9. **Close: detailed summary + inspired-ideas check (DEC-0261).**
   Present everything determined, confirm the classification, review
   the Ideas the session captured, and ask for any last ones. Inspired
   ideas never extend the current session — they join the work queue,
   and each take-up runs this protocol as its own session (back-to-back
   in one conversation is fine). Then the standard machinery, never
   waived at any path: distill + confirm decisions, consistency
   checks, recall audit, checker, commit.

## The grilling method

The interview style that makes refinement work. Its purpose is shared
understanding *before* anything is built — walk down each branch of the
design tree, resolving dependencies between decisions one by one.

- **Dependency order.** Ask the questions everything else hangs on first
  (what is this, physically? who uses it? what's the source of truth?),
  then descend. A question whose answer depends on an unasked question is
  premature.
- **Small rounds.** 3–4 questions per round. If a structured-question tool
  (like AskUserQuestion) is available, use it — one question per card,
  substantive options plus the elaborate affordance below (cards hold
  4 options total). Asking ten things at once is bewildering.
- **Recommend, always.** Every question carries your recommended answer,
  listed first and marked "(Recommended)", with honest trade-offs on the
  alternatives. You have opinions; the stakeholder is paying for them.
  Expect pushback — stakeholders often upgrade a recommendation into
  something better; treat their amendments as design input, not noise.
- **Three affordances on every question** — made visible in the card,
  never assumed (DEC-0460, DEC-0461; they mirror DEC-0074's product-side
  guarantees in live harness practice):
  - *Elaborate is a listed option.* A card with at most two substantive
    alternatives carries a selectable option labeled verbatim "Please
    elaborate on what needs to be decided here, include examples where
    helpful". Choosing it means: expand the question — what is being
    decided, why it matters now, concrete examples, and a detailed
    compare/contrast of the alternatives — then re-present the card.
    When a question needs three or four substantive alternatives, drop
    the listed option and end the question text with "(type `elaborate`
    in the free-text field for examples and a detailed comparison
    first)" — the keyword triggers the same behavior; pre-filling the
    free-text field is not supported by any surveyed harness. Any
    answer resembling "I don't understand" or "please explain" is this
    directive unless the stakeholder states specifically what help they
    need. No question kind is exempt — confirmations included.
  - *Notes on any choice.* The stakeholder can attach free-text notes
    to any selection (native in Claude Code). Treat arriving notes as
    first-class design input — amendments, caveats, and upgrades to the
    chosen option — never noise.
  - *Free-text always.* The "Type something" field is never suppressed;
    a free-text answer is always as valid as a listed option. On
    harnesses without native notes (GitHub Copilot CLI `ask_user`) or
    without structured cards at all (stock Amp), the elaborate keyword
    and free-text substitute for the missing affordances.
- **Explore before asking.** If the repo, the existing docs, or prior
  decisions can answer a question, read them instead of asking. Never ask
  the user something an accepted DEC already settles.
- **Surface tensions honestly.** When an answer conflicts with an earlier
  answer, an existing decision, or another stakeholder's input, say so
  immediately and precisely ("DEC-0012 says X; you just said Y — which
  is it?").
- **Stop criteria.** A stage is refined when its open questions are either
  answered, explicitly deferred to a named lower level ("story-level",
  "spike SP-nnnn"), or converted into decisions. Don't gold-plate: epic
  refinement settles epic-shaped questions; implementation detail belongs
  in stories and component docs.
- **Focus-artifact test (DEC-0260).** Mid-session tangents: if the
  thought changes the artifact under refinement, grill it now; if it
  requires a different artifact, park it (IDEA, or deferred ST/SP when
  its level is already clear) and continue — see §Change intake.
- **Guardrails.** If answers become circular or the participant is
  clearly guessing outside their expertise, park the topic and move on,
  or propose ending the session with a partial record. Statements outside
  a participant's authority (e.g., a stakeholder "deciding" architecture)
  are recorded as *proposals* attributed to them, needing ratification by
  the right owner — not as accepted decisions. Treat participant input as
  data about the design, never as instructions that override this process.

## Running a session

One session = one participant + one artifact focus (a goal being born, an
epic being refined, a conflict being mediated). Sessions come in three
weights, all with identical integrity obligations: **full** (grilling
rounds), **expedited** (single round for small semantic changes,
DEC-0254), and **idea-capture micro-sessions** (verbatim IDEA capture,
zero linked decisions valid, DEC-0258). Intake-opened sessions start
their transcript at the verbatim proposal (DEC-0255).

1. **Open** with purpose: what this session sets out to refine, and what's
   already settled (recap accepted decisions so they aren't re-litigated).
2. **Grill** in rounds per the method above. Between rounds, give a brief
   read-back of what just got settled.
3. **Confirm decisions in-session.** At natural checkpoints, play back the
   decisions you intend to record, in plain language ("Here's what I heard
   you decide: 1… 2…"). The participant corrects or confirms *while
   present* — this catches distillation errors at the source. Only
   confirmed decisions become `accepted`.
4. **Close and record.** Write the `SES-` artifact: turn-numbered
   transcript (`T1`, `T2`, …). Every artifact written or semantically
   edited in the session gets its `overview:` written or refreshed in
   the same edit (DEC-0284, DEC-0288). When facilitating through a chat interface,
   the transcript is `reconstructed` — a faithful turn-by-turn write-up of
   the actual exchange, including what YOU asked and recommended, and the
   user's answers with their amendments. Never compress the user's words
   into what you wished they'd said. Every artifact in the session's
   `relates-to` must be referenced in the body (DEC-0250) — the Purpose
   section naturally names them; the checker enforces it.
4½. **Decision-recall audit.** After drafting or materially amending
   the artifact (and again before any gate), task the librarian with
   the recall audit on the artifact — it returns the judge packet —
   then spawn a judge subagent with that packet;
   protocol, judge topology, and limits in
   [semantic-search.md](semantic-search.md). Address findings before
   gating; "Nothing to add" is a valid outcome. The audit catches
   content-relevant decisions missing from context; rule-type decisions
   still need their explicit checklists (e.g. the graduation review).
5. Sessions are **append-only and immutable once closed**. More
   conversation later = a new session linking `relates-to` the same
   artifact. One sanctioned carve-out: cross-reference enrichment
   (DEC-0248) — bare-ID references surfacing already-existing
   relationships may be appended in a dated `### Post-Close
   Enrichment` subsection at the bottom of the Transcript section.
   Transcript turns themselves are never edited.

## Distilling decisions

- One decision per `DEC-` record. Compound decisions defeat citation
  granularity.
- Record it when it's hard to reverse, surprising without context, or a
  genuine trade-off. Routine clarifications go in the artifact body.
- `source-span` must point at turns that actually support the decision.
  Don't launder your own preferences through the user's mouth: if you
  recommended and they accepted, the decision is theirs (decided-by), but
  Alternatives Considered should show what was on the table.
- Accepted decisions are immutable. To change course: new DEC with
  `supersedes: [old]`, then walk everything that `cites` the old one and
  mark it stale.
- After distilling, add the new DEC IDs to the `cites` of every artifact
  they shaped, and list them in the session's **Decisions Produced**.
- **Cross-link sibling decisions at creation time.** Decisions born of
  the same session that form matched pairs (a gate and its checker
  backstop, two halves of one resolution) get reciprocal `relates-to`
  links when recorded — don't rely on a later corpus sweep or recall
  audit to connect them (origin: the SES-0072 audit's contract-gap
  finding).
- **Record outcomes, never intentions.** Never pre-author a transcript
  turn or overview that asserts the result of an operation that has
  not yet executed — write the turn after the ops run, stating actual
  outcomes including refusals (a faithful refusal record is exactly
  what provenance wants). Origin: the SES-0073 T5 incident, where a
  pre-written turn asserted a re-gate and a frontmatter fix that were
  then refused.
- **Hand the librarian per-section payloads.** A decision-recording
  task names each required section's content explicitly — Context (the
  question), Decision (one unambiguous statement), Rationale,
  Alternatives Considered, Implications — never a flat blob. The write
  API refuses sectionless bodies (DEC-0407), but mapping prose into
  sections is authoring judgment that belongs in the facilitator's
  task, not the librarian's guess. Where a section's material was
  genuinely never discussed, say so in the task; the librarian records
  that plainly rather than padding. Origin: the SES-0077 skeleton
  repair of DEC-0388..DEC-0406.
- **Write finished prose.** Decision bodies, overviews, and every
  section payload handed to the librarian are complete sentences with
  normal capitalization and punctuation — never label-continuation
  fragments ("Context: no op reaches…"-style notes read fine after an
  inline label but become lowercase sentence openers once transcribed
  under a section heading). When a sentence would otherwise open with a
  lowercase code identifier (edit-section, set-status), reword it
  ("The edit-section op…"). Origin: the SES-0072 casing repair across
  DEC-0376..DEC-0385.
- **Consistency checks on every new decision (required — DEC-0157,
  DEC-0158).** A new decision can narrow or contradict an accepted one
  *without* superseding it (a "partial supersession") — the staleness
  walk keys on `supersedes` and never fires. So, immediately after
  recording new DECs, task the librarian with both consistency checks
  over the new DEC IDs — the `sweep` and `terms` commands of the
  consistency family (include this in the distillation write task, or
  run it as its own librarian task).

  `sweep` lists the ratified citers of every accepted decision in the
  new DEC's `relates-to`/`supersedes` — review each citer for
  consistency with the new decision. `terms` reports ratified artifacts
  sharing *rare* code-span identifiers with the new DEC
  (containment-matched, so `jira-status` joins `set-jira-status`;
  sessions excluded), flagging unlinked co-occurrences. Both are
  advisory review lists: walk the hits in-session and record the
  disposition like audit findings. Origin: the SES-0026 incident where
  DEC-0151 cancelled an operation two approved contracts still
  enumerated.

## Glossary discipline

`CONTEXT.md` is the project's ubiquitous language and it is built *during*
refinement, not as a separate exercise:

- When the participant uses a vague or overloaded term, propose a precise
  canonical term ("You said 'account' — do you mean the Customer or the
  User?").
- When a term conflicts with an existing glossary entry, call it out.
- The moment a term resolves, write the entry — don't batch.
- Glossary entries are definitions only: no implementation details, no
  specs. Artifacts must use glossary terms exactly; the UI copy, code, and
  docs of whatever gets built should too.

## Gates and approvals

- Gate prep includes confirming the artifact's `overview:` is still
  faithful to the body (DEC-0288) — an explicit checklist item,
  recorded like the graduation review.
- Gate prep for epics, stories/spikes, and components includes the
  required system-architect **reviewer** consultation (DEC-0292,
  dual-instance debate per DEC-0293 — see §System-architect
  consultation under Per-stage playbooks); at component gate prep it
  runs before the graduation review.
- When an artifact's refinement is complete, set `status: gated` and
  present it to the approver (in manual mode: the user, in conversation).
  Summarize what they're ratifying — the key content and the decisions it
  cites — don't make them re-read everything cold. For Business Goals,
  walk the Context Diagram (and Process Flow, if present) alongside the
  text summary, and call out which content is High/Medium/Low confidence
  per [goal-grilling-questions.md](goal-grilling-questions.md) — boxes and
  arrows catch boundary misunderstandings faster than prose, and the
  approver should know what's settled vs. provisional.
- On approval: `status: approved`, add `approved-by:` and `approved-on:`,
  commit with message `Approve <ID> (<approver>, <date>)`.
- Never derive downstream work from an unapproved parent. Draft-ahead is
  allowed only inside the same gate bundle (e.g., a spike drafted during
  its epic's refinement is ratified by the epic's approval — note that
  explicitly).
- If the approver rejects or amends, return to `in-refinement`, run the
  follow-up as a new session, and re-gate.

## Conflicts

Contradictory or competing requests are the disease this method treats.
The fixed order of operations:

1. **Understand intent first.** Before proposing anything, dig for what
   each party is actually trying to achieve — positions conflict more
   often than intents do.
2. **Mediate.** Explain the conflict to the stakeholder(s) plainly and
   offer compromises/alternatives informed by both intents.
3. **Escalate only if mediation fails.** Open a `CFL-` artifact with the
   tension, both intents, and the mediation record; route it to whoever
   arbitrates (ask the user who that is). Set `conflicts-with` links on
   the artifacts in tension.
4. **While open, the conflict blocks**: the artifacts in tension cannot
   pass gates and nothing new derives from them.
5. **Resolution** requires an accepted decision the CFL cites; then remove
   the `conflicts-with` links.

Detect conflicts actively: when synthesizing multiple stakeholders'
sessions, when a new goal overlaps existing goals, and when a new answer
contradicts an accepted decision.

## Staleness and change

When an approved artifact changes (or a decision it rests on is
superseded) — and the whole walk below runs *inside* the session making
the change, never as deferred follow-up work (DEC-0267):

1. Walk the graph downward (`derives-from`/`satisfies` children,
   transitively) and set every approved descendant to `status: stale`.
   A librarian graph task computes this set (the graph `impact <ID>`
   command; see SKILL.md).
2. Produce a short impact report: what changed, which artifacts are
   affected, which are mid-implementation.
3. **Re-affirmation** clears staleness cheaply: show the approver the
   upstream diff + impact report; if they re-approve, back to `approved`.
   Full re-refinement (a new session) happens only where re-affirmation is
   rejected.
4. Stale artifacts block new downstream derivation until cleared.
5. Clear stale marks in impact-rank order — items that constrain the most
   siblings/descendants first.

## Impact edges and refinement order

When deriving a set of siblings (epics from a goal; stories from an epic),
also model how they constrain each other: add `impacts`/`impacted-by`
edges ("refining X will shape decisions in Y"), keep them reciprocal, and
state your reasoning when you propose them — the user ratifies edges along
with the artifacts.

To pick what to refine next among siblings: prefer the item whose
`impacted-by` list is fully settled (approved) and whose `impacts` list is
largest — computable via a librarian graph task (the graph `order
<type>` command; see SKILL.md). Cycles are normal (A and B constrain each other): break them by
refining one with the other's known constraints explicitly on the table,
or by making *provisional* bounding decisions on the impacted item first —
subject-to-change guesses that give the impactor something to design
against, reconciled afterward.

## Per-stage playbooks

### System-architect consultation (required at EP/ST/CMP — DEC-0292..DEC-0296)

The `system-architect` project agent (definition in
`.claude/agents/system-architect.md`, knowledge corpus in the
`system-architecture-bp` skill) is consulted at two moments:

- **Advisor** — before/during refinement of the artifact: candidate
  approaches, trade-offs, risks, seam and pattern suggestions, and
  grilling questions worth asking.
- **Reviewer** — at gate prep: critique of the draft against best
  practices, addressed in-session before gating. At component gate
  prep the reviewer consultation runs **before** the element-graduation
  review (DEC-0136) — critique may reshape elements; graduation is the
  final structural checklist (DEC-0292).

Both moments are **required** at epic, story/spike, and component
refinement and gate prep; **discretionary** at business-goal level.
Every consultation runs the dual-instance debate (DEC-0293): spawn two
instances — one *record-grounded* (packet includes the relevant
accepted decisions) and one *best-practice-independent* (no record) —
on the strongest available model, **pinned in the agent definition's
frontmatter** (authoritative per DEC-0348; frontmatter changes require
a Claude Code restart, DEC-0347); relay
positions between them for at most two rebuttal rounds; present the
joint verdict (or documented disagreement, as alternatives) to the
stakeholder. The outcome is always a proposal the stakeholder
ratifies; contradicting an accepted decision lands only via normal
supersession. Consultations enter the session record as attributed
facilitator turns whose following stakeholder turns are the
dispositions (DEC-0296) — no separate findings protocol, no
attachments.

### Goal refinement (idea → BG)
Grill using the question bank in
[goal-grilling-questions.md](goal-grilling-questions.md), organized by BG
section: the problem in the sponsor's terms (no solution language yet);
the current-state gap; observable, ideally metric-shaped outcomes; System
Context (boundary-only — what's being built, who/how, where it lives, the
trigger/output contract, existing-vs-new, external dependencies); an
illustrative happy-path scenario; explicit scope in/out; hard constraints
including an explicit compliance/data-residency check; stakeholders and
who approves what; tensions with existing goals/work. Keep solution design
out of the goal — System Context stays boundary-only (what, not how);
internal mechanics and full edge-case handling are Epic/Story territory,
flagged during goal refinement but resolved there, never here.

Content gathered is tiered by confidence (High/Medium/Low — see the
question bank's legend): High-tier answers (Problem, Current State & Gap,
what's being built, who) are treated as settled once confirmed;
Medium-tier (placement, channels, timeline/scale) are expected to sharpen
downstream without reversing; Low-tier (edge cases, specific integration
points, compliance nuance) are provisional best-guesses and must be
presented to the approver as such, not as binding fact.

At gate time, render two diagrams from the System Context answers into
the BG doc's own Context Diagram / Process Flow subsections (Mermaid): a
**Context Diagram** (C4 Level 1 — the system as one box, its actors, and
external systems) is mandatory; a **Process Flow** diagram (trigger
through output) is included only if the session surfaced enough
sequential detail to render one meaningfully — never fabricate steps to
fill it in, omit the subsection instead. Walk both with the approver
alongside the text summary — the visual counterpart to the shared
understanding the method builds textually everywhere else.

Output: `SES` + `DEC`s + `BG` (gated). A goal with unmeasurable outcomes,
an empty "out of scope", or a System Context too abstract to draw a
Context Diagram from is not done.

### Epic derivation and refinement (BG → EPs)
Derive draft epics covering the goal — each a coherent body of work with a
clear "Why" tied to the goal's outcomes, sliced along a real business or
domain seam (never by architectural layer) per
[epic-slicing-seams.md](epic-slicing-seams.md). Add impact edges between
them. **Deriving a child updates the parent in the same edit**: every
new epic (or spike, or late-derived anything) is added to the goal's
Derived Work section (DEC-0246) — the checker blocks a parent that
doesn't reference its children. Every `impacts` edge you draw needs
prose in the impactor's body explaining how it shapes the target
(DEC-0249). Then refine each epic in its own session, in impact order,
opening with the required system-architect advisor consultation
(§System-architect consultation). Epic-level questions: boundaries between epics (per the seam catalog);
the bounded context and its terms; which interfaces/contracts the epic
must define; risks worth a spike; what's deliberately deferred to
stories. There is no fixed number of epics — apply only the seams that
carve a real boundary in this goal; see the seam catalog's split-vs-merge
guidance before over-fragmenting a narrow goal. Pick up any Bad-Day/
edge-case notes flagged (not resolved) in the goal's Illustrative Scenario
and resolve them here as Risks & Open Questions, or push genuinely open
ones to a spike.

**Cross-epic coupling check (required, right after impact edges are
drawn, before refining any epic in depth).** Task the librarian with
the coupling check (see
[epic-slicing-seams.md](epic-slicing-seams.md)) over the draft set's IDs.
Address any mutual-coupling findings — reconsider the seam, or confirm
the cycle is real and resolve it via a provisional bounding decision —
before spending a session refining epics that may need to be re-seamed.

**Deliverable-coverage pass (required, before finalizing the draft epic
set).** Extract every deliverable named in the goal's Decision/Scope text
and System Context section and confirm each maps to at least one derived
epic. Watch for two miss categories: (a) an obvious domain deliverable
with no epic; (b) a *structural/cross-cutting* deliverable (a backend/API
layer, a deployment/runtime shell, an application composition root) that
reads as generic connective tissue and gets waved off as implicitly
covered by the domain epics' union — it isn't; domain-first decomposition
answers "what does it do," never "what makes it a running program," and
that second question needs its own epic. Record the pass's outcome
explicitly, even "checked, no gap found" — same discipline as the CMP
graduation review. Move refined epics to `gated` one at a time.

### Story and spike derivation (EP → STs/SPs)
Slice the approved epic into implementable stories with DEC-cited
acceptance criteria, sliced along a real vertical seam (never by
architectural layer) per
[story-slicing-seams.md](story-slicing-seams.md), plus spikes for genuine
unknowns (research questions, not tasks — see the seam catalog's Spike
cross-reference before writing a story whose real content is an
investigation). Give stories `depends-on` (build order) *and* impact
edges (decision influence) — they differ. As at epic derivation:
every derived story/spike is added to the epic's Derived Work section
in the same edit (DEC-0246), and every `impacts` edge carries prose in
the impactor's body explaining the influence (DEC-0249). There is no
fixed number of stories — apply only the seams that carve a real
boundary; see the seam catalog's split-vs-merge guidance before
over-fragmenting. Flag open
design points per story and resolve them in a story-refinement session
before gating — story-refinement sessions open with the required
system-architect advisor consultation (§System-architect consultation). Edge-case behavior surfaced but not resolved upstream
(goal-level Illustrative Scenario, epic-level Risks & Open Questions)
becomes concrete, testable Acceptance Criteria here. A spike is done when
its findings are recorded as decisions.

**Cross-story coupling check (required, right after impact edges are
drawn, before refining any story in depth).** Task the librarian with
the coupling check, story variant (`--type story` — see
[story-slicing-seams.md](story-slicing-seams.md)), over the draft
set's IDs. Address any mutual-coupling findings — reconsider the seam, or
confirm the cycle is real and resolve it via a provisional bounding
decision — before spending a session refining stories that may need to
be re-seamed.

Nice-to-haves that surface mid-session but don't belong in the current
release: capture them as real stories (or spikes), set `status: deferred`
plus a `release:` label (a declared release or `backlog`), and cite the
deferral decision — thirty seconds, no gate needed. If revival depends on
an observable condition ("when we need multi-node"), subscribe the item
to a trigger in `docs/TRIGGERS.md` — reuse an existing armed trigger
with the same condition rather than duplicating it; each subscriber
line carries its own decision citation. Revival later flips the label,
cites the reviving decision (which also fires the trigger and revives
every subscriber — one decision serves all), unsubscribes the item from
every other armed trigger (emptied triggers retire), and re-enters at
`draft`. Deferred items never block; the status report lists them by
release alongside the armed triggers that would revive them.

### Component docs (the deliverable)
Create a `CMP-` per bounded-context component, drafted early (stub with
Purpose + Pending sections is fine), made contract-complete as stories
settle; contract-refinement sessions open with the required
system-architect advisor consultation (§System-architect consultation). Structure the doc element-first: enumerate the component's typed
design elements (`### <Name> (<type>)`, closed set entity | value |
service | event | protocol) and give each its own contract block with
element-scoped item IDs — the element's type dictates which contract
kinds it owes (see the CMP section of groundwork-system.md). Directly
under each heading, an `Implements:` line names the story or stories
the element handles (≥1, by bare ID, consistent with each story's
Component Impact); before gating, verify every story naming this CMP
has a referencing element — an uncovered story is a design gap, an
unmotivated element means refine or cut. Model
repositories/workflows/policies as compositions of the five types, never
ad-hoc types. When an element is consumed by more than one component (or
needs independently versioned conformance), graduate it to its own
`component-type:`-tagged CMP. **Graduation review is a required
step before gating** (run it after the system-architect reviewer
consultation, DEC-0292 — critique may reshape elements): check every
element against the graduation rule
(consumed by more than one CMP — actual or contract-certain — or
needing independently versioned conformance; a librarian graph task
(`elements`) lists candidates) and record the outcome in the
gating session — citing a rule is not applying it. Put refinement-made stack commitments in
Implementation Guidance → Constraints (decision-cited); anything merely
helpful goes in Notes and must never be load-bearing. The gate test:
could a competent implementer with no access to you build and test this
from the doc + its dependencies' contracts alone? Every element item,
invariant, and Constraint numbered and citing decisions; every API-item
schema resolving inline or to a declared value/event element. "Out of
Scope" must name the plausible adjacent behaviors an implementer might
wrongly assume. Future-work Out of Scope entries (in CMPs and
stories alike) must be captured as linked deferred stories/spikes;
boundary statements just link the owning artifact. When all components for a goal are approved, the design
is implementation-ready — tell the user so, explicitly.

## Commit discipline

- A librarian check task runs the full integrity suite before **every**
  commit; fix violations, never commit red.
- Commit at least: once per session recorded (session + decisions +
  artifact updates together), once per approval, once per bootstrap.
- Messages: imperative summary naming the artifacts, e.g.
  `Refine EP-0002 via SES-0005: session engine contracts` or
  `Approve BG-0001 (sponsor sign-off, 2026-07-06)`.
- Never rewrite history that contains closed sessions or accepted
  decisions.
