---
id: DEC-0125
type: decision
title: The app database port's "counters" are operational bookkeeping; ID allocation state stays rescan-only
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0021 @ T3-T5"
links:
  derives-from: [SES-0021]
  relates-to: [DEC-0121, DEC-0077, DEC-0122]
---

# DEC-0125: Port "Counters" Exclude ID Allocation

## Context

DEC-0121 describes the app database
port's workload as "outbox, bookkeeping, counters."
DEC-0077 says artifact-ID counter
state has **no persistent store anywhere** — startup rescans all refs
for the max ID per prefix. Read literally, "counters" behind a
persistent port contradicts that
(SES-0021 T2-T4).

## Decision

Clarifying — not superseding — DEC-0121:
its "counters" means **operational bookkeeping counters** (outbox
dispatch/retry counts, debounce and regeneration state,
session-inactivity tracking, telemetry tallies) — state whose loss is
an inconvenience, never a source of truth about the design docs.
Artifact-ID allocation state is **excluded from the port**:
DEC-0077 stands unchanged, and the
app database port contract exposes no ID-counter surface.

## Rationale

DEC-0121 never discussed ID
allocation and lists no supersession; in Groundwork, supersession is
explicit, never incidental. The specific decision governs its own
territory over an illustrative workload list. Persisting ID counters
would reintroduce the drift-from-git failure mode rescan-on-boot was
chosen to eliminate, and nothing in the ports work created a new reason
to accept it.

## Alternatives Considered

- **Supersede DEC-0077 and move ID
  counters into the app database** — saves the boot-time ref scan, but
  accepts a counter that can disagree with committed reality across
  refs, and forces rewriting
  ST-0005's criteria. Rejected.

## Implications

ST-0010's scope states the
exclusion explicitly; ST-0005 is
unchanged.
