---
id: DEC-0161
type: decision
title: The decision-recall audit judge runs on Sonnet 5 only, never Opus-class
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0028 @ T1-T3"
links:
  derives-from: [SES-0028]
  supersedes: [DEC-0137]
  relates-to: [DEC-0138]
---

# DEC-0161: Decision-Recall Audit Judge — Sonnet 5 Only

## Context

[DEC-0137](DEC-0137-decision-recall-audit-step.md) set the audit's
judge topology as an Opus-class judge (solo, for candidate lists ≤15;
fork when the facilitator itself runs an Opus-class model, else a
fresh Opus agent) with a fallback to sharded Sonnet-class batches only
past that size. The sponsor directed a narrower rule: Sonnet 5 for
every judge invocation, with no Opus tier at all.

## Decision

The decision-recall audit's judge subagent always runs on a **Sonnet
5** model. This replaces [DEC-0137](DEC-0137-decision-recall-audit-step.md)
point 2's topology in full:

- lists ≤15 → **one** Sonnet 5 judge; fork (inherits session context)
  when the facilitator itself runs Sonnet 5, otherwise a fresh Sonnet 5
  agent fed the packet (+ artifact text if the judge lacks session
  context).
- lists >15 → shard into batches of ~8, each judged comparatively, all
  on Sonnet 5 agents.
- **One candidate per agent remains forbidden** — isolated relevance
  judges over-flag (acquiescence bias) — unchanged from
  [DEC-0137](DEC-0137-decision-recall-audit-step.md).

Every other clause of [DEC-0137](DEC-0137-decision-recall-audit-step.md)
(retrieval mechanics, the ≤4-finding
cap, "Nothing to add" as a valid outcome, in-session disposition, and
the audit's status as a complement — not a replacement — for rule-type
checklists like [DEC-0136](DEC-0136-graduation-review-required.md))
stands unchanged.

## Rationale

Sponsor call. No Opus-tier judge is to run for this step going
forward — a single fixed model tier for judge invocations, regardless
of candidate-list size, is simpler to reason about and keeps the
audit's cost profile predictable.

## Alternatives Considered

- **Keep [DEC-0137](DEC-0137-decision-recall-audit-step.md)'s split
  (Opus ≤15, Sonnet shards >15)** — rejected by
  direct sponsor instruction; no technical concern raised in-session,
  a policy preference for a single model tier.

## Implications

The skill's `SKILL.md` and `references/semantic-search.md` — both the
installed copy (`~/.claude/skills/groundwork-design-session/`) and this
project's vendored copy (`.agents/skills/groundwork-design-session/`)
— are updated to state the Sonnet-5-only topology, consistent with
[DEC-0137](DEC-0137-decision-recall-audit-step.md)'s original sync
requirement. Its status flips to `superseded`; its retrieval mechanics, finding cap, and
complement-not-replacement framing remain live via this decision.
