# Quality Attributes and Trade-off Analysis

**When to reach for this:** Use whenever refinement must turn vague "-ilities" into decidable requirements — at business-goal level (which qualities matter and how much), at epic/story level (scenario-form quality requirements and SLO targets), and at component level (contract QoS clauses). Also use pre-gate to check that quality requirements are measurable and that the trade-offs a design silently makes are named. The companion evaluation reference covers the review *process* (ATAM); this one covers the *substance* being reviewed.

Constructed: 2026-07-09

---

## 1. Qualities must be scenarios, not adjectives

- "Fast", "secure", "scalable" are not requirements. The arc42 quality model (Q42) structures quality work as **requirement scenarios**: each with a *context*, a *trigger/stimulus*, and *acceptance criteria/response measures* — and catalogs 189 quality characteristics with 147 example scenarios and 52 solution tactics to draw from ([arc42 Quality Model](https://quality.arc42.org/)).
- ATAM likewise operationalizes qualities as scenarios — "concrete descriptions of how the system must perform under specific conditions" — used as test cases against the architecture ([SEI, ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
- Prioritization vehicle: the **quality attribute utility tree** — a hierarchical model that breaks "utility" into quality factors, refines them into scenarios, and prioritizes them; only the high-priority branches get deep analysis ([SEI, ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
- arc42 makes the same point structurally: a document's Introduction section carries the **top 3–5 quality goals** stakeholders actually prioritized, and section 10 expands them into a quality tree with scenarios ([arc42 Overview](https://arc42.org/overview)).

**Advisory rule:** cap the driving quality goals at 3–5 ([arc42](https://arc42.org/overview)). A design "prioritizing" ten qualities has prioritized none, and conflicting goals must be surfaced and resolved with stakeholders, not averaged ([Thoughtworks, Fitness Functions](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)).

## 2. Grilling template for one quality scenario

Derived from the scenario anatomy shared by Q42 and ATAM ([arc42 Quality Model](https://quality.arc42.org/); [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)):

1. **Context/environment** — normal load? peak? degraded mode?
2. **Stimulus** — what arrives or happens (request burst, node failure, malicious input, new requirement)?
3. **Response** — what should the system observably do?
4. **Response measure** — the number that makes it testable (latency percentile, RTO, error rate, time-to-change).
5. **Priority** — business value if met, risk if missed.
6. **Owner** — which stakeholder asserted this? (Traceability back to a goal.)

## 2b. Utility tree sketch

The ATAM utility tree turns "quality" into a prioritized workplan: root = utility; branches = quality factors; leaves = concrete scenarios, each rated for business importance and architectural risk, with only the high-priority leaves getting deep analysis ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)). Illustrative shape:

```
Utility
├── Performance
│   └── (H,H) Checkout p99 ≤ 2s at 5x seasonal peak
├── Availability
│   └── (H,M) Payment-provider outage: orders queued, none lost
├── Modifiability
│   └── (M,H) New tax jurisdiction added in ≤ 1 sprint, one component touched
└── Security
    └── (H,M) Leaked API credential revocable within 15 minutes
```

The two ratings (business importance, architectural difficulty/risk) are what make the tree a *triage* device, not just a taxonomy ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).

## 3. Reliability targets: SLIs, SLOs, SLAs

From the Google SRE treatment ([Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)):

- **SLI** = a quantitative indicator (request latency, error rate, availability, durability). **SLO** = target value/range for an SLI. **SLA** = contract with consequences attached. Keep the three distinct.
- Use **percentiles, not averages**: high-percentile latency reveals worst-case behavior that averages hide; a p99 target catches the tail users actually feel.
- Choose targets from **user-facing need, not current performance**: basing SLOs on what the system happens to do today enshrines accidents as promises.
- **Fewer, better SLOs**: pick just enough indicators to cover what users care about; different system types need different indicators (user-facing: availability/latency/throughput; storage: durability joins the list).
- Keep a **safety margin** between internal targets and externally promised numbers, and deliberately avoid overperforming a target users will otherwise learn to rely on.
- SLOs are a **control mechanism**: they drive alerting, engineering prioritization, and the decision of when reliability work outranks features ([SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/)).

**Refinement hook:** any epic/story naming availability or latency should leave the session with an SLI definition, an SLO number, and a measurement point — otherwise it is an adjective, not a requirement ([SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/)).

Typical indicator sets by system type ([SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/)):

| System type | Indicators that matter most |
|---|---|
| User-facing serving | Availability, latency (percentiles), throughput |
| Storage | Latency, availability, **durability** |
| Cross-team consistency | Standardize SLI definitions (measurement window, measurement point) so teams don't re-derive them per project |

A further SRE discipline worth importing: build targets from what users need the system to do, keep a margin between what you promise and what you deliver, and remember every SLO you publish becomes a dependency someone builds on ([SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/)).

## 4. Distributed-consistency trade-offs: CAP, correctly

Brewer's own retrospective corrects the folklore ([CAP Twelve Years Later](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)):

- The "2 of 3" formulation is **misleading**: partitions are rare, so systems can deliver both consistency and availability almost all the time; the real design question is what happens *during* a partition.
- The choice is not binary or global: it can be made **per operation, per data type**, and consistency/availability each come in degrees.
- Recommended discipline when a partition occurs: (1) **detect** it; (2) enter an explicit **partition mode** that limits which operations proceed; (3) run **partition recovery** that restores consistency and compensates for mistakes made while partitioned ([Brewer](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)).
- Techniques for principled recovery: version vectors to track causality; **CRDTs** (commutative/convergent replicated data types) that provably converge after partitions ([Brewer](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)).
- The designer's real job is knowing the system's **invariants**: which ones must never be violated (prohibit risky operations during partitions) and which can be violated then repaired (allow-and-compensate) ([Brewer](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)).

**Review question:** for each cross-component invariant, is the partition-time behavior chosen deliberately (block vs proceed-and-compensate), and is the compensation designed? ([Brewer](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/); see also Saga isolation anomalies, [microservices.io](https://microservices.io/patterns/data/saga.html))

## 5. Recurring trade-off pairs

Sensitivity and trade-off points are ATAM's core discovery: architectural decisions that significantly affect one quality, or that "affect multiple quality attributes, often forcing compromises between competing goals" ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)). Pairs that recur constantly in refinement:

| Decision favors | At the expense of | Canonical discussion |
|---|---|---|
| Strong consistency | Availability/latency under partition | [Brewer, CAP](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/) |
| Async messaging (reliability, scalability, decoupling) | Eventual consistency, duplicate handling, invisible flow | [Azure Architecture Styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/); [Fowler, Event-Driven](https://martinfowler.com/articles/201701-event-driven.html) |
| Fine-grained decomposition (autonomy, independent deploy) | Latency, operational complexity, consistency | [Fowler, Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html) |
| Redundancy/failover (reliability) | Cost, complexity | [Azure WAF Reliability](https://learn.microsoft.com/en-us/azure/well-architected/reliability/); [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) |
| Performance headroom / overprovisioning | Cost efficiency | [Azure WAF Performance Efficiency](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/); [AWS Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) |
| Security controls (inspection, segmentation, encryption) | Performance, operational friction | [Azure WAF Security](https://learn.microsoft.com/en-us/azure/well-architected/security/); [AWS Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) |
| Technology novelty (capability gains) | Operability, unknown-unknowns | [Choose Boring Technology](https://boringtechnology.club/) |
| Replicated data (availability, latency) | Staleness, storage, copy management | [Fowler, Event-Driven](https://martinfowler.com/articles/201701-event-driven.html) |

The Well-Architected frameworks are explicit that pillars trade against each other and publish per-pillar trade-off pages; use them as a prompt list when hunting for unstated costs ([Azure WAF Pillars](https://learn.microsoft.com/en-us/azure/well-architected/pillars); [AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)).

## 6. Making qualities enforceable: fitness functions

- A fitness function measures "how closely an architecture aligns with stated architectural goals," giving continuous feedback during development instead of post-deployment discovery ([Thoughtworks, Fitness Function-Driven Development](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)).
- Once a quality scenario has a response measure (section 2) it is one step from automation: encode it as a pipeline gate. Dimensions with published examples: code quality, resiliency, observability, performance, compliance, security, operability, pipeline standards ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)).
- See the evolutionary-architecture reference for the identification/definition/operationalization process.

## 7. Worked thread: one requirement in three forms

Illustrative example (structure from the cited sources; numbers invented for the illustration):

- **Raw stakeholder statement**: "checkout must be fast even on sale days."
- **Scenario form** (anatomy per [arc42 Quality Model](https://quality.arc42.org/); [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)): *Context*: seasonal peak, 5x normal traffic. *Stimulus*: customer submits checkout. *Response*: order accepted and confirmed. *Response measure*: p99 end-to-end ≤ 2 s; error rate ≤ 0.1%.
- **SLO form** (structure per [Google SRE SLO](https://sre.google/sre-book/service-level-objectives/)): SLI = fraction of checkout requests completing successfully under 2 s, measured at the load balancer; SLO = 99.9% over a rolling 28 days; internal target stricter than any external SLA to preserve margin.
- **Fitness-function form** (per [Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)): a load-test stage in the pipeline replays peak-shaped traffic and fails the build when the latency/error thresholds are exceeded — the gate decision now enforces itself on every change.
- **Trade-off record** (per [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)): meeting the peak target requires capacity headroom — a performance-vs-cost trade-off point for stakeholder sign-off ([Azure WAF Cost Optimization](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/)).

This chain — adjective → scenario → SLO → fitness function → recorded trade-off — is the full maturation path of a quality requirement through refinement.

## 8. Prompt list: qualities refinement forgets to ask about

Use as an interview sweep; the Q42 model's 189 characteristics exist because unprompted stakeholders name only the obvious ones ([arc42 Quality Model](https://quality.arc42.org/)):

- **Observability**: log aggregation, metrics, health endpoints, correlation/trace IDs — an explicit fitness-function dimension, rarely a stakeholder ask ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)).
- **Operability**: runbooks, alerting, safe-deployment hooks ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development); [Azure WAF Operational Excellence](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/)).
- **Compliance/privacy**: PII protection, audit requirements (e.g., GDPR) ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development)).
- **Security as CIA**: confidentiality, integrity, *and* availability of data — plus posture sustainment over time ([Azure WAF Security](https://learn.microsoft.com/en-us/azure/well-architected/security/)).
- **Cost**: a designable quality with targets and monitoring, not an afterthought ([Azure WAF Cost Optimization](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/)).
- **Durability**: distinct from availability; the indicator that matters most for storage-shaped systems ([Google SRE SLO](https://sre.google/sre-book/service-level-objectives/)).
- **Modifiability/evolvability**: internal quality determines feature velocity within weeks — ask "what change must be cheap?" ([Fowler, Software Architecture Guide](https://martinfowler.com/architecture/)).
- **Recoverability**: designed and tested recovery, not just failure avoidance ([Azure WAF Reliability](https://learn.microsoft.com/en-us/azure/well-architected/reliability/); [AWS Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)).
- **Sustainability**: a first-class pillar on AWS ([AWS WAF](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)).

## 9. Review checklist: quality requirements at any gate

1. Are the top quality goals limited to ~3–5 and traceable to named stakeholders/business drivers? ([arc42](https://arc42.org/overview); [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/))
2. Is every quality requirement in scenario form with a measurable response — no bare adjectives? ([arc42 Quality Model](https://quality.arc42.org/))
3. Do reliability/performance targets use SLI/SLO structure with percentile measures and a stated measurement point? ([SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/))
4. Are targets derived from user/business need rather than current behavior, with margin between internal and promised levels? ([SRE SLO chapter](https://sre.google/sre-book/service-level-objectives/))
5. For every major design decision, is at least one quality it *hurts* recorded? A decision with no stated downside hasn't been analyzed — trade-off points are where the risk lives ([SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)).
6. Are cross-component invariants classified: transactional, saga-with-compensation, or eventually consistent — and did the business sign off on the inconsistency windows? ([Brewer](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/); [Fowler Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html))
7. Which quality requirements will be verified automatically (fitness functions), and which only by review? ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development))
8. Have conflicting quality goals between stakeholders been surfaced and explicitly resolved? ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development))
9. Are quality goals traceable forward as well — does each top goal have at least one scenario, and each scenario a place in the design where it is satisfied? (Utility-tree discipline, [SEI ATAM](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/))
10. For the qualities on the forget-list (section 8), was each explicitly considered or explicitly declared out of scope? ([Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development); [arc42 Quality Model](https://quality.arc42.org/))

## 10. Related references in this corpus

- `architecture-evaluation-and-review.md` — the ATAM process that consumes these scenarios and utility trees.
- `evolutionary-architecture.md` — turning response measures into pipeline-enforced fitness functions.
- `cloud-well-architected.md` — pillar-by-pillar question banks for the operational qualities.
- `interface-and-contract-design.md` — where QoS targets land as contract clauses.
- `decomposition-and-seams.md` — the consistency/availability bill each seam creates.
