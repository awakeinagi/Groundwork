---
id: DEC-0043
type: decision
title: PR reviews post as the approver via OAuth, with a program-user fallback
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T2-T3"
links:
  derives-from: [SES-0005]
---

# DEC-0043: OAuth reviews as the approver; program-user fallback

## Context

The UI wraps the PR gate (DEC-0032), so an
approve click must become a host PR review — but business approvers may not
have code-host seats.

## Decision

Approvers with host identities connect them once via OAuth; the connector
posts reviews *as them*, so host-side audit shows the real person. Roles
whose members lack host seats approve through a role-scoped program user,
with the human approver's identity cryptographically attributed in the
review body and the governance event log, and the `gate-policy` check
verifying the attribution. Which roles use which path is per-deployment
configuration.

## Rationale

Preserves host-native audit wherever seats exist without making seat
procurement a blocker for business participation; the attribution +
verification pair keeps the fallback honest.

## Alternatives Considered

- **Mandate seats for all**: blocked by seat cost / IT policy in some orgs.
- **Program users only**: host audit shows only bots; committee gates
  degrade to bot arithmetic.

## Implications

The connector contract includes delegated-review (OAuth token per user) and
program-user review operations; the person registry
(DEC-0046) stores the OAuth linkage.
