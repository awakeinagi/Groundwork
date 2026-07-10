---
id: IDEA-0021
type: idea
title: "Auto-managed, async-appended Session artifact across the baton pass"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  Every session so far is reconstructed after the fact. This idea
  proposes opening the session record live at the first turn and
  appending each turn as it happens, at each facilitator-to-
  stakeholder baton pass, fired non-blocking in the background,
  checked at the next baton pass or before close — changing
  transcript-fidelity from reconstructed toward something closer to
  live and changing the failure mode of an interrupted session. Open
  questions for take-up: what exactly counts as a baton-pass
  boundary, ordering risk from concurrent background writes, whether
  SPEC-session needs a new transcript-fidelity value, and
  composition with the librarian's write-serialization rule.
links:
  derives-from: [SES-0061]
  relates-to: [DEC-0332]
---

# IDEA-0021: Auto-Managed, Async-Appended Session Artifact Across the Baton Pass

## The Idea

Verbatim: "Open a Session artifact at session start. Append to file
after each baton pass from facilitator to stakeholder (user). All of
these operations should be fired off by the facilitator in the
background async and non-blocking. Facilitator can check callback at
next baton pass or before session close."

## Spark Context

Every session this project has run so far is reconstructed after the
fact (`transcript-fidelity: reconstructed` on every SES- artifact) —
the facilitator drafts the full transcript retrospectively, then
writes it in one batch near session close. This idea proposes the
opposite discipline: open the session record live, at the first turn,
and append each turn as it actually happens — specifically at each
"baton pass" (the point where the facilitator hands conversational
control back to the stakeholder, i.e. after presenting something and
awaiting a reply), fired as a non-blocking background operation so the
facilitator doesn't stall waiting on the write to land, checked at the
next baton pass or at close. This would change `transcript-fidelity`
from `reconstructed` toward something closer to `live` (a distinction
SPEC-session may not currently even have a field for) and changes the
failure mode of a session getting interrupted mid-conversation — today
an interrupted session may lose its entire unwritten transcript; a
live-appended one would already have everything up to the last baton
pass on disk.

## Disposition

Pending — awaiting take-up. Real design questions: what exactly counts
as a "baton pass" boundary in practice (every AskUserQuestion? every
plain-text turn awaiting reply?); whether async/non-blocking writes
risk out-of-order turns if a background write from an earlier baton
pass lands after a later one; whether this needs a new
`transcript-fidelity: live` value in SPEC-session; and how this
composes with the librarian's own write-serialization rule (DEC-0332:
only one write-task librarian at a time) if turn-appends fire
concurrently with other in-session writes.
