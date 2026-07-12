---
id: SES-0072
type: session
title: "Take up IDEA-0041 — edit-section phantom-heading guard, recovery path, and session-close completeness gate"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
participant: awakeinagi
participant-role: stakeholder
facilitator: "Claude (Fable 5)"
transcript-fidelity: reconstructed
kind: full
intake:
  origin: idea
  proposed-by: awakeinagi
  source-ref: IDEA-0041
overview: >-
  Six-item scope (T6-T9, expanded from IDEA-0041's original three):
  (1) edit-section/append-turn heading-payload guard; (2)
  --occurrence and delete-section recovery path; (3) ratifying-
  transition structural gate (duplicate headings, placeholders) plus
  checker rules 21-22; (4) session-close identity-frontmatter
  completeness; (5) stakeholder-added zero-decision close warning
  requiring an explicit --no-decisions-ok acknowledgment (T5); (6)
  IDEA-0028 fold-in. Mid-session the stakeholder added a further
  concern (T15): sessions must back-link their produced decisions,
  enforced by checker rule 23, chosen as a full historical backfill
  over a forward-only cutoff, resolved via a relates-to mirror plus
  a new accepted-in stamp (T17-T18). Design and test plan approved
  (T21); built and verified 16/16 green. The real-corpus checker run
  found 12 previously-shipped damaged artifacts, repaired under
  operator sanction (T22-T24). Ten decisions accepted
  (DEC-0376..DEC-0385); relates-to backfilled corpus-wide (373
  links, 65 sessions). Post-close-out, the stakeholder flagged
  lowercase sentence-opener prose across all ten decisions (T25),
  traced to label-continuation fragments in the drafting handoff
  (T26); 47 openers reworded (T28), and finished-prose authoring
  guidance (complete sentences, reword lowercase identifier openers)
  added to the groundwork-design-session and artifact-interact
  skills. Folded in a further scope addition (T29-T31): the write
  path's per-op recheck now validates frontmatter as YAML via PyYAML
  when available, closing the undetected-malformed-frontmatter
  window (DEC-0386). A decision-recall audit (Sonnet 5 judge, T32)
  accepted two findings -- DEC-0312 and DEC-0315 linked into this
  session and their instantiating decisions -- plus a sibling-
  crosslink gap, repaired as DEC-0376<->DEC-0377,
  DEC-0378<->DEC-0379, DEC-0382<->DEC-0383. Eleven decisions
  accepted in total: DEC-0376 through DEC-0386. IDEA-0041 and
  IDEA-0028 dispositioned taken-up.
links:
  relates-to: [IDEA-0041, DEC-0376, DEC-0377, DEC-0378, DEC-0379, DEC-0380, DEC-0381, DEC-0382, DEC-0383, DEC-0384, DEC-0385, IDEA-0028, SP-0015, SP-0013, EP-0009, IDEA-0015, IDEA-0016, IDEA-0025, SES-0062, SES-0063, SES-0067, SES-0071, DEC-0368, DEC-0312, DEC-0315, DEC-0386, IDEA-0042]
---

# SES-0072: Take up IDEA-0041 — edit-section phantom-heading guard, recovery path, and session-close completeness gate

## Purpose

This session takes up IDEA-0041 from the captured-idea work queue
(DEC-0261): the gw_write edit-section phantom-heading defect, four
recorded instances so far (SP-0015 shipped and still unrepaired,
SP-0016 caught pre-commit during SES-0071, DEC-0369/DEC-0370/DEC-0371
caught pre-commit, and SES-0069 shipped and repaired during the
SES-0070 close-out), its proposed write-time guard and recovery-path
fixes, the operator-directed scope expansion to session-close
completeness gating (a set-status-closed precondition and/or a checker
rule for placeholder text and duplicate sibling headings), and the
sanctioned repair of SP-0015's stranded duplication. The session will
also decide whether near-duplicate IDEA-0028 (edit-section duplicate-
heading hardening, the check_links.py first-Design-Elements-only
parsing gap, and a SKILL.md usage-note fix) is folded into this work.

## Transcript

Reconstructed fidelity (pre-application bootstrap record, per
SPEC-session).

T1 — Stakeholder (awakeinagi), verbatim proposal: "Take up IDEA-0041"

T2 — Facilitator, restatement: Restated the intent as running the
intake/refinement session for IDEA-0041 — design and decide fixes for
(a) the edit-section phantom-heading defect (write-time refusal of
heading-shaped replacement content and/or a recovery op for
already-corrupted sections), (b) the session-close completeness gap
(a set-status-closed precondition and/or checker rule for placeholder
text and duplicate sibling headings), and (c) the sanctioned repair of
SP-0015's stranded duplication. Noted that IDEA-0028 is a
near-duplicate covering the same root defect plus a checker parsing
gap (first-Design-Elements-only) and a skill-docs usage note, and
recommended folding it into this session. Noted this is tooling build
work subject to the no-arbitrary-builds guard (DEC-0335/DEC-0345):
written design including a test plan must be presented for approval
before any build. Recommended a full grilling session. Alignment
confirmation from the stakeholder is pending.

**T3 — Facilitator.** Presented the locate-first context report: IDEA-0041 clear to take up (no blockers, no gated items, no open conflicts); IDEA-0028 flagged as a near-duplicate (same edit-section root defect plus the checker first-Design-Elements parsing gap and a docs note); four recorded defect instances (SP-0015 shipped/unrepaired, SP-0016 caught pre-commit, DEC-0369/DEC-0370/DEC-0371 caught pre-commit, SES-0069 shipped/repaired). Asked: alignment on the restatement, fold IDEA-0028 in, and session weight.

**T4 — Stakeholder (awakeinagi).** Alignment: partially — will amend. IDEA-0028: fold it in. Weight: full grilling.

**T5 — Stakeholder (awakeinagi).** Amendment (verbatim): "I'd like to extend the scope a bit for these fixes. I want the librarian to issue a warning on sessions that have no decisions tied to them before closing. This should trigger the calling agent to assess whether or not that makes sense and work with the librarian to fix it if it doesn't."

**T6 — Facilitator.** Restated the five-item scope: (1) edit-section phantom-heading guard and/or recovery path; (2) session-close completeness gate (placeholders, required frontmatter); (3) zero-decision close warning (advisory shape to be pinned in grilling, DEC-0258 idea-capture sessions legitimately zero); (4) SP-0015 repair via sanctioned route; (5) IDEA-0028 fold-in (checker parsing gap + docs note).

**T7 — Stakeholder (awakeinagi).** (verbatim) "Those all sound good except I believe SP-0015 has already been repaired previously. For the librarian issues, please be sure to refer to the assessment SP-0017_librarian_failure.md".

**T8 — Facilitator.** Read the SP-0017_librarian_failure.md post-mortem: two-layer root cause (fragile span handling in the tool; heading-bearing payloads from callers), recommendations (span fix, heading-robust op, checker rule for duplicate sibling headings, librarian post-edit self-check, body-only caller discipline, SP-0015 repair). Verified SP-0015 on disk: still unrepaired — duplicate "Resulting Decisions" heading (empty orphan at line 74, content at line 76), no repair commit since the SES-0064 close-out; the SES-0069/SES-0070 repair wave did not include it. Presented the final six-item scope (adding the assessment's span-resolution framing and checker hardening).

**T9 — Stakeholder (awakeinagi).** Confirmed the six-item scope — start grilling.

**T10 — Stakeholder (awakeinagi).** (verbatim) "Let's work on fixing the librarian's editing skill before we ask it to edit anything else." Facilitator disposition: all further corpus writes held (transcript kept as a local ledger) until the tool fix is built and tested; build order becomes grill → design approval → build → resume corpus writes on the fixed tool.

**T11 — Facilitator.** Grilling round 1 (dependency order), each with a recommendation: (Q1) heading-shaped payload handling — reject with clear error (recommended) vs auto-strip vs strip+warn; (Q2) recovery path — occurrence flag + delete-section op (recommended) vs none vs occurrence-only; (Q3) close-gate enforcement point — both set-status precondition and checker rule (recommended) vs either alone; (Q4) zero-decision close shape — warn + require explicit acknowledgment flag (recommended; the flag is the recorded assessment) vs pure advisory vs advisory + checker backstop. Noted the span-resolution bug itself is fixed regardless (exactly one heading retained, idempotent re-runs) — the defect, not a choice.

**T12 — Stakeholder (awakeinagi).** Accepted all four recommendations: reject with clear error; occurrence flag + delete-section; both precondition and checker rule; warn + require explicit acknowledgment flag.

**T13 — Facilitator.** Recorded the discretionary call to skip the system-architect consultation (method-level session, DEC-0323): a well-scoped tool-defect fix with the option space already mapped by the post-mortem. Grilling round 2: (Q1) placeholder definition — small token list TBD/TODO/FIXME standalone lines plus whole-placeholder sections (recommended) vs broader patterns vs sections-only; (Q2) checker scope — duplicate headings everywhere, placeholders ratified-only (recommended) vs both ratified-only vs both everywhere; (Q3) gate breadth — all ratifying transitions incl. approvals (recommended; would have caught SP-0015 at its own gate) vs session-close only.

**T14 — Stakeholder (awakeinagi).** Accepted all three recommendations: TBD/TODO/FIXME token list; dup headings all artifacts, placeholders ratified-only; all ratifying transitions.

**T15 — Stakeholder (awakeinagi).** Mid-session scope addition (verbatim): "I'm also noticing that SES-0064 is missing all of its decision links in the frontmatter. We need this added to the link checker." Clarified: "The decisions themselves link to the session but the session doesn't link to the decisions. We should catch problems like that." Enrichment per the focus-artifact test (DEC-0260): it changes this session's artifact set — grilled now, not parked.

**T16 — Facilitator.** Back-link convention survey results: no session in the corpus back-links its produced decisions — all ~70 sessions / ~280 decisions lack the edge; SPEC-session defined relates-to as inputs only ("artifacts the session refined"), so the rule establishes a new obligation rather than catching drift. Spikes already back-link produced decisions via cites (both existing cases correct). Separately surfaced: SES-0071's Decisions Produced section reads "TBD." despite producing DEC-0374/DEC-0375 — added to the repair list. Asked: which frontmatter key (extend relates-to recommended vs a new produces: key), and backfill (full recommended vs forward-only cutoff).

**T17 — Stakeholder (awakeinagi).** Chose full backfill. On the key question, raised (verbatim): "Should we use produced/produced-by links between decisions and sessions? But then we'd also need to think about the case where a session opens a decision but doesn't resolve it and it is resolved only in a later session. In that case will both sessions and decisions need to keep both relationships? produce and resolve?"

**T18 — Facilitator.** Reasoned that the produced edge already exists machine-readably as the decision's derives-from (checker rule 4), so the session side needs only a generic mirror — a dedicated produces/produced-by pair would duplicate derives-from; and for open-now-resolve-later, precise semantics belong on the decision: derives-from = distilling session, plus a new accepted-in scalar stamped at set-status accepted (--session), keeping the ratification site graph-queryable with no link-vocabulary change. Proposed: relates-to mirror + accepted-in stamp. Stakeholder accepted the recommendation.

**T19 — Facilitator.** The session-open librarian reported a defect in this session's own record: the body H1 read `SES-XXXX` (body authored before ID allocation) with no safe write-API path to fix an H1 — refused to improvise. Folded into scope: create stamps the allocated ID into placeholder H1s; a checker rule for body-H1 identity; SES-0072's H1 joins the repair list.

**T20 — Facilitator.** Presented the complete written design incl. test plan (DEC-0335/DEC-0345 gate): (A) write-API — heading guard on edit-section/append-turn, --occurrence, delete-section with required-template protection, ratification preconditions (dup sibling headings, placeholders), session-close frontmatter completeness, zero-decision acknowledgment flag, create H1 stamping, accepted-in stamp; (B) checker rules 21-24; (C) SPEC-session/SPEC-decision amendments, SKILL.md and librarian-memory updates; (D) repairs (SP-0015, SES-0072 H1, SES-0071 placeholders) + full relates-to backfill via add-link batches (DEC-0248 enrichment); (E) ten-case test plan on a scratch corpus plus a real-corpus verification run.

**T21 — Stakeholder (awakeinagi).** Design and test plan approved — build it.

**T22 — Facilitator.** Build report: all changes implemented in the canonical skill scripts (gw_write.py, check_links.py synced to tools/), 16/16 tests green (test_gw_guards.py). Real-corpus checker run found MORE than the known inventory: rule 21 — seven artifacts (SP-0015 known, plus EP-0009, IDEA-0015, IDEA-0016, IDEA-0025, SES-0062, SP-0013); rule 22 — six placeholder lines (SES-0071 has four incl. an unfilled Purpose, plus SES-0063 and SES-0067 stray Transcript "TBD." lines); rule 23 — 373 missing back-links across 65 sessions; rule 24 — SES-0072's H1 plus DEC-0368's H1 (leads with SP-0014, missing its own ID prefix). Inspection confirmed every rule-21 hit except SES-0062 is an empty orphan first heading (SES-0062 duplicates the Purpose content verbatim). Presented the extended repair set for sanction: write-API dedups via delete-section for the six orphan-heading artifacts, sanctioned direct edits for the closed sessions (SES-0062, SES-0063, SES-0067, SES-0071), the accepted decision DEC-0368's H1, and SES-0072's H1.

**T23 — Stakeholder (awakeinagi).** Sanctioned the full extended repair set.

**T24 — Facilitator.** Repairs executed. Direct edits (operator-sanctioned, content-preserving): SES-0062 duplicate Purpose block removed (byte-identical copy); SES-0063 and SES-0067 stray "TBD." lines under Transcript deleted; SES-0071 Purpose and Decisions Produced filled from its own transcript/overview (DEC-0374, DEC-0375), stray Transcript "TBD." deleted, Conflicts Raised set to "None."; DEC-0368 H1 prefixed with its own ID; SES-0072 H1 placeholder stamped to SES-0072. Write-API repairs via the new delete-section op: SP-0015, SP-0013 ("Resulting Decisions"), EP-0009 ("Derived Work"), IDEA-0015/IDEA-0016/IDEA-0025 ("Disposition") — each validated the recovery op on a real defect. The 373-link relates-to backfill ran as add-link apply batches. Stakeholder confirmed the ten distilled decisions in plain-language playback.

**T25 — Stakeholder (awakeinagi).** Asked why the librarian was outputting sentences starting with lowercase letters, citing DEC-0384; framed as not necessarily worth fixing — a why question.

**T26 — Facilitator.** Root-caused it to the facilitator, not the librarian: the close-out handoff authored decision sections as label-continuation fragments ("Context: no op reaches…"), which the librarian transcribed faithfully under section headings, turning each fragment's lowercase first word into a sentence opener. Inventoried the spread: all ten of DEC-0376..DEC-0385, most sections plus several overviews. Noted a pure case-flip would corrupt legitimately lowercase code-identifier openers (edit-section, set-status, check_links.py) — a fix needs rewording, and the files were still uncommitted.

**T27 — Stakeholder (awakeinagi).** (verbatim) "Yes fix them if you can. And be sure that skill instructions inform agents to use proper grammar (capitalization, etc.) so when people use the groundwork skill they don't run into the same issue."

**T28 — Facilitator.** Applied the sanctioned mechanical casing polish: 47 opener rewordings across DEC-0376..DEC-0385 (capitalization where plain prose; rephrasing where the opener was a code identifier, e.g. "The edit-section op…"); checker green after. Added finished-prose authoring guidance ("complete sentences, normal capitalization; never label-continuation fragments; reword lowercase identifier openers") to the groundwork-design-session skill (refinement-process reference, Distilling decisions section) and the artifact-interact SKILL.md, canonical repo copies edited and user-scope copies synced. Recorded the lesson in facilitator memory. Assessed and declined a gw tool guard for grammar: identifiers are legitimately lowercase, so a capitalization lint would false-positive — authoring discipline, not a tool check.

**T29 — Stakeholder (awakeinagi).** Asked whether anything in gw.py needs fixing for the grammar issue; asked whether a YAML linter runs on artifact files at create/edit time; asked for research on a Python package for linting YAML files; then directed: (verbatim) "fold the PyYAML-recheck fix into this session now."

**T30 — Facilitator.** Reported the YAML state: the write path never parses frontmatter as YAML (text-surgical, stdlib-only per DEC-0317); YAML validity is enforced only at the pre-commit checker via PyYAML safe_load — so malformed frontmatter can sit undetected between a write and the next full check (the historical unquoted-title defect lived in that window). Ran the DEC-0337 option survey (web, cited): yamllint (PyPI, v1.38) is the canonical Python YAML linter with a documented Python API, but adds style-rule failure classes the corpus has never enforced; ruamel.yaml is a stricter YAML 1.2 parser, not a linter, and could reject frontmatter the checker accepts; schema validators (yamale/StrictYAML-class) do a different job. Recommended PyYAML in the per-op recheck for exact parity with the checker's validity bar, try-imported so the stdlib-only contract survives; presented the design plus test plan (malformed --field create refused naming unparseable YAML; existing suite re-runs green).

**T31 — Stakeholder (awakeinagi).** Approved the PyYAML-recheck design and test plan; confirmed the resulting decision in plain-language playback.

**T32 — Facilitator.** Built and verified the PyYAML-recheck fix: gw_write.py try-imports PyYAML and the post-write recheck refuses on unparseable or non-mapping frontmatter; 17/17 tests green including the new malformed-frontmatter case; full checker green (607 artifacts). Decision-recall audit ran on SES-0072 (15 candidates, Sonnet 5 judge). Two findings accepted: DEC-0312 (the write API as sole sanctioned write path — this session both closed the out-of-band-repair gap via DEC-0377 and, for API-unreachable surfaces like closed-session bodies and H1s, exercised the operator-sanctioned exception to it; DEC-0312 is now linked into this session and DEC-0377) and DEC-0315 (the per-operation-precondition vs. pre-commit-checker enforcement architecture that DEC-0376, DEC-0378, and DEC-0379 instantiate; now linked into this session and those three decisions). The judge's separately flagged contract gap was also accepted: the ten sibling decisions carried no relates-to cross-links despite tight coupling — repaired as DEC-0376↔DEC-0377, DEC-0378↔DEC-0379, DEC-0382↔DEC-0383, and the sibling-crosslink-at-creation practice added to the method reference. The remaining thirteen candidates were judged noise; closest near-miss DEC-0292, already carried via DEC-0323's provenance. Session close summary presented; inspired-ideas check run.

**T33 — Facilitator.** Inspired-ideas check: captured IDEA-0042 (sanctioned-repair override for API-unreachable surfaces — closed-session bodies, frontmatter fields, body H1s) from the recall audit's DEC-0312 finding; inspired idea IDEA-0042 (sanctioned-repair override) captured per the stakeholder's direction.

## Decisions Produced

This session produced eleven accepted decisions:

- DEC-0376 — section payloads are body-only, enforced at write time: edit-section and append-turn reject heading-bearing content.
- DEC-0377 — structural recovery through the write API: edit-section --occurrence N and a delete-section operation.
- DEC-0378 — ratifying status transitions refuse structural defects: duplicate sibling headings and placeholder text.
- DEC-0379 — checker rules 21 and 22: duplicate sibling headings flagged in all artifacts, placeholder text in ratified artifacts only.
- DEC-0380 — session close requires complete identity frontmatter.
- DEC-0381 — zero-decision session close requires an explicit recorded acknowledgment (--no-decisions-ok).
- DEC-0382 — sessions mirror their produced decisions in relates-to, enforced by checker rule 23, with full historical backfill.
- DEC-0383 — accepted-in: the ratification site of a later-accepted decision is stamped by set-status accepted --session.
- DEC-0384 — body H1 identity: create stamps allocated IDs into placeholder H1s; recheck and checker rule 24 enforce own-ID H1s.
- DEC-0385 — IDEA-0028 is absorbed into IDEA-0041's take-up.
- DEC-0386 — the per-op recheck validates frontmatter as YAML when PyYAML is available.

## Conflicts Raised

None yet — session open.
