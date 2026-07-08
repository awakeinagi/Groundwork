---
id: SES-0017
type: session
title: v1 storage stack — embedded LadybugDB + DuckDB, deferral triggers
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [SP-0002, EP-0004, EP-0007, ST-0008, DEC-0061, DEC-0070,
               DEC-0078, DEC-0097]
---

# SES-0017: v1 Storage Stack — Embedded LadybugDB + DuckDB, Deferral Triggers

## Purpose

The participant directed a v1 stack change: defer Postgres + pgvector to
a future spike; the first version uses an embedded LadybugDB for the
graph and DuckDB for the app database and vector/semantic search.
Already settled going in: engine selection was assigned to a prototype
spike ([DEC-0061](../decisions/DEC-0061-engine-via-spike.md)) extended
with the search workload
([DEC-0070](../decisions/DEC-0070-extend-sp-0002-search-infra.md));
the change-event stream is a Postgres transactional outbox
([DEC-0078](../decisions/DEC-0078-postgres-outbox-events.md));
openCypher support is a hard requirement
([DEC-0062](../decisions/DEC-0062-tiered-query-api.md)); ops burden is a
first-class criterion
([DEC-0050](../decisions/DEC-0050-bitbucket-datacenter-v1.md)); deferred
status covers stories and epics only
([DEC-0097](../decisions/DEC-0097-deferred-status.md)).

## Transcript

**T1 — awakeinagi.** I want to defer the use of Postgres + pgvector to a
future spike. For the first version of the app, I will use an embedded
LadybugDB for the graph and DuckDB for the app database and
vector/semantic search.

**T2 — facilitator.** Presented the impact map:
[SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md)'s question
answered by decision rather than prototype (noting the skill's own graph
tool has been dogfooding embedded LadybugDB with openCypher over this
repository);
[DEC-0061](../decisions/DEC-0061-engine-via-spike.md)/[DEC-0070](../decisions/DEC-0070-extend-sp-0002-search-infra.md)
superseded, staling [EP-0004](../epics/EP-0004-graph-index.md) and
[EP-0007](../epics/EP-0007-consolidation-memory-layer.md);
[DEC-0078](../decisions/DEC-0078-postgres-outbox-events.md)'s host
database gone from v1, touching
[ST-0008](../stories/ST-0008-change-event-stream.md) (gated) and
[CMP-0001](../components/CMP-0001-artifact-store-service.md) (draft).
Flagged honestly: embedded engines make v1 single-process/single-writer
— an ops-burden win but it retires the multi-node criterion for v1.
Asked: the spike's fate (recommended archive + future spike on trigger),
outbox fate (recommended keep pattern, host in DuckDB), and what
triggers the future evaluation (recommended named need triggers).

**T3 — awakeinagi.** On [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md): re-scope it to the future evaluation
rather than archive — "and let's make a decision to also allow deferred
status (similar to stories) for spikes." Outbox: keep the pattern,
hosted in DuckDB, as recommended. Triggers: "Let's also add tracked
triggers to the system design. They will live in a tracked file. Let's
grill on the design details."

**T4 — facilitator.** Grilled the trigger design: registry form
(recommended a single `docs/TRIGGERS.md` with parseable `TRG-nnnn`
entries; alternatives full artifact type, per-artifact frontmatter),
entry schema (recommended condition / consequence / status / provenance,
plus fired date-and-links), firing semantics (recommended firing cites a
decision, one decision serving both firing and the consequence), and
surfacing (recommended status report + release-gate review + checker
validation).

**T5 — awakeinagi.** On registry form: "Keep the file easily parsable so
our skill can easily retrieve the trigger conditions and add them to an
agent's context (without using an excessive amount of tokens in the
context)." On schema: "And the skill should only pull active triggers
for the agent context." Accepted the recommendations on firing
semantics and surfacing.

**T6 — facilitator.** Played back seven decisions: the v1 stack
supersessions, the DuckDB-hosted outbox, deferred extended to spikes,
the spike re-scoped and deferred to backlog under four armed triggers, the
registry format (armed-only context loading), decision-cited
firing/retiring, and the surfacing rules — plus the ripple plan (epic
amendments + staleness, story re-pointing, spec/checker/tooling
updates).

**T7 — awakeinagi.** "Decisions confirmed."

## Decisions Produced

- [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md) — v1 storage
  stack: embedded LadybugDB (graph) + DuckDB (app database +
  vector/semantic search); supersedes prototype-spike selection
- [DEC-0103](../decisions/DEC-0103-outbox-in-app-database.md) — the
  change-event outbox pattern survives, hosted in the app database
- [DEC-0104](../decisions/DEC-0104-deferred-extends-to-spikes.md) —
  deferred status and release scoping extend to spikes
- [DEC-0105](../decisions/DEC-0105-sp-0002-rescoped-deferred.md) —
  `SP-0002` re-scoped to the Postgres + pgvector graduation evaluation,
  deferred to backlog under armed triggers
- [DEC-0106](../decisions/DEC-0106-trigger-registry.md) — the trigger
  registry: docs/TRIGGERS.md, parseable entries, armed-only context
  loading
- [DEC-0107](../decisions/DEC-0107-trigger-firing-cites-decision.md) —
  firing and retiring a trigger cite a decision
- [DEC-0108](../decisions/DEC-0108-trigger-surfacing.md) — armed
  triggers surface in the status report, at release-gate reviews, and
  under checker validation

## Conflicts Raised

None.
