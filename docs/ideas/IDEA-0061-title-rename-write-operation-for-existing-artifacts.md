---
id: IDEA-0061
type: idea
title: "Title-rename write operation for existing artifacts"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  The gw write API has no operation that retitles an existing
  artifact: frontmatter title, body H1, and filename slug are all
  unreachable by any current write op. SES-0085 needed two retitles
  (BG-0002's recharter and EP-0009's broadening to Artifact
  Lifecycle & Interaction) and both ran as sanctioned direct edits
  plus git mv, per the SES-0073 precedent. Same shape as the
  IDEA-0042 missing-section gap. A take-up should add a typed
  retitle op updating title, H1, and filename coherently, using the
  checker's id/filename-match and H1-identity rules as its contract.
links:
  derives-from: [SES-0085]
  relates-to: [SES-0085, IDEA-0042]
---

# IDEA-0061: Title-rename write operation for existing artifacts

## The Idea

The gw write API has no operation that retitles an existing artifact — frontmatter title, body H1, and the filename slug are unreachable by any op (create, set-status, add-link, add-cite, remove-cite, update-overview, edit-section, delete-section, append-turn, supersede). SES-0085 needed two retitles (BG-0002's recharter title and EP-0009's broadening to Artifact Lifecycle & Interaction) and both ran as the facilitator's sanctioned direct edits plus git mv, per the SES-0073 precedent. Same shape as the IDEA-0042 missing-section gap. A take-up should add a typed retitle op that updates title, H1, and filename coherently, with the checker's id/filename-match and H1-identity rules as its contract.

## Spark Context

Surfaced twice in SES-0085's cascade when the write API refused the BG-0002 and EP-0009 retitles; the stakeholder chose capture at the session's gate turn (T27).

## Disposition

Pending.
