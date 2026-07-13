---
id: DEC-0500
type: decision
title: "Free-text channels are layout-dependent: notes on preview cards, Other on plain cards"
status: accepted
owner: awakeinagi
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0093 @ T4, T5, T8"
overview: >-
  DEC-0474 named the automatic Other option as the guaranteed free-
  text channel for grilling, but this session's experiments showed
  preview-layout cards (DEC-0472) suppress Other entirely. This
  decision supersedes DEC-0474 and makes the guaranteed channel
  layout-dependent: on preview cards it is the "Something
  else/Please elaborate" option with an attached note, with bare
  per-selection notes and note-only submissions also valid; on plain
  cards it remains the automatic Other option. The harness's native
  "Chat about this" row is acknowledged as a universal escape hatch
  on both layouts. Notes stay first-class design input rather than
  noise, and DEC-0461's harness survey and DEC-0474's non-notes
  fallbacks for harnesses lacking structured cards are otherwise
  unchanged.
links:
  relates-to: [DEC-0472, DEC-0074, DEC-0499, DEC-0501, DEC-0503]
  derives-from: [SES-0093]
  supersedes: [DEC-0474]
---

# DEC-0500: Free-text channels are layout-dependent: notes on preview cards, Other on plain cards

## Context

DEC-0474 named the automatic Other option the guaranteed free-text channel for grilling answers, retiring DEC-0461's reliance on the inline "Type something" field. This session's experiments showed Other itself is suppressed on preview-layout cards, while per-selection notes (the n key) round-trip intact and a note-only submission — no option selected — is accepted by the harness and delivered.

## Decision

The guaranteed free-text channel is layout-dependent. On preview-layout cards it is the "Something else/Please elaborate" option with an attached note, with the bare notes shortcut on any option and note-only submissions remaining valid. On plain-layout cards it is the automatic Other option, as before. The harness-native "Chat about this" row, present on both layouts, is acknowledged as the universal escape hatch into free conversation. Notes remain first-class design input — amendments, caveats, and upgrades to the chosen option, never noise.

## Rationale

An affordance guarantee must name a channel that actually exists on the layout in question; the experiments falsified the premise that Other is universally available.

## Alternatives Considered

Keeping Other as the stated universal channel, which is empirically false on preview cards. Mandating plain layout everywhere to preserve Other, which loses previews and per-selection notes — the affordances DEC-0472 chose preview layout to obtain.

## Implications

Facilitator documentation stops promising Other on preview cards. DEC-0461's harness survey stands as historical record. Fallbacks for harnesses without native notes or structured cards (GitHub Copilot CLI, Amp) are unchanged from DEC-0474.
