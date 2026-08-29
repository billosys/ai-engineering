# Slice 03 Closing Report

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice03-mature-entrypoint-staging-transforms
closed-on: 2026-08-29
closed-by: CC
status: proposed-done
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation-diff-state: uncommitted working tree
```

## Summary

Slice 03 added a narrow package-staging transform for mature language skill
entrypoints. The source `knowledge/rust/SKILL.md` and `knowledge/js/SKILL.md`
files retain their source-oriented path text, while generated package copies
rewrite guide references to package-local `guides/...` paths.

The targeted mature entrypoint `bundled-reference` rows moved from 107 to 0.
The total package-path warning count moved from 402 to 295 with no hard
failures.

## Implementation Diff Scope

Slice 03 edited:

- `Makefile`
- `scripts/stage-skill-entrypoint`
- `package-path-exceptions.tsv`

No mature guide prose, collaboration-framework bundle files, CCDP package
files, package layout expansion, or missing asset additions were changed.

## Artifacts

Durable evidence lives under this slice's `artifacts/` directory:

- `README.md`: artifact directory purpose.
- `baseline-make-check-package-paths.txt`: baseline full package-path gate
  transcript.
- `baseline-mature-bundled-reference-warnings.tsv`: baseline mature-language
  bundled-reference warning inventory.
- `mature-warning-classification.md`: candidate/non-candidate classification.
- `transform-candidate-inventory.tsv`: baseline entrypoint rows selected for
  staging-transform treatment.
- `post-make-check-package-paths.txt`: post-change package-path gate
  transcript.
- `post-mature-bundled-reference-warnings.tsv`: post-change mature-language
  bundled-reference warning inventory.
- `mature-warning-burndown.tsv`: baseline/post package and entrypoint counts.
- `entrypoint-target-resolution.md`: staged zip and source target checks.
- `check-exceptions-only.txt`: exception schema validation.
- `make-check-skills.txt`: skill-description compatibility check.
- `make-all.txt`: full package build compatibility check.
- `git-diff-check-implementation.txt`: implementation whitespace check.
- `git-diff-check-planning.txt`: planning whitespace check.
- `git-status-implementation.txt`: implementation checkout status.
- `implementation-diff-scope.md`: implementation scope inventory.
- `artifact-inventory.txt`: planning `find .../artifacts` inventory.

## Ledger Walk

### F-1

Status: done.

`artifacts/baseline-make-check-package-paths.txt` records the generated-package
baseline from `make check-package-paths`: 0 hard failures, 402 warnings, and 3
explicit exceptions. `artifacts/baseline-mature-bundled-reference-warnings.tsv`
records the mature-language `bundled-reference` inventory: Rust 37 rows,
JavaScript/Deno 157 rows, C++ 2 rows, Go 0 rows, and Erlang 0 rows.

### F-2

Status: done.

`artifacts/mature-warning-classification.md` classifies the baseline before
the exception file changed:

- Rust: 31 entrypoint staging candidates and 6 guide-internal missing
  `09-common-pitfalls.md` rows.
- JavaScript/Deno: 76 entrypoint staging candidates and 81 guide-internal
  `12-deno/**` / `13-biome/**` rows.
- C++: 2 missing image/package-layout rows in `guides/03-functions.md`.
- Go and Erlang: no mature bundled-reference rows.

### F-3

Status: done.

`scripts/stage-skill-entrypoint` is deterministic and constrained. It only
transforms `knowledge/rust/SKILL.md` and `knowledge/js/SKILL.md`; every other
entrypoint is copied unchanged. The helper rewrites source-root guide prefixes
and guide-file references that resolve under the entrypoint's bundled
`guides/` tree. `Makefile` invokes the helper only at the entrypoint staging
step in `pack_skill`.

### F-4

Status: done.

`artifacts/entrypoint-target-resolution.md` records generated zip checks for
Rust and JavaScript/Deno staged `SKILL.md` references, zip member checks for
the corresponding `guides/...` files, and source-checkout target checks. The
post-change package inventory records Rust and JavaScript/Deno entrypoint
`bundled-reference` rows at 0.

### F-5

Status: done.

`package-path-exceptions.tsv` retired the six transformed entrypoint
transitional rows: four Rust `SKILL.md` rows and two JavaScript/Deno
`SKILL.md` rows. The remaining Rust guide-internal rows, JavaScript/Deno
guide-internal rows, and C++ image rows remain visible transitional warnings.
`artifacts/check-exceptions-only.txt` records
`exception schema ok: package-path-exceptions.tsv`.

### F-6

Status: done.

`artifacts/post-make-check-package-paths.txt` records `make check-package-paths`
exiting 0 with 0 hard failures and 295 warnings.
`artifacts/mature-warning-burndown.tsv` records:

- Rust entrypoint bundled-reference rows: 31 -> 0.
- JavaScript/Deno entrypoint bundled-reference rows: 76 -> 0.
- Mature entrypoint bundled-reference rows total: 107 -> 0.
- Total package warnings: 402 -> 295.

### F-7

Status: done.

`artifacts/make-check-skills.txt` records `>> all skill descriptions within
limit`. `artifacts/make-all.txt` records successful package generation through
`collaboration-framework.zip`.

### F-8

Status: done.

`artifacts/implementation-diff-scope.md` and
`artifacts/git-status-implementation.txt` record implementation changes limited
to `Makefile`, `package-path-exceptions.tsv`, and new
`scripts/stage-skill-entrypoint`. `git diff --check` also passed in the
implementation checkout.

### F-9

Status: done.

All durable slice-produced evidence is under
`slice03-mature-entrypoint-staging-transforms/artifacts/`.

### F-10

Status: done.

This report walks F-1 through F-10, names the implementation diff state,
inventories artifacts, and includes Bubble-up to Arc 02 below.

## Bubble-up to Arc 02

This slice delivered the mature-entrypoint staging-transform piece assigned by
the Arc 02 plan. The staging pattern is now proven for mature entrypoints where
source-root or guide-relative text is useful in the source clone but must
resolve as package-local `guides/...` paths in generated zips.

Findings for Arc 02 and Slice 04:

- The targeted mature entrypoint warning class is burned down from 107 to 0.
- Remaining mature-language `bundled-reference` warnings are not entrypoint
  staging candidates: Rust has 6 guide-internal missing `09-common-pitfalls.md`
  rows, JavaScript/Deno has 81 guide-internal cross-guide rows, and C++ has 2
  missing image/package-layout rows.
- Slice 04 should decide whether those remaining transitional rows become
  explicit policy exceptions, later remediation scope, or a tighter warning
  policy. This slice intentionally did not hide them.

Silent-drop diff:

- Scope specified: baseline mature-language inventory, classification before
  edits, narrow entrypoint staging transform, exception retirement, staged and
  source target checks, package gates, compatibility checks, diff-scope
  evidence, durable artifacts, ledger update, and close report.
- Scope delivered: all specified items delivered.
- Silent drops: none known.

No Arc 02 plan change is required before Slice 04. The existing Slice 04
warning-policy-tightening scope remains the right next step.
