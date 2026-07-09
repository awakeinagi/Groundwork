---
id: DEC-0282
type: decision
title: Agent-originated change intent needs no new application contract — the gate topology and intake invariants already force user disposition
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  DEC-0282 constrains IDEA-0001's scope by noting that agent-originated
  change intent needs no new application contract: an application agent
  cannot land semantic change without a human-approved gate PR,
  in-conversation proposals only become sessions when the participant
  confirms, park-as-Idea is already agent-proposable, and origin: agent in
  the intake context records provenance when sessions open. The gate
  topology already enforces user disposition.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T10-T11"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0054, DEC-0257, DEC-0270]
---

# DEC-0282: Agent-proposes/user-disposes is covered structurally

## Context

DEC-0257 (paradigm): agent-originated change intent enters the same
intake — the agent proposes, the user disposes; nothing changes
without a human instruction. Does the application need a contract line
for it?

## Decision

No new contract. An application agent cannot land semantic change
without a human-approved gate PR, its in-conversation proposals only
become sessions when the participant confirms (the alignment
invariant, DEC-0273), park-as-Idea is already agent-proposable
(ST-0065 AC1, DEC-0270), and drift CPs cover out-of-band capture. The
intake pack phrases agent observations as proposals — pack content —
and `origin: agent` in the intake context (DEC-0274) records the
provenance when a session does open. The correspondence is recorded
here rather than mechanized.

## Rationale

A contract line that restates what the gate topology already forces is
redundant, and redundant contract lines drift. ST-0035 AC4's
data-not-instructions rule is the same principle from the other
direction.

## Alternatives Considered

- **Explicit AC in ST-0035**: harmless but duplicative.
- **Eval-harness-only treatment**: testing a rule stated nowhere gives
  the eval nothing contractual to test against.

## Implications

No artifact amendments beyond the `origin: agent` enum value DEC-0274
already carries.
