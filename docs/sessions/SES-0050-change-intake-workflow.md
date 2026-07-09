---
id: SES-0050
type: session
title: Change-intake workflow — mandatory sessions, Idea artifacts, CP extension, local governance
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Session refined the change-intake workflow: the standard process by
  which change intent enters a Groundwork-managed project. Participants
  refined mandatory intake sessions with role-authority checks, clarified
  the boundary between Change Proposals and a new Idea artifact type for
  pre-classification work queuing, and resolved how governance operates
  in skill-only (non-application) projects via versioned configuration
  files. Produced 16 decisions (DEC-0252..DEC-0267) defining intake paths
  (mechanical floor, expedited, full, idea-capture), local governance
  setup, and two Ideas (IDEA-0001, IDEA-0002) parking application-side
  reflection work.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [BG-0001, ST-0035, DEC-0020, DEC-0037, DEC-0046, DEC-0047, IDEA-0001, IDEA-0002]
---

# SES-0050: The Change-Intake Workflow

Method-level session (SES-0035/SES-0047/SES-0049 precedent: fix the
method, then the instances). The stakeholder proposed a standard
workflow for how change intent enters a Groundwork-managed project —
and the session grew to cover a new pre-classification Idea artifact
type, an extension of Change Proposal semantics that unifies with
ST-0035's captured proposals, and how governance (DEC-0020 gate
policies, DEC-0037/DEC-0046 governance-as-code) operates in skill-only
projects without the application. Relates to BG-0001 as the goal whose
product must eventually reflect these method changes (parked as
IDEA-0001 and IDEA-0002, both spawned here).

## Transcript

### T1 — Stakeholder

Proposed refining the Session workflow: any time a user mentions
wanting to make a change (idea, enhancement, fix) to a project using
the Groundwork paradigm, a session should probably start. Proposed
flow, verbatim in structure: (1) user proposes the change; (2) agent
carefully restates its understanding of the proposal's intention and
asks whether to begin a Groundwork design session to incorporate it;
(3) user clarifies/adds (returning to step 2) or confirms alignment;
(4) agent grills, determining during refinement which artifact type(s)
are needed — BG, EP, ST, SP, CMP, or design elements within an
existing CMP; (5) after grilling, agent produces a detailed summary
and asks whether grilling inspired other changes; (6) if yes return to
step 4, else generate the documentation artifacts; (7) session ends.
The workflow should trigger via the agent skill or the local
AGENTS.md.

### T2 — Facilitator

Ran the status report (Mode 3; 400 artifacts) and searched the corpus
for prior intake/triage decisions. Restated the proposal as a
meta-process change, and surfaced three tensions: (1) the system
already has Change Proposal triage (mechanical fix / refinement
session / rejected) — the proposed flow hard-codes "session" as the
only path and covers trivia like typo fixes; (2) the flow is silent on
the existing machinery between grilling and artifacts (decision
confirmation, distillation, consistency checks, recall audit, gates) —
assumed layered, not replaced; (3) the inspired-ideas loop strains
one-session-one-focus when an inspiration targets a different
artifact.

### T3 — Stakeholder

Added: the agent should produce a todo list from the workflow steps to
ensure each step is followed.

### T4 — Facilitator

Restated the addition: the todo list is the flow's enforcement
mechanism, the way checklists enforce rule-type decisions elsewhere in
the method.

### T5 — Stakeholder

Clarified the core rule: "offers to open a session" must not imply
changes could happen outside one — that is not allowed under the
paradigm. Off-record discussion producing no changes is fine; the
moment the user instructs a change, a session must capture the intent
and decisions. On the tensions: (1) include a CP path in the workflow;
stated a belief that a CP is required when a change conflicts with a
pre-existing decision, and asked to be corrected if wrong; (2)
confirmed steps 4–6 implicitly include the existing machinery; (3)
agreed to grill the enrichment-vs-new-session line. Added a new topic:
distinguish dogfooding the paradigm (solo developer as god-mode
stakeholder) from the application, via a config file in the skill's
assets declaring the role — also letting non-application teams use CP
artifacts and triage locally.

### T6 — Facilitator

Restated all additions. Corrected the CP understanding: a CP captures
change proposed from *outside the refinement pipeline* (reviewer
suggestion, implementation feedback, out-of-band edit), triaged to
mechanical fix / refinement session / rejected — the boundary is
channel/provenance, not conflict; conflict with an accepted decision
is handled by supersession + staleness or a CFL. Reported that the
application's identity model (DEC-0046 person registry; ST-0022,
ST-0042) has no local/skill-level analogue yet — open ground for the
config-file idea, to stay consistent with the app model.

### T7 — Stakeholder

Accepted the correction and proposed extending CPs: they should also
capture changes attempted by someone not approved to make them — e.g.
where superseding a decision requires sign-off from a data science
lead, an engineering lead, and a product owner, a lone attempt by any
of them triggers a CP. Contrasted with this project, where superseding
a DEC needs only the stakeholder's sign-off. Teams installing only the
skill need a way to specify that configuration; agreed it should align
with the app-side model.

### T8 — Facilitator

