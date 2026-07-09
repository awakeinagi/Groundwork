---
id: DEC-0168
type: decision
title: The v1 minimum code-host capability set is core orchestration, review posting, read access, permission probe, and check-result posting
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Minimum capability set a host must support: fork provisioning, branch
  create/delete/push, PR open/merge/review-state reads, review posting,
  read-only browse/search under allowlist, permission probe,
  check-result posting. Above minimum (adaptable or emulatable): native
  check registration, team sync, review dismissal, path-scoped reviewer
  rules. None of minimum is BBDC-specific, holds even if SP-0004
  surfaces BBDC quirks.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T2"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0045, DEC-0050, DEC-0036]
---

# DEC-0168: Connector Minimum Capability Set

## Context

DEC-0045
requires a documented minimum capability set a host must support to
run Groundwork at all, with the gate engine's policy compiler adapting
to or emulating whatever a manifest declares above that minimum — but
never defined where the line sits. Bitbucket Data Center, the v1
baseline, already lacks native path-scoped reviewer rules
(DEC-0050), and
SP-0004 has not yet
confirmed BBDC's required-check surface — so the minimum set must not
assume capabilities still under spike.

## Decision

The minimum set a host must support to run Groundwork at all: fork
provisioning; branch create/delete/push; PR open/merge/review-state
reads; review posting (either the delegated-OAuth or program-user
path); read-only browse/search under the repo allowlist; a permission
probe; and check-run result posting (a host must be able to report
pass/fail on a PR somehow). **Above minimum, adaptable or emulatable**:
native required-check *registration*, team synchronization, review
dismissal, and native path-scoped reviewer rules — the service-computed
`gate-policy` check
(DEC-0036)
is precisely the emulation path when a host lacks these.

## Rationale

Every minimum-set item is either load-bearing for the fork-pull gate
mechanism itself (orchestration, review, check-result posting) or for
the agent's read context — none of it is BBDC-specific, so the set
holds even if SP-0004
surfaces BBDC quirks in the check-administration family. Treating
required-check *registration* as above-minimum (rather than mandatory)
keeps the minimum set from foreclosing hosts with weaker admin APIs
before the one open spike about admin-API feasibility even reports.

## Alternatives Considered

- **Require native check registration in the minimum** — simpler
  mental model, but forecloses weaker-admin-API hosts pre-emptively and
  is riskier given SP-0004
  hasn't yet confirmed BBDC's own surface is adequate.

## Implications

`CapabilityManifest`'s schema
(CMP-0005)
encodes exactly this minimum/above-minimum split; a manifest with any
minimum-set flag false makes a connector invalid for deployment.
