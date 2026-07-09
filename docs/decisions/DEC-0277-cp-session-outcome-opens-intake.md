---
id: DEC-0277
type: decision
title: CP triage's session outcome opens an intake-opened session carrying the CP verbatim
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T6-T7, T8-T9"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0047, DEC-0073]
---

# DEC-0277: CP triage routes into intake

## Context

ST-0039 AC2 says substantive changes "trigger a refinement session
with the CP as input" — written before intake existed. Left as-is, the
CP pipeline would remain a second front door with the intake protocol
optional for CP-sourced change.

## Decision

The triage `session` outcome opens an **intake-opened** session whose
intake context carries the CP verbatim as the proposal (`origin: cp`):
T1 is the CP's captured text, and the restate-and-align loop runs
against the proposer or their stand-in. ST-0039 AC2 and
SPEC-change-proposal's lifecycle are amended to say so. The deferred
release-2 triage views story (ST-0055) inherits the shape now, as one
indicative acceptance criterion plus an impact edge from ST-0039 —
cheap while it cannot gate, so revival re-refines against the right
shape instead of rediscovering intake.

## Rationale

One route for all change intent is the point of the intake protocol
(DEC-0255 at the paradigm level). Leaving a known-wrong indicative
contract in a deferred story invites the release-2 planner to inherit
it.

## Alternatives Considered

- **Leave ST-0039 as-is**: "session with the CP as input" arguably
  covers it — but only arguably, which is the ambiguity.
- **A dedicated routing story**: amendment-sized change; a story would
  be ceremony.
- **Revive ST-0055 now**: re-opens DEC-0073's settled v1 surface seam
  for nothing this change needs early.

## Implications

ST-0039 AC2 amended; ST-0055 gains an indicative AC and an
`impacted-by: ST-0039` edge; SPEC-change-proposal's `session` triage
description names the intake opening.
