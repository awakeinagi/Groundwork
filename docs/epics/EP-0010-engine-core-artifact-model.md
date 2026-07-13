---
id: EP-0010
type: epic
title: "Engine Core & Artifact Model"
status: approved
approved-on: 2026-07-13
approved-by: awakeinagi@gmail.com
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Engine Core & Artifact Model is EP-0010's charge for BG-0002's
  single- sourced-mechanics outcome and the static artifact model,
  whose placement here DEC-0464 settled, including DEC-0080's hybrid
  CMP granularity. Refinement session SES-0091 settled this epic's
  contract shapes. The Engine API surface is the transport-
  independent kernel operation catalog with the gw CLI as reference
  adapter (DEC-0478), carrying first-class structured diagnostics
  (DEC-0479) and versioned by compatible extension with tolerant
  readers until the first non-CLI consumer (DEC-0480). The artifact
  model owns both the type roster and the type machinery (DEC-0482);
  schema versioning is a corpus-level SemVer marker with whole-
  corpus atomic migrations (DEC-0483). Rule hosting stays Engine-
  owned with declarative policy configuration, substrate-neutral
  pending ActiveGraph consolidation (DEC-0484), bounded by the
  write-time/check-time enforcement line: only self-trust invariants
  enforce at write time (DEC-0475). The kernel is pure, all I/O
  crosses port contracts (DEC-0477); this epic now owns the port
  contract definitions with embedded zero-hosting default adapters,
  resolving the DEC-0121 overlap and carrying forward DEC-0135's
  protocol-type-component graduation pattern under the new ownership
  (DEC-0476). Concurrency is settled at the single-session level
  (DEC-0485); the two-descriptions coexistence is now governed
  specification-first (DEC-0481). Deferred to component docs and
  stories: per-type schema detail, port specifics, instrumentation,
  and the compliance definition's exact shape (DEC-0486); multi-
  session concurrency defers to SP-0018. Two spikes are
  commissioned: SP-0019 (schema-migration mechanism) and SP-0020
  (checker/graph performance calibration), per DEC-0487. Why also
  fixes quality-goal priority: correctness, performance, migration
  safety, then compatibility (DEC-0475, DEC-0487, DEC-0483,
  DEC-0480, DEC-0477). Status: in- refinement, heading to gate.
links:
  impacts: [EP-0009, EP-0011, EP-0012, EP-0013, EP-0014, EP-0015, EP-0016]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0464, DEC-0469, DEC-0470, DEC-0471, DEC-0423, DEC-0441, DEC-0445, DEC-0346, DEC-0422, DEC-0080, DEC-0121, DEC-0135, DEC-0475, DEC-0476, DEC-0477, DEC-0478, DEC-0479, DEC-0480, DEC-0481, DEC-0482, DEC-0483, DEC-0484, DEC-0485, DEC-0486, DEC-0487]
---

# EP-0010: Engine Core & Artifact Model

## Summary

The home of BG-0002's outcome that all paradigm mechanics exist in
exactly one Groundwork Engine, and of the static artifact model whose
placement DEC-0464 settled here rather than as a separate topic. This
epic is the foundation of the DEC-0462 sibling set: every other epic
in the set consumes the model and machinery it defines. Refinement
session SES-0091 settled the epic's contract shapes; the dispositions
below record them.

## Why (Goal Alignment)

BG-0002's first outcome is single-sourced paradigm mechanics with no
surface reimplementing paradigm logic (DEC-0423, DEC-0441). This epic
is where that single source lives: ID allocation, validation, gate
state, integrity checking, graph sync, format parsing, and semantic
search substrate all belong to one Engine, not to whichever surface
happens to touch an artifact. DEC-0464 additionally settled the
static artifact model (types, schemas, frontmatter, link semantics)
as part of this same epic rather than a standalone topic, since the
model and the machinery that enforces it are inseparable design
concerns.

Quality goals, in priority order: (1) Correctness and corpus
integrity — the Engine never persists a corpus its own operations
cannot trust (DEC-0475, DEC-0485). (2) Performance at interactive
tolerance — full-check and write-path latency bounded by the
fitness-function threshold SP-0020 calibrates (DEC-0487). (3)
Migration safety — whole-corpus atomic migrations, no mixed-version
states (DEC-0483). (4) Compatibility and portability — compatible-
extension API evolution and a runtime-agnostic kernel behind ports
(DEC-0480, DEC-0477).

## Scope

**In:**
- The Engine's paradigm mechanics: ID allocation, validation, gate
  state, integrity-checking machinery — hosting ALL rule families,
  including governance rules, per DEC-0469 — graph sync, format
  parsing, and the semantic-search substrate.
- The static artifact model: types, schemas, frontmatter, and link
  semantics, per DEC-0464, including DEC-0080's hybrid CMP granularity
  (nested design elements with seam-element graduation) as part of
  the artifact model this epic owns.
- Schema versioning, a migration mechanism, and backward compatibility
  for existing corpora, as first-class scope, per DEC-0471.
