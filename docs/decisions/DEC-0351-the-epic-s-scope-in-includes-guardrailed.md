---
id: DEC-0351
type: decision
title: "The epic's Scope-In includes guardrailed exploratory tooling spikes"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-10
decided-by: awakeinagi
decided-on: 2026-07-10
source-span: "SES-0065 @ T9-T10"
overview: >-
  SES-0065's grilling (T9-T10) confirmed the Artifact Interaction
  Surface epic's Scope-In includes exploratory spikes evaluating
  candidate interaction-surface tooling, under guardrails: spike
  outputs are strictly throwaway and are never themselves deployed
  as part of the surface; adoption of anything a spike surfaces
  happens only through the ordinary path -- a DEC-0337 option survey
  followed by DEC-0335 design intake -- never by a spike's findings
  alone authorizing deployment. This gives the currently-open
  SES-0064 activegraph spike program a scoped home under EP-0009
  while keeping BG-0002's no-ungoverned-capability admission
  predicate intact.
links:
  derives-from: [SES-0065]
  relates-to: [DEC-0337, DEC-0335]
---

## Context

Grilling round 1 (T9) asked whether EP-0009 should accommodate
exploratory spikes evaluating candidate tooling for the interaction
surface (e.g. the SES-0064 activegraph spike program's eventual
consumer), given DEC-0335's no-arbitrary-builds guard and DEC-0337's
option-survey requirement.

## Decision

The epic's Scope-In includes guardrailed exploratory tooling spikes:
spikes may evaluate candidate interaction-surface tooling, but their
outputs are strictly throwaway and are never themselves deployed as
part of the surface. Any tooling a spike surfaces as promising only
moves toward adoption through the ordinary path — a DEC-0337 option
survey followed by DEC-0335 design intake — never by a spike's
findings alone authorizing deployment.

## Rationale

Exploratory evaluation work needs a scope home, and this epic is the
natural one; the guardrail keeps that home from becoming a side door
around DEC-0335's approved-design floor or DEC-0337's option-survey
requirement — a spike stays evaluative, not self-authorizing.

## Alternatives Considered

- **Exclude spikes from this epic entirely, house them elsewhere** —
  rejected; there is no other natural epic home for interaction-
  surface tooling evaluation, and excluding it would strand the
  already-open SES-0064 spike program.
- **Allow spike outputs to be adopted directly on stakeholder sign-off
  without the survey/intake path** — rejected; bypasses DEC-0337 and
  DEC-0335, reopening exactly the ungoverned-capability risk BG-0002
  exists to close.

## Implications

EP-0009's Scope In section names this guardrail explicitly. Spike
artifacts (SP-*) derived under this epic must be gated with adoption
routed through DEC-0337/DEC-0335, never treated as pre-approved
builds.
