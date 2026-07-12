---
id: IDEA-0041
type: idea
title: "gw_write edit-section must guard against heading-shaped content creating unaddressable phantom sections"
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-11
proposed-by: awakeinagi
overview: >-
  edit-section located a section by first-heading-match and ended at
  the next heading; if replacement content contained a heading-
  shaped line, that line became a permanent phantom boundary no
  later edit-section call could reach, stranding duplicated content
  with no recovery path short of git. Four independently
  shipped/caught instances were recorded: SP-0015 (shipped,
  unrepaired), SP-0016 (caught pre-commit),
  DEC-0369/DEC-0370/DEC-0371 (caught pre-commit), and SES-0069
  (shipped, repaired 2026-07-12). Per operator direction
  (2026-07-12) the scope expanded to session-close completeness
  (SES-0070 closed with placeholder text and missing frontmatter).
  Taken up and resolved in SES-0072 (folding in near-duplicate
  IDEA-0028): edit-section/append-turn now reject heading-bearing
  payloads at write time (DEC-0376); an --occurrence flag and
  delete-section op provide in-API recovery (DEC-0377); ratifying
  transitions refuse duplicate headings and placeholders (DEC-0378);
  checker rules 21/22 enforce this corpus-wide (DEC-0379); session-
  close now requires complete identity frontmatter (DEC-0380) and an
  explicit zero-decision acknowledgment (DEC-0381). The corpus-wide
  sweep these rules ran found and repaired six further shipped
  instances beyond the original four; SP-0015 was repaired via the
  new delete-section op.
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

**Taken up and resolved (SES-0072, closed out 2026-07-12).** IDEA-0041 was taken up in a full grilling session, which folded in near-duplicate IDEA-0028 (DEC-0385). Resolved by ten accepted decisions: DEC-0376 (edit-section/append-turn reject heading-bearing payloads at write time), DEC-0377 (edit-section `--occurrence N` and the new `delete-section` recovery op), DEC-0378 (ratifying status transitions refuse duplicate sibling headings and placeholder text), DEC-0379 (checker rules 21 and 22), DEC-0380 (session close requires complete identity frontmatter), DEC-0381 (zero-decision session close requires an explicit `--no-decisions-ok` acknowledgment), DEC-0382 (sessions mirror produced decisions in relates-to, checker rule 23, full historical backfill), DEC-0383 (`accepted-in` ratification-site stamp on decision acceptance), DEC-0384 (create stamps allocated IDs into placeholder H1s, checker rule 24), and DEC-0385 (IDEA-0028 absorbed into this take-up). All four originally recorded instances (SP-0015, SP-0016, DEC-0369/DEC-0370/DEC-0371, SES-0069) plus six newly discovered instances found by this session's corpus-wide sweep (EP-0009, IDEA-0015, IDEA-0016, IDEA-0025, SES-0062, SP-0013) were repaired. SP-0015 — this idea's original motivating instance — was repaired via the new `delete-section` op, validating the recovery path against real corpus damage.

