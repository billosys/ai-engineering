# CDC Verification: Slice 01 Package Path Audit

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice01-package-path-audit
verified-by: CDC
verified-on: 2026-08-29
cc-close-commit: a85f9fb
status: verified
```

## Verdict

Slice 01 is verified. The committed close set contains the slice-local audit
artifact, an updated ledger, and a closing report with a per-row walk and
Bubble-up to Arc 01.

All seven slice ledger rows reproduce at CDC strength. The actionable package
path inventory reproduces exactly: 104 bundled-reference, 38
source-clone-reference, 3 repo-only/provenance, 0 example-project path, and
145 total actionable package-context misses.

One non-blocking evidence caveat is recorded below: the report's external URL
count is off by one against the scanner's pre-filter classification path, and
the scanner's CSV output omits external URL rows. This does not affect the
package-path miss inventory because external URLs are explicitly outside
package path resolution.

## Verification Commands

Run from implementation checkout
`/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
rg -n "^INSTALL_ZIPS|\\.zip" Makefile
make help
make all
python3 /private/tmp/package_path_audit.py \
  /Users/oubiwann/lab/billosys/ai-engineering \
  collaboration-framework.zip rust-guidelines.zip go-guidelines.zip \
  cpp-guidelines.zip javascript-deno-guidelines.zip erlang-guidelines.zip \
  cobalt-guidelines.zip visual-design-system.zip tailwindcss.zip \
  deno-js-linter.zip biome-js-linter.zip biome-linter.zip
git diff --check
```

Run from planning worktree
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

```sh
test -f project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md
test ! -e /Users/oubiwann/lab/billosys/ai-engineering/workbench/2026.08.29-package-path-audit.md
rg -n "workbench/2026\\.08\\.29-package-path-audit\\.md" project01-harmonise-paths || true
rg -n "Path Contract|source clone|package root|repo-only|staging" project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md
rg -n "Disposition by Fix Type|source edit|staging|package layout|validation|CCDP" project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|Bubble-up to Arc 01" project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md
git diff --check
```

## Reproduced Counts

After a fresh `make all`, CDC reran `/private/tmp/package_path_audit.py` and
summarized its CSV output:

| Classification | Reproduced count |
| --- | ---: |
| bundled-reference | 104 |
| source-clone-reference | 38 |
| repo-only/provenance | 3 |
| example-project path | 0 |
| parser false positive | 1081 |

The actionable per-zip counts also reproduced:

| Zip | Actionable |
| --- | ---: |
| collaboration-framework.zip | 10 |
| rust-guidelines.zip | 6 |
| go-guidelines.zip | 3 |
| cpp-guidelines.zip | 17 |
| javascript-deno-guidelines.zip | 75 |
| erlang-guidelines.zip | 2 |
| cobalt-guidelines.zip | 1 |
| visual-design-system.zip | 12 |
| tailwindcss.zip | 1 |
| deno-js-linter.zip | 3 |
| biome-js-linter.zip | 7 |
| biome-linter.zip | 8 |

Total actionable package-context misses: 145.

## Ledger Walk

### F-1

Status: reproduced.

`rg -n "^INSTALL_ZIPS|\\.zip" Makefile` reproduced the current `INSTALL_ZIPS`
block at Makefile lines 18-22. The audit report's Zip Set section lists the
same 12 archives.

### F-2

Status: reproduced.

`make all` completed successfully and rebuilt all 12 archives. Independent
`zipfile` inspection reproduced the archive entry counts and Markdown-file
counts shown in the report.

### F-3

Status: reproduced.

CDC reran `/private/tmp/package_path_audit.py` over all 12 generated archives.
The package-context miss counts reproduced exactly for the actionable
classifications.

### F-4

Status: reproduced with caveat.

The actionable mismatch classifications reproduced exactly: 104
bundled-reference, 38 source-clone-reference, 3 repo-only/provenance, and 0
example-project path. Parser false positives also reproduced at 1081.

Caveat: the report says 662 external URL references. Rerunning the scanner's
own classification logic before its CSV filter observed 663 external URL
references, while the published CSV command emits no external URL rows because
the script filters them out. External URLs are explicitly outside package path
resolution, so this does not change the actionable package-miss result. Slice
02 should avoid using filtered CSV output as evidence for classes that the
validator intentionally suppresses.

### F-5

Status: reproduced.

The audit report contains the required Path Contract Proposal with Source
Clone, Package Root, Repo-Only and Provenance Material, External URLs, and
Parser False Positives sections.

### F-6

Status: reproduced.

The audit report contains the required Disposition by Fix Type section covering
source edits, staging-time transforms, package layout changes, validation
exceptions, and CCDP package work.

### F-7

Status: reproduced.

The closing report exists, walks F-1 through F-7, includes the silent-drop diff,
and includes the required Bubble-up to Arc 01 section.

## Stale Location Check

The old implementation-checkout path
`/Users/oubiwann/lab/billosys/ai-engineering/workbench/2026.08.29-package-path-audit.md`
does not exist. A planning-tree search found no stale exact references to
`workbench/2026.08.29-package-path-audit.md`.

## Bubble-up Check

No Arc 01 plan change is required before opening Slice 02. The existing Slice
02 stub already names the right next move: convert the Slice 01 contract into
Make/Bash-friendly validation requirements and decide warning versus hard-fail
gates.

Carry forward one implementation constraint: Slice 02 should design a
Markdown-aware validator rather than converting the temporary broad regex scan
directly into a hard gate.

Carry forward one evidence-reporting constraint: reports should not claim a
filtered CSV contains classes that the scanner suppresses. If a future
validator tracks external URLs, it should emit that count directly or state
that URLs were skipped.

## What Worked

- Moving the audit artifact into the slice directory made the planning record
  self-contained and avoided the ignored `workbench/` trap.
- Rebuilding the actual archives before scanning kept the evidence tied to the
  distribution surface rather than source Markdown alone.
- Separating actionable package-context misses from parser false positives
  prevented a diagnosis script from being mistaken for the final gate.

## Closure

Closed at planning commit `a85f9fb` on 2026-08-29. Verified by CDC on
2026-08-29. Rows: 7. Done/reproduced: 7. Deferred: 0. No-op: 0.
