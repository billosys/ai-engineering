# Downstream Projection Assumptions

## Status

The items below are requirements and design inputs for a later project. No
projection, graph, vector index, transport, or runtime representation exists
in Project05 as a result of this document.

## Minimum Projection Contract

| Projection field or capability | Requirement | Reason |
| --- | --- | --- |
| Stable record identity | Preserve the card ID, revision, original path, and source slice. Do not derive identity from embedding similarity. | The ten records originate in two deliberately different record shapes. |
| Source identity | Retain upstream URL, pinned commit, tree, license/attribution basis, source file identity, heading, and one-based inclusive line locator. | A result must be traceable to the inspected source snapshot. |
| Claim and qualification | Keep the card claim/summary, boundary, source-support comparison, and exclusions together or resolvably linked. | Chunks and embeddings cannot replace claim-level support. |
| Evidence state | Retain evidence grade, extraction confidence, validation state, and dependency caveats separately. | Confidence is not evidence grade, and neither is verification. |
| Lifecycle state | Retain candidate/review state separately from verification, reconciliation, preservation, and admission states. | A runtime must not turn an unreviewed record into an accepted or admitted one by representation alone. |
| Relationships and CQs | Carry only explicit, source-based relationship or competency-question records; retain no relation or CQ where the source card asserts none. | Co-occurrence and vector proximity do not establish a relationship. |
| Operational additions | Future chunks, embeddings, index identifiers, access policies, and transport metadata may be additive and traceable. | They are projection metadata, not source evidence. |

## Import Preconditions

A future importer should reject or quarantine a record when it cannot resolve
its canonical record path, pinned source identity, claim support, or lifecycle
state. It should also preserve unresolved bibliography, figure, and
cross-reference dependencies instead of rewriting them as direct support.

Projection planning must decide whether only operator-accepted records are
eligible for import, whether candidates may appear in a review-only surface,
and what verification/reconciliation/admission evidence is required before a
record can be retained by a memory system. Project05 makes none of those
decisions.
