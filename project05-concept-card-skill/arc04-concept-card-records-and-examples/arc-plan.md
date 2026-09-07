# Arc04 Plan: Concept Card Records And Examples

```yaml
project: project05-concept-card-skill
arc: arc04-concept-card-records-and-examples
status: open
opened: 2026-09-06
depends-on:
  - arc03-concept-cards-skill-core
```

## Capability

Arc04 implements the `concept-cards` support surfaces that make the Arc03
guides directly usable: sibling templates, representative examples,
schema/reference material, and validation review surfaces.

This arc translates Project03 v4.0 template, example, schema, and validation
planning evidence into the current `knowledge/concept-cards/` skill name and
post-Project04 sibling layout. Historical paths under `guides/templates`,
`guides/examples`, `guides/reference`, or `guides/validation` are evidence,
not current placement instructions.

## Dependencies

Arc04 consumes:

- Arc03's closed `concept-cards` core guides;
- Arc02's closed `document-extraction` skill and its output/handoff contracts;
- Project03 v4.0 template, example, schema-surface, validation, and skill
  architecture artifacts preserved under Project05 `artifacts/`;
- current Project04 package/layout conventions, especially sibling support
  directories.

Arc04 leaves Makefile package target wiring, generated zips, README/docs
discoverability, install behavior, and package-path validation to Arc05.
Arc04 may create source-local sibling support directories, but it must not
claim package behavior before Arc05 validates and wires those surfaces.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Record Template Foundation | Add sibling `templates/` records for concept cards, claims, source locators/support, relationships, CQs, extraction runs, validation results, verification results, reconciliation results, preservation decisions, and memory admission. Update `SKILL.md` and `version-history.md` routes without adding examples or package wiring. | Arc03 close. |
| Slice02: Representative Examples | Add sibling `examples/` covering the release-critical example set: minimal card, claim-backed card, CQ coverage, relationship/edge, extraction-run trace, reconciliation, memory-admission, and parallel-worker default recipe. Also update bounded availability/handoff wording surfaced by Slice01 so templates and examples are live while schema/reference and validation-review surfaces remain future. | Slice01. |
| Slice03: Schema Reference And Review Surfaces | Add the source-local schema/reference and validation-review surfaces that document field groups, vocabulary, deterministic structural candidates, semantic audit boundaries, and human/operator review gates. | Slice01, Slice02. |

## Arc Exit Criteria

Arc04 closes when:

- all planned slices are CDC-verified;
- `knowledge/concept-cards/` has sibling `templates/`, `examples/`, and
  schema/reference or validation-review support surfaces whose exact placement
  is explicitly justified by the current package contract;
- templates and examples preserve the Arc03 distinctions among cards, claims,
  source support, locators, edges, CQs, extraction runs, validation results,
  verification results, reconciliation results, preservation decisions, and
  memory admission;
- release-critical examples are present or any operator-approved omission has
  an explicit re-entry condition;
- entrypoint and guide availability wording reflects landed Arc04 support
  surfaces without claiming schema/reference or validation-review work before
  Slice03;
- validation/reference material distinguishes deterministic structural checks,
  semantic audit, human/operator review, and deferred runtime checks;
- `concept-cards` examples and templates route raw document cleanup to
  `document-extraction` and consume prepared source outputs as upstream
  provenance where relevant;
- no package/docs/install wiring, executable validator, runtime graph, memory
  runtime, CCDP service, live corpus extraction, `concept-card-method` root, or
  `source-preparation` root is claimed as complete in this arc.

## Version History

### v1.0 - 2026-09-06

Opened Arc04 after Arc03 closure. Planned source-local support surfaces for
the live `concept-cards` skill: record templates, representative examples,
schema/reference material, and validation review surfaces.

### v1.1 - 2026-09-06

Slice01 CDC verification closed the record template foundation and surfaced
stale guide availability wording for newly live templates. Slice02 scope now
includes bounded availability/handoff cleanup while examples land, without
changing the roadmap, reducing scope, or moving schema/reference and
validation-review work out of Slice03.
