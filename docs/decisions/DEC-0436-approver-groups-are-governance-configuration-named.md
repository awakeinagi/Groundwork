---
id: DEC-0436
type: decision
title: "Approver groups are governance configuration: named groups, per-type policies, per-ID overrides, declared quorum"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0082 @ T33-T34, T37"
overview: >-
  Approver groups are defined once in governance configuration; gate
  policies map artifact types to groups, per-artifact-ID entries
  override the type mapping, and each policy entry declares a quorum
  (any/all/k) defaulting to any. Enforcement follows the DEC-0429
  levels: full projects into host required-reviewer config, basic
  uses a CI approval count, solo resolves to the operator unchanged.
  Confirmed by the stakeholder at SES-0082 T37.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0263, DEC-0428, DEC-0429, DEC-0036, DEC-0234]
---

# DEC-0436: Approver groups are governance configuration: named groups, per-type policies, per-ID overrides, declared quorum

## Context

Frontmatter can now record multiple approvals, but nothing yet says who is authorized to approve a given artifact, or how many of them must sign off. Governance-as-code (DEC-0263) needed an extension covering group membership, per-type and per-artifact policy, and quorum.

## Decision

Approver groups are defined once as named groups in the governance configuration. Gate policies map artifact types to groups, and per-artifact-ID entries may override the type-level mapping, with the ID-specific entry always taking precedence. Each policy entry declares its quorum — any one member, all members, or a stated number — defaulting to any, which preserves today's single-approver behavior until a team opts into stricter quorums.

## Rationale

Enforcement follows the DEC-0429 levels: at full, groups project into the host's required-reviewer configuration; at basic, a continuous-integration check counts frontmatter approvals against policy; at solo, everything resolves to the operator unchanged. Defaulting quorum to any keeps solo and lightly-staffed teams unaffected while giving stricter teams an explicit dial.

## Alternatives Considered

A single flat approver list per artifact type (no per-ID override, no quorum) was rejected as too coarse — it cannot express a high-stakes artifact needing a named specialist's sign-off distinct from its type's default reviewers.

## Implications

Governance configuration schema gains groups, per-type policy, per-ID override, and quorum fields. Enforcement at each of the three levels (DEC-0429) must read this schema; the DEC-0428 approval record supplies the approvals a policy check counts against.
