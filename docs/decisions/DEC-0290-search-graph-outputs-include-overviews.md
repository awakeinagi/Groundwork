---
id: DEC-0290
type: decision
title: Search and graph tool outputs include overviews by default
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0053 @ T10-T11"
overview: >-
  groundwork_search.py results and the artifact-listing outputs of
  groundwork_graph.py (impact, trace, order, similar-style listings)
  include each artifact's overview by default, with a --no-overviews
  opt-out flag. Built now rather than parked: the facilitator proposed
  deferring search enrichment as an IDEA and the stakeholder overrode,
  extending scope to graph outputs as well. One search or traversal then
  frequently answers the question outright, with no follow-up file
  reads.
links:
  derives-from: [SES-0053]
  relates-to: [DEC-0284, DEC-0289, DEC-0116]
---

# DEC-0290: Search and Graph Outputs Include Overviews by Default

## Context

Search results carry ~160-character snippets and graph traversals
return bare IDs — both routinely force follow-up file reads just to
decide relevance. With overviews on every artifact (DEC-0284), both
tools can answer more questions terminally. The facilitator proposed
parking search enrichment as an IDEA; the stakeholder directed it be
built now and extended the scope to graph searches (SES-0053 @ T11).

## Decision

`groundwork_search.py` result output and the artifact-listing outputs
of `groundwork_graph.py` (`impact`, `trace`, `order`, and other
commands that emit artifact lists) include each listed artifact's
overview **by default**, with a `--no-overviews` flag to opt out.

## Rationale

The reader deciding "do I open this file?" is exactly who overviews
serve; surfacing them at the moment of listing collapses the
two-step (list, then read-to-triage) into one. Default-on with an
opt-out matches the goal — token efficiency should be the path of
least resistance; suppression is for narrow piping cases. With the
250-word cap (DEC-0286), even a k=10 result set stays far cheaper
than opening two full files.

## Alternatives Considered

- **Park as an IDEA for later take-up** (facilitator's proposal) —
  overridden by the stakeholder: build now.
- **Opt-in flag (`--overviews`)** — rejected: the efficient path must
  be the default.

## Implications

Both scripts change in the skill (and the vendored copy). The search
index need not store overviews — output enrichment reads frontmatter
at emit time, keeping the index disposable as designed. Graph `query`
(raw openCypher) output stays unenriched — its shape is caller-defined.
