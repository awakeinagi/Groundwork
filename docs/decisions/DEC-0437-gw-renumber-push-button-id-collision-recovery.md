---
id: DEC-0437
type: decision
title: "gw renumber: push-button ID-collision recovery scoped to unmerged branch content"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0082 @ T33-T34, T37"
overview: >-
  gw renumber recovers from multi-user ID collisions after a rebase:
  it detects branch-minted IDs colliding with main, reserves fresh
  IDs via the DEC-0430 reservation mechanism, rewrites every in-
  branch reference (frontmatter, links, prose, the unpublished
  session transcript), and re-runs the checker. It never modifies
  anything already on main, so it violates no immutability
  invariant, analogous to rebasing unpushed commits. Confirmed by
  the stakeholder at SES-0082 T37; mechanics land with SP-0018.
links:
  derives-from: [SES-0082]
  relates-to: [DEC-0430, SP-0018]
---

# DEC-0437: gw renumber: push-button ID-collision recovery scoped to unmerged branch content

## Context

Reservation-at-mint (DEC-0430) prevents ID collisions in the common case, but a multi-user, skills-only workflow can still produce a collision: another writer's branch merges first, minting IDs that a still-open branch also used. The stakeholder asked for a push-button way to recover from that collision.

## Decision

The gw tooling provides a renumber operation for the multi-user collision case in which another writer's work landed first: after a rebase surfaces ID collisions, it detects the branch-minted IDs that now collide with main, reserves fresh IDs through the normal DEC-0430 reservation mechanism, rewrites every reference within the branch's own unmerged diff — frontmatter, links, prose bare-ID mentions, and the branch's not-yet-published session transcript — and re-runs the checker.

## Rationale

The hard rule is that renumber never modifies anything already on main: it is recovery for unpublished work only, which is why it violates no immutability invariant, analogous to rebasing unpushed commits. It is the recovery complement to DEC-0430's prevention-by-reservation.

## Alternatives Considered

Promotion-time reconciliation across all branches was considered and rejected (consistent with DEC-0430's own rejection of that approach as anything but a documented offline fallback): it risks touching already-merged content and does not compose with git's own conflict resolution model.

## Implications

Mechanics land with SP-0018's coordination design. Renumber must be exercised only against a branch's own working tree before merge; any tooling that could reach main content is out of scope by this decision's hard rule.
