# v4.0 Implementation Slice Recommendations

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice05-implementation-plan-synthesis
artifact: v40-implementation-slice-recommendations
status: proposed-done
```

## Purpose

This artifact recommends bounded future implementation slices with inputs,
outputs, source paths, checks, and commit boundary guidance. It is planning
only and does not edit source.

## Recommended Implementation Slices

### Implementation Slice 01: Skill Entrypoint and Core Guides

Inputs:

- accepted Arc03 conceptual model;
- accepted Arc04 skill architecture;
- Arc05 `v40-implementation-plan.md`;
- Arc05 `v40-source-edit-sequence.md`.

Outputs:

- `knowledge/concept-card-method/SKILL.md`;
- `knowledge/concept-card-method/guides/01-load-contract.md`;
- `knowledge/concept-card-method/guides/02-operator-workflow.md`;
- first cross-link map.

Source path:

- `knowledge/concept-card-method/`.

Checks:

- `make check-skills`;
- targeted grep for reason to load, positive load, negative load, problem
  ownership, dependency direction, adjacent-skill routing, and promise
  boundary;
- source checkout diff review.

Commit boundary:

- one source edit commit for the entrypoint and initial guides only.

### Implementation Slice 02: Method Guides

Inputs:

- Slice01 entrypoint and guide map;
- Arc05 source layout plan;
- Arc05 schema and validation plans.

Outputs:

- extraction guide;
- re-extraction and preservation guide;
- evidence lifecycle guide;
- graph/CQ guide;
- reconciliation guide;
- validation/verification guide;
- memory admission guide;
- maintenance and packaging guide.

Source path:

- `knowledge/concept-card-method/guides/*.md`.

Checks:

- grep for concept card, claim, source support, source span, source locator,
  evidence grade, relationship edge, competency question, extraction run,
  validation result, verification result, reconciliation result,
  preservation decision, and memory admission;
- package-local link check after package target exists, or documented
  deferred package check if package target is later.

Commit boundary:

- one source edit commit for guide content only.

### Implementation Slice 03: Templates and Examples

Inputs:

- Arc05 schema surface plan;
- Arc05 validation review plan;
- Arc05 source edit sequence.

Outputs:

- `guides/templates/*.md`;
- `guides/examples/*.md`;
- release-critical examples for minimal card, claim-backed card, CQ coverage,
  relationship edge, extraction-run trace, reconciliation, memory admission,
  and five-agent default recipe.

Source path:

- `knowledge/concept-card-method/guides/templates/`;
- `knowledge/concept-card-method/guides/examples/`.

Checks:

- grep for required fields and lowercase snake_case enum values;
- review that five-agent workflow is a default recipe, not an invariant;
- review that templates preserve user-authored, trace record, and result
  record surfaces.

Commit boundary:

- one source edit commit for templates and examples.

### Implementation Slice 04: Validation Documentation and Support Docs

Inputs:

- Arc05 validation review plan;
- Arc05 validator-scope decision;
- Arc05 deferral register.

Outputs:

- `guides/validation/structural-candidates.md`;
- `guides/validation/semantic-review-boundary.md`;
- `guides/validation/human-review-boundary.md`;
- `guides/validation/deferred-runtime-checks.md`;
- `guides/reference/field-glossary.md`;
- `guides/reference/source-locator-notes.md`;
- `guides/reference/review-checklist.md`;
- `guides/reference/change-log-notes.md`.

Source path:

- `knowledge/concept-card-method/guides/validation/`;
- `knowledge/concept-card-method/guides/reference/`.

Checks:

- grep for deterministic structural checks, semantic audit, human/operator
  review, deferred runtime, can-prove, cannot-prove, executable
  validator-code deferred, and documentation-only validator scope;
- source checkout diff review.

Commit boundary:

- one source edit commit for validation documentation and support documents.

### Implementation Slice 05: README and Packaging

Inputs:

- Arc05 package update plan;
- Arc05 discoverability plan;
- Arc05 verification gate matrix.

Outputs:

- README skill library and package target updates;
- Makefile target `concept-card-method`;
- package list updates in `INSTALL_ZIPS` and `ALL_SKILL_FILES`;
- `.PHONY`, `skills`, help, install, uninstall, clean behavior updates;
- package-path behavior or exception rows.

Source path:

- `README.md`;
- `Makefile`;
- `package-path-exceptions.tsv` if required.

Checks:

- `make check-skills`;
- `make concept-card-method`;
- generated zip listing for `concept-card-method.zip`;
- `make check-package-paths`;
- installability check accepted by the implementation owner;
- README/library discoverability review.

Commit boundary:

- one source edit commit for README and package mechanics. If package-path
  exception rows are needed, consider a separate commit so exception policy is
  reviewable.

### Implementation Slice 06: Release Gate Evidence and Closure

Inputs:

- completed source implementation commits;
- Arc05 release gate plan;
- implementation owner release policy.

Outputs:

- release-gate transcript;
- final generated zip verification;
- source version-history review;
- implementation close report.

Source path:

- no new source path by default unless a gate failure requires a planned fix.

Checks:

- source checkout clean;
- planning checkout hygiene;
- `make check-skills`;
- `make concept-card-method`;
- generated zip listing;
- `make check-package-paths`;
- installability;
- documentation-only validator scope;
- README/library discoverability;
- version-history checks.

Commit boundary:

- evidence-only planning or close commit unless source fixes are required.
  Source fixes should use a remediation slice rather than broadening the close
  slice.

## Deferral Discipline

Each implementation slice should keep deferred work visible. Deferred
executable validator-code, runtime services, GraphRAG, graph database,
ontology database, memory runtime, CCDP service, live extraction, package
release, and generated release artifact work require an owner, rationale, and
re-entry condition before they can move into implementation scope.
