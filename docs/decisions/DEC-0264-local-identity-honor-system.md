---
id: DEC-0264
type: decision
title: Skill-only identity is declared and git-resolved — procedural enforcement locally, cryptographic enforcement is the application's
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T16-T17"
links:
  derives-from: [SES-0050]
  relates-to: [DEC-0046]
---

# DEC-0264: Local identity — declared, honor system

## Context

For the governance files (DEC-0263) to mean anything in skill-only
mode, the agent must know who is instructing it. Without the
application there is no auth layer.

## Decision

`governance/people.yaml` maps person-ids to git identities; the agent
resolves the current operator via git config and treats them as that
person (asking "who am I speaking with?" only when git identity is
missing or ambiguous). Enforcement is **procedural, not
cryptographic**: the agent applies gate policies and captures
unauthorized attempts as CPs (DEC-0262), but a determined local user
can edit anything — it is their repo. The paradigm's local guarantee
is provenance and honest capture, not tamper-proofing; real
enforcement (auth, attribution blocks, service-computed gate checks
per DEC-0036 and DEC-0153) is precisely the application's value-add.

## Rationale

Aligns with DEC-0046's person-id ↔ provider-identity registry shape
(git identity is just another provider). Per-session identity rituals
tax every session for a case git config answers nearly always; no
identity at all would leave the committee example inexpressible
locally and the unauthorized-attempt CP path dead.

## Alternatives Considered

- **Per-session declaration**: kept as the fallback, not the default.
- **No local identity**: drops the feature the stakeholder asked for.

## Implications

Documents an honest limitation: local governance is advisory-strength.
AGENTS.md states it plainly so teams needing hard enforcement know the
application is the boundary.
