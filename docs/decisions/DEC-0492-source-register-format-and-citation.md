---
id: DEC-0492
type: decision
title: "Source Register format and citation"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi
decided-on: 2026-07-13
source-span: "SES-0092"
overview: >-
  The Source Register is a table with columns ID, Title, Reference,
  Type, and Accessed, carrying DEC-0452's required fields. Source
  identifiers S1, S2, and so on are stable within the artifact and
  never renumbered. Every finding cites its sources inline as [Sn]
  lists; the checker verifies that every [Sn] resolves to a register
  row and warns on never-cited sources.
links:
  derives-from: [SES-0092]
  relates-to: [DEC-0452]
---

# DEC-0492: Source Register format and citation

## Context

Findings need a uniform, checkable way to cite the evidence behind
them, and the register needs stable identifiers that survive edits
and additions across rounds.

## Decision

The Source Register is a table with columns ID, Title, Reference,
Type, and Accessed, carrying DEC-0452's required fields. Source
identifiers S1, S2, and so on are stable within the artifact and
never renumbered. Every finding cites its sources inline as [Sn]
lists; the checker verifies that every [Sn] resolves to a register
row and warns on never-cited sources.

## Rationale

Stable, never-renumbered source IDs let findings across many rounds
cite sources without their citations going stale as the register
grows; a mechanical [Sn]-to-register-row resolution check gives the
same "no dangling citation" guarantee cross-artifact bare-ID
references get elsewhere in the corpus, and a never-cited-source
warning catches register entries added but never actually used.

## Alternatives Considered

Per-round-local source numbering was considered and rejected: it
would make a finding's citation ambiguous outside its own round and
break cross-round source reuse.

## Implications

The checker resolves every [Sn] token against the register table and
flags unresolved citations as tier-2 failures and never-cited
register rows as warnings.
