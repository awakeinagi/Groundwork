---
id: DEC-0326
type: decision
title: Enforcement — standing instruction installed at startup plus a non-self-triggering skill
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T6-T7, T10-T11"
supersedes: [DEC-0321]
overview: >-
  The everything-mandatory delegation rule (DEC-0325) is enforced by
  two mechanisms, both stakeholder-specified. (1) Standing
  instruction: part of the groundwork-design-session startup process
  is to install — and thereafter verify — a project-level instruction
  that all agents must use the artifact-librarian to interact with
  artifacts unless the artifact-interact skill has been manually
  loaded (DEC-0327). It lives in the project's AGENTS.md Groundwork
  section AND in project-level memory, in every project using the
  Groundwork documentation paradigm — consumer projects get it at
  bootstrap, not just this repo. (2) De-triggered skill: the
  artifact-interact skill is made non-self-triggering — its
  description is written so it never auto-loads from conversational
  context; explicit load is the only way in. Supersedes DEC-0321: the
  facilitator no longer loads artifact-interact at Step 0; Step 0
  becomes "verify the artifact-librarian agent and artifact-interact
  skill are installed, with a clear error path if not." Amends the
  DEC-0322 build scope: the description-optimization pass now targets
  non-triggering rather than triggering accuracy.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0325, DEC-0327, DEC-0322, DEC-0318]
---

# DEC-0326: Enforcement via Standing Instruction + De-Triggered Skill

## Context

A mandate binding "all agents" needs a mechanism that reaches agents
which never load the design-session skill — ad-hoc main-loop agents
doing unrelated work in a Groundwork repo. DEC-0321 (facilitator
loads artifact-interact at Step 0) directly contradicts the new
sole-path stance.

## Decision

Two enforcement mechanisms:

1. **Standing instruction.** The groundwork-design-session startup
   process (bootstrap for new projects; Step-0 verification for
   existing ones) installs a project-level instruction: *all agents
   must use the artifact-librarian to interact with artifacts, unless
   the artifact-interact skill has been manually loaded.* It is
   written to the project's AGENTS.md Groundwork section and to
   project-level memory, in every project using the Groundwork
   documentation paradigm.
2. **De-triggered skill.** The artifact-interact SKILL.md description
   is deliberately written so the skill never auto-loads from
   conversational context. Explicit load is the only way to use it
   directly.

This supersedes DEC-0321. The facilitator's Step 0 changes from
"load artifact-interact" to "verify the artifact-librarian agent and
the artifact-interact skill are installed," with a clear error path
when they are not. artifact-interact remains the single source of
truth for artifact tool documentation — now read by the librarian
rather than the facilitator.

## Rationale

The standing-instruction surface (AGENTS.md + project memory) is the
one channel every agent reads regardless of which skills it loads.
De-triggering closes the back door: a skill that auto-loads on
context would silently re-create the direct path the mandate closes.

## Alternatives Considered

- **AGENTS.md only** — misses memory-driven agents; the stakeholder
  chose both surfaces at T11.
- **Keep DEC-0321** — contradicts everything-mandatory; rejected.
- **Rely on the skill's own triggering** — the exact opposite is
  needed under a delegation mandate; rejected.

## Implications

The DEC-0322 build's description-optimization pass inverts its
target: the eval now confirms the skill does NOT trigger from
context. The AGENTS.md asset and bootstrap playbook gain the
instruction. DEC-0321's prose in the design-session references is
replaced at cutover (DEC-0320 machinery, extended by SES-0058).
