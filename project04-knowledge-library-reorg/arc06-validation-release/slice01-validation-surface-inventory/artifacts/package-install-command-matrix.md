# package/install command matrix

## Current Disposition

| Command | Expected output | Current disposition | Follow-up |
| --- | --- | --- | --- |
| `git status --short --untracked-files=all` | clean source status | pass | rerun in Slice02 before edits |
| `git diff --check` | no whitespace errors | pass | rerun after any later source edits |
| local README/docs/SKILL link checker | `missing: 0` | pass; 104 local links checked | rerun if docs/SKILL links change |
| route scan with `rg` | expected docs/knowledge/protocol/package routes | pass | rerun if README/docs/SKILL wording changes |
| `make check-skills` | `>> all skill descriptions within limit` | pass | rerun after any skill entrypoint change |
| `make check-package-paths` | all packages build; hard failures: 0 | pass with warning-only output | Slice02 should decide whether warnings remain acceptable or should be narrowed |
| `make all` | all installable skill package zips generated | pass | rerun before package inspection and install smoke |
| generated package inspection | zip root and `SKILL*.md` entrypoint present per package | pass for 12 installable skill packages | Slice02 should preserve this as final evidence |
| `make install INSTALL_DIR="$tmp"` | installable skills unpack into isolated directory | planned, not run in Slice01 | run in Slice02 |
| `make ccdp-package` | fresh `ccdp.zip` protocol package | fail; stale assembled spec | repair or disposition in Slice03 |
| `make check-ccdp-package` | validate `ccdp.zip` zipped and unzipped | fail at `ccdp-package` prerequisite | repair or disposition in Slice03 |

## Generated Package Inspection Commands

Package inspection command:

```sh
for z in *.zip; do
  printf '%s\t' "$z"
  unzip -Z1 "$z" | awk -F/ 'NR==1 {root=$1} END {print root, NR " entries"}'
done
```

Entrypoint inspection command:

```sh
for z in *.zip; do
  printf '== %s ==\n' "$z"
  unzip -Z1 "$z" | rg '(^[^/]+/SKILL[^/]*\.md$|^collaboration-framework/SKILL.md$)' || true
done
```

Observed installable skill package outputs:

| generated package | expected output | disposition |
| --- | --- | --- |
| `rust-guidelines.zip` | root `rust-guidelines`, 41 entries, `rust-guidelines/SKILL.md` | pass |
| `go-guidelines.zip` | root `go-guidelines`, 15 entries, `go-guidelines/SKILL.md` | pass |
| `cpp-guidelines.zip` | root `cpp-guidelines`, 18 entries, `cpp-guidelines/SKILL.md` | pass |
| `javascript-deno-guidelines.zip` | root `javascript-deno-guidelines`, 24 entries, `javascript-deno-guidelines/SKILL.md` | pass |
| `erlang-guidelines.zip` | root `erlang-guidelines`, 20 entries, `erlang-guidelines/SKILL.md` | pass |
| `cobalt-guidelines.zip` | root `cobalt-guidelines`, 4 entries, `cobalt-guidelines/SKILL.md` | pass |
| `visual-design-system.zip` | root `visual-design-system`, 9 entries, `visual-design-system/SKILL.md` | pass |
| `tailwindcss.zip` | root `tailwindcss`, 4 entries, `tailwindcss/SKILL.md` | pass |
| `deno-js-linter.zip` | root `deno-js-linter`, 6 entries, `deno-js-linter/SKILL-js-linter.md` | pass |
| `biome-js-linter.zip` | root `biome-js-linter`, 20 entries, `biome-js-linter/SKILL-js-linter.md` | pass |
| `biome-linter.zip` | root `biome-linter`, 20 entries, `biome-linter/SKILL-web-linter.md` | pass |
| `collaboration-framework.zip` | root `collaboration-framework`, 40 entries, `collaboration-framework/SKILL.md` | pass |

`ccdp.zip` is intentionally excluded from installable skill package pass/fail.
It is a protocol package output and is handled by the CCDP matrix below.

## Temporary Install Smoke Command Plan

Slice02 package/install validation should run:

```sh
tmp="$(mktemp -d /private/tmp/ai-engineering-install.XXXXXX)"
make install INSTALL_DIR="$tmp"
find "$tmp" -maxdepth 2 -name 'SKILL*.md' -print | sort
test -f "$tmp/collaboration-framework/SKILL.md"
test -f "$tmp/rust-guidelines/SKILL.md"
test -f "$tmp/go-guidelines/SKILL.md"
test -f "$tmp/cpp-guidelines/SKILL.md"
test -f "$tmp/javascript-deno-guidelines/SKILL.md"
test -f "$tmp/erlang-guidelines/SKILL.md"
test -f "$tmp/cobalt-guidelines/SKILL.md"
test -f "$tmp/visual-design-system/SKILL.md"
test -f "$tmp/tailwindcss/SKILL.md"
test -f "$tmp/deno-js-linter/SKILL-js-linter.md"
test -f "$tmp/biome-js-linter/SKILL-js-linter.md"
test -f "$tmp/biome-linter/SKILL-web-linter.md"
test ! -e "$tmp/ccdp"
```

Expected output:

- `make install INSTALL_DIR="$tmp"` exits 0.
- all twelve generated installable skill roots are present.
- each installed root has the expected `SKILL.md` or `SKILL-*.md` entrypoint.
- no `ccdp/` root is installed because CCDP is not an installable skill.

## Warning Disposition

`make check-package-paths` passes with hard failures: 0, but warning-only
package-path findings remain visible. Current warning classes include:

- JavaScript/Deno guide-internal shorthand.
- repo-only/provenance references.
- source-clone references.
- example-project paths.
- parser false positives.

These warnings are release-readiness review items, not current hard package
failures.
