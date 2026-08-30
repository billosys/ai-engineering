# Warning Release Disposition

Audit date: 2026-08-29

Primary evidence:

- `artifacts/make-check-package-paths.txt`
- `artifacts/check-package-paths-exceptions-only.txt`
- `package-path-exceptions.tsv`

## Gate Summary

`make check-package-paths` exits 0.

Observed result:

- zips scanned: 12
- Markdown files scanned: 171
- hard failures: 0
- warnings: 295
- explicit exceptions: 3
- skipped external URLs: 656

`scripts/check-package-paths --check-exceptions-only` exits 0 and reports:

```text
exception schema ok: package-path-exceptions.tsv
```

## Warning Classes

The current warning classes are:

- `bundled-reference`: visible backlog, not release-blocking under the Arc 02
  accepted policy.
- `repo-only/provenance`: non-blocking when visibly classified or explicitly
  excepted.
- `source-clone-reference`: non-blocking source-context references, visible
  for later maintenance where needed.
- `example-project path`: non-blocking example paths.
- `parser false positive`: non-blocking scanner false positives.

## Explicit Exceptions

The three explicit exceptions are narrow and non-blocking:

- `collaboration-framework.zip` `docs/CODE-AUDIT.md`
  `knowledge/<slug>/SKILL*.md`: placeholder for source-clone skill discovery,
  not a literal bundled package path.
- `collaboration-framework.zip` `SKILL.md`
  `knowledge/<domain>/SKILL.md`: placeholder for source-clone domain skill
  layout, not a literal bundled package path.
- `go-guidelines.zip` `SKILL.md`
  `knowledge/go/workbench/skills-accepted.md`: workbench provenance file is
  source-clone material and intentionally not bundled.

## Visible Warning Rows

The five warning-policy rows are visible backlog, not release-blocking:

- Rust missing `09-common-pitfalls.md` references: later Rust guide
  maintenance.
- C++ missing `param-passing-*.png` assets: later C++ asset/package-layout
  maintenance.
- JavaScript/Deno `12-deno/*.md` shorthand: later JS guide harmonisation.
- JavaScript/Deno `13-biome/*.md` shorthand: later JS guide harmonisation.

The gate keeps these warnings visible in release checks. They are not hidden by
broad suppression and they do not become hard failures under the current
accepted policy.

## Release Impact

Release-blocking findings: none.

Rationale:

- There are 0 hard failures.
- Explicit exceptions are narrow and schema-valid.
- Remaining warnings were intentionally preserved by Arc 02 as visible backlog
  or later maintenance.
- No warning class discovered in this audit contradicts current README,
  Makefile, install, or CCDP package guidance.
