---
id: ST-0022
type: story
title: Identity — auth providers and person resolution
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0012]
  impacts: [ST-0021]
cites: [DEC-0024, DEC-0033, DEC-0040, DEC-0046, DEC-0152, DEC-0232, DEC-0234]
---

# ST-0022: Identity — Auth Providers and Person Resolution

## Summary

Who anyone is, durably: the pluggable auth-provider contract with the
v1 email/OIDC provider, resolution from auth subject to stable
person-id via `governance/people.yaml`, role claims for the gate
engine, OAuth host-identity linkage, and the one-time migration of
bootstrap-era email identities.

## Acceptance Criteria

1. Authentication sits behind a provider contract (authenticate →
   auth subject); v1 ships a simple email/OIDC provider, and swapping
   in organizational SSO is a new adapter, not a core change
   (per DEC-0024).
2. Auth subjects resolve to stable person-ids via
   `governance/people.yaml`; artifacts and provenance fields reference
   person-ids, and each connector resolves its own identity column
   (host username, Jira accountId) from the same registry entry
   (per DEC-0046).
3. Role claims are resolved for an authenticated person from
   `governance/roles.yaml` membership **including active time-bounded
   delegation entries** — a delegate holds the role's claims exactly
   while the delegation window is open — and exposed to the gate
   engine's policy evaluation
   (per DEC-0046,
   DEC-0040,
   DEC-0024).
4. Per-user OAuth host-identity linkage is keyed by person-id, with
   tokens held envelope-encrypted in the app database via the App
   Database Port — never in the repo
   (per DEC-0152,
   DEC-0046).
5. When the registry is first populated, a mechanical migration
   rewrites bootstrap-period email values in `owner`/`decided-by`/
   `approved-by` frontmatter to person-ids — metadata-only, via the
   `migrate-person-ids` operation of the typed mechanical-write
   allowlist (ST-0006)
   (per DEC-0046,
   DEC-0033).

## Component Impact

CMP-0007 — supplies
the auth-provider protocol, person-resolution, session, and role-claims
contract sections.

CMP-0015 — supplies the
graduated secret-store contract OAuth tokens live behind
(per DEC-0232).

CMP-0016 —
supplies the `RoleClaims` schema and shared delegation-window
evaluation behind the role-claims criterion
(per DEC-0234).

## Out of Scope

Review posting and attribution
(ST-0021); the
`governance/people.yaml` schema itself — owned by
ST-0012; login/session UI
(EP-0006); Participant
Profiles — interaction memory, not identity
(EP-0002).
