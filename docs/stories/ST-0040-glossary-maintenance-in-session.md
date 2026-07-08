---
id: ST-0040
type: story
title: Glossary maintenance in-session
status: approved
owner: ds-lead
approved-by: awakeinagi@gmail.com
approved-on: 2026-07-08
created: 2026-07-08
links:
  derives-from: [EP-0002]
  satisfies: [BG-0001]
  depends-on: [ST-0032, ST-0033]
  impacts: []
  impacted-by: [ST-0032, ST-0033]
cites: [DEC-0012, DEC-0056]
---

# ST-0040: Glossary Maintenance In-Session

## Summary

Every refinement session doubles as domain modeling: the agent
challenges vague or overloaded terms as they surface, proposes precise
canonical terms, and writes the resolved definition into `CONTEXT.md` the
moment it crystallizes — never batched, never deferred to a separate
exercise.

## Acceptance Criteria

1. When a participant uses a vague or overloaded term, the agent proposes
   a precise canonical term and confirms it with the participant before
   treating it as resolved
   (per [DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)).
2. When a term conflicts with an existing `CONTEXT.md` entry, the agent
   surfaces the conflict explicitly rather than silently picking one
   meaning
   (per [DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)).
3. The moment a term resolves, the agent writes the `CONTEXT.md` entry in
   the same session — never batched to session end or a separate pass
   (per [DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)).
4. Glossary entries are definitions only, with no implementation detail
   or spec content, and are gated the same as any other artifact change
   (per [DEC-0012](../decisions/DEC-0012-agent-built-domain-model.md)).
5. The engine surfaces the current `CONTEXT.md` to every strategy pack's
   context recipe by default, so term-challenge behavior has the existing
   glossary available regardless of which pack is running
   (per [DEC-0056](../decisions/DEC-0056-context-recipes-in-packs.md)).

## Component Impact

None yet — a Component Doc for this epic's bounded context is stubbed once the first story here refines toward it.

## Out of Scope

Bounded-context boundary decisions that emerge from glossary terms
(a judgment call made across sessions, not a mechanical rule this story
enforces); `CONTEXT.md`'s gating mechanics as a file
([EP-0001](../epics/EP-0001-artifact-store-and-format-engine.md) /
[EP-0003](../epics/EP-0003-governance-and-gate-engine.md) own gate
machinery generally).

## Notes for Implementers

Criterion 5's "surfaced by default" is a floor, not the full context
recipe — [ST-0038](ST-0038-context-assembly-via-pack-recipes.md) owns
what else a given pack's recipe pulls in.
