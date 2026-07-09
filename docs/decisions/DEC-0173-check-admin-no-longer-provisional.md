---
id: DEC-0173
type: decision
title: Check-administration operations are no longer provisional now that GitHub, not BBDC, is v1; SP-0004 is repurposed as a BBDC-revival spike
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0031 @ T1"
links:
  derives-from: [SES-0031]
  supersedes: [DEC-0166]
  relates-to: [DEC-0172, DEC-0150, DEC-0145, DEC-0141]
---

# DEC-0173: Check-Administration No Longer Provisional

## Context

DEC-0166 marked
`CodeHostConnector.A-5`/`A-6` (check-run result posting and
required-check registration) provisional because
SP-0004 had not yet
validated whether BBDC's merge-check / Code Insights surface could
support per-PR blocking, re-reporting, and un-passing an already-green
check. DEC-0172 moves v1 off
BBDC entirely, onto GitHub.

## Decision

`CodeHostConnector.A-5`/`A-6` are no longer provisional. GitHub's
required-status-checks and Checks API are documented, stable features
that support exactly the semantics
SP-0004 existed to
validate for BBDC: per-PR merge blocking on a named check, re-posting
results on recomputation
(DEC-0145), and
flipping a passed check back to failing on an open PR to re-block merge
(DEC-0141). SP-0004
is repurposed: it no longer blocks any current-release story, and is
deferred to backlog as the validation spike for if/when
ST-0020 (BBDC)
revives, per DEC-0172.

## Rationale

The provisional flag existed to protect the protocol from an unproven
host assumption; GitHub's check-administration surface is well
documented and widely relied upon (it is the mechanism nearly every
CI/CD integration on GitHub uses for exactly this blocking/re-reporting
pattern), so the same category of risk doesn't apply. Re-scoping
SP-0004 rather than
discarding it keeps the question answerable later without re-deriving
it from scratch.

## Alternatives Considered

- **Keep the provisional flag pending a GitHub-specific spike** —
  rejected: GitHub's Checks API behavior for these semantics is public,
  stable documentation, not an open unknown requiring a timeboxed
  spike against a live instance the way BBDC's less-documented
  Code Insights surface was.

## Implications

CMP-0005's
provisional banner, `A-5`/`A-6` flags, `IG-2`, and the related
Out-of-Scope entry are removed; the doc's `cites` list drops
DEC-0166 in
favor of this decision. ST-0020
and SP-0004 move to
`deferred`/`backlog` (per DEC-0172).
