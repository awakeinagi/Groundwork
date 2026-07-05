---
id: DEC-0022
type: decision
title: The v1 vertical slice is goal refinement end-to-end
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T10-T11"
links:
  derives-from: [SES-0001]
---

# DEC-0022: v1 vertical slice — goal refinement end-to-end

## Context

Everything cannot come first; a spine had to be picked for the first thing a
real stakeholder touches.

## Decision

v1 delivers goal refinement end-to-end: web Q&A session → transcript →
distilled Decisions → Business Goal doc in the git-backed store → approval
gate in the UI. No Jira sync, no epic generation, minimal Graph Index.

## Rationale

Proves the hardest and most novel part — an agent grilling business users
unsupervised ([DEC-0003](DEC-0003-unsupervised-sessions.md)) — with the
fewest integrations. Session quality is the core pain point; integrations
are known-shape work.

## Alternatives Considered

- **Full pipeline, thin everywhere**: shows the whole story early but
  starves the Q&A quality of attention.
- **Docs + Jira sync first**: de-risks integrations, defers the novel part.

## Implications

Epic sequencing follows: artifact store, session agent, gate engine, and
session UI carry v1; connectors, full Graph Index, and consolidations
follow.
