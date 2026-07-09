---
id: DEC-0262
type: decision
title: CPs capture unauthorized change attempts, unifying with ST-0035's out-of-authority proposals; live authorized instruction needs no CP
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-09
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-09
source-span: "SES-0050 @ T7-T8, T12-T13"
links:
  derives-from: [SES-0050]
  relates-to: [ST-0035, DEC-0047]
---

# DEC-0262: CP as the artifact form of the captured proposal

## Context

The stakeholder proposed CPs for changes attempted by someone lacking
approval authority (e.g., a lone lead attempting to supersede a
decision whose gate policy requires a committee, per DEC-0020).
Separately, ST-0035 AC2 already requires out-of-authority statements
to be captured as "proposals attributed to them, requiring
ratification by the right holder" — but names no artifact type for the
captured proposal. The CP type itself — prefix, triage states, and the
original source enum (`jira-drift | ui-suggestion |
implementation-feedback`) — was established by DEC-0047; this decision
extends its creation situations and source vocabulary.

## Decision

A Change Proposal is created in exactly two situations: (1) change
intent arriving **out-of-band** — reviewer comments, implementation
feedback, input queued while another session runs (the existing
semantics); (2) an **unauthorized change attempt** — someone instructs
a change they lack authority to approve; the change does not proceed
and the CP captures the attempt verbatim, awaiting triage/ratification
by the actual authority holder(s). The CP is thereby the concrete
artifact form of ST-0035 AC2's captured proposal — one mechanism,
in-session or at intake. A live instruction by an authorized user goes
straight to a session with no CP; the session record is the capture.

## Rationale

The boundary is channel and authority, not conflict — the
stakeholder's earlier conflict-based understanding was corrected
in-session (conflict with accepted decisions is supersession/CFL
territory). Unifying with ST-0035 gives the paradigm and the
application one concept instead of two near-identical
"proposal awaiting ratification" notions.

## Alternatives Considered

- **Every change intent gets a CP**: uniform lineage, but a CP per
  live conversation duplicates the session record.
- **Also capture declined off-record proposals**: preserves "why not
  X?" but records what the user chose to keep off the record; the
  Idea type (DEC-0258, `declined` status) now covers the useful part.
- **Keep ST-0035 capture separate from CPs**: leaves two concepts.

## Implications

Additive to ST-0035 (its AC2 gains a concrete artifact form — noted
for consistency review, no contradiction). CP template/docs gain the
`unauthorized-attempt` source. In solo-governance projects (DEC-0263)
this path is dormant. Application reflection is parked in IDEA-0001.
