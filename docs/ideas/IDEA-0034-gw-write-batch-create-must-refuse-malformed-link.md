---
id: IDEA-0034
type: idea
title: "gw_write batch create must refuse malformed link keys"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-11
proposed-by: awakeinagi
overview: >-
  gw_write batch create must refuse malformed link keys. During
  SES-0067's own idea-capture batch, gw write apply create
  operations carrying the link field as a link string (mirroring the
  CLI --link flag) were silently ignored -- the artifacts were
  created with empty links while the batch printed a clean 'OK
  create' line; only the links dict form is recognized by the batch-
  mode namespace builder. The librarian detected the defect by
  reading created frontmatter directly rather than trusting the
  printed output, and repaired in-band via sanctioned add-link and
  append-turn --enrichment operations. Required fix: a create op
  carrying an unrecognized or malformed link key should refuse or
  warn, never silently no-op. Surfaced and reported per the standing
  instruction recorded at SES-0067 T1 item (4), institutionalized as
  IDEA-0033; captured at SES-0068. Joins the gw-tooling-hardening
  queue beside IDEA-0028.
links:
  derives-from: [SES-0068]
  relates-to: [IDEA-0028, IDEA-0033]
---

# IDEA-0034: gw_write batch create must refuse malformed link keys

## The Idea

"gw_write batch create must refuse malformed link keys." During SES-0067's capture batch, `gw write apply` `create` ops carrying the link field as a `"link"` string (mirroring the CLI `--link` flag) were silently ignored — the artifacts were created with empty links while printing a clean "OK create" line; only the `"links"` dict form is recognized by the batch-mode namespace builder. The librarian detected it by reading created frontmatter directly rather than trusting the output, and repaired in-band via sanctioned add-link and append-turn --enrichment ops. A create op with an unrecognized/malformed link key should refuse or warn, never silently no-op.

## Spark Context

Surfaced by the librarian mid-execution of SES-0067's idea-capture write batch; reported to the facilitator and captured per the standing instruction recorded at SES-0067 T1 item (4) (IDEA-0033). Captured at SES-0068.

## Disposition

Pending.
