---
id: ST-0021
type: story
title: Delegated reviews and program-user attribution
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019, ST-0022]
  impacted-by: [ST-0019, ST-0022]
cites: [DEC-0033, DEC-0043, DEC-0046, DEC-0143, DEC-0152, DEC-0153, DEC-0154]
---

# ST-0021: Delegated Reviews and Program-User Attribution

## Summary

The machinery that turns a UI approval into an attributable host
review: posting as the approver via their linked OAuth identity where a
seat exists, and as the role-scoped program user with a service-signed
attribution block where it doesn't.

## Acceptance Criteria

1. An approver with a linked host identity has their UI approval posted
   as a host PR review *as them* — host-side audit shows the real
   person (per [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
2. For roles on the program-user path, the review body carries the
   structured attribution block — person-id, PR reference, decision
   timestamp — signed with the service's asymmetric key; the public key
   is available to verifiers via deployment configuration
   (per [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md),
   [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
3. The attribution block's schema and signing rules are published as a
   contract item so the `gate-policy` check can verify signature,
   person-id resolution, and role membership independently
   (per [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md),
   [DEC-0046](../decisions/DEC-0046-person-registry.md)).
4. Which roles use which path is read from deployment configuration;
   no governance file is consulted or modified
   (per [DEC-0154](../decisions/DEC-0154-review-path-mapping-deployment-config.md),
   [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)).
5. OAuth tokens and the signing key are stored and read only through
   the encrypted secret store; a token never appears in the repo, logs,
   or error output (per [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
   [DEC-0046](../decisions/DEC-0046-person-registry.md)).
6. An expired or revoked OAuth token fails the review post with a
   re-authorization prompt to the approver — never a silent fallback to
   the program user, which would misattribute the review path
   (per [DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md),
   [DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)).

## Component Impact

[CMP-0007](../components/CMP-0007-identity-and-access.md) — supplies
the review-delegation, token-handling, and attribution-signing
contract sections.

## Out of Scope

Program-user approvals of mechanical and System-Decision auto-PRs —
those are machine-verified by the diff/template checks and carry **no**
human attribution block; the attribution requirement applies only to
reviews that stand in for a human approver's gate decision
(per [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md),
[DEC-0143](../decisions/DEC-0143-system-decisions-via-auto-pr.md)).
Verifying the attribution at gate time — that's the `gate-policy`
check's side of the seam
([ST-0014](ST-0014-gate-policy-check.md), per
[DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md));
the UI review surface itself
([EP-0006](../epics/EP-0006-refinement-web-ui.md)); the host review
API plumbing ([ST-0019](ST-0019-code-host-connector-protocol.md)
defines it, [ST-0020](ST-0020-bitbucket-data-center-connector.md)
implements it).

## Notes for Implementers

The attribution block schema is produced here and consumed by
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) — a
contract-certain two-consumer seam; expect it to be weighed for
graduation at component review.
