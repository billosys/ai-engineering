# CC Prompt: Arc07 Slice04 Reconciliation, Package Validation, and Release Notes

You are CC working in Expedited Mode for Project04 Arc07 Slice04.

Read first:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/arc-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/ledger.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/slice-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/ledger.md`
- Slice02 and Slice03 CDC verifications.
- Slice03 artifacts, especially:
  - `slice03-component-guide-layout/artifacts/reference-and-package-repair-report.md`
  - `slice03-component-guide-layout/artifacts/validation-report.md`

## Assignment

Perform final Arc07 reconciliation after the entrypoint and guide-layout source
moves:

1. Validate README/docs/AGENTS/SKILL/component links.
2. Run final package/build checks.
3. Inspect generated package layout and run an isolated install smoke.
4. Validate or explicitly disposition CCDP package behavior.
5. Reconcile release-note/operator-facing wording in
   `workbench/release-notes/RELEASE-0.5.0.md`.
6. Record whether `workbench/RELEASE-0.5.0.md` is absent in the current source
   checkout; do not recreate that top-level path.
7. Make only narrow source repairs required by evidence.
8. Write the four expected artifacts, update the ledger, and write
   `closing-report.md`.

## Authorized Source Files

Source edits are optional. If validation finds no required repair, create no
source commit and record that explicitly.

If source edits are required, edit only:

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

Do not recreate `workbench/RELEASE-0.5.0.md`. Do not commit generated zips,
`build/`, or `target/skills`. Do not touch CCDP source unless a validation
failure proves it is required; if that happens, stop and bubble up instead of
editing it in this slice.

## Required Validation

Run, at minimum:

- source status before edits;
- source diff check;
- local README/docs/AGENTS/SKILL/component-guide Markdown link validation;
- `make check-skills`;
- `make collab-framework`;
- `make all`;
- `make check-package-paths`;
- generated `collaboration-framework.zip` inspection confirming:
  - `collaboration-framework/SKILL.md`;
  - component-root `SKILL.md` files;
  - moved long material under `guides/`;
  - preserved templates under `templates/`;
  - no legacy `knowledge/<component>/docs/` or `docs/pm` package entries;
- generated installable skill zip inspection for expected package roots and
  `SKILL*.md` entrypoints;
- isolated install smoke with an override install directory, confirming
  installable skill entrypoints and no `ccdp` install root;
- `make ccdp-package`;
- `make check-ccdp-package`;
- final source status.

## Release-Note Reconciliation

Inspect `workbench/release-notes/RELEASE-0.5.0.md`. Update it if its 0.5.0
notes still describe Arc07 component packaging/layout as future work or point
at old `docs/`/root-entrypoint paths.

If you edit it, stage it explicitly with:

```bash
git add -f -- workbench/release-notes/RELEASE-0.5.0.md
```

Also record that `workbench/RELEASE-0.5.0.md` is absent and was not recreated.

## Commit Instructions

If source repairs are needed, commit them before planning closure. Stage only
authorized source paths, with explicit pathspecs. Include
`git add -f -- workbench/release-notes/RELEASE-0.5.0.md` only if that ignored
release-note file changed.

Use a source commit message like:

```text
Reconcile Arc07 release readiness

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then update and commit exactly the Slice04 planning packet:

- `arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/artifacts/final-validation-report.md`
- `arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/artifacts/package-and-install-inspection-report.md`
- `arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/artifacts/release-note-reconciliation-report.md`
- `arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/artifacts/arc07-readiness-report.md`
- `arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/ledger.md`
- `arc07-knowledge-component-entrypoints/slice04-reconciliation-package-validation/closing-report.md`

Use a planning commit message like:

```text
Complete Project04 Arc07 Slice04

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Closure Output

Report:

- source commit hash, or no source commit if no source repair was needed;
- planning commit hash;
- validation commands and outcomes;
- release-note disposition;
- package and install inspection summary;
- CCDP validation disposition;
- whether Arc07 is ready for CDC Slice04 verification and formal arc close;
- any bubble-up to Arc07 or Project04.
