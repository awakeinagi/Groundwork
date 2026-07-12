---
id: SES-0028
type: session
title: Narrow decision-recall audit judge topology to Sonnet 5 only
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Product owner directive narrowing the decision-recall audit's judge
  model tier to Sonnet 5 only, superseding DEC-0137's Opus-class tier
  for candidate lists under 15. Sonnet 5 fills every judge role
  previously given to Opus, including fork-when-facilitator-matches
  case. Leaves audit topology, retrieval, and disposition steps
  unchanged. Produced DEC-0161.
participant: awakeinagi@gmail.com
participant-role: product-owner
facilitator: Claude (Sonnet 5)
transcript-fidelity: verbatim
links:
  relates-to: [DEC-0137, DEC-0161]
---

# SES-0028: Narrow Decision-Recall Audit Judge Topology to Sonnet 5 Only

## Purpose

The sponsor directed, via the `/groundwork-design-session` command
arguments, that the decision-recall audit's judge subagent must run on
Sonnet 5 only. DEC-0137
currently specifies an Opus-class judge for candidate lists ≤15 (fork
or fresh Opus agent), sharding into Sonnet-class batches only beyond
that size. This session records the directive and its scope so the
model-topology clause of DEC-0137
can be properly superseded, and the skill's playbook/reference and
vendored/installed copies re-synced per
DEC-0137's own
Implications.

## Transcript

**T1 — Product Owner.** "The decision-recall audit should use Sonnet 5
models only."

**T2 — Facilitator.** Confirming scope before distilling: this reads as
narrowing the *model tier* only — never escalate to an Opus-class
judge, regardless of candidate-list size — while leaving the rest of
DEC-0137's
topology intact: one judge for lists ≤15, sharded into ~8-candidate
batches for lists >15, still forbidding one-candidate-per-agent
isolation. Sonnet 5 fills every judge role
DEC-0137
previously gave to Opus, including the fork-when-facilitator-matches
case (now: fork when the facilitator itself runs Sonnet 5).

**T3 — Product Owner.** Confirmed — Sonnet 5 across the board, no Opus
tier. No other change to the audit's mechanics, retrieval, or
disposition steps.

## Decisions Produced

DEC-0161

## Conflicts Raised

None.
