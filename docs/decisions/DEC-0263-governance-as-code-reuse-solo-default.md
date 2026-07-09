---
id: DEC-0263
type: decision
title: Skill-only projects reuse the governance-as-code files, seeded at bootstrap with solo god-mode defaults
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  Skill-only projects use the same governance-as-code files the
  application is designed around: governance/roles.yaml, domains.yaml,
  gate-policies.yaml, people.yaml (DEC-0046)—versioned in repo, edited
  via normal PR/commit. Bootstrap seeds governance/ with solo god-mode
  defaults: one person holding all roles, every gate single-approver.
  A project later adopting the application imports governance unchanged.
  Reuses schema per DEC-0037 (audit trail for rights changes).
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T16-T18"
links:
  derives-from: [SES-0050]
  relates-to: [DEC-0020, DEC-0037, DEC-0046]
---

# DEC-0263: Local governance = the same governance-as-code files

## Context

Teams using only the skill (no application) need to configure who may
approve what — the stakeholder's examples: a committee (DS lead + eng
lead + PO) superseding decisions on one team, a solo developer holding
all authority on this project. Invent a config format, or reuse the
app's?

## Decision

Skill-only projects use the **same governance-as-code files** the
application is designed around (DEC-0037): `governance/roles.yaml`,
`governance/domains.yaml`, `governance/gate-policies.yaml`, plus
`governance/people.yaml` (DEC-0046) — versioned in the repo, edited
through the normal PR/commit flow. The skill's bootstrap **seeds**
`governance/` with **solo god-mode defaults**: one person (the
operator) holding all roles, every gate single-approver, committee
gates an edit away (policy vocabulary per DEC-0020). A project later
adopting the application imports its governance unchanged.

## Rationale

No second config format to drift; authority is a property of the
project, not the operator's machine, so it belongs versioned in the
repo; DEC-0037's rationale (audit trail for rights changes, clone
rebuilds full state) applies identically without the app. Solo-default
matches the overwhelmingly common case at zero setup friction.

## Alternatives Considered

- **A new skill-asset config file**: the original proposal; dropped in
  favor of reuse once DEC-0037 was on the table.
- **Skill-level (per-machine) config**: conflicting configs between
  collaborators; invisible to the audit trail.
- **Grill governance at bootstrap**: front-loads ceremony onto
  inception for a setting most projects leave at solo.

## Implications

Bootstrap gains `governance/` seeding; templates gain the seed files;
EP-0003 remains the schema owner — the seeds must stay a valid subset
of its schema (consistency obligation, reviewed at distillation).
AGENTS.md documents the files and the solo default.
