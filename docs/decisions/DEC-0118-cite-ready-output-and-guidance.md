---
id: DEC-0118
type: decision
title: Output is two-tier and cite-ready; skill docs gain usage guidance and cookbook recipes
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T5-T6, T9, T16"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0116, DEC-0119]
---

# DEC-0118: Two-Tier Cite-Ready Output; Guidance and Cookbook Recipes

## Context

Search output must serve an agent's next action (cite, open, traverse)
without flooding its context — the same token-economy concern that
shaped armed-only trigger loading
([DEC-0106](DEC-0106-trigger-registry.md)). And agents need to know
*when* to reach for semantic search versus the graph tool.

## Decision

Results are **two-tier**: a graph-boosted **artifact ranking** on top
(per [DEC-0119](DEC-0119-hybrid-retrieval-semantics.md)), then the
exact **chunk hits** — each with artifact ID, section heading or turn
number, status, similarity score, a short snippet, and any
superseded-by redirect; deduplicated per artifact. Skill documentation
gains: a SKILL.md row routing **meaning-shaped questions** (have we
discussed X? which decision covers Y? is this a duplicate?) to
semantic search and **structure-shaped questions** (what depends on X?
why does Y exist?) to the graph, plus **cookbook recipes in the
skill's reference for the new capabilities** (participant-directed,
T16).

## Rationale

Enough to cite without opening the file; short snippets keep bundles
small. Full-section output was rejected for the exact token-waste
problem the trigger registry was designed against; paths-only output
was rejected because every search would cost follow-up reads.

## Alternatives Considered

- **File paths + scores only**: cheapest, but scores without snippets
  are unjudgeable and force follow-up reads.
- **Full section text in results**: no follow-up reads, floods agent
  context.

## Implications

SKILL.md's process-moments table and the cookbook reference
(`references/graph-queries.md`) are updated alongside the script;
`--json` output is available for programmatic use, matching the graph
tool.
