---
id: DEC-0469
type: decision
title: "One checker, Engine-hosted"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0089 @ T6, T7"
overview: >-
  Self-Governance requires no ungoverned capability, mechanically
  checked (DEC-0442), while Engine Core owns the integrity checker;
  both system-architect consultation instances flagged this boundary
  as the sharpest open question of the epic derivation. The
  stakeholder settled it: there is one checker, hosted by the
  Engine, with governance rules implemented as checker rule families
  inside the Engine's checking machinery. The Self-Governance &
  Dogfooding epic defines which rules exist and their policy; Engine
  Core owns the machinery that runs all rule families. This avoids a
  second enforcement surface that would drift against the first, in
  line with outcome 1's single-sourcing principle, and unblocks both
  charters rather than deferring the boundary to their refinement
  sessions.
links:
  derives-from: [SES-0089]
  relates-to: [DEC-0442, DEC-0462]
---

# DEC-0469: One checker, Engine-hosted

## Context

Self-Governance requires no ungoverned capability, mechanically checked
(DEC-0442), while Engine Core owns the integrity checker; both
consultation instances flagged this boundary as the sharpest open
question of the derivation.

## Decision

There is one checker, hosted by the Engine: governance rules are
checker rule families inside the Engine's checking machinery. The
Self-Governance & Dogfooding epic defines which rules exist and their
policy; Engine Core owns the machinery that runs all rule families.

## Rationale

Outcome 1's single-sourcing — a second enforcement surface would drift
against the first.

## Alternatives Considered

A separate governance verifier consuming Engine data (second
enforcement surface, drift risk); deferring the boundary to epic
refinement (declined — settling it now unblocks both charters).

## Implications

The governance epic contributes rule definitions and policies as
contracts over Engine-hosted machinery.
