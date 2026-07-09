---
id: DEC-0175
type: decision
title: CMP-0009 defaults to REST with GraphQL for gaps, disambiguates GitHub's overloaded 403 by header, and implements idempotency as check-before-create
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Settles CMP-0009's wire-protocol implementation guidance: REST
  primary with GraphQL for gaps, 403-to-error-type disambiguation via
  header inspection, and check-before-create idempotency mechanics on
  natural keys. Constrains normative implementation behavior on every
  CodeHostConnector operation.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0032 @ T2-T3"
links:
  derives-from: [SES-0032]
  relates-to: [DEC-0167, DEC-0172]
---

# DEC-0175: GitHub Wire-Protocol Conventions

## Context

CMP-0005
leaves the wire protocol, error mapping, and idempotency mechanics to
each adapter as Implementation Guidance, not contract. GitHub's REST
API has three properties CMP-0009
needed a concrete answer for: no general idempotency-key support on
creation endpoints, an HTTP 403 that is overloaded between
"permission-denied" and secondary rate-limit abuse detection, and a
choice between REST and GraphQL surfaces of unequal coverage.

## Decision

1. **REST primary, GraphQL for gaps.** REST and the Checks API back
   every operation family with adequate REST coverage (PRs, branches,
   checks, branch protection). GraphQL is used only where REST cannot
   get the data cheaply — e.g. CODEOWNERS-derived reviewer resolution,
   bulk team-membership queries.
2. **403 disambiguation by header.** A `403` response maps to
   `rate-limited` when `X-RateLimit-Remaining: 0` or a `Retry-After`
   header is present; otherwise it maps to `permission-denied`. This
   is a normative Implementation Guidance constraint, not a
   per-adapter judgment call.
3. **Idempotency via check-before-create.** Every creation call on a
   natural key (`provision_fork`, `branch.create`, `pr.open`) first
   reads for the existing resource; if found, that resource is
   returned instead of issuing the write. Satisfies
   DEC-0167's
   idempotency requirement without depending on GitHub's inconsistent
   "already exists" error strings across endpoints.

## Rationale

REST is the best-documented and most stable surface for exactly the
operation families this contract leans on hardest (Checks API, branch
protection); GraphQL earns its keep only where it saves real
round-trips. GitHub's secondary rate limits are a known abuse-detection
behavior that returns `403` instead of `429` — treating every `403` as
`permission-denied` would make a legitimate backoff case look like a
hard failure, and treating every `403` as `rate-limited` would mask
real authorization problems as transient. Check-before-create trades
one extra read per creation call for a robust, natural-key-based
idempotency guarantee that doesn't depend on parsing GitHub's
per-endpoint error text.

## Alternatives Considered

- **GraphQL primary**: fewer round-trips in aggregate, but a
  less-trodden path for the Checks/branch-protection surface this
  contract depends on most, and REST is still required for parts of
  that surface regardless.
- **Always treat 403 as permission-denied**: simpler, but would
  surface GitHub's secondary rate limits as hard authorization
  failures instead of retryable ones.
- **Create-then-catch-409/422**: fewer calls in the common
  first-time-creation case, but GitHub's "already exists" error
  strings aren't consistent across endpoints — a fragile parse target
  for something DEC-0167
  requires to be reliable.

## Implications

CMP-0009's
Implementation Guidance states both the REST/GraphQL split and the
403/idempotency conventions as normative constraints on every
`CodeHostConnector` operation the adapter implements.
