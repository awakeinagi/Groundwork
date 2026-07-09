---
id: DEC-0157
type: decision
title: A relates-to sweep over accepted decisions' citers is required at decision distillation
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Immediately after new decisions are distilled, facilitator runs
  consistency tool's sweep on each: for every accepted decision in new
  DEC's relates-to/supersedes, tool lists that decision's ratified
  citers and facilitator reviews each for consistency with the new
  decision, recording disposition. Catches partial supersessions the
  staleness walk misses.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0027 @ T1-T3"
links:
  derives-from: [SES-0027]
  relates-to: [DEC-0137]
---

# DEC-0157: The Relates-To Sweep at Distillation

## Context

DEC-0151 partially
cancelled DEC-0048
without superseding it, and two approved artifacts
(ST-0006,
CMP-0001) kept
enumerating the cancelled operation until a judge noticed en route. The
staleness walk keys on `supersedes` alone, so a narrowing decision —
a *partial supersession* — is structurally invisible to it.

## Decision

Immediately after new decisions are distilled, the facilitator runs the
consistency tool's `sweep` on each: for every **accepted** decision in
the new DEC's `relates-to`/`supersedes`, the tool (a 1-hop reverse-cites
traversal, `groundwork_consistency.py sweep`) lists that decision's
ratified citers, and the facilitator reviews each citer for consistency
with the new decision, recording the disposition in the session like an
audit finding.

## Rationale

The existing `impact` algorithm already computes exactly this set — the
miss was a modeling gap (no typed edge for partial supersession), not
an algorithm gap. Treating `relates-to`-on-accepted as a sweep trigger
closes most of the gap at zero modeling cost, in the spirit of the
checklist discipline for rule-type decisions
(DEC-0136).

## Alternatives Considered

- **An `amends` link type feeding the staleness walk** — the structural
  fix; deferred to SP-0006
  (DEC-0159) since it changes
  the closed link vocabulary.
- **Rely on the semantic audit** — it caught this one late and as a
  side effect; contract enumeration overlap is not reliably
  content-similar.

## Implications

The skill's SKILL.md and refinement-process reference carry the step;
`scripts/groundwork_consistency.py` ships it. Replayed on the incident,
the sweep flags ST-0006,
CMP-0001, and
EP-0005 from
DEC-0151's
`relates-to` in one hop. When EP-0002
derives stories, this step is design input for the product's session
agent, like the audit before it
(DEC-0137).
