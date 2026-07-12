---
id: DEC-0429
type: decision
title: "Governance declares an enforcement level and projects one-way into host configuration"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-12
source-span: "SES-0082 T14, T18, T19, T20, T21, T31"
accepted-in: SES-0082
overview: >-
  Governance configuration carries an enforcement level — solo (bare
  git, agent discipline plus checker, the honored baseline), basic
  (PRs plus required CI), full (projected branch protection).
  Projection is one-way: the governance YAML is source, host config
  is derived, never hand-maintained in parallel. Projection tooling
  is built at first multi-user team need; the checker warns on
  capability mismatches.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0263, DEC-0326, DEC-0036, DEC-0172, DEC-0315]
---

# DEC-0429: Governance declares an enforcement level and projects one-way into host configuration

## Context

DEC-I established that enforcement is host-projected but paradigm-recorded. SES-0082 still needed a concrete mechanism for declaring how strictly a given deployment enforces approval, ranging from a bare solo repository to a fully protected team host.

## Decision

The governance configuration carries an enforcement level: solo (bare git; agent discipline plus the checker — the honored baseline, not a failure mode), basic (pull requests and required continuous integration), and full (governance projected into host branch protection). Projection is one-way: the governance YAML is the source and host configuration is derived; the two are never hand-maintained in parallel. Projection tooling is built when the first multi-user team needs it. The checker warns when policy demands enforcement the declared host capability cannot provide.

## Rationale

Naming solo as an honored baseline (not a degraded fallback) matters: it is today's real, correct operating mode for this project and for any single-maintainer adopter, and treating it as a failure state would misrepresent the paradigm's actual usage. One-way projection avoids the classic drift failure of hand-maintained parallel configs — the governance file and the host's actual protection rules silently diverging. Deferring projection tooling until it's actually needed follows the same discipline as DEC-D's engine-extraction trigger.

## Alternatives Considered

Treating solo mode as merely "enforcement level zero" pending eventual upgrade was rejected — it does not reflect this project's own status or the paradigm's design intent. Building projection tooling immediately, ahead of any multi-user team, was rejected as speculative work with no current consumer.

## Implications

A governance YAML schema needs an enforcement-level field (solo/basic/full) if it doesn't already carry one. Projection tooling is chartered only once a real multi-user team adopts the paradigm, not before. The checker gains a warning path for enforcement/host-capability mismatches.
