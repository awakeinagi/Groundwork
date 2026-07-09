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

Refine CMP-0007 from
stub to contract-complete: element decomposition from
ST-0021 and
ST-0022,
graduation questions flagged by
DEC-0153
and discovered in approved neighbors, and the contract semantics the
elements hang on. Settled context recapped at open:
DEC-0024,
DEC-0040,
DEC-0043,
DEC-0046,
DEC-0152,
DEC-0153,
DEC-0154.

## Transcript

**T1 (facilitator).** Presented the proposed eight-element decomposition
for CMP-0007 (AuthProvider protocol, AuthSubject value, IdentityService
service, RoleClaims value, HostIdentityLink entity, SecretStore
service, AttributionBlock value, ReviewDelegationService service) and
three structural findings from the approved neighbors: (1)
CMP-0009's `IG-5` already
stores webhook signing secrets in the encrypted app-database secret
store and CMP-0010 hands
the master key to "the app-database-backed secrets facility" — a
contract-certain second consumer, so the graduation rule applies to
SecretStore now; (2) AttributionBlock has exactly one external
consumer (CMP-0004
verifies; CMP-0005
passes it through opaquely); (3) a dependency cycle looms between
CMP-0004 and CMP-0007 (attribution block one way, governance-config
consumption the other). Asked four structural questions with
recommendations: SecretStore graduation (recommended: graduate),
AttributionBlock placement (recommended: keep in CMP-0007),
governance-schema sourcing (recommended: depend on CMP-0004's
GovernanceConfig), and the person-id migration split (recommended:
identity provides the mapping, CMP-0001 executes).

**T2 (participant).** Answered: graduate SecretStore to CMP-0015;
keep AttributionBlock in CMP-0007; **graduate GovernanceConfig out of
CMP-0004** into its own standalone CMP (chose beyond the
recommendation, accepting the CMP-0004 re-gate); migration split as
recommended (identity maps, CMP-0001 executes).

**T3 (facilitator).** Read back T2. Asked four contract-semantics
questions: session ownership between login and request-time identity
(recommended: CMP-0007 issues and validates sessions), OAuth-linking
dance ownership (recommended: CMP-0007 end-to-end, CMP-0011 exposes
the callback route only), signing-key rotation (recommended: `key_id`
in the attribution block, ordered active-public-key list in deployment
configuration), and SecretStore crypto specificity (recommended:
properties in the contract, named v1 defaults as Implementation
Constraints).

**T4 (participant).** Accepted all four recommendations.

**T5 (facilitator).** Surfaced a tension found cross-reading CMP-0004:
ST-0022
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
CMP-0004 re-gate; CMP-0009/CMP-0010 pointer amendments;
ST-0012/ST-0021/ST-0022 Component Impact additions.

**T8 (participant).** Confirmed all eight.

**T9 (facilitator).** Corrected a wrong premise from T1 before
recording: the governance file schemas are owned by CMP-0001
(`SchemaValidator.D-2`), not CMP-0004 — `GovernanceConfig.D-1`
explicitly defines no schema of its own, only the parsed in-memory
value. The schema-sourcing cycle claimed at T1 does not exist; the
duplication-of-evaluation rationale and the attribution/claims cycle
do. Asked whether decision 3 stands with corrected content: CMP-0016 =
GovernanceConfig value + RoleResolution service, schemas remaining
CMP-0001's (recommended), versus dropping the graduation or homing
RoleResolution in CMP-0007.

**T10 (participant).** Re-confirmed decision 3 on the corrected
premise: graduate the value plus RoleResolution to CMP-0016.

## Decisions Produced

- DEC-0232 — SecretStore graduates to CMP-0015
- DEC-0233 — AttributionBlock stays in CMP-0007
- DEC-0234 — GovernanceConfig value + RoleResolution graduate to CMP-0016
- DEC-0235 — migration split: identity maps, CMP-0001 executes
- DEC-0236 — CMP-0007 owns sessions; opaque server-side handles
- DEC-0237 — CMP-0007 owns the OAuth linking flow
- DEC-0238 — key_id in the attribution block; active-key list in deployment config
- DEC-0239 — crypto properties in contract; named defaults as constraints

## Consistency-Check Dispositions

`groundwork_consistency.py sweep`/`terms` over DEC-0232..0239
(protocol per DEC-0157/DEC-0158):

- CMP-0004,
  CMP-0009,
  CMP-0010,
  ST-0012,
  ST-0014,
  ST-0021,
  ST-0022
  — amended in this session's bundle (the ripple the decisions
  themselves mandate).
- ST-0042
  (surfaced by the sweep, previously unconsidered) — reviewed:
  consistent; it is the UI surface of the flows
  DEC-0236/DEC-0237
  give backend contracts to; its Component Impact intentionally awaits
  the UI epic's own CMP.
- CMP-0012 (`Job.D-2` secret
  references), ST-0024,
  ST-0057,
  ST-0060,
  EP-0003,
  EP-0005, and the
  remaining DEC-0033/DEC-0046/DEC-0043
  citers — reviewed: generic references to the store/flows that remain
  true under the graduations; no edits needed.
- `terms` hits (`IG-5`, `GovernanceConfig`, `SchemaValidator.D-2`,
  `migrate-person-ids`) — all point at the artifacts amended above or
  at CMP-0001,
  whose schema/allowlist ownership is unchanged (and confirmed: the
  `migrate-person-ids` executor exists there).

## Conflicts Raised

None. The T5 tension (duplicated delegation evaluation) was resolved
in-session by DEC-0234.
