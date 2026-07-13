---
id: DEC-0490
type: decision
title: "Round-section convention"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  Each research round is an H2 section titled "Round N — YYYY-MM-DD"
  with N sequential and gapless from 1 and dates non-decreasing. Its
  required subsections are Findings, Business-Goal Applicability,
  and Goals Assessment — the met-or-unmet judgment against each
  numbered goal. Sources Added and Open Questions are optional
  subsections. Next Round Plan is required exactly when the round's
  Goals Assessment concludes goals unmet and research continuing,
  recording the targeted goals, planned queries, and source leads
  that make the loop resumable across sessions; it is omitted on a
  concluding round. Closed rounds are append-only per DEC-0448.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0448, DEC-0450, DEC-0453]
---

# DEC-0490: Round-section convention

## Context

Research proceeds in discrete passes across possibly many sessions;
the artifact needs a stable, machine-checkable convention for how each
pass is recorded, ordered, and — when work continues — resumed.

## Decision

Each research round is an H2 section titled "Round N — YYYY-MM-DD"
with N sequential and gapless from 1 and dates non-decreasing. Its
required subsections are Findings, Business-Goal Applicability, and
Goals Assessment — the met-or-unmet judgment against each numbered
goal. Sources Added and Open Questions are optional subsections. Next
Round Plan is required exactly when the round's Goals Assessment
concludes goals unmet and research continuing, recording the targeted
goals, planned queries, and source leads that make the loop resumable
across sessions; it is omitted on a concluding round. Closed rounds
are append-only per DEC-0448.

## Rationale

Gapless, date-ordered numbering makes round completeness mechanically
verifiable; the three required subsections mirror the section's job
(evidence, business relevance, loop state) exactly, and a conditional
Next Round Plan gives an interrupted loop a durable, resumable
handoff without cluttering a concluding round with irrelevant
"what's next" content.

## Alternatives Considered

An unconditional Next Round Plan on every round was considered and
rejected as noise on concluding rounds; free-form round titles without
gapless numbering were rejected because they make the checker's
completeness and ordering checks impossible.

## Implications

The checker verifies round numbering gaplessness, date ordering, the
three required subsections' presence, and Next Round Plan's
conditional presence against the round's own Goals Assessment
verdict.
