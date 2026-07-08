---
id: CMP-0010
type: component
title: Composition Root
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
context: platform
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0003, CMP-0012, CMP-0013, CMP-0014]
cites: [DEC-0001, DEC-0102, DEC-0121, DEC-0122, DEC-0124, DEC-0132, DEC-0133,
        DEC-0152, DEC-0201, DEC-0203, DEC-0204, DEC-0205, DEC-0206, DEC-0208,
        DEC-0222, DEC-0226, DEC-0227, DEC-0228, DEC-0232]
---

# CMP-0010: Composition Root

## Purpose

The single place where all six infrastructure Port contracts (app
database, vector store, embedding, graph store, Queue, KV-store) are
bound to concrete Adapters at process startup, from a structured YAML
deployment config file
([DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)) — so
every consumer rides a config-swappable seam instead of a hard-wired
engine reference
([ST-0057](../stories/ST-0057-composition-root.md),
[DEC-0201](../decisions/DEC-0201-composition-root-split.md)). It produces
a typed application container and injects each bound Port into consumers
by constructor
([DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)),
and owns the deterministic process startup/shutdown ordering
([DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md)).

## Ubiquitous Language

Port, Adapter, Composition Root — per
[CONTEXT.md](../../CONTEXT.md). Component-local structural term:
**Application Container** (the typed value the Composition Root builds,
holding one Port-typed reference per Port plus the constructed
top-level services — the concrete form of "everything programs against
Port contracts only").

## Design Elements

### DeploymentConfig (value)

Implements: [ST-0057](../stories/ST-0057-composition-root.md)

- `DeploymentConfig.D-1` — schema: a top-level YAML map with one entry
  per Port (`app-database`, `vector-store`, `embedding`, `graph-store`,
  `queue`, `kv-store`), each entry `{ adapter: <name>, settings: { … } }`.
  The `{adapter, settings}` shape is **uniform across all six Ports**,
  kept even where only one Adapter is valid in v1 — that uniformity is
  what keeps a future swap a config-only change (per
  [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md),
  [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md),
  [DEC-0203](../decisions/DEC-0203-queue-kv-ports-added.md)).
- `DeploymentConfig.D-2` — the config file path is resolved from a
  single environment variable with a documented default path, and the
  file is parsed once at process startup (per
  [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md)).
- `DeploymentConfig.D-3` — environment variables may override only a
  **closed, documented set** of values: the master secret-decryption
  key (per
  [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md))
  plus an enumerated set of per-deployment path/endpoint values. Adapter
  *selection* is never sourced from an environment variable, and a
  variable outside the enumerated set is not honored as an override (per
  [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md),
  [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)).
- `DeploymentConfig.D-4` — immutable after load; equality by value (per
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)).

### ApplicationContainer (value)

Implements: [ST-0057](../stories/ST-0057-composition-root.md)

- `ApplicationContainer.D-1` — schema: exactly one bound instance per
  Port (the six), plus references to the constructed top-level services.
  Every Port field is typed to the **Port contract, never to a concrete
  Adapter type** — the container's shape does not change when the bound
  Adapter changes (per
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md),
  [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
- `ApplicationContainer.D-2` — immutable after build; consumers hold
  only the Port-typed references injected into their constructors — never
  the container as an ambient global (per
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)).

### CompositionRoot (service)

Implements: [ST-0057](../stories/ST-0057-composition-root.md)

- `CompositionRoot.A-1` — `build_container(config: DeploymentConfig) →
  ApplicationContainer`. Binds each of the six Ports to the Adapter
  named in `config`, constructs the top-level services with those Ports
  injected by constructor, and returns the typed container (per
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md),
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md)).
- `CompositionRoot.A-2` — `startup()` / `shutdown()`: the deterministic
  process lifecycle. `startup()` runs **open engine resources → bind
  Adapters → build container services → `JobRuntime.start()` → ready**;
  `shutdown()` runs the reverse — **stop claiming new jobs → drain
  in-flight work (grace period) → close engine resources**. Invoked by
  [CMP-0011](CMP-0011-inbound-api.md)'s ASGI lifespan (forward-declared
  per
  [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md)),
  and available to any non-HTTP entrypoint (per
  [DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md),
  [DEC-0208](../decisions/DEC-0208-queue-port-runtime-split.md)).
