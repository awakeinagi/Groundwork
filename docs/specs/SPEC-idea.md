# SPEC: Idea (IDEA)

A pre-classification capture of raw change intent — too raw to know
which artifact level (goal, epic, story, spike, component) it lands at
(DEC-0258, DEC-0259). Captured verbatim in seconds so the thought
survives the moment; it joins the project's work queue until an intake
session takes it up or it is declined with rationale (DEC-0261).
Reflected in the application per DEC-0268 and DEC-0269.

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: idea
proposed-by: <person-id>       # required
links:
  derives-from: [SES-....]     # the spawning session, when there is one
  relates-to: []               # artifacts the idea appears to touch
```

## Lifecycle

`captured → taken-up | declined`. Ideas never use the common
gate lifecycle: they pass no gates, and nothing derives from them
except their take-up intake session. Terminal states persist; Ideas
are never deleted. Tier-1 rejections: any `release:` field, any
gate-lifecycle status value, a missing `proposed-by`.

## Required body sections

1. **The Idea** — the proposer's words, verbatim; not a refinement.
2. **Spark Context** — where and when it arose (mid-session park via
   the focus-artifact test, brain-dump, review thought).
3. **Disposition** — `Pending.` while captured; at take-up, names the
   intake session (status `taken-up`); at decline, the rationale and
   decider (status `declined`).

## Rules

- An Idea captures intent whose artifact level is *unknown*; intent
  whose level is already clear is captured as a deferred story/spike
  instead (DEC-0259). Ideas never carry `release:` labels or trigger
  subscriptions.
- The spawning session cross-references every Idea it produces
  (`relates-to` + body mention); the take-up session lists the Idea in
  `derives-from`. Both are tier-2/PR checks, not tier-1 (DEC-0269) —
  the referencing edit may land later in the same branch.
- A declined Idea's Disposition must contain the rationale — tier-2.
- Captured Ideas surface in work-queue reads alongside untriaged CPs
  (DEC-0261, DEC-0270).
