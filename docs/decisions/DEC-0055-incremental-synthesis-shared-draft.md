---
id: DEC-0055
type: decision
title: Synthesis runs incrementally per session close, over a shared visible draft
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T2-T3"
links:
  derives-from: [SES-0006]
---

# DEC-0055: Incremental synthesis with a shared draft

## Context

Multiple stakeholders refine the same item in separate 1:1 sessions
(DEC-0021); synthesis timing determines
how fresh conflicts are when detected.

## Decision

Synthesis runs as each session closes: the agent merges new material into
the item draft on the item branch, runs conflict detection against prior
sessions' decisions, and on divergence opens the mediation flow with the
affected participants (DEC-0005).
The evolving synthesized draft is visible to all participants for async
comment; comments enter as Change Proposals
(DEC-0047). The PR gate sees one
coherent draft plus full multi-session provenance.

## Rationale

Conflicts surface while intent is warm, not weeks later; sharing the draft
keeps participants invested without the anchoring risk of live co-editing
(sessions themselves remain independent 1:1 conversations).

## Alternatives Considered

- **Batch synthesis at the end**: conflicts surface after intent has gone
  cold.
- **Live shared document**: later participants anchor on earlier answers,
  eroding 1:1 independence.

## Implications

Session-close triggers a synthesis step in the session engine; draft
visibility and commenting are EP-0006 UI surface.
