---
id: DEC-0189
type: decision
title: Business Goals gain a required Current State & Gap section
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Adds a required "Current State & Gap" section to the Business Goal
  template, positioned after Problem: what exists today to address
  this need and what specific technology/capability gap lets the
  problem persist. Applies standard gap-analysis discipline.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0035 @ T13-T14"
links:
  derives-from: [SES-0035]
  relates-to: [DEC-0190, DEC-0193]
  supersedes: []
---

# DEC-0189: Business Goals Gain a Required "Current State & Gap" Section

## Context

Retrospective on `EP-0008`'s missing predecessor found that
DEC-0001 named "backend services" as
a deliverable, but nothing in the Business Goal template forced anyone to
articulate why the current landscape didn't already cover it — the
existing **Problem** section captures business pain, not a technical
diagnosis of what's missing today.

## Decision

The Business Goal template gains a required **Current State & Gap**
section, positioned directly after Problem: what exists today to address
this (systems, manual workarounds, prior tooling, or nothing), and what
specific technology/capability gap lets the problem persist. Distinct from
Problem (the human/business pain) and from System Context's
build-vs-reuse question (per
DEC-0190, which scopes the *new*
system's own parts, not the ambient landscape).

## Rationale

This is standard Gap Analysis (As-Is vs. To-Be — TOGAF's baseline-vs-target
framing). Naming the ambient landscape's shortfall explicitly, before
committing to a solution, sharpens exactly how much needs to be built and
reduces the chance a whole deliverable category goes unaccounted for, as
happened with "backend services."

## Alternatives Considered

- **Fold into Problem as one expanded section**: rejected — conflates
  business pain (why it hurts) with technical diagnosis (why nothing
  today already fixes it), losing citation/audit granularity between two
  different kinds of claims.

## Implications

`references/templates.md`, `references/groundwork-system.md`, and
`references/refinement-process.md` in the `groundwork-design-session`
skill are updated; the question bank lives in
`references/goal-grilling-questions.md`. BG-0001 is backfilled with this
section.
