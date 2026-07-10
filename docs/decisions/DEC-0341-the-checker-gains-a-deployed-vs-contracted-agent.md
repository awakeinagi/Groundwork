---
id: DEC-0341
type: decision
title: The checker gains a deployed-vs-contracted agent conformance check
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T10-T11, T19"
overview: >-
  The integrity checker suite gains a conformance check: every
  deployed agent definition's effective configuration — declared
  frontmatter plus the implicit grants those fields trigger — is
  diffed against the runtime-policy section of its gated Component
  Doc; any divergence is a violation naming field, contracted value,
  and deployed value; agents without a gated CMP are findings once
  the backfill lands. Runs wherever the checker runs (pre-commit,
  CI). This is the mechanism that catches the next silent grant: the
  gate catches the first version, the diff catches every version
  after, converting BG-0002's no-ungoverned-capability outcome from
  prose into a test. Built under the DEC-0335 intake path alongside
  the DEC-0340 SPEC amendment.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0340, DEC-0335]
---

# DEC-0341: The Deployed-vs-Contracted Conformance Check

## Context

The librarian's ungoverned grant was invisible because nothing
compared the deployed definition against any approved statement of
what it should be. Both architect instances converged: a boundary
that is documented but not measured decays; the gate alone catches
nothing after the gate passes.

## Decision

The project's integrity checker suite gains a conformance check: for
every deployed agent definition (`.claude/agents/*.md`), diff its
effective configuration — the declared frontmatter fields plus the
implicit grants they trigger (per the DEC-0340 field inventory) —
against the runtime-policy section of its gated CMP. Any divergence
is a violation naming the field, the contracted value, and the
deployed value. Agents without a gated CMP are themselves findings
once the DEC-0342 backfill lands. The check runs wherever the checker
runs: before every commit and in any CI wiring.

## Rationale

This is the mechanism that catches the NEXT silent grant — the gate
catches the first version, the diff catches every version after. It
converts BG-0002's no-ungoverned-capability outcome from prose into a
test.

## Alternatives Considered

- **Gate-time review only** — protects nothing after the meeting
  ends; rejected.
- **Standalone tool outside the checker** — separate invocation gets
  skipped; the checker is already the mandatory pre-commit gate;
  rejected.

## Implications

Built under the DEC-0335 intake path (it is itself a build: short
design, approval, then implementation — likely alongside the DEC-0340
SPEC amendment since it consumes the profile's shape). The effective-
configuration computation must encode the implicit-grant table from
the T17 research and track documentation changes to it.
