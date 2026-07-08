---
id: DEC-0166
type: decision
title: CMP-0005 drafts and gates now; check-administration operations are marked provisional pending SP-0004
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0030 @ T1"
links:
  derives-from: [SES-0030]
  relates-to: [DEC-0150, DEC-0142, DEC-0132]
---

# DEC-0166: [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md) Drafts Now; Check-Administration Marked Provisional

## Context

[ST-0019](../stories/ST-0019-code-host-connector-protocol.md)'s
implementer notes instruct: do not harden the check-administration
operation family (required-check registration, check-run result
posting) before [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)'s
findings land, since a failed assumption there could rework the
protocol shape itself
([DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md)).
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) is approved
but unexecuted. [CMP-0001](../components/CMP-0001-artifact-store-service.md)
and [CMP-0004](../components/CMP-0004-governance-gate-engine.md) both
carry forward-declared consumption of this contract
([DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
[DEC-0142](../decisions/DEC-0142-gate-engine-owns-check-registration.md)),
so leaving [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
undrafted stalls both.

## Decision

[CMP-0005](../components/CMP-0005-code-host-connector-protocol.md) is
drafted in full — including the check-administration operation family —
and gated this session. The check-administration items
(`CodeHostConnector.A-5`, `A-6`) are explicitly marked **provisional**
in Implementation Guidance: their shape may change once
[SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) reports
findings, at which point [CMP-0005](../components/CMP-0005-code-host-connector-protocol.md)
either re-affirms unchanged or amends through a new session — an
ordinary contract-change cycle, not a gate blocker today.

## Rationale

The consumer-side shape (what [CMP-0001](../components/CMP-0001-artifact-store-service.md)
and [CMP-0004](../components/CMP-0004-governance-gate-engine.md) need)
is already fixed by their forward declarations; only the BBDC-side
feasibility of the assumed semantics is unconfirmed. Marking the risk
explicitly, rather than leaving the whole component undrafted, matches
the precedent [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)
set for exactly this kind of cross-epic sequencing risk.

## Alternatives Considered

- **Leave check-administration Pending, gate the rest** — keeps the doc
  honestly incomplete but leaves [CMP-0001](../components/CMP-0001-artifact-store-service.md)/[CMP-0004](../components/CMP-0004-governance-gate-engine.md)'s
  consumption unsatisfied longer for no offsetting benefit — the
  provisional-and-flagged approach carries the same risk information
  with a usable contract today.
- **Hold the whole session until [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md) executes** — stalls
  [ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md) and
  [ST-0021](../stories/ST-0021-delegated-reviews-and-attribution.md) on
  a 3-day spike with no scheduled instance/owner in this conversation;
  rejected as unnecessary serialization.

## Implications

`CodeHostConnector.A-5`/`A-6` and their Implementation Guidance entry
carry an explicit provisional flag; [ST-0020](../stories/ST-0020-bitbucket-data-center-connector.md)'s
own gate still waits on [SP-0004](../spikes/SP-0004-bbdc-required-check-surface.md)
per [DEC-0150](../decisions/DEC-0150-sp-0004-bbdc-check-surface-spike.md) —
this decision only unblocks the protocol-level contract, not the BBDC
implementation.
