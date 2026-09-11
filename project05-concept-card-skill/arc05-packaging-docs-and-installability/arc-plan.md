# Arc05 Plan: Packaging, Docs, And Installability

```yaml
project: project05-concept-card-skill
arc: arc05-packaging-docs-and-installability
status: closed
opened: 2026-09-10
depends-on:
  - arc02-document-extraction-skill
  - arc03-concept-cards-skill-core
  - arc04-concept-card-records-and-examples
```

## Capability

Arc05 turns the two live source skills into repository-supported installable
skills. It wires `document-extraction` and `concept-cards` into Makefile
package targets, generated skill zips, install behavior, README/docs
discoverability, package-path validation, and inspected installed contents.

This arc is nondeferrable for Project05. It must not report either skill as
installable until the generated package contents and an install destination are
inspected.

## Dependencies

Arc05 consumes:

- Arc02's `knowledge/document-extraction/` source skill, including sibling
  `templates/` and `examples/`;
- Arc03 and Arc04's `knowledge/concept-cards/` source skill, including sibling
  `templates/`, `examples/`, and `references/`;
- current Makefile packaging helpers and validation scripts;
- repository docs for skill-library discoverability and building/installing.

Arc05 leaves final project close, whole-project ledger reconciliation, and any
operator-facing final deferral statement to Arc06.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Package Targets And Support Directories | Add Makefile/package wiring for `document-extraction` and `concept-cards`; ensure generated zips include `guides/`, `version-history.md`, `templates/`, `examples/`, and `concept-cards/references/` where present; update skill/version gates only as needed for the new packages. | Arc04 close. |
| Slice02: Docs And Discoverability | Update README/docs skill-library/building/installing/anatomy surfaces so both new method skills are discoverable as current installable packages, with boundaries for package contents and no stale planned-method language. | Slice01. |
| Slice03: Package Validation And Install Smoke | Run package-path and install-oriented gates, inspect generated zip contents for both skills, install to an isolated destination, inspect installed contents, reconcile package/docs claims, and record any explicit Arc06 closure inputs. | Slice01, Slice02. |

## Arc Exit Criteria

Arc05 closes when:

- both `document-extraction.zip` and `concept-cards.zip` are produced by
  Makefile targets and included in aggregate build/install lists;
- generated packages contain the intended entrypoint, sibling
  `version-history.md`, `guides/`, `templates/`, `examples/`, and any planned
  package-supported `references/` directory;
- `make print-skill-zips`, `make all`, `make check-skills`,
  `make check-skill-versions`, and `make check-package-paths` account for both
  new skills;
- docs and README discoverability list both skills as live installable method
  skills rather than planned material;
- an isolated install smoke demonstrates both skills unpack into the install
  destination with their support directories present;
- source and package-local Markdown links for the new skills are validated or
  explicitly dispositioned;
- no runtime service, executable validator, live-corpus extraction, memory
  runtime, graph database, ontology database, GraphRAG integration, CCDP
  service, or release publishing outside repository-local gates is claimed as
  complete.

## Version History

### v1.0 - 2026-09-10

Opened Arc05 after Arc04 closure. The arc is planned as three slices:
package targets/support directories, docs/discoverability, and package
validation/install smoke.

### v1.1 - 2026-09-11

Slice03 CDC verification closed package validation and install smoke after a
narrow CDC repair corrected remaining live-guide Slice02 discoverability
wording. Arc05 is closed and Arc06 is opened for final project-level gate
evidence, ledger reconciliation, explicit deferral/no-op statement, and
Project05 closure.
