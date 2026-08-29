# Slice 03 CDC Verification

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice03-mature-entrypoint-staging-transforms
verified-on: 2026-08-29
verified-by: CDC
status: verified-closed
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation-commit: a8decce
planning-close-commit: 11a115c
```

## Verdict

CDC verified Arc 02 Slice 03 as closed.

The slice delivered the intended mature-entrypoint staging transform without
rewriting mature guide prose. The transform is constrained to the Rust and
JavaScript/Deno skill entrypoints, package copies resolve through `guides/...`,
source entrypoints remain source-root useful, and the targeted mature
entrypoint `bundled-reference` warning class moved from 107 rows to 0.

## Reproduced Evidence

From `/Users/oubiwann/lab/billosys/ai-engineering`:

- `make check-package-paths`
  - `zips scanned: 12`
  - `markdown files scanned: 171`
  - `hard failures: 0`
  - `warnings: 295`
  - `explicit exceptions: 3`
  - `skipped external URLs: 656`
  - `parser-suppressed material: omitted by Markdown parser`
- `scripts/check-package-paths --check-exceptions-only`
  - `exception schema ok: package-path-exceptions.tsv`
- `make check-skills`
  - `>> all skill descriptions within limit`
- `make all`
  - regenerated all package zips through `collaboration-framework.zip`
- `git diff --check`
  - passed
- `git status --short --branch`
  - `## main...origin/main`

From `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

- `git diff --check`
  - passed
- `find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/artifacts -maxdepth 2 -type f -print`
  - confirms durable evidence is under this slice's `artifacts/` directory
- `rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 02" .../closing-report.md`
  - confirms the close report walks every ledger row, inventories artifacts,
    and includes Bubble-up to Arc 02

CC's `artifacts/mature-warning-burndown.tsv` records:

- Rust entrypoint `bundled-reference` rows: 31 -> 0
- JavaScript/Deno entrypoint `bundled-reference` rows: 76 -> 0
- Mature entrypoint `bundled-reference` rows total: 107 -> 0
- Total package warnings: 402 -> 295

CDC reproduced the final package-path totals and independently inspected the
staged package output. Rebuilt `rust-guidelines.zip` and
`javascript-deno-guidelines.zip` contain package-local `guides/...` entrypoint
references while retaining the expected guide members under each generated
package root.

## Ledger Verification

### F-1

Status: verified done.

The baseline package-path transcript and mature-language bundled-reference
inventory exist under `artifacts/`. They record 0 hard failures, 402 total
warnings, and mature bundled-reference rows concentrated in Rust,
JavaScript/Deno, and C++.

### F-2

Status: verified done.

`artifacts/mature-warning-classification.md` classifies the mature warning
surface before the transform:

- Rust: 31 entrypoint staging candidates and 6 guide-internal missing
  `09-common-pitfalls.md` rows.
- JavaScript/Deno: 76 entrypoint staging candidates and 81 guide-internal
  `12-deno/**` / `13-biome/**` cross-guide rows.
- C++: 2 missing image/package-layout rows in `guides/03-functions.md`.
- Go and Erlang: no mature bundled-reference action for this slice.

### F-3

Status: verified done.

The implementation is narrow and deterministic. `Makefile` routes per-domain
skill entrypoint staging through `scripts/stage-skill-entrypoint`; the helper
names only `knowledge/rust/SKILL.md` and `knowledge/js/SKILL.md` as transformed
files, and copies all other entrypoints unchanged.

### F-4

Status: verified done.

`artifacts/entrypoint-target-resolution.md` records package and source target
checks. CDC also inspected rebuilt staged entrypoints from the generated zips:
the packaged Rust and JavaScript/Deno entrypoints use package-local
`guides/...` references, and the zip member listings include the corresponding
guide files.

### F-5

Status: verified done.

`package-path-exceptions.tsv` retired the six resolved transitional entrypoint
rows: four Rust `SKILL.md` rows and two JavaScript/Deno `SKILL.md` rows. The
remaining Rust guide-internal, JavaScript/Deno guide-internal, and C++ image
rows remain visible transitional warnings for Slice 04 policy disposition.
The exception schema check passes.

### F-6

Status: verified done.

`make check-package-paths` exits 0 with 0 hard failures and 295 warnings. The
targeted mature-entrypoint bundled-reference warning class moved from 107 rows
to 0, matching the slice close report.

### F-7

Status: verified done.

`make check-skills` and `make all` both pass from the implementation checkout.
`make check-package-paths` also rebuilds all zips before checking them.

### F-8

Status: verified done.

CDC inspected source commit `a8decce`. The implementation scope is limited to:

- `Makefile`
- `package-path-exceptions.tsv`
- `scripts/stage-skill-entrypoint`

No mature guide prose, collaboration-framework bundle files, CCDP package
files, package layout expansion, or missing asset additions were changed.

### F-9

Status: verified done.

Durable slice-produced evidence is under
`slice03-mature-entrypoint-staging-transforms/artifacts/`.

### F-10

Status: verified done.

`closing-report.md` walks F-1 through F-10, names implementation state,
inventories artifacts, and includes Bubble-up to Arc 02. CDC notes that the
implementation is now committed on `main` at `a8decce`.

## Bubble-up Check

The slice delivered the mature-entrypoint staging-transform capability assigned
by `arc-plan.md`.

Silent-drop diff:

- Scope specified: baseline mature-language inventory, classification before
  edits, narrow entrypoint staging transform, exception retirement, staged and
  source target checks, package gates, compatibility checks, diff-scope
  evidence, durable artifacts, ledger update, and close report.
- Scope delivered: all specified items delivered.
- Silent drops: none found.

Slice 04 should now tighten the warning policy surface. The remaining 295
warnings include 89 `bundled-reference` rows, 146 `repo-only/provenance` rows,
26 `source-clone-reference` rows, 25 `example-project path` rows, and 9 parser
false positives. Slice 04 should retire or reclassify transitional rows,
promote truly intentional rows to explicit exceptions, and leave any real
later-arc remediation visible rather than hiding it behind a broad allowlist.
