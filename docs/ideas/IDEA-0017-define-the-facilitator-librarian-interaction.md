---
id: IDEA-0017
type: idea
title: "Define the facilitator/librarian interaction protocol explicitly"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  DEC-0324 and DEC-0331 fix the librarian's interaction shape at a
  high level (task-level intent in, distilled result out,
  statelessness), but no artifact specifies the protocol at contract
  granularity: what a well-formed task-intent prompt must contain,
  the standard report format's fields, how errors are distinguished
  from refusals, and what a caller may assume the librarian already
  knows. This session ran many librarian tasks by practice/example
  rather than written spec; a future session should formalize it,
  likely as part of the pending librarian Component Doc's
  conversational-patterns contract dimension. SES-0076's decisions
  DEC-0388..DEC-0393 now constrain this idea: any future protocol
  formalization must honor the targeted-read charter, the lock-
  serialized write model, the dependency rule, and the background-
  by-default interaction pattern.
links:
  derives-from: [SES-0061]
  relates-to: [DEC-0324, DEC-0331]
---

# IDEA-0017: Define the Facilitator/Librarian Interaction Protocol Explicitly

## The Idea

Verbatim: "We need to clearly define the interaction protocol between
the facilitator and the librarian. e.g. context passed, data passed,
etc."

## Spark Context

DEC-0324 fixes the shape at a high level (task-level intent in;
distilled result, verbatim on request, out) and DEC-0331 fixes
statelessness (everything the task needs travels in the prompt; every
task's memory-relevant lesson must reach the librarian's own memory
skill for anything to persist). But no artifact yet specifies the
protocol at contract granularity: what exactly a task-intent prompt
must contain to be well-formed (does it need explicit file paths,
prior context, expected output shape?), what the standard report
format's fields mean precisely (this session's transcripts show the
Answer/Operations/Refusals/Validation/Verbatim shape emerging by
practice, never specified), how errors versus refusals are
distinguished in the response, and what a caller may assume it does
NOT need to restate because the librarian already has it (e.g. project
root, which decisions govern which operations). This session ran many
librarian tasks somewhat improvisationally; a written protocol would
let any future facilitator (or a second concurrent one) use the
librarian correctly without re-deriving the shape from example.

## Disposition

Pending — awaiting take-up. Likely lands as part of the
artifact-librarian's own Component Doc contract backlog once the
pending epic (IDEA-0015) is derived — this is arguably the librarian's
"conversational patterns" contract dimension the system-architect
consultation already flagged as needing to be first-class for an
agent component.

SES-0076's decisions DEC-0388..DEC-0393 now constrain this idea: any future protocol formalization must honor the targeted-read charter, the lock-serialized write model, the dependency rule, and the background-by-default interaction pattern.

