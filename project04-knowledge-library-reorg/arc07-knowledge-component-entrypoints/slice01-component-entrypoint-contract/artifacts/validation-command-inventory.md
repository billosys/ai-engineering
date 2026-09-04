# Validation Command Inventory

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice01-component-entrypoint-contract
status: proposed-done
source_edits: none
```

## Purpose

This validation command inventory records source/package/link/install checks
for later Arc07 implementation slices and explicitly dispositions CCDP
validation.

## Read-Only Slice01 Checks

Slice01 required checks:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short --untracked-files=all
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg diff --check
```

Expected Slice01 source disposition: source status clean before and after
work, with no source edits and no generated packages.

## Later Source-Edit Slice Checks

Every source-edit slice should run:

```sh
git status --short --untracked-files=all
git diff --check
```

For README/docs/SKILL local-link validation, reuse the existing Arc06 Python
checker pattern over:

- `README.md`;
- source collaboration-framework entrypoint;
- relevant `docs/*.md`;
- affected component `SKILL.md`;
- affected component `guides/*.md`;
- affected component `templates/*.md`.

The checker must verify local Markdown links after source moves.

## Package and Install Checks

Later implementation slices should run these gates as appropriate:

```sh
make check-skills
make collab-framework
make all
make check-package-paths
```

Package inspection should confirm:

- generated package root remains `collaboration-framework/`;
- generated package entrypoint remains `collaboration-framework/SKILL.md`;
- moved component material appears under the expected package-local paths;
- component-root `SKILL.md` wayfinders are included or excluded according to
  the accepted Makefile `CF_FILES` contract;
- no generated zip or `build/` output is committed.

Isolated install smoke should use a temporary install directory:

```sh
tmp=$(mktemp -d /private/tmp/ai-engineering-arc07-install.XXXXXX)
make install INSTALL_DIR="$tmp"
find "$tmp" -maxdepth 2 -name 'SKILL*.md' | sort
```

Expected install disposition:

- all installable skill package entrypoints are present;
- `collaboration-framework/SKILL.md` is present in the install tree;
- component-root `SKILL.md` files are available only as bundled dependency
  files under the collaboration-framework package unless a later accepted plan
  changes package topology;
- no `ccdp` install root appears.

## CCDP Disposition

CCDP validation is not required for the source-move slices unless the
implementation touches `protocols/ccdp`, CCDP docs, or package/release
surfaces that mention CCDP.

Arc07 should still run final CCDP validation in Slice04 reconciliation:

```sh
make ccdp-package
make check-ccdp-package
```

Expected CCDP disposition:

- CCDP remains a protocol package, not an installable skill.
- Arc07 must not repackage CCDP as a component or skill.
- If no CCDP-facing source changed, failures should be handled as
  release-readiness re-entry evidence, not as justification for broad Arc07
  component cleanup.

## Commit and Cleanliness Checks

Before each later source commit:

```sh
git diff --name-only
git diff --check
git status --short --untracked-files=all
```

Before each later planning commit:

```sh
git diff --check
git status --short --untracked-files=all
```

Generated artifact handling:

```sh
git status --short --ignored --untracked-files=all -- 'target/skills' build
git ls-files 'target/skills/*.zip' build
```

Expected disposition: generated zips under `target/skills` and `build/` are
ignored/untracked unless a separate release process explicitly authorizes a
tracked artifact.

