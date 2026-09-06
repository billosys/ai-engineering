# Relationships And Competency Questions

Use this guide to represent and review relationships and competency questions
(CQs) in a bounded card set. Start with the [operator workflow](./02-operator-workflow.md)
and identify the input revisions, requested relationship/CQ scope and intended
use. This is method guidance, not runtime graph/database construction.

## Select Relationship Identity

Read both endpoint constructs and state the proposed relationship in a plain
sentence. A card-local navigation field is sufficient for a simple reading
aid. Give a relationship edge its own stable identity when source support,
evidence grade, verification result, reconciliation result, run provenance,
preservation decision, graph closure state or conflict must attach to the
relationship itself. CQ coverage that relies on the relationship also needs
that recoverable edge identity. A file need not be created for every edge if
the accepted record format can identify it unambiguously within an artifact.

When promoting a navigation field, retain its origin and map it to the edge.
Do not leave two independently editable copies that can disagree silently.
Do not promote an editorial suggestion into a supported assertion merely by
assigning an identifier.

## Identify Endpoints And Meaning

1. Resolve each endpoint to its construct type, stable identity and revision.
   Cards are ordinary endpoints; claims, CQs or other accepted constructs may
   be more precise for support or coverage. Record each endpoint's role.
   A slug or filename is a location, not proof of stable concept identity.
2. State the relation type and its meaning for these endpoints, including
   conditions and scope. Two valid endpoint references establish neither the
   relationship's truth nor its suitability for the intended use.
3. Record direction and any inverse reading or symmetric view. Preserve the
   method vocabulary below; document any accepted extension explicitly.
4. Inspect the selected source span or supported premises for the relationship
   assertion itself. Explain how the evidence connects these endpoints. Source
   support for each card separately does not establish an edge between them.
   Label an inferred or editorial relationship as such; record its reasoning
   and limits rather than attributing it to an unstated source assertion.
5. Attach evidence grade and separate extraction confidence using
   [evidence lifecycle](./05-evidence-lifecycle.md). Record actor, method/run,
   input snapshots and provenance for creation or revision. For a review of an
   existing edge, reference its prior run without inventing a new extraction.

| Relation | Direction and reading |
| --- | --- |
| `prerequisites` | If A lists B as a prerequisite, B -> A means B supports understanding A. Preserve A's card-local list while making that edge orientation explicit. |
| `extends` | If A extends B, A -> B means A elaborates B; the inverse B -> A reads “is extended by.” |
| `related` | Symmetric association; explain the relevant connection, without inventing a dependency. |
| `contrasts_with` | Symmetric comparison; retain the specific basis and conditions of contrast. |

An inverse navigation view is not a second independently supported claim.
Symmetric relations should be recoverable from either endpoint without
contradictory copies. A missing reciprocal view is a structural gap only when
the accepted representation requires it; a single canonical edge may already
serve both endpoints. Contradictory direction, evidence or status needs
[reconciliation](./07-reconciliation.md), not an automatic reciprocal edit.

## Review Closure And Lifecycle Attachments

Enumerate the bounded set inspected and its referenced endpoints. Resolve
references or retain dangling ones as explicitly unresolved/deferred with a
reason and re-entry condition. Do not invent placeholder concepts to claim
closure. Reference completeness within this set is not completeness of the
domain's conceptual graph.

Keep the edge's validation result, verification result/state, reconciliation
result/state, preservation decision and memory admission separate. An endpoint
being verified or admitted does not transfer that status to its edge. Use
[validation and verification](./08-validation-verification.md) for reference
checks and semantic review against actual evidence. If an endpoint splits,
merges or changes meaning, reassess the edge and its coverage dependents;
preserve the old revision and result applicability under
[re-extraction and preservation](./04-re-extraction-preservation.md).

## Establish A Competency Question

Give each competency question an identity and revision, its actual question
text, originating operator question/source scope/run, and the intended use.
State what an adequate answer would contain: relevant distinctions, conditions,
support and any review requirements. Do not reduce a multi-part question to a
keyword whose presence can be counted as success.

