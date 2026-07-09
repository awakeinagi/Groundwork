---
id: DEC-0166
type: decision
title: CMP-0005 drafts and gates now; check-administration operations are marked provisional pending SP-0004
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  CMP-0005 is drafted in full and gated this session. The
  check-administration items (A-5, A-6) are explicitly marked
  provisional; shape may change once SP-0004 reports, at which point
  CMP-0005 either re-affirms unchanged or amends through a new session.
  The consumer-side shape is already fixed; only BBDC-side feasibility
  is unconfirmed.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T1"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0150, DEC-0142, DEC-0132]
---

# DEC-0166: CMP-0005 Drafts Now; Check-Administration Marked Provisional

## Context

ST-0019's
implementer notes instruct: do not harden the check-administration
operation family (required-check registration, check-run result
posting) before SP-0004's
findings land, since a failed assumption there could rework the
protocol shape itself
(DEC-0150).
SP-0004 is approved
but unexecuted. CMP-0001
and CMP-0004 both
carry forward-declared consumption of this contract
(DEC-0132,
DEC-0142),
so leaving CMP-0005
undrafted stalls both.

## Decision

CMP-0005 is
drafted in full — including the check-administration operation family —
and gated this session. The check-administration items
(`CodeHostConnector.A-5`, `A-6`) are explicitly marked **provisional**
in Implementation Guidance: their shape may change once
SP-0004 reports
findings, at which point CMP-0005
either re-affirms unchanged or amends through a new session — an
ordinary contract-change cycle, not a gate blocker today.

## Rationale

The consumer-side shape (what CMP-0001
and CMP-0004 need)
is already fixed by their forward declarations; only the BBDC-side
feasibility of the assumed semantics is unconfirmed. Marking the risk
explicitly, rather than leaving the whole component undrafted, matches
the precedent DEC-0132
set for exactly this kind of cross-epic sequencing risk.

## Alternatives Considered

- **Leave check-administration Pending, gate the rest** — keeps the doc
  honestly incomplete but leaves CMP-0001/CMP-0004's
  consumption unsatisfied longer for no offsetting benefit — the
  provisional-and-flagged approach carries the same risk information
  with a usable contract today.
- **Hold the whole session until SP-0004 executes** — stalls
  ST-0020 and
  ST-0021 on
  a 3-day spike with no scheduled instance/owner in this conversation;
  rejected as unnecessary serialization.

## Implications

`CodeHostConnector.A-5`/`A-6` and their Implementation Guidance entry
carry an explicit provisional flag; ST-0020's
own gate still waits on SP-0004
per DEC-0150 —
this decision only unblocks the protocol-level contract, not the BBDC
implementation.
