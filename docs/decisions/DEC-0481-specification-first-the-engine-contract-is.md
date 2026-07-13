---
id: DEC-0481
type: decision
title: "Specification-first: the Engine contract is normative; the deployed scripts are its provisional implementation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T4-T5"
overview: >-
  DEC-0346 and DEC-0422 leave the deployed gw scripts and their
  contracted description coexisting, and EP-0010 needed the
  authority direction between them. This decision commits EP-0010 to
  specification-first: the Engine contract is normative, the gw
  scripts are its provisional implementation, and discrepancies are
  bugs in the scripts, never in the contract.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0346, DEC-0422, DEC-0478]
---

# DEC-0481: Specification-first: the Engine contract is normative; the deployed scripts are its provisional implementation

## Context

DEC-0346 and DEC-0422 leave the deployed implementation and its contracted description coexisting; EP-0010 needed the direction of authority between them.

## Decision

EP-0010 proceeds specification-first. The Engine contract is the normative artifact, the existing gw scripts are its provisional implementation, and discrepancies between them are bugs in the scripts, never in the contract.

## Rationale

Implementation-first would promote incidental script behavior into contract, while specification-first keeps the two-descriptions coexistence resolvable at the native-rebuild moment.

## Alternatives Considered

Documenting the scripts' current behavior as the de facto contract was rejected as freezing accidents into obligations.

## Implications

Contract authoring may not simply transcribe script behavior; every contracted operation gets deliberately reviewed semantics.
