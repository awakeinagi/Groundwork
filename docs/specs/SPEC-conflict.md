# SPEC: Conflict (CFL)

A first-class record of contradictory or competing requests — the artifact
form of Groundwork's core pain point. Conflicts block downstream generation
from every artifact they touch until resolved
(DEC-0005).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: conflict
status: open | mediating | escalated | resolved   # reduced lifecycle
escalated-to: <arbiter>            # required once status: escalated
links:
  relates-to: [BG-...., EP-....]   # ALL artifacts in tension (≥ 2 parties'
                                   # artifacts, or artifact vs. existing work)
```

Artifacts in tension link back with `conflicts-with: [CFL-....]` while the
conflict is unresolved; those links are removed at resolution.

## Required body sections

1. **The Tension** — what contradicts what, stated neutrally.
2. **Party Intents** — for each party, the underlying intent the agent
   uncovered through intent-first questioning (not just their stated
   position). This is what makes mediation and escalation informed.
3. **Mediation Record** — compromises and alternatives the agent proposed,
   and each party's response.
4. **Resolution** — filled at close: the outcome, citing the Decision(s)
   that resolved it and who ratified them.

## Lifecycle rules

- The agent's order of operations is fixed: understand each party's intent
  first → propose informed compromises (`mediating`) → escalate to the
  Arbiter with the full record only if mediation fails (`escalated`).
- `resolved` requires at least one `accepted` Decision that the resolution
  cites.
- While any linked Conflict is unresolved, the artifacts in tension cannot
  pass a gate and nothing new may be derived from them.
