# Slice 04 CDC Verification

```yaml
project: project01-harmonise-paths
arc: arc03-ccdp-distribution-package
slice: slice04-ccdp-reader-guidance
verified-on: 2026-08-29
verified-by: CDC
status: verified-closed
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
implementation-commit: b5e55c5
planning-close-commit: a0e81ac
```

## Verdict

CDC verified Arc 03 Slice 04 as closed.

The slice delivered the reader-facing guidance complement to the CCDP package:
source-clone users are pointed at `protocols/ccdp/README.md`, package users
are pointed at `ccdp/README.md`, and the package README is sourced from
`protocols/ccdp/README.md` instead of generated inline by the root `Makefile`.
No remediation slice is required before Arc 03 close.

## Reproduced Evidence

From `/Users/oubiwann/lab/billosys/ai-engineering`:

- `git show --stat --oneline HEAD`
  - `b5e55c5 Document CCDP reader entrypoints`
  - changed `README.md`, `Makefile`, and `protocols/ccdp/README.md`
- `make ccdp-package`
  - passed
  - assembled-spec freshness check passed
  - produced `ccdp.zip` with one `ccdp/` root and 122 entries
- `make check-ccdp-package`
  - passed
  - reported 42 Markdown files scanned
  - reported 14 package references checked
  - reported 91 protocol-syntax skips
  - reported 4 external URLs skipped
  - reported 0 shape errors, 0 README errors, and 0 Markdown path failures
  - rebuilt from an extracted package using the packaged `Makefile`
- `unzip -p ccdp.zip ccdp/README.md`
  - confirmed package-local links to the assembled spec, `src/README.md`,
    `json/MANIFEST.md`, `visual-guide/index.html`, and
    `visual-guide/ccdp-reference.md`
- `make check-package-paths`
  - passed
  - reported 12 zips scanned, 171 Markdown files scanned, 0 hard failures,
    295 warnings, 3 explicit exceptions, and 656 skipped external URLs
- `make all`
  - passed
- `make ccdp`
  - passed
- `scripts/check-package-paths --check-exceptions-only`
  - passed with `exception schema ok: package-path-exceptions.tsv`
- `make check-skills`
  - passed
- `git diff --check`
  - passed
- `git diff --cached --check`
  - passed
- `git status --short --branch --untracked-files=all`
  - `## main...origin/main [ahead 3]`

From `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

- `git show --stat --oneline HEAD`
  - `a0e81ac Close CCDP reader guidance slice`
  - added the Slice 04 close report and durable `artifacts/`
  - updated the Slice 04 ledger
- `git diff --check`
  - passed
- `git diff --cached --check`
  - passed
- `test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice04-ccdp-reader-guidance/closing-report.md`
  - passed
- `rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|Artifacts|Bubble-up to Arc 03" .../closing-report.md`
  - confirmed the close report walks every row, inventories artifacts, and
    bubbles forward to Arc 03

The CC close report names the implementation state as an uncommitted source
diff. At CDC verification time, that source work had already been committed as
`b5e55c5`. CDC verified the committed state and both worktrees remained clean
apart from the pre-existing untracked `project02-collab-breakout/` planning
stub.

## Ledger Verification

### F-1

Status: verified done.

`README.md` now points source-clone users to
`protocols/ccdp/README.md`,
`protocols/ccdp/composite-cognition-dispatch-protocol.md`,
`protocols/ccdp/src/README.md`, `protocols/ccdp/json/MANIFEST.md`,
`protocols/ccdp/visual-guide/index.html`, and
`protocols/ccdp/visual-guide/ccdp-reference.md`.

### F-2

Status: verified done.

`unzip -p ccdp.zip ccdp/README.md` confirmed package users are pointed at
package-local paths: `composite-cognition-dispatch-protocol.md`,
`src/README.md`, `json/MANIFEST.md`, `visual-guide/index.html`, and
`visual-guide/ccdp-reference.md`.

### F-3

Status: verified done.

The root README distinguishes installable skill bundle zips from `ccdp.zip`.
The root `Makefile` help lists `make ccdp`, `make ccdp-package`, and
`make check-ccdp-package`, while `INSTALL_ZIPS`, `make skills`, `make all`,
and `make install` remain skill-bundle scoped.

### F-4

Status: verified done.

`Makefile` copies `protocols/ccdp/README.md` into `ccdp/README.md`.
`make check-ccdp-package` reports 0 README errors and 0 Markdown path failures.

### F-5

Status: verified done.

Changed guidance labels `protocols/ccdp/workbench/` and
`protocols/ccdp/prompts/` as source-only provenance/review/prompt material
that is intentionally excluded from `ccdp.zip`.

### F-6

Status: verified done.

`make ccdp-package` and `make check-ccdp-package` both passed against the
committed source state.

### F-7

Status: verified done.

`make ccdp` passed after the reader-guidance changes. The source checkout
remained clean afterward, so no generated assembled-spec drift was introduced.

### F-8

Status: verified done.

`make check-package-paths`, `make all`, `scripts/check-package-paths
--check-exceptions-only`, and `make check-skills` all passed. The existing
skill-bundle package-path baseline remains 0 hard failures, 295 warnings, and
3 explicit exceptions.

### F-9

Status: verified done.

The implementation commit is scoped to reader guidance and README staging:
`README.md`, `Makefile`, and `protocols/ccdp/README.md`. No CCDP runtime
behavior, protocol semantic rewrite, workbench inclusion, prompt inclusion, or
unrelated source edit was found.

### F-10

Status: verified done.

`closing-report.md` exists, inventories durable artifacts, names implementation
state, walks F-1 through F-10, and bubbles the result to Arc 03. CDC reconciled
the stale "uncommitted diff" wording with the current committed source state.

## Bubble-up Check

Slice 04 delivered the final reader-guidance piece assigned by Arc 03. CCDP now
has package mechanics, validation, source-clone guidance, and package-local
reader guidance.

Silent-drop diff:

- Scope specified: document source-clone entrypoints, document package/unzipped
  entrypoints, distinguish skill zips from `ccdp.zip`, keep package README
  source-aligned, label excluded workbench/prompts material, preserve existing
  checks, and close with durable artifacts.
- Scope delivered: all specified items are present in source commit `b5e55c5`
  and planning close commit `a0e81ac`, with CDC-reproduced gates.
- Silent drops: none found.

Arc-plan impact: Arc 03 can proceed to formal close. Arc 04 remains the next
planned arc for release/adoption hardening and publication-facing polish.
