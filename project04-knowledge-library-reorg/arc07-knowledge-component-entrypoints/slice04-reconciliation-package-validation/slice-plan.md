# Slice 04: Reconciliation, Package Validation, and Release Notes

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice04-reconciliation-package-validation
status: open
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized-if-needed
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Perform final Arc07 reconciliation after the entrypoint and component guide
layout moves. Validate source links, generated skill packages, install
behavior, CCDP package disposition, and release-note/operator-facing wording.

## Scope

In scope:

- Final README/docs/AGENTS/SKILL/component link validation.
- Final `make check-skills`, `make collab-framework`, `make all`, and
  `make check-package-paths` validation.
- Generated package inspection for `collaboration-framework.zip` and the
  installable skill packages affected by full packaging.
- Isolated install smoke confirming installable skill entrypoints and no CCDP
  install root.
- CCDP validation disposition, including `make ccdp-package` and
  `make check-ccdp-package` unless no longer applicable.
- Release-note reconciliation for
  `workbench/release-notes/RELEASE-0.5.0.md`.
- Explicit disposition that `workbench/RELEASE-0.5.0.md` is absent in the
  current source checkout.
- Narrow source repairs found by the final validation.

Out of scope:

- New component layout moves beyond narrow repairs.
- New installable component packages.
- Concept-card-method implementation.
- Broad README/docs rewrites.
- Repackaging CCDP as an installable skill.
- Committing generated zips, `build/`, or `target/skills`.

## Authorized Source Files

Source edits are optional. If validation finds no required repair, create no
source commit and record that result.

If edits are required, CC may edit only:

- `README.md`
- `AGENTS.md`
- `docs/**`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/*/SKILL.md`
- `knowledge/*/guides/**`
- `knowledge/*/templates/**`
- `Makefile`
- `scripts/stage-skill-entrypoint`
- `assets/packaging/path-exceptions.tsv`
- `workbench/release-notes/RELEASE-0.5.0.md`

If a needed source edit falls outside this list, stop and bubble it up.

## Expected Artifacts

- `artifacts/final-validation-report.md`
- `artifacts/package-and-install-inspection-report.md`
- `artifacts/release-note-reconciliation-report.md`
- `artifacts/arc07-readiness-report.md`

## Verification Approach

CC should begin from clean source and planning checkouts. Run the validation
first; make narrow source repairs only if evidence requires them. If
`workbench/release-notes/RELEASE-0.5.0.md` is updated, stage it explicitly with
`git add -f` because `workbench/` is ignored. Do not recreate
`workbench/RELEASE-0.5.0.md`; record its absence and use the existing
`workbench/release-notes/RELEASE-0.5.0.md` file.

## Exit Criteria

- Final source link validation passes.
- Final package validation passes with hard failures: 0.
- `collaboration-framework.zip` package inspection confirms the accepted
  Arc07 layout.
- Isolated install smoke passes and confirms no CCDP install root.
- CCDP package validation passes or is explicitly dispositioned with evidence.
- Release-note reconciliation is complete for
  `workbench/release-notes/RELEASE-0.5.0.md`.
- Source commit is created only if source repairs are needed, with explicit
  path staging and both required co-author trailers.
- Planning artifacts, ledger, and `closing-report.md` are committed in a
  separate planning commit with both required co-author trailers.
