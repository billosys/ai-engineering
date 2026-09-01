# Slice 03: Skill Kind and Topology Classification

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice03-skill-topology-classification
status: open
opened-on: 2026-09-01
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
```

## Goal

Define and apply a decision instrument for classifying the repository's skill
surfaces by two independent axes:

- skill or knowledge kind; and
- composition topology: atomic, composite, bridge/integration layer, or
  application/task bundle.

This slice answers: what kinds of skills and support surfaces does Project04
actually need to name, which current and planned surfaces are atomic or
composite, and what public vocabulary should Arc05 later use or avoid?

## Scope

In scope:

- Consume the verified Slice01 source inventory artifacts.
- Consume the verified Slice02 imported-architecture and conflict/question
  artifacts.
- Consume the project-level external ontology rubric research as input, not as
  accepted taxonomy.
- Inspect the live source checkout as needed for current skill surfaces:
  top-level `SKILL.md`, `README.md`, `knowledge/*/SKILL*.md`, `knowledge/*/`,
  `templates/`, `protocols/`, `Makefile`, and package-path validation surfaces.
- Classify current and planned skill surfaces by kind and topology.
- Treat Rust as the candidate atomic domain/tooling anchor and
  `collaboration-framework` as the accepted composite framework/operational
  anchor.
- Assess required edge cases: `concept-card-method`, `knowledge/biome/`,
  `knowledge/js/` plus `knowledge/deno/` plus `knowledge/biome/`, Project02
  specialist framework components, CCDP, and template/support surfaces.
- Produce durable artifacts under this slice's `artifacts/` directory.
- Identify public-language implications and Arc02 directory-contract inputs
  without deciding final source roots.

Out of scope:

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, or generated
  zips.
- Writing final public documentation.
- Deciding Arc02's final target directory contract.
- Treating the external ontology rubric as accepted without testing it against
  current and planned repository surfaces.
- Re-opening Project02 or Project03 accepted architecture except to record a
  classification conflict or re-entry condition.

## Artifacts

Expected artifact home: `artifacts/`.

Expected artifacts:

- `artifacts/skill-kind-topology-decision-instrument.md`
- `artifacts/skill-kind-topology-classification-matrix.md`
- `artifacts/public-language-implications.md`

## Verification Approach

Use planning-tree and source-checkout inspection with targeted `rg` checks.
The artifacts should cite concrete paths, distinguish source-backed current
surfaces from planned surfaces, and explicitly separate the kind axis from the
topology axis. The final close must show that every ledger row was satisfied
by evidence in the artifacts.

## Exit Criteria

- The classification decision instrument defines the kind axis and topology
  axis separately, with evidence questions and classification rules.
- The classification matrix covers current packaged skill surfaces, planned
  Project02 framework components, planned Project03 `concept-card-method`,
  CCDP, and template/support surfaces.
- Rust is assessed as the atomic anchor and `collaboration-framework` as the
  composite anchor, with evidence and caveats.
- Edge cases are explicitly tested rather than smoothed over.
- Public-language implications identify vocabulary to use, vocabulary to avoid,
  and questions for Arc02 and Arc05.
- No source checkout files are edited.

## Version History

### v1.0 - 2026-09-01

Opened Slice03 as the skill kind and atomic/composite topology classification
pass for Project04 Arc01.
