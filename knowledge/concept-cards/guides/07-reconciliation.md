# Reconciliation

Use reconciliation to resolve or explicitly retain conflicts among cards,
claims, support, edges, CQs and run outputs. Start with the
[operator workflow](./02-operator-workflow.md), identify the requested scope
and preserve the input revisions. A reconciliation result explains a conflict
and its disposition; reconciliation state summarizes that result's current
applicability. Neither substitutes for other evidence or lifecycle decisions.

## Establish Targets And Conflict Scope

Inventory affected construct identities and revisions, prior runs and actors,
source snapshots/support, prior results and incoming/outgoing dependencies.
Record who raised the conflict and which parts have actually been inspected.
For outputs from multiple workers, retain worker scope and provenance where
they exist; this procedure does not require spawning workers.

State the disagreement precisely before selecting a disposition. Separate
conflicts that require different evidence or decisions. A clean card format,
newer file, repeated assertion or worker majority does not select a winner.
Agreement among workers using the same source is not independent source
corroboration. Missing evidence is a limit on comparison, not evidence that
the competing material is false.

| Conflict | Required comparison |
| --- | --- |
| Duplicate concepts | Compare concept boundaries, meanings and source usage; same names need not mean the same concept, and different names need not mean different concepts. Inventory unique claims, explanations and dependencies before proposing a merge. |
| Competing definitions | Compare exact assertions, domain/edition, conditions and source spans. Distinguish incompatible claims from different senses or contexts; retain legitimate alternatives with their scope. |
| Slug or identifier drift | Compare stable identity with names, paths and aliases. Determine whether this is relocation, renaming or a changed concept; do not repoint an old identity to a new meaning silently. |
| Taxonomy drift | Compare the classification criterion and model scope, source evidence and prior placement. Record a model reason for moving or retaining a concept instead of treating folder order as authority. |
| Conflicting source support | Inspect both assertions and spans with provenance, dates/revisions, qualifications and preparation caveats. Distinguish source disagreement from extraction error or inaccessible content. |
| Relationship asymmetry | Compare endpoint roles, type, direction, inverse/symmetric views, support and status using the [relationship guide](./06-graph-cq.md). Distinguish a missing required view from contradictory relation meaning. |
| CQ coverage disputes | Compare question revision, answer criteria, component mappings and actual support. A coverage map, an answerability judgment and a retrieval result can disagree without being interchangeable results. |
| Preservation or worker conflict | Compare prior value and each worker's actual source/task scope, output and rationale. A merge must account for unique material and remaining disagreement, not merely keep the longest output. |

## Compare Evidence Before Deciding

1. Freeze or identify the candidate revisions. For every disputed assertion,
   locate its source span and support attachment. Keep bibliographic identity,
   extraction confidence and [evidence grade](./05-evidence-lifecycle.md)
   distinct from the comparison itself.
2. Read the relevant source content and context. Check whether qualifiers,
   source revisions, different concept senses or inference explain the
   apparent conflict. Route damaged or unusable source preparation to
   `document-extraction` when needed, retaining downstream uncertainty until
   the affected material can be assessed.
3. Compare prior value as secondary evidence of what must survive. It can
   reveal a useful distinction or lost explanation even when it lacks support;
   preserving that history does not establish its truth. Follow
   [re-extraction and preservation](./04-re-extraction-preservation.md).
4. State the supported alternatives and the limits of the comparison. If a
   domain judgment or unavailable source is necessary, name that dependency
   and retain the unresolved alternatives. Do not manufacture consensus.
5. Choose a scoped disposition with rationale: merge genuine duplicates while
   preserving unique value; distinguish concepts/senses; correct an extraction
   or reference error; supersede an outdated interpretation; retain competing
   supported views; reject an unsupported candidate for the intended use; or
   leave the conflict unresolved/deferred with a re-entry condition.

These are procedural options, not final record enums or an automatic algorithm.
A rejected candidate remains traceable with its rationale. A deferred conflict
remains a conflict; recording it does not mean it has been resolved.

## Record The Result And Apply Its Implications

For each conflict or explicitly bounded group, record:

- Result identity, date, actor/reconciler role, method and relevant run IDs;
  distinguish operator reports, direct inspection and inference.
- Conflict class and exact affected constructs/revisions, dependencies and
  scope exclusions; retain links to both old alternatives and resulting values.
- Inspected source support, spans and comparison observations, evidence limits,
  prior result references, chosen disposition and the reasoning for it.
- Preservation decisions for unique prior value: preserved and where,
  superseded and by what, rejected and why, or unresolved and what is needed.
- Structural validation needed after identity/reference changes; semantic
  verification needed for revised assertions and any prior results whose
  applicability changed.
- Memory admission implications for each affected target and intended use,
  including prior admissions needing reassessment, plus unresolved work,
  required acceptance where applicable and re-entry conditions.

Apply authorized changes while retaining the comparison trail. Update affected
references deliberately: splitting a concept may require reviewing every edge
and CQ mapping rather than redirecting them all to one replacement. Identify
uninspected or external dependents as remaining work. If only a proposal was
requested, report the proposed changes without implying they were applied.

## Keep Lifecycle Results Separate

Tie reconciliation state to the actual result, target revision and remaining
conflict scope. “Resolved” for one conflict is not a verdict on all conflicts
in the card set. A decision to retain distinct contextual meanings can resolve
a false conflict while leaving their factual claims unverified.

Run the needed [validation and verification](./08-validation-verification.md)
checks separately, recording their own evidence and actor scope. Structural
validity does not resolve competing meanings. A reconciliation judgment does
not establish a verification result or independent verification. Preserved
history is not endorsement; superseded/rejected material must remain
distinguishable from active claims.

Use [memory admission](./09-memory-admission.md) for any requested reliance
decision. Neither a completed reconciliation result nor operator preference
replaces the applicable source-support and review requirements. On later
revision, retain the old result and reassess its applicability rather than
silently copying “resolved” to the new construct.

## Human-Assisted Operation

Request the precise competing revisions, source excerpts, dependency list and
prior-value records needed for the comparison. Attribute reported checks to
their observer and keep unavailable evidence explicit. Return a proposed
result and proposed edits when direct inspection or writing is unavailable.
Do not claim the operator's entire corpus was reconciled from a supplied pair.
If required acceptance is missing, record that dependency without inventing it.

## Agent-Direct Operation

Inspect accessible candidates and source evidence, preserve inputs and record
the actual comparison scope. Save authorized results and changes at the accepted
home; reopen them to check target/revision references and preservation links.
Record the assistant's judgments as direct same-context work. Worker agreement
or a second pass by the same assistant does not create independent review.

## Handoff

Report result identities and locations, affected old/new revisions, conflict
classes, evidence comparisons, dispositions/rationale, actor/run provenance
and uninspected dependencies. Enumerate prior value and its preservation
destinations, remaining conflicts and re-entry conditions. Give validation,
verification, reconciliation, preservation and memory admission their separate
outcomes or mark them unassessed. Name the next source comparison, domain
review, acceptance or revised-target check that would change the result.

This procedure supplies method records, not a reconciliation runtime or proof
that an entire corpus was processed. See
[maintenance and package boundaries](./10-maintenance-packaging.md) for the
remaining support and integration work.
