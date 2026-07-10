# Decomposition and Seam Selection

**When to reach for this:** Use when refinement is carving a business goal or epic into components, services, or modules — deciding where the boundaries (seams) go, what each side owns, and how the pieces relate. Also use when reviewing a draft decomposition pre-gate: it supplies boundary-quality criteria, known anti-patterns, and the questions that expose a seam drawn in the wrong place. Seam mistakes are the most expensive architecture mistakes to reverse, especially across process boundaries ([Fowler, MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html)).

Constructed: 2026-07-09

---

## 1. First principle: cut along the domain, not the technology

- Decompose by **business capability** — what the organization does to generate value (e.g., order management, inventory management) — rather than by technical layer. Capabilities are stable ("business capabilities change slowly"), so the architecture stays stable while implementations churn; teams become cross-functional and autonomous; services get high cohesion and loose coupling ([microservices.io, Decompose by Business Capability](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)).
- The DDD variant: decompose by **subdomain**, classifying each as *core* (business differentiator), *supporting*, or *generic* (buy/off-the-shelf). Apply the Single Responsibility Principle and the Common Closure Principle — things that change together belong together ([microservices.io, Decompose by Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
- Both patterns share one hard prerequisite: identifying capabilities/subdomains "requires deep business domain knowledge and stakeholder engagement" ([microservices.io](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)) — which is precisely what goal→epic refinement interviews should surface. Feed decomposition from those interviews, not from an org chart or a database schema.
- The same rule holds inside a monolith: organize modules as vertical business slices, because business-feature changes are far more frequent than technology-platform swaps, and a vertical slice localizes each change to one module ([Grzybek, Modular Monolith Primer](https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer); [Shopify Engineering](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)).

## 2. Bounded contexts: the unit of model consistency

- A **Bounded Context** is a section of a large domain within which one model and one ubiquitous language hold consistently. Its motivation: "total unification of the domain model for a large system will not be feasible or cost-effective" — so stop pretending one canonical model can span the enterprise ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)).
- The same word ("customer", "product", "order") legitimately means different things in different contexts; a bounded context lets each team keep internal consistency without forcing artificial company-wide consensus on terminology ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)).
- Practical decomposition method (Azure's DDD-based process): (1) analyze the business domain and map business functions and their dependencies; (2) identify core/supporting/generic subdomains; (3) draw bounded contexts around model-consistent areas; (4) build a **context map** showing how contexts integrate; (5) derive services from contexts. Boundaries should follow *functional cohesion and loose coupling*, "not organization boundaries or technical layers" ([Azure, Domain Analysis for Microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
- Treat decomposition as **iterative, not one-shot** — Azure explicitly frames it as an ongoing process ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)), and Uber describes evolving service architecture as "trimming a hedge so that it eventually grows correctly" rather than a top-down one-time effort ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).

**Seam heuristic for refinement:** when two epics/stories keep needing different definitions of the same noun, that terminology fault line is a candidate bounded-context boundary ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)).

## 3. What a good boundary looks like (testable criteria)

Shopify's componentization gives concrete, checkable boundary rules ([Shopify Engineering](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)):

1. **Public API only**: cross-component communication goes through explicitly declared public interfaces; everything else is private.
2. **Exclusive data ownership**: each component owns its data; direct data-layer associations across a boundary are *always* violations.
3. **Declared dependencies**: a component loads only what it declares.
4. **Enforcement is automated**: their CI tool (Wedge) builds a call graph, isolates cross-boundary calls and data coupling, and scores each component's isolation — boundaries that are only documented, not measured, decay.

Complementary criteria from the microservice literature:

- One service = one capability/subdomain responsibility; independently deployable; data private to the owner — "services don't share data" ([Azure Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/); [microservices.io](https://microservices.io/patterns/microservices.html)).
- Module autonomy is a function of *how many* things it depends on, *how intensely*, and *how stable* those dependencies are — prefer few, occasional, stable dependencies ([Grzybek](https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer)).
- "Good choices of service boundaries will reduce [operational] problems, but boundaries in the wrong place makes it much worse" ([Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).

## 4. Structure above the seam: domains, layers, gateways (scale > ~dozens of services)

Uber's DOMA addresses what happens *after* decomposition succeeds too well (2,200 services; debugging traversed ~50 services across 12 teams; "networked monoliths" that required synchronized deploys) ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)):

- **Domains**: group related services into logical collections; there is "no guidance" on a universally right size — one service to tens ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- **Layers with a dependency direction**: infrastructure → business → product → presentation → edge; a layer depends only on layers beneath it, and higher layers have smaller blast radius and more product specificity ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- **Gateways**: a single entry point per domain, hiding internal services behind one interface — enabling migrations and platform rewrites without forcing upstream changes; Uber saw 25–50% onboarding-time reductions and support-cost drops of an order of magnitude ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- **Extensions**: logic extensions (provider/plugin interfaces) and data extensions (typed arbitrary attachments) let other teams add behavior without modifying a domain's core ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- Sizing note: microservices at Uber had an average half-life of ~1.5 years — design the *domain and gateway* level to outlive individual services ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).

## 4b. Worked shape of a domain analysis (illustrative)

The published walkthroughs (Azure's drone-delivery example, microservices.io's e-commerce example) follow the same recognizable shape ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis); [microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)); an advisor can reproduce it live in a session:

- **Business functions first**: list what the business does — take orders, schedule delivery, track packages, invoice customers — and the information handoffs between these activities ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
- **Classify**: scheduling/dispatch logic is *core* (the differentiator); accounts and invoicing are *supporting*; authentication or email delivery are *generic* — off-the-shelf candidates ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html); [Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
- **Notice the language splits**: "delivery" means a scheduled job to dispatch, a tracked shipment to the customer-facing context, and a billable line item to invoicing — three bounded contexts hiding in one noun ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)).
- **Draw the context map**: which context is upstream of which, and where translation happens ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
- **Only then** talk services: contexts become components/services, with core subdomains getting the strongest teams and the most design attention ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).

