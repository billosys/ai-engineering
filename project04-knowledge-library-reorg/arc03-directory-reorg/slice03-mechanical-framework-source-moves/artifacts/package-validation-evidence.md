# Package Validation Evidence

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
artifact: package-validation-evidence
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_commit: 99cebae1e98004164e4ea6735c4a68bc60c233da
source-files-edited: true
```

## Package Validation Summary

The collaboration-framework package route validates after moving the payload
under `knowledge/collaboration-framework/`.

source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`.
source commit: `99cebae1e98004164e4ea6735c4a68bc60c233da`.
edited source paths: `SKILL.md`, `Makefile`,
`package-path-exceptions.tsv`, and
`knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md`.
moved source paths: the old `docs/` and `templates/` collaboration-framework
payload paths now under `knowledge/collaboration-framework/`.
clean final source status: `git status --short --untracked-files=all`
returned no output after the source commit and validation.

## Commands

| Command | Result |
|---------|--------|
| `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` before source edits | Returned no output. |
| `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check` | Returned no output. |
| `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --name-status --find-renames` | Recorded route/package edits and payload renames; committed diff records `R100` for pure moves and `R098` for the methodology file. |
| `make check-skills` | Passed with `>> all skill descriptions within limit`. |
| `make collab-framework` | Passed and produced `collaboration-framework.zip`. |
| `./scripts/check-package-paths --exceptions package-path-exceptions.tsv collaboration-framework.zip` | Passed with `hard failures: 0`, `warnings: 64`, and `explicit exceptions: 2`. |
| `make check-package-paths` | Passed after the methodology link repair; it rebuilt all generated zips and exited 0. |

## Makefile CF_FILES

`Makefile` `CF_FILES` now references:

- `SKILL.md`
- `knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md`
- `knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md`
- `knowledge/collaboration-framework/docs/pm/*.md`
- `knowledge/collaboration-framework/docs/CODE-AUDIT.md`
- `knowledge/collaboration-framework/docs/CODE-COVERAGE.md`
- `knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md`
- `knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md`
- `knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md`
- `knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md`

## Generated Package Inspection

Generated package inspection for `collaboration-framework.zip` showed:

- package root: `collaboration-framework/`;
- entrypoint: `collaboration-framework/SKILL.md`;
- entrypoint frontmatter: `name: collaboration-framework`;
- moved source payload packaged under
  `collaboration-framework/knowledge/collaboration-framework/docs/` and
  `collaboration-framework/knowledge/collaboration-framework/templates/`.

Generated zip not committed: `collaboration-framework.zip` and the other
rebuilt zips are ignored release artifacts. `git status --short --untracked-files=all`
returned no output after the source commit and package validation.

## Exception-Path Handling

`package-path-exceptions.tsv` changed only one existing exception path for
`collaboration-framework.zip`:

- old document path: `docs/CODE-AUDIT.md`;
- new document path:
  `knowledge/collaboration-framework/docs/CODE-AUDIT.md`.

This is mechanical maintenance of an existing exception after file movement.
No new exception was added. No broad exception was added. No accepted warning
was added.
