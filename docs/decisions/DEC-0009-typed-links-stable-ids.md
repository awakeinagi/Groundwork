---
id: DEC-0009
type: decision
title: Cross-references are typed links over stable IDs in frontmatter
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T6-T7"
links:
  derives-from: [SES-0001]
---

# DEC-0009: Cross-references are typed links over stable IDs in frontmatter

## Context

Cross-references are Groundwork's alignment backbone — the mechanism tying
implementation detail back to business intent. The linking scheme is nearly
irreversible once docs proliferate.

## Decision

Every artifact gets an immutable ID (`BG-0001`, `EP-0031`, …). Relationships
live in YAML frontmatter as a closed, typed vocabulary — `derives-from`,
`satisfies`, `depends-on`, `conflicts-with`, `supersedes`, `relates-to` —
plus `cites` for Decision citations. A link checker validates graph
integrity (no dangling refs; every work artifact traces to a goal).

## Rationale

Machine traversal (impact analysis, traceability audits, the Graph Index)
requires unambiguous semantics; inline wiki-links can't provide them.

## Alternatives Considered

- **Inline wiki-links only**: lighter to author; relationship semantics
  ambiguous, traversal unreliable.
- **Graph database as truth**: most queryable, but splits truth — resolved by
  adopting the graph as a derived index instead
  ([DEC-0010](DEC-0010-graph-index-derived.md)).

## Implications

Formalized in [SPEC-artifact-common](../specs/SPEC-artifact-common.md);
enforced by `tools/check_links.py`.