The classification also sets the build/buy conversation: spending scarce innovation capacity on a generic subdomain is the exact misallocation the innovation-token argument warns against ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html); [Choose Boring Technology](https://boringtechnology.club/)).

## 5. Data across seams: the consistency bill

Every seam that separates data owners creates a consistency question the design must answer explicitly:

- With database-per-service, cross-service invariants cannot use ACID transactions; the **Saga** pattern sequences local transactions with *compensating transactions* for rollback ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html)). Two coordination models:
  - **Choreography** — each service publishes events that trigger the next local transaction downstream; no central coordinator ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html)).
  - **Orchestration** — a central orchestrator tells each participant what to do and tracks progress ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html)).
- Sagas cost you automatic rollback and ACID isolation: compensation logic is hand-written, and concurrent sagas can interleave anomalously — the design must name its countermeasures, not assume them away ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html)).
- Alternatively, replicate reference data via **event-carried state transfer** — consumers keep their own copies, gaining availability and latency at the price of "lots of data schlepped around" and managed staleness ([Fowler, Event-Driven](https://martinfowler.com/articles/201701-event-driven.html)).
- Business tolerance matters: firms often "prize availability more" and tolerate inconsistency windows better than engineers assume — but someone must ask the business, per invariant ([Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).
- For deeper mechanics (partitioning, replication, versioned values, failure detection), consult the distributed-systems pattern catalog ([Joshi, Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/)).

## 5b. The team dimension of every seam

- Module boundaries matter more as teams grow and become geographically distributed — Fowler flags this explicitly as a Conway's Law consideration: the communication structure of the organization presses on the architecture ([Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).
- Capability-aligned services are what make **cross-functional, autonomous teams** possible — the team owns a business outcome, not a technical layer ([microservices.io, Business Capability](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html); [Fowler & Lewis, Microservices](https://martinfowler.com/articles/microservices.html)).
- But domains "are not necessarily aligned with organizational structure" — Uber deliberately allowed logical domain grouping to differ from the org chart, so reorganizations don't force re-architecture ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- Review both mismatch directions: a seam no team can own end-to-end will be orphaned; a seam that exists only because two teams exist is org-chart mirroring ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis); [microservices.io](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)).

## 5c. Questions that surface seams during grilling

Each maps to a decomposition force with a source behind it:

1. "Which of these things change together when the business changes?" — common closure ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
2. "Does this word mean the same thing to both of you?" — bounded-context detection ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html)).
3. "Which capability differentiates you from competitors, and which could you buy?" — core/supporting/generic triage ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
4. "Who must be able to change and ship without waiting on whom?" — the autonomy a seam must buy to pay its rent ([Fowler & Lewis, Microservices](https://martinfowler.com/articles/microservices.html); [Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).
5. "Which data must be correct together, always?" — invariant mapping before ownership is assigned ([Brewer, CAP](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/); [microservices.io, Saga](https://microservices.io/patterns/data/saga.html)).
6. "What load grows on its own curve?" — genuinely divergent scaling can justify a seam, though evidence for it as a *primary* driver is weak ([Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).

## 6. Anti-patterns to flag in review

- **Decomposition by technical layer** (GUI service, business-logic service, data service): guarantees every feature change crosses every boundary; both capability and subdomain patterns exist precisely to prevent this ([microservices.io](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html); [Grzybek](https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer)).
- **Networked monolith**: services that look independent but require synchronized deployments — the costs of distribution with none of the autonomy ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- **Shared database / cross-boundary data reach-ins**: Shopify treats cross-component data associations as unconditional violations; integration databases are a coupling source microservices exist to eliminate ([Shopify](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity); [Fowler Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)).
- **Premature fine granularity**: boundaries drawn before the domain is understood; prefer coarse first, split later ([Fowler, MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html)).
- **Org-chart mirroring as a default**: boundaries should follow functional cohesion, "not organization boundaries" ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)) — though note domains need not match org structure and both directions of mismatch deserve scrutiny ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- **A "big ball of mud" hiding under any style**: complexity of the architecture must match the domain, or dependencies silently stop being managed ([Azure Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/)).

## 7. Working procedure: from refinement interviews to candidate components

A repeatable sequence, assembled from the DDD-based process Azure documents and the capability/subdomain patterns ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis); [microservices.io](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)):

1. **Map the business functions** and their dependencies from the goal/epic interviews — what the organization does, who does it, what information flows between activities ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
2. **List candidate capabilities/subdomains** in business language (order management, customer management, inventory) — names a domain expert would recognize ([microservices.io, Business Capability](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)).
3. **Classify each subdomain**: core (differentiator — invest and own), supporting, or generic (candidate to buy or adopt off-the-shelf) ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html); [Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
4. **Draw bounded contexts** where one model and one vocabulary hold consistently; note where the same noun changes meaning ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html); [Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
5. **Build the context map**: for each pair of touching contexts, record the integration point and the direction of dependency ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
6. **Derive components/services from contexts**, applying single-responsibility and common-closure checks — what changes together stays together ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
7. **Assign data ownership** per component and flag every invariant that would span owners — each such invariant needs an explicit consistency strategy before the design gates ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html); [Shopify](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)).
8. **Schedule a revisit**: record which boundaries are confident and which are provisional — decomposition is iterative by nature ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis); [Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).

## 8. Sizing: how big should a piece be?

- There is no universal right size: Uber found "no guidance" possible on domain size — real domains ranged from one service to tens ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/)).
- The operative tests are responsibility-shaped, not line-count-shaped: one capability/subdomain per service, and common closure — a routine business change should land inside one component ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
- **Every seam charges rent**: latency, failure modes, consistency management, and operational surface all increase per boundary crossed ([Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html)). A seam that doesn't buy autonomy (independent change, deploy, scaling, or ownership) isn't paying its rent.
- Prefer coarse-grained pieces first and split along proven fault lines later; splitting a too-big component is routine, while re-joining wrongly separated services is expensive ([Fowler, MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html)).
- Check the team dimension: capability-aligned decomposition should yield boundaries a cross-functional team can own end-to-end ([microservices.io, Business Capability](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)).

