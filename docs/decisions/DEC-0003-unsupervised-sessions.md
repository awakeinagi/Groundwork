---
id: DEC-0003
type: decision
title: Refinement sessions are unsupervised from the start
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T2-T3"
links:
  derives-from: [SES-0001]
---

# DEC-0003: Refinement sessions are unsupervised from the start

## Context

Refinement sessions could begin with a technical facilitator present (lower
agent quality bar, learn what works first) or have business stakeholders
converse with the agent directly from day one.

## Decision

Business stakeholders interact with the agent directly, with no technical
facilitator in the loop, from the first release.

## Rationale

Sponsor's call at SES-0001 T3, accepting the higher bar over the facilitated
on-ramp the agent recommended.

## Alternatives Considered

- **Facilitated first** (agent's recommendation): safer learning curve,
  slower path to the target operating model.
- **Async document exchange**: written question sets; slower, no live
  refinement dynamic.

## Implications

The session agent, UI, and guardrails must be production-grade at v1: the
agent cannot rely on a human to rescue a confused session. This raises the
stakes of DEC-0005
(mediation) and DEC-0006 (gates as the
quality backstop), and shaped
DEC-0022 (v1 focuses on session
quality).
