# Operator-Accepted Project05 Reorientation

```yaml
project: project05-concept-card-skill
artifact: operator-accepted-project05-reorientation
status: operator-accepted planning input
accepted_on: 2026-09-06
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Accepted Corrections

Project05 began before Project04 completed a large repository reorganization.
Therefore, Project05's seed artifacts are useful evidence but do not
necessarily represent the latest repository organization.

The operator accepted these corrections before opening Project05:

- Current Project04 layout conventions supersede old Project03/Project05
  package workarounds.
- Guides should remain single-purpose; templates, examples, and other support
  material should live in sibling directories when the skill needs them.
- `source-preparation` is renamed to `document-extraction` because the skill
  should stand alone for PDF, EPUB, HTML, converted Markdown, indexing,
  reading, review, and downstream method use.
- `concept-card-method` is renamed to `concept-cards` for the live skill.
- `ontology-engineering` is reserved as a likely future composite skill that
  may route among concept cards, NeON-style methods, competency questions,
  ontology lifecycle work, alignment, and graph/knowledge modeling.
- The first Project05 work should be readiness and inventory, but not as a
  path to deferring the key implementation objectives.

## Nondeferrable Project05 Direction

Project05 must create at least two detailed live skills:

- `document-extraction`
- `concept-cards`

Later sessions must not convert these into planning-only artifacts or defer the
core implementation without explicit operator approval recorded in Project05.

Permitted deferrals are limited to adjacent future systems that are not needed
for the two skills to exist and be usable, such as executable validators,
runtime services, graph databases, ontology databases, GraphRAG integrations,
CCDP service integration, memory runtime automation, CI expansion, or release
publishing outside repository-local validation gates.

## Planning Consequence

The Project05 plan-of-record should:

- treat copied Project03 artifacts as evidence and provenance;
- treat Project04's closed layout as the current source/package authority;
- open with a readiness and scope-lock arc;
- make `document-extraction` an upstream sibling skill, not a subdirectory of
  `concept-cards`;
- implement `concept-cards` as the concept-card v4.0 method skill; and
- reserve `ontology-engineering` for a later possible composite skill unless
  the operator expands Project05.
