---
id: IDEA-0026
type: idea
title: "Repair contract-item provenance defects found by SP-0013"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  SP-0013's executed findings surfaced several contract-item
  provenance defects in the approved CMPs: four items with no
  citation at the item level (KvStorePort.A-3,
  StalenessSweepService.A-1, CodeHostConnector.A-10, HostEvent.B-1);
  CMP-0001 and CMP-0004 disagreeing on the same contract-item
  family's size (A-1..A-10 vs A-1..A-8); Implements: lines using
  bare IDs rather than the resolvable-link form DEC-0092 mandates;
  and two provenance shapes the projection could not model at all --
  story-acceptance-criteria citations and implemented-protocol-item
  citations. Proposes repairing these defects and deciding a
  sanctioned representation for the two unmodeled provenance shapes.
links:
  derives-from: [SES-0064]
  relates-to: [SP-0013, DEC-0092, CMP-0001, CMP-0004]
---

## The Idea

Repair the contract-item provenance defects SP-0013's findings surfaced: the four items with no citation at the item level (KvStorePort.A-3, StalenessSweepService.A-1, CodeHostConnector.A-10, HostEvent.B-1); the CMP-0001/CMP-0004 disagreement on the same contract-item family's size (A-1..A-10 vs A-1..A-8); `Implements:` lines that use bare IDs rather than the resolvable-link form DEC-0092 mandates; and deciding the sanctioned representation for the two non-DEC provenance shapes the projection could not model -- story-acceptance-criteria citations (RestSurface.A-1..A-4 citing ST-0058 AC1/AC4) and implemented-protocol-item citations (GitHubConnector.A-2/A-3 citing CodeHostConnector.A-2/A-3).

## Spark Context

Raised at SES-0064 T21-T22 from SP-0013's executed findings (Provenance edge cases and Corpus ambiguities).

## Disposition

Pending.
