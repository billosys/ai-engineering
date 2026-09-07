# Slice01 Plan: Record Template Foundation

```yaml
project: project05-concept-card-skill
arc: arc04-concept-card-records-and-examples
slice: slice01-record-template-foundation
status: open
opened: 2026-09-06
depends-on:
  - arc03-concept-cards-skill-core
```

## Scope

Slice01 adds the source-local template foundation for `concept-cards`. It
creates sibling `knowledge/concept-cards/templates/` records and routes them
from the entrypoint while preserving the current Arc03 guides and Project04
sibling support layout.

The template set should make the method directly usable by an assistant or a
human operator without requiring a runtime database or executable validator.
Templates should be Markdown records with YAML frontmatter plus named sections,
following the accepted Project03 schema-surface treatment while translating
stale historical paths into the current `knowledge/concept-cards/templates/`
placement.

## Required Source Changes

Implement, at minimum, these sibling templates:

- `knowledge/concept-cards/templates/concept-card.md`
- `knowledge/concept-cards/templates/claim.md`
- `knowledge/concept-cards/templates/source-locator.md`
- `knowledge/concept-cards/templates/source-support.md`
- `knowledge/concept-cards/templates/relationship-edge.md`
- `knowledge/concept-cards/templates/competency-question.md`
- `knowledge/concept-cards/templates/extraction-run.md`
- `knowledge/concept-cards/templates/validation-result.md`
- `knowledge/concept-cards/templates/verification-result.md`
- `knowledge/concept-cards/templates/reconciliation-result.md`
- `knowledge/concept-cards/templates/preservation-decision.md`
- `knowledge/concept-cards/templates/memory-admission.md`

Update `knowledge/concept-cards/SKILL.md` to route the templates as live
support material, and update `knowledge/concept-cards/version-history.md` with
a compatible minor version bump. Do not add a template-local history file or
duplicate the skill version in template prose.

## Design Requirements

Templates must preserve these distinctions:

- concept card versus claim;
- source support versus source locator/source span and general provenance;
- evidence grade versus extraction confidence;
- validation result versus verification result/state;
- reconciliation result/state versus preservation decision;
- relationship edge support versus endpoint support;
- competency-question coverage versus answerability;
- memory admission versus artifact retention, storage, validation,
  verification, or runtime write.

Templates should include enough fields and named sections for direct use, but
they remain templates, not final schemas or validators. Use placeholders and
stable field names that can later support deterministic structural checks. Avoid
inventing executable behavior, database semantics, package behavior, or memory
runtime behavior.

Where templates reference source inputs, they should route raw PDF, EPUB, HTML,
and converted-source cleanup to `document-extraction` and accept prepared
source outputs as upstream provenance.

## Out Of Scope

Out of scope for Slice01:

- `examples/`;
- schema/reference or validation-review support surfaces beyond what is needed
  to make the templates understandable;
- Makefile package targets, generated zips, package path exceptions,
  README/docs discoverability, and install behavior;
- executable validators, validation scripts, runtime graph services,
  GraphRAG, ontology databases, memory runtime automation, CCDP services, live
  corpus extraction, or package release;
- `knowledge/concept-card-method/` or `knowledge/source-preparation/`.

## Closure Requirements

Slice01 closes when:

- all required template files exist under `knowledge/concept-cards/templates/`;
- `SKILL.md` routes the template support surface and `version-history.md`
  records the change;
- the repository-wide skill version contract is preserved;
- template contents preserve the required construct and lifecycle distinctions;
- document-extraction handoff boundaries are represented where source inputs
  are referenced;
- examples, schema/reference surfaces, package/docs/install work, validators,
  runtime services and old roots remain absent;
- focused validation passes.
