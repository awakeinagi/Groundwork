---
id: DEC-0109
type: decision
title: Trigger entries hold decision-cited subscriber lists; a firing revives all subscribers
status: accepted
owner: awakeinagi@gmail.com
created: 2026-07-07
overview: >-
  Supersedes DEC-0106, restating the registry with subscriptions. Each trigger
  entry holds a Subscribers list (one line per subscription: action verb,
  linked target, and subscription's decision citation). A firing revives all
  subscribers; the condition holding is a world fact, not specific to one item.
  Late subscriptions stay individually attributable. One condition, many
  watchers, with per-subscription provenance keeping "why is this watching
  this?" answerable per line.
decided-by: awakeinagi@gmail.com
decided-on: 2026-07-07
source-span: "SES-0018 @ T1-T3"
links:
  derives-from: [SES-0018]
  supersedes: [DEC-0106]
  relates-to: [DEC-0107, DEC-0110]
---

# DEC-0109: Trigger Subscriptions

## Context

DEC-0106 gave each trigger one
`**Consequence:**` line. That duplicates conditions when several items
share one (each would need its own trigger) and leaves no structure for
removing a single item's subscription when it revives.

## Decision

Supersedes DEC-0106, restating the
registry with subscriptions. `docs/TRIGGERS.md` is unchanged in
location, ID discipline, statuses, armed-only context loading, and
never-delete history. The entry format becomes:

```markdown
## TRG-0001 (armed)
**Condition:** <observable, human-testable statement>
**Subscribers:**
- <action> <markdown-linked target> (per <markdown-linked DEC>)
**Cites:** <markdown link to the decision that armed the trigger>
```

- One line per subscription: an action verb (`revive …`, `derive a
  spike from …`, `open a session on …`), the linked target, and the
  **subscription's own decision citation** — the entry-level
  `**Cites:**` records who armed the trigger; each subscriber line
  records who subscribed that item, so late subscriptions (a different
  decision, months later) stay individually attributable.
- **A firing revives all subscribers.** The condition holding is a fact
  about the world, not about one item; each consequence executes citing
  the one firing decision
  (DEC-0107 unchanged).
- Fired/retired entries keep their subscriber lines as history.

## Rationale

One condition, many watchers — the participant's requirement — with
per-subscription provenance so "why is this item watching this
condition?" is answerable per line, matching the acceptance-criteria
citation idiom used everywhere else. Line-regular subscriptions make
unsubscription a one-line deletion the checker can reason about.

## Alternatives Considered

- **One prose Consequence naming several targets**: no format change,
  but unsubscription means editing prose and the checker can't tell
  targets from incidental links.
- **Fire per subscriber**: more control, but an armed trigger whose
  condition already held is a contradiction, and it hides scope creep
  in the registry.
- **Entry-level Cites only**: loses attribution the moment a second
  decision subscribes a second item.

## Implications

[SPEC-triggers](../specs/SPEC-triggers.md) is rewritten; the existing
`TRG-0001`–`TRG-0004` entries convert to the new format (subscriber:
SP-0002, per
DEC-0105); checker and status
tooling parse subscriber lines. Lifecycle invariants are
DEC-0110.
