---
id: DEC-0032
type: decision
title: The Groundwork UI wraps the PR; approvers never need the code host
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0003 @ T4-T5"
links:
  derives-from: [SES-0003]
---

# DEC-0032: The UI wraps the PR gate

## Context

PR approval is the gate sign-off ([DEC-0028](DEC-0028-fork-pull-pr-gating.md)),
but people interface with Groundwork via its UI
([DEC-0002](DEC-0002-doc-store-canonical.md)) — a Product Owner approving a
Business Goal should not need to navigate a Bitbucket/GitHub pull request.

## Decision

The Groundwork UI renders the gate as a rich review surface (artifact diff,
provenance, impact report) and its approve/request-changes actions drive the
host's PR-review API through the code-host connector. The PR remains the
durable, auditable gate record. Technical users may also review host-side;
both paths land in the same PR record. Committee gates
([DEC-0020](DEC-0020-configurable-gate-policies.md)) map onto the host's
required-reviewer/approval-count mechanics, configured by the gate engine.

## Rationale

Keeps the single-surface promise for business users while making the host's
PR machinery — reviews, required checks, merge protection — the enforcement
substrate instead of a parallel app-internal approval store.

## Alternatives Considered

- **Host-native only**: requires code-host seats and git literacy from
  business stakeholders.
- **UI approval with mechanical auto-merge**: splits the audit trail; the PR
  no longer shows who approved.

## Implications

Approvers need host identities the connector can act for (or on behalf of,
via delegated review) — an EP-0005 contract requirement. Gate-policy
configuration (EP-0003) compiles down to host branch-protection settings.
