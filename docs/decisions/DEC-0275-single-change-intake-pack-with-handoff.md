---
id: DEC-0275
type: decision
title: A single change-intake pack owns the protocol through path-pick and hands off in-session to the artifact-type pack
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T4-T5, T8-T9"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0053, DEC-0056, DEC-0256, DEC-0266]
---

# DEC-0275: One change-intake pack, with in-session hand-off

## Context

ST-0033 AC1 enumerates the closed pack set per artifact-type-and-phase
(goal-refinement, epic-refinement, story-refinement,
conflict-mediation, CP-triage). Intake cannot be per-artifact-type:
locate-first classification (DEC-0266) means the artifact level is not
known when the session opens. Separately, the protocol's step-tracking
mechanisms — the todo-list discipline (DEC-0256) and locate-first
itself — needed an application home.

## Decision

One new **change-intake pack** joins the closed set. It owns the
protocol from proposal through path-pick and classification, then
hands off in-session to the matching artifact-type pack for the
grilling body; the hand-off is recorded in the session. The expedited
path and idea-capture micro-sessions are phases/stopping-criteria of
this same pack. The protocol's step machinery is pack content, not new
contract: the pack's phase structure with stopping criteria *is* the
todo list (rendered by ST-0043's existing progress panel), and
locate-first is the pack's context recipe plus the on-demand
search/graph tools DEC-0056 already provides packs.

## Rationale

The protocol lives in exactly one place and evolves as eval-gated pack
versions. An intake phase duplicated across five packs has the
dependency order backwards — pack selection is what intake's
classification step determines. Engine-enforced step tracking would
over-harden the conversational layer DEC-0273 assigns to packs.

## Alternatives Considered

- **Intake phase in every artifact-type pack**: five duplicates, wrong
  dependency order.
- **Per-kind intake packs** (intake-goal, intake-epic, …):
  combinatorial growth, same wrong order.
- **Engine-enforced step machine / dedicated checklist UI story**:
  redundant — DEC-0273's invariants pin the corners that matter, and
  the progress panel already renders phase state.

## Implications

ST-0033 AC1's enumeration grows by one, with a new AC describing the
hand-off. No amendments to ST-0038 or ST-0043 — locate-first and step
tracking ride existing capabilities.
