# Slice 04: Documentation Link and Navigation Reconciliation

```yaml
project: project04-knowledge-library-reorg
arc: arc04-user-docs
slice: slice04-doc-link-navigation-reconciliation
status: open
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: conditional
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Reconcile README/docs navigation, documentation links, package-path behavior,
and Arc04 close readiness after the focused end-user guide set has landed.

## Scope

In scope:

- Validate all README/docs navigation routes introduced or preserved by
  Slice02 and Slice03.
- Identify and repair narrow README/docs link defects if any are found.
- Confirm generated skill packages and CCDP package validation remain green
  after the expanded docs guide set.
- Confirm the `docs/` versus `knowledge/` boundary remains visible and
  intact.
- Confirm Arc05 remains the owner of final public skill-kind and
  atomic/composite vocabulary.
- Produce Arc04 close-readiness evidence for CDC's formal arc close.

Out of scope:

- Rewriting the focused guide content except for narrow link, navigation,
  wording, or consistency repairs found during reconciliation.
- Finalizing public skill taxonomy or atomic/composite positioning; Arc05 owns
  that work.
- Moving source material between `docs/`, `knowledge/`, `templates/`, or
  `protocols/`.
- Changing `Makefile`, package roots, package-path exceptions, `SKILL.md`, or
  generated zips unless an explicit operator gate is recorded.
- Closing Arc04; CDC owns formal arc close after Slice04 is verified.

## Expected Artifacts

- `artifacts/documentation-link-reconciliation-report.md`
- `artifacts/navigation-route-validation-evidence.md`
- `artifacts/package-and-build-validation-evidence.md`
- `artifacts/arc04-close-readiness-report.md`

## Verification Approach

If source edits are required, CC will commit them first, then commit the
planning close packet. Source commits must explicitly list every edited source
file. If no source edits are required, record `source commit: none` and explain
why.

Required validation includes:

- source `git status --short --untracked-files=all`;
- source `git diff --check`;
- README/docs link and stale-route scans from Slice02 and Slice03;
- `find docs -maxdepth 2 -type f | sort`;
- README/docs heading scan;
- a file-existence check for every local Markdown link in README/docs, or a
  documented equivalent link validation pass;
- `make check-skills`;
- `make check-package-paths`;
- `make all`;
- `make ccdp-package`;
- `make check-ccdp-package`;
- planning `git diff --check`;
- all six Slice04 ledger verifier commands;
- final source and planning `git status --short`.

## Exit Criteria

- README/docs navigation routes resolve or are explicitly dispositioned.
- No unrepaired stale post-Arc03 docs route remains.
- Source/package validation is green with hard package-path failures at zero.
- Any remaining package-path warnings are classified as pre-existing,
  explicit, or outside Arc04 source scope.
- Arc04 close readiness is recorded with all four child slices accounted for.
- Source and planning commits use explicit file lists and required trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all six ledger rows and bubbles findings up to
  Arc04.
