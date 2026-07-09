---
id: DEC-0052
type: decision
title: Raw chat transcripts are canonical ground truth; distillation is regenerable
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T3"
links:
  derives-from: [SES-0006]
---

# DEC-0052: Raw transcripts as ground truth; regenerable distillation

## Context

Agent-produced summaries and Decision records can drift from what was
actually said (information drift, hallucination). The sponsor requires the
raw chat record be kept available so decisions and summaries can be
regenerated when distillation is suspect.

## Decision

The session transcript stored in the SES artifact **is** the raw message
log — verbatim, turn-numbered, append-only — not an agent summary of it.
Any condensed view (session summaries, consolidations) is a derived layer
that never replaces the raw record. Distillation is a re-runnable function
of the raw transcript: when drift or hallucination is suspected, decisions
and summaries are regenerated from raw and diffed against what was
accepted.

## Rationale

Everything downstream — decisions, contracts, gates — cites transcript
spans; that chain is only as trustworthy as the fidelity of what spans
point to. Regeneration turns "do we trust the agent's reading?" from a
debate into a diff.

## Alternatives Considered

- **Summarized transcripts with raw discarded**: loses the ability to
  re-examine or regenerate — rejected outright.
- **Raw log as a separate artifact from SES**: considered (sponsor left it
  open); folded into the SES artifact instead so provenance stays one hop.

## Implications

[SPEC-session](../specs/SPEC-session.md) strengthened: transcript = raw
message log. Periodic drift audits run regeneration diffs
(DEC-0058). For pre-application sessions
(this repo's bootstrap), `transcript-fidelity: reconstructed` marks the
exception; app-hosted sessions are always `verbatim`.
