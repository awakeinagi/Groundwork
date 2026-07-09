---
id: SES-0035
type: session
title: Goal-template redesign — backend-platform epic gap retrospective and BG grilling overhaul
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Retrospective on why EP-0008 (Backend Application Platform) gap
  emerged. Root cause: domain-first epic derivation answers what it does,
  not what makes a running program; structural/cross-cutting deliverables
  go unaddressed. Redesigned BG template and goal-grilling playbook with
  two new required sections: Current State & Gap (diagnostic TOGAF-style)
  and System Context (C4-inspired boundary, six ordered questions). Added
  Illustrative Scenario guidance tiered High/Medium/Low per BABOK.
  Updated templates, playbooks, and references. Produced DEC-0189-DEC-0194.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [BG-0001]
---

# SES-0035: Goal-Template Redesign — Backend-Platform Epic Gap Retrospective and BG Grilling Overhaul

## Purpose

Triggered while starting to derive a new epic (working title `EP-0008`,
"Backend Application Platform") to cover process/service architecture, the
inbound API layer, and deployment/runtime concerns — none of which any of
the seven approved epics own. Before grilling that epic, the session pivots
into a retrospective on why the gap existed at all, then redesigns the
Business Goal template and goal-level grilling process to prevent the same
class of miss recurring. `EP-0008` itself is not derived in this session —
it remains pending.

## Transcript

**T1 — Stakeholder.** Proposed adding `EP-0008` ("Backend Application
Platform") to capture the connective tissue tying the seven domain epics
into a runnable v1 application.

**T2 — Facilitator.** Confirmed none of
EP-0001..EP-0007
covers this; searched accepted decisions for prior ground
(DEC-0121 infra ports,
DEC-0187 SSE
transport, DEC-0001/
DEC-0018
standalone-app/stack) and found the composition/runtime layer genuinely
undecided. Asked for the raw scope and the "why now."

**T3 — Stakeholder.** Scope is "all of the above" — process/service
architecture, API layer, and deployment/runtime concerns together. Why
now: need to build a working v1 of Groundwork.

**T4 — Facilitator.** Prepared a first grilling round for `EP-0008` (epic
boundary, process shape, API framework, async model) with recommendations,
ready to present.

**T5 — Stakeholder.** Interrupted before answering: asked why this never
surfaced as an epic during the original
BG-0001 →
EP-0001..EP-0007
derivation.

**T6 — Facilitator.** Traced
SES-0001/SES-0002:
the seven epics were derived directly from SES-0001's synthesis (T14),
mapping 1:1 onto the sponsor-named bounded contexts (storage, sessions,
governance, graph, connectors/identity, UI, memory). "Standalone
application" was captured only as a single goal-level constraint
(DEC-0001) and never
decomposed into its own bounded context — domain-first decomposition
answers "what does it do," not "what makes it a running program." That gap
only becomes visible once actually assembling a runnable v1, which is
where the stakeholder now is.

**T7 — Stakeholder.** Pushed further:
DEC-0001's own
Decision text literally names "backend services" as one of three
deliverables (web UI, backend services, connector integrations) — how
could a real gap exist when the requirement was written down? What
questions were skipped in the original sessions, and why did the agent not
think it necessary?

**T8 — Facilitator.** Traced where "backend services"-shaped decisions
actually landed:
DEC-0121 (infra ports)
under
EP-0001/EP-0004/EP-0007's
SES-0020,
DEC-0187 (SSE
transport) under
EP-0006's
SES-0034,
DEC-0152
(secrets storage) under
EP-0005's
SES-0026,
DEC-0163
(governance API shape) under
CMP-0004's
SES-0029 — each
answered narrowly by whichever domain epic needed it that day, never by a
question aimed at "backend services" as its own deliverable. Root cause:
SES-0001 T14's synthesis listed capability-shaped items (pipeline,
storage, governance, graph, memory) but never asked the structural
follow-up ("a standalone app has some process and API shape; what is it?")
after committing to "standalone application" in T2-T3.

**T9 — Stakeholder.** Asked to turn this into a durable fix: what
directives should the agent follow at BG/EP grilling time to prevent
recurrence?

