---
id: SP-0016
type: spike
title: "Reactive hook-loop economics"
status: approved
approved-on: 2026-07-11
approved-by: awakeinagi
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: does the edit-fires-rules loop pay for itself in context
  economy? SP-0016 wired the loop end-to-end (throwaway per
  DEC-0351, reusing SP-0014's projector and 24-rule rulebase,
  activegraph==1.9.0) and measured it descriptively, with no kill
  bar (DEC-0355). Base tests: a benign edit fired the PostToolUse
  hook and injected "no new structural findings" (~0.69s, ~35
  tokens); a seeded superseded-cite violation (DEC-0289 on CMP-0001)
  was caught, injected as a single delta finding (DEC-0118
  packaging), and corrected by the editing agent to successor
  DEC-0316 using only the injected finding, with no source texts
  read -- confirming the T3 context-window force-multiplier premise
  (DEC-0354). Cost: ~0.5s cold per edit over the 588-artifact
  corpus. Two stretch experiments addressed DEC-0368's open
  differential-evidence question: marginal cost is corpus-
  independent (~0.1ms/edit, ~140x cheaper than batch) only for self-
  scoped delta behaviors reading the triggering event -- built-in
  pattern subscriptions re-scan the whole graph and reach batch cost
  at scale; and loop safety holds only with idempotent rules or an
  enforced budget={max_events} cap, since an unguarded cyclic
  cascade is non-terminating. Resulting decisions: DEC-0374 (hook-
  loop is economically viable) and DEC-0375 (marginal-cost advantage
  is conditional; loop safety needs idempotence or budget caps).
  Depends on SP-0014 (impacted-by). Deliverable: measured demo
  report, complete.
links:
  impacted-by: [SP-0014]
  derives-from: [EP-0009]
  relates-to: [SP-0014]
cites: [DEC-0354, DEC-0351, DEC-0335, DEC-0337, DEC-0355, DEC-0345, DEC-0336, DEC-0315, DEC-0118, DEC-0289, DEC-0316, DEC-0368, DEC-0374, DEC-0375]
---

> Guardrails (DEC-0351): this spike's outputs are strictly throwaway and are never deployed as part of the artifact interaction surface. Adoption of anything it surfaces happens only through the ordinary path -- a DEC-0337 option survey followed by DEC-0335 design intake -- never by this spike's findings alone.

## Question

Does the edit-fires-rules loop pay for itself in context economy? Concretely: when an edit triggers a hook that projects the delta into ActiveGraph, fires SP-0014's rulebase, and injects findings back into the editing agent's context, what is the measured latency and token cost per edit, and does the agent catch and correct a seeded violation without ever loading the source best-practice text?

## Why It Blocks

Blocks nothing today. It is the direct test of the stakeholder's original T3 framing (context-window force-multiplier): if the hook loop is too slow or too token-expensive to be worth it, or the agent needs source text anyway to act on findings, the core economic case for DEC-0354's approach weakens.

## Method

Wire the loop end-to-end once: a PostToolUse hook on a design-editing agent projects the edit delta as events into the ActiveGraph run; SP-0014's rulebase fires over the updated projection; findings are injected back into the editing agent's context. Run a scripted design-edit task that includes a seeded violation and observe whether the agent catches and corrects it.

This spike builds a throwaway executable; per DEC-0345, its validation approach (the checks described above) is part of the reviewed spike design, not chosen ad hoc after the fact, and is sized minimally per DEC-0336's throwaway-scope yardstick.

This PostToolUse hook is itself a per-operation check in the sense DEC-0315 distinguishes from the full-checker pre-commit gate -- the same architecture question the check family answers for artifact writes. The findings-injection format follows DEC-0118's cite-ready two-tier output packaging precedent, so injected findings stay traceable to source.

## Evaluation Criteria
Descriptive measures, no pass/fail threshold (DEC-0355): measured latency per edit; tokens injected per edit; whether the seeded violation is caught and corrected without source best-practice texts in the editing agent's context.

## Data-Source Assumptions
SP-0014's rulebase exists and is available to fire against the hook-triggered projection. The Claude Code hook surface (PostToolUse) is available in the execution environment, and edit deltas are parseable into ActiveGraph events.

## Findings

SP-0016 wired the reactive hook loop end-to-end (throwaway per DEC-0351, reusing SP-0014's projector + 24-rule rulebase in a uv-managed venv, activegraph==1.9.0) and measured it; descriptive only, no kill bar (DEC-0355). Base tests: T-a, a benign edit by a live Sonnet design-editing agent fired the PostToolUse frontmatter hook end-to-end and injected 'no new structural findings' (~0.69s hook latency, ~35 injected tokens). T-c, a seeded R8 superseded-cite: the agent added superseded DEC-0289 to CMP-0001 invariant C-3, the hook injected only that edit-introduced finding (delta vs a clean baseline, DEC-0118 cite-ready packaging with the successor redirect), and the agent corrected DEC-0289 to DEC-0316 using only the injected finding, with no best-practice or decision source texts in its context (the successor appeared only in the injection; the agent read no decision files). Catch-and-correct cost: two hook fires (~0.5s each), ~99 injected tokens; cold per-edit latency ~0.5s over the 588-artifact corpus. Stretch 1 (marginal cost, addressing DEC-0368): batch cost grows linearly with corpus; ActiveGraph's built-in pattern subscriptions re-scan the whole graph on every firing (the v0.7 matcher ignores the triggering event) and reach batch cost at scale; only self-scoped delta behaviors reading event.payload are corpus-independent (~0.1 ms/edit, ~140x cheaper). Stretch 2 (loop economics): idempotent stale-propagation converges to a fixpoint even on dependency cycles; an unguarded cyclic cascade is non-terminating and only ActiveGraph's budget={max_events} cap halts it -- budget caps are load-bearing.

## Resulting Decisions

DEC-0374 -- the reactive hook-loop is economically viable for Groundwork's checker (base-test evidence: catch-and-correct from injected findings alone, ~0.5s and tiny token cost).
DEC-0375 -- the reactive-substrate marginal-cost advantage is conditional (self-scoped delta rules, not naive pattern subscriptions) and loop safety needs idempotence or budget caps; supplies the differential evidence DEC-0368 left open.