Record the active roles separately: requirement, coverage target,
answerability check, verification target or retrieval probe. One CQ can serve
several roles, but a result from one role does not settle another. For example,
a question asking when A requires B needs the conditions of that relationship;
the presence of cards named A and B does not establish an answer.

## Assess Coverage And Answerability

1. Break the question into its required answer components without changing
   its meaning. Map each component to exact card, claim, source support/span
   and edge revisions. Record a CQ coverage assertion explaining what each
   mapped construct supplies, rather than merely listing related cards.
2. Identify missing components, inaccessible sources, partial support,
   contradictory claims and unreviewed relations. Preserve these as coverage
   gaps. A map with all references resolving can still lack adequate evidence.
3. Attempt a source-grounded answer using only the mapped material. Show the
   reasoning and identify any extra assumptions or unsupported steps. Record
   whether the question is answerable fully, partly or not yet within the
   stated scope; these descriptions are not a mandated schema enum.
4. Evaluate suitability for the intended use separately. An exploratory answer
   can remain unverified; durable semantic reliance requires the applicable
   [memory admission](./09-memory-admission.md) decision. A question may have
   coverage while lacking the support, verification or admission needed for
   its intended answer. Do not change the use silently to claim success.
5. Attach actual validation and verification results with actor, evidence,
   criteria and scope. Route disputed coverage or interpretations to
   [reconciliation](./07-reconciliation.md). Keeping the CQ and its old answer
   is a preservation decision, not resolution of the dispute.

A retrieval probe, when separately requested and available, records the query,
searched snapshot/scope, method, returned constructs and whether those results
helped answer the question. Retrieval success does not prove semantic support,
verification or memory admission; retrieval failure does not prove the corpus
lacks an answer. This guide supplies no retrieval runtime or index.

## Preserve Changed, Obsolete And Deferred Questions

Keep prior question text, requirement origin, coverage and results when the CQ
changes. Link the revision or replacement and explain which old observations
still apply. A substantially different requirement needs a distinct identity
or an explicit revision relationship, not a silent rewrite under old results.

For an obsolete CQ, record why it no longer fits the accepted scope, who made
that decision and any replacement. Obsolete does not mean answered. For a
deferred CQ, retain the unmet requirement, reason, remaining evidence/work and
re-entry condition. Report active, obsolete and deferred sets separately so
removing difficult questions cannot inflate coverage. Reassess dependents when
source, claim, edge or intended-use revisions change.

## Human-Assisted Operation

Request the specific endpoint revisions, relation sentence, source spans,
question/answer criteria and prior results needed for the bounded review.
Attribute supplied observations to the operator and distinguish inspected
excerpts from a reported whole-card or whole-source check. Return proposed
edge/CQ records and missing evidence when direct access or writing is absent;
do not claim saved records, complete graph inspection or independent review.

## Agent-Direct Operation

Inspect accessible endpoints, source spans and CQ mappings directly. Preserve
old values, record the actual subset checked and write only authorized method
records to their accepted home. Reopen changed records to check references and
revision associations. Record semantic judgments separately from reference
checks; same-context review remains same-context. Do not build a graph database
or execute a retrieval service just because an edge or CQ is represented.

## Handoff

Report input/output paths and revisions, actor/run, edge identities and
endpoint roles, directions/inverses, relation meaning, source support and
unresolved references. Include CQ identities/roles, component coverage maps,
bounded answerability judgments, any actual retrieval observations, changed/
obsolete/deferred decisions and their history. Keep evidence grade, confidence,
validation, verification, reconciliation, preservation and admission visible
at their assessed scope; name unassessed work explicitly.

Identify the next evidence comparison, conflict disposition or review needed,
with remaining coverage and re-entry conditions. Consult
[maintenance and package boundaries](./10-maintenance-packaging.md) before
promising support assets or runtime behavior beyond these method records.
