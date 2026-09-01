# CC Prompt: Slice 02 Imported Architecture and Prior Proposal Integration

You are working in the planning worktree for:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg`

Open and complete:

`arc01-material-inventory/slice02-imported-architecture-integration/`

## Required Reading

Before writing artifacts, read:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/01-scales-of-work.md`
4. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/02-canonical-planning-worktree.md`
5. `/Users/oubiwann/.codex/skills/collaboration-framework/docs/pm/03-planning-top-down.md`
6. `/Users/oubiwann/.codex/skills/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
7. `project-plan.md`
8. `ledger.md`
9. `arc01-material-inventory/arc-plan.md`
10. `arc01-material-inventory/ledger.md`
11. `arc01-material-inventory/slice02-imported-architecture-integration/slice-plan.md`
12. `arc01-material-inventory/slice02-imported-architecture-integration/ledger.md`
13. `arc01-material-inventory/slice01-source-surface-inventory/cdc-verification.md`
14. The three Slice01 artifacts under `arc01-material-inventory/slice01-source-surface-inventory/artifacts/`
15. All Project04 project-level artifacts under `artifacts/`

Inspect Project03 planning artifacts only as needed to recover accepted
concept-card-method and method-skill facts relevant to Project04. Do not
perform a broad Project03 audit.

## Mission

Produce the imported-architecture and prior-proposal integration evidence for
Project04 Arc01. Your job is to distinguish what Project04 must preserve from
what Project04 merely inherits as a hypothesis, sequencing idea, compatibility
risk, or open question.

This is not a source-edit slice. Do not edit the implementation checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`.

## Produce

Create the slice artifact home if needed:

`arc01-material-inventory/slice02-imported-architecture-integration/artifacts/`

Then create:

- `artifacts/imported-architecture-evidence-map.md`
- `artifacts/prior-proposal-register.md`
- `artifacts/project04-integration-conflicts-and-questions.md`

### `imported-architecture-evidence-map.md`

Include:

- The verified Slice01 inventory artifacts consumed as source-surface context.
- The external ontology rubric as input, not accepted taxonomy.
- Accepted Project02 facts Project04 must preserve, especially:
  `collaboration-framework` as daily-driver composer, the seven specialist
  components, `engineering-methods` ownership of source/package/release gates,
  ontology critique placement, component version-history policy, and CCDP as a
  separate protocol distribution.
- Project03 method-skill facts relevant to `concept-card-method`, including
  thin `SKILL.md` plus guides, validation surfaces, and CCDP/memory-admission
  boundaries where visible from accepted Project03 artifacts.
- A clear distinction between accepted facts, implementation-plan hypotheses,
  compatibility obligations, and Slice03 topology inputs.

### `prior-proposal-register.md`

Include one row per Project04 project-level artifact:

- `operator-accepted-architecture.md`
- `component-file-layout-plan.md`
- `package-target-plan.md`
- `skill-entrypoint-validation-plan.md`
- `readme-wayfinding-plan.md`
- `migration-compatibility-plan.md`
- `package-path-link-exception-plan.md`
- `implementation-sequence-roadmap.md`
- `external-ontology-rubric-research.md`

For each row, record:

- artifact path
- source project or origin
- status for Project04 (`accepted fact`, `working hypothesis`,
  `constraint`, `conflict`, `open question`, or similar)
- concrete Project04 relevance
- what Arc02 must decide or preserve

### `project04-integration-conflicts-and-questions.md`

Include:

- Conflicts or tensions between Project02 component-root plans and Project04's
  current `docs/` as user-docs / `knowledge/` as substrate direction.
- Conflicts or tensions between Project03 method-skill plans and Project04's
  skill kind/topology model.
- Compatibility obligations for README, `SKILL.md`, package roots,
  package-local links, package-path exceptions, `AGENTS.md`/`CLAUDE.md`, and
  CCDP separation.
- A concrete Arc02 decision list: move/remain/wrapper-doc questions, package
  root questions, source root questions for atomic and composite skills,
  exception policy questions, and re-entry conditions for reopened decisions.

## Ledger Work

Update `ledger.md` as you work. For each row you complete, set `Status` to
`done` and fill `Evidence` with `attested:` evidence pointing to the artifact
and command result. Leave no open rows when you hand back.

Run every ledger Verify command from:

`arc01-material-inventory/slice02-imported-architecture-integration/`

Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

## Closing Report

Create `closing-report.md` only after all ledger rows are final. The closing
report must include:

- Summary.
- Ledger Walk with all 7 rows.
- Artifact Inventory.
- Verification Run.
- Bubble-up to the Arc:
  - whether Slice02 delivered its assigned Arc01 piece;
  - findings for Arc01 and whether they require an `arc-plan.md` update before
    Slice03;
  - silent-drop diff comparing scope as specified to scope as delivered.
- What Worked.
- Closure statement with row counts.

Expected final status is `proposed-done`; CDC will verify independently.

## Constraints

- Do not edit source checkout files.
- Do not create final public docs.
- Do not decide final skill topology; route edge cases and needed evidence to
  Slice03.
- Do not decide the final directory contract; produce the Arc02 inputs that
  make that decision possible.
