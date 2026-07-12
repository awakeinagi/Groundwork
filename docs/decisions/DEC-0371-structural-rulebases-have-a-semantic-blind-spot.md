---
id: DEC-0371
type: decision
title: "Structural rulebases have a semantic blind spot bounding automated design evidence"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-11
source-span: "SES-0070"
overview: >-
  A purely structural rulebase over element/edge topology cannot
  surface a decision's driver when no rule encodes it — a sharper
  bound than 'semantic vs structural.' Confirmed on two axes across
  SP-0017's benchmarks: semantic drivers (closure axis, ubiquitous-
  language cohesion, from DEC-0307) are unmodeled and missed; and
  even a STRUCTURAL driver is missed when unmodeled — event-contract
  decoupling behind DEC-0134's ChangeEvent graduation. Coverage is
  extensible by adding rules (decoupling, closure-axis), but until
  then the DEC-0293 human debate remains required wherever an
  unmodeled driver may be in play. Bounds automated fork-and-diff
  evidence. PRELIMINARY (proposed).
links:
  derives-from: [SES-0070]
  relates-to: [SP-0017, SES-0070, DEC-0293, DEC-0307, SP-0014, DEC-0136, DEC-0354]
---

# Structural rulebases have a semantic blind spot bounding automated design evidence

## Context

PRELIMINARY -- proposed pending ratification at the ActiveGraph adoption/consolidation session. Across SP-0017's two benchmarks the findings-diff missed grounds of two distinct kinds, sharpening the blind-spot characterization.

## Decision

A purely structural rulebase over element/edge topology cannot surface a decision's driver when NO RULE ENCODES THAT DRIVER. This is sharper than "semantic vs structural": the blind spot is the ABSENCE of a rule modeling the decision's actual driver. Confirmed on two axes -- (a) semantic drivers (closure axis / reasons-for-change; ubiquitous-language cohesion) are unmodeled and were missed on the grouping benchmark; (b) even a STRUCTURAL driver is missed when unmodeled -- event-contract decoupling drove ChangeEvent's graduation but no rule models decoupling, so the diff missed it on the graduation benchmark.

## Rationale

Bounds automated fork-and-diff evidence: it sees only decision drivers that some rule encodes. Coverage is extensible by adding rules (e.g. a decoupling or closure-axis rule), but until then the DEC-0293 human debate remains required wherever an unmodeled driver may be in play.

## Alternatives Considered

Attempting to compile semantic rules to close the gap within SP-0017's timebox was considered and deferred — out of scope for the single-benchmark run; a candidate direction for the stakeholder-directed capability-assessment extension.

## Implications

Automated structural evidence is partial by design; the DEC-0293 human debate protocol remains required wherever an unmodeled driver (semantic or structural) may be in play. Consistent with the no-kill-bar framing (DEC-0355), this result bounds the method rather than failing it.
