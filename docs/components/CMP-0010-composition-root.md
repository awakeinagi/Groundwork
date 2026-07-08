---
id: CMP-0010
type: component
title: Composition Root
status: draft
owner: eng-lead
created: 2026-07-08
context: platform
links:
  derives-from: [EP-0008]
  satisfies: [BG-0001]
  depends-on: [CMP-0012, CMP-0014]
---

# CMP-0010: Composition Root

## Purpose

The single place where all six infrastructure Port contracts (app
database, vector store, embedding, graph store, Queue, KV-store) are
bound to concrete Adapters at process startup, from a structured YAML
deployment config file
([DEC-0206](../decisions/DEC-0206-composition-root-yaml-config.md)) —
so every consumer rides a config-swappable seam instead of a hard-wired
engine reference
([ST-0057](../stories/ST-0057-composition-root.md)).

## Pending — Ubiquitous Language

## Pending — Design Elements

Element decomposition follows [ST-0057](../stories/ST-0057-composition-root.md)
refinement: the config schema shape, the binding/startup service, and
the fail-fast validation behavior.

## Pending — Component Invariants

## Pending — Implementation Guidance

## Pending — Dependencies

Consumes [CMP-0012](CMP-0012-queue-port.md) (Queue Port) and
[CMP-0014](CMP-0014-kv-store-port.md) (KV-store Port) contracts to bind
their v1 default Adapters; exact consumed sections declared at contract
time.

## Pending — Acceptance & Test Expectations

## Pending — Out of Scope
