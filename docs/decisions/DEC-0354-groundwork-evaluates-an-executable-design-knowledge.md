---
id: DEC-0354
type: decision
title: "Groundwork evaluates an executable-design-knowledge approach via an ActiveGraph spike program under EP-0009"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0064 @ T3-T11"
overview: >-
  Groundwork will evaluate an "executable design knowledge" approach
  -- compiling design best practices and rule-type decisions into
  reactive rules that fire over a typed projection of the design
  corpus, using ActiveGraph (event-sourced reactive graph runtime;
  Python package activegraph v1.9.0, Apache-2.0) as candidate
  substrate -- via a five-spike exploratory program housed under
  EP-0009 as its first derived work. Confirmed in SES-0064 (T3-T11)
  through stakeholder option selection: projection (SP-A),
  structural rule precision (SP-B), prose-to-rule compilation
  fidelity (SP-C), reactive hook-loop economics (SP-D), and fork-
  and-diff evidence (SP-E). Relates to DEC-0339 (the epic's
  charter), DEC-0350 (EP-0009's derivation naming this spike program
  its first derived work), and DEC-0351 (the epic's guardrailed-
  spike Scope-In).
links:
  derives-from: [SES-0064]
  relates-to: [DEC-0339, DEC-0350, DEC-0351]
---

## Context

SES-0064 T3 asked how the ActiveGraph tool (event-sourced reactive graph runtime; Python package activegraph v1.9.0, Apache-2.0) could benefit Groundwork. Discussion (T3-T11) elaborated an "executable design knowledge" idea: compile design best practices (the system-architecture-bp corpus) and Groundwork's own rule-type decisions into reactive rules that fire over a typed projection of the design corpus, rather than relying on agents loading summarized prose into context. The stakeholder confirmed a five-spike program to test the idea empirically (T9), and EP-0009 has since been approved with DEC-0350 naming this program its first derived work and DEC-0351 scoping guardrailed exploratory spikes into the epic.

## Decision

Groundwork will evaluate the executable-design-knowledge approach described above -- compiling design best practices and rule-type decisions into reactive rules firing over a typed projection of the design corpus, with ActiveGraph as candidate substrate -- via a five-spike exploratory program (SP-A projection, SP-B structural rule precision, SP-C prose-to-rule compilation fidelity, SP-D reactive hook-loop economics, SP-E fork-and-diff evidence), housed under EP-0009 as its first derived work.

## Rationale

The component-doc corpus already carries element-scoped, contract-item-scoped, and typed dependency data (T5-T6 grounding) that no current tool queries below whole-component granularity; reactive rules firing over a typed projection could turn that latent structure into design feedback without the editing agent loading summarized best-practice text into its context window every time. Spiking the idea empirically, rather than deciding by argument, matches DEC-0337's research-before-build posture and DEC-0335's no-arbitrary-builds guard.

## Alternatives Considered

- **Decide on adoption now, by argument, without spikes** -- rejected; ActiveGraph's alpha-stage maturity and the compilation-lossiness risk raised at T4 make this an empirical question, not an armchair one.
- **Skip the idea entirely and keep design-knowledge access text-in-context only** -- rejected; the stakeholder judged the potential force-multiplier (T3) worth a bounded, guardrailed evaluation before dismissing it.
- **Evaluate only the structural-rule angle, skip hook-loop and fork-and-diff spikes** -- rejected; the stakeholder confirmed all five spikes (T9) as together answering the questions that matter for an eventual adoption decision.

## Implications

Five SP artifacts derive from EP-0009 under this decision, each carrying explicit evaluation criteria and data-source assumptions (per DEC-0355) and the throwaway-output guardrails of DEC-0351. No adoption of ActiveGraph or any spike output occurs by this decision alone -- DEC-0356 defers the DEC-0337 option survey to after the spikes report.
