# Interface and Contract Design

**When to reach for this:** Use at story and component refinement, when a component's externally visible surface — operations, payloads, events, error behavior, versioning and deprecation policy — is being specified, and pre-gate when checking a component doc claims to be "contract-complete." It covers what a complete contract contains, how contracts stay evolvable without breaking consumers, what counts as a breaking change, and the checklist a reviewer should run before graduating a contract.

Constructed: 2026-07-09

---

## 1. What a contract actually includes

A provider contract is more than a schema. Its composition spans ([Robinson, Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html)):

- **Document schemas** (payload structure and types)
- **Operation interfaces** (what can be invoked)
- **Conversational patterns** (message-exchange sequences — order and statefulness of interactions)
- **Policy** (security requirements, transactional context)
- **Quality of service** (availability, latency, throughput expectations)

A component doc that specifies only endpoints and fields has covered one of five contract dimensions — flag the gap. QoS expectations belong in the contract as SLO-style targets (see the quality-attributes reference; [Google SRE, Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)).

## 2. Three kinds of contract, and who holds the pen

Robinson's taxonomy ([Consumer-Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html)):

| | Provider contract | Consumer contract | Consumer-driven contract |
|---|---|---|---|
| Openness | Closed | Open | Closed |
| Completeness | Complete | Incomplete (only what this consumer uses) | Complete (union of consumer expectations) |
| Number | Single | One per consumer | Single |
| Authority | Authoritative | Non-authoritative | Non-authoritative |
| Bounded by | Time/space (versioning) | Time/space | The set of active consumers |

Why it matters for refinement:

- Consumer contracts turn each consumer's real expectations into **assertions the provider can run** — executable documentation of exactly which elements consumers depend on ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).
- The aggregated consumer-driven contract gives the provider a "repository of knowledge" about how its interface is actually used, enabling per-change impact assessment and targeted migration of only the affected consumers ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).
- Caveats: the pattern suits a "closed community of well-known services" (one enterprise), it "excavates and puts on display" hidden couplings rather than removing them, and consumer demands must not drag a service outside its business mandate ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).

**Advisory move:** when a story defines a provider component, ask which consumers exist and capture *their* expectations as part of the contract work — design the provider surface from consumer need, keeping services "lean, focused on actual consumer needs rather than speculative capabilities" ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).

## 3. Robustness: design both sides to tolerate evolution

