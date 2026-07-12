---
id: IDEA-0041
type: idea
title: "gw_write edit-section must guard against heading-shaped content creating unaddressable phantom sections"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-11
proposed-by: awakeinagi
overview: >-
  edit-section locates a section by first-heading-match and ends at
  the next heading; if replacement content itself contains a
  heading-shaped line, that line becomes a permanent phantom
  boundary that no later edit-section call can ever reach or remove,
  stranding duplicated content with no recovery path short of git.
  This is a recurring defect with four independently shipped/caught
  instances: SP-0015 (approved, closed at SES-0064, still
  unrepaired), SP-0016 (caught pre-commit during SES-0071, redone),
  DEC-0369/ DEC-0370/DEC-0371 (caught pre-commit, sanctioned dedup),
  and SES-0069 (shipped and committed, repaired 2026-07-12 during
  the SES-0070 close-out). Proposed fixes: (1) edit-section refuses
  content containing a heading-level line at write time, or (2) an
  occurrence-disambiguation flag / delete-section op lets an
  already-corrupted section be recovered through the write API. Per
  operator direction (2026-07-12), the fix scope is expanded to also
  cover session-close completeness: SES-0070 was closed and
  committed with placeholder "TBD." text still in required body
  sections and required frontmatter fields missing, which the write
  API's closed- session immutability gate then correctly refused to
  repair ordinarily, forcing a sanctioned direct edit. The eventual
  fix session should add a set-status-closed precondition and/or a
  checker rule for placeholder text and duplicate sibling headings
  in ratified artifacts, and should repair SP-0015's stranded
  duplication via the proper sanctioned route. Reported per refuse-
  and-report (DEC-0330); captured at operator request.
links:
  derives-from: [SES-0071]
---

# gw_write edit-section must guard against heading-shaped replacement content creating unaddressable phantom sections

## The Idea

`edit-section`'s `section_span` locates a section by scanning for the first heading line matching the given substring, then ends the span at the next heading of equal-or-higher markdown level (`gw_write.py` `Artifact.section_span`). If a caller's replacement `content` itself contains a line that looks like a markdown heading of the same or higher level (e.g. a stray `## <Section Name>` line embedded in body text), that line becomes a real, permanent heading boundary in the file once written. On every subsequent `edit-section` call targeting that same heading text, `section_span` always resolves `start` to the FIRST occurrence (the original heading) and `end` to the NEXT heading found — which is now that accidentally-introduced phantom heading, not the section's true end. The result: every corrective edit-section call only ever touches the (now-tiny) span between the real heading and the phantom one, permanently stranding whatever content already sits after the phantom heading. Because the API has no way to target a specific occurrence of a repeated heading string and no delete-range operation, the stranded duplicate content can never be reached or removed through the write API once created — it requires an out-of-band fix (e.g. git revert) that the librarian is not permitted to perform (git is off-limits, DEC-0333).

Concretely hit during SES-0071/SP-0016 write-up: replacement content for SP-0016's "Findings" and "Resulting Decisions" sections was mistakenly authored WITH the section's own `## Findings` / `## Resulting Decisions` heading line included at the top (mirroring how the sections read in the source file), rather than as pure section-body content. `edit-section` accepted it silently (no validation catches heading-shaped lines in content), embedding a phantom duplicate heading. A follow-up corrective `edit-section` call (this time with the heading correctly stripped) did not fix the file — per the mechanism above, it inserted a second full copy of the section's content ahead of the phantom heading, leaving the original heading-embedded copy stranded after it. Both sections in `docs/spikes/SP-0016-reactive-hook-loop-economics.md` ended up with fully duplicated content blocks, unfixable via any further `edit-section` call.

## Spark Context

Surfaced by the artifact-librarian mid-execution of a SES-0071 write task (recording SP-0016's Findings/Resulting Decisions and two resulting decisions DEC-0374/DEC-0375). Reported to the operator immediately per refuse-and-report (DEC-0330); the operator asked for this idea to be captured.

## Disposition

Pending. Two independent fixes would each close this gap, either is likely sufficient:

1. **Reject heading-shaped content at write time.** `edit-section` should scan `content` for lines matching `HEADING_RE` at a level less-than-or-equal to the target section's level and refuse (`REFUSED: replacement content contains a heading-level line; edit-section replaces section BODY only, not the heading — strip it`) rather than writing it silently. This prevents the phantom-heading state from ever being created.
2. **Give `edit-section` (or a new op) a way to recover once a phantom heading exists** — e.g. an `--occurrence N` flag to disambiguate repeated heading text, or a `delete-section`/`replace-whole-section-including-duplicates` op that collapses everything from the first matching heading through the LAST occurrence of that same heading text (rather than stopping at the second). Either would make an already-corrupted section recoverable through the sanctioned write path instead of requiring git.

Until fixed, the operational workaround (recorded in the librarian's memory) is: before any `edit-section` call, grep the prepared content for a leading `#`-heading line matching the target section name and strip it — the op keeps the existing heading itself, content is body-only.

**Prior shipped instance (recurring defect).** This is not a first occurrence. SP-0015 (approved, closed at SES-0064) independently carries the same signature: a duplicated `## Resulting Decisions` heading with one shared body, produced by the same edit-section phantom-heading mechanism. The identical signature was caught pre-commit on SP-0016 during this idea's own capture. With two independent shipped/caught instances, this is a recurring defect, not a one-off. The eventual fix session for this idea should also REPAIR SP-0015's stranded duplication via the proper sanctioned route (not a freehand edit), once a recovery op or corrected edit-section exists.

**Fourth shipped instance (SES-0069).** SES-0069 (closed session, committed) independently carried the same signature: a duplicated "## Decisions Produced" heading — an empty first occurrence followed by the real content in a second occurrence. Found 2026-07-12 during the SES-0070 close-out repair; repaired the same day by operator-sanctioned direct dedup (content preserved, no data loss). Instance tally is now four: SP-0015 (shipped, still unrepaired), SP-0016 (caught pre-commit, redone), DEC-0369/DEC-0370/DEC-0371 (caught pre-commit, sanctioned dedup), and SES-0069 (shipped, repaired 2026-07-12).

**Fix scope expanded per operator direction (2026-07-12).** The session-close step must verify close-out completeness BEFORE `set-status closed` runs: no "TBD." or other placeholder text remaining in required body sections (Decisions Produced, Conflicts Raised, Purpose, Transcript), and session frontmatter complete (`participant`, `participant-role`, `facilitator`, `transcript-fidelity`). Motivating instance: SES-0070 was closed and committed with Decisions Produced and Conflicts Raised still "TBD.", a stray placeholder left in Transcript, and all four of the above frontmatter fields missing; the write API's closed-session immutability gate then correctly refused the ordinary repair path (`append-turn --enrichment` cannot fix frontmatter or replace body sections), forcing an operator-sanctioned direct edit instead. Candidate enforcements for the eventual fix session to weigh: (a) a `set-status-closed` precondition in `gw_write` that checks for placeholder text and frontmatter completeness before allowing the transition, and/or (b) a `check` rule for placeholder text and duplicate sibling headings in ratified artifacts — either would have caught every instance recorded above at the gate, before commit.

