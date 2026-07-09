---
id: SES-0008
type: session
title: EP-0007 refinement — placement, churn, search, serving, profiles
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0007, EP-0004, SP-0002]
---

# SES-0008: EP-0007 Refinement Session

## Purpose

Refine EP-0007
(Consolidation Memory Layer) to gate-readiness: consolidation placement and
churn policy, ownership of text/semantic search (deferred here by
DEC-0063), the serving contract for context recipes, quality assurance for
agent-generated summaries, search infrastructure, and the boundary of
"memory system for the agent."

## Transcript

**T1 — Sponsor.** Approved EP-0004 (ratifying SP-0002). Handle EP-0007.

**T2 — Agent.** Round 1: (a) consolidation placement given zero traffic at
launch (recommended static always-on catalog plus telemetry-driven
additions/retirements); (b) regeneration churn under active refinement
(recommended debounce with quiet-window/max-wait, plus on-demand
regeneration for stale-at-request); (c) search ownership, noting conflict
detection needs semantic similarity (recommended retrieval layer owns
full-text + embedding search as a derived, rebuildable index);
(d) serving-contract intelligence (recommended deterministic recipe
resolver assembling ranked, budget-truncated bundles with citations and
freshness proofs).

**T3 — Sponsor.** All four as recommended.

**T4 — Agent.** Round 2: (a) human gate on consolidations (recommended
none — automated faithfulness checks blocking serving instead);
(b) search/vector infrastructure (recommended extending SP-0002 with the
retrieval workload rather than a separate spike); (c) scope of "memory" —
consolidations only vs. participant interaction profiles vs. full memory
system (recommended consolidations + retrieval only, profiles deferred
over privacy weight).

**T5 — Sponsor.** (a) No human gate, automated checks. (b) Extend SP-0002.
(c) **Design to support both** consolidations/retrieval *and* participant
profiles — but profiles are **opt-in by users**, and profile data must be
**easily readable and editable by users via the UI**.

**T6 — Agent (synthesis).** Distilled DEC-0065–DEC-0071. The profile
decision adds an impact edge EP-0007→EP-0006 (profile viewer/editor and
consent surface are new UI requirements). Extended SP-0002's scope with
the search/vector workload. Rewrote EP-0007 and moved it to `gated`.

## Decisions Produced

DEC-0065,
DEC-0066,
DEC-0067,
DEC-0068,
DEC-0069,
DEC-0070,
DEC-0071

## Conflicts Raised

None.
