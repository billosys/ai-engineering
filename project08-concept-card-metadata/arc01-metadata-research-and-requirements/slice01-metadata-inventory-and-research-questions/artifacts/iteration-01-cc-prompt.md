# CC Iteration 01: Complete And Reproduce The Metadata Inventory

Read the Project08 AGENTS.md and project/arc plans, then this slice's
`slice-plan.md`, `ledger.md`, `cdc-verification.md` and current artifacts.
This is a follow-up within Arc01 Slice01, not Slice02. All original outcomes
remain required; the ledger now has eight rows.

**Do not stage or commit any files.** The operator suspended the initial commit
instruction. Leave the corrected packet for CDC review. No Ruby script is to
enter Git history. Use Fennel for scripting; use Rust/LFE only if the work grows
into substantial tooling. Do not substitute Python.

## Scope

Change only this slice's implementation/evidence artifacts, its ledger and
CC closing report. The CDC report and project/arc plans are review inputs.
The source checkout, old prompts, external corpora and captured baseline bytes
remain read-only. Preserve unrelated work.

## Required Corrections

1. **R1: replace the helper.** Implement `artifacts/inventory-frontmatter.fnl`
   using a proven YAML parser with documented dependency/version/setup. Fennel
   must own the reporting logic; do not wrap or embed Ruby/Python. Fennel is
   installed, but default Lua imports did not expose YAML/JSON/filesystem
   libraries during CDC review. Resolve dependencies deliberately and locally;
   do not write a regex/ad hoc YAML parser or silently require an unavailable
   library. Native/parser interoperability is acceptable with explicit setup.
   Do not install globally or modify unrelated runtime configuration.
2. Preserve inventory semantics: all input paths/hashes, parsed values, nested
   shapes, missing versus null versus empty structures, and visible parse errors.
   Compare the old JSON to fresh output semantically; byte-identical Ruby error
   strings, Ruby class names and JSON whitespace are not required. Explain any
   parser/dialect changes, including boolean/date/null handling. Do not preserve
   a mistaken count merely for parity. Keep canonical ordering deterministic.
   Verify malformed/non-mapping/empty/unterminated frontmatter and missing roots
   are reported explicitly rather than crashing or silently shrinking coverage.
   Add focused fixtures where needed to protect these distinctions.
3. After validating the replacement, delete the untracked
   `artifacts/inventory_frontmatter.rb`. Retain no renamed/embedded Ruby source.
   Regenerate `frontmatter-inventory.json` and update the reports to the actual
   helper and parser. Historical prose may honestly say the initial draft used
   Ruby; do not falsify provenance or leave Ruby as the active reproduction route.
4. **R2: complete the crosswalk.** Account for every discovered top-level and
   nested field in its record context; the submitted JSON currently has 169
   distinct top-level names. Add `artifacts/field-dispositions.json` as a
   machine-checkable index linked to the readable crosswalk. Include field path,
   applicable record/corpus, observed shapes/presence, concrete evidence and
   semantic disposition plus query/migration implications. Shared entries are
   fine only when explicit mappings and meaning establish that they apply.
   Check for uncovered field paths mechanically; do not use catch-all
   "lifecycle"/"provenance" dispositions to conceal missing analysis.
   Inspect prose-only field definitions in prompts, guides and references,
   including the relevant document-extraction handoff. Register discoveries
   separately from frontmatter parsing. Final schema selection remains Arc02.
5. **R3: correct the summaries.** The submitted JSON has 52 typed records,
   including 31 concept-card records (templates/examples included). Arc07 has
   ten cards and four supports. Distinguish the 224-card
   `design-scale-erlang-otp/` subset from the useful wider 1,664-file Erlang
   census. Derive each report total from fresh inventory and identify its exact
   population. Reconcile inventory, input register, crosswalk, ledger and close
   report; fix "checked-in" wording for this uncommitted packet and the claim
   of 27 files in each baseline tree (14 rich plus 13 teaching, 27 total).
6. **R4: make reproduction self-contained.** Record exact commands and working
   directories for setup, inventory generation, summary/field coverage checks,
   baseline comparison, and hygiene. Include actual tool versions, exit statuses
   and outputs. Give exact paths and revision/hash identities for all inspected
   prompts, guides, references and handoff inputs. Attach file/section/value
   evidence to semantic conclusions and old/new body comparisons. Do not infer
   that all prose files were semantically inventoried because a parser reported
   "no frontmatter".
7. **R5: refresh availability.** CDC found the supposedly absent checkout clean
   at `/private/tmp/project05-compcogneuro-book-e0c697b4`, with HEAD
   `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` and both chapter files present.
   Check again, timestamp the observation and reconcile all absence claims.
   Preserve "not semantically re-verified" as a separate scope statement.
   Do not expand this correction into extraction or claim verification.

## Verification And Return

Run the Fennel inventory twice to demonstrate deterministic output on unchanged
inputs. Check every declared root, parsed/file/record-kind totals, nested field
disposition coverage, representative source-to-crosswalk traces and all baseline
hashes. Preserve the three malformed historical cards unchanged; parsing failures
are valuable fixtures, not permission to repair captured evidence.

Check whitespace on both tracked changes and new authored files: ordinary
`git diff --check` does not inspect untracked content. Separate pre-existing
formatting in byte-preserved baseline copies from new authored defects. Verify
there is no Ruby source among deliverables, the index remains empty, the
planning HEAD has not advanced, and source status is unchanged. Inspect script
contents as well as extensions. No package gates are needed for this slice.

Update the ledger and `closing-report.md` as revised CC proposed-done, with an
Iteration 01 section addressing R1-R5 and S1-8. Retain the prior review history,
name what changed, record remaining gaps, and bubble research implications into
the handoff without declaring the arc/project closed. Do not edit CDC's report.
List every new helper/fixture/index in the artifact inventory. Report that the
packet remains uncommitted and independent CDC verification is pending.
