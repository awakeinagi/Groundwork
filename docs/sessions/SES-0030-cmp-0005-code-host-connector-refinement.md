---
id: SES-0030
type: session
title: Refine CMP-0005 (Code-Host Connector Protocol) — element decomposition and contract shape
status: closed
owner: awakeinagi@gmail.com
created: 2026-07-08
overview: >-
  Refined CMP-0005 from stub to contract-complete. Handled SP-0004
  blocker by drafting full contract with check-administration flagged
  provisional pending spike findings. Settled one-protocol-element
  decomposition, typed-error-conditions convention, v1 minimum capability
  set, push-webhook event delivery, and allowlist filtering as
  behavior clause. Decision-recall audit flagged missing deferral
  decision; added check-unregister operation found by audit gap.
  Produced DEC-0166-DEC-0171.
participant: awakeinagi@gmail.com
participant-role: eng-lead
facilitator: Claude (Sonnet 5)
transcript-fidelity: reconstructed
links:
  derives-from: [EP-0005]
  relates-to: [ST-0019, ST-0023]
---

# SES-0030: Refine the Code-Host Connector Protocol Component Doc

## Purpose

CMP-0005
existed only as a stub. Both stories that motivate it —
ST-0019 (protocol
and capability manifest) and
ST-0023 (read-only
context access) — are approved with detailed acceptance criteria, so
this session targeted the genuinely open translation choices: how to
handle the SP-0004
check-administration blocker,
how the component decomposes into Design Elements, the error/idempotency
convention, the minimum capability set, the webhook delivery model, and
where allowlist enforcement lives.

## Transcript

**T1 — Facilitator.** Opened with the
SP-0004 blocker:
ST-0019's
implementer notes say not to harden check-registration/result-posting
before SP-0004's
findings land, and SP-0004
is approved but unexecuted (no BBDC instance
available in this conversation). Presented three options: (a) draft the
full contract now with check-administration explicitly flagged
provisional, gating the component this session; (b) draft everything
except check-administration, leaving it a genuine Pending section and
holding the gate on that family; (c) hold the entire session until
SP-0004 executes.
Recommended (a) — the consumer-side shape from
CMP-0001 and
CMP-0004's
forward declarations is already fixed; only BBDC-side feasibility is
open, and flagging the risk costs less than stalling the whole
component.

Also asked how Design Elements should decompose, offering
CMP-0003's
one-big-protocol-element-with-lettered-families pattern as the
recommended shape against splitting into multiple protocol elements by
concern (orchestration / reviews / administration / reads).

Also asked whether to adopt
CMP-0003's
typed-error-condition convention (per
DEC-0129,
DEC-0139)
for this protocol's operations, versus leaving failure handling to
adapter discretion.

**T2 — Product Owner.** Accepted all three recommendations: draft the
full contract now with check-administration flagged provisional; one
`CodeHostConnector` protocol element with lettered operation families;
typed error conditions per operation.

**T3 — Facilitator.** Second round. Asked what belongs in the v1
minimum capability set
(DEC-0045
requires one, undefined until now),
recommending: core orchestration, review posting (either path),
read-only browse/search, permission probe, and check-run result
posting as the minimum, with required-check *registration*, team-sync,
review-dismissal, and native path-scoped reviewer rules as
above-minimum/emulatable — against making native check registration
itself mandatory. Asked how webhook/event delivery should work,
recommending push (connector registers a webhook, normalizes payloads
to a `HostEvent` schema) per
DEC-0145's
existing design, against a pull/poll-based protocol operation. Asked
where allowlist enforcement
(DEC-0049) belongs,
recommending a behavior clause directly on the read-operation family
against a separate `AllowlistFilter` element.

**T4 — Product Owner.** Accepted all three recommendations: the
orchestration/review/read/probe/check-result-posting minimum set with
registration and admin capabilities above it; push-webhook delivery;
allowlist filtering as a read-operation behavior clause, not a separate
element.

**T5 — Facilitator.** Drafted the full contract from the confirmed
shape: `CodeHostConnector` (protocol, eleven API items `A-1`–`A-11`
plus two behavior items covering capability gating and conformance),
`CapabilityManifest` (value, the minimum/above-minimum schema),
`HostEvent` (event, the normalized webhook-event schema). Ran the
graduation review against all three candidates: none is consumed by
more than one component outside CMP-0005's
own API surface, and none needs independently versioned conformance
apart from the whole protocol — no graduation, matching the bar
CMP-0002/CMP-0003
cleared (an actual second consumer) which isn't met here. Confirmed the
Dependencies section against the exact forward-declared consumption
lists already recorded in
CMP-0001 (amended
per DEC-0142)
and CMP-0004, and
verified every operation either list names resolves to a lettered item
in the new contract.

**T6 — Product Owner.** Confirmed the drafted contract and the
no-graduation call.

**T7 — Facilitator.** Ran the decision-recall audit (Sonnet 5 judge)
against the drafted contract. Findings: (1) the "additional hosts
deferred" Out of Scope bullet named
ST-0028 but
not DEC-0156,
the decision establishing the deferral-and-trigger mechanism itself —
added; (2) `CodeHostConnector.A-4`'s `attribution_block` parameter was
described only as "opaque, pre-signed" without citing
DEC-0153,
which defines its concrete shape — added a citation and shape summary
so implementers know what they're passing through; (3) a genuine
contract gap: `A-6` had no operation to clear a required-check entry
once a gate policy stops requiring it. Presented the gap to the Product
Owner with a recommendation to close it now (small addition, matches a
real reconciliation need
CMP-0004's
`PolicyCompiler` will have) against deferring it as an explicit
boundary statement.

**T8 — Product Owner.** Chose to close the gap now.

**T9 — Facilitator.** Added `check.unregister_required(repo, branch,
check_names[])` to `CodeHostConnector.A-6`, applied the
DEC-0156
and
DEC-0153
citations, and re-ran the checker — clean.

## Decisions Produced

- DEC-0166 —
  CMP-0005
  drafts and gates now; check-administration operations marked
  provisional pending
  SP-0004.
- DEC-0167 —
  typed error conditions and natural-key idempotency convention.
- DEC-0168 —
  the v1 minimum capability set.
- DEC-0169 —
  push-webhook event delivery; polling is the sweep's backstop only.
- DEC-0170 —
  allowlist filtering as a read-operation behavior clause.
- DEC-0171 —
  three-element decomposition (`CodeHostConnector`,
  `CapabilityManifest`, `HostEvent`); no graduation.

## Conflicts Raised

None.
