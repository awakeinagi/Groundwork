---
id: DEC-0314
type: decision
title: Calling convention — CLI subcommands plus a JSON batch apply
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T8-T9"
overview: >-
  Agents invoke artifact-interact's typed operations through the Bash
  tool as CLI subcommands — one subcommand per operation for
  ergonomic single edits — plus an apply command accepting a JSON
  operation list for multi-operation transactions (e.g. close-session
  = append turns + set status + update overview, validated and
  applied as a unit). Long content payloads travel via stdin or
  --from-file, never shell-quoted arguments. Operations validate
  before touching disk and return a compact diff so the agent
  confirms the result without re-reading the file — directly serving
  the proposal's context-bloat goal. Chosen over subcommands-only (no
  transactional composition) and over JSON-operation-documents-only
  (uniform but clunky for small edits).
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0313, DEC-0316]
---

# DEC-0314: CLI Subcommands Plus JSON Batch Apply

## Context

The stakeholder asked how agents would call the typed operations
(SES-0057 T7); the facilitator laid out the subcommand pattern, the
JSON operation-document alternative, and their composition.

## Decision

The write API exposes one CLI subcommand per typed operation, plus
`apply` taking a JSON operation list for multi-operation
transactions. Payloads pass via stdin or `--from-file`. Every
operation validates before writing and returns a compact diff.

## Rationale

Subcommands are what an agent types naturally for a single edit; the
JSON batch gives transactional multi-step changes (validated as a
unit) without making every small edit pay document-assembly overhead.
Compact diffs close the loop without whole-file re-reads.

## Alternatives Considered

- **Subcommands only** — sequential multi-step changes lose
  transactional validation; rejected.
- **JSON operation documents only** — machine-checkable but clunky
  for one-line edits; rejected as the sole surface.

## Implications

The unified CLI (DEC-0316) hosts these as its write family. Batch
semantics (all-or-nothing) are defined in the DEC-0322 build.
