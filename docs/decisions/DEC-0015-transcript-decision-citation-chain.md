---
id: DEC-0015
type: decision
title: "Provenance chain: transcript → Decision record → citation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-05
overview: >-
  Raw session transcripts are stored verbatim and append-only; the agent
  distills each session into discrete Decision records citing specific
  transcript spans. Contracts, requirements, and acceptance criteria cite
  Decisions rather than transcripts. This establishes a citable provenance
  chain — stakeholder utterance, distilled decision, contract constraint —
  where the transcripts remain retrievable for dispute resolution. The
  approach avoids both the maintenance burden of constant distillation and the
  loss of audit trail from discarding transcripts entirely.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-05
source-span: "SES-0001 @ T8-T9"
links:
  derives-from: [SES-0001]
---

# DEC-0015: Provenance chain — transcript → Decision → citation

## Context

A stakeholder says something in a Q&A session; it becomes a decision; the
decision shapes a contract. The artifact chain connecting those steps
determines whether "why does the contract say this?" is ever answerable.

## Decision

Raw session transcripts are stored verbatim and append-only. The agent
distills each session into discrete Decision records (context, choice,
rationale, who decided, citing transcript turn spans). Contracts,
requirements, and acceptance criteria cite Decision IDs. Implementation
agents crawl to Decisions and rarely need raw transcripts.

## Rationale

Decisions give agents concise, citable rationale without wading through
conversation; retained transcripts preserve the ability to re-examine what
was actually said when a decision is disputed.

## Alternatives Considered

- **Transcripts only**: no distillation to maintain; agents wade through
  conversation to reconstruct rationale.
- **Decisions only, transcripts discarded**: cleaner store; loses the
  dispute-resolution trail.

## Implications

Formalized in [SPEC-session](../specs/SPEC-session.md) and
[SPEC-decision](../specs/SPEC-decision.md); the `cites` field exists on all
artifacts ([SPEC-artifact-common](../specs/SPEC-artifact-common.md)).
