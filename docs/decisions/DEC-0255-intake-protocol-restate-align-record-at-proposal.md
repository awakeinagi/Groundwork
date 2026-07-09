---
id: DEC-0255
type: decision
title: Change intake runs a restate-and-align loop, and the session record opens at the verbatim proposal
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T1-T2, T10-T11"
links:
  derives-from: [SES-0050]
  relates-to: [DEC-0262]
---

# DEC-0255: The intake protocol — restate, align, record from intent

## Context

The stakeholder proposed a standard flow for change intent entering a
Groundwork project. Two questions defined its shape: how alignment is
reached before grilling, and where the session record begins.

## Decision

Change intake follows a fixed protocol: (1) the proposer states the
change; (2) the agent restates its understanding of the *intention*
and asks whether to begin a session; (3) clarifications and additions
return to step 2 until the proposer confirms alignment; (4) the
**authority check** runs against the governance config — an
instruction outside the instructor's decision rights proceeds no
further: a CP captures the attempt verbatim (DEC-0262) and intake ends
there; (5) otherwise the confirmed path runs (full grilling, expedited
per DEC-0254, mechanical fix per DEC-0253, or idea capture per
DEC-0258). When a session opens,
its record begins at the proposal itself: T1 reconstructs the verbatim
proposal, T2 the agent's restatement, and the alignment loop follows —
provenance starts at intent. If the exchange stays off-record (no
change instructed), nothing is recorded.

## Rationale

The alignment loop is where intent gets corrected — losing it loses
the most error-prone part of the provenance chain. SES-0050 itself
demonstrates the value: its T1–T9 preserve two proposal amendments and
a corrected CP understanding that no post-grilling summary would
reconstruct faithfully.

## Alternatives Considered

- **Record starts at grilling, proposal summarized in Purpose**:
  lighter, but compresses the user's words into what the agent heard —
  the exact failure the restate loop exists to catch.

## Implications

The session template's transcript guidance and the skill's intake
playbook encode T1-at-the-proposal. DEC-0256's todo list tracks the
protocol's steps from first mention.
