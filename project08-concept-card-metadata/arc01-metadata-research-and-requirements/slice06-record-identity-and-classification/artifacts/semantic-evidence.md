# Slice06 Semantic Evidence

## Scope

This packet covers exactly 37 root pairs: id/revision for eleven non-card
record kinds, record_type for those kinds plus concept-card, and untyped
category/subcategory/tier. It excludes nested IDs, actors, subjects, endpoints,
lifecycle decisions, locators and predicates.

## Identity, revision and type

Every current template named in semantic-membership.json has record_type, id and
revision at frontmatter lines 2-4; its hash and exact path are in that registry.
For each kind, id identifies the record itself and revision revises that record:
claim is an assertion, competency-question a question, extraction-run an
execution trace, memory-admission a scoped reliance decision,
preservation-decision a prior-value disposition, reconciliation-result a
conflict comparison, relationship-edge a relation record, source-locator a
coordinate record, source-support a support linkage, and validation/verification
results records of distinct checks. Thus an actor.id, subject_ref.id,
endpoint ID or cited-source revision is not the root record ID in scope.

record_type selects a representation contract, not a domain ontology. The
concept-card template is also registered because its type is within scope, while
its id/revision are accepted Batch01 pairs and excluded here. Template nulls
show representability but not populated generated values. Available populated
synthetic/real examples are recorded in the inventory and include the Arc07
concept card, source-support, CQ, extraction-run, memory-admission,
reconciliation and edge records; template-only kinds are explicitly not claimed
to have generated populated evidence.

## Legacy classification

v3.2 rerun prompt 0010, Classification lines 353-356 and requirements
879-890, calls category a primary domain taxonomy, subcategory an optional
finer classification, and tier foundational/intermediate/advanced. It keeps
them separate from provenance and coordinates. Complete Musician accent-types
has category rhythm-meter, subcategory metric-organization, tier foundational,
prerequisites meter, pdf_page 33 and a Quick Definition; Erlang
application-behaviour supplies category applications-releases, subcategory
applications, tier intermediate and prerequisites otp-application. These are
observations, not a judgment of either card against its source or a claim that
tier follows a complete graph. Current concept-card template omits all three,
but template absence does not prove their values were migrated or lost.

Lookup consequence: category/subcategory support legacy discovery facets, while
tier supports pedagogical filtering only with its stated limits. A migration
must retain these observations or explicitly disposition each; it must not
silently turn tier into a coordinate or taxonomy label.

## Limits

This is same-context semantic inspection, not CDC verification. It selects no
future classification standard and makes no corpus-wide authority/migration
claim. The remaining 508 non-Batch01 pairs remain owned by their prior work.
