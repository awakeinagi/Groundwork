---
id: SES-0078
type: session
title: "Legacy skeleton repair — take up IDEA-0052 (rule-26 promotion prerequisite)"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-12
kind: expedited
participant: awakeinagi
participant-role: stakeholder
facilitator: "Claude (Fable 5)"
transcript-fidelity: verbatim
intake: {origin: user, proposed-by: awakeinagi}
overview: >-
  Expedited take-up session (DEC-0254) for IDEA-0052, the legacy-
  skeleton-repair idea captured from SES-0077 item 9's rule-26
  rollout sweep. Repaired the thirty-six artifacts checker rule 26
  reported as missing required body sections — twenty-six older
  decisions in two historical clusters (DEC-0121 through DEC-0139
  and DEC-0214 through DEC-0225), eight sessions, one component
  stub, and one spike — as operator-sanctioned facilitator direct
  edits under the verbatim-relocation-plus-marked-filler convention
  SES-0077 used, every non-verbatim line marked "skeleton restored
  at SES-0078". The twenty-six decisions' missing Implications and
  Alternatives Considered content was derived from each decision's
  source-session testimony per the T5 amendment; every one of
  DEC-0214 through DEC-0225 had a genuine recorded alternative, so
  the minimal-filler fallback was never needed. DEC-0408 codifies
  the repair convention as a standing decision; DEC-0409 promotes
  checker rule 26 from WARN to FAIL corpus-wide. Repairs, promotion,
  and full verification are complete. Decision-recall audits (T8/T9)
  found nothing further for DEC-0409 and one genuine lineage finding
  for DEC-0408, resolved as DEC-0248 enrichment: relates-to links to
  its precedents DEC-0091 and DEC-0248. The judge's create-op
  contract-gap finding is captured as IDEA-0053. Consistency sweep
  and terms checks returned zero hits. Session closed.
links:
  relates-to: [IDEA-0052, SES-0077, DEC-0408, DEC-0409, IDEA-0053]
---

# SES-0078: Legacy skeleton repair — take up IDEA-0052 (rule-26 promotion prerequisite)

## Purpose

This session takes up IDEA-0052, the legacy-skeleton-repair idea captured
from SES-0077 item 9's rule-26 rollout sweep. The purpose is to repair the
thirty-six legacy artifacts that checker rule 26 reports as missing required
body sections — twenty-six older decisions in two historical clusters
(DEC-0121 through DEC-0139 and DEC-0214 through DEC-0225, mostly missing
Implications and Alternatives Considered), eight sessions, one component
stub, and one spike — using the same operator-sanctioned direct-edit
convention and verbatim-relocation-plus-marked-filler treatment that
SES-0077 applied to its nineteen decisions, so that checker rule 26 can be
promoted from WARN to FAIL and the section skeleton becomes a hard
corpus-wide guarantee.

## Transcript

T1 (awakeinagi): "Take up IDEA-0052: legacy skeleton repair session"

T2 (Claude (Fable 5)): "IDEA-0052, captured from SES-0077 item 9's rule-26
rollout sweep, proposes repairing the thirty-six artifacts checker rule 26
reports as missing required body sections — twenty-six older decisions in
two historical clusters (DEC-0121 through DEC-0139 and DEC-0214 through
DEC-0225, mostly missing Implications and Alternatives Considered), eight
sessions, one component stub, and one spike — so that rule 26 can promote
from WARN to FAIL and the section skeleton becomes a hard corpus-wide
guarantee. Repairs on accepted/closed artifacts receive the same
operator-sanctioned direct-edit treatment SES-0077's nineteen repairs
received, with the same verbatim-relocation-plus-marked-filler convention."

T3 (awakeinagi): "Restatement confirmed as matching intent; session opened.
Path confirmed: expedited session per DEC-0254 — the repair convention is
settled by SES-0077; this take-up applies it to the remaining offenders
plus the rule-26 promotion. The repair design (cluster-by-cluster approach
and verification plan) will still be presented for approval before any
edits, and every integrity step runs."

T4 (facilitator, Claude (Fable 5)): "The facilitator presented the repair design and test plan: all thirty-six rule-26 offenders repaired as operator-sanctioned facilitator direct edits under this session's sanction — the same class as SES-0077 T17, structure-only and meaning-preserving, every non-verbatim line carrying the literal marker 'skeleton restored at SES-0078'. Group A: fourteen decisions (DEC-0121 cluster) gain their missing Implications section. Group B: twelve decisions (DEC-0214 through DEC-0225) gain Alternatives Considered and Implications. Group C: eight closed sessions gain missing Purpose (derived from each session's existing overview) and/or Conflicts Raised sections at canonical positions, transcript turns untouched per DEC-0248; each 'None raised' statement is verified against the conflict artifacts before writing. Group D: CMP-0006's seven 'Pending —' placeholder headings are renamed to canonical headings with bodies noting the DEC-0172 backlog deferral. Group E: SP-0012's 'Decisions Produced' heading is renamed to the skeleton's required 'Resulting Decisions'. Checker rule 26 then promotes from WARN to FAIL in check_links.py with tools/check_links.py re-synced byte-identical. Test plan: outline check on all thirty-six, full checker with zero rule-26 findings, git diff audit proving additions and heading renames only, a scratch-copy negative test proving the promoted rule fails a stripped artifact, and byte-identical sync verification."

