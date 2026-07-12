---
id: DEC-0312
type: decision
title: The artifact-interact write API is the sole sanctioned write path for agents
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0057 @ T8-T9"
overview: >-
  Once artifact-interact ships, agents mutate corpus artifacts only
  through its typed write operations; freehand Edit/Write on docs/
  artifact files becomes a process violation. This dogfoods the
  product's own write-authority architecture into the method tooling:
  DEC-0029 (all writes via the storage API, no exceptions) and
  DEC-0033 (mechanical writes are typed service operations, never
  arbitrary diffs). Guardrails move from agent discipline to
  mechanical enforcement: the scripts validate before touching disk,
  refuse invariant-violating operations with errors naming the
  sanctioned alternative (e.g. editing an accepted DEC directs to
  supersede), and perform bookkeeping (ID allocation, reciprocity,
  approval stamping) atomically. Chosen over a guardrailed-but-
  optional API and over a validate-only lint approach. The honesty of
  the sole-path stance is backed by the full-lifecycle operation
  surface (DEC-0313).
links:
  derives-from: [SES-0057]
  relates-to: [DEC-0029, DEC-0033, DEC-0310, DEC-0313, DEC-0377]
---

# DEC-0312: The Write API Is the Sole Sanctioned Write Path

## Context

Today artifact writes are freehand Edit/Write calls whose correctness
rests entirely on the agent following prose rules (immutability,
transition legality, same-edit overview refresh, ID allocation). The
new skill could make its write API advisory or mandatory.

## Decision

The artifact-interact write API is the sole sanctioned write path:
agents perform artifact mutations only through its typed operations;
freehand editing of `docs/` artifact files is a process violation
once the skill ships.

## Rationale

Mirrors the ratified product architecture (DEC-0029, DEC-0033): one
write authority preserves every invariant the corpus exists to keep.
Mechanical enforcement replaces discipline — the class of drift the
integrity machinery keeps catching after the fact gets prevented at
write time instead.

## Alternatives Considered

- **Guardrailed but optional** — guardrails only protect writes that
  opt in; rejected.
- **Validate-only lint after freehand edits** — catches violations
  after the fact instead of preventing them; rejected.
- **Sole path with a raw-edit escape hatch** — considered for
  operation-set gaps; rejected in favor of full lifecycle coverage
  (DEC-0313).

## Implications

The design-session process references and installed AGENTS.md must
re-state their write instructions in terms of typed operations at the
DEC-0320 cutover. Operations must exist for everything sessions
actually do (DEC-0313), or the stance breaks.
