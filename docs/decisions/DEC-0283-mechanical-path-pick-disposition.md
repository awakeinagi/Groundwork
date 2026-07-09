---
id: DEC-0283
type: decision
title: A mechanical path-pick closes the session with a recorded disposition; the fix rides the existing mechanical paths
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0052 @ T10-T11"
links:
  derives-from: [SES-0052]
  relates-to: [DEC-0253]
---

# DEC-0283: The mechanical path inside a session

## Context

When an intake conversation's path-pick lands on "mechanical fix"
(DEC-0253) *inside* an already-open session, what happens to the
session and the fix?

## Decision

The session closes recording the path-pick disposition — zero
decisions is valid, the same shape as idea-capture — and the fix
executes through the paths that already exist: a mechanical-fix PR or
typed operation, exactly as ST-0039 AC2 handles CP-sourced trivia.
DEC-0253's "no session needed for mechanical" still holds for fixes
that never enter a session; this covers only ones discovered
mid-conversation. No new contract — this is change-intake pack
stopping-criteria content.

## Rationale

Forbidding mechanical outcomes in sessions punishes users for asking
in the wrong door — the mechanical floor exists so trivia stays cheap.
Auto-converting to a CP adds a queue hop to something a typed
operation completes in seconds; DEC-0253 already rejected CP-per-typo
as ceremony without provenance value.

## Alternatives Considered

- **Forbid mechanical outcomes in sessions**: forces trivia through
  expedited-or-heavier.
- **Auto-convert to a CP**: rejected for live instruction at the
  paradigm level already.

## Implications

The change-intake pack's path-pick phase includes the mechanical
outcome with its stopping criterion; no story amendments.
