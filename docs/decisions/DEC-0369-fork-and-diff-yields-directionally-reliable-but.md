---
id: DEC-0369
type: decision
title: "Fork-and-diff yields directionally-reliable but rationale-partial structural evidence for grouping decisions"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-11
source-span: "SES-0070"
overview: >-
  Fork-and-diff over SP-0014's structural rulebase, tested on two
  already-decided questions (DEC-0307 grouping; DEC-0134/0135
  graduation), reproduced both decided outcomes DIRECTIONALLY but
  only partially reproduced their reasoning. On grouping it surfaced
  three of five human rejection grounds (blind to the two semantic
  ones); on graduation it fired precisely on the multi-consumer port
  (AppDatabasePort) yet missed the decoupling-driven event
  graduation (ChangeEvent) — a driver no rule models. Correspondence
  quality tracks whether a rule encodes the decision's actual
  driver. Corroborating evidence alongside, not a replacement for,
  the DEC-0293 dual-instance debate. PRELIMINARY (proposed) pending
  ratification at the cross-spike ActiveGraph adoption survey.
links:
  derives-from: [SES-0070]
  relates-to: [SP-0017, SES-0070, DEC-0293, DEC-0307, DEC-0135, SP-0014, DEC-0354]
---

# Fork-and-diff yields directionally-reliable but rationale-partial structural evidence for grouping decisions

## Context

PRELIMINARY -- proposed pending ratification at a dedicated ActiveGraph adoption/consolidation session (SP-0017 closed on its fork-and-diff charter; findings held proposed). SP-0017 ran fork-and-diff on TWO already-decided questions through SP-0014's structural rulebase via ActiveGraph Runtime.fork: (1) DEC-0307's component grouping (bounded-context vs a vertical-slice cut) and (2) DEC-0134/0135's seam graduation (graduated standalone vs kept inline); each diff was compared against the recorded decision rationale.

## Decision

Fork-and-diff reproduced BOTH decided outcomes DIRECTIONALLY -- every diff signal favored the decided answer. Correspondence QUALITY tracked how well the rulebase's rules model the decision's actual driver. On grouping (benchmark 1) correspondence was PARTIAL: the diff surfaced three of five human rejection grounds (shared-seam blurring; flows still spanning components; re-gating cost) plus an unnamed one (introduced dependency cycles), but was blind to the two semantic grounds (common-closure, ubiquitous-language cohesion). On graduation (benchmark 2) correspondence was DIRECT but heuristic-bounded: rule R16 fired precisely on the un-graduated seam AppDatabasePort (4 external consumers) and cleared when graduated, yet MISSED ChangeEvent's graduation, which was driven by event-contract decoupling (1 consumer) -- a driver no rule models.

## Rationale

An automated structural diff corroborates a decision's DIRECTION reliably across both benchmarks, but reproduces its REASONING only to the extent a rule encodes that decision's actual driver. Positioned as corroborating evidence ALONGSIDE, not a replacement for, the DEC-0293 dual-instance architect debate.

## Alternatives Considered

Treating the findings-diff as a standalone substitute for the human debate was considered and rejected — it is blind to two of the five recorded grounds.

## Implications

Fork-and-diff evidence is corroborating, not dispositive; its coverage grows directly with the rulebase's coverage of decision-driver types. The DEC-0293 dual-instance protocol remains necessary wherever a decision's driver is unmodeled. This run had no kill bar (DEC-0355); the verdict is descriptive (graded correspondence), not pass/fail.
