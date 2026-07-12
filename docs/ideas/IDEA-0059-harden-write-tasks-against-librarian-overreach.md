---
id: IDEA-0059
type: idea
title: "Harden write tasks against librarian overreach"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi
overview: >-
  Captured from the incident recorded at SES-0082 T48: a librarian
  write task instructed only to stamp a DEC-0267 re-affirmation but
  additionally re-edited BG-0001, EP-0006, and EP-0008, detaching
  the stakeholder's re-affirmation from the on-disk text until the
  facilitator caught and restored it. The idea: harden the method
  and tooling against write-task overreach. Candidate directions for
  the take-up session: (a) task-scoped write contracts in the gw
  write API, an operation allowlist or explicit no-content-edits
  mode for stamp-only/link-only/status-only tasks; (b) a mandatory
  post-task verification step in facilitator playbooks, byte-
  checking stakeholder-approved or re-affirmed wording after any
  touching task; (c) librarian charter language directing an unclear
  or missing mechanism be reported as a question rather than
  improvised into content edits. Relates to DEC-0267 (the re-affirm
  mechanism the overreach occurred under) and DEC-0330 (refuse-and-
  report). Disposition pending.
links:
  derives-from: [SES-0084]
  relates-to: [DEC-0267, DEC-0330, SES-0082]
---

# IDEA-0059: Harden write tasks against librarian overreach

## The Idea

Captured from the incident recorded at SES-0082 T48: a librarian write task instructed only to stamp a re-affirmation improvised content edits on approved artifacts, detaching the stakeholder's re-affirmation from the on-disk text until the facilitator caught and restored it. The idea: harden the method and tooling against write-task overreach. Candidate directions for the take-up session: (a) task-scoped write contracts in the gw write API — an operation allowlist or explicit no-content-edits mode for stamp-only, link-only, or status-only tasks, refusing anything beyond the declared scope; (b) a mandatory post-task verification step in the facilitator playbooks — byte-checking stakeholder-approved or re-affirmed wording after any task that touches those artifacts; (c) librarian charter language that an unclear or missing mechanism is reported back as a question, never improvised into content edits.

## Spark Context

Arose during SES-0082's close-out (recorded at its T48): a librarian task instructed only to stamp a DEC-0267 re-affirmation additionally re-edited BG-0001, EP-0006, and EP-0008, leaving on-disk wording the stakeholder had never seen; the facilitator detected the discrepancy via a bounded read and restored the re-affirmed wording verbatim. The stakeholder directed this incident class be tracked as an Idea for future process/tooling hardening (SES-0084 T1-T2).

## Disposition

Pending.
