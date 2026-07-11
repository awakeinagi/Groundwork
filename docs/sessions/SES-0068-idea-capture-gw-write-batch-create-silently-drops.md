---
id: SES-0068
type: session
title: "Idea capture: gw_write batch create silently drops malformed link keys"
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-11
participant: awakeinagi
participant-role: stakeholder
facilitator: Claude Code (Fable 5)
transcript-fidelity: reconstructed
overview: >-
  Idea-capture micro-session (DEC-0258) run per the standing
  instruction recorded at SES-0067 T1 item (4) and institutionalized
  as IDEA-0033: subagent-encountered problems are reported to the
  facilitator and recorded as Ideas. Captures one tooling defect the
  librarian surfaced while executing SES-0067's own capture batch:
  gw write apply create operations carrying the link field as a link
  string (mirroring the CLI --link flag) were silently ignored --
  artifacts were created with empty links while the batch printed a
  clean 'OK create' line, because only the links dict form is
  recognized by the batch-mode namespace builder. The librarian
  caught it by reading created frontmatter directly rather than
  trusting the printed output, and repaired in-band via sanctioned
  add-link and append-turn --enrichment operations. Captured
  verbatim as IDEA-0034 (joins the gw-tooling-hardening queue beside
  IDEA-0028); zero decisions produced (valid per DEC-0258); no
  product or method artifact change.
links:
  relates-to: [DEC-0258, DEC-0312, DEC-0314, SES-0067, IDEA-0028, IDEA-0033]
---

# SES-0068: Idea capture: gw_write batch create silently drops malformed link keys

## Purpose

Idea-capture micro-session (DEC-0258) capturing one tooling defect the librarian surfaced during SES-0067's own capture batch execution, per the standing instruction recorded at SES-0067 T1 item (4) and institutionalized as IDEA-0033: subagent-encountered problems are reported to the facilitator and recorded as Ideas. The defect concerns the typed write API (DEC-0312) batch-apply mechanism (DEC-0314): `create` operations carrying a malformed `link` key silently produced link-less artifacts instead of refusing or warning.

## Transcript

**T1 — Facilitator (relaying the librarian's report).** During SES-0067's capture batch, `gw write apply` `create` ops carrying the link field as a `"link"` string (mirroring the CLI `--link` flag) were silently ignored — the artifacts were created with empty links while printing a clean "OK create" line; only the `"links"` dict form is recognized by the batch-mode namespace builder. The librarian detected it by reading created frontmatter directly rather than trusting the output, and repaired in-band via sanctioned add-link and append-turn --enrichment ops. A create op with an unrecognized/malformed link key should refuse or warn, never silently no-op.

**T2 — Facilitator.** Captured as an Idea per the standing instruction; joins the gw-tooling-hardening queue beside IDEA-0028.

## Decisions Produced

None.

## Conflicts Raised

None.
