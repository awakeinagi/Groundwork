---
id: DEC-0404
type: decision
title: "All printing scripts handle closed output pipes gracefully"
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-12
decided-by: awakeinagi
decided-on: 2026-07-12
source-span: "SES-0077 @ T12-T13"
overview: >-
  No script handled SIGPIPE, so piping any read command through an
  early-closing consumer produced a BrokenPipeError traceback, newly
  loud under the DEC-0388 direct-read charter, IDEA-0048's spark.
  Every printing script's entry point now catches BrokenPipeError,
  re-points stdout at the null device, and exits zero, applying to
  the read family primarily, plus search, graph, status,
  consistency, coupling, and the checker's report loop. Decided at
  SES-0077.
links:
  derives-from: [SES-0077]
  relates-to: [DEC-0388, DEC-0314, IDEA-0048]
---
# DEC-0404: All printing scripts handle closed output pipes gracefully

## Context

No script handled SIGPIPE, so piping any read command through an early-closing consumer produced a `BrokenPipeError` traceback — newly loud under the DEC-0388 direct-read charter, and the spark for IDEA-0048.

## Decision

Every printing script's entry point now catches `BrokenPipeError`, re-points stdout at the null device, and exits zero. This applies primarily to the read family, plus search, graph, status, consistency, coupling, and the checker's report loop.

## Rationale

Not separately recorded at distillation; the rationale is carried by the Context and Decision above and by the source session's transcript at the recorded source span (skeleton restored at SES-0077).

## Alternatives Considered

No alternatives were separately recorded at distillation (skeleton restored at SES-0077).

## Implications

No separate implications were recorded at distillation; the operative consequences are stated in the Decision (skeleton restored at SES-0077).
