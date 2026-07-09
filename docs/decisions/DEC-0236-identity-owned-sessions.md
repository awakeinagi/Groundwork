---
id: DEC-0236
type: decision
title: CMP-0007 issues and validates sessions as opaque, revocable server-side handles
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T3-T6"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0024]
---

# DEC-0236: Identity-Owned Sessions, Opaque Server-Side Handles

## Context

CMP-0011 requires an
authenticated Participant on every route via
ST-0022's
provider contract; who owns the session between login and
request-time identity was undefined.

## Decision

CMP-0007 issues and
validates sessions: `issue_session` after provider authentication,
`validate_session` on every request, `revoke_session` on logout. The
token is an opaque random handle; session state (person-id, expiry)
lives in the app database via the App Database Port bookkeeping
family. TTL comes from deployment configuration.

## Rationale

All identity state in one component; the API layer stays a thin
caller. Opaque server-side sessions are instantly revocable (logout,
role change) and fit the embedded single-process stack.

## Alternatives Considered

- **CMP-0011 mints its own cookie/JWT**: splits identity across two
  components; claim refresh and revocation get harder.
- **Stateless per-request auth**: awkward for the email provider path.
- **Signed stateless tokens**: revocation needs a denylist anyway;
  baked-in claims go stale against delegation windows.

## Implications

Role claims are resolved fresh at validation time, not baked into the
token; CMP-0011's
auth behavior is unchanged (it already delegates to this contract).
