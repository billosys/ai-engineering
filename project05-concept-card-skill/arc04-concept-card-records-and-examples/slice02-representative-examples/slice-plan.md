# Slice02 Plan: Representative Examples

```yaml
project: project05-concept-card-skill
arc: arc04-concept-card-records-and-examples
slice: slice02-representative-examples
status: open
opened: 2026-09-06
depends-on:
  - slice01-record-template-foundation
```

## Scope

Slice02 adds the release-critical example set for the `concept-cards` skill
under sibling `knowledge/concept-cards/examples/`. The examples should make the
Arc03 guides and Slice01 templates concrete enough for direct assistant use and
human-assisted review, while remaining synthetic or explicitly scoped so they
do not claim real corpus verification.

Slice02 also performs the bounded availability/handoff cleanup surfaced by
Slice01 CDC verification: existing guide text should no longer say templates
are future or unavailable, and after this slice lands it should not say
examples are future or unavailable. Schema/reference and validation-review
support remain future until Slice03.

## Required Source Changes

Implement, at minimum, these sibling examples:

- `knowledge/concept-cards/examples/minimal-card.md`
- `knowledge/concept-cards/examples/claim-backed-card.md`
- `knowledge/concept-cards/examples/cq-coverage.md`
- `knowledge/concept-cards/examples/relationship-edge.md`
- `knowledge/concept-cards/examples/extraction-run-trace.md`
- `knowledge/concept-cards/examples/reconciliation.md`
- `knowledge/concept-cards/examples/memory-admission.md`
- `knowledge/concept-cards/examples/parallel-worker-default-recipe.md`

Update `knowledge/concept-cards/SKILL.md` to route the examples as live
support material, and update `knowledge/concept-cards/version-history.md` with
a compatible minor version bump.

Update only the bounded availability/handoff wording needed in existing
`knowledge/concept-cards/guides/` files so live templates and examples are not
described as future, while schema/reference and validation-review support
remain future.

## Example Requirements

Examples must preserve:

- user-authored, trace-record, and result-record surface classes;
- concept card, claim, source support, source locator/source span,
  relationship edge, competency question, extraction run, validation result,
  verification result, reconciliation result, preservation decision, and memory
  admission as distinct constructs;
- evidence grade, extraction confidence, validation result, verification
  state/result, reconciliation state/result, preservation decision, and memory
  admission as distinct lifecycle concerns;
- relationship edge support as distinct from endpoint support;
- CQ coverage as distinct from answerability and retrieval observations;
- the five-agent workflow as a default recipe, not an invariant, with actual
  worker scope recorded in the extraction-run trace;
- document-extraction outputs as upstream provenance, not claim support or raw
  source cleanup owned by `concept-cards`.

Use examples that are readable and representative. Synthetic examples are
acceptable and should be labeled as synthetic. If any example uses real source
material, quote within copyright limits and record source identity, access, and
review limits precisely.

## Out Of Scope

Out of scope for Slice02:

- schema/reference and validation-review support surfaces;
- Makefile package targets, generated zips, package path exceptions,
  README/docs discoverability, and install behavior;
- executable validators, validation scripts, runtime graph services,
  GraphRAG, ontology databases, memory runtime automation, CCDP services, live
  corpus extraction, or package release;
- `knowledge/concept-card-method/` or `knowledge/source-preparation/`.

## Closure Requirements

Slice02 closes when:

- all required example files exist under `knowledge/concept-cards/examples/`;
- `SKILL.md` routes the example support surface and `version-history.md`
  records the change;
- bounded guide availability/handoff wording is current for live templates and
  examples, while schema/reference and validation-review support remain future;
- examples preserve the required construct and lifecycle distinctions;
- document-extraction handoff boundaries are represented where source inputs
  are referenced;
- schema/reference surfaces, package/docs/install work, validators, runtime
  services and old roots remain absent;
- focused validation passes.
