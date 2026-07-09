---
id: DEC-0197
type: decision
title: No fixed epic count; explicit split-vs-merge heuristics adopted
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  States explicitly there is no fixed or required number of epics per
  goal; the six seams are candidate cuts to consider, not a quota to
  fill. Signals for split: independent Why for each half, falls on
  opposite side of seam, zero-mutual-blocking parallelism, low coupling
  per DEC-0196. Signals for merge: persistent mutual coupling that never
  resolves, one half has no standalone outcome, scope too narrow to
  justify gate/session overhead. Constrains epic-slicing-seams.md and
  Epic playbook. Status accepted.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0036 @ T3, T5"
links:
  derives-from: [SES-0036]
  relates-to: [DEC-0194, DEC-0195, DEC-0196]
  supersedes: []
---

# DEC-0197: No Fixed Epic Count; Explicit Split-vs-Merge Heuristics Adopted

## Context

Combining a six-seam checklist
(DEC-0195) with the existing
deliverable-coverage pass
(DEC-0194) risked reading as
a mandate to maximize epic count — apply every seam to every goal
regardless of its size.

## Decision

`epic-slicing-seams.md` states explicitly that there is no fixed or
required number of epics per goal; the six seams are candidate cuts to
consider, not a quota to fill. Concrete signals are given for when to
split a candidate epic (independent "Why"s for each half; the halves fall
on opposite sides of a named seam; zero-mutual-blocking parallelism; the
the coupling check (DEC-0196) shows low
coupling) versus when to keep two candidates merged (the coupling check
shows persistent mutual coupling that never resolves; one half has no
standalone outcome of its own; the goal's total scope is too narrow to
justify the gate/session overhead of a second epic).

## Rationale

The coverage pass already pushes toward completeness (every deliverable
mapped to *an* epic); without an explicit counterweight, pairing it with
a six-seam checklist could drive artificial fragmentation on small
goals. Tying the split/merge judgment to the same mechanical signal used
to catch bad splits (mutual coupling,
DEC-0196) makes the two
decisions reinforce each other instead of duplicating guidance.

## Alternatives Considered

- **Leave epic-count guidance implicit**, trusting facilitator judgment:
  rejected — given the coverage pass already pushes toward more epics, an
  explicit counterweight was worth stating rather than left as an
  assumed judgment call that could silently drift toward
  over-fragmentation.

## Implications

`refinement-process.md`'s Epic playbook references the split-vs-merge
guidance alongside the seam catalog and the coverage pass.
