---
id: DEC-0046
type: decision
title: A PR-gated person registry maps stable person-ids to provider identities
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T2-T3"
links:
  derives-from: [SES-0005]
---

# DEC-0046: Person registry — governance/people.yaml

## Context

One human exists as an OIDC subject, a Bitbucket username, and a Jira
accountId; `decided-by`/`approved-by` provenance needs an identity that
survives provider swaps (DEC-0024) and
renames.

## Decision

`governance/people.yaml` — PR-gated like all governance
(DEC-0037) — maps a stable person-id to
display name, email, auth subject, host username(s), and Jira accountId.
Artifacts reference the person-id; each connector resolves its own column;
the Admin UI edits the file like any governance config.

## Rationale

Provenance is the system's spine; its identity keys belong in the
clone-rebuildable repo, not a service table or mutable email.

## Alternatives Considered

- **Service identity table**: person linkage lost to clones.
- **Email as key**: breaks on rename/rehire; depends on host search APIs.

## Implications

Existing artifacts use emails as owner/decided-by values from the bootstrap
period; a mechanical migration to person-ids happens when the registry is
first populated. OAuth token references
(DEC-0043) key off
person-id; tokens themselves stay in the service's secret store, never in
the repo.
