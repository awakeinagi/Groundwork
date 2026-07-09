---
id: DEC-0233
type: decision
title: The attribution block stays a CMP-0007 element; CMP-0004 consumes it as a dependency
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-08
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-08
source-span: "SES-0045 @ T1-T2"
links:
  derives-from: [SES-0045]
  relates-to: [DEC-0153, DEC-0136]
---

# DEC-0233: AttributionBlock Stays in the Identity Component

## Context

DEC-0153 flagged the
attribution-block schema as a cross-component seam to weigh at
graduation review:
CMP-0004 verifies
it, while CMP-0005
passes it through explicitly opaquely.

## Decision

The `AttributionBlock` value element stays in
CMP-0007.
CMP-0004 adds a
`depends-on` edge consuming its schema and verification items. This is
the recorded outcome of the graduation review for this element.

## Rationale

One external consumer does not meet the more-than-one-CMP bar
(DEC-0136); the block's
signing rules are inseparable from the review-delegation service that
produces it.

## Alternatives Considered

- **Graduate to a value-type CMP**: cleaner if more verifiers appear;
  one more doc and gate now for a single consumer.

## Implications

If a second external consumer appears, the review re-runs and the
element graduates then.
