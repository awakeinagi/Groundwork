# Trigger Registry

Watched conditions with subscribed deferred items, revived when the
condition fires. Format per
[SPEC-triggers](specs/SPEC-triggers.md)
([DEC-0109](decisions/DEC-0109-trigger-subscriptions.md)): entries are
`## TRG-nnnn (armed|fired|retired)` with a decision-cited subscriber
line per item; firing or retiring cites a decision
([DEC-0107](decisions/DEC-0107-trigger-firing-cites-decision.md)); a
firing revives **all** subscribers; revival unsubscribes the item from
every other armed trigger, and an emptied armed trigger retires
([DEC-0110](decisions/DEC-0110-subscription-lifecycle.md)). Tooling
loads **armed** entries only into agent context.

## TRG-0001 (armed)
**Condition:** Groundwork must run multi-node or highly available — more
than one app instance serving users.
**Subscribers:**
- revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md) (per [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md))
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0002 (armed)
**Condition:** More than one concurrent writer process is required —
the single-writer embedded model (DuckDB/LadybugDB) is the bottleneck.
**Subscribers:**
- revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md) (per [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md))
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0003 (armed)
**Condition:** Embedded engine performance degrades at real corpus or
query scale (graph rebuilds, overlay queries, or vector search
exceeding acceptable latency).
**Subscribers:**
- revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md) (per [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md))
- revive [SP-0003](spikes/SP-0003-hnsw-index-adoption.md) (per [DEC-0115](decisions/DEC-0115-sp-0003-hnsw-deferred.md))
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0004 (armed)
**Condition:** An enterprise deployment mandates external managed
databases (policy or compliance), ruling out embedded storage.
**Subscribers:**
- revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md) (per [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md))
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)
