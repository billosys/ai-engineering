# Arc 01: Repository Material Inventory and Classification

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
status: active
opened-on: 2026-09-01
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
```

## Capability

Arc01 produces the source-backed evidence base for Project04. It inventories
the repository's current documentation, knowledge-library, template, protocol,
skill, README, package, and validation surfaces; classifies each material by
role; assesses imported Project02/Project03 planning inputs; and defines a
testable skill-topology model for atomic and composite skills.

This arc does not move source files or write final public documentation. Its
job is to make the later directory contract and migration plan evidence-based.

## Inputs

- Project04 `project-plan.md` and project `ledger.md`.
- Project-level imported artifacts under `artifacts/`.
- Project-level external rubric research:
  `artifacts/external-ontology-rubric-research.md`.
- Source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.
- Current `README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`,
  `protocols/`, `Makefile`, `package-path-exceptions.tsv`, and validation
  scripts.
- Project02 accepted collaboration-framework component architecture.
- Project03 accepted method-skill vocabulary and concept-card method planning
  boundary.

## Boundaries

In scope:

- Read-only inventory of live source files and directories.
- Classification of material roles: end-user docs, knowledge substrate, skill
  entrypoint, framework/operational material, method material, protocol
  distribution, template/support asset, package/release gate, compatibility
  surface, and scratch/workbench material.
- Classification of skill kind and skill topology, keeping the kind axis
  separate from the atomic/composite topology axis.
- Assessment of imported Project02 and Project03 materials as inputs to
  Project04, including any conflicts with the new docs/knowledge-library
  direction.
- Open question and decision-register preparation for Arc02.

Out of scope:

- Moving, deleting, or renaming source files.
- Editing source `README.md`, source `SKILL.md`, `docs/`, `knowledge/`,
  `templates/`, `protocols/`, `Makefile`, package-path exceptions, or generated
  zips.
- Writing final end-user docs.
- Selecting the final directory contract before the full inventory and topology
  classification exist.
- Re-opening Project02 or Project03 decisions except to record Project04
  integration questions.

## Slice Breakdown

### Slice 01: Source Surface Inventory

Status: verified-closed on 2026-09-01.

Scope: inventory the live source checkout and produce a file/directory surface
map for `README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`,
`protocols/`, `Makefile`, package-path exceptions, validation scripts, and
top-level compatibility files.

Expected artifacts:

- `slice01-source-surface-inventory/artifacts/current-source-surface-map.md`
- `slice01-source-surface-inventory/artifacts/material-role-classification.md`
- `slice01-source-surface-inventory/artifacts/source-validation-surface-map.md`

### Slice 02: Imported Architecture and Prior Proposal Integration

Status: verified-closed on 2026-09-01.

Scope: assess Project04 project-level artifacts copied from Project02 and any
Project03 method-skill inputs. Identify accepted facts, source-layout
hypotheses, package/readme/link constraints, and conflicts introduced by the
Project04 docs/knowledge-library direction.

Expected artifacts:

- `slice02-imported-architecture-integration/artifacts/imported-architecture-evidence-map.md`
- `slice02-imported-architecture-integration/artifacts/prior-proposal-register.md`
- `slice02-imported-architecture-integration/artifacts/project04-integration-conflicts-and-questions.md`

### Slice 03: Skill Kind and Topology Classification

Status: verified-closed on 2026-09-01.

Scope: define the decision instrument for skill kind and skill topology, then
classify current and planned skill surfaces. Treat Rust as the candidate atomic
skill anchor and `collaboration-framework` as the accepted composite skill
anchor; test whether other domain/tooling, framework/operational, method, and
protocol/support surfaces fit those examples or require new vocabulary.

Expected artifacts:

- `slice03-skill-topology-classification/artifacts/skill-kind-topology-decision-instrument.md`
- `slice03-skill-topology-classification/artifacts/skill-kind-topology-classification-matrix.md`
- `slice03-skill-topology-classification/artifacts/public-language-implications.md`

### Slice 04: Arc01 Synthesis for Directory Contract

Status: open as of 2026-09-01.

Scope: synthesize the source inventory, imported-material assessment, and
skill-topology classification into a compact Arc02 input packet. The synthesis
must distinguish accepted facts, working hypotheses, unresolved decisions,
source-edit risks, and validation obligations.

Expected outputs include an Arc02 readiness packet and a directory-contract
requirements list.

## Dependencies

- Slice01 precedes all later Arc01 slices because the imported architecture and
  topology model must be tested against the live source surface.
- Slice02 and Slice03 can proceed after Slice01 closes; their findings compose
  in Slice04.
- Arc02 must not open until Slice04 closes or the operator explicitly accepts a
  narrower Arc02 input set.

## Version History

### v1.0 - 2026-09-01

Opened Arc01 for read-only repository material inventory and classification,
including the newly required atomic/composite skill-topology assessment.

### v1.1 - 2026-09-01

Added the project-level external ontology rubric research note as an explicit
input to Slice03's skill kind and topology classification work.

### v1.2 - 2026-09-01

Recorded Slice01 as verified-closed and opened Slice02,
`slice02-imported-architecture-integration`, for Project02/Project03 prior
proposal integration and Arc02 question preparation.

### v1.3 - 2026-09-01

Recorded Slice02 as verified-closed. No slice-breakdown or sequencing change
was required before Slice03; Slice02 produced the expected imported-material
evidence and Arc02 question inputs.

### v1.4 - 2026-09-01

Opened Slice03, `slice03-skill-topology-classification`, for skill kind and
atomic/composite topology classification using verified Slice01, verified
Slice02, live source-surface evidence, and external ontology rubric input.

### v1.5 - 2026-09-01

Recorded Slice03 as verified-closed. No slice-breakdown or sequencing change
was required before Slice04; Slice03 produced the expected skill-kind/topology
decision instrument, classification matrix, and public-language inputs.

### v1.6 - 2026-09-01

Opened Slice04, `slice04-arc01-synthesis`, to synthesize verified Slice01,
Slice02, and Slice03 evidence into an Arc02 readiness packet, directory-contract
requirements list, and Arc01 synthesis decision register.
