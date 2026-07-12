---
id: IDEA-0037
type: idea
title: "Complete error contracts for six happy-path-only services"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-11
proposed-by: awakeinagi@gmail.com
overview: >-
  Add failure/error contract language to the A/B items of the six
  services SP-0014 found specifying only success paths:
  BranchOrchestrator and WorktreeManager (CMP-0001), GovernanceInit
  and StalenessSweepService (CMP-0004), EmailNotifier (CMP-0008),
  SessionSseEndpoint (CMP-0011). A contract that only describes
  success is half a contract.
links:
  derives-from: [SES-0069]
---

# IDEA-0037: Complete error contracts for six happy-path-only services

## The Idea

Add failure/error contract language to the A/B items of the six services SP-0014 found specifying only success paths: BranchOrchestrator and WorktreeManager (CMP-0001), GovernanceInit and StalenessSweepService (CMP-0004), EmailNotifier (CMP-0008), SessionSseEndpoint (CMP-0011). A contract that only describes success is half a contract.

## Spark Context

SP-0014 findings disposition, SES-0069 (rule R24).

## Disposition

Pending.

