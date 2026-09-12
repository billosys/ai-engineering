# CDC Review: Arc01 Slice01

Date: 2026-09-12. Status: **changes required; not independently closed**.
Reviewed the uncommitted CC packet against the project, arc, slice and seven
original ledger rows. Iteration 01 is ready for CC. No files were staged or
committed by this review, and the source checkout remained clean.

## Findings

### R1 - Operator Tooling Requirement (Closure Blocker)

`artifacts/inventory_frontmatter.rb:1` introduces a Ruby helper. The operator
explicitly requires its replacement before any commit and prefers Fennel for
scripts, Rust/LFE for substantial tooling. Replace the helper with Fennel and an
established YAML parser; do not retain Ruby under another name or call it through
a wrapper. Regenerate evidence and remove the untracked Ruby source after the
replacement is verified. S1-8 records this newly explicit acceptance requirement.

### R2 - Incomplete Field Dispositions (Serious)

`artifacts/capability-crosswalk.md:6` provides 14 capability-group rows, not a
disposition for every discovered field. The raw JSON contains 169 distinct
top-level keys, plus nested fields. For example, `operator_acceptance`,
`runtime_write`, `numbering_basis`, `range_convention` and nested CQ coverage
assertions have no field-specific preservation/meaning analysis. Generic
"lifecycle" or "CQs" rows cannot demonstrate that these data survive.

Expand the crosswalk with a machine-checkable field-to-disposition index, typed
record context, nested paths, real examples and meaning/query consequences.
Distinguish an observed disposition from a proposed future requirement. Account
for metadata described in guides/references/prompts even where there is no
frontmatter block. This blocks S1-3/S1-4's completeness claims and S1-5/S1-6's
claimed coverage until their conclusions are reconciled to that inventory.

### R3 - Incorrect Population Summaries (Correctness-Grade)

`artifacts/metadata-inventory.md:51` says 31 parsed records use `record_type`
and 23 are cards. Its own JSON has **52 typed records, including 31 concept-card
records**. These totals include templates and synthetic examples, so they must
not be presented as counts of real extracted cards.

`artifacts/input-register.md` describes Arc07's 14 parsed records as candidate
cards. They are **10 concept cards and four source-support records**, plus two
README files without frontmatter. The 1,664 Erlang files cover the whole library;
the originally requested `design-scale-erlang-otp/` subset has **224** records.
The broader census is useful, but the book subset must remain identifiable.

Correct reports, ledger attestations and closing report consistently. Derive
summary counts from the inventory and separate corpus, record kind, fixture
versus real output, parse status and distinct concept identity.

### R4 - Reproduction And Input Traceability Gaps (Correctness-Grade)

`artifacts/validation-evidence.md:3` lists outcomes but omits the actual helper
invocation, dependency setup, working directory, field-union commands and checksum
normalization command. The input register abbreviates predecessor filenames and
does not pin the prose-only method inputs used for its semantic conclusions.
The JSON does hash the scanned Markdown, which is useful but does not cover every
claimed guide/prompt/preparation-handoff input.

Supply exact commands, tool/parser versions, dependency setup, exit statuses and
observed outputs. Register exact inspected prompt/guide/reference paths and
identities, including relevant document-extraction handoff material. Link
crosswalk assertions to concrete files/sections/values. Reproduction should not
require CDC to reconstruct the original command from `roots` in the JSON.

### R5 - Source Availability Needs Correction (Correctness-Grade)

The input register, validation report and CC closing report F-04 say
`/private/tmp/project05-compcogneuro-book-e0c697b4` is absent. During CDC review
it exists, is clean, resolves to the exact pinned commit
`e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`, and contains both named chapter files.
Update the availability record with actual commands and observation time.
Do not claim that this proves the source was available to CC at every earlier
instant; the current blanket absence statement is nevertheless inaccurate.
"Source support not re-verified in this slice" remains a valid, distinct limit.
This correction does not require a semantic source audit or a new extraction.

## Independently Reproduced Observations

- Enumerated all nine roots: 390, 1,664, 9, 7, 14, 13, 12, 9 and 6 Markdown
  files respectively, matching the JSON's 2,124 file census.
- Verified all 2,124 registered SHA-256 values against current files.
- Verified all 54 manifest entries (27 originals plus 27 copies). Two
  `diff -rq` comparisons independently confirmed byte-identical baseline trees.
