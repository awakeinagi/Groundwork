---
id: DEC-0372
type: decision
title: "ActiveGraph event-log provenance and deterministic replay are a strong fit for Groundwork's audit trail and impact analysis"
status: proposed
owner: awakeinagi@gmail.com
created: 2026-07-11
source-span: "SES-0070"
overview: >-
  PRELIMINARY -- proposed pending ratification at a dedicated
  ActiveGraph adoption/consolidation session. Round 3 of the SP-0017
  extension tested ActiveGraph's audit-trail machinery over the
  corpus projection (835 objects / 980 relations / 1815 events).
  save_state + Runtime.load reproduces a byte-identical event set
  (deterministic replay); the item-to-decision citation graph
  reconstructs from the reloaded event log alone and matches the
  live graph exactly (native provenance); and patching one cited
  decision to superseded and re-running localizes the finding-diff
  to exactly the affected findings (impact localization). The event
  log is the same append-only, immutable provenance record
  Groundwork already treats as source of truth, and could back both
  the audit trail and the impact/staleness analysis currently served
  by the separate graph index. One usage nuance recorded: detecting
  which shared inputs a fork mutated requires walking
  fork_only_events for patch.applied, not diff.divergent_objects,
  and semantic impact is best surfaced by re-running rules and
  diffing findings.
links:
  derives-from: [SES-0070]
  relates-to: [SP-0017, SES-0070, EP-0009, SP-0014, DEC-0138, DEC-0117, DEC-0146, DEC-0354]
---

## Context

PRELIMINARY -- proposed pending ratification at a dedicated ActiveGraph adoption/consolidation session (stakeholder extended SP-0017 into a full ActiveGraph capability assessment; SP-0017 closed on its fork-and-diff charter, these broader findings held proposed). Round 3 tested the runtime's audit-trail machinery over the corpus projection (835 objects / 980 relations / 1815 events).

## Decision

ActiveGraph's audit-trail machinery is a strong fit for Groundwork: (a) DETERMINISTIC REPLAY -- save_state + Runtime.load rebuilds a byte-identical object/relation/event set, reproducibly; (b) NATIVE PROVENANCE -- the item-to-decision citation graph reconstructs from the reloaded event log ALONE and matches the live graph exactly, with the full trace exportable; (c) IMPACT LOCALIZATION -- patching one cited decision (DEC-0152, cited by 20 items) to superseded and re-running localized the finding-diff to exactly the 20 affected R8 findings. The event log is precisely the append-only, immutable session/provenance record Groundwork already treats as source of truth, and could back BOTH the audit trail and the impact/staleness analysis currently served by the separate graph index.

## Rationale

This is the strongest single-capability fit found in the assessment; it maps onto two things Groundwork already does (immutable provenance; impact/staleness walks).

## Alternatives Considered

Keeping provenance/impact solely in the current LadybugDB graph index -- noted as the incumbent this capability could unify with the source-of-truth event log.

## Implications

Feeds the deferred ActiveGraph adoption decision. One usage nuance: detecting which SHARED inputs a fork mutated requires walking fork_only_events for patch.applied, NOT diff.divergent_objects (which tracks divergently-CREATED objects); semantic impact is best surfaced by re-running rules and diffing findings.

This is a capability finding from SP-0014's structural-projection lineage (cf. DEC-0368, which found no differential reactive-substrate evidence); any adoption is a separate DEC-0337/DEC-0335 decision.

