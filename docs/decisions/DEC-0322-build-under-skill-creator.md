---
id: DEC-0322
type: decision
title: artifact-interact is built under the skill-creator methodology
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T5"
overview: >-
  The construction of the artifact-interact skill follows the
  skill-creator methodology: draft the SKILL.md and scripts, define
  realistic test prompts, run with-skill and baseline evaluations,
  review results with the stakeholder, and iterate — plus a
  description-optimization pass for triggering accuracy. The design
  session (SES-0057) governs what the skill is and why (DEC-0310..
  DEC-0321); skill-creator governs how it is built and verified.
  Build-level choices the session deliberately left open (exact read
  affordances and flags, batch semantics, error message formats) are
  settled inside this loop and ratified by the stakeholder through
  its review cycle.
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0313, DEC-0316]
---

# DEC-0322: Build Under skill-creator

## Context

Mid-intake, the stakeholder invoked the skill-creator skill with the
directive to use it when creating artifact-interact (SES-0057 T5).

## Decision

artifact-interact is built under the skill-creator methodology: draft,
test prompts, with-skill vs baseline evaluation, stakeholder review
iterations, and a description-optimization pass. The session's
decisions bound the design; the build loop settles the deliberately
open build-level details (affordance/flag shapes, batch semantics,
error formats) with stakeholder review.

## Rationale

The skill is itself tooling with objectively verifiable behavior —
exactly the artifact class the eval-driven skill-creator loop exists
for; it also gives the open build-level details a ratification path
without another design session.

## Alternatives Considered

- **Direct authoring without an eval loop** — faster, no measured
  verification of the context-bloat and efficiency goals; rejected by
  stakeholder instruction.

## Implications

The build produces test prompts and evals alongside the skill;
regressions in the guardrails become measurable. Cutover obligations
(DEC-0320) fold into the build's definition of done.
