---
id: DEC-0331
type: decision
title: The librarian is stateless per task but keeps a persistent behavioral memory
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0058 @ T10-T11"
overview: >-
  Each librarian delegation is a self-contained task: the caller puts
  everything needed in the prompt, a fresh instance executes it, and
  the distilled result carries all state back — no cross-task
  continuation in the contract, so no instance ever acts on a stale
  view of the corpus. Stakeholder amendment on top of the stateless
  base: the librarian maintains a persistent memory it uses to refine
  its own behavior through experience and interaction with the user —
  recurring task shapes, effective distillation patterns, pitfalls,
  caller preferences. The memory is strictly behavioral: how the
  librarian works, never an alternate source of corpus truth — corpus
  facts live in the artifacts, and a memory entry contradicting the
  corpus is a bug. Memory location, format, and update discipline are
  build territory under the DEC-0322/DEC-0334 loop.
links:
  derives-from: [SES-0058]
  relates-to: [DEC-0324, DEC-0334]
---

# DEC-0331: Stateless per Task, with a Learning Memory

## Context

Task-level delegation (DEC-0324) left open whether a caller may
continue one librarian instance across chained tasks, and whether the
librarian accumulates any experience at all.

## Decision

- **Stateless contract**: fresh spawn per task; the prompt carries
  everything needed; results carry all state back. Continuation via
  messaging remains mechanically possible but is not part of the
  contract.
- **Learning memory (stakeholder amendment)**: the librarian keeps a
  persistent memory to refine its behavior through experience and
  interaction with the user — behavioral knowledge only (task
  patterns, distillation quality, pitfalls, preferences), never
  corpus facts.

## Rationale

Statelessness keeps the contract simple and eliminates
stale-instance drift. The memory recovers the benefit continuation
would have offered — getting better at recurring work — without
carrying corpus state between tasks.

## Alternatives Considered

- **Continuable instances** — saves re-priming on chains, but the
  instance's corpus view goes stale and errors compound; rejected as
  contract (though not mechanically forbidden).
- **Pure statelessness, no memory** — the facilitator's original
  recommendation; the stakeholder amended it at T11 to add the
  learning memory.

## Implications

The build (DEC-0334) fixes the memory's location, format, and update
discipline, and the definition instructs the librarian that memory
never overrides the corpus.
