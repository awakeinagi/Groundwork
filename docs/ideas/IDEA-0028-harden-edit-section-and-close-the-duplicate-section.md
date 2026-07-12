---
id: IDEA-0028
type: idea
title: "Harden edit-section and close the duplicate-section checker gap"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Three defects surfaced mid-backfill at SES-0066 T18: (a)
  gw_write.py's edit-section re-prepends the matched heading, so
  payloads restating the heading create duplicate sections, and
  section_span cannot disambiguate identical headings; (b)
  check_links.py parses only the FIRST Design Elements section, so
  duplicated sections/elements pass every rule silently; (c) the
  artifact-interact SKILL.md needs a body-only-payload usage note.
  Absorbed into IDEA-0041's take-up at SES-0072 (DEC-0385) rather
  than worked separately: (a) and (c) are resolved by the body-only
  payload rejection at write time (DEC-0376); (b) is resolved by
  checker rule 21's duplicate-sibling-heading scan, which also
  catches duplicated Design Elements sections (DEC-0379).
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

**Taken up, absorbed into IDEA-0041's take-up (SES-0072, 2026-07-12).** Per DEC-0385, IDEA-0028 described the same root defect as IDEA-0041 (edit-section heading-restatement hardening) with two additions, both resolved by SES-0072's decisions rather than worked as a separate session: the duplicate-Design-Elements-only checker parsing loophole closes via checker rule 21 (DEC-0379), and the body-only payload contract is enforced at write time (DEC-0376) and documented in the artifact-interact SKILL.md's writing guidance. IDEA-0027 (linked via relates-to) is unaffected by this disposition.

