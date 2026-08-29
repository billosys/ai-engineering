# Slice 04 CDC Verification

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice04-warning-policy-tightening
verified-on: 2026-08-29
verified-by: CDC
status: verified-closed
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation-commit: 4168a57
planning-close-commit: 9c568b7
```

## Verdict

CDC verified Arc 02 Slice 04 as closed.

The slice delivered warning-policy tightening without suppressing unresolved
package usability work. The five stale `transitional-warning` /
`expires=after-arc02` rows in `package-path-exceptions.tsv` were converted to
ordinary visible warnings with concrete later-maintenance expiry labels. No new
explicit exceptions, broad allowlists, checker suppressions, mature guide prose
rewrites, CCDP targets, or package layout changes were introduced.

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
- Warning class counts from the package-path output:
  - 89 `bundled-reference`
  - 146 `repo-only/provenance`
  - 26 `source-clone-reference`
  - 25 `example-project path`
  - 9 parser false positives
- `scripts/check-package-paths --check-exceptions-only`
  - `exception schema ok: package-path-exceptions.tsv`
- `make check-skills`
  - `>> all skill descriptions within limit`
- `make all`
  - regenerated all package zips through `collaboration-framework.zip`
- `git diff --check`
  - passed
- `rg -n "after-arc02|transitional-warning" package-path-exceptions.tsv`
  - no matches

CDC initially ran two package-writing Make targets concurrently during
verification, which produced transient duplicate `guides/guides` entries in
the generated zips and a spurious package-path failure. CDC discarded that
result, reran the package-writing gates serially, and reproduced the passing
package-path gate twice. The final serial transcript has no `guides/guides`
matches.

From `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

- `git diff --check`
  - passed
- `find project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts -maxdepth 2 -type f -print`
  - confirms durable evidence is under this slice's `artifacts/` directory
- `rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 02" .../closing-report.md`
  - confirms the close report walks every ledger row, inventories artifacts,
    and includes Bubble-up to Arc 02

## Ledger Verification

### F-1

Status: verified done.

The current warning baseline is recorded in
`artifacts/current-warning-baseline.txt`,
`artifacts/current-warning-inventory.tsv`, and
`artifacts/current-warning-counts.tsv`. CDC reproduced the baseline from
generated zips with 0 hard failures and 295 warnings.

### F-2

Status: verified done.

`artifacts/warning-policy-classification.md` classifies the remaining warning
classes and distinguishes visible later remediation from narrow explicit
exceptions.

### F-3

Status: verified done.

`artifacts/transitional-exception-disposition.md` walks every prior
`expires=after-arc02` row. CDC confirmed no `after-arc02` or
`transitional-warning` text remains in `package-path-exceptions.tsv`.

### F-4

Status: verified done.

The implementation commit changes only five disposition/reason/expiry rows in
`package-path-exceptions.tsv`. No broad explicit exception or checker
suppression was added.

### F-5

Status: verified done.

`artifacts/later-arc-backlog.md` preserves unresolved package usability work as
visible backlog: Rust missing CLI pitfalls guide references, C++ missing image
assets, JavaScript/Deno guide shorthand, repo/provenance references,
source-clone references, example-project paths, and parser false positives.

### F-6

Status: verified done.

`make check-package-paths` exits 0 after policy tightening with 0 hard failures,
295 warnings, and 3 explicit exceptions.

### F-7

Status: verified done.

`scripts/check-package-paths --check-exceptions-only`, `make check-skills`, and
`make all` pass from the implementation checkout.

### F-8

Status: verified done.

CDC inspected source commit `4168a57`. The implementation scope is limited to
`package-path-exceptions.tsv`; no checker code, mature guide prose,
collaboration-framework methodology, CCDP target, or package layout expansion
changed.

### F-9

Status: verified done.

Durable slice-produced evidence is under
`slice04-warning-policy-tightening/artifacts/`.

### F-10

Status: verified done.

`closing-report.md` walks F-1 through F-10, names implementation state,
inventories artifacts, and includes Bubble-up to Arc 02. CDC notes that the
implementation is now committed on `main` at `4168a57`.

## Bubble-up Check

The slice delivered the warning-policy tightening piece assigned by
`arc-plan.md`. It removed stale Arc 02 transitional debt, kept the warning
surface visible, and prepared Arc 02 for formal composition close.

Silent-drop diff:

- Scope specified: current warning baseline, classification, transitional row
  disposition, narrow exception policy, later-arc backlog, package gates,
  compatibility checks, diff-scope evidence, durable artifacts, ledger update,
  and close report.
- Scope delivered: all specified items delivered.
- Silent drops: none found.

No remediation slice is required before Arc 02 close. The remaining package
warning backlog is intentionally routed to later guide/package maintenance or
release/adoption policy work, not hidden as Arc 02 success.
