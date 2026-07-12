---
id: DEC-0370
type: decision
title: "The ActiveGraph fork-and-diff mechanism is viable for design-alternative evaluation in Groundwork"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-11
source-span: "SES-0070"
overview: >-
  The ActiveGraph fork-and-diff mechanism — a SQLite-backed element-
  grain substrate, one Runtime.fork per design alternative applying
  only the varied variable as an overlay, and a rule-findings set-
  difference — cleanly isolates a single design variable and
  GENERALIZES: it ran two structurally different benchmarks
  (DEC-0307 grouping; DEC-0134/0135 graduation) from one shared
  substrate with all six method-tests passing each (substrate
  parity, SP-0014 anchor, fork isolation, diff confinement,
  determinism, non-triviality), plus a global anchor reproducing
  SP-0014's boundary findings exactly. A reusable, method-tested
  Groundwork evaluation capability, bounded by DEC-0371's driver
  blind spot. PRELIMINARY (proposed).
links:
  derives-from: [SES-0070]
  relates-to: [SP-0017, SES-0070, DEC-0293, DEC-0307, DEC-0345, SP-0014, DEC-0354]
---

# The ActiveGraph fork-and-diff mechanism is viable for design-alternative evaluation in Groundwork

## Context

PRELIMINARY -- proposed pending ratification at the ActiveGraph adoption/consolidation session. SP-0017 built a SQLite-backed element-grain substrate (shared, grouping-free), one ActiveGraph Runtime.fork per design alternative applying only the varied variable as an overlay, and a rule-findings set-difference between forks, then validated the method itself before trusting its output.

## Decision

The fork-and-diff mechanism cleanly isolates a single design variable and GENERALIZES: it ran two structurally different benchmarks (DEC-0307 grouping; DEC-0134/0135 graduation) from ONE shared substrate with all six method-tests passing on EACH -- substrate parity, anchor to SP-0014's recorded findings, fork isolation, diff confinement to boundary-sensitive rules, determinism, and non-triviality -- plus a global anchor confirming the natural grouping reproduces SP-0014's boundary findings exactly.

## Rationale

Establishes fork-and-diff as a reusable, method-tested Groundwork capability for evaluating rival design alternatives against a rulebase.

## Alternatives Considered

Trusting the diff output without a method test was considered and rejected (DEC-0345 requires validating the method itself, not just its output).

## Implications

Fork-and-diff is a reusable, method-tested Groundwork evaluation capability, validated on more than one benchmark, subject to the semantic/driver blind-spot bound recorded in DEC-0371.
