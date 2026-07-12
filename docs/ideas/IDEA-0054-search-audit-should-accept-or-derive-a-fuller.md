---
id: IDEA-0054
type: idea
title: "search audit should accept or derive a fuller considered set"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: Claude Fable 5 (facilitator), noted by the DEC-0413 recall-audit judge, capture sanctioned within this closing task
overview: >-
  During SES-0079's DEC-0413 recall audit (T8), the judge observed
  that the search-audit packet's considered field listed only
  DEC-0391 and DEC-0413, while the session had actually weighed a
  dozen decisions across its design and build turns. The packet has
  no mechanism to carry the fuller in-session considered set (e.g.
  via the session's relates-to/cites), so a judge relying on the
  packet alone would over-flag decisions the session already
  examined as unconsidered. Proposal: let search audit accept a
  --considered list, or derive one from the target session's
  relates-to/cites, so the packet's considered field reflects what
  was actually weighed.
links:
  derives-from: [SES-0079]
  relates-to: [DEC-0413]
---

# IDEA-0054: Let `search audit` accept or derive a fuller "considered" set for recall-audit packets

## The Idea

Let `search audit` accept a `--considered` list (or derive it from the session's `relates-to`/`cites`) so the packet's `considered` field reflects reality, instead of only the one or two decisions literally named in the audit invocation.

## Spark Context

During the DEC-0413 recall audit at SES-0079 (T8), the judge noted the search-audit packet's `considered` field listed only `["DEC-0391","DEC-0413"]` while the session had actually considered a dozen decisions across its design and build turns. The packet has no way to carry the fuller in-session considered set, so a judge relying on it alone would over-flag decisions the session already weighed as if they had never been examined.

## Disposition

Pending.
