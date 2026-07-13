---
id: DEC-0508
type: decision
title: "Dogfooding-loop contract: the existing intake path, no dedicated machinery"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0094 @ T4–T5, T10–T11"
overview: >-
  DEC-0463 merged dogfooding into EP-0014 without defining its
  mechanism. During SES-0094's consultation, dedicated capture
  machinery was proposed and withdrawn against the DEC-0335 no-
  arbitrary-builds guard once the record-grounded architect showed
  the existing intake path already carries dogfooding output
  (IDEA-0064, IDEA-0065 from SES-0089). This decision states the
  loop's mechanism is the existing change-intake path — observations
  enter as IDEA-* items when not acted on immediately — formalized
  by one derived story, with no dedicated capture machinery built.
links:
  derives-from: [SES-0094]
  relates-to: [DEC-0335, DEC-0463, DEC-0019]
---

# DEC-0508: Dogfooding-loop contract: the existing intake path, no dedicated machinery

## Context

DEC-0463 merged dogfooding into this epic and DEC-0019 founded the practice, but the record defined the loop's purpose rather than its mechanism. During the SES-0094 consultation the best-practice-independent architect initially proposed dedicated capture machinery (a friction-report artifact type, a tagged backlog channel, a review cadence, loop metrics) and withdrew it against the DEC-0335 no-arbitrary-builds guard; the record-grounded architect showed the existing path already carries dogfooding output (IDEA-0064 and IDEA-0065 entered through it in SES-0089).

## Decision

The dogfooding loop's mechanism is the existing intake path: observations from the Groundwork project's own use of the paradigm enter change intake like any other proposal, captured as IDEA-* items when not acted on immediately. A derived story formalizes this contract. No dedicated capture machinery is built.

## Rationale

The existing pipeline demonstrably works and no lost-observation gap has been experienced; building machinery without a demonstrated gap fails DEC-0335.

## Alternatives Considered

Light tagging of dogfooding-born items for measurability was declined for now — it is a semantic format change needing its own design, wanted only if the loop should be measured rather than merely working. Dedicated capture machinery was rejected outright for lack of a demonstrated gap.

## Implications

One dogfooding-lane story formalizes the contract sentence. If observations are ever lost in practice, that evidence reopens the tagging or machinery question through normal intake.
