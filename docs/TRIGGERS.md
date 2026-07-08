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
- revive [SP-0009](spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md) (per [DEC-0205](decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md))
- revive [SP-0010](spikes/SP-0010-external-kv-store-adapter-evaluation.md) (per [DEC-0205](decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md))
**Cites:** [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md)

## TRG-0002 (armed)
**Condition:** More than one concurrent writer process is required —
the single-writer embedded model (DuckDB/LadybugDB) is the bottleneck.
**Subscribers:**
- revive [SP-0002](spikes/SP-0002-postgres-pgvector-graduation.md) (per [DEC-0105](decisions/DEC-0105-sp-0002-rescoped-deferred.md))
- revive [SP-0009](spikes/SP-0009-aws-sqs-queue-adapter-evaluation.md) (per [DEC-0205](decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md))
- revive [SP-0010](spikes/SP-0010-external-kv-store-adapter-evaluation.md) (per [DEC-0205](decisions/DEC-0205-graduation-trigger-reuse-and-spikes.md))
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

## TRG-0005 (armed)
**Condition:** The first post-launch change to an artifact SPEC
document occurs — any gated edit to `docs/specs/SPEC-*.md` after the
reference implementation ships.
**Subscribers:**
- revive [ST-0011](stories/ST-0011-schema-evolution-machinery.md) (per [DEC-0133](decisions/DEC-0133-out-of-scope-differentiated-rule.md))
**Cites:** [DEC-0133](decisions/DEC-0133-out-of-scope-differentiated-rule.md)

## TRG-0006 (armed)
**Condition:** An enterprise deployment mandates an external secret
store (policy or compliance), ruling out embedded encrypted secrets in
the app database.
**Subscribers:**
- revive [SP-0005](spikes/SP-0005-external-secret-store-adapter.md) (per [DEC-0152](decisions/DEC-0152-secrets-encrypted-in-app-database.md))
**Cites:** [DEC-0152](decisions/DEC-0152-secrets-encrypted-in-app-database.md)

## TRG-0007 (armed)
**Condition:** A deployment requires a code host other than GitHub
(Bitbucket Cloud, GitLab, …). Bitbucket Data Center has its own
dedicated trigger, `TRG-0010`.
**Subscribers:**
- revive [ST-0028](stories/ST-0028-additional-code-host-connectors.md) (per [DEC-0156](decisions/DEC-0156-future-connector-families-deferred.md))
**Cites:** [DEC-0156](decisions/DEC-0156-future-connector-families-deferred.md), [DEC-0172](decisions/DEC-0172-github-v1-bbdc-deferred.md)

## TRG-0008 (armed)
**Condition:** A deployment requires a notification channel beyond
email (Slack, Teams, …).
**Subscribers:**
- revive [ST-0029](stories/ST-0029-additional-notifier-adapters.md) (per [DEC-0156](decisions/DEC-0156-future-connector-families-deferred.md))
**Cites:** [DEC-0156](decisions/DEC-0156-future-connector-families-deferred.md)

## TRG-0009 (armed)
**Condition:** A deployment requires a work-management system other
than Jira Data Center (monday.com, OpenProject, Jira Cloud, …).
**Subscribers:**
- revive [ST-0030](stories/ST-0030-additional-work-management-connectors.md) (per [DEC-0156](decisions/DEC-0156-future-connector-families-deferred.md))
**Cites:** [DEC-0156](decisions/DEC-0156-future-connector-families-deferred.md)

## TRG-0010 (armed)
**Condition:** A deployment requires Bitbucket Data Center.
**Subscribers:**
- revive [ST-0020](stories/ST-0020-bitbucket-data-center-connector.md) (per [DEC-0172](decisions/DEC-0172-github-v1-bbdc-deferred.md))
- revive [SP-0004](spikes/SP-0004-bbdc-required-check-surface.md) (per [DEC-0172](decisions/DEC-0172-github-v1-bbdc-deferred.md))
**Cites:** [DEC-0172](decisions/DEC-0172-github-v1-bbdc-deferred.md)
