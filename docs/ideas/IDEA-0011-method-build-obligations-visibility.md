---
id: IDEA-0011
type: idea
title: Surface ratified-but-unbuilt method tooling in the status report and work queue
status: taken-up
owner: awakeinagi@gmail.com
created: 2026-07-09
proposed-by: awakeinagi
overview: >-
  Captured mid-SES-0058 after the stakeholder asked why the
  artifact-interact skill decided in SES-0057 (DEC-0322 mandated its
  build) was never built: "decided, not yet built" was a legitimate
  state for method tooling, but nothing tracked it — the status
  report's work queue showed drafts, gated artifacts, conflicts,
  change proposals, and Ideas, while a ratified method-level build
  obligation appeared nowhere. Taken up at SES-0059 (DEC-0344):
  resolved structurally by the BG-0002 method track — method work
  now lives in the artifact tree, so obligations surface in the
  status report natively, and BG-0002 carries the residual nothing-
  ratified-stays-invisibly-unbuilt criterion. Status: taken-up.
links:
  derives-from: [SES-0058]
---

# IDEA-0011: Surface Ratified-but-Unbuilt Method Tooling

## The Idea

Verbatim: "Why didn't we create the artifact-interact skill in the
previous session? That seems like a surfaced gap in our
design-session workflow."

Facilitator restatement (aligned in-session): ratified
method-tooling build obligations (like DEC-0322's) are invisible to
the status report and work queue; the process needs them surfaced.

## Spark Context

Raised mid-SES-0058, immediately after the facilitator's locate-first
pass discovered that the artifact-interact skill decided in SES-0057
had never been built — a fact no process surface tracked. SES-0057
closed correctly by its own rules (sessions produce decisions;
DEC-0322 deferred construction to a skill-creator build loop), but
nothing queued the build or would have reminded a future session of
it.

## Disposition

Taken up at SES-0059 (DEC-0344). The fix is structural: method work now lives in the artifact tree under BG-0002, so build obligations surface in the status report and frontier natively; BG-0002 outcome 4 carries the residual guarantee that nothing ratified stays invisibly unbuilt. The immediate instance (the unbuilt artifact-interact skill) was built at SES-0058.

