---
id: SES-0037
type: session
title: Story-slicing seam guidance and coupling-check generalization
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Introduced five story-slicing seams validated against established
  literature (Workflow Steps, Business Rule Variations, Simple/Complex,
  Variations in Data, Defer Performance): Data, Chronological, Fidelity,
  Logic, and Operational. Added sixth seam Operations/CRUD (artifact
  lifecycle). Generalized coupling-check script to --type {epic,story}
  mode. Validated spike pattern as native to Groundwork's SP artifact
  type rather than as a seventh seam. Updated refinement-process.md and
  SKILL.md with INVEST-grounded split-vs-merge guidance and anti-pattern
  warnings. Produced DEC-0198-DEC-0200.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [SES-0036, DEC-0198, DEC-0199, DEC-0200]
---

# SES-0037: Story-Slicing Seam Guidance and Coupling-Check Generalization

## Purpose

Continuation of the epic-slicing work
(SES-0036), one level down: guidance
for slicing an approved epic into stories (EP → STs/SPs), which the
Story playbook lacked the same way the Epic playbook lacked seam
guidance before SES-0036.

## Transcript

**T1 — Stakeholder.** Proposed story-slicing guidance: vertical slicing
as the corrected term from the start (learned from the epic-seam
terminology correction), with five named seams (Data, Chronological,
Fidelity, Logic, Operational), each with a Rule and Examples, warning
against horizontal/layer-based story splits ("Write SQL schema," "Create
API endpoint," "Design UI component").

**T2 — Facilitator.** Validated all five against Richard Lawrence's
"Patterns for Splitting User Stories" (Workflow Steps, Business Rule
Variations, Simple/Complex, Variations in Data, Defer Performance) — a
clean match, confirming these are established patterns. Flagged a
near-miss, not a real conflict: the Fidelity Seam's "basic browser alert"
example sits next to
DEC-0188,
which requires every v1 story to cite the WCAG 2.1 AA + responsive
baseline. On inspection, native browser dialogs clear that bar
automatically, so the example holds — but the caveat ("basic" means
unstyled, never sub-baseline) was worth writing in explicitly. Proposed
a sixth seam, Operations/CRUD, grounded in Groundwork's own artifact
lifecycle (draft → gated → approved → stale/superseded). Proposed
reusing (not duplicating) the epic-level coupling-check script
(DEC-0196) via a
`--type story` extension, and carrying "no fixed count" over
(per DEC-0197) grounded
in INVEST instead of re-derived language.

**T3 — Stakeholder.** Shared a supplementary source:
<https://socadk.github.io/design-practice-repository/activities/DPR-StorySplitting.html>.

**T4 — Facilitator.** Fetched and reviewed the source. It confirmed the
CRUD seam by its canonical name — Lawrence calls it "Operations
Completion" — and surfaced one pattern not yet covered: "Architectural
Spike vs. Implementation." Rather than a seventh seam, this validated
that Groundwork's existing `SP-` (Spike) artifact type already *is* this
pattern natively — a story whose real content is an investigation
should become a Spike, not an undersized story. The source also
confirmed Mike Cohn's SPIDR mnemonic (Spikes, Paths, Interfaces, Data,
Rules) as a complementary cross-reference, and supplied two pieces of
guidance worth citing directly: the anti-pattern warning against
"inventing unnecessary splits without stakeholder demand," and the
observation that splitting well helps "identify candidate components and
API endpoints" — directly relevant to Groundwork's own Component Impact
field.

**T5 — Stakeholder.** Approved proceeding on this basis.

**T6 — Facilitator.** Generalized
`scripts/groundwork_epic_coupling.py` with a `--type {epic,story}` flag
(default `epic`, preserving
DEC-0196's
documented behavior unchanged); story mode groups stories and spikes
together by their parent epic. Regression-tested epic mode against this
project's real epic set (identical output to the pre-existing script).
Smoke-tested story mode against every existing epic's story/spike set:
zero mutual coupling found anywhere, a clean validation of this
project's own story-level slicing. Wrote
`references/story-slicing-seams.md` (six seams, the
DEC-0188
caveat, the
Spike cross-reference, SPIDR footnote, and INVEST-grounded
split-vs-merge guidance citing the DPR anti-pattern warning). Wired the
seam catalog and the coupling check into `refinement-process.md`'s Story
playbook and into `SKILL.md` (reference map, and the coupling-check
paragraph generalized to cover both epic and story usage).

## Decisions Produced

DEC-0198,
DEC-0199,
DEC-0200

## Conflicts Raised

None.
