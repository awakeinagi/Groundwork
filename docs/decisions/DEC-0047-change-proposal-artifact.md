---
id: DEC-0047
type: decision
title: Change proposals are a first-class artifact type (CP)
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T4-T5"
links:
  derives-from: [SES-0005]
---

# DEC-0047: Change Proposal (CP) as a first-class artifact type

## Context

The drift flow ([DEC-0044](DEC-0044-drift-revert-capture-proposal.md))
captures edits as "change proposals" — a concept the taxonomy lacked.
Similar proposal-shaped input will arrive from UI suggestion-edits and,
eventually, implementation-swarm feedback.

## Decision

A new lightweight artifact type with prefix `CP`: captured diff, proposer
(person-id), source (`jira-drift` | `ui-suggestion` |
`implementation-feedback`), triage state (`pending` | `mechanical` |
`session` | `rejected`), linked `relates-to` the target artifact. The agent
triages: trivial → mechanical fix PR citing the CP; substantive → a
refinement session with the CP as input; rejected proposals persist with
their triage rationale.

## Rationale

One container for every "someone outside the pipeline wants this changed"
event gives proposals durable audit (including what was proposed and
declined) and a uniform triage flow, at the cost of one small spec.

## Alternatives Considered

- **Draft commit on the item branch**: an external edit mutating canonical
  drafts uninvited blurs the API-writes-only rule
  ([DEC-0029](DEC-0029-api-writes-git-reads.md)).
- **Session-only**: unactioned proposals evaporate without audit.

## Implications

New [SPEC-change-proposal](../specs/SPEC-change-proposal.md); checker and
common spec updated with the `CP` prefix; CP triage added to the session
agent's scope ([EP-0002](../epics/EP-0002-refinement-session-agent.md)).
