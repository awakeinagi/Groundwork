---
id: DEC-0095
type: decision
title: Percent-complete metrics — design % from docs, implementation % projection-side
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Establishes two percent-complete metrics rolled up from element-to-story
  Implements edges. Design % measures fraction of elements referencing each
  story that are design-complete (typed contract obligations met, no Pending
  content), rolled up story → epic → business goal equally. Implementation %
  joins the same structure against external Jira status, never committing
  volatile build state into canon. Stories with no referencing element read 0%
  and flag as uncovered. Both metrics degrade gracefully.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0015 @ T2-T5"
links:
  derives-from: [SES-0015]
  relates-to: [DEC-0092, DEC-0093, DEC-0010, DEC-0013]
---

# DEC-0095: Percent-complete metrics — design % from docs, implementation % projection-side

## Context

The participant wants a percent-complete estimate per level of the
design (story → epic → business goal), and a way to decide when each
level is done. "Complete" forks: design completion is computable from
the docs alone, while implementation completion needs a "built &
passing" signal from beyond the Handoff Manifest.

## Decision

Two metrics, both computed over the element→story Implements edges
(DEC-0092), both estimates rather
than project management:

- **Design %.** An element is **design-complete** when its typed
  contract obligations
  (DEC-0088) are met with no
  Pending content. A story's design % is the fraction of elements
  referencing it that are design-complete; a story with no referencing
  element is 0% and flagged uncovered (per
  DEC-0093). An epic's
  design % is the equal-weighted average over its derived stories; a
  business goal's, over its epics.
- **Implementation %.** The same rollup, with the per-story
  built-and-passing signal living **projection-side, never in canon**:
  v1 joins the Graph Index against Jira story status via the existing
  connector (EP-0005,
  DEC-0013); a later enhancement
  under EP-0004 upgrades the join to
  per-element contract-test results flowing back across the Handoff
  Manifest. No volatile build state is ever committed into design
  markdown.

## Rationale

Design % is available immediately and honestly (today every element of
CMP-0001 is Pending,
so its stories sit at 0% designed — true). Keeping implementation status
out of canon preserves the Canonical Store as pure design and matches
the projection principle (DEC-0010):
volatile external facts are joined at query time, not committed.
Equal weighting is chosen because any weighting scheme (story points,
item counts) invents precision the docs don't contain; a future
decision can refine it with real data.

## Alternatives Considered

- **Design completion only in v1** (facilitator's recommendation): the
  participant upgraded it — define both semantics now so the completion
  story is told end-to-end, deferring only the richer status source.
- **Mechanical writes of implementation status into canon**: auditable
  in git but high-churn build state in design docs, and elements have
  no frontmatter to hold it — rejected.
- **Story-level Jira only, forever**: implementation % only as granular
  and honest as manual Jira transitions — rejected as the end state,
  accepted as the v1 join.

## Implications

The Graph Index (EP-0004) owes
IMPLEMENTS edges and the two rollup queries; the per-element
contract-test feed is named future scope of that epic. Design % is
computable by the skill's graph tooling today. Implementation % joins
Jira status via EP-0005
connectors. Both metrics degrade gracefully: uncovered stories read 0%,
never unknown.
