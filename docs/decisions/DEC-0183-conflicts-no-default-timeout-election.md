---
id: DEC-0183
type: decision
title: Escalated Conflicts do not default into the general artifact timeout-to-default election
status: accepted
owner: ds-lead
created: 2026-07-08
overview: >-
  Decides that escalated Conflicts do not default into DEC-0039's
  timeout-to-default election mechanism. An owner can still opt in
  explicitly, but no CFL artifact auto-resolves on a clock by default.
  Preserves mediation-driven conflict resolution.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0033 @ T9-T10"
links:
  derives-from: [SES-0033]
  relates-to: [DEC-0039]
  supersedes: []
---

# DEC-0183: Escalated Conflicts Do Not Default into the General Artifact Timeout-to-Default Election

## Context

The decision-recall audit on
ST-0036
noted that DEC-0039's
per-artifact timeout-to-default election is generally available but
left unaddressed for `CFL-` artifacts specifically: should an escalated
Conflict be able to auto-resolve on a clock, or must it always wait for
a ratified Decision?

## Decision

Escalated Conflicts do not default into
DEC-0039's
timeout-to-default election. The general election mechanism remains
available — an artifact owner can still elect a `CFL-` into it per its
standard opt-in path — but no `CFL-` auto-resolves on a clock by
default.

## Rationale

A Conflict is exactly the case the non-timeout default behavior of
DEC-0039 fits: a real
disagreement between people, not a routine artifact whose staleness can
safely auto-resolve. Defaulting conflicts into a clock would let a
contested design decision get made by inaction rather than by the
resolution the mediation/escalation flow
(DEC-0005) is
built to produce.

## Alternatives Considered

- **CFLs default into timeout-to-default**: avoids conflicts stalling
  work indefinitely, but requires defining a generic "default rule" for
  an arbitrary disagreement — there's no safe universal default for
  contested intent, unlike the routine-staleness case
  DEC-0039 was originally
  built for.

## Implications

ST-0036
records this as the resolution of its
DEC-0039 contract gap; no
new acceptance criterion needed since the behavior is "do nothing
extra" — `CFL-` artifacts simply don't opt in by default.
