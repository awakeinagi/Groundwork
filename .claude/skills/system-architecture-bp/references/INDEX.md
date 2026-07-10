# Corpus index — system-architecture-bp

Constructed: 2026-07-09 by the DEC-0295 pipeline (extraction agent →
10-Haiku exploration swarm → facilitator assembly, generator subagent
drafting). Refresh is on-demand only; a re-run enters via change
intake. Body of record for the pipeline: SES-0054 in the
project-documentation-system corpus.

## Reference docs by topic

| Doc | Reach for it when advising on |
|---|---|
| [architecture-styles.md](architecture-styles.md) | Style selection & trade-offs, monolith-first default, event-pattern disambiguation, style smells |
| [decomposition-and-seams.md](decomposition-and-seams.md) | Bounded contexts, capability/subdomain cuts, service boundary criteria, seam checklists |
| [interface-and-contract-design.md](interface-and-contract-design.md) | Contract dimensions, consumer-driven contracts, breaking changes, versioning, contract completeness |
| [quality-attributes-and-tradeoffs.md](quality-attributes-and-tradeoffs.md) | Scenario-form quality attributes, utility trees, SLOs, trade-off analysis |
| [architecture-evaluation-and-review.md](architecture-evaluation-and-review.md) | ATAM (full & lightweight), technology vetting, adversarial review prompts, reviewer checklists |
| [documentation-practices.md](documentation-practices.md) | ADR format, arc42 sections, C4 levels, design docs, doc anti-rot |
| [cloud-well-architected.md](cloud-well-architected.md) | AWS/Azure pillar maps, per-pillar review questions, twelve-factor checklist |
| [evolutionary-architecture.md](evolutionary-architecture.md) | Monolith-first sequencing, strangler fig, fitness functions, evolution decision records |

Vendored primary texts: `../vendored/arc42/` (CC-BY-SA 4.0) and
`../vendored/awesome-software-architecture/` (CC0) — see
`../vendored/NOTICE.md`.

## Source scorecard (DEC-0295 pipeline, constructed 2026-07-09)

55 sources explored by the 10-agent swarm; inclusion bar relevancy ≥7 AND quality ≥7.
54 selected, 0 borderline, 1 fetch-failed (kept as appendix pointer).

