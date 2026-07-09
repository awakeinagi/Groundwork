---
id: DEC-0172
type: decision
title: GitHub (cloud) is the v1 code-host connector; Bitbucket Data Center is deferred to backlog behind a demand trigger
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0031 @ T1"
links:
  derives-from: [SES-0031]
  supersedes: [DEC-0050]
  relates-to: [DEC-0045, DEC-0036, DEC-0150, DEC-0156]
---

# DEC-0172: GitHub Is the v1 Code-Host Connector

## Context

DEC-0050 picked Bitbucket Data
Center as the sole v1 host on the assumption that it matched the
organization's actual hosting. This repository's own remote is
`github.com/awakeinagi/Groundwork` — the actual dogfooding target is
GitHub Cloud, not BBDC, and BBDC required a real instance (via
SP-0004) this
conversation doesn't have access to.

## Decision

**GitHub (cloud, github.com)** — not GitHub Enterprise Server — is the
v1 code-host connector's reference implementation. Bitbucket Data
Center is **deferred to backlog**, subscribed to a new trigger
(`TRG-0010`: a deployment requires Bitbucket Data Center) alongside its
validation spike. This is a straightforward swap, not an architecture
change: CMP-0005's
protocol is already host-agnostic and capability-declaring
(DEC-0045) — the
pluggability that decision bought is exactly what makes this swap cheap
and is itself the first real validation of that pluggability, ahead of
schedule (originally ST-0028's
job). DEC-0036's
two-layer gate design (host branch protection + service `gate-policy`
check) is unaffected: its driver is committee composition and
role-conditional approval logic that exceeds any host's native
vocabulary, GitHub's CODEOWNERS included — GitHub's richer native rules
(path-scoped CODEOWNERS reviewers, required status checks, a documented
Checks API) are an implementation-quality improvement
CMP-0006/CMP-0009
can lean on more heavily, not a reason to remove the service-computed
layer.

## Rationale

Matches the actual, available dogfooding environment; avoids blocking
the connector build on SP-0004,
a timeboxed spike against a real BBDC instance this session cannot run.
GitHub's documented Checks API and required-status-checks are known to
support per-PR blocking, re-reporting, and flipping an already-green
check back to failing on an open PR — precisely the semantics
SP-0004 existed to
validate for BBDC — so the check-administration risk that spike
tracked doesn't apply to the new v1 target
(see DEC-0173).
Deferring rather than dropping BBDC preserves two sessions' worth of
groundwork (DEC-0050's
rationale, SP-0004's
spike design) for if/when a self-hosted deployment needs it.

## Alternatives Considered

- **GitHub Enterprise Server** — architecturally closer to BBDC
  (self-hosted, similar admin-API shape), but no instance is available
  in this dogfooding session; GitHub Cloud is what's actually being
  used right now.
- **Drop BBDC entirely, no trigger** — loses the recorded rationale and
  spike design for no bookkeeping benefit, since artifacts are never
  deleted regardless.

## Implications

ST-0020 and
SP-0004 move to
`deferred`/`backlog`, subscribed to new trigger `TRG-0010`. A new
current-release story
(ST-0031) and component stub
(CMP-0009) take BBDC's
former v1 slot. EP-0005,
ST-0003,
ST-0013,
CMP-0001, and
CMP-0004 each name
Bitbucket Data Center as the v1 target and go stale, cleared by
re-affirmation in this session.
ST-0028's
scope drops GitHub (no longer "additional") from its host list.
