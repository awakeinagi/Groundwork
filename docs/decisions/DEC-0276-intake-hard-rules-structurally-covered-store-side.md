---
id: DEC-0276
type: decision
title: The store already structurally enforces the no-session and mechanical-floor rules — no EP-0001 change
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0276 constrains IDEA-0001's scope by noting that the store already
  structurally enforces DEC-0252 and DEC-0253: the write topology makes
  sessionless semantic change abnormal via per-session worktrees and gate
  PRs; the only sessionless write path is the closed typed
  mechanical-operation set, which is exactly the mechanical floor; and
  tier-2 checks verify decisions derive from sessions or spikes. No
  EP-0001 changes are needed; the correspondence is noted in amended
  stories.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T4-T5"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0030, DEC-0033, DEC-0252, DEC-0253]
---

# DEC-0276: DEC-0252/0253 are structurally covered store-side

## Context

Does DEC-0252 (no semantic change outside sessions) need new
store-side enforcement in the application, expanding IDEA-0001's scope
into EP-0001?

## Decision

No. The write topology already makes sessionless semantic change
abnormal: every session's writes land in a per-session worktree
(DEC-0030) and flow through human-approved gate PRs, the only
sessionless write path is the closed typed mechanical-operation set
(DEC-0033) — which is exactly DEC-0253's mechanical floor, already
typed — and the tier-2 check suite verifies decisions derive from a
session or spike (CMP-0001 CheckSuite.B-1). The affected set stays
EP-0002 + EP-0006 (plus spec files); the correspondence is noted in
the amended stories rather than mechanized.

## Rationale

Adding a check for a rule the topology already enforces buys
belt-and-braces at the price of CMP-0001 amendments and their cascade.
If a real bypass is ever found, hardening can arrive as its own
intake.

## Alternatives Considered

- **Explicit tier-2 check** rejecting semantic diffs that trace to no
  session: expands the change into EP-0001 for no live gap.
- **Defer to component refinement**: leaves this session's
  classification of the affected set ambiguous — what DEC-0266 says to
  resolve before close.

## Implications

EP-0001, ST-0002, ST-0006, ST-0007, and CMP-0001 are untouched by
IDEA-0001's take-up.
