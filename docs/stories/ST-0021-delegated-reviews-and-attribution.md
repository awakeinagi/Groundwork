---
id: ST-0021
type: story
title: Delegated reviews and program-user attribution
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
overview: >-
  Machinery turning UI approval into attributable host review: posting
  as the approver via their linked OAuth identity where available, or
  as role-scoped program user with service-signed attribution block.
  Attribution block schema published for gate verification. Tokens and
  signing key held in encrypted secret store.
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019, ST-0022]
  impacted-by: [ST-0019, ST-0022]
cites: [DEC-0033, DEC-0043, DEC-0046, DEC-0143, DEC-0152, DEC-0153, DEC-0154,
        DEC-0172, DEC-0232]
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
   person (per DEC-0043).
2. For roles on the program-user path, the review body carries the
   structured attribution block — person-id, PR reference, decision
   timestamp — signed with the service's asymmetric key; the public key
   is available to verifiers via deployment configuration
   (per DEC-0153,
   DEC-0043).
3. The attribution block's schema and signing rules are published as a
   contract item so the `gate-policy` check can verify signature,
   person-id resolution, and role membership independently
   (per DEC-0153,
   DEC-0046).
4. Which roles use which path is read from deployment configuration;
   no governance file is consulted or modified
   (per DEC-0154,
   DEC-0043).
5. OAuth tokens and the signing key are stored and read only through
   the encrypted secret store; a token never appears in the repo, logs,
   or error output (per DEC-0152,
   DEC-0046).
6. An expired or revoked OAuth token fails the review post with a
   re-authorization prompt to the approver — never a silent fallback to
   the program user, which would misattribute the review path
   (per DEC-0043,
   DEC-0153).

## Component Impact

CMP-0007 — supplies
the review-delegation, token-handling, and attribution-signing
contract sections.

CMP-0015 — supplies the
graduated secret-store contract the tokens and signing key live behind
(per DEC-0232).

## Out of Scope

Program-user approvals of mechanical and System-Decision auto-PRs —
those are machine-verified by the diff/template checks and carry **no**
human attribution block; the attribution requirement applies only to
reviews that stand in for a human approver's gate decision
(per DEC-0033,
DEC-0143).
Verifying the attribution at gate time — that's the `gate-policy`
check's side of the seam
(ST-0014, per
DEC-0153);
the UI review surface itself
(EP-0006); the host review
API plumbing (ST-0019
defines it, ST-0031 implements it for
v1, per DEC-0172;
ST-0020, deferred,
would implement it for Bitbucket Data Center).

## Notes for Implementers

The attribution block schema is produced here and consumed by
CMP-0004 — a
contract-certain two-consumer seam; expect it to be weighed for
graduation at component review.
