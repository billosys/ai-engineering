# Arc 04: README Decomposition and End-User Documentation

```yaml
project: project04-knowledge-library-reorg
arc: arc04-user-docs
status: active
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: per-slice
operating-mode: expedited
```

## Capability

Arc04 splits the current top-level README into a concise repository
orientation plus focused end-user documentation under `docs/`. The resulting
`docs/` tree explains the repository's materials, packages, methods, protocols,
knowledge library, build/install workflow, and contribution paths without
becoming the material substrate itself.

Arc04 consumes Arc03's final layout. It must document what exists after the
directory reorganization, not reopen the source layout contract or perform
public skill vocabulary finalization reserved for Arc05.

## Inputs

- Project04 `project-plan.md` and project `ledger.md`.
- Arc03 close:
  - `../arc03-directory-reorg/closing-report.md`
  - `../arc03-directory-reorg/slice06-implementation-reconciliation/cdc-verification.md`
  - `../arc03-directory-reorg/slice06-implementation-reconciliation/artifacts/arc03-close-readiness-report.md`
- Arc01 skill topology and public language implications artifacts.
- Arc02 accepted directory contract and migration/validation artifacts.
- Source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`.

## Boundaries

In scope:

- README decomposition into a short, stable orientation document.
- Focused user-facing docs under `docs/` for repository overview, skill
  library, collaboration framework, knowledge-library anatomy, build/install
  workflow, CCDP/protocol distribution, and contribution paths.
- Navigation and link updates needed for README/docs coherence.
- Clear distinction between `docs/` as explanatory documentation and
  `knowledge/` as source/derived knowledge substrate.
- Validation of README/docs links and package-facing references touched by
  documentation edits.

Out of scope:

- Moving more material between `docs/`, `knowledge/`, `templates/`, or
  `protocols/` unless a documentation link defect requires a narrow route fix.
- Rewriting final public skill-kind or atomic/composite vocabulary; Arc05 owns
  that work.
- Changing package roots, Makefile package lists, package-path exceptions, or
  generated zips except for a narrow documentation-link repair required by an
  opened slice.
- Folding CCDP into installable skill packages.
- Reopening Arc02 or Arc03 layout decisions.

## Expedited Mode

Project04 remains in Expedited Mode.

- CC commits after changes, before CDC review, using explicit file lists.
- CDC commits CDC verification and planning updates after review.
- Closed slices automatically advance to the next slice.
- After the last Arc04 slice closes, CDC closes Arc04 and opens Arc05 with its
  first slice.

## Slice Breakdown

### Slice 01: README and Docs Decomposition Map

Status: verified-closed.

Scope: produce a read-only map of current README content, existing `docs/`
surfaces, target user-doc topics, source-edit sequence, validation commands,
and Arc05 vocabulary boundaries before README/docs source edits begin.

Expected artifacts:

- `slice01-readme-docs-decomposition-map/artifacts/readme-source-surface-map.md`
- `slice01-readme-docs-decomposition-map/artifacts/end-user-docs-decomposition-plan.md`
- `slice01-readme-docs-decomposition-map/artifacts/arc04-doc-edit-sequence.md`
- `slice01-readme-docs-decomposition-map/artifacts/public-language-boundary-register.md`
- `slice01-readme-docs-decomposition-map/artifacts/docs-validation-command-inventory.md`

### Slice 02: README Orientation Rewrite

Status: verified-closed.

Scope: rewrite `README.md` into a concise top-level orientation that points to
focused docs and preserves build/install/package entrypoints.

### Slice 03: Focused End-User Guide Set

Status: verified-closed.

Scope: create or update focused `docs/*.md` guides that explain the repository,
skill library, collaboration framework, knowledge library, build/install
workflow, protocol distribution, and contribution paths.

### Slice 04: Documentation Link and Navigation Reconciliation

Status: open.

Scope: reconcile README/docs navigation, path references, package-path checks,
and source checkout status after Arc04 documentation edits.

## Dependencies

- Slice01 must close before README/docs source edits because it establishes the
  decomposition plan and vocabulary boundaries.
- Slice02 must keep README concise and avoid moving final skill taxonomy work
  forward from Arc05.
- Slice03 depends on the Slice01 target guide map and Slice02 README
  wayfinding.
- Slice04 closes the arc by validating links, navigation, and source/package
  behavior after documentation edits.

## Version History

### v1.3 - 2026-09-02

Recorded Slice03 as verified-closed after CDC reproduced all six ledger rows,
checked the source and planning commits, reran the README/docs and package
validation gates, and confirmed the seven focused guide files were expanded
without moving knowledge substrate back into `docs/`. Opened Slice04,
`slice04-doc-link-navigation-reconciliation`, as the final Arc04 slice for
documentation link/navigation reconciliation and Arc04 close readiness.

### v1.2 - 2026-09-02

Recorded Slice02 as verified-closed after CDC reproduced all six ledger rows,
checked the source and planning commits, reran the README/docs and package
validation gates, and confirmed the concise README orientation with focused
doc stubs. Opened Slice03, `slice03-focused-end-user-guide-set`, to expand the
seven focused `docs/*.md` guide stubs into usable end-user documentation while
preserving the Arc05 vocabulary boundary.

### v1.1 - 2026-09-02

Recorded Slice01 as verified-closed after CDC reproduced all six ledger rows
and confirmed the slice was planning-only. Opened Slice02,
`slice02-readme-orientation-rewrite`, as the first README/docs source-edit
slice, with route repair for stale `docs/dev`, former framework-doc, and moved
template references discovered by Slice01.

### v1.0 - 2026-09-02

Opened Arc04 after Arc03 closed. Planned four documentation-sized slices and
opened Slice01, `slice01-readme-docs-decomposition-map`, as a read-only
decomposition and validation map before README/docs source edits.
