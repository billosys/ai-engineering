# CDC Review: Arc01 Slice01

Date: 2026-09-12. Current status: **Iteration 03 required; not closed**.
Iteration 01 was committed as `e2ea1e68` with operator permission after a
no-Ruby inspection. The current independent review is appended below; the
initial review is retained as history.

## Initial Review (Historical)

Status at initial review: **changes required; not independently closed**.
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

## Iteration 01 Independent Review

Reviewed commit `e2ea1e68` on 2026-09-12. Planning and source checkouts were
clean on entry. The operator explicitly released the earlier commit hold;
the report's repeated "uncommitted" wording is historical, not live Git state.
Project06 commit `1a385435` is separate and was not altered.

### What Reproduced

- No Ruby source was found in the Project08 commit tree or the replacement helper.
  The implementation uses Fennel with an embedded Perl/YAML::XS bridge.
- YAML::XS 0.82 and JSON::PP 4.06 load in the local environment.
- Two full nine-root helper runs succeeded and were byte-identical to each other
  and the committed inventory.
- The existing malformed, empty, nonmapping, unterminated and missing-root cases
  return reported errors rather than crashing.
- All 54 baseline checksum entries match (27 originals and 27 copies).
- The corrected population counts and exact CompCogNeuro pin from the previous
  review remain useful evidence; none establishes semantic source verification.

These improvements resolve Ruby removal and demonstrate determinism. They do
not yet establish lossless parsing or a complete semantic inventory.

### R6 - Parser Bridge Loses Types (Serious)

At `artifacts/inventory-frontmatter.fnl:28`, YAML values pass through default
Perl scalars before JSON serialization. The existing valid fixture's
`nested.value: true` becomes JSON number `1`. The independent reviewer fixture
`artifacts/cdc-type-probes/types.md` additionally demonstrates:

| YAML input | Actual JSON | Required distinction |
| --- | --- | --- |
| `truth: true` | `"truth": 1` | Boolean versus integer |
| `falsehood: false` | `"falsehood": ""` | Boolean versus empty string |
| `one: 1` | `"one": 1` | Must not collide with true |
| `empty_text: ""` | `"empty_text": ""` | Must not collide with false |

All non-null scalar shapes become `scalar`, losing the previous distinction
among strings, numbers and booleans. Sequence shapes are JSON-encoded strings
inside the shape array, rather than structured shape objects. This is a
substantive failure of the slice's value/shape preservation requirement.
Recording the parser difference does not make this lossy transformation pass.

The comments also overstate the Fennel ownership: embedded Perl reads files,
hashes them, frames frontmatter, walks shapes and builds record JSON; the Fennel
`closing-frontmatter` helper is unused. Keep interoperability with the established
parser, but implement inventory/report logic in Fennel as the accepted plan says.
Resolve typing at the parser boundary, with assertions rather than guessed repair.

### R7 - Null/Empty Field Paths Omitted (Serious)

The 307-entry index is not a complete enumeration. An independent walk over
every object-key path (including keys inside sequence elements) finds 300 unique
paths. Thirty of those are absent from the submitted index, which additionally
contains some array-element paths. Those two populations are not interchangeable.

Missing examples include `coverage_assertions.0.id`,
`coverage_assertions.0.revision`, `coverage_assertions.0.covered_refs`,
`endpoint_roles.from_role`, `operator_acceptance.required`,
`source_spans.0.source_ref` and `worker_scope.roles`.
They are observed null/empty fields, precisely the cases the requirement says
must remain distinguishable from absence. Per-field context counts also need
regeneration so null-valued template occurrences are represented.

### R2 - Semantic Crosswalk Still Unfinished (Serious)

All 307 entries have the exact same `semantic_disposition`:
"inventory-observed; Arc02 must make an explicit retain/rename/relocate/weaken/absent
decision for this exact path". Their `query_migration_implication` strings are
also all identical. The readable crosswalk remains the same 14 broad group rows.
This is an index of future work, not the required field-specific assessment of
observed meaning, retention and lookup consequences. Future schema selection
remains Arc02, but it does not own the unfinished Slice01 comparison.

### R4/R5 - Reproduction And Reporting Still Incomplete

`artifacts/validation-evidence.md:10` contains `<the nine roots from
input-register.md>` rather than an executable command, and no repeatable
field-index generation route is recorded. The input register still abbreviates
predecessor and guide names and omits their identities.

The validation report still calls the source snapshot unavailable, contradicting
the corrected input register. The CC closing report's artifact inventory still
lists the removed Ruby file and "27 files in each" tree, and its row walk has
seven rows despite eight ledger rows. These old statements are not clearly
marked superseded; adding a correction paragraph has not reconciled the report.

