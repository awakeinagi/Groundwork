---
id: DEC-0491
type: decision
title: "Numbered research goals"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  Research Goals is a numbered list — G1, G2, and so on — and Goals
  Assessments reference goals by number, so remaining work is
  mechanically computable by an agent mid-loop. This stable
  numbering is what lets the goals-met loop (DEC-0450) and the
  round-section convention's Goals Assessment subsection
  interoperate without free-text matching.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0450]
---

# DEC-0491: Numbered research goals

## Context

A goals-met loop needs a stable way to reference "which target is
this finding for" and "which targets remain" without free-text
matching.

## Decision

Research Goals is a numbered list — G1, G2, and so on — and Goals
Assessments reference goals by number, so remaining work is
mechanically computable by an agent mid-loop.

## Rationale

Stable numeric identifiers let an agent (or the checker) diff the
goal list against every round's Goals Assessment and compute exactly
which goals remain unmet, without any natural-language matching or
stakeholder re-reading.

## Alternatives Considered

Free-text goal descriptions referenced by paraphrase were considered
and rejected: they are not machine-diffable and would force every
Goals Assessment to be manually cross-checked against the goal list.

## Implications

Goals Assessment subsections cite goals as "Gn met"/"Gn unmet" by
number; the checker can verify every numbered goal is addressed by
the final round before allowing the concluded transition.
