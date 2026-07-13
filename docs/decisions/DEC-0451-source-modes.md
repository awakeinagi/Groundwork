---
id: DEC-0451
type: decision
title: "Source modes"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0086"
overview: >-
  Every research effort records, at intake, which of three source
  modes governs it: the stakeholder provides a complete source list;
  the stakeholder provides a seed list and the agent expands the
  search to find more information; or the agent searches for sources
  on its own. Naming the mode up front sets the right expectation
  for how much source-discovery latitude the agent has, and gives
  the findings-review step at conclusion a clear standard to check
  the investigation's source-gathering against.
links:
  derives-from: [SES-0086]
---

# DEC-0451: Source modes

## Context

The stakeholder's T6 workflow description named three ways a research session could choose its sources; grilling round 2 (T7) confirmed the multi-file and lifecycle shape but left source handling to be captured directly from the stakeholder's description.

## Decision

Every research effort records, at intake, which of three source modes governs it: the stakeholder provides a complete source list; the stakeholder provides a seed list and the agent expands the search to find more information; or the agent searches for sources on its own.

## Rationale

Naming the mode up front sets the right expectation for how much source-discovery latitude the agent has, and gives the findings-review step a clear standard to check the investigation against.

## Alternatives Considered

Leaving source discovery undifferentiated (always "agent searches freely") was rejected — the stakeholder's description explicitly distinguished degrees of stakeholder control.

## Implications

The RSCH main file's frontmatter or research-goals section records the chosen source mode alongside the goals it governs.
