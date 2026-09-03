# Slice 03: Public Wording Implementation

```yaml
project: project04-knowledge-library-reorg
arc: arc05-skill-vocabulary
slice: slice03-public-wording-implementation
status: open
opened-by: CDC
opened-on: 2026-09-03
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: true
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Apply the accepted Arc05 public vocabulary to the authorized public source
surfaces without changing package behavior, source layout, or deferred skill
availability.

## Scope

In scope:

- Edit `README.md` where accepted vocabulary improves first-pass orientation.
- Edit focused docs only where accepted vocabulary, examples, or avoid-list
  caveats need to be reflected:
  - `docs/repository-overview.md`
  - `docs/skill-library.md`
  - `docs/collaboration-framework.md`
  - `docs/knowledge-library-anatomy.md`
  - `docs/protocols.md`
  - `docs/contributing.md`
  - `docs/building-and-installing.md`
- Edit top-level `SKILL.md` only for accepted public wording and route
  clarity.
- Preserve docs/ versus knowledge/ routing: docs explain repository materials;
  knowledge stores the source and derived substrate.
- Use `concept-card-method` only as a planned method skill until source and
  package support exist.
- Record any deferred package-facing, metadata, Makefile, package-root, or
  generated-zip wording need rather than editing those surfaces.

Out of scope:

- Editing `Makefile`.
- Editing `package-path-exceptions.tsv`.
- Editing generated `*.zip` files.
- Editing `knowledge/*/SKILL*.md` frontmatter names, descriptions, or
  categories.
- Editing `protocols/ccdp/**`.
- Editing `templates/GUIDE.md`.
- Moving or renaming source files.
- Changing package roots, package lists, package target names, `INSTALL_ZIPS`,
  `ALL_SKILL_FILES`, or `CF_FILES`.
- Implementing `concept-card-method`.
- Repackaging CCDP as an installable skill.

## Expected Artifacts

- `artifacts/public-wording-implementation-map.md`
- `artifacts/vocabulary-scan-evidence.md`
- `artifacts/source-change-and-validation-evidence.md`
- `artifacts/deferred-reentry-notes.md`

## Verification Approach

CC will commit source edits first, then commit the planning close packet. The
source commit must explicitly list every edited source file. Generated zips
must not be committed.

Required validation includes:

- source `git status --short --untracked-files=all` before edits;
- source `git diff --check`;
- accepted/avoided vocabulary scans over `README.md`, `docs/`, and top-level
  `SKILL.md`;
- README/docs route scans for `docs/`, `knowledge/`, `protocols/`,
  `templates/`, `Makefile`, and package links;
- local Markdown link validation if any links change;
- `make check-skills`;
- `make check-package-paths` if top-level `SKILL.md` changes;
- `make all` if top-level `SKILL.md` changes;
- `make ccdp-package` and `make check-ccdp-package` if `docs/protocols.md`
  changes CCDP route or package wording;
- planning `git diff --check`;
- all seven Slice03 ledger verifier commands;
- final source and planning `git status --short --untracked-files=all`.

## Exit Criteria

- Accepted public vocabulary is reflected in authorized README/docs/SKILL
  wording.
- Public examples and edge cases are consistent with Slice02 decisions:
  Rust as the atomic domain/tooling example, `collaboration-framework` as the
  composite framework/operational example, CCDP as protocol distribution /
  protocol package, Biome as a multi-entrypoint knowledge root, and
  `concept-card-method` as planned method skill.
- Avoided claims are absent or appear only as quoted/caveated "not this"
  language.
- Unauthorized package, source-layout, generated-zip, protocol-source,
  template, and knowledge-entrypoint surfaces remain unchanged.
- Any discovered need outside authorization is recorded as a deferral or
  re-entry note.
- Source and planning commits use explicit file lists and required trailers.
- Source and planning worktrees finish clean.
- `closing-report.md` walks all seven ledger rows and bubbles findings up to
  Arc05.
