# Slice 02 Closing Report: Contract Gate Design

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice02-contract-gate-design
status: proposed-done
closed-by: CC
closed-on: 2026-08-29
```

## Outcome

Slice 02 produced the requested design report:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md`

The work stayed inside the slice boundary. No checker was implemented; no
Makefile, source Markdown, mature language guide, CCDP package target, or zip
layout was modified.

## Evidence Commands

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
```

## Ledger Walk

### F-1

Status: done.

Criterion: The design report consumes the Slice 01 audit, closing report, and
CDC verification, including the parser false-positive and filtered-evidence
caveats.

Evidence: attested. The report has "Inputs Consumed" and carries forward the
Slice 01 CDC constraints: no raw regex hard gate, no filtered CSV overclaiming,
and explicit external URL handling. It references the verified 145 actionable
package-context misses.

### F-2

Status: done.

Criterion: The design names the validation surface and final Make/script entry
points.

Evidence: attested. The report chooses generated zips named by `INSTALL_ZIPS`
as the primary validation surface, `make check-package-paths` as the Makefile
target, and `scripts/check-package-paths` as the checker script entry point. It
also explains why staging directories are debug-only rather than the
authoritative surface.

### F-3

Status: done.

Criterion: The design defines hard-fail, warning, pass, or
explicit-exception behavior for every Slice 01 classification.

Evidence: attested. The report's "Classification Behavior" table covers
`bundled-reference`, `source-clone-reference`, `repo-only/provenance`,
`example-project path`, `external URL`, `parser false positive`, and
`unclassified`, including hard fail, warning, pass/skipped, and exception
behavior.

### F-4

Status: done.

Criterion: The design specifies Markdown-aware parsing behavior and rejects a
raw regex hard gate.

Evidence: attested. The report's "Markdown-Aware Parsing Requirements" section
specifies fenced code, indented code, inline links, reference definitions, code
spans, anchors, placeholders, external URLs, path normalization, and raw regex
rejection.

### F-5

Status: done.

Criterion: The design specifies the allowlist or exception schema, including
where the file lives or why no file is needed.

Evidence: attested. The report specifies `package-path-exceptions.tsv` as the
repository path and defines required columns, allowed classifications,
dispositions, reasons, source pointers, and expiration/re-entry conditions.

### F-6

Status: done.

Criterion: The design explains source edits versus staging-time transforms,
and package layout changes versus repo-only/provenance exceptions.

Evidence: attested. The report contains "Source Edit Versus Staging-Time
Transform" and "Package Layout Change Boundaries" sections with concrete
guidance for guide-local links, source-root guide paths, `workbench/**`,
`docs/dev/**`, extraction metadata, source corpora, tooling, planning
artifacts, and provenance material.

### F-7

Status: done.

Criterion: The design defines Slice 03 implementation scope and explicit
non-goals.

Evidence: attested. The report's "Slice 03 Implementation Scope" section names
the target, script, exception file, generated zip scan, parser behavior,
classification/reporting behavior, tests/fixtures, and integration points. It
also lists non-goals including mature guide edits, CCDP package targets, zip
layout changes, URL liveness checks, and raw regex hard gating.

### F-8

Status: done.

Criterion: The close report walks every ledger row and bubbles findings up to
Arc 01.

Evidence: attested. This closing report walks F-1 through F-8 and includes the
required "Bubble-up to Arc 01" section below.

## Silent-Drop Diff

Scope as specified:

- produce the slice-local design report;
- specify validation surface;
- name Make target and checker script entry point;
- choose implementation style;
- define classification and failure behavior;
- define exception schema and repository path;
- specify Markdown-aware parser requirements;
- explain source edit versus staging-time transform guidance;
- explain package layout boundaries;
- reserve or defer CCDP/protocol package work;
- define Slice 03 implementation scope and non-goals;
- update the slice ledger with attested evidence;
- write this close report with F-1 through F-8 and Bubble-up to Arc 01.

Scope delivered:

- all specified items delivered.

Silent drops: none known.

Deferred:

- checker implementation is deferred to Slice 03;
- Makefile changes are deferred to Slice 03;
- source/skill harmonisation is deferred to Arc 02 unless Slice 03 needs a
  minimal transitional exception file;
- CCDP package targets remain deferred to Arc 03.

## Bubble-up to Arc 01

Did this slice deliver its assigned Arc 01 piece?

Yes. Arc 01 assigned Slice 02 to convert the accepted Slice 01 contract into
Make/Bash-friendly validation requirements and decide warning versus hard-fail
gates. The design names the generated-zip validation surface, the
`check-package-paths` Make target, the `scripts/check-package-paths` entry
point, the exception schema, classification behavior, parser requirements, and
Slice 03 boundaries.

What did implementing this slice reveal that the arc-plan did not anticipate?

One implementation detail should carry forward: the script entry point should
avoid the ignored `/scripts/*.py` pattern. The design therefore chooses
`scripts/check-package-paths`, a no-suffix Python 3 script, unless Slice 03
also changes `.gitignore` deliberately.

The design also makes generated zips, not staging directories, the
authoritative validation surface. Staging scans can be a debug mode, but the
Arc 01 contract should be accepted against distributable zip contents.

Does Arc 01 need an arc-plan change before Slice 03?

No required plan change. The current Arc 01 plan already stubs Slice 03 as a
package path gate implementation slice after Slice 02 closes. Slice 03 can be
planned from this design without revising the arc scope.

Silent-drop diff at slice scale:

- specified Arc 01 contribution: implementation-ready gate design;
- delivered contribution:
  `slice02-contract-gate-design/2026.08.29-contract-gate-design.md`;
- missing contribution: none known.
