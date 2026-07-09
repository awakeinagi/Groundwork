---
id: ST-0005
type: story
title: ID allocation — service lock, durability, multi-node behavior
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-07
owner: eng-lead
created: 2026-07-06
links:
  derives-from: [EP-0001]
  satisfies: [BG-0001]
  depends-on: [ST-0002]
  impacted-by: [ST-0002]
cites: [DEC-0009, DEC-0031, DEC-0077]
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
4. Counter state survives service restart via rescan-on-boot: startup
   scans all refs for the max existing ID per prefix; no persistent
   counter store exists anywhere (per DEC-0077).
5. Single-allocator deployment is a documented constraint of the service
   (per DEC-0077).

## Component Impact

CMP-0001 — supplies
the ID-allocation sections of its Behavior and Data Contracts.

## Out of Scope

ID formats and prefixes themselves (fixed by SPEC-artifact-common).

## Notes for Implementers

The boot scan must cover every ref, not just main — unmerged item branches
hold allocated IDs (per DEC-0077).
