# Slice04 Authored Semantic Families

`semantic-membership.json` expands these authored families to 303 observed
path/kind pairs. It is a planning comparison artifact, not a future schema.

## identity-labels

Subject: the concept, record, source, claim, CQ, edge, or assertion identified
in its own context—not every nested `id`. Legacy cards use `concept`, `slug`
and `aliases`; current concept-card templates define `id`, `revision`, `title`
and `concept_slug` (`templates/concept-card.md`, frontmatter). `aliases` occurs
in both surfaces, so it is preserved; its authority/normalization remains an
Arc02 question. Losing a concept ID/slug/alias prevents direct lookup and
migration matching; losing an assertion ID prevents a coverage result from
targeting that assertion. Bodies may repeat a label but prose is not a stable
lookup projection.

## classification-progression

Subject: historical discovery classification (`category`, `subcategory`) and
pedagogical placement (`tier`, chapter/section/page). Complete Musician cards
provide real scalar values; current templates do not require the three-level
legacy classification. This is an observed weakening of compulsory structured
projection, not evidence that the old values vanished. Query consequence:
category/tier browsing and chapter/page filtering need an explicit migration
projection; book-specific locations must not be forced on web sources.

## source-locator

Subject: a cited resource, its prepared/snapshot representation, and a located
span. `references/record-field-groups.md` and document-extraction output/locator
guides distinguish resource identity, preparation and locator/span. `source_refs[].id`
identifies the referenced source, while `source_spans[].source_ref` links a span
to it; neither identifies the card. Legacy source/title/author/chapter/page
fields are preserved as values but relocated into scoped current references.
Null locator components record inapplicability, not absence of a source.

## claim-support

Subject: an assertion and the support/attachment connecting it to source spans.
Current claim/source-support templates distinguish claim identity from support;
legacy cards often retain support only in body prose. The structured relation is
therefore strengthened/currently explicit, while prose remains readable context
not machine-query equivalence. Losing claim/support links prevents review of
which span warrants which assertion.

## relationship-graph

Subject: a directed/symmetric typed relation and its endpoints. Legacy
`prerequisites`, `extends`, `related` and `contrasts_with` are useful flat
traversal lists; current edge records add endpoints, direction, predicate and
support context (`templates/relationship-edge.md`; guide 06). This is a
strengthening, not proof that every legacy relation has migrated. Endpoint-role
nulls remain observed role data. Prose mentions cannot answer prerequisite,
reverse-edge, cycle or contrast queries.

## cq-coverage

Subject: a competency question and its component/coverage assertion. Legacy
`answers_questions` is a question-text list; current CQ/coverage records add
identity, covered components and scoped assertions. `coverage_assertions[].id`
identifies the assertion, not its parent card. This strengthens queryable CQ
coverage while leaving answerability/verification authority to Slice05.

Open questions: Arc02 must choose authorities and migration form; Slice04 does
not select a schema or claim source-support verification.
