---
id: DEC-0164
type: decision
title: GatePolicyCheck evaluates live on every call, with no cached CompiledPolicy
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0029 @ T5-T6"
links:
  derives-from: [SES-0029]
  relates-to: [DEC-0131, DEC-0141, DEC-0145, DEC-0162]
---

# DEC-0164: GatePolicyCheck — Live Evaluation, No Cache

## Context

[ST-0014](../stories/ST-0014-gate-policy-check.md)'s `gate-policy`
check evaluates domain-conditional approvers,
role verification, committee quorum, staleness, and attribution on
every relevant event and reconciliation sweep pass
([DEC-0145](DEC-0145-event-driven-check-recomputation.md)). Whether the
evaluator reads `governance/*.yaml` and PR facts fresh each call, or
consults a persisted `CompiledPolicy` snapshot refreshed on governance
ChangeEvents, was undecided.

## Decision

`GatePolicyCheck.evaluate(pr-ref)` reads `governance/*.yaml` at the PR's
target-branch ref, PR review state (via the code-host connector),
staleness state (via `StorageService`/Graph Index), and open-conflict
state, fresh on every call. No `CompiledPolicy` value element exists;
nothing about policy evaluation is persisted between calls.

## Rationale

Keeps [CMP-0004](../components/CMP-0004-governance-gate-engine.md) inside
[DEC-0131](DEC-0131-rebuild-sufficiency-invariant.md)'s discipline
without adding a second place policy state can go stale, and stays
trivially coherent with
[DEC-0141](DEC-0141-midflight-policy-recompute.md)'s mid-flight
recomputation: a governance-change merge simply triggers the same
live-read evaluation on every open PR, rather than requiring a cache
invalidation step that could itself lag or duplicate.

## Alternatives Considered

A cached `CompiledPolicy` value, refreshed on governance ChangeEvents —
rejected: it would speed reads at the cost of a rebuild-sufficiency
surface and a second state machine (cache freshness) to keep correct
under [DEC-0145](DEC-0145-event-driven-check-recomputation.md)'s
at-least-once delivery, for a performance gain not shown to be
necessary at v1's embedded, single-process scale
([DEC-0102](DEC-0102-v1-embedded-stack.md)).

## Implications

`GatePolicyCheck` carries no data-contract (`D`) obligations of its own
beyond what it reads through existing dependencies; if evaluation
latency becomes a real problem at scale, introducing a cache is a
superseding decision, not a silent optimization.
