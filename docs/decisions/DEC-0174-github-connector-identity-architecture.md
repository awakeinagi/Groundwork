---
id: DEC-0174
type: decision
title: CMP-0009 uses two GitHub Apps (Orchestrator, Reader) for credential separation; forks land in a dedicated service account; program-user reviews post under the Orchestrator App's bot identity
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0032 @ T2-T3"
links:
  derives-from: [SES-0032]
  relates-to: [DEC-0028, DEC-0043, DEC-0045, DEC-0153, DEC-0172]
---

# DEC-0174: GitHub Connector Identity Architecture

## Context

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)'s
`C-2` requires read-context credentials
(`CodeHostConnector.A-9`) to never be the same credential as
orchestration writes (`A-1`–`A-8`).
[DEC-0028](DEC-0028-fork-pull-pr-gating.md) has "the agent" own "a local
fork of the upstream doc repository" but never specified where that
fork lives on a real host. [DEC-0043](DEC-0043-oauth-reviews-program-user-fallback.md)'s
program-user review path needed a concrete GitHub identity.
[CMP-0009](../components/CMP-0009-github-connector.md) (GitHub, cloud)
had to answer all three concretely to be contract-complete.

## Decision

Three GitHub-specific identity choices, settled together as one
architecture:

1. **Two GitHub Apps.** A "Groundwork Orchestrator" App (write
   permissions: contents, pull requests, checks, administration/branch
   protection, and — where the installation grants it — org members)
   handles every `CodeHostConnector.A-1`–`A-8` operation. A separate
   "Groundwork Reader" App (read-only: contents, metadata) handles
   `A-9` allowlisted context reads, installed only on allowlisted
   repositories. The two Apps are structurally distinct installations
   with distinct tokens — `C-2`'s separation holds by construction,
   not by code-path convention.
2. **Dedicated fork account.** The Orchestrator App is installed on a
   dedicated service-owned GitHub account/org; `provision_fork`
   (`A-1`) forks land there, independent of the source repo's org
   membership or visibility settings.
3. **Program-user reviews post under the Orchestrator App's bot
   identity.** All role-scoped program-user reviews
   ([DEC-0043](DEC-0043-oauth-reviews-program-user-fallback.md)) post
   via the Orchestrator App's installation token, appearing host-side
   as the App's bot account (e.g. `groundwork[bot]`). Role
   differentiation is carried entirely in
   [DEC-0153](DEC-0153-service-signed-attribution-block.md)'s signed
   attribution block, not in distinct GitHub identities — no
   per-role GitHub account is provisioned.

## Rationale

Two Apps satisfy `C-2` structurally, which is stronger and cheaper to
audit than a single-App, code-enforced boundary that a future
permission-broadening PR could silently erode. A dedicated fork
account keeps forked item branches off the source org's own namespace,
matching the classic contributor fork-and-PR pattern
[DEC-0028](DEC-0028-fork-pull-pr-gating.md) already assumes. GitHub
Apps natively support posting reviews under their own bot identity, so
no additional per-role GitHub accounts need provisioning or
credentialing — the attribution block already carries the real human
identity, which is the property that actually matters for audit.

## Alternatives Considered

- **One GitHub App, two installations**: installation tokens from the
  same App share an identity in GitHub's own audit trail, weakening
  the separation `C-2` is for.
- **One App, one token, policy-enforced separation**: cheapest to
  build, but the guarantee lives only in code discipline and would
  silently break if the App's permission set were ever broadened for
  an unrelated reason.
- **Direct branches on the source repo (no literal fork)**: simpler,
  but diverges from [DEC-0028](DEC-0028-fork-pull-pr-gating.md)'s
  "local fork" language and puts in-refinement item branches directly
  on the source org's repo.
- **Dedicated machine-user account per role** for program reviews:
  matches host-native review semantics more tightly but multiplies
  credentials to provision and rotate, one per role-scoped program
  user, for no attribution benefit the signed block doesn't already
  provide.

## Implications

[CMP-0009](../components/CMP-0009-github-connector.md)'s
Implementation Guidance names both App registrations and their
permission sets explicitly. Deployment documentation (out of this
design's scope) must cover provisioning two App registrations instead
of one.