### Reproduction Commands

Run from the source checkout in Bash. These commands reconstruct the census
arguments from the pinned submitted JSON for this review; CC must still deliver
a self-contained recipe and an index-generation/check route.

```sh
slice_dir=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions
review_dir=$(mktemp -d /private/tmp/project08-cdc-i01.XXXXXX)
set --
while IFS= read -r root; do
  set -- "$@" "$root"
done < <(jq -r '.roots[]' "$slice_dir/artifacts/frontmatter-inventory.json")
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" "$review_dir/run1.json" "$@"
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" "$review_dir/run2.json" "$@"
cmp "$review_dir/run1.json" "$review_dir/run2.json"
cmp "$review_dir/run1.json" "$slice_dir/artifacts/frontmatter-inventory.json"
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" "$review_dir/types.json" "$slice_dir/artifacts/cdc-type-probes"
jq '.records[0] | {values,shapes}' "$review_dir/types.json"
jq '[.field_paths[].semantic_disposition] | group_by(.) | map({text:.[0],count:length})' "$slice_dir/artifacts/field-dispositions.json"
jq --slurpfile index "$slice_dir/artifacts/field-dispositions.json" '[.records[] | .values // {} | paths | select(.[-1]|type=="string") | map(tostring) | join(".")] | unique as $observed | ($index[0].field_paths|map(.field_path)|unique) as $indexed | {observed:($observed|length),indexed:($indexed|length),missing:($observed-$indexed)}' "$review_dir/run1.json"
```

The temporary type fixture was subsequently preserved byte-for-byte in
`artifacts/cdc-type-probes/types.md`; no source card or captured baseline changed.
The 300/307 figures use the submitted concrete-index notation. A documented
normalization is acceptable on correction; dropping empty/false/null paths is not.

### Row Walk And Bubble-Up

S1-2 remains reproduced. S1-1, S1-3 through S1-7 require the input/report,
type-preservation and semantic/path-coverage corrections above. S1-8's no-Ruby
and operator-authorized commit requirements are satisfied, while the specified
Fennel ownership of inventory logic still needs the R6 correction.

Iteration 02 is required within this slice. Project/arc/slice plans and the
current prompt have been updated accordingly. Slice02 remains unopened. No
schema choice, semantic verification, source-skill change, or quality requirement
was deferred by this review. The operator's commit authorization is honored;
formal CDC acceptance remains based on the outstanding evidence.

## Iteration 02 Independent Review

Reviewed `e554d74c`. Source is clean. Earlier CDC/project-plan changes remain
uncommitted and were preserved by CC. No Ruby source was reintroduced.

### Resolved And Reproduced

- Full nine-root census completed successfully and was byte-identical to the
  committed inventory: 2,124 files, 2,106 parsed mappings and the existing
  population totals.
- The independent type fixture now retains true/false, numbers, quoted numeric
  strings, nulls, empty strings/containers, and structured nested shapes.
- An independent normalized walk of the parsed inventory and comparison with
  the committed field index found **308 expected paths, 308 actual paths,
  zero missing and zero extraneous**. Null/empty paths omitted previously are
  now included. This resolves the original R7 completeness defect.
- A fresh helper-generated index equals the committed index after removing the
  three semantic annotation columns. The mechanical generation is reproducible.
- All 54 baseline checksum entries pass. Earlier baseline data remains intact.

The original boolean/scalar-type and path-omission defects in R6/R7 are resolved.
The remaining findings below are distinct from those verified improvements.

### R8 - Custom JSON Codec Emits Invalid JSON (Serious)

`artifacts/inventory-frontmatter.fnl:30` escapes quotes, backslashes, newline,
carriage return and tab, but not other JSON control characters. The helper exits
0 on a valid YAML string `text: "page\fbreak"`, then writes a literal form-feed
byte into JSON. `jq` rejects its output with exit 4:
`Invalid string: control characters from U+0000 through U+001F must be escaped`.

Reviewer input is preserved at `artifacts/cdc-edge-probes/json-controls.md`.
This defect warrants replacing the hand-written JSON codec with an established
implementation, keeping explicit null/array/boolean distinctions and the Fennel
inventory logic. The narrow YAML parser bridge remains acceptable.

### R9 - Empty/Null Frontmatter Misclassified (Correctness-Grade)

The existing `inventory-fixtures/empty.md` has both delimiters, yet the new
framing function reports `unterminated-frontmatter`. A separately probed
`--- / null / ---` document becomes `frontmatter: true`, `keys: []`,
`values: null`: the internal null-marker table passes the root mapping check.
Empty content, null document, valid empty mapping, nonmapping sequence and
unterminated content need correct distinct handling.

