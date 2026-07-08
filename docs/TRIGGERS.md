# Trigger Registry

Watched conditions that revive deferred work or start new work when the
world changes. Format per
[SPEC-triggers](specs/SPEC-triggers.md)
([DEC-0106](decisions/DEC-0106-trigger-registry.md)): entries are
`## TRG-nnnn (armed|fired|retired)`; firing or retiring cites a decision
([DEC-0107](decisions/DEC-0107-trigger-firing-cites-decision.md)).
Tooling loads **armed** entries only into agent context.

## TRG-0001 (armed)
**Condition:** Groundwork must run multi-node or highly available — more
than one app instance serving users.
**Consequence:** revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md)
(Postgres + pgvector graduation evaluation).
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0002 (armed)
**Condition:** More than one concurrent writer process is required —
the single-writer embedded model (DuckDB/LadybugDB) is the bottleneck.
**Consequence:** revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md).
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0003 (armed)
**Condition:** Embedded engine performance degrades at real corpus or
query scale (graph rebuilds, overlay queries, or vector search
exceeding acceptable latency).
**Consequence:** revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md).
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0004 (armed)
**Condition:** An enterprise deployment mandates external managed
databases (policy or compliance), ruling out embedded storage.
**Consequence:** revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md).
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)
