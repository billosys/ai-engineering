# CDC Verification: Slice 02 Contract Gate Design

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice02-contract-gate-design
verified-by: CDC
verified-on: 2026-08-29
cc-close-commit: c64363b
status: verified
```

## Verdict

Slice 02 is verified. The committed close set contains the slice-local design
report, the updated slice ledger, and a closing report with a per-row walk and
Bubble-up to Arc 01.

All eight slice ledger rows reproduce at CDC strength. The design is ready to
drive Slice 03 planning: `make check-package-paths` fronts a checked-in
`scripts/check-package-paths` parser script, generated zips are the
authoritative validation surface, and `package-path-exceptions.tsv` is the
line-oriented exception schema.

## Verification Commands

Run from planning worktree
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
git diff --check
rg -n "Slice 01|parser false positive|filtered CSV|external URL|145" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "check-package-paths|Makefile|script|generated zip|staging" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "bundled-reference|source-clone-reference|repo-only/provenance|example-project path|external URL|parser false positive|hard fail|warning|exception" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "Markdown-aware|fenced code|inline link|reference definition|code span|anchor|raw regex" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "allowlist|exception schema|classification|reason|path" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "source edit|staging-time transform|package layout|repo-only|provenance" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
rg -n "Slice 03|implementation scope|non-goals|out of scope|CCDP|mature" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md
test -f project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|Bubble-up to Arc 01" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/closing-report.md
rg -n "\| F-[0-9]+ \|.*\| open \|" project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/ledger.md
```

Run from implementation checkout
`/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
git diff --check
rg -n "/scripts/\*\.py" .gitignore
```

## Ledger Walk

### F-1

Status: reproduced.

The design report consumes the Slice 01 audit, closing report, and CDC
verification. It cites the verified 145 actionable misses and carries forward
the parser false-positive, filtered CSV, and external URL accounting caveats.

### F-2

Status: reproduced.

The design names generated zips from `INSTALL_ZIPS` as the authoritative
validation surface, `check-package-paths` as the Make target, and
`scripts/check-package-paths` as the checker entry point. It treats staging
directories as debug-only.

### F-3

Status: reproduced.

The classification table covers `bundled-reference`, `source-clone-reference`,
`repo-only/provenance`, `example-project path`, `external URL`, `parser false
positive`, and `unclassified`, with hard-fail, warning, pass/skipped, and
explicit-exception behavior.

### F-4

Status: reproduced.

The Markdown-aware parser requirements cover inline links, image links,
reference definitions, fenced code, indented code, code spans, anchors,
placeholders, external URLs, path normalization, and raw regex rejection.

### F-5

Status: reproduced.

The design specifies top-level `package-path-exceptions.tsv` with required
columns: package, document, target, classification, disposition, reason,
source, and expires. It also defines the allowed dispositions and rejects empty
reasons.

### F-6

Status: reproduced.

The design distinguishes source edits from staging-time transforms and defines
package layout boundaries. It explicitly keeps workbench material, source
corpora, extraction metadata, maintenance tooling, planning artifacts, and
full CCDP distribution materials out of default skill bundles.

### F-7

Status: reproduced.

The Slice 03 implementation section names the target, script, exception file,
generated zip scan, parser behavior, classification/reporting behavior, tests
or fixtures, and Make integration. It also lists non-goals including mature
guide edits, CCDP package targets, zip layout changes, URL liveness checks,
and raw regex hard gating.

### F-8

Status: reproduced.

The closing report exists, walks F-1 through F-8, includes a silent-drop diff,
and includes the required Bubble-up to Arc 01 section.

## Additional Checks

The committed CC close set at `c64363b` contains only:

- `slice02-contract-gate-design/2026.08.29-contract-gate-design.md`;
- `slice02-contract-gate-design/closing-report.md`;
- `slice02-contract-gate-design/ledger.md`.

The implementation checkout had no slice changes. The design's choice of
`scripts/check-package-paths` as a no-suffix script is consistent with the
current implementation `.gitignore`, which ignores `/scripts/*.py`.

The ledger has no remaining open F-rows.

## Bubble-up Check

Slice 02 delivered its assigned Arc 01 piece. The arc asked for the Slice 01
contract to become concrete validation requirements, including warning versus
hard-fail gates. The design does that and is implementation-ready.

The close report's bubble-up is complete and honest. It surfaces two
carry-forward details for Slice 03: generated zips are authoritative, and the
script entry point should avoid the ignored `/scripts/*.py` pattern unless
Slice 03 deliberately changes `.gitignore`.

No arc scope change is required before Slice 03. This verification updates the
arc plan only to record Slice 02 as verified/closed and Slice 03 as ready, not
opened.

## What Worked

- Keeping the design artifact inside the slice directory preserved the new
  planning-branch pattern and avoided implementation `workbench/` churn.
- The design made the parser boundary explicit: Make owns orchestration, while
  a small structured script owns Markdown and zip semantics.
- Generated zips as the authoritative surface keeps the gate attached to the
  real distribution artifact rather than a source-only proxy.

## Closure

Closed at planning commit `c64363b` on 2026-08-29. Verified by CDC on
2026-08-29. Rows: 8. Done/reproduced: 8. Deferred: 0. No-op: 0.
