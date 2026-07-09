# SPEC: Trigger Registry

The tracked file of watched conditions with subscribed deferred items,
revived when a condition fires. Established by
DEC-0106, reshaped with
subscriptions by
DEC-0109; firing
semantics per
DEC-0107;
lifecycle invariants per
DEC-0110; surfacing
and validation per DEC-0108.

The registry is **not an artifact**: one file, `docs/TRIGGERS.md`, no
YAML frontmatter, no artifact ID. `TRG-` IDs are registry-scoped —
sequential, 4-digit, never reused. Entries are never deleted; fired and
retired entries are the registry's history.

## Entry format

Strict and regex-extractable, so tooling can pull entries into agent
context cheaply:

```markdown
## TRG-0001 (armed)
**Condition:** <observable, human-testable statement>
**Subscribers:**
- <action> <markdown-linked target> (per <markdown-linked DEC>)
- <action> <markdown-linked target> (per <markdown-linked DEC>)
**Cites:** <markdown link to the decision that armed this trigger>
```

- Heading grammar: `## TRG-<4 digits> (armed|fired|retired)`.
- `**Condition:**` — phrased so a human can decide "does this hold
  today?"; no vague aspirations.
- `**Subscribers:**` — one line per subscription: an action verb
  (`revive …`, `derive a spike from …`, `open a session on …`), the
  resolvable markdown-linked target, and the subscription's own decision
  citation `(per [DEC-nnnn](…))`. The entry-level `**Cites:**` records
  who armed the trigger; each subscriber line records who subscribed
  that item — a later decision may add a subscriber to an existing
  trigger, individually attributable.
- A `fired` entry adds `**Fired:**` with the date, a markdown link to
  the firing decision, and the outcome; a `retired` entry adds
  `**Retired:**` likewise.

## Semantics

- **Armed** — the condition is being watched. Tooling that loads
  triggers into agent context loads **armed entries only**.
- **Fired** — the condition was observed to hold, recorded by a decision
  (DEC-0107).
  **A firing revives all subscribers** — the condition holding is a fact
  about the world, not about one item; each consequence executes citing
  the one firing decision, which also satisfies
  DEC-0100 for
  each revival.
- **Retired** — the condition is no longer worth watching;
  decision-cited.

## Lifecycle invariants (DEC-0110)

1. An armed trigger's subscribers are all currently `deferred`
   artifacts, and there is at least one — checker-enforced, which makes
   the unsubscribe rule impossible to forget silently.
2. When an item leaves `deferred` (a firing, or a direct decision-cited
   revival), its subscriber lines are removed from **all other armed
   triggers** in the same change, covered by the same reviving decision.
   A revived item cannot be revived again.
3. An armed trigger emptied by unsubscription **auto-retires**, citing
   the same reviving decision in its `**Retired:**` line. A condition
   that matters again later gets a new TRG entry.

## Surfacing

- The status report lists armed triggers (ID, subscribers, condition)
  next to the Deferred section.
- A release-declaration amendment to a Business Goal reviews the
  registry ([SPEC-business-goal](SPEC-business-goal.md)).

## Validation (enforced by `tools/check_links.py`)

1. Every `## TRG-` heading matches the grammar; statuses are from the
   closed set; `TRG-` IDs are unique.
2. Armed entries carry `**Condition:**`, `**Subscribers:**` (with ≥1
   well-formed subscriber line), and `**Cites:**`; fired/retired entries
   additionally carry their `**Fired:**`/`**Retired:**` line containing
   at least one markdown link (the firing/retiring decision).
3. Every subscriber line has a resolvable target and a `(per …)`
   decision citation; on **armed** entries the target artifact's status
   is `deferred` (fired/retired entries keep their lines as history,
   exempt).
4. All relative markdown links in the registry resolve.
