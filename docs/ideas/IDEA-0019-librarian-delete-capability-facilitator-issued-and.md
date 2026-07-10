---
id: IDEA-0019
type: idea
title: "Librarian delete capability, facilitator-issued and bookkept"
status: captured
owner: awakeinagi@gmail.com
created: 2026-07-10
proposed-by: awakeinagi
overview: >-
  The write API deliberately has no delete operation (IDs are never
  reused, even after deletion, per SPEC-artifact-common). This
  session hit the adjacent problem twice — mistaken draft files
  needing removal before never having been committed — handled by
  the facilitator deleting untracked files directly, never the
  librarian. The stakeholder's proposal generalizes this into a
  real, facilitator-authorized, bookkept delete capability. Open
  questions for take-up: whether deletion applies only to never-
  committed drafts or to committed/historical artifacts (which
  collides with immutability rules), the bookkeeping record's own
  shape, and that this is itself DEC-0335-governed build work
  needing a presented design first.
links:
  derives-from: [SES-0061]
  relates-to: [DEC-0312, DEC-0330, DEC-0335, DEC-0333]
---

# IDEA-0019: Librarian Delete Capability, Facilitator-Issued and Bookkept

## The Idea

Verbatim: "Librarian needs the ability to delete files. Facilitator
should be the one to issue the delete order and we need bookkeeping
around these delete orders."

## Spark Context

The current write API (DEC-0313's roster) deliberately has no delete
operation — SPEC-artifact-common's integrity rules say IDs are
sequential per prefix and never reused, even after deletion, which is
a corpus-wide invariant a careless delete could violate silently (a
deleted artifact's ID must never be reissued; anything that cited it
becomes a dangling reference unless handled). This session hit the
adjacent problem twice — mistakenly-created, never-committed draft
files that needed removing before retrying — and resolved it each time
by having the facilitator delete the untracked files directly (a
one-off, git-status-verified, "nothing was ever committed" case), with
the librarian never touching git or performing the deletion itself.
The stakeholder's proposal generalizes this: a real delete capability
in the librarian's hands, but gated by the facilitator issuing the
order (an authority split, not a technical one — parallels DEC-0330's
refuse-and-report pattern, where the librarian executes but doesn't
originate process-level choices) with bookkeeping (what was deleted,
why, when, by whose order) so a delete is never silent or
unaccountable the way this session's untracked-file cleanups were
merely because nothing had reached git yet.

## Disposition

Pending — awaiting take-up. Real design questions: does "delete"
apply only to never-committed drafts (safe, narrow) or to committed,
historical artifacts (much higher stakes — collides with "sessions are
append-only" and "accepted decisions are immutable"); what the
bookkeeping record's own artifact shape is (a decision? a dedicated
log?); and how this interacts with IDEA-0019's own existence — a
delete operation is exactly the kind of build DEC-0335 governs, so
take-up must include a presented design and test plan before any
implementation.
