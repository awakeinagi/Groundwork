# SPEC: Business Goal (BG)

The foundational statement of a refined business intent — the root of the
traceability graph. Produced by synthesizing one or more refinement Sessions
with Stakeholders; approved by a Product Owner (or committee, per Gate Policy).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: business-goal
sponsor: <named stakeholder who owns the intent>
links:
  derives-from: [SES-....]   # the session(s) this goal was synthesized from
```

## Required body sections

1. **Problem** — the pain or opportunity, in the sponsor's terms, free of
   solution language.
2. **Intent** — what the business wants to be true afterward, and why now.
3. **Outcomes & Success Criteria** — observable, ideally measurable results
   that would demonstrate the goal is met. Each criterion cites the Decision
   that established it.
4. **Scope** — explicitly in and explicitly out. If the goal's work is
   release-scoped, this section also declares the named releases as a
   machine-parseable list
   ([DEC-0099](../decisions/DEC-0099-releases-declared-in-goal-scope.md)):
   one item per release, the value in a code span (a SemVer prefix per
   [DEC-0098](../decisions/DEC-0098-semver-release-labels.md)), the
   current release marked `(current)`:

   ```markdown
   **Releases:**
   - `1` (current) — goal refinement end-to-end
   - `2` — connectors-led expansion
   ```

   `release:` labels in descendant stories/epics/spikes must exactly
   match a declared value (or be `backlog`); adding, renaming, or
   re-scoping a release is a gated amendment to this goal. Any such
   amendment must review the [trigger registry](../TRIGGERS.md) — has an
   armed condition been met?
   ([DEC-0108](../decisions/DEC-0108-trigger-surfacing.md)).
5. **Constraints** — non-negotiables: regulatory, technical, budget, timeline,
   organizational.
6. **Stakeholders & Roles** — who cares, who answers questions, who approves.
7. **Conflicts & Tensions** — known tensions with other goals or existing
   work, each linked to its `CFL` artifact (or "None identified").
8. **Derived Work** — the Epics derived from this goal (maintained as they
   are created).

## Rules

- A Business Goal must be `approved` before any Epic may be derived from it.
- Solution design does not belong here; if a Session produced solution-level
  decisions, they attach to the Epics/Components that implement them.
- When a goal changes after approval, Impact Analysis runs over its subtree
  and descendants are marked `stale`
  ([DEC-0007](../decisions/DEC-0007-impact-analysis-stale-marks.md)).
