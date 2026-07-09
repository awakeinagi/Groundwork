---
id: SES-0021
type: session
title: Realign gated EP-0001 stories with release scoping, trigger subscriptions, and infrastructure ports
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-07
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude Code (claude-fable-5)
transcript-fidelity: reconstructed
links:
  relates-to: [ST-0001, ST-0007, ST-0008, ST-0010, EP-0001, DEC-0121, DEC-0077]
---

# SES-0021: Gated-Story Realignment

## Purpose

The eight gated stories (ST-0001–ST-0008)
were gated on 2026-07-06, before four design sessions landed:
SES-0016 (release scoping),
SES-0017 (embedded stack +
trigger registry), SES-0018
(trigger subscriptions), and
SES-0020 (infrastructure
ports). This session audits the gated set against the decisions those
sessions produced, agrees the amendments, and resolves a wording
tension between DEC-0121
and DEC-0077.

## Transcript

**T1 — awakeinagi.** Asked the facilitator to revisit the gated stories
and see if they need updating given the recent changes to the design.

**T2 — facilitator.** Presented the audit verdict: two stories need
real amendment, one a light touch, five are unaffected, and
EP-0001 has a
new coverage gap. Specifically: (1)
ST-0007's check inventory is
missing the release-scoping rule family
(DEC-0097,
DEC-0098,
DEC-0099,
DEC-0101,
DEC-0104) and the
trigger-registry rule family
(DEC-0108,
DEC-0109,
DEC-0110);
(2) ST-0001's frontmatter
schemas must validate the `deferred` status and `release:` grammar;
(3) ST-0008's outbox
criterion should be phrased against the app database port
(DEC-0121,
DEC-0122,
DEC-0124);
(4) no story delivers the app database port
EP-0001 now
lists in Interfaces & Contracts — recommended a new story rather than
folding it into
ST-0008, since the port
serves outbox and bookkeeping and the conformance suite is a distinct
deliverable. Flagged one genuine tension:
DEC-0121 lists
"counters" among app-database-port workloads while
DEC-0077 says no
persistent ID-counter store exists anywhere; recommended reading
DEC-0121's "counters"
as operational bookkeeping counters, leaving
DEC-0077 intact, rather
than superseding it. Noted
SES-0019 does not touch
the gated set (its product output
ST-0009 is deferred
backlog and skill tooling is outside the port requirement per
DEC-0121).
ST-0002,
ST-0003,
ST-0004,
ST-0005, and
ST-0006 are
unaffected.

**T3 — awakeinagi.** Asked for an overview of the proposed
"counters = non-ID bookkeeping" reading of
DEC-0121.

**T4 — facilitator.** Explained the collision and the reading:
DEC-0077 is a specific,
deliberate decision that ID-counter state has no persistent store —
rescan-on-boot over all refs — chosen so no second source of truth can
drift from git; DEC-0121's
"counters" is one word in an illustrative workload list, its session
never discussed ID allocation, and it does not list
DEC-0077 as superseded.
Proposed reading: the port's counters are operational bookkeeping
(outbox retry counts, debounce state, session-inactivity tracking) —
losable inconvenience, not truth; ID counters are derivable truth about
the repo and stay rescan-only. Supersession in Groundwork is explicit,
never incidental; specific beats general; and the engineering still
favors rescan-on-boot. Consequences: no change to
ST-0005; the new port story's
scope wording makes the exclusion explicit; the alternative
(superseding DEC-0077)
was not recommended.

**T5 — awakeinagi.** "Agreed on all three — run SES-0021 as proposed."
Ratified: (1) amend
ST-0001,
ST-0007, and
ST-0008 as presented;
(2) derive a new story
(ST-0010) for the app
database port; (3) the counters-as-operational-bookkeeping reading of
DEC-0121, with
DEC-0077 standing.

## Decisions Produced

- DEC-0125
  — clarifying, not superseding:
  DEC-0121's app-database-port
  "counters" are operational bookkeeping; artifact-ID allocation state
  stays rescan-only per
  DEC-0077.

The story amendments themselves cite already-accepted decisions — they
are alignment, not new design.

## Conflicts Raised

None — the DEC-0121/DEC-0077
tension was resolved in-session by clarification
(DEC-0125).
