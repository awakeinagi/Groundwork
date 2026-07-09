---
id: ST-0019
type: story
title: Code-host connector protocol and capability manifest
status: approved
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
owner: eng-lead
created: 2026-07-08
links:
  derives-from: [EP-0005]
  satisfies: [BG-0001]
  impacts: [ST-0020, ST-0021, ST-0023, ST-0024, ST-0025, ST-0031]
cites: [DEC-0014, DEC-0028, DEC-0032, DEC-0036, DEC-0043, DEC-0045, DEC-0049,
        DEC-0079, DEC-0132, DEC-0142, DEC-0145, DEC-0150, DEC-0172]
---

# ST-0019: Code-Host Connector Protocol and Capability Manifest

## Summary

The host-agnostic seam every host interaction crosses: the code-host
connector protocol's operation families, its capability manifest schema
with the documented minimum capability set, the normalized webhook
event schema, and the conformance suite that qualifies any adapter —
satisfying the consumption lists the artifact store and gate engine
have already forward-declared.

## Acceptance Criteria

1. The protocol defines every operation family the boundary needs:
   fork provisioning; branch create/delete and push; PR open, merge,
   and review-state; review posting on both the delegated-OAuth and
   program-user paths; check-run result posting; required-check
   registration; branch-protection administration; team
   administration; read-only browse/search; permission probe; and
   webhook/event subscription
   (per DEC-0028,
   DEC-0032,
   DEC-0043,
   DEC-0132,
   DEC-0142,
   DEC-0049).
2. CMP-0001's
   forward-declared consumption list — fork provisioning, branch
   create/delete, PR open/merge/review-state, check-run result
   posting, permission probe — is satisfied operation-for-operation,
   or a conflict is raised
   (per DEC-0132).
3. The gate engine's operations — required-check registration,
   branch-protection write and reconcile, team administration — are
   defined as CMP-0004
   consumes them, keeping registration distinct from result posting
   (per DEC-0142,
   DEC-0036).
4. Each connector declares a capability manifest against a published
   schema; a documented minimum capability set states what a host must
   support to run Groundwork at all, and every operation above the
   minimum is marked so the gate engine's compiler can adapt or emulate
   (per DEC-0045).
5. Host webhooks surface through the protocol as a normalized event
   schema (PR state, review, push, check events) that downstream
   consumers subscribe to without host-specific parsing
   (per DEC-0145,
   DEC-0045).
6. A protocol conformance suite qualifies any adapter; the local-git
   fake connector passes it in full — manifest included — and remains
   the hermetic CI double for every consumer
   (per DEC-0079).

## Component Impact

CMP-0005 —
supplies the protocol's operation contracts, manifest schema, event
schema, and conformance expectations.

## Out of Scope

Adapter implementations — the GitHub connector, v1
(ST-0031, per
DEC-0172) and the
Bitbucket Data Center connector, deferred
(ST-0020); allowlist
*enforcement* and citation format for reads
(ST-0023); token handling and
attribution signing
(ST-0021); connectors
for additional hosts
(ST-0028, deferred);
writing to codebases — permanently out for the whole system
(per DEC-0014).

## Notes for Implementers

The fake connector predates this story
(ST-0003 ships it); this
story owns the protocol spec and conformance suite the fake must
track — expect to adjust the fake, never the contract, when they
disagree.

Do not harden the check-administration operation family (registration,
result posting) before
SP-0004's findings
land — if BBDC cannot express the assumed semantics, the protocol
shape, not just the adapter, may need rework
(per DEC-0150).

The manifest-plus-conformance shape established here is the "standard
connector pattern" EP-0005's sibling contracts follow: ST-0024's
notifier contract and ST-0025's work-management contract each declare
per-adapter capability manifests in this story's schema-plus-minimum-set
shape (per DEC-0045).
