---
id: DEC-0334
type: decision
title: The librarian ships as one deliverable with the artifact-interact skill
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T8-T9"
overview: >-
  The artifact-librarian is built, evaluated, and shipped inside the
  same DEC-0322 skill-creator loop as the artifact-interact skill —
  they are one interaction surface designed together, and the
  SES-0058 amendments (non-triggering description per DEC-0326, the
  overview-writer recharter per DEC-0328) already reshape the skill
  build, so a separate follow-on build would redo the description and
  eval work. The agent definition lives in this repo's
  .claude/agents/ (with the existing project agents); the skill's
  DEC-0319 install script installs both the skill and the agent into
  a target project; and IDEA-0010's eventual plugin would bundle the
  librarian alongside the other skills and agents. Evaluation covers
  the pair: skill CLI correctness AND librarian task-contract
  behavior (distillation fidelity, refusal reporting, verbatim
  mode).
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0322, DEC-0319, DEC-0324, DEC-0326, DEC-0328, IDEA-0010]
---

# DEC-0334: One Deliverable with the Skill

## Context

The artifact-interact skill was decided in SES-0057 but not yet built
when SES-0058 designed the librarian. Sequencing question: build the
skill first as scoped, or fold the agent into that build?

## Decision

One deliverable. The librarian is built and evaluated inside the same
DEC-0322 skill-creator loop as the skill; its definition lives in
this repo's `.claude/agents/`; the DEC-0319 install script installs
skill and agent together; IDEA-0010's plugin would bundle both.

## Rationale

Skill and agent are one interaction surface — the skill's CLI shape
and the librarian's task contract constrain each other, and SES-0058
already amends the skill build (de-triggered description, DEC-0326;
recharters, DEC-0328). Sequential builds would do the
description/eval work twice.

## Alternatives Considered

- **Separate follow-on build** — cleaner sequencing on paper, double
  work in practice; rejected.

## Implications

The DEC-0322 eval set expands to cover librarian behavior. The
install script's contract (DEC-0319) grows an agents component.
