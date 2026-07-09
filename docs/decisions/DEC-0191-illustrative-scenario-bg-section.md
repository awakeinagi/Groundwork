---
id: DEC-0191
type: decision
title: Business Goals gain a non-binding Illustrative Scenario section
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0035 @ T15-T17"
links:
  derives-from: [SES-0035]
  relates-to: [DEC-0192, DEC-0193]
  supersedes: []
---

# DEC-0191: Business Goals Gain a Non-Binding "Illustrative Scenario" Section

## Context

The stakeholder's proposed goal-grilling recipe included a "Perfect Day"
happy-path workflow and "Bad Day" edge-case questions. Both aid shared
understanding, but are solution/implementation-shaped in a way that risks
goal-level altitude discipline and creates churn if treated as binding
spec at a stage that gates on sponsor approval.

## Decision

The Business Goal template gains an **Illustrative Scenario** section: a
required, non-binding happy-path walkthrough (chronological bullets,
trigger to output) plus optional bad-path notes, captured only when they
surface naturally during the session. Never treated as a specification.
Full edge-case enumeration is deferred to Epic (Risks & Open Questions)
and Story (Acceptance Criteria) refinement.

## Rationale

Grounds shared understanding with a concrete example without dragging
implementation-detail churn into a goal-gated, hard-to-amend artifact.
Matches Groundwork's existing altitude ladder — the stakeholder's
High/Medium/Low question tiers map to BABOK's Business/Stakeholder/
Solution requirement classification, which Groundwork already implements
as separate gated artifact types (BG/EP/ST).

## Alternatives Considered

- **Require full edge-case enumeration at goal level** (the original "Bad
  Day" framing): rejected — edge-case handling is discovered
  incrementally during epic/story refinement; baking it into the BG would
  force goal-level re-affirmation for changes the sponsor never needed to
  weigh in on, undermining the gating discipline
  BG-0001's own Outcome 4 ("Parallel
  implementability") depends on.

## Implications

Epic and Story playbooks in `references/refinement-process.md` gain a
carry-forward step to pick up flagged-but-unresolved bad paths.
BG-0001 is backfilled with this section.
