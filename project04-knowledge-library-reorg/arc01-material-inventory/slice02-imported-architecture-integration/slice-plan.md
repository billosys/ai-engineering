# Slice 02: Imported Architecture and Prior Proposal Integration

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice02-imported-architecture-integration
status: open
opened-on: 2026-09-01
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: false
```

## Goal

Integrate Project04's project-level imported materials into Arc01's evidence
base. This slice answers: what prior Project02 and Project03 facts should
Project04 preserve, which imported proposals are merely hypotheses or
implementation plans, and what conflicts or open questions do they create for
Arc02's target directory contract?

This slice is an assessment and synthesis pass. It does not decide the final
directory contract, classify every skill topology, or authorize source edits.

## Scope

In scope:

- Read Project04 `project-plan.md`, project `ledger.md`, Arc01 `arc-plan.md`,
  Arc01 `ledger.md`, and the verified Slice01 artifacts.
- Read the Project04 project-level imported artifacts under `artifacts/`:
  `operator-accepted-architecture.md`, component layout, package target,
  skill-entrypoint validation, README wayfinding, migration compatibility,
  package-path/link exception, implementation sequence, and external ontology
  rubric research.
- Inspect Project03 planning artifacts only as needed to recover the accepted
  concept-card-method and method-skill boundary relevant to Project04.
- Distinguish accepted facts, working hypotheses, source/package constraints,
  implementation-sequence assumptions, compatibility obligations, conflicts,
  superseded statements, and Arc02 questions.
- Produce durable artifacts under this slice's `artifacts/` directory.
- Keep Slice03 ownership intact: classify topology edge cases only enough to
  identify inputs and questions for the later skill-kind/topology slice.

Out of scope:

- Moving, deleting, renaming, or editing source checkout files.
- Editing source `README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`,
  `protocols/`, `Makefile`, package-path exceptions, or generated zips.
- Treating Project02 implementation plans as source-edit authorization.
- Re-opening Project02 accepted architecture except to record Project04
  integration conflicts or re-entry conditions already named by Project02.
- Finalizing atomic/composite terminology; Slice03 owns the classification
  instrument and matrix.
- Writing Arc02's final target directory contract.

## Artifacts

Expected artifact home: `artifacts/`.

Expected artifacts:

- `artifacts/imported-architecture-evidence-map.md`
- `artifacts/prior-proposal-register.md`
- `artifacts/project04-integration-conflicts-and-questions.md`

## Verification Approach

Use planning-tree inspection and targeted `rg` checks. The artifacts should
cite concrete planning artifact paths and identify which claims are accepted,
which are hypotheses, which are constraints, and which are open questions.
The final close must show that every ledger row was satisfied by evidence in
the artifacts.

## Exit Criteria

- Every Project04 project-level imported artifact is represented in the prior
  proposal register.
- Project02 accepted architecture facts are preserved separately from Project02
  implementation-plan hypotheses.
- Project03 method-skill and concept-card-method inputs are assessed at the
  level needed for Project04, without turning Slice02 into Slice03.
- Conflicts between the Project02 component-root proposal, Project03 method
  skill direction, and Project04's `docs/`/`knowledge/` direction are listed.
- Arc02 receives a concrete set of directory-contract decisions and questions.
- No source checkout files are edited.

## Version History

### v1.0 - 2026-09-01

Opened Slice02 as the imported Project02/Project03 architecture and prior
proposal integration pass for Project04 Arc01.
