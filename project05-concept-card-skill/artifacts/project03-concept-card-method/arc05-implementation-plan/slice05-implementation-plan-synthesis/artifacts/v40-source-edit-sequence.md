# v4.0 Source Edit Sequence

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice05-implementation-plan-synthesis
artifact: v40-source-edit-sequence
status: proposed-done
planned-source-home: knowledge/concept-card-method/
```

## Purpose

This artifact defines the future source edit sequence for implementing the
v4.0 concept-card method skill. It is a source edit sequence, not source
implementation. It does not edit source and does not claim release readiness.

## Sequence

### 1. Establish Source Home

Create `knowledge/concept-card-method/` in the source checkout only in a
future implementation slice that authorizes source edits.

Required source paths:

- `knowledge/concept-card-method/SKILL.md`;
- `knowledge/concept-card-method/guides/`;
- `knowledge/concept-card-method/guides/templates/`;
- `knowledge/concept-card-method/guides/examples/`;
- `knowledge/concept-card-method/guides/validation/`;
- `knowledge/concept-card-method/guides/reference/`.

### 2. Add Thin Entrypoint

Create `knowledge/concept-card-method/SKILL.md` with:

- `name: concept-card-method`;
- reason to load;
- positive load cases;
- negative load cases;
- problem ownership;
- dependency direction;
- adjacent-skill routing;
- guide map;
- package promise boundary;
- documentation-only validator scope;
- local version history.

### 3. Add Guides

Create guide files under `guides/`:

- `01-load-contract.md`;
- `02-operator-workflow.md`;
- `03-extraction.md`;
- `04-re-extraction-preservation.md`;
- `05-evidence-lifecycle.md`;
- `06-graph-cq.md`;
- `07-reconciliation.md`;
- `08-validation-verification.md`;
- `09-memory-admission.md`;
- `10-maintenance-packaging.md`.

Each guide should link only to package-local surfaces unless a package-path
exception is explicitly justified.

### 4. Add Templates

Create package-compatible template files under `guides/templates/`:

- `concept-card.md`;
- `claim-source-support.md`;
- `competency-question.md`;
- `relationship-edge.md`;
- `extraction-run.md`;
- `validation-result.md`;
- `verification-result.md`;
- `reconciliation-result.md`;
- `preservation-decision.md`;
- `memory-admission.md`.

Templates should use Markdown records with YAML frontmatter and lowercase
snake_case enum values from the Slice03 plan.

### 5. Add Examples

Create package-compatible example files under `guides/examples/`:

- `minimal-card.md`;
- `claim-backed-card.md`;
- `cq-coverage.md`;
- `relationship-edge.md`;
- `extraction-run-trace.md`;
- `reconciliation.md`;
- `memory-admission.md`;
- `five-agent-default-recipe.md`.

Examples should be release-critical unless the future implementation records a
specific deferral with owner, rationale, and re-entry condition.

### 6. Add Validation Documentation

Create validation documentation under `guides/validation/`:

- `structural-candidates.md`;
- `semantic-review-boundary.md`;
- `human-review-boundary.md`;
- `deferred-runtime-checks.md`.

This step documents deterministic validation candidates and review boundaries.
It does not implement executable validator-code.

### 7. Add Support Documents

Create support document files under `guides/reference/`:

- `field-glossary.md`;
- `source-locator-notes.md`;
- `review-checklist.md`;
- `change-log-notes.md`.

These support documents should preserve source span, source locator, review,
and version history obligations without adding runtime behavior.

### 8. Update README

Update `README.md` only in an authorized implementation slice:

- add the concept-card method skill to the skill library;
- update any knowledge skill count if present;
- explain README/library discoverability for the reason to load;
- document package expectation for `concept-card-method.zip`;
- mention `make concept-card-method`, `make check-skills`, and
  `make check-package-paths`;
- preserve the promise boundary around documentation-only validator scope,
  generated zips, package release, release readiness, runtime services,
  GraphRAG, graph database, ontology database, memory runtime, CCDP service,
  and live extraction.

### 9. Update Makefile and Package Lists

Update `Makefile` only in an authorized implementation slice:

- add `concept-card-method.zip` to `INSTALL_ZIPS`;
- add `knowledge/concept-card-method/SKILL.md` to `ALL_SKILL_FILES`;
- add `concept-card-method` to `.PHONY`;
- add `concept-card-method` to the `skills` aggregate;
- add help text for the package target;
- reuse the existing `pack_skill` behavior where possible;
- keep `make clean` behavior limited to ignored build output and generated
  zip artifacts.

### 10. Check Package-Path Behavior

Prefer package-local links that resolve inside `concept-card-method/`.

Edit `package-path-exceptions.tsv` only if an intentional source-only or
excluded target cannot be represented as a package-local link. Any exception
row must include package, document, target, classification, disposition,
reason, source, and expires.

### 11. Build and Inspect Generated Zip

Run future generated zip verification after source changes:

- `make concept-card-method`;
- inspect `concept-card-method.zip`;
- confirm it contains `concept-card-method/SKILL.md`;
- confirm it contains `concept-card-method/guides/**`;
- confirm templates, examples, validation documentation, and support documents
  are included through `guides/`;
- confirm generated zips stay ignored and are not committed unless a later
  release owner explicitly changes policy.

### 12. Record Source Version-History Obligations

Record source version history for:

- `knowledge/concept-card-method/SKILL.md`;
- guide files;
- template files;
- example files;
- validation documentation;
- support document files;
- `README.md`;
- `Makefile`;
- any `package-path-exceptions.tsv` change.

If a touched file has no local history, name the enclosing version history
surface before the implementation commit.

## Boundary

This source edit sequence is planning only. It does not edit source,
implement tests, create generated zips, perform package release, implement
executable validator-code, create runtime services, claim release readiness,
or modify CI.
