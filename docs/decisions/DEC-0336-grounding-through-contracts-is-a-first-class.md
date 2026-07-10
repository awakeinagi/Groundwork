---
id: DEC-0336
type: decision
title: Grounding through contracts is a first-class Groundwork priority
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0059 @ T12-T14"
overview: >-
  Alongside provenance, Groundwork commits to grounding through
  contracts: everything living in a project carries a written
  statement of what it does, what it touches, and how it is
  configured — before it exists — wherever possible. Pure-prose
  process material stays governed by sessions and decision records.
  The sizing yardstick is the stakeholder's formulation: what is the
  minimum specification/design documentation needed to reconcile
  this change against the original intent? Motivated by SES-0058's
  drift: intent was specified, configuration was not, and
  unspecified configuration is where drift lives. Stated next to
  provenance in the AGENTS.md asset; first mechanical instantiation
  is the DEC-0340 agent-contract profile.
links:
  derives-from: [SES-0059]
  relates-to: [DEC-0335, DEC-0015]
---

# DEC-0336: Grounding Through Contracts — a First-Class Priority

## Context

Groundwork's named first-class commitment was provenance (every claim
traces to a decision). SES-0058 showed a second commitment was
implicit and unenforced: the librarian's behaviors were decided but
its configuration was never written down, so its implementation
drifted with no document to diff against. Stakeholder at T12:
Groundwork is supposed to "work" on "ground"ing the agents handling
implementation.

## Decision

Grounding through contracts becomes a first-class Groundwork priority
alongside provenance: everything that lives in a Groundwork project
carries a written statement of what it does, what it touches, and how
it is configured — before it exists — wherever possible. Pure-prose
process material (references, templates, question banks) remains
sufficiently governed by sessions and decision records; it is the
record. The sizing yardstick is the stakeholder's T14 formulation:
*"what is the minimum amount of specification/design documentation
that I will need to reconcile this change against the original
intent?"* — every change answers that question, and that minimum is
what gets written.

## Rationale

Unspecified configuration is where drift lives: intent was specified
in SES-0058, configuration was not, and the drift arrived exactly
there. A first-class priority is read by agents before acting; a
gate-only rule fires after the work exists.

## Alternatives Considered

- **Tooling-only scope** — leaves future non-tooling residents
  uncovered; the priority states the principle, DEC-0335's floor and
  DEC-0338's predicate handle proportionality; rejected.
- **Gate-level enforcement only** — catches too late; rejected at T13.

## Implications

Stated in the AGENTS.md asset next to provenance. The reconciliation
yardstick becomes the test facilitators apply at intake when sizing
design documentation (DEC-0335) and research (DEC-0337). The
agent-contract profile (DEC-0340) is its first mechanical
instantiation.
