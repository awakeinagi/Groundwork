---
id: SES-0009
type: session
title: EP-0007 amendment — human review and flagging of consolidations
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
overview: >-
  Amendment to EP-0007 refinement following SES-0008, establishing human
  backstop to automated faithfulness checking. Consolidations browsable
  via UI with source references, freshness state, and check history; any
  user can flag with an issue report. Flags quarantine immediately (never
  served, fallback to sources) pending disposition in review queue
  (regenerate, fix sources, or correct checker). Confirmed human-caught
  misses feed evaluation corpus as regression cases, permanently
  strengthening automated guard. Produced 1 decision.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0007, SES-0008, DEC-0072]
---

# SES-0009: Consolidation Review & Flagging (EP-0007 Amendment)

## Purpose

Follow-up to SES-0008, amending the
gated EP-0007 before sign-off: ensure humans can review consolidations and
flag problems that the agents and the automated eval system miss.

## Transcript

**T1 — Sponsor.** Make sure we have the ability to view consolidations via
the UI so a human can review and flag them when there are issues that the
agents/eval system miss.

**T2 — Agent (synthesis).** Adopted as the human backstop to
DEC-0069's
automated-only guard: the UI surfaces consolidations (content, source
refs, freshness state, check history) for browsing and review; any user
can flag one with an issue report. A flag **quarantines** the
consolidation immediately — treated as stale, never served, with the
recipe resolver falling back to underlying sources — pending disposition
in a review queue (regenerate, fix sources, or correct the faithfulness
checker). Confirmed human-caught misses become regression cases in the
evaluation corpus, so each flag permanently strengthens the automated
guard. Recorded as DEC-0072;
EP-0007's scope and SPEC-consolidation updated; the EP-0007→EP-0006 impact
edge (already present for profiles) now also carries the consolidation
review/flag surface.

## Decisions Produced

DEC-0072

## Conflicts Raised

None.
