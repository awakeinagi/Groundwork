---
id: IDEA-0053
type: idea
title: "Decision-create should not silently permit reference-heavy bodies with an empty relates-to"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  The decision-create write operation accepted DEC-0408 with a body
  bare-citing eight artifacts while its frontmatter carried zero
  relates-to entries; nothing warned. This blinds the citer graph
  and retrieval-based recall audits to an artifact's true
  provenance. A future session should decide whether create (or the
  checker) should flag decisions whose bodies bare-cite artifacts
  absent from their relates-to. Spark: the SES-0078 decision-recall
  audit judge's finding on DEC-0408.
links:
  relates-to: [SES-0078, DEC-0408]
---

# IDEA-0053: Decision-create should not silently permit reference-heavy bodies with an empty relates-to

## The Idea

The decision-create write operation accepted DEC-0408 with a body bare-citing eight artifacts while its frontmatter carried zero relates-to entries; nothing warned. This blinds the citer graph and retrieval-based recall audits to the artifact's true provenance. A future session should decide whether create (or the checker) should flag decisions whose bodies bare-cite artifacts absent from their relates-to.

## Spark Context

The SES-0078 decision-recall audit on DEC-0408 (judge finding).

## Disposition

Pending.
