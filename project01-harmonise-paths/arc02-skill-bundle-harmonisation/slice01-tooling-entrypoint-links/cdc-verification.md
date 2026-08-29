# Slice 01 CDC Verification

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice01-tooling-entrypoint-links
verified-on: 2026-08-29
verified-by: CDC
status: verified-closed
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation-commit: 09d1550
planning-close-commit: 362603b
```

## Verdict

CDC verified Arc 02 Slice 01 as closed.

The slice delivered the assigned Arc 02 piece: low-risk tooling/simple skill
entrypoint links now use package/source-valid `guides/...` paths, the targeted
bundled-reference warning class is burned down from 20 to 0, and the package
path gate remains green with 0 hard failures.

The implementation changes are committed on `main` at `09d1550`, and the
planning close is committed on `planning` at `362603b`.

## Reproduced Evidence

From `/Users/oubiwann/lab/billosys/ai-engineering`:

- `make check-package-paths`
  - `zips scanned: 12`
  - `markdown files scanned: 171`
  - `hard failures: 0`
  - `warnings: 406`
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
- targeted source-root reference check:
  - `rg -n "knowledge/(deno|biome|tailwindcss|cobalt)/guides" ...`
  - no matches
- targeted exception retirement check:
  - `rg -n "knowledge/(deno|biome|tailwindcss|cobalt)/guides" package-path-exceptions.tsv`
  - no matches

From `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

- `git diff --check`
  - passed
- `find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/artifacts -maxdepth 3 -type f -print`
  - confirms durable evidence is under this slice's `artifacts/` directory
- `rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|Artifacts|Bubble-up to Arc 02" .../closing-report.md`
  - confirms the close report walks every ledger row, inventories artifacts,
    and includes Bubble-up to Arc 02

CC's own artifact `artifacts/targeted-warning-burndown.txt` records:

- baseline targeted bundled-reference warnings: 20
- post-change targeted bundled-reference warnings: 0
- total warnings before: 426
- total warnings after: 406

The independent `make check-package-paths` rerun reproduced the final total
warning count of 406 and 0 hard failures.

## Ledger Verification

### F-1

Status: verified done.

The baseline targeted warning inventory exists under `artifacts/` and records
20 targeted bundled-reference warnings before the slice. The baseline full gate
artifact records 426 total warnings and 0 hard failures.

### F-2

Status: verified done.

The targeted files no longer contain
`knowledge/(deno|biome|tailwindcss|cobalt)/guides` references, and the
replacement `guides/...` paths are the package-local paths produced in the
generated skill bundles.

### F-3

Status: verified done.

The targeted transitional exception rows are absent from
`package-path-exceptions.tsv`, and the exception schema check passes.

### F-4

Status: verified done.

`make check-package-paths` exits 0 with 0 hard failures. The targeted warning
class moved from 20 to 0 and total warnings moved from 426 to 406.

### F-5

Status: verified done.

`make check-skills` and `make all` both pass from the implementation checkout.

### F-6

Status: verified done.

The source implementation commit `09d1550` contains:

- `Makefile`
- `knowledge/biome/SKILL-js-linter.md`
- `knowledge/biome/SKILL-web-linter.md`
- `knowledge/cobalt/SKILL.md`
- `knowledge/deno/SKILL-js-linter.md`
- `knowledge/tailwindcss/SKILL.md`
- `package-path-exceptions.tsv`
- `scripts/check-package-paths`

This includes the inherited Arc 01 package-gate implementation plus the Slice
01 entrypoint and exception-file changes. No mature guide prose, CCDP package
target, package layout expansion, or planning-methodology source change is in
the Slice 01 implementation scope.

### F-7

Status: verified done.

The slice-produced durable evidence is under
`slice01-tooling-entrypoint-links/artifacts/`. No source `workbench/` artifact
is needed for this close.

### F-8

Status: verified done.

`closing-report.md` walks F-1 through F-8, names the implementation diff state,
inventories artifacts, and includes Bubble-up to Arc 02.

## Bubble-up Check

The slice delivered the first Arc 02 burn-down pattern exactly as assigned in
`arc-plan.md`: simple/tooling skill entrypoints were harmonised where one
`guides/...` spelling works in both source and generated package context.

Silent-drop diff:

- Scope specified: baseline targeted inventory, source/package-valid
  entrypoint edits, targeted transitional exception retirement, package gate
  proof, compatibility checks, artifact evidence, and close report.
- Scope delivered: all specified items delivered.
- Silent drops: none found.

No Arc 02 plan change is required before opening Slice 02. The already-planned
Slice 02 collaboration-framework link focus remains the correct next slice.

## What Worked

- Keeping the first Arc 02 burn-down to small/simple entrypoints gave a clean
  source-edit proof before touching the collaboration-framework bundle or
  mature language packs.
- Slice-local `artifacts/` made the evidence trail easy to verify without
  polluting the source checkout.
- The generated-zips-as-authority gate made the package-context warning count
  independently reproducible.
