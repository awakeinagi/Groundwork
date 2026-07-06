---
id: ST-0005
type: story
title: ID allocation — service lock, durability, multi-node behavior
status: draft
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002]
  impacted-by: [ST-0002]
cites: [DEC-0009, DEC-0031]
---

# ST-0005: ID Allocation

## Summary

The allocator behind every artifact ID: sequential per prefix, never
reused, correct under concurrency — including creations on unmerged item
branches — durable across restarts, and specified for multi-node
deployment.

## Acceptance Criteria

1. IDs are allocated sequentially per prefix and never reused, including
   for artifacts later deleted or abandoned on unmerged branches
   (per DEC-0009).
2. Concurrent creation requests never mint duplicate IDs; allocation is
   serialized by a thread/process-safe lock in the service (per DEC-0031).
3. Allocation accounts for artifacts existing only on unmerged item
   branches — a fresh scan of all refs yields no ID collisions
   (per DEC-0031).
4. Counter state survives service restart without manual intervention;
   the durability mechanism is settled in this story's refinement
   (per DEC-0031 implications).
5. Multi-node behavior is explicitly specified: either single-allocator
   deployment is a documented constraint, or a distributed lock is
   provided (per DEC-0031 implications).

## Component Impact

[CMP-0001](../components/CMP-0001-artifact-store-service.md) — supplies
the ID-allocation sections of its Behavior and Data Contracts.

## Out of Scope

ID formats and prefixes themselves (fixed by SPEC-artifact-common).

## Notes for Implementers

Durability approach (rescan-on-boot vs. allocation log vs. service DB) is
an open refinement point for this story's session.
