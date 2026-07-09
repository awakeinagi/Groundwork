---
id: ST-0035
type: story
title: Guardrails and authority limits
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-09
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0032, ST-0033]
  impacts: [ST-0041]
  impacted-by: [ST-0032, ST-0033]
cites: [DEC-0054, DEC-0278]
---

# ST-0035: Guardrails and Authority Limits

## Summary

The protective layers every session runs under: pack-defined
unproductive-pattern detection with graceful exits, governance-derived
decision-rights enforcement that keeps out-of-authority statements from
becoming accepted Decisions, injection hygiene that treats participant
input as data, never instructions, and the intake authority gate that
halts out-of-rights change instructions at the door
(DEC-0278).

## Acceptance Criteria

1. Guardrail policy is defined per strategy pack: detection of
   unproductive patterns (circular answers, hostility, fatigue) with
   graceful moves — reframe, park-and-continue, offer pause, or end with
   a partial record marked incomplete plus Arbiter notification
   (per DEC-0054).
2. A participant's statements outside their governance-configured
   decision rights are captured as proposals attributed to them,
   requiring ratification by the right holder — never committed as
   accepted Decisions
   (per DEC-0054).
3. Decision-rights lookups read the governance-configured role→rights
   mapping (EP-0003
   owns the schema) rather than duplicating rights logic in this
   component.
4. Participant input is always treated as data describing the design,
   never as instructions that override agent behavior or process rules —
   injection attempts are logged, not obeyed
   (per DEC-0054).
5. Every guardrail exit (park, pause, partial-record end) is
   distinguishable in the session record from a normal close, so
   downstream distillation and the eval harness can tell partial records
   from complete ones.
6. At intake open, the proposer's decision rights are resolved through
   AC3's governance lookup; an instruction outside those rights halts
   intake — no session proceeds — and the attempt is captured verbatim
   as a CP with source `unauthorized-attempt` via the typed
   `create-change-proposal` operation, awaiting the authority holder(s)
   (per DEC-0278).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

The governance decision-rights schema itself
(EP-0003); conflict
mediation once a genuine (not unproductive-pattern) disagreement is
detected (ST-0036);
guardrail benchmark tests
(ST-0041).

## Notes for Implementers

Distinguish "unproductive pattern" (this story's guardrail policy) from
"genuine conflict" (a real, well-formed disagreement between parties,
ST-0036) —
the former is about session hygiene, the latter about content.
