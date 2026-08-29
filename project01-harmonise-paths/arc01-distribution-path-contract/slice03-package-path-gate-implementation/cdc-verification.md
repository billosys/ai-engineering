# CDC Verification: Slice 03 Package Path Gate Implementation

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice03-package-path-gate-implementation
verified-by: CDC
verified-on: 2026-08-29
cc-close-commit: da4c0fc
implementation-state: working-tree diff
status: verified
```

## Verdict

Slice 03 is verified against the current implementation working-tree diff.
The committed planning close set contains the updated slice ledger, a
row-by-row closing report, and durable evidence transcripts under this slice's
`artifacts/` directory.

All nine slice ledger rows reproduce at CDC strength. The implementation adds
the expected public Make target, no-suffix checker script, and transitional
exception file. The package gate runs over all 12 generated zips with zero
hard failures under the transitional policy.

The implementation changes are not committed in the source checkout at the
time of this verification. They are present as:

- `Makefile`
- `package-path-exceptions.tsv`
- `scripts/check-package-paths`

## Verification Commands

Run from implementation checkout
`/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
rg -n "check-package-paths" Makefile
test -x scripts/check-package-paths
test ! -e scripts/check-package-paths.py
scripts/check-package-paths --self-test
scripts/check-package-paths --check-exceptions-only
make check-package-paths
make check-skills
make all
git diff --check
git diff --name-only
git diff --cached --name-only
git status --short --untracked-files=all
```

Additional CDC fixtures:

```sh
scripts/check-package-paths --exceptions '' /var/folders/dt/kc8ndn6d3kx8c1jnxr05drsh0000gn/T/cdc-slice03-hard-nn3ajm4y/fixture.zip
scripts/check-package-paths --exceptions /var/folders/dt/kc8ndn6d3kx8c1jnxr05drsh0000gn/T/cdc-slice03-bad-exc-crvlvg9c/bad.tsv collaboration-framework.zip
```

Run from planning worktree
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
find project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|Artifacts|Bubble-up to Arc 01" project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/closing-report.md
rg -n "\| F-[0-9]+ \|.*\| open \|" project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/ledger.md
```

## Reproduced Package Gate Summary

`make check-package-paths` exited 0 and reported:

```text
package path check
zips scanned: 12
markdown files scanned: 171
hard failures: 0
warnings: 426
explicit exceptions: 3
skipped external URLs: 656
parser-suppressed material: omitted by Markdown parser
```

The current warnings are not harmonisation closure. They are visible
transitional work for Arc 02.

## Ledger Walk

### F-1

Status: reproduced.

`rg -n "check-package-paths" Makefile` shows the Make target, help line, and
script invocation. `scripts/check-package-paths` is executable, and
`scripts/check-package-paths.py` does not exist. `package-path-exceptions.tsv`
exists in the implementation checkout.

### F-2

Status: reproduced.

`make check-package-paths` exited 0 and scanned the generated zips named by
`INSTALL_ZIPS`. The reproduced summary shows `zips scanned: 12` and
`markdown files scanned: 171`.

### F-3

Status: reproduced.

`scripts/check-package-paths --self-test` reported `ok` for inline links,
image links, reference definitions, same-file anchors, path anchors, fenced
code, indented code, conservative code spans, placeholders, external URLs,
parser-suppressed material, and valid package paths.

### F-4

Status: reproduced.

The current package scan exits 0. A CDC-created missing-link fixture exits 1
with one `bundled-reference` hard failure. A CDC-created malformed exception
TSV exits 2 with the expected schema-header error. A missing exception file
also exits 2 as an invocation/schema error.

### F-5

Status: reproduced.

The package gate summary separates hard failures, warnings, explicit
exceptions, skipped external URLs, and parser-suppressed material. It states
that parser-suppressed material is omitted by the Markdown parser rather than
claiming a zero count, and external URLs are reported directly.

### F-6

Status: reproduced.

The slice artifact directory contains durable transcripts for package scan,
parser self-test, malformed schema, hard-failure fixture, exception schema,
entrypoint checks, implementation diff scope, `make check-skills`, `make all`,
and whitespace checks. No implementation `workbench/` artifact is required for
closure.

### F-7

Status: reproduced.

Implementation scope is limited to `Makefile`, `package-path-exceptions.tsv`,
and `scripts/check-package-paths`. No mature guide prose, CCDP package target,
package layout expansion, or planning-methodology file is part of the
implementation diff.

### F-8

Status: reproduced.

`make check-skills` exited 0 with `>> all skill descriptions within limit`.
`make all` exited 0 and rebuilt all generated skill zips through the final
`collaboration-framework.zip` target.

### F-9

Status: reproduced.

The closing report exists, walks F-1 through F-9, names the implementation
state as uncommitted, inventories artifacts, and includes Bubble-up to Arc 01.

## Bubble-up Check

Slice 03 delivered its assigned Arc 01 piece: the distribution path contract
is executable through `make check-package-paths` against generated zip
artifacts.

The close report's bubble-up is honest. It correctly states that current
warnings remain Arc 02 harmonisation work, transitional bundled-reference rows
should expire after Arc 02, code-span findings remain warnings by design, and
visual-design source-clone links are visible as package warnings.

No new Slice 03 iteration is required.

Arc 01 should now close formally before Arc 02 is planned in detail. The arc
close should record that the source implementation was verified as a
working-tree diff unless the operator commits the implementation before arc
close.

## What Worked

- The new per-slice `artifacts/` home made CC's durable evidence easy to
  inspect without adding scratch files to the source checkout.
- The gate is Make-owned but keeps Markdown and zip semantics in a structured
  script, which matches the Slice 02 design boundary.
- Transitional warnings keep the package-path debt visible without pretending
  Arc 02 harmonisation has already happened.

## Closure

Closed at planning commit `da4c0fc` on 2026-08-29. Verified by CDC on
2026-08-29. Rows: 9. Done/reproduced: 9. Deferred: 0. No-op: 0.
