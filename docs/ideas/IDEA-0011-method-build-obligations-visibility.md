---
id: IDEA-0011
type: idea
title: Surface ratified-but-unbuilt method tooling in the status report and work queue
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-09
proposed-by: awakeinagi
overview: >-
  Captured mid-SES-0058 after the stakeholder asked why the
  artifact-interact skill decided in SES-0057 (DEC-0322 mandated its
  build) was never built: "decided, not yet built" is a legitimate
  state for method tooling, but nothing tracks it — the status
  report's work queue shows drafts, gated artifacts, conflicts,
  change proposals, and Ideas, while a ratified method-level build
  obligation appears nowhere. The facilitator only discovered the
  unbuilt skill by inspecting .claude/skills/ directly. The gap:
  method-tooling build obligations need a visible home in the status
  report / work queue so a session that ratifies a build also leaves
  a trail the next session start surfaces. Facilitator restatement
  aligned with the stakeholder in-session. Disposition pending —
  partially mitigated for the current instance by SES-0058's own
  build-before-commit execution, but the systemic tracking gap
  remains.
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

Pending — awaiting take-up via the change-intake protocol as its own
session. The immediate instance is being handled inside SES-0058's
build-before-commit execution; the systemic fix (status-report /
work-queue visibility for method build obligations) is this Idea.
