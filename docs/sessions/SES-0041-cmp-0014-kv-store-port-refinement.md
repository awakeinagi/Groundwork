---
id: SES-0041
type: session
title: KV-Store Port contract refinement
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Refined CMP-0014 (KV-store Port) toward contract-completeness from
  ST-0062, which pre-resolved the Queue Port's layering ambiguity.
  Settled key shape as (namespace, key) pair, mandatory TTL on every
  set(), and atomic set-if-absent primitive for coordination-lock use
  case. Decision-recall audit surfaced same citation consistency gaps as
  CMP-0012 (port-graduation pattern and deferral decision); correctly
  declined to cross-cite Queue Port's adapter pattern since that's
  Queue-specific. No graduation indicated. Produced DEC-0219-DEC-0221.
participant: awakeinagi@gmail.com
participant-role: stakeholder
facilitator: Claude Sonnet 5 (claude-sonnet-5) via Claude Code CLI
transcript-fidelity: reconstructed
links:
  relates-to: [EP-0008, ST-0062, CMP-0014]
---

# SES-0041: KV-Store Port Contract Refinement

## Purpose

Refine the stubbed CMP-0014
(KV-store Port) toward contract-completeness. Most of the contract is
already settled by ST-0062's
Acceptance Criteria, including the adapter-layering ambiguity (resolved
at story grain, unlike the identical ambiguity that needed a session
for the Queue Port). This session resolves the remaining points: the
key-addressing shape, whether TTL is mandatory, and whether the
"single-writer coordination locks" use case named in scope needs an
atomic port operation.

## Transcript

**T1 — Facilitator.** Asked a Round 1 question set, each with a
recommended answer:
1. Key shape — a flat `key` string vs. a `(namespace, key)` pair
   mirroring `AppDatabasePort.A-3`'s bookkeeping family. Recommended:
   `(namespace, key)`, so rate-limiting, coordination locks, and
   caching consumers can't collide on key names.
2. TTL requirement — mandatory on every `set()` vs. optional
   (no-TTL keys live forever). Recommended: mandatory, to structurally
   enforce the port's ephemeral-only scope
   (DEC-0203) rather
   than let it drift into a second permanent store.
3. Atomic lock primitive — ST-0062's
   scope names "single-writer coordination locks," but plain
   `get()`+`set()` composition races. Flagged this as a contract gap:
   recommended adding an atomic `set-if-absent` operation so the
   port can actually deliver the use case its own scope names, rather
   than leaving lock semantics to caller-composed, unsafe get/set.

**T2 — Stakeholder.** Confirmed all three recommendations as given.

**T3 — Facilitator.** Decision-recall audit on the drafted
CMP-0014 surfaced the same
two citation-consistency gaps found for its sibling
CMP-0012 in the same session
thread: `DEC-0135` (port-graduation pattern, invoked by the header
blockquote but missing from `cites:`) and `DEC-0205` (trigger-deferral
decision backing the External Adapters Out of Scope bullet). Also
specifically judged whether `DEC-0218` (Queue Port's identical
"sibling adapter on the co-located engine" pattern, decided earlier in
this same session) should be cross-cited here: ruled no — `DEC-0218`
is scoped to the Queue adapter specifically; `CMP-0014`'s own
Implementation Guidance already states the identical pattern for the
KV adapter directly, citing the general-purpose decisions
(`DEC-0204`, `DEC-0129`) that both narrow from, so citing a
Queue-specific decision here would misattribute provenance. All other
candidates
(CMP-0004/CMP-0005
decomposition decisions, release-label grammar, BBDC connector
specifics) were noise from generic term overlap.

**T4 — Facilitator.** Graduation review: checked `KvStorePort` against
the graduation rule via the graph tool's `elements` command. Consumed
only within `CMP-0014` today; no graduation indicated.

### Post-Close Enrichment

- 2026-07-08 — Cross-reference enrichment (per DEC-0248, DEC-0250):
  this session refined CMP-0014, a component of the Backend
  Application Platform epic EP-0008.

## Decisions Produced

DEC-0219,
DEC-0220,
DEC-0221

## Conflicts Raised

None.
