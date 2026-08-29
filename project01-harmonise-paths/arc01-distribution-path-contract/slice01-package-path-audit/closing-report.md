# Slice 01 Closing Report: Package Path Audit

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice01-package-path-audit
status: proposed-done
closed-by: CC
closed-on: 2026-08-29
```

## Outcome

Slice 01 produced the requested package path audit report:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md`

The implementation work stayed inside the slice boundary: diagnosis and path
contract only. No mature language guides, skill files, Makefile targets, final
validation gate, or CCDP package targets were changed.

## Evidence Commands

Executed from implementation checkout
`/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make help
rg -n "^INSTALL_ZIPS|\\.zip" Makefile
sed -n '1,220p' Makefile
make all
python3 /private/tmp/package_path_audit.py \
  /Users/oubiwann/lab/billosys/ai-engineering \
  collaboration-framework.zip rust-guidelines.zip go-guidelines.zip \
  cpp-guidelines.zip javascript-deno-guidelines.zip erlang-guidelines.zip \
  cobalt-guidelines.zip visual-design-system.zip tailwindcss.zip \
  deno-js-linter.zip biome-js-linter.zip biome-linter.zip \
  > /private/tmp/package_path_audit.csv
```

Summary from `/private/tmp/package_path_audit.csv`:

- 12 zips scanned.
- 171 Markdown files scanned.
- 145 actionable package-context misses classified.
- 104 bundled-reference.
- 38 source-clone-reference.
- 3 repo-only/provenance.
- 0 example-project path.
- 662 external URL references classified outside package resolution.
- 1081 parser false positives separated from actionable misses.

## Ledger Walk

### F-1

Status: done.

Criterion: The audit identifies the exact top-level zip set under review from
the current Makefile.

Evidence: attested. `rg -n "^INSTALL_ZIPS|\\.zip" Makefile` shows the current
`INSTALL_ZIPS` block at Makefile:18-22. The report's "Zip Set" section lists
all 12 archives from that block.

### F-2

Status: done.

Criterion: The audit inspects actual generated zip contents rather than only
source Markdown.

Evidence: attested. `make all` rebuilt every archive named by `INSTALL_ZIPS`
and printed each archive listing. The report records archive entry counts and
Markdown-file counts from Python `zipfile` inspection.

### F-3

Status: done.

Criterion: The audit reproduces package-context path misses for bundled
Markdown references.

Evidence: attested. `/private/tmp/package_path_audit.py` scanned Markdown inside
each zip package root and wrote `/private/tmp/package_path_audit.csv`. The
report includes the exact scan command, scanner method, and counts by zip.

### F-4

Status: done.

Criterion: Each observed mismatch is classified as bundled-reference,
source-clone-reference, repo-only/provenance, example-project path, external
URL, or parser false positive.

Evidence: attested. The report's summary and "Counts by Zip and Class" table
classify all observed scanner output. There is no unclassified miss bucket.
The opened class names were retained.

### F-5

Status: done.

Criterion: The report recommends a path contract that supports both
cloned-source and zip/unzipped use.

Evidence: attested. The report contains a "Path Contract Proposal" section with
explicit `Source Clone`, `Package Root`, `Repo-Only and Provenance Material`,
`External URLs`, and `Parser False Positives` subsections.

### F-6

Status: done.

Criterion: The report distinguishes source edits, staging-time transforms,
package layout changes, validation exceptions, and CCDP package work.

Evidence: attested. The report contains a "Disposition by Fix Type" section
with rows for source edit, staging-time transform, package layout change,
validation exception, and CCDP package work.

### F-7

Status: done.

Criterion: The close report walks every ledger row and bubbles findings up to
Arc 01.

Evidence: attested. This closing report walks F-1 through F-7 and includes the
required "Bubble-up to Arc 01" section below.

## Silent-Drop Diff

Scope as specified:

- inspect Makefile packaging definitions;
- inspect or rebuild every generated zip named by `INSTALL_ZIPS`;
- scan bundled Markdown for package-context path misses;
- classify misses with the opened vocabulary;
- recommend the path contract and later fix dispositions;
- update the slice ledger with attested evidence;
- write this closing report with F-1 through F-7 and bubble-up.

Scope delivered:

- all specified items delivered.

Silent drops: none known.

Deferred:

- final validation gate implementation is intentionally deferred to Slice 02.
- source/skill/Makefile/CCDP package changes are intentionally deferred to
  later implementation slices and arcs.
- independent reproduction is deferred to CDC verification; this close is
  attested/proposed-done.

## Bubble-up to Arc 01

Did this slice deliver its assigned Arc 01 piece?

Yes. Arc 01 assigned Slice 01 to reproduce the source-root versus package-root
mismatch, classify current package-invalid references, and propose the
contract language that Slice 02 can turn into validation requirements. The
report supplies the inventory, classifications, contract proposal, and Slice 02
implications.

What did implementation reveal that the arc-plan did not anticipate?

The broad diagnosis scanner found 1081 parser false positives, mostly from
examples and C++-heavy Markdown. This reinforces that Slice 02 should not
convert the temporary regex scanner directly into a hard gate. The validation
design needs Markdown-aware skipping for fenced code, placeholders, examples,
anchors, and non-path identifiers.

The audit also found no confirmed `example-project path` package misses in the
actionable set. The category should remain in the contract because it is useful
for later validation policy, but Slice 02 should treat it as an allowlist class
with evidence rather than a currently observed high-volume class.

Does Arc 01 need an arc-plan change before Slice 02?

No required plan change. The current Slice 02 stub already says it should
convert the Slice 01 contract into Make/Bash-friendly validation requirements
and decide warning versus hard-fail gates. The only planning emphasis to carry
forward is that Slice 02 must design a real validator rather than hardening the
temporary regex scanner without Markdown structure.

Silent-drop diff at slice scale:

- specified Arc 01 contribution: evidence-backed inventory plus path semantics
  contract proposal;
- delivered contribution: `2026.08.29-package-path-audit.md` in this slice
  directory, with
  zip set, package model, scan method, counts, inventory, path contract,
  disposition by fix type, and Slice 02 implications;
- missing contribution: none known.
