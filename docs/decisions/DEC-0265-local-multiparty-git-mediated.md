---
id: DEC-0265
type: decision
title: Multi-party governance in skill-only mode is git-mediated and asynchronous
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T16-T17"
links:
  derives-from: [SES-0050]
---

# DEC-0265: Local multi-party coordination rides the repo

## Context

Teams sharing a repo with only the skill installed still need triage,
ratification, and committee sign-off (DEC-0263) — without a
centralized application to host the interaction.

## Decision

The repository is the coordination medium: CPs and gated artifacts
land as commits/PRs; each authority holder runs their own agent
session to triage, ratify, or approve — recorded in frontmatter
(`approved-by`, `approved-on`) and session records; committee gates
collect sign-offs across sessions, and PR review can carry them.
Asynchronous and lo-fi, fully auditable.

## Rationale

It needs nothing that isn't already in the paradigm — git, artifacts,
frontmatter. It also draws the paradigm/application boundary crisply:
the app's value becomes real-time facilitation, enforcement, identity,
and dashboards, not the governance semantics themselves.

## Alternatives Considered

- **Shared-session facilitation** (multiple stakeholders, one
  terminal): workable for co-located teams and not forbidden, but
  attribution rests on the transcript, and asynchronous ratification
  needs the git path anyway.
- **Out of scope locally**: contradicts the goal of teams using CP
  triage on shared repos without the app.

## Implications

Committee approval in skill-only mode may span multiple commits (one
per sign-off); the artifact reaches `approved` when the policy's role
set is satisfied. AGENTS.md documents the pattern.