The null-root and empty-mapping probes are preserved alongside the JSON probe.
The null-root observation was inspected after replacing the unrelated literal
form-feed byte with a space solely in a display pipeline; no generated or
source file was repaired. R8 still records the original invalid output.

### R2 - Semantic Work Still Incomplete

The updated index adds specific meanings for some paths, but 109 entries still
use the generic "records the observed metadata component named by this exact
path and context" description. One hundred dispositions still instruct Arc02
to decide rather than record the observed comparison. The query/migration text
is the same generic sentence with only the field path substituted.

There are also specific incorrect or unsupported classifications:

- `actor.id` is described as identifying a local record or nested assertion;
  it identifies the performer recorded alongside role and operating mode.
- `source_refs[].id` is given the same local-record description instead of
  identifying the referenced source.
- `aliases` is labeled weakened without demonstrating loss; it is visibly
  retained in the current template and legacy cards. Any narrower failure needs
  actual evidence and its scope.

Local anchors include `knowledge/concept-cards/templates/concept-card.md:7`,
`:10`, `:12` and the entrypoint's reference-identity convention. The index
must be a meaningful semantic comparison, not suffix-based descriptions.
An explicitly mapped semantic-family analysis can reduce repetition while
preserving complete field/context accountability. Future schema selection
remains Arc02; the unfinished observed comparison belongs to this slice.

### R4 - Documented Coverage Check Does Not Run

The coverage command in `artifacts/validation-evidence.md` reads
`.records[]` from `field-dispositions.json`, which contains no records.
Executing it verbatim exits **5**, `Cannot iterate over null (null)`.
Its numeric-path normalization also differs from the committed `[]` notation.

The corrected independent command below passes, but that does not validate the
documented recipe. The recipe also uses `mapfile` without specifying a suitable
shell; the local `/bin/bash` is 3.2. The input register still contains
abbreviated prose inputs and the obsolete parser description. Exact guide/
prompt identities and the mechanical-to-semantic annotation workflow remain
unrecorded. Update and execute the documented route literally.

### Independent Commands And Evidence

Commands run from the source checkout; `slice_dir` is the Slice01 path used
in earlier review commands. The run artifacts were under
`/private/tmp/project08-cdc-i02.02u7xj`. Probes created there were later
preserved byte-for-byte in `artifacts/cdc-edge-probes/`.

```sh
review_dir=/private/tmp/project08-cdc-i02.02u7xj
set --
while IFS= read -r root; do
  set -- "$@" "$root"
done < <(jq -r '.roots[]' "$slice_dir/artifacts/frontmatter-inventory.json")
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" --field-index "$review_dir/index.json" "$review_dir/census.json" "$@"
cmp "$review_dir/census.json" "$slice_dir/artifacts/frontmatter-inventory.json"
jq --slurpfile index "$slice_dir/artifacts/field-dispositions.json" '[.records[]|select(.frontmatter)|.values|paths|map(if type=="number" then "[]" else . end)|join(".")|gsub("\\.\\[\\]";"[]")]|unique as $expected|($index[0].field_paths|map(.field_path)|unique) as $actual|{expected:($expected|length),actual:($actual|length),missing:($expected-$actual),extraneous:($actual-$expected)}' "$review_dir/census.json"
jq -n --slurpfile actual "$review_dir/index.json" --slurpfile committed "$slice_dir/artifacts/field-dispositions.json" '($committed[0].field_paths|map(del(.observed_meaning,.observed_disposition,.query_migration_implication))) == $actual[0].field_paths'
fennel "$slice_dir/artifacts/inventory-frontmatter.fnl" --field-index "$review_dir/edge-index.json" "$review_dir/edge.json" "$slice_dir/artifacts/cdc-edge-probes"
jq . "$review_dir/edge.json"
```

The last command fails as described in R8; this is intentional negative
evidence, not a passed gate. Existing fixture output also exposes R9.

### Current Row Walk And Bubble-Up

S1-2 and S1-8 are reproduced: baseline preservation and approved Fennel/parser
tooling are retained, and the prior hold was released. S1-3 has substantial
reproduced census/type/path evidence but remains open for R8/R9. S1-1 and S1-7
remain open for R4. S1-4 through S1-6 remain open until R2's semantic analysis
and derived research handoff are complete.

Iteration 03 is prepared within the current slice; Slice02 remains unopened.
No requirement is dropped or transferred to later design. The five-iteration
limit remains a sizing signal: expose actual unreviewed semantic families and
propose a bounded split if necessary, rather than mark generic text complete.
