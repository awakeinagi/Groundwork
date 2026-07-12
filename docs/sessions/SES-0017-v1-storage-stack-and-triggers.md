---
id: SES-0017
type: session
title: v1 storage stack — embedded LadybugDB + DuckDB, deferral triggers
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Directed v1 storage stack change: embedded LadybugDB for graph, DuckDB
  for app database and vector/semantic search; deferred Postgres +
  pgvector to future spike. Superseded prototype-spike selections.
  DuckDB-hosted transactional outbox pattern retained. Re-scoped SP-0002
  to future evaluation under four armed triggers. Extended deferred
  status to spikes. Established trigger registry in docs/TRIGGERS.md with
  parseable TRG-nnnn entries; skill context loading filters armed-only
  triggers. Firing/retiring cites decisions. Seven decisions produced.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [SP-0002, EP-0004, EP-0007, ST-0008, DEC-0061, DEC-0070, DEC-0078, DEC-0097, DEC-0102, DEC-0103, DEC-0104, DEC-0105, DEC-0106, DEC-0107, DEC-0108]
---

# SES-0017: v1 Storage Stack — Embedded LadybugDB + DuckDB, Deferral Triggers

## Purpose

The participant directed a v1 stack change: defer Postgres + pgvector to
a future spike; the first version uses an embedded LadybugDB for the
graph and DuckDB for the app database and vector/semantic search.
Already settled going in: engine selection was assigned to a prototype
spike (DEC-0061) extended
with the search workload
(DEC-0070);
the change-event stream is a Postgres transactional outbox
(DEC-0078);
openCypher support is a hard requirement
(DEC-0062); ops burden is a
first-class criterion
(DEC-0050); deferred
status covers stories and epics only
(DEC-0097).

## Transcript

**T1 — awakeinagi.** I want to defer the use of Postgres + pgvector to a
future spike. For the first version of the app, I will use an embedded
LadybugDB for the graph and DuckDB for the app database and
vector/semantic search.

**T2 — facilitator.** Presented the impact map:
SP-0002's question
answered by decision rather than prototype (noting the skill's own graph
tool has been dogfooding embedded LadybugDB with openCypher over this
repository);
DEC-0061/DEC-0070
superseded, staling EP-0004 and
EP-0007;
DEC-0078's host
database gone from v1, touching
ST-0008 (gated) and
CMP-0001 (draft).
Flagged honestly: embedded engines make v1 single-process/single-writer
— an ops-burden win but it retires the multi-node criterion for v1.
Asked: the spike's fate (recommended archive + future spike on trigger),
outbox fate (recommended keep pattern, host in DuckDB), and what
triggers the future evaluation (recommended named need triggers).

**T3 — awakeinagi.** On SP-0002: re-scope it to the future evaluation
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

- DEC-0102 — v1 storage
  stack: embedded LadybugDB (graph) + DuckDB (app database +
  vector/semantic search); supersedes prototype-spike selection
- DEC-0103 — the
  change-event outbox pattern survives, hosted in the app database
- DEC-0104 —
  deferred status and release scoping extend to spikes
- DEC-0105 —
  `SP-0002` re-scoped to the Postgres + pgvector graduation evaluation,
  deferred to backlog under armed triggers
- DEC-0106 — the trigger
  registry: docs/TRIGGERS.md, parseable entries, armed-only context
  loading
- DEC-0107 —
  firing and retiring a trigger cite a decision
- DEC-0108 — armed
  triggers surface in the status report, at release-gate reviews, and
  under checker validation

## Conflicts Raised

None.
