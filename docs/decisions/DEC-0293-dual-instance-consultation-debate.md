---
id: DEC-0293
type: decision
title: Every system-architect consultation runs a dual-instance debate — record-grounded vs best-practice-independent — with a capped exchange; the verdict is a proposal
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0054 @ T11-T14"
overview: >-
  Every system-architect consultation (both moments of DEC-0292)
  spawns two instances of the agent: a record-grounded instance whose
  packet includes the relevant accepted decisions and which must
  ground its advice in them, and a best-practice-independent instance
  that advises unconstrained. The facilitator relays positions between
  them for at most two rebuttal rounds; they yield a joint verdict or
  a documented disagreement presented as alternatives. The verdict is
  always a proposal the stakeholder ratifies; where it recommends
  contradicting an accepted decision, that lands only via normal
  supersession — advice never overrides the record. Stakeholder-
  amended design (SES-0054 T12): the independent instance exists to
  discover tensions the grounded instance might rationalize away.
links:
  derives-from: [SES-0054]
  relates-to: [DEC-0292]
---

# DEC-0293: Dual-Instance Consultation Debate

## Context

A best-practices advisor grounded in the accepted decision record can
rationalize existing choices instead of challenging them; one advising
unconstrained re-litigates settled decisions. The stakeholder amended
the facilitator's grounded-only recommendation into a two-instance
debate (SES-0054 T12).

## Decision

Every consultation — both the advisor and reviewer moments of
DEC-0292 — runs as a **dual-instance debate**:

1. Spawn two instances of the system-architect agent:
   - **Record-grounded**: its consultation packet includes the
     relevant accepted decisions; it must ground advice in them and
     explicitly flag any tension.
   - **Best-practice-independent**: it advises purely from best
     practices, blind to the decision record.
2. The facilitator relays positions between the instances for at most
   **two rebuttal rounds**.
3. The instances yield a **joint verdict**, or a **documented
   disagreement** the facilitator presents as alternatives.
4. The outcome is always a **proposal the stakeholder ratifies**.
   Where it recommends contradicting an accepted decision, the change
   lands only via normal supersession; advice never overrides the
   record.

## Rationale

Running the debate on every consultation (not escalation-only) was
chosen because the independent instance can discover tensions the
grounded instance rationalizes away — escalation-only gives a second
opinion only to tensions the grounded instance itself notices. The
two-round cap bounds cost and avoids artificial consensus; documented
disagreement is a valid, presentable outcome. Proposal status keeps
the debate consistent with the standing rule that non-decider
statements need ratification.

## Alternatives Considered

- **Grounded instance only, tensions raised as topics** — the
  facilitator's original recommendation; superseded by the
  stakeholder's amendment for the rationalization-blindness reason.
- **Escalation-only debate** — half the cost; rejected as above.
- **Free discussion until convergence** — rejected: unbounded cost and
  risk of artificial consensus.
- **Third-instance arbiter** — rejected: one more strong-model spawn
  per debate for marginal tiebreak value.

## Implications

Each DEC-0292 consultation moment costs two strong-model spawns plus
up to two facilitator-mediated relay rounds — with advisor and
reviewer moments both required at EP/ST/CMP, four spawns per artifact
is the steady state. The facilitator's playbooks must assemble two
distinct consultation packets (with and without the relevant accepted
decisions). Debate outcomes reach the record via DEC-0296.
