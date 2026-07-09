---
id: ST-0031
type: story
title: GitHub connector
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  depends-on: [ST-0019]
  impacted-by: [ST-0019]
cites: [DEC-0043, DEC-0045, DEC-0079, DEC-0141, DEC-0145, DEC-0172, DEC-0173]
---

# ST-0031: GitHub Connector

## Summary

The v1 reference implementation of the code-host connector protocol:
GitHub (cloud), with an honest capability manifest, GitHub's Checks API
and required-status-checks as the required-check surface, CODEOWNERS
and org teams for reviewer/team routing, and GitHub webhooks feeding
the normalized event schema. Takes Bitbucket Data Center's former v1
slot (per DEC-0172).

## Acceptance Criteria

1. The connector implements the full protocol from
   ST-0019 and passes its
   conformance suite (per DEC-0172,
   DEC-0045).
2. Its capability manifest declares GitHub's real surface — including
   native path-scoped reviewer requirements via CODEOWNERS
   (`native_path_scoped_reviewers: true`, above-minimum, exploitable by
   the gate compiler as an optimization, never required — the
   service-computed `gate-policy` check remains load-bearing for
   role-conditional and committee-composition logic no host vocabulary
   expresses)
   (per DEC-0172,
   DEC-0045).
3. Required-check registration, unregistration, and result posting are
   implemented on GitHub's Checks API / required-status-checks surface,
   supporting per-PR blocking, idempotent re-posting on recomputation,
   and flipping an already-green check back to failing on an open PR
   (per DEC-0173,
   DEC-0145,
   DEC-0141).
4. Team administration maps role projections onto GitHub org teams
   (per DEC-0172).
5. GitHub webhook event families (pull_request, pull_request_review,
   push, check_run/check_suite) are translated into the protocol's
   normalized event schema with no host-specific payloads leaking to
   consumers
   (per DEC-0172,
   DEC-0045).
6. Consumer test suites that pass against the local-git fake pass
   against this connector unchanged — the swap-in is the pluggability
   validation, and this story is itself the first live proof of that
   pluggability (the reference host swapped from Bitbucket Data Center
   to GitHub without a protocol change)
   (per DEC-0079,
   DEC-0045,
   DEC-0172).

## Component Impact

CMP-0009 — the whole
component.

## Out of Scope

Other hosts, including the now-deferred Bitbucket Data Center
(ST-0020, deferred;
ST-0028, deferred); the
protocol itself (ST-0019);
Jira Data Center — a work-management concern
(ST-0025, deferred).

## Notes for Implementers

GitHub's Checks API distinguishes check runs (fine-grained, app-owned)
from commit statuses (legacy, coarser); use check runs — they carry
`details_url`, structured output, and re-run semantics that map cleanly
onto `CodeHostConnector.A-5`/`A-6`. GitHub Apps are the natural
credential model for the program-user review path
(DEC-0043);
OAuth Apps for the delegated-user path — both are identity's concern
(ST-0021), not this
story's.
