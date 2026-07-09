---
id: DEC-0243
type: decision
title: The full corpus is de-linkified in one mechanical pass under DEC-0091's sanction
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0047 @ T3-T4, T7-T8"
links:
  derives-from: [SES-0047]
  relates-to: [DEC-0091, DEC-0242]
---

# DEC-0243: Full-Corpus De-Linkification Pass

## Context

DEC-0242 flips the body cross-reference convention to bare IDs. The
existing corpus — including 45 closed sessions (append-only) and 239
accepted decisions (immutable) — is written in DEC-0090's linked
form. The facilitator recommended migrating living artifacts only,
the strictest reading of immutability; the stakeholder chose
corpus-wide consistency.

## Decision

One mechanical pass converts inline artifact links to bare IDs across
the **entire** corpus — components, stories, spikes, epics, goals,
sessions, decisions, specs, CONTEXT.md, AGENTS.md, and the trigger
registry. The pass runs under DEC-0091's existing sanction: reference
formatting that changes no words, meaning, or structure is a
sanctioned edit class on closed sessions and accepted decisions, for
the initial linkification *and future fixes of the same class* — this
pass is that class, inverse direction. The four links whose display
text is descriptive prose rather than a bare ID are reworded by hand
to prose plus bare ID, preserving meaning. The commit performing the
pass cites this decision.

## Rationale

The same trade DEC-0091 already settled, in the same direction:
immutability protects *what was said and decided*, and unwrapping a
link changes neither — git history preserves the pre-pass text.
A living-artifacts-only migration would leave the bulk of the corpus
permanently mixed-style and require per-type grandfathering in the
checker; decisions in particular are read heavily during design, so
exempting them forfeits real savings (~12% of 527 KB).

## Alternatives Considered

- **Living artifacts only** (facilitator's recommendation): cleanest
  immutability posture, ~60% of the read-time savings, but a
  permanently mixed corpus and grandfathering complexity.
- **Forward-only, no retrofit**: zero migration risk; the CMPs — the
  biggest re-read cost — keep their overhead indefinitely.

## Implications

The corpus drops ~65k tokens (~20%). The checker needs no
grandfathering — one rule for every artifact. DEC-0091's sanction now
has two applications on record; its edit-class definition, not its
direction, is the operative content.