- The Engine's port contract definitions — graph store, vector store,
  embedding provider, corpus filesystem — with embedded zero-hosting
  default adapters; consuming surfaces may diverge on adapter
  implementation but never on feature support, per DEC-0476.
- The write-time/check-time enforcement boundary: the Engine enforces
  at write time only its self-trust invariants, with all other rules
  running as check-time rule families, per DEC-0475.

**Out:**
- Dynamic artifact lifecycle operations — EP-0009's domain, per
  DEC-0445 (the EP-0010→EP-0009 impact edge: EP-0009 operates on the
  model and machinery this epic defines).
- Agent and skill surfaces — the sibling epic for that concern (the
  EP-0010→EP-0011 impact edge: agent/skill surfaces are thin consumers
  of the Engine API).
- Extension points, schema registries, and plugin contracts — a firm
  line drawn by DEC-0470, re-openable only by a session that
  supersedes it.
- The Application (BG-0001, per DEC-0441).

## Domain Context

Bounded context: **Groundwork Engine — core mechanics & artifact
model** (per DEC-0462, DEC-0464). This epic is the Engine-proper
context that every consuming surface (agents, skills, runtimes,
adoption tooling, collaboration, governance, observability) sits atop.
This session crystallized the terms Engine Kernel, Kernel Operation
Catalog, Corpus Schema Marker, and Structured Diagnostics, defined in
CONTEXT.md.

## Interfaces & Contracts to Define

- **Engine API surface** — decided: the normative contract is the
  transport-independent kernel operation catalog with the gw CLI as
  reference driving adapter (DEC-0478); structured diagnostics are
  first-class in every operation contract (DEC-0479); the API evolves
  by compatible extension with tolerant readers until the first
  non-CLI consumer, and foreign corpora pin schema versions (DEC-0480).
  Operation-level detail lands in component docs. This is the Engine
  API surface that agent/skill consumers call against (the
  EP-0010→EP-0011 impact edge).
- **Static artifact-model schema contract** — decided at the shape
  level: EP-0010 owns both the artifact-type roster and the type
  machinery (DEC-0482); per-type schema details defer to stories and
  component docs (DEC-0486). EP-0009 operates on the model and
  machinery this epic defines (the EP-0010→EP-0009 impact edge).
- **Schema-versioning and migration** — decided at the shape level: a
  corpus-level SemVer marker with whole-corpus atomic migrations
  (DEC-0483); the mechanism is deferred to spike SP-0019 (DEC-0487).
- **Rule-family hosting** — decided: Engine-owned rule code with
  declarative policy configuration, substrate-neutral pending the
  ActiveGraph consolidation (DEC-0484), bounded by the DEC-0475
  enforcement line and hosting all rule families, including governance,
  per DEC-0469 (the EP-0010→EP-0014 impact edge: governance rules run
  as rule families on this epic's checker machinery).
- **Runtime-agnostic substrate** — decided: the kernel is pure, all I/O
  crosses port contracts (DEC-0477); this epic owns the port contract
  definitions with embedded zero-hosting default adapters, resolving
  the DEC-0121 port-ownership overlap between EP-0004/EP-0007's store
  ports and this epic's graph-sync and search claims (DEC-0476);
  DEC-0135's graduation pattern — infrastructure ports arriving as
  standalone protocol-type components — carries over under this
  ownership change: the ports this epic owns are expected to land as
  protocol-type components in its own decomposition, DEC-0135's
  original premise that EP-0004/EP-0007 would derive them being
  narrowed by DEC-0476 accordingly. Port interface specifics defer to
  component docs (DEC-0486). This bounds what cross-runtime parity can
  promise (the EP-0010→EP-0012 impact edge).
- **Compliance definition** — deferred: it emerges from this epic's
  stories and is due before EP-0013's stories begin (DEC-0486). This
  is the same definition adoption verifies a corpus against (the
  EP-0010→EP-0013 impact edge).
- **Concurrency-safe write path** — decided at the single-session
  level: the verified invariants (per-artifact if-match conflict
  detection, refusal rather than merge, atomic recoverable batches)
  are the contracted model (DEC-0485); multi-session semantics are
  deferred to SP-0018's findings. This bounds the collaboration model
  (the EP-0010→EP-0015 impact edge).
- **Instrumentation points** — deferred to component docs (DEC-0486).
  These are the primary surface observability captures (the
  EP-0010→EP-0016 impact edge).

## Risks & Open Questions

- The DEC-0346/DEC-0422 two-descriptions coexistence (the deployed
  implementation and its contracted description existing in parallel)
  persists until a native rebuild moment; it is now governed
  specification-first per DEC-0481 — the contract is normative, the
  deployed scripts are provisional, and discrepancies are script bugs.
- Multi-session concurrency semantics await SP-0018's findings
  (DEC-0485).
- The schema-migration mechanism awaits SP-0019 (DEC-0487); checker
  and graph performance calibration awaits SP-0020.

## Derived Work

SP-0019 (the schema-migration mechanism under the corpus-level SemVer
marker) and SP-0020 (checker and graph performance calibration across
corpus scales) — both drafted ahead in this epic's gate bundle at
SES-0091 and ratified by this epic's approval, per DEC-0487.

