---
id: DEC-0113
type: decision
title: The search corpus is section-level chunks plus per-turn transcript rows, with metadata columns
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T3-T4, T15"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0111, DEC-0119]
---

# DEC-0113: Section Chunks plus Per-Turn Transcript Rows

## Context

Retrieval granularity determines what a hit lands on. Whole-file
embeddings blur long sessions and component docs into single vectors;
the unit an agent actually cites is a section — or, for provenance
digging, an individual transcript turn.

## Decision

The index holds **one row per `##`/`###` section** across all of
`docs/` plus `CONTEXT.md`, **plus one row per `T<n>` transcript turn**
inside session Transcript sections. Every row carries metadata columns:
artifact ID, artifact type, status, section heading, and turn number.

## Rationale

Section hits land the agent on the right part of the right doc —
cite-ready. Per-turn rows make "who said what, when" searchable: the
POC's prior-art tests found the exact turn where clickable links were
first requested
([SES-0014](../sessions/SES-0014-clickable-cross-references.md) T1) and
where version scoping was raised
([SES-0016](../sessions/SES-0016-version-scoped-stories.md) T1), 3 for 3. The metadata columns are what make DuckDB
pre-filtering possible (verified in-session: `--type`/`--status`/
`--current` filters are plain `WHERE` clauses over these columns, per
[DEC-0119](DEC-0119-hybrid-retrieval-semantics.md)) — no additional
metadata is needed beyond what frontmatter already provides.

## Alternatives Considered

- **Whole-artifact embeddings**: simplest; hits identify the doc, not
  where in it; quality drops for long files.
- **Sections only (facilitator's original recommendation)**: turns come
  along inside their sections, but coarse — the participant upgraded to
  per-turn rows for provenance-grade recall.

## Implications

Roughly doubles row count over sections-only (922 chunks for the
current 147 docs — measured, trivial at this scale). Two chunking rules
to maintain: heading splits and the `**T<n> — <speaker>.**` turn
pattern.
