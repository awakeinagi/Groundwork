---
id: DEC-0159
type: decision
title: An amends link type for partial supersession is evaluated by spike SP-0006, not adopted now
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  SP-0006 is a timeboxed spike evaluating amends link type: staleness
  semantics, checker rules, graph-tool support, migration of existing
  narrowing decisions, and whether the DEC-0157 sweep covers the need
  at acceptable cost. Adoption, if any, is a decision the spike
  produces. Vocabulary changes ripple through spec, checker, and graph
  tool.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0027 @ T2-T3"
links:
  derives-from: [SES-0027]
  relates-to: [DEC-0157]
---

# DEC-0159: Amends-Link Spike Opened

## Context

The structural fix for partial supersession is a typed edge — an
`amends`/`narrows` link letting the existing staleness walk see a
decision that cancels part of another. But the link vocabulary is
**closed** by design, extended only by an accepted decision and spec
change, and the edge's semantics (does `amends` stale citers the way
`supersedes` does? partially? how do checker reciprocity and the graph
tool treat it?) are not obvious.

## Decision

SP-0006 — a timeboxed spike —
evaluates the `amends` link type: staleness semantics, checker rules,
graph-tool support, migration of existing narrowing decisions
(DEC-0151→DEC-0048,
DEC-0151→DEC-0130),
and whether the DEC-0157
sweep already covers the need at acceptable cost. Adoption, if any, is
a decision the spike produces.

## Rationale

Vocabulary changes ripple through the spec, checker, graph tool, and
every future artifact; the sweep closes most of the gap today, so the
structural change deserves evidence, not reflex.

## Alternatives Considered

- **Adopt `amends` now**: fastest structural fix, but semantics decided
  under incident pressure tend to encode one incident's shape.
- **Never; sweep is enough**: plausible — and exactly what the spike
  should confirm or refute.

## Implications

SP-0006 is drafted deriving
from BG-0001 (process-level); its
findings must produce at least one decision.
