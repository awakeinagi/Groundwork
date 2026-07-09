---
id: DEC-0165
type: decision
title: ConflictGate exposes escalate, resolve, and override-approver operations; timeout election is frontmatter
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0029 @ T5-T6"
links:
  derives-from: [SES-0029]
  relates-to: [DEC-0039, DEC-0143, DEC-0147, DEC-0162]
---

# DEC-0165: ConflictGate Operation Surface

## Context

ST-0015
requires the `conflicts-open` blocking check plus Arbiter
conflict operations: escalation, resolution, approver override, and the
electable timeout-to-default path
(DEC-0039). Whether these
operations get explicit API items or stay implicit (mechanical writes
or session-agent-driven) was undecided.

## Decision

`ConflictGate` exposes three API items — `escalate(conflict-id)`,
`resolve(conflict-id, decision-ref)`, `override-approver(gate-ref,
new-approver)` — plus the `conflicts-open` check evaluation and the
timeout-fire path that drafts a System Decision via the auto-PR
machinery (DEC-0143). The
per-artifact timeout-to-default election itself is expressed in
artifact frontmatter, tier-1 validated by
CMP-0001 — not a
service operation.

## Rationale

Matches
ST-0015's
acceptance criteria one-to-one and gives the Arbiter
queue (DEC-0147) concrete operations
to act through rather than leaving escalation and override as
unspecified session-agent behavior. Keeping the timeout election in
frontmatter (not an API call) is consistent with every other
gate-relevant configuration living as versioned, tier-1-validated
artifact data.

## Alternatives Considered

Minimal surface — only `evaluate` (the blocking check) and
`fire-timeout` (the System-Decision drafter) — treating
escalation/resolution/override as implicit mechanical writes or
session-agent actions. Rejected: escalation and resolution are
Arbiter-initiated design actions, not metadata-only facts, so they
belong in `ConflictGate`'s explicit contract rather than being smuggled
into the mechanical-write allowlist.

## Implications

`ConflictGate`'s API contract carries these three explicit items plus
its check-evaluation and timeout-fire behavior items; the Arbiter UI
(EP-0006) calls this surface
directly rather than composing conflict resolution out of generic
storage writes.
