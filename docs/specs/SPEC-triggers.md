# SPEC: Trigger Registry

The tracked file of watched conditions that revive deferred work or
start new work when the world changes. Established by
[DEC-0106](../decisions/DEC-0106-trigger-registry.md); firing semantics
per [DEC-0107](../decisions/DEC-0107-trigger-firing-cites-decision.md);
surfacing and validation per
[DEC-0108](../decisions/DEC-0108-trigger-surfacing.md).

The registry is **not an artifact**: one file, `docs/TRIGGERS.md`, no
YAML frontmatter, no artifact ID. `TRG-` IDs are registry-scoped —
sequential, 4-digit, never reused.

## Entry format

Strict and regex-extractable, so tooling can pull entries into agent
context cheaply:

```markdown
## TRG-0001 (armed)
**Condition:** <observable, human-testable statement>
**Consequence:** <action> <markdown-linked target artifact(s)>
**Cites:** <markdown link to the decision that armed this trigger>
```

- Heading grammar: `## TRG-<4 digits> (armed|fired|retired)`.
- `**Condition:**` — phrased so a human can decide "does this hold
  today?"; no vague aspirations.
- `**Consequence:**` — what happens on firing: revive a deferred
  artifact, derive a new spike from a named parent, or open a session on
  a named artifact. Targets are resolvable markdown links.
- `**Cites:**` — the decision that armed the trigger.
- A `fired` entry adds `**Fired:**` with the date, a markdown link to
  the firing decision, and the outcome; a `retired` entry adds
  `**Retired:**` likewise. Entries are never deleted — fired and retired
  entries are the registry's history.

## Semantics

- **Armed** — the condition is being watched. Tooling that loads
  triggers into agent context loads **armed entries only**.
- **Fired** — the condition was observed to hold, recorded by a decision
  ([DEC-0107](../decisions/DEC-0107-trigger-firing-cites-decision.md));
  the consequence executed citing that decision. When the consequence is
  a revival, the same decision satisfies
  [DEC-0100](../decisions/DEC-0100-scope-moves-cite-decisions.md) — one
  decision, no double ceremony.
- **Retired** — the condition is no longer worth watching; also
  decision-cited.

## Surfacing

- The status report lists armed triggers (ID, target, condition) next to
  the Deferred section.
- A release-declaration amendment to a Business Goal reviews the
  registry ([SPEC-business-goal](SPEC-business-goal.md)).

## Validation (enforced by `tools/check_links.py`)

1. Every `## TRG-` heading matches the grammar; statuses are from the
   closed set.
2. `TRG-` IDs are unique.
3. Armed entries carry `**Condition:**`, `**Consequence:**`, and
   `**Cites:**` lines; fired/retired entries additionally carry their
   `**Fired:**`/`**Retired:**` line containing at least one markdown
   link (the firing/retiring decision).
4. All relative markdown links in the registry resolve.