T5 (stakeholder, awakeinagi): "Design and test plan approved, with one amendment and two additions. Amendment — filler policy for the twenty-six decisions: rather than minimal marked filler, derive the missing Implications and Alternatives Considered content from each decision's source-session testimony, strictly from what the recorded turns and the decision's own text support, every derived line marked 'skeleton restored at SES-0078'; minimal marked filler ('Not separately recorded at acceptance.') remains the fallback where the transcript genuinely records nothing on point. Additions — first, codify the verbatim-relocation-plus-marked-filler repair convention as a standing decision this session (its second use; it currently lives only in SES-0077's transcript). Second, append a brief marked evidence note to IDEA-0042 recording that SES-0078 repeated the freehand sanctioned-repair stopgap across thirty-six artifacts, strengthening the case for the sanctioned-repair write operation."

T6 (facilitator, Claude (Fable 5)): "Repairs executed and verified. The twenty-six decisions received transcript-derived sections per the T5 amendment — every one of DEC-0214 through DEC-0225 had a genuine recorded alternative in its source session, so no artifact anywhere needed the minimal-filler fallback; every derived paragraph carries the marker 'skeleton restored at SES-0078'. The eight closed sessions gained Purpose sections derived from their own overviews and/or Conflicts Raised sections at canonical positions with transcript turns untouched; the corpus contains zero conflict artifacts, so every 'None raised' statement is verifiably true. CMP-0006's seven placeholder headings were normalized to canonical headings with marked deferral notes citing DEC-0172, which was added to its cites. SP-0012's Decisions Produced heading was renamed to Resulting Decisions. Checker rule 26 then promoted from WARN to FAIL in check_links.py with tools/check_links.py re-synced byte-identical. All five test-plan steps passed: zero rule-26 findings corpus-wide; full checker reports 648 artifacts sound with only the nineteen pre-existing unrelated story coverage-gap warnings; the git diff audit proved pure additions on all decisions and sessions and exactly the intended renames on CMP-0006 and SP-0012; a scratch-copy negative test confirmed the promoted rule fails a stripped artifact; the sync is byte-identical."

T7 (stakeholder, awakeinagi): "DEC-0408's recorded text is confirmed as the standing repair convention. The rule-26 promotion decision payload is confirmed for recording as accepted. Inspired-ideas check: no new ideas; close the session."

T8 (facilitator, Claude (Fable 5)): "Decision-recall audits ran on both new decisions with Sonnet 5 judges. DEC-0409: nothing to add — the judge verified the closest candidates (DEC-0315's pre-commit-gate rule and the byte-identical tools-sync convention) are already carried by the cited DEC-0407 and SES-0078 provenance chains. DEC-0408: one genuine finding — DEC-0091 and DEC-0248, the two prior sanctioned-edit-class precedents on immutable artifacts, both drew their boundary at meaning-preserving changes only, and DEC-0408's convention consciously extends beyond that boundary via marker discipline without acknowledging the lineage; its frontmatter also carried no relates-to entries. The judge separately flagged a contract gap: the decision-create operation silently permitted a bare-ID-heavy body with an empty relates-to field, blinding the citer graph and retrieval-based recall audits to the artifact's true provenance. Consistency sweep and terms checks over DEC-0408 and DEC-0409 returned zero hits."

T9 (stakeholder, awakeinagi): "Dispositions confirmed. The lineage finding resolves enrichment-only per DEC-0248: add relates-to links from DEC-0408 to DEC-0091 and DEC-0248, with this turn recording the acknowledgment that DEC-0408 knowingly extends the meaning-preserving sanction boundary those decisions established, kept safe by the every-non-verbatim-line marker discipline its Rationale already argues. The create-op relates-to contract gap is captured as an Idea for its own future take-up (IDEA-0053). No further items; close the session."

## Decisions Produced

DEC-0408 (codifying the verbatim-relocation-plus-marked-filler repair convention as a standing decision, approved T5) and DEC-0409 (promoting checker rule 26 to FAIL corpus-wide, confirmed accepted T7). All thirty-six rule-26 repairs were executed and verified per T6. The T8/T9 decision-recall audit dispositioned both decisions: DEC-0409 needed nothing further; DEC-0408 gained relates-to links to its lineage precedents DEC-0091 and DEC-0248, and the judge's contract-gap finding was captured as IDEA-0053 for future take-up.

## Conflicts Raised

None.
