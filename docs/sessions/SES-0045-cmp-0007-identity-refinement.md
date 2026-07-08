---
id: SES-0045
type: session
title: CMP-0007 Identity & Access refinement — structure, seams, and contract semantics
status: closed
owner: eng-lead
created: 2026-07-08
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: "Claude Code (claude-fable-5), groundwork-design-session skill"
transcript-fidelity: reconstructed
links:
  relates-to: [CMP-0007, CMP-0015, CMP-0016, CMP-0004, ST-0021, ST-0022]
---

# SES-0045: Identity & Access Component Refinement

## Purpose

Refine [CMP-0007](../components/CMP-0007-identity-and-access.md) from
stub to contract-complete: element decomposition from
[ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md) and
[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md),
graduation questions flagged by
[DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md)
and discovered in approved neighbors, and the contract semantics the
elements hang on. Settled context recapped at open:
[DEC-0024](../decisions/DEC-0024-pluggable-auth.md),
[DEC-0040](../decisions/DEC-0040-role-pool-delegation.md),
[DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md),
[DEC-0046](../decisions/DEC-0046-person-registry.md),
[DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
[DEC-0153](../decisions/DEC-0153-service-signed-attribution-block.md),
[DEC-0154](../decisions/DEC-0154-review-path-mapping-deployment-config.md).

## Transcript

**T1 (facilitator).** Presented the proposed eight-element decomposition
for [CMP-0007](../components/CMP-0007-identity-and-access.md) (AuthProvider protocol, AuthSubject value, IdentityService
service, RoleClaims value, HostIdentityLink entity, SecretStore
service, AttributionBlock value, ReviewDelegationService service) and
three structural findings from the approved neighbors: (1)
[CMP-0009](../components/CMP-0009-github-connector.md)'s `IG-5` already
stores webhook signing secrets in the encrypted app-database secret
store and [CMP-0010](../components/CMP-0010-composition-root.md) hands
the master key to "the app-database-backed secrets facility" — a
contract-certain second consumer, so the graduation rule applies to
SecretStore now; (2) AttributionBlock has exactly one external
consumer ([CMP-0004](../components/CMP-0004-governance-gate-engine.md)
verifies; [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
passes it through opaquely); (3) a dependency cycle looms between
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) and [CMP-0007](../components/CMP-0007-identity-and-access.md) (attribution block one way, governance-config
consumption the other). Asked four structural questions with
recommendations: SecretStore graduation (recommended: graduate),
AttributionBlock placement (recommended: keep in [CMP-0007](../components/CMP-0007-identity-and-access.md)),
governance-schema sourcing (recommended: depend on [CMP-0004](../components/CMP-0004-governance-gate-engine.md)'s
GovernanceConfig), and the person-id migration split (recommended:
identity provides the mapping, [CMP-0001](../components/CMP-0001-artifact-store-service.md) executes).

**T2 (participant).** Answered: graduate SecretStore to [CMP-0015](../components/CMP-0015-secret-store.md);
keep AttributionBlock in [CMP-0007](../components/CMP-0007-identity-and-access.md); **graduate GovernanceConfig out of
[CMP-0004](../components/CMP-0004-governance-gate-engine.md)** into its own standalone CMP (chose beyond the
recommendation, accepting the [CMP-0004](../components/CMP-0004-governance-gate-engine.md) re-gate); migration split as
recommended (identity maps, [CMP-0001](../components/CMP-0001-artifact-store-service.md) executes).

**T3 (facilitator).** Read back T2. Asked four contract-semantics
questions: session ownership between login and request-time identity
(recommended: [CMP-0007](../components/CMP-0007-identity-and-access.md) issues and validates sessions), OAuth-linking
dance ownership (recommended: [CMP-0007](../components/CMP-0007-identity-and-access.md) end-to-end, [CMP-0011](../components/CMP-0011-inbound-api.md) exposes
the callback route only), signing-key rotation (recommended: `key_id`
in the attribution block, ordered active-public-key list in deployment
configuration), and SecretStore crypto specificity (recommended:
properties in the contract, named v1 defaults as Implementation
Constraints).

**T4 (participant).** Accepted all four recommendations.

**T5 (facilitator).** Surfaced a tension found cross-reading [CMP-0004](../components/CMP-0004-governance-gate-engine.md):
[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)
AC3 exposes role claims (with delegation windows) to the gate engine,
but approved `GatePolicyCheck.B-1/B-3` has the gate engine evaluating
roles and delegation itself — delegation-window logic would exist
twice. Asked whether the graduated governance-config CMP should carry
a shared RoleResolution service (recommended), plus the session-token
form (recommended: opaque server-side handles via the App Database
Port bookkeeping family).

**T6 (participant).** Accepted both recommendations: the graduated CMP
carries schemas-plus-RoleResolution; sessions are opaque server-side
handles with deployment-configured TTL.

**T7 (facilitator).** Played back eight decisions in plain language
(secret-store graduation; attribution block stays; governance-config
graduation with RoleResolution; migration split; identity-owned
sessions; identity-owned OAuth dance; key_id rotation scheme;
secret-store crypto discipline) with the amendment ripple:
[CMP-0004](../components/CMP-0004-governance-gate-engine.md) re-gate; [CMP-0009](../components/CMP-0009-github-connector.md)/[CMP-0010](../components/CMP-0010-composition-root.md) pointer amendments;
[ST-0012](../stories/ST-0012-governance-config-schemas.md)/[ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md)/[ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md) Component Impact additions.

**T8 (participant).** Confirmed all eight.

**T9 (facilitator).** Corrected a wrong premise from T1 before
recording: the governance file schemas are owned by [CMP-0001](../components/CMP-0001-artifact-store-service.md)
(`SchemaValidator.D-2`), not [CMP-0004](../components/CMP-0004-governance-gate-engine.md) — `GovernanceConfig.D-1`
explicitly defines no schema of its own, only the parsed in-memory
value. The schema-sourcing cycle claimed at T1 does not exist; the
duplication-of-evaluation rationale and the attribution/claims cycle
do. Asked whether decision 3 stands with corrected content: [CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md) =
GovernanceConfig value + RoleResolution service, schemas remaining
[CMP-0001](../components/CMP-0001-artifact-store-service.md)'s (recommended), versus dropping the graduation or homing
RoleResolution in [CMP-0007](../components/CMP-0007-identity-and-access.md).

**T10 (participant).** Re-confirmed decision 3 on the corrected
premise: graduate the value plus RoleResolution to [CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md).

## Decisions Produced

- [DEC-0232](../decisions/DEC-0232-graduate-secret-store.md) — SecretStore graduates to [CMP-0015](../components/CMP-0015-secret-store.md)
- [DEC-0233](../decisions/DEC-0233-attribution-block-stays-in-cmp-0007.md) — AttributionBlock stays in [CMP-0007](../components/CMP-0007-identity-and-access.md)
- [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md) — GovernanceConfig value + RoleResolution graduate to [CMP-0016](../components/CMP-0016-governance-config-and-role-resolution.md)
- [DEC-0235](../decisions/DEC-0235-person-id-migration-split.md) — migration split: identity maps, [CMP-0001](../components/CMP-0001-artifact-store-service.md) executes
- [DEC-0236](../decisions/DEC-0236-identity-owned-sessions.md) — [CMP-0007](../components/CMP-0007-identity-and-access.md) owns sessions; opaque server-side handles
- [DEC-0237](../decisions/DEC-0237-identity-owned-oauth-linking.md) — [CMP-0007](../components/CMP-0007-identity-and-access.md) owns the OAuth linking flow
- [DEC-0238](../decisions/DEC-0238-attribution-key-rotation.md) — key_id in the attribution block; active-key list in deployment config
- [DEC-0239](../decisions/DEC-0239-secret-store-crypto-properties.md) — crypto properties in contract; named defaults as constraints

## Consistency-Check Dispositions

`groundwork_consistency.py sweep`/`terms` over [DEC-0232](../decisions/DEC-0232-graduate-secret-store.md)..0239
(protocol per [DEC-0157](../decisions/DEC-0157-relates-to-sweep-at-distillation.md)/[DEC-0158](../decisions/DEC-0158-identifier-cooccurrence-audit.md)):

- [CMP-0004](../components/CMP-0004-governance-gate-engine.md),
  [CMP-0009](../components/CMP-0009-github-connector.md),
  [CMP-0010](../components/CMP-0010-composition-root.md),
  [ST-0012](../stories/ST-0012-governance-config-schemas.md),
  [ST-0014](../stories/ST-0014-gate-policy-check.md),
  [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md),
  [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md)
  — amended in this session's bundle (the ripple the decisions
  themselves mandate).
