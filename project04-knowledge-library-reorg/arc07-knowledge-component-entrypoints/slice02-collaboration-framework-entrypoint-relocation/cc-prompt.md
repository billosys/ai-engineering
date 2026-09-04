# CC Prompt: Arc07 Slice02 Collaboration Framework Entrypoint Relocation

You are CC working in Expedited Mode for Project04 Arc07 Slice02.

Read first:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/arc-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/ledger.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/slice-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/ledger.md`
- Slice01 artifacts, especially:
  - `slice01-component-entrypoint-contract/artifacts/component-entrypoint-decision-register.md`
  - `slice01-component-entrypoint-contract/artifacts/source-migration-impact-map.md`
  - `slice01-component-entrypoint-contract/artifacts/implementation-slice-roadmap.md`

## Assignment

Implement only the collaboration-framework entrypoint relocation:

1. Move repository-root `SKILL.md` to
   `knowledge/collaboration-framework/SKILL.md` with an explicit `git mv`.
2. Update Makefile/package behavior so:
   - `ALL_SKILL_FILES` uses the moved source entrypoint;
   - `CF_FILES` and `make collab-framework` use the moved source entrypoint;
   - generated `collaboration-framework.zip` still contains package root
     `collaboration-framework/` and package entrypoint
     `collaboration-framework/SKILL.md`.
3. Repair direct README/docs/source references caused by this move.
4. Repair package-local links or narrow staging behavior before adding or
   widening package-path exceptions.
5. Record the implementation and validation evidence in the four expected
   artifacts, update the ledger, and write `closing-report.md`.

## Authorized Source Files

You may edit only these source files unless a hard blocker requires a
bubble-up:

- `SKILL.md`
- `knowledge/collaboration-framework/SKILL.md`
- `Makefile`
- `scripts/stage-skill-entrypoint`
- `README.md`
- `docs/skill-library.md`
- `docs/knowledge-library-anatomy.md`
- `docs/repository-overview.md`
- `docs/collaboration-framework.md`
- `docs/ORIGINS.md`
- `assets/packaging/path-exceptions.tsv`

Do not move component `docs/` directories in this slice. Do not add
component-root `SKILL.md` files for the other framework components in this
slice. Those are Slice03.

Do not update release notes in this slice. Do not touch CCDP source. Do not
commit generated zips, `build/`, or ignored build outputs.

## Required Mechanics

- Use `git mv SKILL.md knowledge/collaboration-framework/SKILL.md`.
- If any directory cleanup is unexpectedly required, use `rmdir` only for empty
  directories. Do not use `rm -rf`.
- Preserve source prose except for necessary path/routing adjustments.
- If a file outside the authorized source list is required, stop and record the
  needed expansion in the slice evidence instead of silently editing it.

## Source Validation

Run, at minimum:

- source status before edits;
- source diff check;
- local README/docs/SKILL link validation;
- `make check-skills`;
- `make collab-framework`;
- generated `collaboration-framework.zip` inspection confirming package root
  and `collaboration-framework/SKILL.md` entrypoint;
- final source status.

Run `make check-package-paths` if you change package-path exceptions,
package-local links, or staging behavior in a way that can affect package-path
validation.

## Commit Instructions

After source validation passes, commit the source changes before planning
closure. Stage only the authorized source paths with an explicit pathspec:

```bash
git add -A -- SKILL.md knowledge/collaboration-framework/SKILL.md Makefile scripts/stage-skill-entrypoint README.md docs/skill-library.md docs/knowledge-library-anatomy.md docs/repository-overview.md docs/collaboration-framework.md docs/ORIGINS.md assets/packaging/path-exceptions.tsv
```

Use a source commit message like:

```text
Relocate collaboration framework source entrypoint

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then update and commit exactly the Slice02 planning packet:

- `arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/artifacts/entrypoint-relocation-report.md`
- `arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/artifacts/makefile-package-staging-report.md`
- `arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/artifacts/source-reference-repair-report.md`
- `arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/artifacts/validation-report.md`
- `arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/ledger.md`
- `arc07-knowledge-component-entrypoints/slice02-collaboration-framework-entrypoint-relocation/closing-report.md`

Use a planning commit message like:

```text
Complete Project04 Arc07 Slice02

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Closure Output

Report:

- source commit hash, or no source commit if no source edit was required;
- planning commit hash;
- files changed;
- validation commands and outcomes;
- whether root `SKILL.md` is absent and
  `knowledge/collaboration-framework/SKILL.md` is present;
- whether `collaboration-framework.zip` still exposes
  `collaboration-framework/SKILL.md`;
- any bubble-up to Slice03 or Arc07.
