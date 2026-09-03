# Slice 04: Vocabulary Reconciliation and Arc Close Readiness

```yaml
project: project04-knowledge-library-reorg
arc: arc05-skill-vocabulary
slice: slice04-vocabulary-reconciliation
status: open
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: optional-narrow-repair
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Reconcile the accepted Arc05 vocabulary after source wording implementation,
verify README/docs/SKILL consistency and package/path gates, disposition the
Slice03 CCDP re-entry item, and prepare Arc05 for formal arc close.

## Scope

In scope:

- Verify public wording consistency across `README.md`, `docs/`, and
  top-level `SKILL.md`.
- Verify the accepted skill-kind/topology vocabulary remains present and the
  prohibited claims remain absent or properly caveated.
- Verify local README/docs links and route references remain coherent.
- Run package/build checks needed for Arc05 vocabulary readiness.
- Disposition the Slice03 CCDP stale assembled-spec re-entry item without
  silently editing `protocols/ccdp/**`.
- Create an Arc05 close-readiness report that states whether Arc05 can close
  after CDC verification of Slice04.
- Make only narrow public wording or link repairs in the authorized
  README/docs/SKILL surfaces if validation exposes a defect.

Out of scope:

- Editing `protocols/ccdp/**` without explicit operator authorization.
- Refreshing the assembled CCDP spec.
- Editing `Makefile`, `package-path-exceptions.tsv`, generated zips, package
  roots, package lists, package target names, `INSTALL_ZIPS`,
  `ALL_SKILL_FILES`, or `CF_FILES`.
- Editing `knowledge/*/SKILL*.md` frontmatter names, descriptions, or
  categories.
- Editing `templates/GUIDE.md`.
- Moving or renaming source files.
- Implementing `concept-card-method`.
- Closing Arc05; CDC owns formal arc close after Slice04 is CDC-verified.

## Expected Artifacts

- `artifacts/vocabulary-reconciliation-report.md`
- `artifacts/navigation-and-link-validation-evidence.md`
- `artifacts/package-and-build-validation-evidence.md`
- `artifacts/ccdp-reentry-disposition.md`
- `artifacts/arc05-close-readiness-report.md`

## Verification Approach

CC should start read-only. If validation exposes a narrow README/docs/SKILL
wording or link defect inside the authorized surfaces, make the repair and
commit the source edit first with an explicit file list. If no source repair is
needed, create no source commit and say so explicitly.

Required validation includes:

- source `git status --short --untracked-files=all` before work;
- source `git diff --check`;
- accepted/avoided vocabulary scans over `README.md`, `docs/`, and `SKILL.md`;
- local README/docs/SKILL link validation;
- README/docs route scans for `docs/`, `knowledge/`, `protocols/`,
  `templates/`, `Makefile`, and package links;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- CCDP package check disposition: either reproduced as green if no longer
  stale, or recorded as a deferred/re-entry item if it still requires
  `protocols/ccdp/**` edits outside authorization;
- planning `git diff --check`;
- all seven Slice04 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Exit Criteria

- README/docs/SKILL wording consistently reflects accepted Arc05 vocabulary.
- Prohibited claims remain absent or explicitly caveated.
- README/docs/SKILL local routes and links are valid or any remaining issue is
  explicitly dispositioned.
- Package/path/build validation is green for Arc05-owned surfaces.
- CCDP stale assembled-spec behavior is explicitly resolved or deferred with
  a re-entry condition and no unauthorized protocol edit.
- Arc05 close-readiness evidence states whether formal arc close can proceed.
- Source and planning commits, if any, use explicit file lists and required
  trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all seven ledger rows and bubbles findings up to
  Arc05.