- **Tolerant Reader** (Postel's Law applied to integration): consumers should read only the elements they need, ignore unknown elements, and encapsulate parsing in one place (a DTO/gateway) so payload changes touch one class — this is what makes *compatible* provider changes actually non-breaking in practice ([Fowler, TolerantReader](https://martinfowler.com/bliki/TolerantReader.html)).
- Prefer flexible extraction (e.g., path queries for just the needed nodes) over rigid whole-schema binding; schema-driven code generation that rejects unknown fields re-creates brittleness ([Fowler, TolerantReader](https://martinfowler.com/bliki/TolerantReader.html)).
- Provider-side mirror: schemas can carry explicit **extension points** so new optional fields have a sanctioned place, giving forwards/backwards compatibility under a must-ignore discipline ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).
- Zalando's guidelines codify the same duo as API-level rules: providers must only make backward-compatible ("non-breaking") extensions, consumers must follow tolerant-reader conventions, and compatibility obligations bind both parties ([Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/)).

## 4. What is a breaking change (make the list explicit in every contract)

Stripe's operational definition ([Stripe, API Versioning](https://stripe.com/blog/api-versioning)):

- **Compatible:** adding new endpoints; adding new fields that were never previously present.
- **Breaking:** removing fields; renaming fields; changing a field's type; changing the meaning/values of a returned field (their example: a boolean `verified` becoming a multi-valued `status`).
- The governing rule: "fields that were present before should stay present, and fields should always preserve their same type and name" ([Stripe](https://stripe.com/blog/api-versioning)).

A contract that doesn't state its compatibility rules leaves every future change to be litigated ad hoc. Zalando makes the policy explicit at the guideline level — always evolve compatibly if possible, and treat deprecation as a defined procedure (announce, monitor usage, sunset) rather than an event ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)).

## 5. Versioning strategy (when compatibility isn't enough)

Stripe's system, proven over "almost a hundred backwards-incompatible upgrades" in six years while staying compatible with every version since 2011 ([Stripe](https://stripe.com/blog/api-versioning)):

- **Date-named rolling versions** (e.g., `2017-05-24`) instead of v1/v2/v3; an account is **pinned** to the current version at its first request and never surprised by later breaking changes; upgrades are deliberate (per-request header override, or dashboard-level upgrade).
- Each breaking change lives in a self-contained **version change module** — documentation + transformation function + affected resources — and responses are produced current-first, then transformed *backward through the module chain* to the consumer's pinned version. Old versions stay abstracted out of core code paths.
- Changes whose effects can't be encapsulated (side-effect changes) are explicitly marked and consciously minimized — reduced encapsulation is treated as a smell ([Stripe](https://stripe.com/blog/api-versioning)).
- Three design principles worth quoting into any versioning DEC: keep upgrades **lightweight** (cheap for users and provider), make versioning **first-class** (so docs and changelogs generate automatically), and make old versions **fixed-cost** to maintain ([Stripe](https://stripe.com/blog/api-versioning)).
- Their meta-lesson: the best versioning system is the one you rarely use — "trying to get the design of our APIs right the first time," backed by a lightweight API review before any change ships ([Stripe](https://stripe.com/blog/api-versioning)).

**Heuristic:** for internal component contracts, prefer compatible extension + tolerant readers over any versioning machinery; introduce versioning only where consumers are external or unknown ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/); [Stripe](https://stripe.com/blog/api-versioning)).

## 6. API-first design conventions (defaults worth adopting wholesale)

Zalando's guidelines — battle-tested across a large microservice fleet — supply ready defaults so contract reviews argue about substance, not style ([Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/)):

- **API-first**: define the interface as an OpenAPI spec, with peer review, *before* implementation — the API is treated as a product whose customer is the developer.
- Consistent naming (snake_case properties, kebab-case URL paths, pluralized resource names); semantic use of HTTP methods and status codes.
- Standard mechanics specified per API, not improvised per endpoint ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)):
  - Pagination — cursor-based where underlying result sets change;
  - A single error payload shape used across all endpoints;
  - Optimistic locking conventions for concurrent updates;
  - Caching behavior declared via standard headers.
- Security defaults (OAuth2/Bearer) declared in the spec itself, not in side documents.
- The guidelines' framing is as important as the rules: APIs are **products**, judged by developer experience and consistency across the whole service fleet ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)).
- **Event contracts too**: events crossing team boundaries carry schemas and compatibility obligations exactly like synchronous APIs ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)). If an interaction uses event-carried state transfer, the event payload *is* a public contract with replication semantics to document ([Fowler, Event-Driven](https://martinfowler.com/articles/201701-event-driven.html)).

## 7. Client-facing shape: gateways and BFFs

- An **API Gateway** gives clients a single entry point, addressing four recurring mismatches ([microservices.io, API Gateway](https://microservices.io/patterns/apigateway.html)):
  - **Granularity**: internal services are finer-grained than any client wants to orchestrate;
  - **Client diversity**: mobile, web, and third-party integrations each need a different API shape (the Backends-for-Frontends variant gives each client type its own);
  - **Network variability**: mobile clients on unreliable networks shouldn't fan out many calls themselves;
  - **Dynamic topology**: service instances and partitioning change; clients shouldn't track that.
- The costs: one more network hop and one more highly available component to build and operate ([microservices.io, API Gateway](https://microservices.io/patterns/apigateway.html)).
- Its contract value: it **insulates clients from internal partitioning** — internal seams can move without breaking external consumers ([microservices.io, API Gateway](https://microservices.io/patterns/apigateway.html)); domain gateways serve the same role between internal domains at scale ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- Review angle: external/public contracts deserve stricter compatibility and versioning treatment than intra-domain ones; the gateway is where that line is drawn ([microservices.io](https://microservices.io/patterns/apigateway.html); [Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)).

## 8. Failure semantics: the contract's dark half

A contract that only describes success is half a contract — "design for failure" is a defining characteristic of service-based systems, because every remote call "can fail at any time" ([Fowler & Lewis, Microservices](https://martinfowler.com/articles/microservices.html); [Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)). Specify per operation:

- **Error surface**: semantic HTTP status codes and a standard error payload shape, uniform across the API rather than invented per endpoint ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/)).
- **Retry safety**: which operations are idempotent, and how non-idempotent ones are protected (idempotency keys and optimistic-locking conventions are standard parts of the guideline set) ([Zalando Guidelines](https://opensource.zalando.com/restful-api-guidelines/); Stripe's version modules track idempotency-key handling as contract-visible data — [Stripe](https://stripe.com/blog/api-versioning)).
- **Duplicate and ordering behavior for events**: async messaging buys decoupling and retriability at the price of possible duplicate messages and eventual consistency — consumers' dedup/ordering assumptions belong in the event contract ([Azure Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/)).
- **Degradation**: what the consumer should do when the provider is down or slow — tolerant-reader consumers plus event-carried state copies are the standard resilience moves, each with documented staleness ([Fowler, TolerantReader](https://martinfowler.com/bliki/TolerantReader.html); [Fowler, Event-Driven](https://martinfowler.com/articles/201701-event-driven.html)).
- **QoS bounds**: latency/availability/throughput expectations stated as measurable targets, since they are contract elements consumers will build against ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html); [Google SRE SLO](https://sre.google/sre-book/service-level-objectives/)).

## 9. Contract completeness skeleton

A component-doc contract section is complete when it can answer every row (dimensions per [Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html); mechanics per [Zalando](https://opensource.zalando.com/restful-api-guidelines/) and [Stripe](https://stripe.com/blog/api-versioning)):

| Clause | Contents |
|---|---|
| Operations | Each operation's purpose, inputs, outputs, side effects |
| Schemas | Payload structures, types, required vs optional, extension policy |
| Conversation | Ordering/state requirements across calls; sync vs async per interaction |
| Errors | Status-code semantics, error payload shape, retryability per error |
| Idempotency & concurrency | Retry-safe operations, idempotency keys, locking strategy |
| Events published/consumed | Schema, pattern (notification vs state transfer), delivery semantics |
| Policy | AuthN/AuthZ requirements, data classification, transactional context |
| QoS | Availability/latency/throughput targets and measurement point |
| Compatibility | What counts as breaking here; consumer must-ignore obligations |
| Versioning & deprecation | Strategy, pinning, sunset procedure (or explicit "compatible-evolution only") |
| Known consumers | Who depends on this, and where their expectations are recorded |

## 9b. Red flags in a submitted contract

- **The contract mirrors the database schema** — internal storage shapes leaking through the interface make every refactoring a breaking change; interfaces should insulate consumers from internal partitioning ([microservices.io, API Gateway](https://microservices.io/patterns/apigateway.html); [Martin, Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)).
- **No error or failure section** — only the happy path is specified ([Fowler & Lewis, Microservices](https://martinfowler.com/articles/microservices.html); [Zalando](https://opensource.zalando.com/restful-api-guidelines/)).
- **Versioning machinery for a two-team internal API** — compatible extension plus tolerant readers would carry the cost-free path ([Stripe](https://stripe.com/blog/api-versioning); [Fowler, TolerantReader](https://martinfowler.com/bliki/TolerantReader.html)).
- **Per-endpoint improvisation** — pagination, errors, naming differing across operations of one API ([Zalando](https://opensource.zalando.com/restful-api-guidelines/)).
- **"Consumers: TBD"** — a provider surface designed speculatively rather than from consumer expectations ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html)).
- **Event payloads treated as internal details** — anything another team consumes is a governed contract ([Zalando](https://opensource.zalando.com/restful-api-guidelines/)).

## 10. Review checklist: is this contract complete and evolvable?

1. Does the contract cover all five dimensions — schema, operations, conversation/ordering, policy (security, transactionality), and QoS — or just fields and endpoints? ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html))
2. Are the known consumers enumerated, and are their expectations captured (ideally as runnable assertions) rather than assumed? ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html))
3. Does the contract state its compatibility rules — what the provider may add, what consumers must ignore? ([Stripe](https://stripe.com/blog/api-versioning); [Fowler, TolerantReader](https://martinfowler.com/bliki/TolerantReader.html))
4. Is there a versioning/deprecation policy proportionate to the audience (none needed for tolerant internal pairs; explicit pinning/sunsetting for external consumers)? ([Stripe](https://stripe.com/blog/api-versioning); [Zalando](https://opensource.zalando.com/restful-api-guidelines/))
5. Are error responses, pagination, idempotency/retry semantics, and concurrency control specified — the mechanics every consumer will otherwise guess at? ([Zalando](https://opensource.zalando.com/restful-api-guidelines/))
6. For async interactions: which event pattern is this (notification vs state transfer), and is the event schema treated as a governed contract? ([Fowler, Event-Driven](https://martinfowler.com/articles/201701-event-driven.html); [Zalando](https://opensource.zalando.com/restful-api-guidelines/))
7. Does the interface expose implementation details (storage shapes, internal service partitioning) that will make future refactoring a breaking change? Gateways/facades exist to prevent exactly this ([microservices.io, API Gateway](https://microservices.io/patterns/apigateway.html)).
8. Is any consumer-requested capability outside the provider's business mandate (conceptual-integrity check)? ([Robinson](https://martinfowler.com/articles/consumerDrivenContracts.html))
9. Was the contract reviewed by someone other than its author before being frozen — Stripe routes every API change through review precisely to avoid needing the versioning machinery ([Stripe](https://stripe.com/blog/api-versioning))?

## 11. Related references in this corpus

- `decomposition-and-seams.md` — a contract exists per seam; boundary quality determines contract stability.
- `quality-attributes-and-tradeoffs.md` — SLI/SLO structure for the QoS clauses of a contract.
- `evolutionary-architecture.md` — how contracts evolve over years: strangling, versioning, consumer-driven visibility.
- `architecture-styles.md` — the four event patterns behind any async clause in a contract.
- `architecture-evaluation-and-review.md` — running the contract checklist inside a gate review.
