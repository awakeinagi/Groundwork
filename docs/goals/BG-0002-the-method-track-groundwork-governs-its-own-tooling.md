---
id: BG-0002
type: business-goal
title: The Method Track — Groundwork governs its own tooling
status: approved
approved-on: 2026-07-12
approved-by: awakeinagi
owner: awakeinagi@gmail.com
created: 2026-07-09
overview: >-
  The method track: every deployed execution surface of the
  Groundwork method — agents, skills with scripts, install
  machinery, hooks operating on Groundwork corpora — is documented,
  contracted, and gated by the same pipeline it implements. Born
  from the SES-0058 drift (a deployed agent holding tools nobody
  discussed) and the dropped dogfooding commitment (per DEC-0019).
  Outcomes: gated contracts for every method executable; no
  ungoverned capability (mechanically checked, DEC-0341); human
  gates before deployment; nothing ratified invisibly unbuilt
  (IDEA-0011's fix, DEC-0344); no build without the DEC-0335 intake.
  Admission predicate: can runtime behavior diverge from the record
  without anyone editing the record? Non-goals: product features,
  prose references, re-deciding ratified architecture. This track's
  delegation/contract pattern is permanent — BG-0001's application
  implements it natively, inheriting this track's contracts; only
  current implementations may later be rebuilt natively (per
  DEC-0346, narrowing DEC-0338's sacrificial framing). First derived
  work: the Artifact Interaction Surface epic (DEC-0339) carrying
  the DEC-0342 backfill. Status: approved.
links:
  relates-to: [SES-0059, BG-0001, DEC-0346]
cites: [DEC-0335, DEC-0336, DEC-0337, DEC-0338, DEC-0339, DEC-0340, DEC-0341, DEC-0342, DEC-0343, DEC-0344, DEC-0345, DEC-0324, DEC-0006, DEC-0011, DEC-0312, DEC-0263, DEC-0325, DEC-0019, DEC-0350, DEC-0351, DEC-0388]
---

# BG-0002: The Method Track — Groundwork Governs Its Own Tooling

## Problem

The Groundwork method's own executable tooling — agents, skills,
scripts that operate on the corpora it governs — was built outside the
rigor the method applies to everything else. SES-0058's deliverables
(the artifact-librarian agent, the artifact-interact skill) went from
one conversation to deployment with no requirements Story, no
contract, no gate; the deployed agent immediately held file-editing
tools nobody discussed (per DEC-0324, DEC-0343). Dogfooding was a
stated goal of this project (per DEC-0019), and the ball was dropped:
the method that exists to ground implementing agents did not ground
its own.

## Intent

Every deployed execution surface of the Groundwork method is
documented, contracted, and gated by the same pipeline it implements —
Stories state why it exists and when it is done; Component Docs state
what it does, what it touches, and how it is configured; humans
approve at every gate (per DEC-0006, DEC-0338). Why now: the drift
already happened once (per DEC-0343), and the guard rule that prevents
its recurrence (per DEC-0335) needs a track where the method's own
work can comply with it.

## Outcomes & Success Criteria

1. Every deployed method executable traces to a gated Component Doc
   whose contract lines cite decisions (per DEC-0338, DEC-0011).
2. No ungoverned capability: a deployed agent holding any tool,
   model, memory, or write path absent from its gated contract is a
   named gate failure, detected mechanically by the conformance check
   (per DEC-0340, DEC-0341).
3. Method tooling changes pass human gates before deployment; the
   breaking-change list in each contract states which changes re-gate
   (per DEC-0340).
4. Nothing ratified stays invisibly unbuilt: method obligations live
   in this tree and surface in the status report and frontier
   (per DEC-0344).
5. No method build enters implementation without the intake path —
   research survey, written design, approval (per DEC-0335,
   DEC-0337).

## Scope

**In:** deployed execution surfaces operating on Groundwork corpora —
agent definitions, skills with scripts, install machinery, hooks. The
admission test (per DEC-0338): can its runtime behavior diverge from
its record without anyone editing the record? The sizing yardstick for
all documentation in this track (per DEC-0336): the minimum
specification needed to reconcile a change against original intent.

**Out (non-goals):** product features (BG-0001's tree); pure-prose
process references, templates, and question banks (session- and
decision-governed — they are the record, per DEC-0336); re-deciding
architecture the record already settles (per DEC-0312's precedent).

**Releases:** current. First derived work: the Artifact Interaction
Surface epic (per DEC-0339) and, through it, the backfill of the
SES-0058 deliverables (per DEC-0342). A distribution/packaging epic is
anticipated but derives only at IDEA-0010's take-up (per DEC-0339).

## Constraints

- The no-arbitrary-builds guard (per DEC-0335) is this track's
  governing premise: nothing here is built without a presented,
  approved design; configuration is never mechanical.
- Grounding through contracts is first-class (per DEC-0336).
- Research precedes tooling decisions, sized to the decision (per
  DEC-0337).
- Every executable build's presented design includes its test plan;
  approval covers both (per DEC-0345).
- Writes and synthesis reads run through the artifact-librarian, while
  targeted bounded reads are chartered directly to every agent (per
  DEC-0388, which superseded DEC-0325); its own contract is this
  track's first deliverable (per DEC-0342).

## Stakeholders & Roles

Solo governance (per DEC-0263): the operator holds sponsor, approver,
and arbiter roles for this track, as for BG-0001.

## Conflicts & Tensions

- This track establishes a permanent design pattern — mandatory
  delegation through a governed subagent, corpus interaction
  restricted to a typed contract API, gate-enforced agent/tool
  contracts — that BG-0001's application is expected to implement
  natively, inheriting these already-gated contracts rather than
  re-deciding delegation and write-authority from scratch (per
  DEC-0346, narrowing DEC-0338). What remains provisional is narrower:
  today's specific implementation — a CLI script plus a
  Claude-Code-specific subagent — may later be rebuilt as a native
  application feature. Each component under this goal still carries an
  absorption clause, recorded as armed triggers in docs/TRIGGERS.md
  (per DEC-0338), but those triggers now describe when an
  *implementation* may be retired, never when the *pattern* is
  discontinued. Until an implementation is rebuilt, two descriptions
  of artifact handling coexist deliberately: this track documents
  today's working tooling; BG-0001 designs its native successor.
- Full standard gates on small tooling is a deliberate cost (ratified
  over lighter ceremony); the Scope predicate and the DEC-0336
  yardstick are the pressure valves that keep it proportionate.

## Derived Work

- EP-0009 (Artifact Interaction Surface, status draft), derived at
  SES-0065's take-up of IDEA-0015: carries DEC-0339's full charter
  (per DEC-0350) — the DEC-0342 backfill stories and the two
  Component Docs for the artifact-librarian and artifact-interact —
  plus guardrailed exploratory tooling spikes (DEC-0351). Pending
  gate approval.