- [ST-0042](../stories/ST-0042-identity-login-and-oauth-linking.md)
  (surfaced by the sweep, previously unconsidered) — reviewed:
  consistent; it is the UI surface of the flows
  [DEC-0236](../decisions/DEC-0236-identity-owned-sessions.md)/[DEC-0237](../decisions/DEC-0237-identity-owned-oauth-linking.md)
  give backend contracts to; its Component Impact intentionally awaits
  the UI epic's own CMP.
- [CMP-0012](../components/CMP-0012-queue-port.md) (`Job.D-2` secret
  references), [ST-0024](../stories/ST-0024-notifier-connector-email-adapter.md),
  [ST-0057](../stories/ST-0057-composition-root.md),
  [ST-0060](../stories/ST-0060-queue-port.md),
  [EP-0003](../epics/EP-0003-governance-and-gate-engine.md),
  [EP-0005](../epics/EP-0005-connectors-and-identity.md), and the
  remaining [DEC-0033](../decisions/DEC-0033-typed-mechanical-writes.md)/[DEC-0046](../decisions/DEC-0046-person-registry.md)/[DEC-0043](../decisions/DEC-0043-oauth-reviews-program-user-fallback.md)
  citers — reviewed: generic references to the store/flows that remain
  true under the graduations; no edits needed.
- `terms` hits (`IG-5`, `GovernanceConfig`, `SchemaValidator.D-2`,
  `migrate-person-ids`) — all point at the artifacts amended above or
  at [CMP-0001](../components/CMP-0001-artifact-store-service.md),
  whose schema/allowlist ownership is unchanged (and confirmed: the
  `migrate-person-ids` executor exists there).

## Conflicts Raised

None. The T5 tension (duplicated delegation evaluation) was resolved
in-session by [DEC-0234](../decisions/DEC-0234-graduate-governance-config-role-resolution.md).
