---
id: DEC-0337
type: decision
title: Research into the option space is required before build/tooling decisions, sized to the decision
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T12-T14, T17"
overview: >-
  Any tooling or technology decision requires a documented option
  survey before the decision: what options exist, what each does,
  which matter for the proposal. Sized to the decision — from a web
  search of official documentation recorded in the session (the
  agent-frontmatter lookup that verified memory: auto-grants
  Read/Write/Edit is the model) up to a full Spike for open
  questions. The grilling then covers every surveyed option
  explicitly; an unsurveyed option chosen silently is a process
  violation. Exists because a ten-minute lookup would have prevented
  the SES-0058 drift entirely.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0336, DEC-0340]
---

# DEC-0337: Required Research, Sized to the Decision

## Context

SES-0058 chose an agent's configuration without anyone asking "what
are the configuration options for an agent, and what does each do?" A
ten-minute documentation lookup — performed only later, in this
session — revealed that the `memory:` field silently grants
Read/Write/Edit, which was the entire drift. The stakeholder at T12:
research into the available options was in order, and this research
should be a core part of our flow.

## Decision

Any decision about tooling or technology in a Groundwork project
requires a documented survey of the option space BEFORE the decision
is made: what options exist, what each does, which are relevant to the
proposal. The survey is sized to the decision — as light as a web
search of official documentation recorded in the session (the agent
frontmatter lookup at T17 is the model), up to a full Spike
(question → method → findings → decisions) for genuinely open
questions. The subsequent grilling covers every surveyed option
explicitly; an unsurveyed option chosen silently is a process
violation.

## Rationale

The T17 lookup would have prevented the incident had it run in
SES-0058. Spikes already exist as Groundwork's research container;
what was missing was the obligation and the recognition that
research can be minutes, not days — the ceremony must not deter the
lookup.

## Alternatives Considered

- **Always a formal Spike** — heaviest paper trail, deters
  five-minute lookups; rejected at T14.
- **Facilitator judgment** — that was the status quo that produced
  the incident; rejected.

## Implications

The design-session references gain the research step at build/tooling
decision points. Survey results enter the session transcript (or the
Spike) so the contract (DEC-0336) can cite them. The T17 field
inventory becomes the seed content for the DEC-0340 checklist.
