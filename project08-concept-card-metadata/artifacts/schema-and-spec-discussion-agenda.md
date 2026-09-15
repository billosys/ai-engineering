# Schema And Specification Discussion Agenda

Date: 2026-09-14.
Status: operator-requested discussion checkpoint; design questions are open.
Owner: Arc06 Slice11 prepares the handoff; Arc02 owns the design decisions.
Gate: [project-plan.md](../project-plan.md), project ledger P-15.

## Why This Is Explicit

The project already assigned schema/validator choices to Arc02. The operator
now explicitly asks to review schemas together and discuss creating a spec
before anything is finalized or formalized as the metadata contract. This
agenda preserves that request; it is not the specification or an approved
schema design. Evidence remediation and exploratory comparison may continue.

The current source concept-cards SKILL describes templates and review
conventions, not executable schemas or a finalized specification. Treat
historical prompts, current templates and populated outputs as separate
evidence surfaces; none wins by default.

## Proposed Discussion Structure

Start with concrete historical and current cards, then examine three connected
layers. These are discussion categories, not selected implementation components.

1. Semantic model: what the entities, fields and relationships mean; which
   information belongs to a concept, card revision, source, claim or assessment.
2. Machine-checkable schemas: the permitted structures and values, presence/
   null/empty rules, extensions and reference constraints we choose to enforce.
3. Readable specification: the shared contract explaining meanings, authority,
   invariants, processing behavior, compatibility and conformance, with examples.

Discuss how these layers relate and which is authoritative for each kind of
rule. A schema passing does not establish source truth or teaching quality.
A written example should not silently establish a mandatory field or enum.

## Questions To Resolve Together

- Scope: one concept-card specification, a set of related record specifications,
  or a core profile with optional extensions? Which use cases need lightweight
  card-local metadata and which justify separate records?
- Identity and graph use: stable IDs versus slugs/paths/revisions; directly
  queryable relationship assertions; direction, inverse views, uncertainty and
  support; authority when both card-local lists and edge records exist.
- Source generality: works/resources, editions/snapshots, formats, locators and
  attribution across books, papers, white papers, blogs and wiki articles.
- Discovery and pedagogy: tagging, taxonomic structures and teaching depth
  without requiring one domain's category/subcategory/tier structure.
- Questions and lifecycle: clear field names, competency-question linkage,
  evidence and confidence, result references versus summaries, stale/conflict/
  unknown states, and no information loss or implied memory admission.
- Body/metadata contract: readable teaching bodies, source-grounded examples,
  common errors, construction/recognition and rich relationships, with explicit
  boundaries on what is authoritative or machine-queryable.
- Conformance: required versus optional/conditional fields; absent/null/empty;
  unknown fields; extensibility; diagnostics; structural validity versus
  reference resolution versus semantic verification and operator acceptance.
- Representation: candidate schema languages or constraint systems, YAML/
  Markdown handling and graph interoperability. Compare practical tradeoffs
  after primary-source research; no technology is selected by this agenda.
- Compatibility: historical-to-current mappings, loss reporting, reversible
  transforms where feasible, schema/spec identifiers versus skill versions,
  migration policy and the existing 4.x / intended 4.9.x delivery constraint.
- Delivery: spec format, canonical location, examples, conformance fixtures,
  validator responsibilities, ownership and how to prevent duplicated rules
  drifting across guidance, templates, schemas and specification.

## Discussion Inputs And Decision Record

Bring a compact comparison of representative historical music/Erlang and
current minimal/rich cards and related records, with the relevant semantic
findings and actual lookup use cases. Preserve unsupported/contradictory cells;
do not beautify examples into evidence of an already accepted model.

The later discussion packet should offer alternatives, costs, unanswered
questions and a provisional spec outline. It need not wait to begin informal
conversation, but final architecture still requires Arc06's composed evidence.

Record the operator's decisions on scope, schema/spec form, authority,
deliverables and acceptance checks before normative adoption or implementation
as the accepted contract. Do not manufacture approval from this agenda, the
remediation authorization, CC self-attestation or the passage of later slices.
P-15 remains open until both the discussion and agreed delivery are evidenced.

Arc04 remains able to expose and fix body/metadata design problems. Return
material changes to this discussion gate before promoting them to normative
rules; preserve all repeated-run and operator quality gates.
