---
id: SP-0020
type: spike
title: "Checker and graph performance calibration across corpus scales"
status: approved
approved-on: 2026-07-13
approved-by: awakeinagi@gmail.com
owner: awakeinagi@gmail.com
created: 2026-07-13
timebox: 1d
overview: >-
  A one-day spike calibrating the Engine's performance fitness
  function that DEC-0487 commissions. It synthesizes corpora at
  roughly 750, 2,000, 5,000, and 10,000 artifacts and measures full-
  check, single-write-apply, and graph-sync latency cold and warm,
  validating DEC-0387's warm-projection speedup finding at scale, to
  find where those latencies cross interactive tolerance and to
  calibrate a defensible threshold. Commissioned by DEC-0487 at
  SES-0091 as EP-0010 derived work; drafted ahead of EP-0010's own
  gate and ratified by that gate's approval rather than gated
  individually.
links:
  derives-from: [EP-0010]
  satisfies: [BG-0002]
cites: [DEC-0487, DEC-0387]
---

# SP-0020: Checker and graph performance calibration across corpus scales

## Question

At what corpus sizes do full-check and incremental graph-sync
latencies cross interactive tolerance, and what threshold should the
Engine's performance fitness function enforce?

## Why It Blocks

Without measured baselines a performance target is an adjective, and
the fitness function DEC-0487 commissions this spike to calibrate
cannot gate anything. The Engine's quality contract needs a defensible
threshold before performance-sensitive stories are written. Commissioned
by DEC-0487 at SES-0091; this spike is drafted ahead within EP-0010's
gate bundle and ratified by the epic's own approval rather than gated
individually.

## Method

Synthesize corpora at roughly 750 (current scale), 2,000, 5,000, and
10,000 artifacts by cloning and perturbing real artifacts; measure
full check, single-write apply with post-write re-validation, and
graph sync, both cold and warm, validating DEC-0387's warm-projection
speedup finding at scale. Deliverable: measured latency curves plus a
calibrated fitness-function threshold recorded as a decision. Timebox:
one day.

Before measurement, the spike fixes a definition of interactive
tolerance (per-operation-class p95 latency bounds); the calibrated
threshold is then derived from the measured data against that fixed
definition.

## Findings

Not started.

## Resulting Decisions

None yet; the spike must produce at least one decision at completion.
