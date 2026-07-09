---
id: DEC-0054
type: decision
title: Sessions enforce guardrail policies, role decision rights, and injection hygiene
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0006 @ T2-T3"
links:
  derives-from: [SES-0006]
---

# DEC-0054: Guardrails, authority limits, injection hygiene

## Context

Unsupervised sessions (DEC-0003) will
encounter confused participants, unusable answers, scope creep, and people
"deciding" things outside their authority — with no facilitator present.

## Decision

Three layers. **Guardrail policy** (defined per strategy pack): detection
of unproductive patterns (circular answers, hostility, fatigue) with
graceful moves — reframe, park-and-continue, offer pause, or end with a
partial record marked incomplete plus Arbiter notification. **Authority
limits**: governance config defines each role's decision rights; a
participant's statements outside their rights are captured as *proposals*
attributed to them, requiring ratification by the right holder — never as
accepted Decisions. **Injection hygiene**: participant input is always
treated as data, never as instructions to the agent.

## Rationale

The unsupervised bet fails on the worst session, not the average one;
authority limits keep overreach out of accepted DECs that downstream
contracts would cite before any gate sees them.

## Alternatives Considered

- **Escalate early, always**: reintroduces the facilitator by the back
  door.
- **Trust the participant**: authority overreach lands in accepted
  provenance.

## Implications

`governance/roles.yaml` gains decision-rights configuration — an EP-0003
config-schema extension (new impact edge EP-0002→EP-0003). Guardrail
behavior is eval-tested (DEC-0058).
