---
id: DEC-0367
type: decision
title: "Compiled structural rules fire true findings; precision is source-dependent"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-11
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-11
source-span: "SP-0014 findings; SES-0069 @ T12-T17"
overview: >-
  SP-0014's 24-rule throwaway rulebase, fired over the re-
  established SP-0013 projection, produced 102 findings of which the
  stakeholder disposed 33 as real or change-worthy -- including four
  ratified contract items citing superseded DEC-0014, three multi-
  consumer elements missed by gate-time graduation reviews, six
  happy-path-only service contracts, and a numeric error in
  DEC-0359's own record -- none caught by the existing checker or
  gate process. This affirms SP-0014's question and DEC-0354's
  executable-design-knowledge premise. Precision proved strongly
  source-dependent: rules compiled from accepted decisions fired
  near-perfectly (all five calibration instruments passed; the one
  deviation was compilation infidelity, not source or substrate
  error), while rules compiled from prose best practices produced
  the large majority of the noise. Rationale rests on SP-0014's
  Findings catalog and per-rule precision notes, dispositions taken
  at SES-0069. The alternative -- a mostly-noise outcome that would
  have weakened the premise regardless of substrate -- did not
  occur. Implications: the premise holds for decision-compiled
  rules; prose-compiled rules need role modeling and convention
  awareness before they are precision-viable, corroborating
  SP-0015's compilation-fidelity concern from the structural side.
  Remediation routed to IDEA-0035, IDEA-0036, IDEA-0037, IDEA-0038,
  and the IDEA-0039 architecture-review session.
links:
  derives-from: [SP-0014]
  relates-to: [DEC-0354, DEC-0355, DEC-0359, SP-0013]
cites: [DEC-0354, DEC-0355, DEC-0359]
---

# Compiled structural rules fire true findings; precision is source-dependent

## Context

SP-0014 asked whether structural rules hand-compiled from curated sources and fired over the projected corpus produce real findings on the real design, or noise.

## Decision

SP-0014's question is answered affirmatively. The 24-rule throwaway rulebase fired 102 findings over the re-established SP-0013 projection; the stakeholder disposed 33 as real or change-worthy — including four ratified contract items citing superseded DEC-0014, three multi-consumer elements missed by gate-time graduation reviews, six happy-path-only service contracts, and a numeric error in DEC-0359's own record — none of which the existing checker or gate process had caught. Precision is strongly source-dependent: rules compiled from accepted decisions fired near-perfectly (all five calibration instruments passed; the single deviation was compilation infidelity, not source or substrate error), while rules compiled from prose best practices produced the large majority of the noise.

## Rationale

The findings catalog and per-rule precision notes recorded in SP-0014's Findings section, dispositions taken at SES-0069.

## Alternatives Considered

The null outcome — mostly-noise firing — would have weakened DEC-0354's executable-design-knowledge premise regardless of substrate; it did not occur.

## Implications

The premise holds for decision-compiled rules; prose-compiled rules need role modeling and convention awareness before they are precision-viable (corroborating SP-0015's compilation-fidelity concern from the structural side); remediation routed to IDEA-0035, IDEA-0036, IDEA-0037, IDEA-0038 and the IDEA-0039 architecture-review session.
