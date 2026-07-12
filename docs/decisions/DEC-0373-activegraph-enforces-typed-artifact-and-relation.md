---
id: DEC-0373
type: decision
title: "ActiveGraph enforces typed artifact and relation schemas like a write API, but its gate is behavior-mediated and not a drop-in for Groundwork's write-API gates"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-11
source-span: "SES-0070"
overview: >-
  PRELIMINARY -- proposed pending ratification at the ActiveGraph
  adoption/consolidation session. Round 4 modeled a minimal
  Groundwork pack (typed object types + a gating policy) to test
  whether ActiveGraph could be the write-API/gate substrate.
  Malformed writes (bad status value, bad kind, missing required
  field) and wrong-direction relations raise PackSchemaViolation,
  while valid writes succeed -- a strong fit for the write API's
  validation role. The policy gate works end to end: a behavior's
  proposed gated artifact stays PENDING until
  approve(approved_by=...), which materializes it and logs
  approval.proposed/approval.granted with the approver recorded. But
  gating is behavior-mediated -- a direct add_object of a gated type
  bypasses the gate entirely, and the ActiveGraph contract itself
  defers gate-enforcement hardening -- whereas Groundwork's write
  API enforces gates on every mutation. Usable as a write-substrate
  only if all writes funnel through gated behaviors, or the gate is
  hardened.
links:
  derives-from: [SES-0070]
  relates-to: [SP-0017, SES-0070, EP-0009, DEC-0312, DEC-0136, DEC-0033, DEC-0029, DEC-0315, DEC-0354]
---

## Context

PRELIMINARY -- proposed pending ratification at the ActiveGraph adoption/consolidation session (as above). Round 4 modeled a minimal Groundwork pack (typed object types + a gating policy) to test whether ActiveGraph could BE the write-API/gate substrate.

## Decision

ActiveGraph packs enforce typed artifact schemas and typed relations as a write API would: malformed writes (bad status value, bad kind, missing required field) and wrong-direction relations raise PackSchemaViolation, while valid writes succeed. The policy gate works end to end -- a behavior's proposed gated artifact stays PENDING until approve(approved_by=...), which materializes it and logs approval.proposed/approval.granted with the approver recorded. BUT gating is BEHAVIOR-MEDIATED: a DIRECT add_object of a gated type bypasses the gate entirely (the ActiveGraph CONTRACT itself defers gate-enforcement hardening). Groundwork's write API, by contrast, enforces gates on EVERY mutation.

## Rationale

Strong fit for schema/relation validation (the write API's validation role); partial fit for gate enforcement -- usable only if ALL writes funnel through gated behaviors, or the gate is hardened.

## Alternatives Considered

Relying on ActiveGraph's gate as-is for approval enforcement -- rejected as bypassable by direct writes.

## Implications

Feeds the deferred ActiveGraph adoption decision; the write-substrate role would require either a strict no-direct-write discipline or gate-enforcement hardening.

Per DEC-0351 this is throwaway spike evidence; any write-substrate adoption routes through the DEC-0337 option survey and DEC-0335 design intake, not by building it here.

