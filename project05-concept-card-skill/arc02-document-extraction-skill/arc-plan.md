# Arc02 Plan: Document Extraction Skill

```yaml
project: project05-concept-card-skill
arc: arc02-document-extraction-skill
status: open
opened: 2026-09-06
depends-on:
  - arc01-readiness-and-scope-lock
```

## Capability

Arc02 implements `document-extraction` as a detailed standalone skill for
turning PDF, EPUB, HTML, converted Markdown, and converter-produced source
bundles into usable Markdown, structure maps, media references, locators,
manifests, readiness reports, and caveat records.

The skill must be useful on its own for indexing, reading, review, and ordinary
analysis, while also producing outputs that `concept-cards` can consume as
upstream provenance.

## Dependencies

Arc02 consumes:

- Project05 Arc01 readiness artifacts, especially package surface
  requirements and naming/scope boundaries;
- `artifacts/operator-accepted-src-prep-arch.md`, with its old
  `source-preparation` name translated to `document-extraction`;
- historical PDF and EPUB prompts under `old/dev/concept-cards/`;
- current Project04 package/layout conventions.

Arc02 leaves Makefile, docs, package target, generated zip, and install wiring
to Arc05 unless a slice explicitly adds a source-local support file that
requires earlier package behavior.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Source Scaffold And Load Contract | Create the `knowledge/document-extraction/` source root with entrypoint, version history, load contract, workflow guide, and output contract. | Arc01 close. |
| Slice02: Format Preparation Guides | Add detailed PDF/Marker and EPUB/pandoc preparation guides by modernizing the preserved v2 prompts. | Slice01. |
| Slice03: Structure, Media, Locators, And Reports | Add shared guides for HTML/converted Markdown handling, media normalization, structure mapping/splitting, locator semantics, validation/readiness reports, and caveats. | Slice01, Slice02. |
| Slice04: Templates And Examples | Add sibling templates and examples for manifests, structure maps, locator maps, media reports, validation/readiness reports, caveat records, and downstream `concept-cards` consumption. | Slice01, Slice02, Slice03. |

## Arc Exit Criteria

Arc02 closes when:

- all planned slices are CDC-verified;
- `knowledge/document-extraction/` exists with `SKILL.md`,
  `version-history.md`, focused `guides/`, sibling `templates/`, and sibling
  `examples/`;
- the skill supports human-assisted and agent-direct use;
- PDF, EPUB, HTML, and converted-Markdown guidance are represented;
- output contracts cover downstream concept-card extraction and standalone
  indexing, reading, and review;
- no superseded `knowledge/source-preparation/` root is introduced.

## Version History

### v1.0 - 2026-09-06

Opened Arc02 after Arc01 closure. Planned the implementation sequence for the
live `document-extraction` skill.