- `CompositionRoot.B-1` — for the four pre-existing Ports, binds the
  already-decided v1 Adapters: LadybugDB (graph store), DuckDB (app
  database and vector store), and the local-model or REST-client
  embedding Adapter selected by a config field (per
  [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
  [DEC-0124](../decisions/DEC-0124-v1-adapter-set.md)).
- `CompositionRoot.B-2` — for Queue and KV-store, binds each Port's
  single v1 default Adapter — the DB-backed durable queue table
  ([CMP-0012](CMP-0012-queue-port.md)) and the app-database-reuse KV
  table ([CMP-0014](CMP-0014-kv-store-port.md)); no other Adapter is
  selectable through v1 config (per
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
- `CompositionRoot.B-3` — fail-fast validation: an unknown Adapter name,
  a missing required field, or an unknown/extra config key aborts
  process startup with a clear, actionable error — never a silent
  fallback to a default Adapter (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
  [ST-0057](../stories/ST-0057-composition-root.md) AC5).
- `CompositionRoot.B-4` — swap discipline: swapping the Adapter bound to
  any Port is a config change plus (if needed) a new Adapter
  implementation — never a change to consumer code, since consumers
  reference only Port contracts (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
  [DEC-0121](../decisions/DEC-0121-infrastructure-ports.md)).
- `CompositionRoot.B-5` — environment overrides layer on top of the file
  for the enumerated set only (`DeploymentConfig.D-3`); Adapter
  selection is never driven by an environment variable alone (per
  [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md),
  [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)).
- `CompositionRoot.B-6` — sole binder: exactly one Composition Root
  exists per process and it is the only holder of Adapter-selection
  knowledge; no other component knows or asks which Adapter is bound to
  a Port (per
  [DEC-0201](../decisions/DEC-0201-composition-root-split.md),
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)).

## Component Invariants

- `C-1` — every consumer receives its Ports by constructor injection
  from the container; no global or ambient binding registry exists (per
  [DEC-0226](../decisions/DEC-0226-composition-root-typed-container-constructor-injection.md)).
- `C-2` — no Port is ever bound except through config: there is no
  compiled-in default Adapter and no silent fallback on bad config (per
  [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
  [ST-0057](../stories/ST-0057-composition-root.md) AC5).
- `C-3` — startup and shutdown always run the one deterministic
  ordering; a failure partway through `startup()` tears down the
  resources already opened rather than leaving them dangling (per
  [DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md)).

## Implementation Guidance

### Constraints

- `IG-1` — config format is YAML; its path is resolved from a single
  environment variable with a documented default (per
  [DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md),
  [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md)).
- `IG-2` — v1 is single-process / single-writer; the Root binds embedded
  Adapters only. External/graduated Adapters are deferred behind
  `TRG-0001`/`TRG-0002` (per
  [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md),
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md),
  [DEC-0205](../decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md)).
- `IG-3` — the master secret-decryption key is read from the environment,
  never from the YAML; connector/service secrets themselves stay
  envelope-encrypted in the app database, not in config (per
  [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md),
  [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md)).

### Notes

- The exact environment-variable names and the default config path are
  implementation choices within the `DeploymentConfig.D-2`/`D-3` rule —
  the contract fixes the *shape* (one path var + a closed override set),
  not the spellings.
- The uniform per-Port `{adapter, settings}` shape is retained even for
  Ports with a single valid v1 Adapter precisely so a future swap stays
  config-only ([ST-0057](../stories/ST-0057-composition-root.md) Notes).

## Dependencies

- [CMP-0003](CMP-0003-app-database-port.md) — the App Database Port
  contract the Root binds the DuckDB Adapter against; consumed as the
  Port surface for binding, not any Adapter internal.
- [CMP-0012](CMP-0012-queue-port.md) — the Queue Port contract; the Root
  binds its v1 durable Adapter (per
  [DEC-0204](../decisions/DEC-0204-v1-default-adapters-deferred-alternates.md)).
- [CMP-0014](CMP-0014-kv-store-port.md) — the KV-store Port contract; the
  Root binds its v1 app-database-reuse Adapter.
- [CMP-0013](CMP-0013-background-job-execution-runtime.md) — consumed:
  `JobRuntime.A-2` (`start()`/`stop()`), wired during
  `startup()`/`shutdown()`; the Root only starts and stops the runtime,
  it does not register handlers (see Out of Scope).
- Forward-declared (per
  [DEC-0132](../decisions/DEC-0132-connector-consumption-forward-declared.md),
  for the Port contracts not yet drafted as standalone components): the
  graph-store, vector-store, and embedding Port contracts owned by
  [EP-0004](../epics/EP-0004-graph-index.md)/[EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md),
  bound to their already-decided v1 Adapters per
  [DEC-0102](../decisions/DEC-0102-v1-embedded-stack.md)/[DEC-0124](../decisions/DEC-0124-v1-adapter-set.md).

## Acceptance & Test Expectations

1. Full binding: a valid YAML config binds all six Ports to their v1
   Adapters and `build_container` returns a container whose fields are
   Port-typed (per
   [ST-0057](../stories/ST-0057-composition-root.md) AC1/AC3/AC4).
2. Fail-fast: an unknown Adapter name, a missing required field, and an
   unknown extra key each abort startup with an actionable error and no
   Adapter bound — never a silent default (per
   [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
   [ST-0057](../stories/ST-0057-composition-root.md) AC5).
3. Swap conformance: changing the embedding Adapter field (the one
   genuine v1 choice) rebinds it with no change to any consumer's code
   (per [DEC-0122](../decisions/DEC-0122-config-selected-adapters.md),
   [ST-0057](../stories/ST-0057-composition-root.md) AC6).
4. Env precedence: an enumerated override variable layers on top of the
   file, while a value driving Adapter selection is refused — selection
   stays in the YAML (per
   [DEC-0228](../decisions/DEC-0228-composition-root-config-path-and-enumerated-overrides.md),
   [ST-0057](../stories/ST-0057-composition-root.md) AC2).
5. Lifecycle ordering: `startup()` opens resources and starts the
   `JobRuntime` in order and `shutdown()` drains then closes in reverse;
   a fault injected mid-`startup()` tears down already-opened resources
   (per
   [DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md)).

## Out of Scope

Boundary statements (per
[DEC-0133](../decisions/DEC-0133-out-of-scope-differentiated-rule.md)):

- The Port *contracts* themselves — owned by
  [EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md)/[EP-0004](../epics/EP-0004-graph-index.md)/[EP-0007](../epics/EP-0007-consolidation-memory-layer.md)
  and [CMP-0003](CMP-0003-app-database-port.md)/[CMP-0012](CMP-0012-queue-port.md)/[CMP-0014](CMP-0014-kv-store-port.md);
  this component only wires them (per
  [DEC-0201](../decisions/DEC-0201-composition-root-split.md)).
- Concrete Adapter *implementations* — each owned by its Port's
  story/component; the Root selects and binds, it does not implement
  Adapters.
- Job-handler registration — owned by
  [CMP-0013](CMP-0013-background-job-execution-runtime.md)'s `JobRuntime`;
  producers register their handlers directly and no central registry of
  job-types is maintained by the Composition Root. The Root only
  `start()`s/`stop()`s the runtime during its lifecycle sequence (per
  [DEC-0222](../decisions/DEC-0222-runtime-owns-handler-registration.md)).
- The ASGI application and the HTTP/SSE surface —
  [CMP-0011](CMP-0011-inbound-api.md); its lifespan invokes
  `startup()`/`shutdown()`, but the API surface is not defined here (per
  [DEC-0227](../decisions/DEC-0227-composition-root-owns-startup-shutdown-ordering.md)).
- External/graduated Adapters (Postgres/pgvector, AWS SQS, external
  KV-store) — deferred behind `TRG-0001`/`TRG-0002` and evaluated by
  [SP-0002](../spikes/SP-0002-postgres-pgvector-graduation.md),
  [SP-0009](../spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md),
  [SP-0010](../spikes/SP-0010-external-kv-store-adapter-evaluation.md)
  (per
  [DEC-0205](../decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md)).
- Secret storage and envelope-encryption mechanics — the Root loads the
  master key from the environment and hands it to the Secret Store
  ([CMP-0015](CMP-0015-secret-store.md), graduated per
  [DEC-0232](../decisions/DEC-0232-graduate-secret-store.md); flow per
  [ST-0022](../stories/ST-0022-identity-auth-and-person-resolution.md));
  the encryption itself lives there, not here (per
  [DEC-0152](../decisions/DEC-0152-secrets-encrypted-in-app-database.md)).
