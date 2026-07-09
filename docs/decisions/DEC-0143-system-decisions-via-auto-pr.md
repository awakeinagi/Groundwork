---
id: DEC-0143
type: decision
title: System Decisions ride the auto-PR machinery with a template-conformance check
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Gate engine drafts each System Decision from fixed template citing the
  artifact's timeout election and configured default rule, routing it through
  existing auto-PR machinery: program-user approval gated by deterministic
  template-conformance check. No new write path; mechanical allowlist
  untouched. Reuses verified-fallback pattern already trusted for protected
  mains: machine verification replaces human approval where human could not
  meaningfully reject. PR history keeps every auto-resolution visible.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0025 @ T2-T3"
links:
  derives-from: [SES-0025]
  relates-to: [DEC-0039, DEC-0033]
---

# DEC-0143: System Decisions via Auto-PR

## Context

Timeout-to-default auto-resolutions must be recorded as Decisions
citing the election and the default rule
(DEC-0039) — but creating
a Decision artifact is design content, which the mechanical-write
allowlist deliberately cannot express
(DEC-0033).

## Decision

The gate engine drafts each System Decision from a fixed template —
citing the artifact's timeout election and the configured default
rule — and routes it through the existing
DEC-0033 auto-PR machinery:
program-user approval gated by a deterministic template-conformance
check. No new write path; the mechanical allowlist is untouched.

## Rationale

Reuses the verified-fallback pattern already trusted for protected
mains: machine verification replaces human approval precisely where a
human could not meaningfully reject (the election already authorized
the outcome). PR history keeps every auto-resolution visible.

## Alternatives Considered

- **New `create-system-decision` mechanical operation**: cheapest at
  runtime, but the first mechanical op creating an artifact with
  decision semantics — a precedent that weakens the allowlist's
  never-design-content line.
- **Arbiter countersigns each record**: keeps humans in the loop but
  reintroduces the non-decision backlog the election exists to avoid.

## Implications

The template-conformance check joins the validator family the gate
engine provisions
(DEC-0142);
"System Decision" enters the glossary; criteria land in
ST-0015.
