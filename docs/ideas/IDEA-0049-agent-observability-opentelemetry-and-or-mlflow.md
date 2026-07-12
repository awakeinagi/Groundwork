---
id: IDEA-0049
type: idea
title: "Agent observability: OpenTelemetry and/or MLflow integration for profiling agents"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-12
proposed-by: awakeinagi@gmail.com
overview: >-
  Stakeholder verbatim ask at SES-0076 close: OTel and/or MLFlow
  integration for agents so we can start profiling them for further
  optimization. Instrumenting agent spawns, task durations, and
  tool-call profiles would ground the post-adoption measurements
  that IDEA-0046 and the DEC-0393 backgrounding defaults call for,
  replacing anecdotal wall-clock complaints with traces.
links:
  derives-from: [SES-0076]
  relates-to: [IDEA-0046]
---

# IDEA-0049: Agent observability: OpenTelemetry and/or MLflow integration for profiling agents

## The Idea

Instrument agent spawns, task durations, and tool-call profiles with OpenTelemetry and/or MLflow, so agents can be profiled for further optimization instead of relying on anecdotal wall-clock complaints.

## Spark Context

Stakeholder verbatim ask at SES-0076 close: "OTel and/or MLFLow integration for agents so we can start profiling them for further optimization." Instrumenting agent spawns, task durations, and tool-call profiles would ground the post-adoption measurements that IDEA-0046 and the DEC-0393 backgrounding defaults call for, replacing anecdotal wall-clock complaints with traces.

## Disposition

Pending — awaiting take-up. Relates to IDEA-0046, the post-adoption measurement idea this would instrument.