## 8b. Outputs a decomposition session should leave behind

- **Capability/subdomain map** with core/supporting/generic classification ([microservices.io, Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
- **Context map**: bounded contexts, their integration points, and dependency directions ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
- **Data-ownership table**: every entity assigned to exactly one owner ([Shopify](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)).
- **Cross-owner invariant list**, each with its consistency strategy (transaction, saga + compensation, or accepted eventual consistency) ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html); [Brewer, CAP](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)).
- **Provisional-boundary notes**: which seams are confident, which await domain learning, and when they get revisited ([Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)).
- **Glossary entries** per context — the terminology fault lines made explicit ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html); [arc42 Overview](https://arc42.org/overview)).

## 9. Review checklist: proposed decomposition

For each proposed component/service boundary, ask:

1. Which business capability or subdomain does it map to, and is that classification (core/supporting/generic) stated? ([microservices.io](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html))
2. Could a domain expert recognize the component names? If they're technical nouns, suspect layer-decomposition ([microservices.io](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html)).
3. Do terms mean one thing inside the boundary? Where the same noun crosses boundaries, is the translation documented (context map)? ([Fowler, BoundedContext](https://martinfowler.com/bliki/BoundedContext.html); [Azure Domain Analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis))
4. Who owns each datum? Does any invariant span owners — and if so, is a saga/compensation or replication strategy named, with its isolation anomalies considered? ([microservices.io, Saga](https://microservices.io/patterns/data/saga.html))
5. Can each side change and deploy without coordinating with the other for routine work? If not, why is this a seam at all? ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/); [Fowler & Lewis](https://martinfowler.com/articles/microservices.html))
6. What enforces the boundary mechanically (CI checks, dependency rules, isolation scoring)? ([Shopify](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity))
7. Is there a dependency direction (layering) so blast radius and change-frequency gradients are explicit? ([Uber DOMA](https://www.uber.com/blog/microservice-architecture/))
8. Which change scenarios were tested against the decomposition ("if the business changes X, how many components move")? Common-closure violations show up here ([microservices.io](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html)).
9. Is this the coarsest decomposition that solves today's problem, with named seams for future splitting, rather than speculative fine granularity? ([Fowler, MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html))

## 10. Related references in this corpus

- `architecture-styles.md` — whether to distribute at all precedes where to cut; the microservice premium and modular-monolith option.
- `interface-and-contract-design.md` — once a seam is chosen, its contract is the deliverable.
- `quality-attributes-and-tradeoffs.md` — consistency/availability decisions each seam forces (CAP, invariants).
- `evolutionary-architecture.md` — moving seams later: strangler fig, gateways, boundary fitness functions.
- `architecture-evaluation-and-review.md` — running the seam checklist as part of a gate review.