Reported the settled ground the addition lands on: DEC-0020 already
defines fixed role-mapping and committee gate policies (the
stakeholder's example is DEC-0020's committee case); ST-0035 AC2
already requires out-of-authority statements to be captured as
proposals requiring ratification — with no concrete artifact type
named; DEC-0037's governance-as-code files are the app-side
configuration home. Framed the open question: whether the CP formally
becomes the artifact form of ST-0035's captured proposal.

### T9 — Stakeholder

Confirmed alignment; asked to begin grilling.

### T10 — Facilitator

Round 1 (recommendations first): (1) threshold — mechanical floor,
crisply defined (recommended) / mechanical fixes get a CP / no floor;
(2) provenance — session record opens at the verbatim proposal
(recommended) / starts at grilling; (3) enforcement when a user says
"skip the session" — hard rule + expedited single-round path
(recommended) / hard rule with full process always / warn-then-comply;
(4) todo list — created at session open from a template plus dynamic
topics (recommended) / at first mention / fixed static list.

### T11 — Stakeholder

(1) Mechanical floor accepted. (2) Record opens at the proposal.
(3) Hard rule + expedited path. (4) Amended: at *first mention* but
with template + dynamic content — when a change is mentioned, the
agent loads minimal items ("restate intention; confirm alignment;
start session?"); on confirmation the list expands to support the
confirmed path (grilling flow, or changes without grilling — the
expedited flow).

### T12 — Facilitator

Read-back, then round 2: (1) agent-originated change intent — same
intake, agent proposes / user disposes (recommended) / agent files a
CP / out of scope; (2) expedited sessions — all integrity steps, none
waived (recommended) / waive the recall audit / scale by blast radius;
(3) CP creation triggers — out-of-band + unauthorized only
(recommended) / every intent gets a CP / also capture declined
proposals; (4) unify CP with ST-0035 AC2's captured proposal —
yes (recommended) / keep separate.

### T13 — Stakeholder

(1) Agent proposes, user disposes. (2) All integrity steps, none
waived. (3) Mostly out-of-band + unauthorized — and proposed a new
artifact type, **Ideas** (e.g. IDEA-0001), cleanly handling new ideas
that arise during a session and require a separate one, without
convoluting the CP's purpose; also usable when a user wants to propose
an idea without grilling or generating artifacts — a session artifact
is still recorded, but no decisions need link to it. (4) Unify.

### T14 — Facilitator

Read-back, flagging the Idea type's existing neighbor (mid-session
nice-to-haves captured today as deferred stories/spikes with release
labels and triggers). Round 3: (1) IDEA vs the deferral mechanism —
pre-classification only (recommended) / replace informal deferral /
coexist by judgment; (2) enrich-vs-park line — focus-artifact test
(recommended) / ask each time / size-based; (3) the steps 5–6 loop
becomes summary → review parked IDEAs → new session per pick, never
extending the current one — yes (recommended) / same session
continues; (4) IDEA lifecycle — captured → taken-up | declined in
docs/ideas/ with checker and status-report support (recommended) /
statusless inbox note / full gated artifact.

### T15 — Stakeholder

(1) Pre-classification only. (2) Focus-artifact test. (3) Mostly
agreed, amended the framing: IDEA artifacts become *work to do* for
the project, like a draft needing refinement — when the user asks
"what is to be done?", the agent can propose starting sessions around
previous ideas; this lets users brain-dump easily when inspiration
strikes. Whenever an IDEA is generated in a session, that session's
artifact must cross-reference it, keeping provenance of the spawn
context. (4) Lifecycle accepted.

### T16 — Facilitator

Read-back, then round 4 on the local/application boundary: (1) config
home — project-level file following an app-schema subset
(recommended) / skill-level config on the operator's machine / a
section in AGENTS.md; (2) solo god-mode as bootstrap default — yes
(recommended) / ask at bootstrap; (3) local identity — declared,
git-resolved, honor system with procedural enforcement (recommended) /
per-session declaration / no local identity; (4) local multi-party —
git-mediated asynchronous coordination (recommended) / shared-session
facilitation / out of scope locally.

### T17 — Stakeholder

(1) Agreed with project-level — and proposed simply reusing the
governance-as-code files already designed in DEC-0037 and related
decisions. (2) Solo default. (3) Honor system. (4) Git-mediated.

### T18 — Facilitator

Confirmed DEC-0037 fits: `governance/roles.yaml`, `domains.yaml`,
`gate-policies.yaml` (plus `people.yaml`, DEC-0046) — versioned,
PR-edited, Arbiter-owned; the skill's bootstrap seeds these instead of
inventing a config format, and an app adoption imports them unchanged.
Round 5: (1) artifact-level classification — locate-first via
semantic search + graph trace at session open, hypothesis maintained
through grilling, confirmed at summary (recommended) / classify up
front / classify at the end; (2) changes modifying approved artifacts —
supersession/staleness machinery fires inside the intake session
(recommended) / cascade as follow-up work; (3) reflecting this
session's outcomes in the application's design — park as the first
IDEA artifacts, dogfooding the new type (recommended) / expand this
session / skip.