| Source | Topic | Rel | Qual |
|---|---|---|---|
| [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) | cloud | 9 | 9 |
| [Azure Well-Architected Framework - Pillars overview](https://learn.microsoft.com/en-us/azure/well-architected/pillars) | cloud | 9 | 9 |
| [Security quick links - Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/security/) | cloud | 9 | 9 |
| [Operational excellence quick links - Microsoft Azure Well-Architected ](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/) | cloud | 9 | 9 |
| [Operational Excellence Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) | cloud | 8 | 9 |
| [Cost Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) | cloud | 8 | 9 |
| [The Twelve-Factor App](https://12factor.net/) | cloud | 8 | 9 |
| [Security Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) | cloud | 7 | 9 |
| [Cost optimization quick links - Microsoft Azure Well-Architected Frame](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/) | cloud | 7 | 8 |
| [Consumer-Driven Contracts: A Service Evolution Pattern (Ian Robinson)](https://martinfowler.com/articles/consumerDrivenContracts.html) | contracts | 10 | 9 |
| [Tolerant Reader](https://martinfowler.com/bliki/TolerantReader.html) | contracts | 9 | 10 |
| [Zalando RESTful API and Event Guidelines](https://opensource.zalando.com/restful-api-guidelines/) | contracts | 9 | 9 |
| [Pattern: API Gateway / Backends for Frontends](https://microservices.io/patterns/apigateway.html) | contracts | 9 | 9 |
| [APIs as Infrastructure: Future-Proofing Stripe with Versioning](https://stripe.com/blog/api-versioning) | contracts | 8 | 8 |
| [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) | decomposition | 10 | 10 |
| [Pattern: Decompose by Business Capability](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html) | decomposition | 10 | 9 |
| [Pattern: Decompose by Subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html) | decomposition | 10 | 9 |
| [Using Domain Analysis to Model Microservices (Azure Architecture Cente](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) | decomposition | 10 | 9 |
| [Introducing Domain-Oriented Microservice Architecture](https://www.uber.com/blog/microservice-architecture/) | decomposition | 9 | 9 |
| [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | documentation | 10 | 10 |
| [C4 Model - Introduction](https://c4model.com/introduction) | documentation | 10 | 9 |
| [C4 Model - System Context Diagram](https://c4model.com/diagrams/system-context) | documentation | 10 | 9 |
| [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) | documentation | 9 | 9 |
| [C4 Model - Container Diagram](https://c4model.com/diagrams/container) | documentation | 9 | 9 |
| [Component Diagrams in the C4 Model](https://c4model.com/diagrams/component) | documentation | 9 | 9 |
| [arc42 Template Overview](https://arc42.org/overview) | documentation | 9 | 9 |
| [Architecture Tradeoff Analysis Method (ATAM)](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) | evaluation | 10 | 9 |
| [Review checklist / C4 model](https://c4model.com/diagrams/checklist) | evaluation | 9 | 8 |
| [Choose Boring Technology](https://boringtechnology.club/) | evaluation | 7 | 8 |
| [Monolith First (Martin Fowler)](https://martinfowler.com/bliki/MonolithFirst.html) | evolution | 10 | 10 |
| [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) | evolution | 9 | 10 |
| [Fitness function-driven development](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development) | evolution | 9 | 9 |
| [Deconstructing the Monolith: Designing Software that Maximizes Develop](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) | evolution | 9 | 9 |
| [Software Architecture](https://martinfowler.com/architecture/) | foundations | 10 | 10 |
| [Catalog of Patterns of Distributed Systems](https://martinfowler.com/articles/patterns-of-distributed-systems/) | patterns | 10 | 10 |
| [Cloud Design Patterns - Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/) | patterns | 10 | 9 |
| [Microservice Architecture Pattern Language Index](https://microservices.io/patterns/index.html) | patterns | 9 | 9 |
| [Pattern: Saga (microservices.io)](https://microservices.io/patterns/data/saga.html) | patterns | 9 | 8 |
| [Catalog of Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/) | patterns | 8 | 8 |
| [CAP Twelve Years Later: How the 'Rules' Have Changed](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/) | quality-attributes | 10 | 10 |
| [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) | quality-attributes | 9 | 10 |
| [Reliability quick links - Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/reliability/) | quality-attributes | 9 | 9 |
| [arc42 Quality Model (Q42)](https://quality.arc42.org/) | quality-attributes | 9 | 9 |
| [Reliability Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) | quality-attributes | 9 | 9 |
| [Performance Efficiency Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) | quality-attributes | 9 | 9 |
| [Azure Well-Architected Framework - Performance Efficiency Pillar](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/) | quality-attributes | 8 | 8 |
| [Microservices](https://martinfowler.com/articles/microservices.html) | styles | 10 | 10 |
| [What do you mean by 'Event-Driven'?](https://martinfowler.com/articles/201701-event-driven.html) | styles | 10 | 10 |
| [Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html) | styles | 10 | 9 |
| [Microservice Architecture Pattern](https://microservices.io/patterns/microservices.html) | styles | 10 | 9 |
| [Azure Architecture Center - Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/) | styles | 10 | 9 |
| [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) | styles | 10 | 9 |
| [Hexagonal Architecture](https://jmgarridopaz.github.io/content/hexagonalarchitecture.html) | styles | 9 | 9 |
| [Modular Monolith: A Primer (Kamil Grzybek)](https://www.kamilgrzybek.com/blog/posts/modular-monolith-primer) | styles | 9 | 9 |

### Appendix — pointers only

- [Who Needs an Architect? (Martin Fowler, IEEE Software)](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf) — canonical essay; PDF fetch failed in the pipeline run (binary not parseable), retained as a pointer without scores.
