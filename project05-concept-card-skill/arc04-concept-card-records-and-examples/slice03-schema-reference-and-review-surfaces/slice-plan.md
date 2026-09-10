# Slice03 Plan: Schema Reference And Review Surfaces

```yaml
project: project05-concept-card-skill
arc: arc04-concept-card-records-and-examples
slice: slice03-schema-reference-and-review-surfaces
status: open
opened: 2026-09-10
depends-on:
  - slice01-record-template-foundation
  - slice02-representative-examples
```

## Scope

Slice03 adds the source-local schema/reference and validation-review support
surfaces for `concept-cards` under sibling
`knowledge/concept-cards/references/`.

The path choice is intentional: current Project05 layout keeps support
material as skill-root siblings rather than burying it under `guides/` for
packaging convenience. Current Makefile helper macros already copy `guides/`,
`templates/`, and `examples/` for component-style skills but do not yet copy a
`references/` directory. Slice03 must therefore record this as an Arc05
package-support requirement while making no package/install claim in this
slice.

## Required Source Changes

Implement, at minimum, these sibling reference files:

- `knowledge/concept-cards/references/README.md`
- `knowledge/concept-cards/references/record-field-groups.md`
- `knowledge/concept-cards/references/vocabulary.md`
- `knowledge/concept-cards/references/structural-validation-candidates.md`
- `knowledge/concept-cards/references/semantic-audit-boundaries.md`
- `knowledge/concept-cards/references/operator-review-gates.md`

Update `knowledge/concept-cards/SKILL.md` to route the reference/review support
surface as live source material. Update `knowledge/concept-cards/version-history.md`
with a compatible minor version bump. Update bounded availability/handoff
wording in existing guides so schema/reference and validation-review support
is no longer described as future after this slice lands.

## Design Requirements

Reference and review surfaces must document:

- record field groups for cards, claims, source support, source locators/spans,
  relationship edges, CQs, extraction runs, validation results, verification
  results, reconciliation results, preservation decisions, and memory
  admission;
- vocabulary or enum-like terms used by templates and examples without
  claiming a finalized executable schema;
- deterministic structural validation candidates, including required fields,
  required sections, reference presence, local graph closure, source-support
  presence, CQ coverage references, preservation decision records, memory
  admission gate fields, path/slug hygiene, and obvious consistency;
- semantic audit boundaries, including source-support warrant, evidence grade
  adequacy, extraction confidence calibration, relationship meaning, CQ
  answerability, reconciliation rationale, and preservation rationale;
- human/operator review gates for memory admission, conflict disposition,
  preservation exceptions, material uncertainty, and method exceptions;
- deferred runtime checks, including graph databases, GraphRAG, ontology
  databases, memory runtime enforcement, CCDP service orchestration, and live
  corpus extraction.

These surfaces are Markdown reference/review material, not executable
validators, JSON Schema, runtime services, or proof that validation or
verification was performed.

## Out Of Scope

Out of scope for Slice03:

- Makefile package targets, generated zips, package path exceptions,
  README/docs discoverability, and install behavior;
- executable validators, validation scripts, JSON Schema, runtime graph
  services, GraphRAG, ontology databases, memory runtime automation, CCDP
  services, live corpus extraction, or package release;
- new examples or templates except bounded cross-link updates if needed;
- `knowledge/concept-card-method/` or `knowledge/source-preparation/`.

## Closure Requirements

Slice03 closes when:

- all required `references/` files exist under `knowledge/concept-cards/`;
- `SKILL.md` routes the reference/review support surface and
  `version-history.md` records the change;
- guide availability/handoff wording is current for live templates, examples,
  and references;
- reference/review surfaces preserve the required construct and lifecycle
  distinctions;
- deterministic validation, semantic audit, human/operator review, and
  deferred runtime boundaries are explicit;
- the Arc05 package-support requirement for `references/` is recorded without
  claiming package/install behavior;
- package/docs/install work, executable validators, runtime services and old
  roots remain absent;
- focused validation passes.
