---
id: IDEA-0022
type: idea
title: "Write API's post-write recheck should skip code spans/blocks like the full checker does"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  The write API's post-write recheck (Corpus.recheck in gw_write.py)
  scans frontmatter and body for bare artifact IDs without excluding
  Markdown code spans/blocks, unlike the full checker
  (check_links.py) which correctly skips them per SPEC-artifact-
  common's rule 7. This caused false-positive refusals during
  SES-0061 when a verbatim stakeholder quote contained a code-span-
  wrapped, intentionally not-yet-existing artifact ID — the full
  checker confirmed the affected files clean, but the recheck still
  refused. A related, stricter edge case surfaced while drafting
  this very idea: the code-span carve-out is scoped to body Markdown
  only, so even a backtick-wrapped ID placed inside a frontmatter
  overview field is NOT exempted by either the recheck or the full
  checker — a distinct, narrower gap from the body-only case this
  idea primarily describes. A future session should align recheck's
  ID-scanning with the full checker's code-span-aware logic for body
  content, and separately decide whether the overview field should
  ever be allowed to contain an intentionally-unresolvable token at
  all, or must always avoid the literal pattern entirely.
cites: [DEC-0315, DEC-0242]
links:
  derives-from: [SES-0061]
  relates-to: [IDEA-0014]
---

# IDEA-0022: Write API's Post-Write Recheck Should Skip Code Spans/Blocks Like the Full Checker Does

## The Idea

Verbatim: "The write API's per-operation post-write recheck (Corpus.recheck
in gw_write.py) scans frontmatter and body for bare artifact IDs without
excluding Markdown code spans/blocks, unlike the full checker
(check_links.py) which correctly skips them per SPEC-artifact-common's
rule 7."

## Spark Context

The per-op re-check that DEC-0315 layers on top of every write operation
(parseability, ID/filename match, link resolution, overview cap,
reciprocity of touched pairs) is meant to be a fast, targeted echo of what
the full checker independently guarantees — not a stricter or divergent
pass. But `Corpus.recheck` in `gw_write.py` scans body and frontmatter text
for bare artifact-ID patterns without excluding Markdown code spans or
fenced code blocks, whereas the full checker (`check_links.py`) correctly
carves those out per SPEC-artifact-common's rule 7 — the code-span
carve-out DEC-0242 establishes for bare-ID cross-references in body prose.
This caused a false-positive refusal during SES-0061: a verbatim
stakeholder quote contained a code-span-wrapped, intentionally
not-yet-existing artifact ID, and while the full checker confirmed the
affected files clean, the recheck still refused the write.

A related, stricter edge case surfaced while drafting this very idea: the
code-span carve-out is scoped to body Markdown only, so even a
backtick-wrapped ID placed inside a frontmatter overview field is NOT
exempted by either the recheck or the full checker — a distinct, narrower
gap from the body-only case this idea primarily describes.

## Disposition

Pending — awaiting take-up. A future session should align `Corpus.recheck`'s
ID-scanning with the full checker's code-span-aware logic for body content,
and separately decide whether the overview field should ever be allowed to
contain an intentionally-unresolvable token at all, or must always avoid
the literal pattern entirely.
