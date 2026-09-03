# Slice 02: Top-Level Compatibility Decision

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice02-top-level-compatibility-decision
status: open
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: permitted-if-required-by-this-slice
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Select and validate the compatibility path for the top-level `SKILL.md`
entrypoint before any collaboration-framework composer source material moves.
The slice must choose one of three outcomes: validated shim, replacement route,
or explicit no-shim path.

## Scope

In scope:

- Inspect the current top-level `SKILL.md`, `Makefile` collaboration-framework
  packaging route, `AGENTS.md`/`CLAUDE.md` compatibility behavior, and README
  route implications needed for this decision.
- Select one compatibility path and record the rationale, implementation
  status, and re-entry conditions.
- Implement only the minimal source change required by the selected path, if a
  source change is required in this slice.
- Validate `make check-skills`, `make collab-framework`, source status/diff
  hygiene, and package-entrypoint behavior for the selected path.
- Record exact source files touched, or record that no source files were
  edited.

Out of scope:

- Moving collaboration-framework composer source material into
  `knowledge/collaboration-framework/`.
- Moving `docs/`, `templates/`, `knowledge/`, `protocols/ccdp`, or package
  exception files.
- Deep README rewrite, end-user docs prose, public skill taxonomy language, or
  Arc04/Arc05 vocabulary work.
- Adding persistent package-path exceptions or accepted warnings.
- Committing generated zips unless the slice explicitly proves they are source
  artifacts that must be versioned.

## Allowed Source Scope

This slice may edit source files only when the selected compatibility path
requires it. Allowed source surfaces are limited to:

- `SKILL.md`
- `Makefile`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md` symlink behavior or compatibility references

Any broader source edit requires operator approval before implementation.

## Expected Artifacts

- `artifacts/top-level-skill-compatibility-decision.md`
- `artifacts/compatibility-implementation-record.md`
- `artifacts/validation-evidence-map.md`

## Verification Approach

CC will close the slice by updating the slice ledger to attested evidence,
creating the three expected artifacts, writing `closing-report.md`, and
committing with explicit file lists. CDC will independently reproduce the
ledger rows before closing the slice.

Required validation includes source checkout `status --short`, source
`diff --check` when source edits exist, `make check-skills`,
`make collab-framework`, route/package behavior review for
`collaboration-framework.zip`, and planning checkout `diff --check`.

## Exit Criteria

- One compatibility path is selected and documented: validated shim,
  replacement route, or explicit no-shim.
- Source edits are either absent or limited to the allowed source scope.
- Required validation evidence is recorded with command outcomes.
- Arc02/Arc03 ordering is preserved: compatibility before composer moves,
  mechanical moves before prose rewrites, and package-local repair before
  exceptions.
- CC commits source edits separately if source files changed, then commits the
  exact planning close packet.
- `closing-report.md` walks all six rows, records source/planning checkout
  status, and bubbles findings up to Arc03.
