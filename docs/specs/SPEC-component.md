# SPEC: Component Doc (CMP)

The contract-complete specification of one system component, aligned with a
DDD-style bounded context. This is the artifact handed to the Implementation
Swarm: an implementer holding this doc plus the interface contracts of its
dependencies (not their internals) can implement and test the component
(DEC-0011).

A component comprises typed **design elements** (entity, value, service,
event, protocol) declared and contracted per
[SPEC-design-elements](SPEC-design-elements.md). By default a CMP is
bounded-context-scale with elements nested inside; a seam element
graduates to its own standalone CMP per the graduation rule
(DEC-0080).

Extends [SPEC-artifact-common](SPEC-artifact-common.md).

## Frontmatter additions

```yaml
type: component
context: <bounded context name>     # glossary-resolved
component-type: protocol            # ONLY on standalone element CMPs
                                    # (graduated seams); one of:
                                    # entity | value | service | event |
                                    # protocol. Absent on composite
                                    # bounded-context CMPs.
links:
  derives-from: [EP-....]           # or ST-.... when a story births it
  satisfies: [BG-....]
  depends-on: [CMP-....]            # dependency components (contracts only)
```

Component Docs get **no Jira issue**; the stories that build them are the
trackable units (DEC-0013).

## Required body sections

1. **Purpose** — what this component is for, tied to the goals it satisfies.
2. **Ubiquitous Language** — the glossary terms this component's model uses;
   any term not in CONTEXT.md must be resolved there first.
3. **Design Elements** — the component's typed elements, each declared as
   `### <ElementName> (<type>)` and carrying its own contract block with
   element-scoped item IDs (`<ElementName>.<B|A|D>-<n>`), per
   [SPEC-design-elements](SPEC-design-elements.md)
   (DEC-0081,
   DEC-0087).
   Each element declares the stories it implements on a mandated
   `Implements:` line directly under its heading
   (DEC-0092).
   Each element's type mandates its contract kinds
   (DEC-0088);
   schemas in language-neutral form (JSON Schema / OpenAPI fragments),
   with API-item schemas resolving inline or to declared value/event
   elements (DEC-0089).
4. **Component Invariants** — cross-element guarantees, numbered `C-<n>`
   (e.g. transactional couplings between elements, whole-component
   failure behavior).
5. **Implementation Guidance**
   (DEC-0085) —
   two subsections:
   - **Constraints** — numbered `IG-<n>`, normative for the reference
     implementation, each citing its Decision(s); the binding home for
     refinement-made stack commitments (e.g. a spike-chosen store).
   - **Notes** — advisory, may be stack-specific, never gate-checked and
     never load-bearing: the contract sections must remain sufficient
     without them
     (DEC-0018).
6. **Dependencies** — for each `depends-on` component: which of its contract
   sections/items are consumed, pinned to the dependency's approved version
   (git ref). Internals of dependencies are out of bounds.
7. **Acceptance & Test Expectations** — what a passing implementation must
   demonstrate; contract tests to be produced. For `protocol`-type
   standalone CMPs this includes the conformance suite any implementation
   must pass.
8. **Out of Scope** — explicitly excluded behavior, especially plausible
   adjacent behavior an implementer might assume. The differentiated
   entry rule of
   DEC-0133
   applies: future-work entries must exist as (and link) deferred
   stories/spikes; boundary statements link the owning artifact where
   one exists and never mint deferred artifacts.

## Rules

- **Graduation review (required before gating)**: every design element
  is checked against the graduation rule of
  DEC-0080 —
  consumed by more than one CMP (actual or contract-certain), or
  needing independently versioned conformance — and the outcome is
  recorded in the gating session
  (DEC-0136).
- Contract-completeness is the standard; crawlable cross-references (to
  Decisions, Sessions, ancestor docs) are the sanctioned fallback when an
  implementer needs more context — ideally never necessary, iteratively
  improved when it proves necessary
  (DEC-0011).
- Every contract item — element items, Component Invariants, and
  Implementation Guidance Constraints — must cite at least one Decision;
  uncited items are gate-blockers. Implementation Guidance Notes are
  exempt.
- Every element carries an `Implements:` line naming ≥1 story, resolvable
  and consistent with each named story's Component Impact
  (DEC-0092,
  DEC-0094);
  a CMP cannot pass its gate while a story whose Component Impact names
  it has no referencing element
  (DEC-0093).
  Amendment or supersession of a referenced story marks this CMP stale,
  with the impact report scoped to the referencing elements
  (DEC-0096).
- Element headings, types, typed obligations, and item-ID well-formedness
  are validated at the gate (tier-2 suite, ST-0007); the element-type
  enum and `component-type` field are tier-1 schema-validated (ST-0001).
- Approved Component Docs are the inputs to the Handoff Manifest
  ([SPEC-handoff-manifest](SPEC-handoff-manifest.md)).
