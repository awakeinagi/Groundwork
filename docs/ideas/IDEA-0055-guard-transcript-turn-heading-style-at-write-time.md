---
id: IDEA-0055
type: idea
title: "Guard transcript turn-heading style at write time"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  Append-turn's auto-numbering and read-turns both recognize only
  ###- or **-prefixed turn headings; nothing guards transcript
  heading style at write time. SES-0081's turns landed as plain-text
  Tn(...) paragraph openers, invisible to the turn regex: auto-
  numbering restarted at T1 (a duplicate the checker's rule 21
  cannot see, since it only scans real headings), and read-turns
  returned nothing. The repair window closes at session close (edit-
  section refuses closed sessions), making mislabeled turns an
  operator-direct-edit surface. Captures possible shapes for a
  future session: write-time refusal/warning on plain-text turn
  openers, normalization to ### Tn headings, or a checker rule for
  monotonic turn-heading labels.
links:
  derives-from: [SES-0081]
  relates-to: [DEC-0414]
---

# IDEA-0055: Guard transcript turn-heading style at write time

## The Idea

Append-turn's auto-numbering and the read family's turn addressing both recognize only `###-` or `**-`prefixed turn headings, but nothing guards transcript heading style at write time. SES-0081's turns landed as plain-text "Tn (...)" paragraph openers (via create body and appended payloads), making the transcript invisible to the turn-recognition regex: auto-numbering restarted at T1, a duplicate label the checker cannot see since rule 21 only scans real Markdown headings, and read-turns returned nothing for the existing turns. The repair window also closes at session close, since edit-section refuses closed sessions, so mislabeled turns become an operator-direct-edit surface. Possible shapes, for a future session to weigh: append-turn refuses or warns when the Transcript section contains turn-like plain-text openers its regex cannot see; create/append normalize turn openers to `### Tn` headings; the checker gains a rule that transcript turn labels are monotonically increasing Markdown headings.

## Spark Context

Found during SES-0081's own close, when the closing turn was assigned T1 over an existing plain-text T1-T6 transcript in the same session; repaired by operator-sanctioned direct normalization of the headings.

## Disposition

Pending.
