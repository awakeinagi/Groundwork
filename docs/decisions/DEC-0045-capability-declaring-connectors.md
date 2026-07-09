---
id: DEC-0045
type: decision
title: Connectors declare capability manifests; the gate compiler adapts
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-06
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-06
source-span: "SES-0005 @ T2-T3"
links:
  derives-from: [SES-0005]
---

# DEC-0045: Capability-declaring connector contracts

## Context

Bitbucket and GitHub differ in review semantics, required-check APIs, and
team models; the gate engine (EP-0003) must stay host-agnostic
(DEC-0036).

## Decision

The code-host contract defines its operations plus a capability manifest
each connector declares (`required-checks`, `team-sync`,
`review-dismissal`, …). A documented minimum capability set is required to
host Groundwork at all; above the minimum, the gate engine's policy
compiler adapts — emulating missing host features via the `gate-policy`
check where possible.

## Rationale

New hosts become new connectors plus manifests, never core changes —
the pluggable-boundary constraint of BG-0001 applied to variance, without
sacrificing richer hosts' features to the lowest common denominator.

## Alternatives Considered

- **Lowest common denominator**: discards e.g. richer protection rules.
- **Host-specific logic in core**: every new host touches core.

## Implications

The minimum capability set is part of the connector spec (CMP-level); the
v1 baseline is set by Bitbucket Data Center
(DEC-0050).
