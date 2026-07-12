---
id: DEC-0408
type: decision
title: "Codify the verbatim-relocation-plus-marked-filler repair convention"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: SES-0078 @ T4-T5
overview: >-
  SES-0077 repaired nineteen decisions as operator-sanctioned direct
  edits using an ad hoc convention: relocate existing verbatim
  content into its correct required section, and fill genuine gaps
  with minimal marked filler carrying a literal repair-session
  marker. SES-0078 repeated the convention across thirty-six further
  offenders, amending the filler policy to prefer transcript-derived
  content over minimal filler where the source session's record
  supports it, falling back to marked filler only where the
  transcript is silent. This decision codifies the convention as a
  standing, citable method on its second use, so future
  rule-26-style repair sessions do not need to re-derive it from
  SES-0077's transcript alone.
links:
  relates-to: [DEC-0091, DEC-0248]
  derives-from: [SES-0078]
---

# DEC-0408: Codify the verbatim-relocation-plus-marked-filler repair convention

## Context

SES-0077 repaired nineteen decisions flagged by checker rule 26 (missing required body sections) as operator-sanctioned facilitator direct edits, using an ad hoc convention: relocate existing verbatim content into its correct required section where the transcript or artifact's own text already supplied it, and fill genuine gaps with minimal marked filler so every non-verbatim line stayed distinguishable from original testimony. SES-0078 repeated the same convention across thirty-six further offenders (Groups A through E: fourteen DEC-0121-cluster decisions, twelve DEC-0214 through DEC-0225 decisions, eight closed sessions, CMP-0006's placeholder headings, and SP-0012's heading rename), amending the filler policy to prefer transcript-derived content over minimal filler where the source session's recorded turns and the artifact's own text support it. Two independent uses of the same unwritten convention is enough recurrence that it should be a named, citable decision rather than something that lives only in SES-0077's transcript.

## Decision

The verbatim-relocation-plus-marked-filler convention is adopted as the standing repair method for operator-sanctioned direct edits on API-unreachable surfaces (IDEA-0042): relocate existing verbatim content to its correct required-section position wherever the source material already supplies it; where content is genuinely missing, prefer deriving it from the artifact's own source-session testimony and existing text over inventing new substantive content, falling back to minimal marked filler (for example, "Not separately recorded at acceptance.") only where the transcript records nothing on point; every non-verbatim line, whether transcript-derived or fallback filler, carries a literal marker naming the repairing session (for example, "skeleton restored at SES-0078").

## Rationale

Marking every non-verbatim line preserves the distinction between what a ratified artifact's original participants actually said and what a later repair session reconstructed or filled, so provenance stays auditable even when the repair itself falls outside the typed write API. Preferring transcript-derived content over filler keeps repaired sections substantive and traceable to real testimony rather than uniform boilerplate, while the marked-filler fallback still guarantees every required section gets real content when the transcript is silent.

## Alternatives Considered

Leaving the convention undocumented and re-deriving it ad hoc each time a rule-26-style repair session runs was rejected: it already needed restating in full at SES-0078's take-up, and a second recurrence without a named decision would leave future repair sessions no citable reference. Requiring all repaired content to be transcript-derived, with no filler fallback, was rejected because some historical artifacts' transcripts genuinely record nothing on the missing section's topic, and forcing derivation would produce fabricated content rather than an honest gap marker.

## Implications

Future rule-26-style (or analogous) repair sessions cite this decision instead of re-deriving the convention from SES-0077's transcript. The convention remains an operator-sanctioned direct-edit practice, not a change to the typed write API itself; IDEA-0042 continues to track the prerequisite work of bringing these repairs in-API.