- Recomputed from the submitted JSON: 2,106 reported parses, 15 missing
  frontmatter blocks, three reported errors, 52 typed records, 31 card records,
  169 top-level keys, Arc07's ten cards/four supports, and the 224-file book subset.
- Inspected the three reported failure headers: each contains an unquoted
  colon-space in `title`. Preserved copies were not repaired.
- Confirmed the live skill blob
  `33880bb84997e3eb00d6eba50e1a09ea9f33330e` matches CC's registration.
- Confirmed the source checkout is clean, planning HEAD is still `03c5b207`,
  and the planning index is empty. Tracked `git diff --check` passes.

The JSON recounts reproduce arithmetic over CC's output, **not independent YAML
parsing**. CDC did not execute Ruby. Fennel 1.6.1 on Lua 5.5 is installed;
`lyaml`, `yaml`, `cjson`, `dkjson` and `lfs` were not available through
the default `require` path during the probe. Dependency selection/setup and
fresh parsing remain part of Iteration 01. No graph traversal, semantic support,
operator acceptance or full prompt-to-field trace has been independently proved.

### Commands Used

Run from the source checkout; `slice_dir` below is a shell variable for brevity.

```sh
slice_dir=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions
jq -r '.roots[]' "$slice_dir/artifacts/frontmatter-inventory.json" |
  while IFS= read -r root; do
    printf '%s: ' "$root"
    find "$root" -type f -name '*.md' | wc -l
  done
jq -r '.records[] | "\(.sha256)  \(.path)"' "$slice_dir/artifacts/frontmatter-inventory.json" |
  shasum -a 256 -c -
shasum -a 256 -c "$slice_dir/artifacts/baseline-snapshots/source-sha256sums.txt" "$slice_dir/artifacts/baseline-snapshots/copy-sha256sums.txt"
diff -rq workbench/compcogneuro-rich-rerun-2026-09-12 "$slice_dir/artifacts/baseline-snapshots/compcogneuro-rich-rerun-2026-09-12"
diff -rq workbench/compcogneuro-teaching-rerun-2026-09-12 "$slice_dir/artifacts/baseline-snapshots/compcogneuro-teaching-rerun-2026-09-12"
jq '[.records[] | select(.values.record_type)] | group_by(.values.record_type) | map({type:.[0].values.record_type,count:length})' "$slice_dir/artifacts/frontmatter-inventory.json"
jq '[.records[].keys // []] | add | unique | length' "$slice_dir/artifacts/frontmatter-inventory.json"
git -C /private/tmp/project05-compcogneuro-book-e0c697b4 rev-parse HEAD
git -C /private/tmp/project05-compcogneuro-book-e0c697b4 status --short
git hash-object knowledge/concept-cards/SKILL.md
git -C .worktrees/planning diff --check
git -C .worktrees/planning diff --cached --name-only
git status --short
```

## Ledger Disposition

| Row | CDC result | Required next evidence |
| --- | --- | --- |
| S1-1 | Open; source blob/file hashes match, registration/availability incomplete | R4/R5 corrected register |
| S1-2 | Done, reproduced file preservation; still uncommitted | Retain the identical snapshots through replacement |
| S1-3 | Open; file census/hashes reproduced, parsing not rerun and summary incorrect | R1/R2/R3 fresh parsing and complete inventory |
| S1-4 | Open; exhaustive disposition claim not met | R2 field/nested-path coverage check |
| S1-5 | Open; useful direction, incomplete demonstrated coverage | R2/R4 evidence-specific body/metadata comparison |
| S1-6 | Open; sensible provisional agenda, refresh after complete crosswalk | R2/R3/R5 research-agenda reconciliation |
| S1-7 | Open; source/index clean, reproduction instructions incomplete | R1/R4 and revised close packet |
| S1-8 | Open; new operator condition | Fennel replacement, no Ruby source and no commit |

## Bubble-Up Check

Useful baseline preservation and initial findings are retained. The inventory
and no-loss crosswalk are not complete enough to discharge the original slice
scope. R1 adds an operator tooling condition; R2-R5 correct existing deliverables.
The arc plan now records Iteration 01 and keeps Slice02 unopened. No new arc,
schema selection, source implementation or reduced requirement is warranted.
The CC report remains its original attestation pending a revised submission.
