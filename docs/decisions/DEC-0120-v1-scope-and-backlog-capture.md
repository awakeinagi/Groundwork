---
id: DEC-0120
type: decision
title: v1 ships only capabilities that tested well; the rest are captured in deferred story ST-0009
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0019 @ T12-T14"
links:
  derives-from: [SES-0019]
  relates-to: [DEC-0106, DEC-0119]
---

# DEC-0120: v1 Scope Cut and Backlog Capture

## Context

The participant asked for all nine proposed hybrid capabilities to be
tested for feasibility before scoping
([SES-0019](../sessions/SES-0019-semantic-search-hybrid-tooling.md)
T12). POC 2 ran each against the real corpus and produced clear
verdicts.

## Decision

**v1 of `groundwork_search.py` ships** the tested winners: core search,
current-truth redirect, graph boost, subtree scoping, `--type`/
`--status`/`--current` pre-filters, `--turns` prior-art recall,
`similar <ID>`, and the graph-staleness warning (all per
[DEC-0119](DEC-0119-hybrid-retrieval-semantics.md)).

**Not shipped**, with POC evidence:

- **Trigger matching** — *rejected*: missed the clearest paraphrase
  (concurrent-writer statement scored 0.23 vs `TRG-0002`), and armed
  triggers already load into agent context by design
  ([DEC-0106](DEC-0106-trigger-registry.md)); the reading agent does
  this matching natively.
- **Unlinked-neighbor audit** — *deferred*: mechanically instant but
  naive output was template-similarity noise; needs tuning (count
  element-mediated links as connected; compare content sections only).
- **Glossary-drift detection** — *deferred*: flagged 14% of all chunks,
  overwhelmingly false positives.
- **Seam-candidate clustering** — *deferred*: untestable until more
  than one Component Doc exists.

The deferred three are captured in **one backlog story**,
[ST-0009](../stories/ST-0009-hybrid-search-capabilities.md)
(`deferred`, `release: backlog`; this decision is the deferral citation
per [DEC-0100](DEC-0100-scope-moves-cite-decisions.md)).

## Rationale

Ship what the evidence supports; record what it doesn't with the
evidence attached, so future revival starts from the tuning insights
instead of rediscovering them. One story rather than three: the
capabilities share the index, the graph access, and would likely be
built together.

## Alternatives Considered

- **Ship a first-cut unlinked audit marked experimental**: known-noisy
  output erodes trust in the tool's other results.
- **No capture**: session transcripts aren't a work queue; the tuning
  insights would be lost.

## Implications

[ST-0009](../stories/ST-0009-hybrid-search-capabilities.md) sits in
the backlog without a trigger subscription — revival is by want, not
by watched condition. Trigger matching is recorded as
rejected-with-evidence and should not be re-proposed without new facts.
