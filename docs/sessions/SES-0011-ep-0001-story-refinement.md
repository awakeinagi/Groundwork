---
id: SES-0011
type: session
title: EP-0001 story refinement — counter durability, event transport, dev connector
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-06
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Fable 5 (claude-fable-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [ST-0003, ST-0005, ST-0008, EP-0001]
---

# SES-0011: [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) Story Refinement

## Purpose

Refine the drafted [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) story set ([ST-0001](../stories/ST-0001-tier1-schema-suite.md)–[ST-0008](../stories/ST-0008-change-event-stream.md),
[CMP-0001](../components/CMP-0001-artifact-store-service.md) stub) to
gate-readiness — the first story-level refinement of the project. Three
stories carried flagged open design points; the rest derived fully from
accepted decisions.

## Transcript

**T1 — Sponsor.** "Let's continue" — proceed with the agreed next step
([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) stories).

**T2 — Agent.** Drafted [ST-0001](../stories/ST-0001-tier1-schema-suite.md)–[ST-0008](../stories/ST-0008-change-event-stream.md) with DEC-cited acceptance
criteria, sibling dependency and impact edges, and the [CMP-0001](../components/CMP-0001-artifact-store-service.md) draft
stub. Opened refinement on the three open points: (a) ID counter
durability for [ST-0005](../stories/ST-0005-id-allocation.md) (recommended rescan-on-boot); (b) event-stream
transport for [ST-0008](../stories/ST-0008-change-event-stream.md) (recommended transactional outbox in Postgres);
(c) development-time code-host strategy for [ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md) (recommended a
local-git fake connector implementing the full contract).

**T3 — Sponsor.** All three as recommended.

**T4 — Agent (synthesis).** Distilled [DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md)–[DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md), folded them into
[ST-0005](../stories/ST-0005-id-allocation.md)/[ST-0008](../stories/ST-0008-change-event-stream.md)/[ST-0003](../stories/ST-0003-item-branch-pr-orchestration.md), and moved the eight stories to `gated` for
sponsor sign-off.

## Decisions Produced

[DEC-0077](../decisions/DEC-0077-id-rescan-on-boot.md),
[DEC-0078](../decisions/DEC-0078-postgres-outbox-events.md),
[DEC-0079](../decisions/DEC-0079-local-git-fake-connector.md)

## Conflicts Raised

None.
