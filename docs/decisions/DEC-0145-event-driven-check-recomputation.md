---
id: DEC-0145
type: decision
title: Gate checks recompute on ChangeEvents and host webhooks, backstopped by a reconciliation sweep
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T4-T5"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0036, DEC-0038, DEC-0060, DEC-0128]
---

# DEC-0145: Event-Driven Check Recomputation

## Context

A `gate-policy` check that passed can silently become wrong while its
PR sits open — an ancestor goes stale, a conflict opens, a review
lands. The freshness contract of the service-computed checks
(DEC-0036) needed
definition.

## Decision

The gate engine subscribes to ChangeEvents
(CMP-0002) and host webhooks
(reviews, pushes, PR lifecycle) and re-posts affected checks on each
relevant event, idempotently under at-least-once delivery
(DEC-0060). A periodic
reconciliation sweep re-verifies every open PR's checks as the backstop
for missed events. Governance-change merges trigger the bulk variant
(DEC-0141).

## Rationale

Graph-side invalidation must reach idle PRs — that is precisely the
staleness-blocking case
(DEC-0038) — so
host-side triggers alone are insufficient. Events give freshness within
seconds; the sweep bounds the damage of any missed delivery.

## Alternatives Considered

- **PR events only**: an ancestor going stale never reaches an idle PR.
- **Compute at merge attempt**: correct at the only moment that
  technically matters, but check states lie in the host UI the whole
  time the PR is open.

## Implications

Check evaluation must be idempotent and cheap enough for bulk
recomputation; the sweep interval is deployment configuration.
Criteria land in ST-0014
and ST-0016.
