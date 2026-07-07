# SPEC: Design Elements

The typed constituents of a Component Doc: the taxonomy, the contract
obligations each type carries, how elements are declared and identified,
when an element graduates to its own CMP, and the catalog of modeling
patterns. Referenced by [SPEC-component](SPEC-component.md)
([DEC-0086](../decisions/DEC-0086-design-elements-spec-home.md)); this
spec is language-agnostic per
[DEC-0018](../decisions/DEC-0018-python-backend-language-agnostic-specs.md).

## The taxonomy

Exactly five element types
([DEC-0082](../decisions/DEC-0082-closed-element-type-taxonomy.md)).
The set is **closed**: adding a type requires a refinement session, an
accepted Decision, and a change to this spec. Ad-hoc types are tier-1
validation failures.

- **entity** — a domain concept with persistent identity, lifecycle, and
  mutable state; identity survives state changes.
- **value** — an immutable, attribute-defined item; equality by value;
  no identity, no lifecycle.
- **service** — a stateless capability exposing operations; any state it
  touches is owned by entities/values or external stores it contracts
  for.
- **event** — a schema'd payload that crosses a boundary, with defined
  emission, ordering, and delivery semantics.
- **protocol** — a capability seam: the contract an implementation must
  satisfy, defined independently of any implementation.

Reference-stack mappings (illustrative, **non-normative**): entity → a
Python class with identity; value → frozen dataclass / frozen pydantic
model; service → function or class with methods; event → pydantic model
/ TypedDict; protocol → `typing.Protocol`.

## Typed contract obligations

An element's type determines which contract kinds its block must define
([DEC-0088](../decisions/DEC-0088-revised-typed-obligations.md),
superseding DEC-0083). Missing mandated kinds are gate-blockers, checked
per element by the tier-2 suite (ST-0007).

| Type | Mandatory contract kinds | Conditional |
|---|---|---|
| entity | behavior contract: identity semantics, lifecycle states, allowed transitions, domain-operation semantics (B); data contract (D) | API contract (A) — required exactly when the entity's operations are exposed at the component boundary (e.g., a graduated standalone entity CMP) |
| value | data contract: schema, equality/immutability invariants (D) | — |
| service | API contract (A), behavior contract (B) | — |
| event | schema (D), emission/ordering/delivery semantics (B) | — |
| protocol | API contract implementations must satisfy (A), conformance expectations (B) | — |

**Schema-resolution rule**
([DEC-0089](../decisions/DEC-0089-api-schema-resolution-rule.md)): in
every API contract item, each request/response schema is either defined
inline (language-neutral form) or resolves to a declared **value** or
**event** element — in the same doc or in a `depends-on` component's
contract. Dangling type references are gate-blockers. Services stay
stateless (no D-kind); their payloads live in the A-items or in the
value/event elements those items reference.

## Declaration syntax and item IDs

([DEC-0087](../decisions/DEC-0087-parseable-element-headings.md),
[DEC-0081](../decisions/DEC-0081-element-first-contract-layout.md))

- Elements are declared **only** as level-3 headings inside a CMP's
  `## Design Elements` section: `### <ElementName> (<type>)`.
  `<ElementName>` is a glossary-resolved term in PascalCase; `<type>` is
  one of the five, lowercase. This heading is the single source of
  truth — there is **no** frontmatter mirror; machine consumers query
  element nodes via the Graph Index
  ([DEC-0010](../decisions/DEC-0010-graph-index-derived.md)).
- Contract items are element-scoped:
  `<ElementName>.<K>-<n>` where `K` ∈ `B` (behavior), `A` (API),
  `D` (data), numbered sequentially per element and kind
  (e.g. `StorageService.B-3`, `ArtifactId.D-1`).
- Component-level cross-element guarantees live in
  `## Component Invariants` as `C-<n>` items; reference-implementation
  constraints live in Implementation Guidance as `IG-<n>` items (see
  [SPEC-component](SPEC-component.md)).
- Item IDs are unique within their doc. Cross-document references name
  the doc: `CMP-0001 § StorageService.B-3`.
- Every contract item cites at least one Decision, exactly as before
  ([DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).

## Seam graduation

([DEC-0080](../decisions/DEC-0080-hybrid-component-granularity.md))

By default elements live nested inside their bounded-context CMP. An
element **graduates** to its own standalone CMP when it is a seam
between components:

- it is consumed by more than one CMP, **or**
- it requires independently versioned conformance (its own contract
  tests and release cadence).

A standalone element CMP declares its type in frontmatter
(`component-type: <type>`, see [SPEC-component](SPEC-component.md)), and
its Design Elements section contains that single element's contract
block (plus any private helper values/events it owns). Typical
graduates: cross-component protocols (e.g. the code-host connector
contract), shared event schemas, shared value kernels.

## Modeling patterns catalog

([DEC-0084](../decisions/DEC-0084-modeling-patterns-catalog.md))

Common constructs are modeled as **compositions** of the five types —
never as new types. Each pattern names the sub-elements required so the
composition stays independently buildable-and-testable
([DEC-0011](../decisions/DEC-0011-contract-complete-component-docs.md)).
Guidance for authors, not additional gate rules. The catalog grows by
mechanical spec edit as constructs recur.

### Repository / Store

A persistence seam. Model as a **protocol** defining the access
contract (operations, consistency and transactionality guarantees) plus
the **entity**/**value** types it stores. The backing technology is an
Implementation Guidance concern, never part of the protocol.
Required sub-elements: the access protocol (with conformance
expectations any backend must pass) and the stored entity/value schemas.

### Workflow / Process (saga)

Long-running, multi-step orchestration. Model as a **service** whose
behavior contract is an explicit state machine (states, transitions,
timeout and compensation/failure behavior), plus **event** elements for
what it emits/consumes, plus — when instances must be addressable — an
**entity** for the process instance (identity = process ID).
Required sub-elements: the state-machine behavior contract, the event
schemas with ordering semantics, failure/timeout transitions.

### Policy / Rule

Declarative, configuration-driven rules (e.g. gate policies, decision
rights). Model as a **value** carrying the rule's schema'd declarative
representation, plus the **service** that evaluates it (evaluation
semantics, precedence, behavior on conflicting or missing rules).
Required sub-elements: the rule-representation value schema and the
evaluator's behavior contract with worked evaluation examples.
