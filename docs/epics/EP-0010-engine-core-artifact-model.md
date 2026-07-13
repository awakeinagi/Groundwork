---
id: EP-0010
type: epic
title: "Engine Core & Artifact Model"
status: draft
owner: awakeinagi@gmail.com
created: 2026-07-13
overview: >-
  Engine Core & Artifact Model is the home of BG-0002's single-
  sourced-mechanics outcome and of the static artifact model, whose
  placement here DEC-0464 settled, including DEC-0080's hybrid CMP
  granularity (nested design elements with seam-element graduation)
  as part of that model. In scope: the Engine's paradigm mechanics
  (ID allocation, validation, gate state, integrity-checking
  machinery hosting all rule families including governance rules per
  DEC-0469, graph sync, format parsing, semantic search substrate);
  the static artifact model (types, schemas, frontmatter, link
  semantics, per DEC-0464); schema versioning, a migration
  mechanism, and backward compatibility for existing corpora as
  first-class scope, per DEC-0471. Out of scope: dynamic artifact
  lifecycle operations (EP-0009's domain per DEC-0445), agent and
  skill surfaces, extension points/schema registries/plugin
  contracts (a firm line per DEC-0470), and the Application
  (BG-0001). This epic is the foundation of the DEC-0462 sibling
  set: it impacts EP-0009 and all six sibling epics, each consuming
  the model and machinery it defines. Open risks: the Engine-
  authoritative versus skill-convention rule line, checker/graph
  performance at scale, the DEC-0346/DEC-0422 two-descriptions
  coexistence, and a port-ownership overlap with the BG-0001 track —
  DEC-0121 assigned the graph-store port to EP-0004 and the vector-
  store/embedding ports to EP-0007 while this epic claims graph sync
  and semantic search, unresolved until this epic's own refinement
  (BG-0001's own reframing is a deferred separate step per
  DEC-0441). Derives from BG-0002; draft status pending its own
  refinement session.
links:
  impacts: [EP-0009, EP-0011, EP-0012, EP-0013, EP-0014, EP-0015, EP-0016]
  derives-from: [BG-0002]
cites: [DEC-0462, DEC-0464, DEC-0469, DEC-0470, DEC-0471, DEC-0423, DEC-0441, DEC-0445, DEC-0346, DEC-0422, DEC-0080, DEC-0121]
---

# EP-0010: Engine Core & Artifact Model

## Summary

The home of BG-0002's outcome that all paradigm mechanics exist in
exactly one Groundwork Engine, and of the static artifact model whose
placement DEC-0464 settled here rather than as a separate topic. This
epic is the foundation of the DEC-0462 sibling set: every other epic
in the set consumes the model and machinery it defines.

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

## Interfaces & Contracts to Define

- The Engine API surface that agent/skill consumers call against (the
  EP-0010→EP-0011 impact edge).
- The static artifact-model schema contract: types, required
  frontmatter, link vocabulary, and the rules that validate them.
- The schema-versioning and migration-mechanism contract for existing
  corpora (DEC-0471).
- The rule-family hosting contract for governance rules running on
  this epic's checker machinery (DEC-0469; the EP-0010→EP-0014 impact
  edge: governance rules run as rule families on this epic's checker
  machinery).
- A runtime-agnostic Engine substrate contract that bounds what
  cross-runtime parity can promise (the EP-0010→EP-0012 impact edge).
- The Engine's compliance definition — the same definition adoption
  verifies a corpus against (the EP-0010→EP-0013 impact edge).
- The concurrency-safe write path and corpus invariants, which bound
  the collaboration model (the EP-0010→EP-0015 impact edge).
- The Engine-operation instrumentation points, the primary surface
  observability captures (the EP-0010→EP-0016 impact edge).

## Risks & Open Questions

- The Engine-authoritative vs. skill-convention rule line — which
  paradigm rules are mechanically enforced versus legitimately left
  as convention in the skills — is unsettled and is carried to this
  epic's own refinement as a decision to make there.
- Checker and graph performance at corpus scale is a candidate spike.
- The DEC-0346/DEC-0422 two-descriptions coexistence (the deployed
  implementation and its contracted description existing in parallel)
  carries into this epic until a native rebuild moment resolves it.
- A port-ownership overlap with the BG-0001 track: DEC-0121 assigned
  the graph-store port to EP-0004 and the vector-store/embedding
  ports to EP-0007 (both BG-0001), while this epic claims graph sync
  and the semantic-search substrate — an overlap nothing currently
  reconciles. Resolve at this epic's own refinement, noting BG-0001's
  own reframing is a deferred separate step (DEC-0441).

## Derived Work

None yet; this epic derives stories and spikes at its own refinement
session.
