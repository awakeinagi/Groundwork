---
id: DEC-0266
type: decision
title: Intake sessions classify a change's artifact level locate-first — search and graph at open, hypothesis maintained through grilling
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0266 constrains intake sessions to classify a change's artifact
  level locate-first at session open, using semantic search and graph
  trace to locate affected artifacts, then maintaining a working
  hypothesis throughout grilling that is revised as answers land and
  confirmed in the post-grilling summary. Classification is continuous
  and grounded in the existing corpus rather than the proposal's
  wording, preventing premature anchoring on unrefined framing and
  enabling level-appropriate question bank selection.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T18-T19"
links:
  derives-from: [SES-0050]
---

# DEC-0266: Locate-first classification

## Context

The intake flow's step 4 requires determining which artifact type(s) a
change lands at (BG, EP, ST, SP, CMP, or design elements within an
existing CMP). When and how is that determination made?

## Decision

At session open the agent runs semantic search and graph trace over
the change intent to **locate** the artifacts it touches, then
maintains a **working hypothesis** of the affected set and levels
throughout grilling — revising as answers land, selecting
level-appropriate question banks from it, and confirming it in the
post-grilling summary. Classification is continuous, grounded in the
existing corpus rather than the proposal's wording.

## Rationale

Grilling exists because proposals mis-state their own scope — early
one-shot classification anchors on the unrefined framing, while
end-only classification wastes the question banks (goal-bank versus
story-seam questions cannot be selected without a hypothesis).

## Alternatives Considered

- **Classify up front, then grill**: anchoring.
- **Classify at summary only**: unguided grilling.

## Implications

The intake playbook's session-open step names the search and graph
commands; the summary template confirms the final classification.
