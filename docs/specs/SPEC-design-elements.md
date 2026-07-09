# SPEC: Design Elements

The typed constituents of a Component Doc: the taxonomy, the contract
obligations each type carries, how elements are declared and identified,
when an element graduates to its own CMP, and the catalog of modeling
patterns. Referenced by [SPEC-component](SPEC-component.md)
(DEC-0086); this
spec is language-agnostic per
DEC-0018.

## The taxonomy

Exactly five element types
(DEC-0082).
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
(DEC-0088,
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
(DEC-0089): in
every API contract item, each request/response schema is either defined
inline (language-neutral form) or resolves to a declared **value** or
**event** element — in the same doc or in a `depends-on` component's
contract. Dangling type references are gate-blockers. Services stay
stateless (no D-kind); their payloads live in the A-items or in the
value/event elements those items reference.

## Declaration syntax and item IDs

(DEC-0087,
DEC-0081)

- Elements are declared **only** as level-3 headings inside a CMP's
  `## Design Elements` section: `### <ElementName> (<type>)`.
  `<ElementName>` is a glossary-resolved term in PascalCase; `<type>` is
  one of the five, lowercase. This heading is the single source of
  truth — there is **no** frontmatter mirror; machine consumers query
  element nodes via the Graph Index
  (DEC-0010).
- Directly under its heading, every element carries a mandated
  **`Implements:`** line listing, as resolvable markdown links, the
  story or stories whose implementation the element handles
  (DEC-0092). At
  least one story is required; a missing line, empty list, or
  unresolvable target is a gate-blocker. An element may only reference
  a story whose Component Impact section links this CMP
  (DEC-0094).
  Private helper values/events list the same stories as the element
  they support; a graduated seam CMP references the stories that
  birthed the seam. The Graph Index derives element→story `IMPLEMENTS`
  edges from these lines; story amendments propagate staleness to
  referencing CMPs with element-scoped impact reports
  (DEC-0096),
  and the design/implementation percent-complete metrics are computed
  over these edges
  (DEC-0095).
- Directly under the `Implements:` line, every element carries a
  mandated **`Uses:`** line (DEC-0299) declaring each dependency on
  another element as a named contract item with an edge-type
  qualifier from the closed set `interface | implementation | test`:
  `Uses: SchemaValidator.A-1 (interface), ItemBranch.B-2 (implementation)`
  — or `Uses: none`. Semantics: `(interface)` is contract-only and
  non-serializing (the consumer builds against stubs generated from
  the referenced items, which ship in its work-package bundle; the
  default when omitted); `(implementation)` requires the built
  artifact and is the only qualifier constraining build-order;
  `(test)` is needed only at test execution and must target an owned
  test-double element (DEC-0306 — a test double is an element of the
  component owning the contract it fakes, promoted from Notes on
  first `(test)` reference). Unresolvable targets or unknown
  qualifiers are gate-blockers. A component's frontmatter
  `depends-on` must equal the exact projection of its members'
  cross-component `Uses:` targets, and the lifted component edge is
  typed strongest-member-wins, `implementation > interface > test`
  (DEC-0309); the checker enforces the projection in both directions.
  The element's atomicity — terminal, dependencies declared and
  typed, obligations complete — is verified at gate time per
  DEC-0303 (DEC-0136 checklist extension plus the mechanical
  bundle-closure check).
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
  (DEC-0011).

## Seam graduation

(DEC-0080)

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

(DEC-0084)

Common constructs are modeled as **compositions** of the five types —
never as new types. Each pattern names the sub-elements required so the
composition stays independently buildable-and-testable
(DEC-0011).
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
