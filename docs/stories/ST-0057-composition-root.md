---
id: ST-0057
type: story
title: Composition Root — config-driven Port/Adapter binding
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [ST-0010, ST-0060, ST-0062]
  impacts: [ST-0058, ST-0059]
  impacted-by: [ST-0060, ST-0062]
cites: [DEC-0001, DEC-0121, DEC-0122, DEC-0102, DEC-0124, DEC-0152, DEC-0201,
        DEC-0203, DEC-0204, DEC-0206, DEC-0209]
---

# ST-0057: Composition Root — Config-Driven Port/Adapter Binding

## Summary

The single place where all six infrastructure Port contracts are bound
to concrete Adapters at process startup, from a structured deployment
config file — so every other story in this epic, and every engine
epic's Port, rides one config-swappable seam instead of hard-wired
engine references
([DEC-0201](../decisions/DEC-0201-composition-root-split.md)).

## Acceptance Criteria

1. A single YAML deployment-config file names the Adapter bound to each
   of the six Ports (app database, vector store, embedding, graph
   store, Queue, KV-store) at process startup
   (per [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md),
   [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
   [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)).
2. Environment variables layer on top of the file for environment-
   specific overrides and the master secret-decryption key only —
   never for connector/service secrets themselves, which stay
   envelope-encrypted in the app database per the established pattern
   ([DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)).
   Adapter *selection* is never driven by an environment variable
   alone
   (per [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)).
3. For the four pre-existing Ports, the Composition Root binds the
   already-decided v1 Adapters: embedded LadybugDB (graph store),
   DuckDB (app database, vector search), and the local-model or
   REST-client embedding adapter, selected by a config field
   (per [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
   [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
4. For Queue and KV-store, the Composition Root binds each Port's v1
   default Adapter — the durable DB-backed queue table
   ([ST-0060](ST-0060-queue-port.md)) and the app-database-reuse KV
   table ([ST-0062](ST-0062-kv-store-port.md)); no other Adapter is
   selectable through v1 config
   (per [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
5. An invalid or missing config value (unknown Adapter name, missing
   required field) fails process startup with a clear, actionable
   error — never a silent fallback to a default Adapter
   (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
6. Swapping an Adapter for any Port is a config change plus (if needed)
   a new Adapter implementation — never a change to consumer code
   (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
   [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed
once the first story here refines toward it.

## Out of Scope

- Port *contracts* themselves — owned by
  [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)/[EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
  ([DEC-0201](../decisions/DEC-0201-composition-root-split.md)); this
  story only wires them.
- External/graduated adapters — deferred behind
  [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md),
  [SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md),
  [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md).
- The deferred ephemeral Queue adapter and dedicated KV-store library
  adapter ([ST-0063](ST-0063-ephemeral-in-memory-queue-adapter.md),
  [ST-0064](ST-0064-dedicated-embedded-kv-library-adapter.md)) — config
  support for selecting them arrives if/when they're built.

## Notes for Implementers

The config schema's per-Port shape (adapter name + adapter-specific
settings block) should stay uniform across all six Ports even though
today only the embedding Port has a genuine v1 choice — that
uniformity is what keeps a future Adapter swap a config-only change.
