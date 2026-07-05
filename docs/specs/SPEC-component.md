# SPEC: Component Doc (CMP)

The contract-complete specification of one system component, aligned with a
DDD-style bounded context. This is the artifact handed to the Implementation
Swarm: an implementer holding this doc plus the interface contracts of its
dependencies (not their internals) can implement and test the component
([DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: component
context: <bounded context name>     # glossary-resolved
links:
  derives-from: [EP-....]           # or ST-.... when a story births it
  satisfies: [BG-....]
  depends-on: [CMP-....]            # dependency components (contracts only)
```

Component Docs get **no Jira issue**; the stories that build them are the
trackable units ([DEC-0013](../decisions/DEC-0013-jira-summary-plus-link.md)).

## Required body sections

1. **Purpose** — what this component is for, tied to the goals it satisfies.
2. **Ubiquitous Language** — the glossary terms this component's model uses;
   any term not in CONTEXT.md must be resolved there first.
3. **Behavior Contract** — itemized, numbered behavioral guarantees
   (invariants, state transitions, side effects, failure behavior). Each item
   cites its Decision(s): `(per DEC-....)`.
4. **API Contract** — every exposed operation: signature, request/response
   schemas, error taxonomy, idempotency and ordering guarantees. Schemas in a
   language-neutral form (JSON Schema / OpenAPI fragments).
5. **Data Contract** — owned entities, their schemas, lifecycle, retention;
   what is persisted vs. derived.
6. **Dependencies** — for each `depends-on` component: which of its contract
   sections are consumed, pinned to the dependency's approved version
   (git ref). Internals of dependencies are out of bounds.
7. **Acceptance & Test Expectations** — what a passing implementation must
   demonstrate; contract tests to be produced.
8. **Out of Scope** — explicitly excluded behavior, especially plausible
   adjacent behavior an implementer might assume.

## Rules

- Contract-completeness is the standard; crawlable cross-references (to
  Decisions, Sessions, ancestor docs) are the sanctioned fallback when an
  implementer needs more context — ideally never necessary, iteratively
  improved when it proves necessary
  ([DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).
- Every Behavior/API/Data contract item must cite at least one Decision;
  uncited items are gate-blockers.
- Approved Component Docs are the inputs to the Handoff Manifest
  ([SPEC-handoff-manifest](SPEC-handoff-manifest.md)).
