---
id: SP-0016
type: spike
title: "Reactive hook-loop economics"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-10
timebox: 1 session
overview: >-
  Question: does the edit-fires-rules loop pay for itself in context
  economy? Method: wire end-to-end once -- a PostToolUse hook on a
  design-editing agent projects the edit delta as events into the
  ActiveGraph run; SP-0014 (SP-B)'s rulebase fires; findings are
  injected back into the editing agent's context; run a scripted
  design-edit task with a seeded violation. Depends on SP-0014
  (impacted-by). Evaluation criteria: measured latency per edit;
  tokens injected per edit; whether the seeded violation is caught
  and corrected without source texts in the agent's context --
  explicitly no kill bar (DEC-0355). Data-source assumptions:
  SP-0014's rulebase exists; Claude Code hook surface (PostToolUse)
  available and edit deltas parseable into events. Deliverable:
  measured demo report.
links:
  impacted-by: [SP-0014]
  derives-from: [EP-0009]
  relates-to: [SP-0014]
cites: [DEC-0354, DEC-0351, DEC-0335, DEC-0337, DEC-0355, DEC-0345, DEC-0336, DEC-0315, DEC-0118]
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

Pending — recorded at spike completion.


## Resulting Decisions

Pending — a completed spike produces at least one decision, even "assumption confirmed, no change."
