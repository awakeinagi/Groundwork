---
id: DEC-0478
type: decision
title: "The kernel operation catalog is the Engine's normative API contract; the gw CLI is its reference adapter"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T6-T9"
overview: >-
  The Engine's contract needed a normative locus: kernel operations
  or the deployed CLI. This decision makes the transport-independent
  kernel operation catalog — typed inputs/outputs with enumerated
  errors per operation — the normative API contract, with the gw CLI
  as its reference driving adapter mapped one-to-one onto the
  catalog; conformance is judged against the catalog, never the
  CLI's textual surface.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0423, DEC-0477, DEC-0479, DEC-0481]
---

# DEC-0478: The kernel operation catalog is the Engine's normative API contract; the gw CLI is its reference adapter

## Context

The Engine's contract needed a normative locus: the kernel operation level or the deployed CLI surface.

## Decision

The Engine's normative API contract is a transport-independent kernel operation catalog: typed inputs and outputs with enumerated errors for every operation. The gw CLI is the reference driving adapter, mapped one-to-one onto the catalog, and conformance of any adapter is judged against the catalog, never against the CLI's textual surface.

## Rationale

The specification-first posture requires the contract to be normative over the provisional scripts, and a single catalog gives EP-0012 parity a checkable meaning while letting future consumers bind without a contract rewrite.

## Alternatives Considered

Making the CLI surface the contract is nearly free today but promotes incidental flags and output text into normative contract and forces future consumers to subprocess-wrap the CLI.

## Implications

EP-0011 skills and EP-0013 adoption tooling program against catalog semantics; drift between catalog and scripts is a script bug; a conformance suite becomes a natural component-level deliverable.
