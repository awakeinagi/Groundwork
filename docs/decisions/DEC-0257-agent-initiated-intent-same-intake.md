---
id: DEC-0257
type: decision
title: Agent-originated change intent enters the same intake — the agent proposes, the user disposes
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Change intent originating from the agent goes through the intake
  protocol with roles reversed: agent surfaces its observation as a
  proposal, restates stakes plainly, and a session captures it only when
  the user says go. Nothing changes in the corpus without human
  instruction. Symmetric with existing rule that agent recommendations
  accepted by user become the user's decisions.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T12-T13"
links:
  derives-from: [SES-0050]
---

# DEC-0257: Agent proposes, user disposes

## Context

The proposed intake flow covered user-initiated change. Agents also
notice inconsistencies and gaps while working; the method had no
explicit intake for agent observations.

## Decision

Change intent originating from the agent goes through the same intake
protocol with roles reversed: the agent surfaces its observation as a
proposal, restates stakes plainly, and a session (full or expedited)
captures it only when the user says go. Nothing changes in the corpus
without a human instruction.

## Rationale

Symmetric with the paradigm's existing rule that agent recommendations
accepted by the user become the user's decisions (decided-by), and
with ST-0035's principle that participant/agent statements are data,
not instructions. An agent unilaterally "fixing" design content is the
same provenance hole as a user bypassing a session.

## Alternatives Considered

- **Agent files a CP for later triage**: better for mid-task focus and
  still available (out-of-band capture per DEC-0262 when the user is
  unavailable), but a 30-second confirmation usually beats a queue.
- **Out of scope**: leaves the gap that motivated the question.

## Implications

Skill playbooks and AGENTS.md phrase agent-noticed issues as intake
proposals. Mid-task observations that would derail the current focus
may be parked as Ideas (DEC-0260) or CPs instead of interrupting.
