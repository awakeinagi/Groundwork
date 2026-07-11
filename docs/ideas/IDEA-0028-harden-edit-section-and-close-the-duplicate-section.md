---
id: IDEA-0028
type: idea
title: "Harden edit-section and close the duplicate-section checker gap"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Three defects surfaced mid-backfill: (a) gw_write.py's edit-
  section re-prepends the matched heading, so payloads restating the
  heading create duplicate sections, and section_span cannot
  disambiguate identical headings -- add a defensive refusal +
  duplicate-heading error; (b) check_links.py parses only the FIRST
  Design Elements section (DESIGN_ELEMENTS_RE), so duplicated
  sections and duplicated element/item definitions pass every rule
  silently, including rule 7's duplicate-name check and rule 20 --
  add a duplicate-identical-H2 rule; (c) the artifact-interact
  SKILL.md needs a usage note (payload = section body only). Batch-2
  incident + external defect alert (T18) are the evidence; librarian
  behavioral memory already carries the pitfall.
links:
  derives-from: [SES-0066]
  relates-to: [IDEA-0027]
---

## The Idea

"Harden edit-section and close the duplicate-section checker gap." Three defects surfaced mid-backfill at SES-0066 T18: (a) `gw_write.py`'s `edit-section` re-prepends the matched heading, so payloads that restate the heading create duplicate sections, and `section_span` cannot disambiguate identical headings once duplicated — add a defensive refusal for heading-restating payloads plus a duplicate-identical-heading error. (b) `check_links.py` parses only the FIRST Design Elements section (`DESIGN_ELEMENTS_RE`), so duplicated sections and duplicated element/item definitions pass every rule silently, including rule 7's duplicate-name check and rule 20's Uses: mandate — add a duplicate-identical-H2 rule. (c) the artifact-interact `SKILL.md` needs a usage note clarifying that an `edit-section` payload is the section body only, not a heading-plus-body restatement.

## Spark Context

Surfaced mid-backfill during SES-0066's serialized per-CMP write batches (T18): a batch-2 incident produced duplicated Design Elements sections in seven CMPs, self-detected and self-repaired by the batch-2 librarian before an external session's defect alert arrived; the facilitator's verification (T18) confirmed zero affected files remained and traced the root cause to the two tooling gaps above. Flagged as a capture candidate at T18, pending stakeholder disposition between capture-as-IDEA and expedited in-session fixes.

## Disposition

Pending.