### T19 — Stakeholder

All three recommendations accepted.

### T20 — Facilitator

Presented the detailed grilling summary — the revised intake workflow
(trigger, todo enforcement, restate/align, path selection across
mechanical floor / expedited / full / idea-capture, locate-first
classification, focus-artifact test, in-session cascade, summary +
inspired-ideas check, integrity machinery), the Idea artifact type,
the CP extension and ST-0035 unification, local governance reuse with
solo defaults, and app-side reflection parked as IDEA-0001/IDEA-0002 —
and asked the inspired-ideas question.

### T21 — Stakeholder

No new ideas; directed artifact generation.

### T22 — Facilitator (distillation checks & recall audit)

**Consistency checks (per DEC-0157, DEC-0158)** ran over
DEC-0252..DEC-0267 immediately after recording. `sweep`: 12 ratified
citers flagged via DEC-0263/DEC-0264's relates-to (the citers of
DEC-0020, DEC-0037, DEC-0046 — CMP-0001, CMP-0004, CMP-0007, CMP-0016,
EP-0003, EP-0005, ST-0001, ST-0006, ST-0012, ST-0013, ST-0014,
ST-0021, ST-0022, ST-0042). Disposition: the new decisions *extend*
the governance model to skill-only operation without changing the
app-side semantics those artifacts rest on — additive, no
contradiction, no staleness; one standing obligation recorded: the
bootstrap governance seeds must remain a valid subset of EP-0003's
schema. `terms`: DEC-0265 shares `approved-by` with CMP-0001,
DEC-0024, DEC-0046, DEC-0235, ST-0022 — the shared frontmatter field,
used consistently; reviewed, clear, no link needed.

**Decision-recall audit** on this session (15 candidates, one Sonnet 5
judge). Findings and resolutions:

- DEC-0047 (change proposals are a first-class artifact type)
  genuinely relevant and uncited — DEC-0262 amends that type's
  creation situations and source vocabulary without naming the
  decision that established it. Resolved by amending DEC-0262
  (relates-to + Context provenance sentence) and this session's
  relates-to.
- Contract gap: DEC-0255's protocol enumerated four confirmed paths
  but never placed the authority gate — DEC-0262's fifth outcome —
  in the sequence; an implementer reading DEC-0255 alone would have
  no unauthorized-attempt branch. Resolved by amending DEC-0255: the
  authority check runs between alignment confirmation and path
  selection, ending intake with a CP when rights are lacking
  (relates-to DEC-0262 added); the skill's intake playbook and
  AGENTS.md carry the same step.
- Judge's closest near-miss, rejected: DEC-0049 (repo read allowlist
  in governance config) is the same governance-as-code file family
  DEC-0263 reuses, but governs a different concern (agent codebase
  read scope, not approval authority) — no gap.

### T23 — Facilitator (execution record)

Implemented in-session:

- **Corpus**: DEC-0252..DEC-0267 recorded; IDEA-0001 and IDEA-0002
  captured (`docs/ideas/` created) — the first Ideas, parking
  application-side reflection of this session's outcomes;
  `governance/` seeded with solo-default `people.yaml`, `roles.yaml`,
  `domains.yaml`, `gate-policies.yaml` (DEC-0263); CONTEXT.md gained
  Idea, Change Intake, Mechanical Fix, Expedited Session, and
  Focus-Artifact Test entries, the Artifact list updated, and the
  Change Proposal definition extended per DEC-0262; AGENTS.md's
  "How design changes are made" section replaced with the
  change-intake protocol, the artifact tree gaining `governance/` and
  `docs/ideas/`, and the status-lifecycle section gaining CP triage
  and Idea lifecycles.
- **Skill** (method level, per the SES-0035 precedent): SKILL.md
  gained the change-intake trigger (description + standing section),
  bootstrap now seeds `governance/` and `docs/ideas/`, and Mode-3
  work selection lists captured Ideas; refinement-process.md gained
  the §Change intake protocol, session weights (full / expedited /
  idea-capture), the focus-artifact-test grilling bullet, and the
  in-session cascade note; groundwork-system.md gained the Idea
  catalog entry and lifecycle, the extended CP entry, and the
  repository-layout additions; templates.md gained the Idea template,
  the `unauthorized-attempt` CP source, and the governance seeds.
- **Tooling**: `check_links.py` (skill + project copies),
  `status_report.py` (captured-ideas open item), and the graph,
  consistency, and coupling scripts all accept the `IDEA` prefix and
  `idea` type; the vendored `.agents/skills` copy synced.
- **Verification**: `check_links.py` → OK, 419 artifacts, 0
  violations (18 pre-existing coverage-gap warnings untouched); graph
  rebuilt (419 artifacts, 5,949 edges); all five reciprocity audits
  empty.

## Decisions Produced

DEC-0252, DEC-0253, DEC-0254, DEC-0255, DEC-0256, DEC-0257, DEC-0258,
DEC-0259, DEC-0260, DEC-0261, DEC-0262, DEC-0263, DEC-0264, DEC-0265,
DEC-0266, DEC-0267

## Conflicts Raised

None.
