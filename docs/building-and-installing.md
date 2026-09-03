# Building And Installing

The repository uses [`Makefile`](../Makefile) targets for packaging,
validation, installation, and CCDP distribution work. Run commands from the
source checkout root.

Use `make help` for the current target list.

## Skill Package Commands

| Command | Purpose |
|---|---|
| `make all` | Build every installable skill zip, including the collaboration framework. |
| `make skills` | Build the per-domain and tooling skill zips. |
| `make collab-framework` | Build `collaboration-framework.zip`. |
| `make rust`, `make go`, `make cpp`, `make js`, `make erlang` | Build one language skill package. |
| `make cobalt`, `make design`, `make tailwindcss`, `make deno`, `make biome` | Build one tooling or design package target. |
| `make clean` | Remove `build/` and generated zips. |

Generated skill zips are named from the packaged skill entrypoint's
frontmatter and contain a package-local directory root. They are generated
artifacts, not hand-edited source.

## Validation Commands

| Command | Purpose |
|---|---|
| `make check-skills` | Validate packaged skill description lengths. |
| `make check-package-paths` | Build skill zips and validate package-context Markdown paths. |
| `git diff --check` | Check staged or unstaged text changes for whitespace issues. |
| `git status --short --untracked-files=all` | Confirm exactly what changed. |

Package-path validation checks generated skill zips. That is intentional: the
package surface is the installable artifact a loader sees.

## Installing Skills

Use:

```sh
make install
```

By default, this builds all installable skill zips and unpacks them into
`~/.agents/skills`. Override the destination with `INSTALL_DIR=...` when you
need a different loader location.

Use:

```sh
make uninstall
```

to remove installed skill directories from the selected install directory.

## CCDP Commands

CCDP is distributed separately from installable skills.

| Command | Purpose |
|---|---|
| `make ccdp` | Assemble `protocols/ccdp/composite-cognition-dispatch-protocol.md`. |
| `make ccdp-package` | Build `ccdp.zip`. |
| `make check-ccdp-package` | Validate `ccdp.zip`, package-local Markdown paths, and extracted-package rebuild. |

Do not expect `make all`, `make skills`, or `make install` to build or install
`ccdp.zip`. Use the CCDP-specific targets for protocol package work.

## Commit Discipline

When making source changes, stage and commit only the intended source files.
Packaging commands may refresh generated zips during validation; do not commit
those generated artifacts unless a release process explicitly calls for them.
