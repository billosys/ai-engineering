# CC Iteration 04: Authored Semantics And Literal Reproduction

Use a fresh CC context. Read Project08 AGENTS.md, project/arc/slice plans and
ledgers, the latest appended CDC review and current artifacts. Starting repair
commit: `b5ed9dd1`. This remains Arc01 Slice01; Slice02 is not open.

The focused control-character and empty/null classification probes pass.
The original typed-values/shapes and path-coverage corrections are valuable
baseline evidence. **Primary work now is the authored semantic analysis and
its reproducible handoff.** Do not substitute another helper-only repair for
R2/R4. CC's explicit unfinished-work report is retained and respected.

## 1. Size And Author The Semantic Work

Start by grouping the observed fields into families according to actual meaning,
not suffix. Inspect the full v3.2 extraction/re-extraction prompts, the actual
historical/current records and the current definition guides/references.

Useful starting groups include concept identity/labels; classification and
pedagogical progression; bibliographic identity; source snapshot/representation;
locators/spans; claims/support; evidence/confidence; relationship endpoints and
predicates; competency questions and coverage assertions; run/actor/worker
provenance; validation/verification; reconciliation; preservation; admission/
operator acceptance. Split groups wherever subject or authority differs.
These are prompts for judgment, not an accepted taxonomy or fixed group count.

Write `artifacts/semantic-families.md` and an explicit
`artifacts/semantic-membership.json`. Each authored family needs:

- A stable family ID and a concrete definition of the information it carries.
- Exact local definition paths/sections and representative value examples.
- Enumerated field-path/record-context membership, including null/empty cases.
- Legacy and current representations, or an explicit current-only distinction.
- Observed preservation, rename, relocation, weakening, absence, ambiguity or
  intentional change, with evidence rather than a future decision placeholder.
- A concrete consequence for lookup, provenance, migration or source review.
- Open research questions kept separate from observations and future design.

Correct the known misleading examples: actor identity identifies the performer;
source reference identity identifies the referenced source; assertion identity
identifies an assertion. Do not group them merely because they end in `.id`.
Do not label aliases weakened without an actual supported difference. Fields
with the same spelling but different record scope require contextual analysis.

Use a deterministic Fennel join/check route to combine the mechanical census
with the authored family map into the existing `field-dispositions.json`.
Keep narrative analysis authored; do not regenerate it from key-name heuristics.
Check coverage against every observed normalized path and its relevant record
contexts, not merely presence of 308 non-empty strings. Every membership must
resolve to an authored family and a cited meaning; report uncovered contexts,
unmatched memberships, ambiguous overlaps and unsupported dispositions.

Read actual sources while writing. Starting local references include
`knowledge/concept-cards/references/record-field-groups.md`,
`knowledge/concept-cards/references/vocabulary.md`,
`knowledge/concept-cards/guides/01-load-contract.md` and the operation-specific
guides/templates, plus `knowledge/document-extraction/guides/03-output-contract.md`
and `knowledge/document-extraction/guides/09-locator-model.md`. Register the
actual inspected set; these examples are neither an exhaustive list nor a
claim that every listed file supplies every field definition.

## 2. Complete R4 As A Literal Replay

Write a complete command sequence that runs under macOS `/bin/bash` 3.2,
or explicitly name and verify another shell. Include all nine roots literally;
no `mapfile`, ellipses or placeholder roots in a Bash 3.2 recipe. Use separate
inputs for inventory and field-index comparisons. Normalize `items[].id`
consistently, including array containers and null/false/empty fields.

Include dependency/version probes, census generation, semantic join/check,
fixtures with asserted expected outcomes, independent path/context coverage,
baseline checksums and whitespace/worktree checks. Run the recipe exactly as
written with fail-fast behavior; preserve actual outputs and exit statuses in
`artifacts/validation-evidence.md`. Identify its source/planning commit bases.

Update `input-register.md` with exact inspected guide/prompt paths and
revision/hash identities. Replace abbreviated predecessor filenames and the
obsolete parser description. Refresh the crosswalk and research agenda from
the authored findings, without choosing the Arc02 schema.

## 3. Resolve The Remaining Instruction Dispositions

The focused patch fixes the exhibited R8/R9 cases but retains the hand-written
JSON codec and a framing pattern requiring a newline after the closing
delimiter. Iteration 03 requested an established JSON implementation and
closing-at-EOF handling. These are still recorded instructions, not newly
introduced requirements.

Resolve them using proven dependencies and bounded regression assertions, or
report a concrete alternative for CDC to assess with evidence and tradeoffs.
Do not mark them fulfilled merely because the existing focused probes pass.
Preserve null/container/boolean distinctions and Fennel ownership of inventory
logic. No Ruby or Python wrapper. Avoid additional unrelated parser features.

## Completion, Sizing And Commit

This is iteration four of the existing slice, not the fourth project trial.
Size the semantic-family work at the start. If it cannot fit one fresh context
with review headroom, identify the specific remaining families/rows and propose
bounded slices for the arc; keep unfinished rows open. Do not transfer them
silently to Arc02 or declare partial analysis complete. The project has room
for additional slices, and every original requirement still needs an owner.

Edit only this slice's authored artifacts, necessary Fennel helpers/fixtures,
ledger and CC closing report. Preserve reviewer records and baseline copies.
No source-skill, corpus, package or unrelated project changes. List every
delivered file in the close packet.

Walk all eight ledger rows with exact evidence. Clearly label old all-done
tables as historical; the current report must agree with current open/done
rows. Report R2/R4 and instruction dispositions separately from previously
verified fixes. Passing a parser check is not a semantic review.

Commit explicitly enumerated corrected slice files only, with both repository
co-author trailers. Preserve unrelated staged edits and prior commits.
Return the commit, reproducible findings, remaining gaps and honest proposed
status. Independent CDC verification and formal slice closure remain pending.