**T10 — Facilitator.** Proposed two directives: (1) at goal refinement,
when the physical-form-factor decision commits to a real running
application, explicitly grill the application/runtime shell (composition
root, inbound API surface, process/deployment topology, background
execution) as its own concern, separate from domain capabilities; (2) at
epic derivation, run a required deliverable-coverage pass over the goal's
Decision/Scope text before finalizing the draft epic set, watching for
structural/cross-cutting deliverables that get silently treated as
covered by the union of domain epics.

**T11 — Stakeholder.** Wanted a required BG field: a high-level
description of the real-world product being built — "what are we
building," then where it lives, who interacts with it and how, what
exists vs. must be built, what existing parts need updating, what
external systems it depends on. Asked whether an established SE/PM
paradigm already covers this.

**T12 — Facilitator.** Identified the C4 model (Level 1 System Context,
Level 2 Container) and arc42's "System Scope and Context" template
section as the matching paradigm — deliberately boundary-only (no
internals), which is exactly Groundwork's existing goal/epic altitude
split, so adopting it sharpens rather than violates the "no solution
language in goals" rule. Proposed a "System Context" BG section with six
ordered questions (what, who/how, where, existing-vs-new, what changes,
external systems), directly feeding the epic-derivation coverage pass.

**T13 — Stakeholder.** Asked for a second new required field: "what
problem are we solving" / "what is the technology gap today," distinct
from the existing Problem section.

**T14 — Facilitator.** Named this Gap Analysis (As-Is vs. To-Be,
TOGAF-style) and distinguished it from both Problem (business pain) and
System Context's build-vs-reuse question (the new system's own parts) —
Current State & Gap is diagnostic: why isn't the current landscape already
sufficient. Proposed placement: Problem → Current State & Gap → Intent →
System Context → Outcomes → Scope → Constraints → Stakeholders & Roles →
Conflicts & Tensions → Derived Work.

**T15 — Stakeholder.** Supplied a full 13-question recipe tiered
High/Medium/Low (strategic vision, functional boundaries, operational
logic), plus a "Next Steps" flow ending in a visual workflow diagram for
stakeholder sign-off before technical design begins.

**T16 — Facilitator.** Matched the tiering to BABOK's requirement
classification (Business/Stakeholder/Solution requirements) and noted
Groundwork already implements that tiering as separate gated artifact
types (BG/EP/ST) — the reason Low-tier questions (edge-case/"Bad Day"
handling, full happy-path detail) shouldn't be pulled into the BG: doing
so would undo the gating benefit (independent re-approval, staleness
scoping, parallel implementability) the method exists to provide. Mapped
all 13 questions onto the emerging BG section list, folded the
visual-diagram idea into the goal-gate itself as a C4 Level 1 Context
Diagram, and produced the "Net result" section ordering.

**T17 — Stakeholder.** Approved the net-result ordering. Asked to add
Illustrative Scenario questions (happy path required, bad paths
optional); confirmed the diagram addition (C4 Level 1 always, a process
flowchart when the session yields enough detail); specified that all of
this content is "subject to change" during refinement with volatility
inversely proportional to abstraction (the least abstract, most detailed
content most likely to change); asked for the question bank to live in a
new `references/goal-grilling-questions.md`; for the BG template and
skill reference docs to gain the necessary sections; and for the diagram
feature to be documented in the goal-refinement process docs.

**T18 — Facilitator.** Implemented: `references/goal-grilling-questions.md`
(question bank, tiered); `references/templates.md` BG template (Current
State & Gap, System Context with Context Diagram/Process Flow
subsections, Illustrative Scenario, sharpened Outcomes/Constraints);
`references/groundwork-system.md` BG artifact-catalog entry synced;
`references/refinement-process.md` Goal playbook (question-bank pointer,
tier guidance, diagram-generation step), Gates section (diagram
walkthrough at BG gate), Epic/Story playbooks (deliverable-coverage pass;
carry-forward of demoted edge-case content); `SKILL.md` reference map and
Mode 2 pointer updated.

## Decisions Produced

DEC-0189,
DEC-0190,
DEC-0191,
DEC-0192,
DEC-0193,
DEC-0194

## Conflicts Raised

None.
