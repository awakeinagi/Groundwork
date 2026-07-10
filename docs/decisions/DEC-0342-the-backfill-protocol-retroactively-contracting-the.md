---
id: DEC-0342
type: decision
title: The backfill protocol — retroactively contracting the SES-0058 deliverables
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T6, T10-T11, T19"
overview: >-
  The as-built artifact-librarian and artifact-interact are
  retroactively documented and gated under BG-0002: Stories and both
  CMPs written intent-first from the decision record and caller
  expectations — never transcribed from the as-built — then the as-
  built diffed against them, every divergence explicitly
  dispositioned by the stakeholder (keep, via a recording decision,
  or fix, via a defect item). Strangler-shaped: first slice is the
  librarian's tool surface with its conformance check, then widen.
  Adversarial scenarios at gate; independent review via the system-
  architect reviewer moment; honest retro-documented provenance
  deriving from SES-0057/SES-0058/SES-0059; contract altitude
  preserved (DEC-0322's eval-loop territory stays out). Executes as
  the DEC-0339 epic's first stories after BG-0002 approves.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0324, DEC-0334, DEC-0341, DEC-0313, DEC-0292, DEC-0322, DEC-0339, DEC-0343]
---

# DEC-0342: The Backfill Protocol for the SES-0058 Deliverables

## Context

The artifact-librarian and artifact-interact exist and run, but no
Story states their requirements and no CMP states their contracts.
Round 1 ratified backfill-and-gate over grandfathering; the architect
debate supplied the discipline.

## Decision

The as-built librarian and skill are retroactively documented and
gated under BG-0002, by this protocol:

1. **Intent-first authoring:** the Story(s) and both CMPs are written
   from the decision record (DEC-0324..DEC-0334 and this session's
   decisions) and the callers' actual expectations — never transcribed
   from the as-built. Then the as-built is diffed against them.
2. **Every divergence is dispositioned explicitly** by the
   stakeholder: keep (a new decision records the acceptance) or fix
   (a defect item). Nothing is silently blessed by being already
   deployed.
3. **First slice: the librarian's tool surface** — the live symptom —
   gated with its conformance check (DEC-0341) before the wider
   contract; then widen.
4. **Adversarial gate scenarios** beyond the happy path (illegal
   writes, concurrent write tasks, model-class discontinuation,
   operations outside the DEC-0313 roster).
5. **Independent review:** the system-architect reviewer moment
   (DEC-0292) runs at each gate; the build's author does not review
   their own contract.
6. **Honest provenance:** the backfilled artifacts state they are
   retro-documented (the corpus's reconstructed-fidelity mechanism),
   deriving from SES-0057/SES-0058/SES-0059 — never simulating
   requirements-first history.
7. **Contract altitude:** DEC-0322's eval-loop territory (flag shapes,
   batch semantics, error formats) stays out of the contracts;
   transcribing it would turn every build iteration into a gate event.

## Rationale

Backfill inverts the gate-before-build order once, as repair; the
protocol exists so the repair cannot launder drift into contract
(the T15/T18 memory-mechanism episode already demonstrated both the
laundering risk and the correct sequence: research → options →
approval → implement).

## Alternatives Considered

- **Grandfather the as-built** — leaves the incident class untracked;
  rejected at T6.
- **Big-bang single gate** — rubber-stamps or blocks everything;
  rejected for the strangler-shaped slicing.

## Implications

Executes after BG-0002 and the DEC-0339 epic approve, as that epic's
first stories. The in-session hot-fix and memory mechanism (DEC-0343)
are inputs: the CMP contracts the ratified state, and the tool-grant
episode enters the contract's rationale lines.
