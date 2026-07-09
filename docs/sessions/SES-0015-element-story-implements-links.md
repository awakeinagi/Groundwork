---
id: SES-0015
type: session
title: Element→story Implements links and percent-complete metrics
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Introduced Element→story Implements links enabling completion
  decidability and percent-complete metrics at each design level.
  Settled: mandatory `Implements:` line under each element heading
  (parseable, Graph Index emits element→story edges), gate-blocker
  validation, design completion % computable immediately (implementation
  % semantics deferred to future work), reciprocity tier-2 consistency
  check (element may only reference story whose Component Impact links
  its CMP), staleness propagates story→CMP direction only with
  element-scoped impact reporting. Reverse coverage verified via
  CMP-gate check plus corpus-wide audit.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [CMP-0001, ST-0007, DEC-0087, DEC-0090]
---

# SES-0015: Element→Story Implements Links and Percent-Complete Metrics

## Purpose

The participant proposed requiring that design elements in Component Docs
be cross-referenced to the story or stories whose implementation they
handle, to make story/epic/goal completion decidable and to enable a
percent-complete estimate per level of the design. Already settled going
in: elements are declared only via parseable `### <Name> (<type>)`
headings with no frontmatter mirror
(DEC-0087); body
cross-references must be resolvable markdown links
(DEC-0090);
stories declare doc-level story→CMP impact in their Component Impact
section; and
CMP-0001 already
names its filling stories informally in each element's Pending block.

## Transcript

**T1 — awakeinagi.** I want to add a requirement that design elements in
component docs must be cross-referenced to the story or stories that they
are handling the implementation for. These cross-references will make it
easier to decide when a story (then Epic, then Business Goal) has been
completed. And also allow us to estimate "percent complete" for each
level of the design, an important and much needed metric.

**T2 — Facilitator.** Framed the anchors above, flagged that the change
would re-amend the gated validation stories (as
SES-0012 did), and surfaced
a hidden fork: "completed" ultimately depends on implementation status,
which lives beyond the Handoff Manifest, while the design tree natively
measures only design completion. Round 1 questions with recommendations:
(1) metric semantics — recommended design completion first, edge shaped
so implementation tracking can ride it later; alternatives were
implementation completion or both defined now; (2) attachment point —
recommended a mandated `Implements:` line directly under each element
heading (parseable like the headings, Graph Index emits element→story
edges), over per-item citation suffixes or a hybrid; (3) element-side
obligation — recommended mandatory with gate-blocker (mirror of the
uncited-acceptance-criterion rule), over a declared-escape variant or
advisory-only; (4) reverse coverage — recommended a CMP-gate check plus
corpus-wide audit, over audit-only or no reverse check, noting it cannot
be a story-gate check because elements do not exist when a story gates.

**T3 — awakeinagi.** Chose **both metrics defined now** (upgrading the
recommendation: design % computable immediately, implementation %
semantics defined with the status source deferred to named future work).
Accepted the recommended `Implements:` line, the mandatory gate-blocker
rule, and the CMP-gate-plus-audit reverse coverage check.

**T4 — Facilitator.** Round 2. Surfaced a naming collision:
[SPEC-story](../specs/SPEC-story.md)'s Component Impact reads "which
Component Docs this story *implements* or modifies" — the same word in
the opposite direction. Questions with recommendations: (1) where
implementation status lives — recommended projection-side, never in
canon (Graph Index joins element→story edges with Jira story status in
v1 via the existing EP-0005
connector; per-element contract-test feed as a later
EP-0004 enhancement), over mechanical
writes into canon or story-level-Jira-forever; (2) naming — recommended
fixing **Implements** as element→story in the glossary and mechanically
rewording Component Impact to "builds or modifies", over `Realizes:` or
tolerating both directions; (3) reciprocity — recommended a tier-2
consistency check (an element may only reference a story whose Component
Impact links its CMP), over no cross-check or retiring Component Impact;
(4) staleness — recommended the Implements edge propagate staleness
story→CMP with element-scoped impact reporting, one direction only, over
an informational-only edge.

**T5 — awakeinagi.** Accepted all four recommendations.

**T6 — Facilitator.** Read back five distilled decisions in plain
language — the Implements line, the coverage check, the reciprocity
check, the percent-complete semantics, and staleness propagation — plus
the follow-through plan (spec amendments, glossary entry, Implements
lines in CMP-0001,
re-amendment of ST-0007,
checker and skill updates).

**T7 — awakeinagi.** Asked for a detailed overview of each decision
before confirming.

**T8 — Facilitator.** Provided per-decision overviews: what each decides,
why (including the DEC-0090
lesson that non-enforced conventions drift), worked syntax examples, edge
cases (helper elements inherit their parent element's stories; graduated
seam CMPs reference the stories that birthed the seam), timing (coverage
bites at CMP gate, not story gate), the equal-weighted rollup rationale
(any weighting invents precision the docs don't contain), accepted costs,
and how the five interlock (edge → falsifiable coverage → two-direction
honesty → metric arithmetic → truth over time).

**T9 — awakeinagi.** Confirmed all five decisions — record and execute.

## Decisions Produced

DEC-0092,
DEC-0093,
DEC-0094,
DEC-0095,
DEC-0096

## Conflicts Raised

None.
