---
id: IDEA-0069
type: idea
title: "Recall-audit judge packet should carry provenance edges for the considered set"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-13
proposed-by: judge (SES-0093 recall audit)
overview: >-
  The SES-0093 recall audit's judge found the packet unfalsifiable
  on its own provenance-chain instruction: it supplies IDs and
  overviews but no cites/supersedes/superseded-by edges for the
  considered set. Proposed remedy is to include those edges in the
  judge packet.
links:
  relates-to: [SES-0093]
---

# IDEA-0069: Recall-audit judge packet should carry provenance edges for the considered set

## The Idea

The SES-0093 recall audit's judge reported a contract gap in the audit machinery itself: judge_instructions require following citation chains before flagging a candidate ("a decision already carried by a cited decision's provenance is NOT missing"), but the packet supplies only IDs for the considered set and overviews for candidates — no cites, supersedes, or superseded-by edges — while also instructing the judge to work from the packet alone. The provenance-chain test is therefore unfalsifiable from the packet as constructed. Proposed remedy: include at least the cites/supersedes/superseded-by edges for the considered set in the judge packet.

## Spark Context

Raised by the recall-audit judge during SES-0093's close-out audit of the session's decision set, as a separately reported finding about the audit tooling itself rather than the corpus content under review.

## Disposition

Captured; not yet taken up.
