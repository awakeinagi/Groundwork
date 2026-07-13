---
id: DEC-0487
type: decision
title: "Two EP-0010 spikes commissioned: schema-migration mechanism and performance calibration"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-13
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-13
source-span: "SES-0091 @ T12-T15"
overview: >-
  Two genuine unknowns surfaced at EP-0010 refinement: the schema-
  migration mechanism's shape and checker/graph performance at
  scale. This decision commissions two one-day-timeboxed spikes as
  EP-0010 derived work — migration-mechanism investigation (in-place
  versus side-by-side, replaying the Research-type addition) and
  performance calibration (latency curves at 750-10,000 artifacts,
  validating DEC-0387 at scale) — neither blocking the epic gate,
  only the stories that need their answers.
links:
  derives-from: [SES-0091]
  relates-to: [DEC-0387, DEC-0483]
---

# DEC-0487: Two EP-0010 spikes commissioned: schema-migration mechanism and performance calibration

## Context

Two genuine unknowns surfaced at refinement: the migration mechanism's shape and checker and graph performance at corpus scale.

## Decision

Two spikes are commissioned as EP-0010 derived work, drafted in this session and ratified with the epic's gate. The first investigates the schema-migration mechanism — in-place rewrite versus side-by-side migration under the corpus-level marker, replaying the Research-type addition as its test case — on a one-day timebox. The second calibrates performance — full-check and graph-sync latency curves at roughly 750 to 10,000 artifacts, validating DEC-0387's warm-projection finding at scale — delivering the calibrated fitness-function threshold, on a one-day timebox.

## Rationale

The migration mechanism cannot be designed from first principles against real corpora, and an uncalibrated performance threshold is a wish rather than a gate; the advisor debate's crossed concessions synthesized as calibrate-then-monitor.

## Alternatives Considered

Prose risk lines instead of owned artifacts were rejected as rediscovery debt. A standing fitness function with an uncalibrated threshold was rejected on the calibration argument, and waiting for performance pain was rejected once calibration cost fell to a one-day spike.

## Implications

Neither spike blocks the epic gate; each blocks only the stories that need its answer; the calibration spike's finding becomes the decision the performance fitness function cites.
