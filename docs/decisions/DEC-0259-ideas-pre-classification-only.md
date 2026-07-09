---
id: DEC-0259
type: decision
title: Ideas are pre-classification capture only — intent whose artifact level is already clear uses the existing deferral path
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T14-T15"
links:
  derives-from: [SES-0050]
---

# DEC-0259: The Idea / deferred-work boundary

## Context

The method already captures mid-session nice-to-haves as deferred
stories/spikes with `release:` labels and trigger subscriptions. Where
does the new Idea type (DEC-0258) end and that mechanism begin?

## Decision

An Idea captures intent **too raw to classify** — it is not yet known
whether it is goal-, epic-, story-, spike-, or component-shaped. The
moment intent's artifact level is clear (e.g., an obviously
story-shaped nice-to-have inside the epic being refined), it is
captured directly as a deferred ST/SP exactly as today. Ideas never
carry `release:` labels or trigger subscriptions; taking an Idea up
converts it, through an intake session, into artifacts that do.

## Rationale

The deferral mechanism's value is that deferred items are *classified,
linked work* — they hold a place in the tree and revive into it. An
Idea holds no place in the tree yet. Keeping the boundary at
classification preserves the thirty-second deferral path untouched and
gives the rawer capture form its own cheap home.

## Alternatives Considered

- **All new intent starts as an Idea**: uniform entry point, but adds
  a hop to the currently-instant deferral path and would touch settled
  deferral decisions for no gain.
- **Coexist by agent judgment**: leaves ambiguous exactly the boundary
  this session existed to eliminate.

## Implications

Playbook wording: "know its level → deferred ST/SP; don't → Idea."
The checker's release/deferral rules never apply to Ideas.
