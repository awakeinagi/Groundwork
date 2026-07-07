---
id: DEC-0056
type: decision
title: Context assembly is a declarative recipe inside the strategy pack
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T4-T5"
links:
  derives-from: [SES-0006]
---

# DEC-0056: Declarative context recipes in packs

## Context

What the agent loads at session start (ancestor chain, sibling impact
edges, open conflicts, glossary, consolidations) differs by session type,
and context-window economy is an explicit sponsor concern
([DEC-0017](DEC-0017-consolidation-memory-layer.md)).

## Decision

Each strategy pack declares a context recipe: required graph paths,
preferred consolidations, fallback crawls, a token budget with priority
order for truncation, and whether on-demand graph-query tools are enabled
mid-session. The retrieval layer ([EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)) resolves the recipe at
session start and on demand.

## Rationale

Context behavior becomes versioned and reviewable per session type instead
of buried in code — consistent with the pack-as-plugin framing
([DEC-0053](DEC-0053-strategy-packs-as-plugins.md)).

## Alternatives Considered

- **Fixed system-wide recipe**: goal refinement and story refinement
  genuinely need different context.
- **Agent self-serve only**: first-question latency and quality suffer.

## Implications

The recipe schema joins the pack format spec; [EP-0007](../epics/EP-0007-consolidation-memory-layer.md)'s retrieval contract
takes recipes as input (impact edge [EP-0002](../epics/EP-0002-refinement-session-agent.md)→[EP-0007](../epics/EP-0007-consolidation-memory-layer.md) already recorded).
