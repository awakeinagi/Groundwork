---
id: DEC-0021
type: decision
title: Sessions are 1:1; the agent synthesizes across sessions
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Each refinement session is one-on-one between participant and agent; agent
  synthesizes perspectives across sessions, detects cross-participant conflicts,
  and runs mediation flow; simpler UI, cleaner transcripts with unambiguous
  attribution essential for decided-by provenance, natural async resumability.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T10-T11"
links:
  derives-from: [SES-0001]
---

# DEC-0021: Sessions are 1:1; the agent synthesizes across sessions

## Context

Multiple stakeholders often have input on one goal. Sessions could be shared
multi-party conversations or separate 1:1 conversations the agent merges.

## Decision

Each refinement session is 1:1 — one participant with the agent. The agent
synthesizes perspectives across sessions into the target artifact, detecting
cross-participant conflicts between sessions and running the mediation flow
(DEC-0005).

## Rationale

Simpler session UI, cleaner transcripts with unambiguous attribution
(essential for `decided-by` provenance), and natural async resumability —
each participant engages on their own schedule.

## Alternatives Considered

- **Multi-party live sessions**: richer dynamics, but needs turn-taking UX
  and muddies who decided what.
- **Both from day one**: more v1 surface area than the value justifies.

## Implications

Synthesis is a first-class agent capability with its own quality bar;
Conflict artifacts are the mechanism by which disagreement between sessions
becomes visible ([SPEC-conflict](../specs/SPEC-conflict.md)).
