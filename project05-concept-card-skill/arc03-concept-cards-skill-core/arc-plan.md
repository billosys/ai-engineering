# Arc03 Plan: Concept Cards Skill Core

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
status: open
opened: 2026-09-06
depends-on:
  - arc01-readiness-and-scope-lock
  - arc02-document-extraction-skill
```

## Capability

Arc03 implements the core `concept-cards` skill source: a detailed standalone
method skill for creating, re-extracting, validating, reconciling, preserving,
and using provenance-bearing concept cards.

This arc owns the skill entrypoint and concern-based guides. It translates the
closed Project03 v4.0 planning work from the historical `concept-card-method`
name into the current `concept-cards` skill and post-Project04 sibling layout.

## Dependencies

Arc03 consumes:

- Project05 Arc01 readiness artifacts, especially the accepted names
  `document-extraction` and `concept-cards`;
- Arc02's closed `document-extraction` source skill, because `concept-cards`
  routes raw PDF/EPUB/HTML and converted-source preparation to it;
- Project03's closed v4.0 conceptual model, skill architecture, and
  implementation-planning artifacts;
- current Project04 package/layout conventions.

Arc03 leaves templates, examples, schema/reference material, and validation
review surfaces to Arc04. It leaves Makefile, docs, package target, generated
zip, and install wiring to Arc05.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Source Scaffold And Load Contract | Create the `knowledge/concept-cards/` source root with entrypoint, version history, load contract, operator workflow, guide map, and future-route boundaries. | Arc02 close. |
| Slice02: Extraction, Re-Extraction, And Provenance | Add core guides for source-faithful extraction, re-extraction, preservation decisions, source spans, source support, and extraction-run provenance. | Slice01. |
| Slice03: Evidence, Validation, And Verification | Add guides for evidence lifecycle, extraction confidence, evidence grade, validation results, verification results, and review boundaries without collapsing these states. | Slice01, Slice02. |
| Slice04: Relationships, CQs, Reconciliation, And Memory | Add guides for relationship edges, competency questions, graph/CQ coverage, reconciliation, memory admission, and maintenance/promise boundaries. | Slice01, Slice02, Slice03. |

## Arc Exit Criteria

Arc03 closes when:

- all planned slices are CDC-verified;
- `knowledge/concept-cards/` exists with `SKILL.md`, sibling
  `version-history.md`, and focused `guides/`;
- the skill preserves Project03 v4.0 distinctions among concept card, claim,
  source support, source span/source locator, relationship edge, competency
  question, extraction run, validation result, verification result,
  reconciliation result, preservation decision, and memory admission;
- evidence grade, extraction confidence, validation result, verification
  state/result, reconciliation state/result, and memory admission remain
  distinct;
- `concept-cards` routes raw document cleanup and extraction preparation to
  `document-extraction` and consumes prepared outputs as upstream provenance;
- the historical `concept-card-method` root is not introduced;
- no templates/examples/package/docs/install wiring are claimed as complete in
  this arc.

## Version History

### v1.0 - 2026-09-06

Opened Arc03 after Arc02 closure. Planned the implementation sequence for the
live `concept-cards` skill core, translating Project03 evidence through
Project05 naming and layout decisions.
