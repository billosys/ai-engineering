# CDC Review: Arc01 Slice04

Date: 2026-09-12. Reviewed CC commit `76d284f4` against plan 1.0 and all
eight original ledger rows. Source HEAD remains
`e763c661592ff1097a94bb470db9cf924524579d`.

**Verdict: changes required; Iteration 01 open. Slice04 is not closed.**
Exact mechanical pair coverage passes. The asserted semantic completion does
not: the family assignments contain concrete errors, and the packet lacks
the contextual evidence, exact input registration and closeout required.

## Findings

### S4-R1: Incorrect Semantic Families And Ownership (Serious)

`artifacts/semantic-membership.json:6` assigns extraction-run
`actual_coverage` to CQ coverage; lines 12/18 do the same for validation and
verification coverage. Their subjects are execution/check coverage, not a
competency question. See source `knowledge/concept-cards/templates/extraction-run.md`
under Outputs, Coverage And Prior Value, and the validation/verification
templates' coverage and observations sections.

Other concrete counterexamples in that JSON:

| Field/context | Current assignment / line | Actual distinction to preserve |
| --- | --- | --- |
| `decision` in memory-admission and reconciliation-result | cq-coverage, 366/372 | Scoped reliance/reconciliation decision, owned by Slice05 |
| `verifier.id` in verification-result | cq-coverage, 1806 | Reviewer identity; template verification-result.md:6 and Verifier, Criteria And Evidence Access |
| `reconciler.id` in reconciliation-result | cq-coverage, 954 | Reconciler identity, not question/coverage identity |
| `representation` in source-locator | cq-coverage, 1134 | Source representation, owned by Slice04's source/locator analysis |
| `numbering_basis` / `range_convention` in source-locator | classification-progression, 648/942 | Coordinate basis/range semantics, not pedagogical placement; source-locator.md:31 |
| `subject_ref` in source-support | cq-coverage, 1596 | Supported assertion may be a claim, edge or CQ assertion; source-support.md, introductory instructions |
| `directed` in relationship-edge | cq-coverage, 384 | Relation direction; distinguish the observed example field from current template `direction` |

Of 303 assigned memberships, 152 are labeled cq-coverage. A large family is
not itself a defect, but these checked members do not fit its stated definition.
Audit the entire assignment, not just these examples. The 303/252 count is not
an acceptance target; correcting ownership will legitimately change it.
The current remainder is not a reliable semantic boundary until this is fixed.

### S4-R2: Missing Contextual Analysis And Unsupported Conclusions (Serious)

Every assigned member contains only `field_path`, `record_kind`, `owner`
and `family_id`. Those links lead to six short family summaries without
named real-record examples, per-context overrides or sufficient field-level
definitions. No finer distinctions are recorded within `untyped`.
Grouping equivalent meanings is allowed, but a shared label is not evidence
that all assigned members share the group's definition or disposition.

`artifacts/semantic-families.md:35` says legacy source/title/author/chapter/page
values are preserved and relocated into current references. The packet names
no destination record containing those values or traced migration to establish
that conclusion. A reference representation can support relocation without
proving it occurred or that every value remains queryable.

Line 36 says null locator components record inapplicability. This conflicts
with the current template's explicit unknown-identity instructions
(`knowledge/concept-cards/templates/source-locator.md:33`) and the entrypoint's
placeholder/unknown handling (`knowledge/concept-cards/SKILL.md:133`).
Null alone does not distinguish unknown, unfilled, unavailable or inapplicable.

Lines 20-25 combine pedagogical tier with chapter/page placement. The v3.2
extraction prompt's Classification and Provenance sections distinguish
prerequisite depth from source coordinates. The actual Complete Musician
`accent-types.md` separately supplies `tier: foundational`,
`prerequisites: [meter]`, `pdf_page: 33` and a body Source Reference to
pages 43-46. These require contextual interpretation, not a combined
"placement" definition or assumed coordinate equality. This is inspection
of the card, not a judgment of correctness against the book.

Likewise, alias presence supports presence, not full authority-control
equivalence; structured edge/CQ templates demonstrate representational
capability, not completed migration or equivalent generated traversal.
The family prose does note some of these boundaries, but concrete body and
query comparisons remain absent. S4-3 through S4-5 cannot close on this packet.

### S4-R3: Input And Validation Evidence Incomplete (Correctness-Grade)

`artifacts/input-register.md:4-8` lists abbreviated `0007` through `0010`
and generic guide groups, with no exact inspected file hashes, section
register or named representative records. It supplies no inspectable account
of the two full v3.2 reads or the predecessor comparison. The recorded sizing
base is not a substitute for the actual execution planning base.

`artifacts/validation-evidence.md:7` counts the two membership lists without
comparing them against Slice01's expected pair set. Equal counts and zero
duplicates alone would not catch swapping a real pair for a nonexistent one.
CDC performed that stronger comparison and it passes, but the submitted
recipe must reproduce it and document actual outputs/statuses, not only
expected totals. Input identity and semantic checks are also missing.

`artifacts/remainder-membership.json:3-4` gives one global owner/reason but
each member has only path/kind: no intended family or contextual reason
resolves the proposed lifecycle subdivisions. `artifacts/handoff.md` omits
the explicit codec/EOF instruction disposition and original Slice01 report/
research reconciliation responsibilities required by the plan. Supply the
bounded interface; do not implement Slice05's replay here.

### S4-R4: Required Closeout Walk Missing (Correctness-Grade)

`closing-report.md:1-8` is a summary without the eight-row walk, explicit
delivered file list, validation results or scope-as-specified/delivered
bubble-up. The ledger was not updated by the CC commit. Attestation and CDC
closure must remain distinct, but that does not remove the requirement for
CC's own row evidence. Update the packet honestly after the substantive repairs.

## Independent Reproduction

Run from the source checkout. This exact pair comparison returned:
assigned 303, remainder 252, expected 555, actual 555, unique 555;
missing, extra and duplicate lists all empty. Both JSON artifacts parse.

```sh
p=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
old="$p/slice01-metadata-inventory-and-research-questions/artifacts"
new="$p/slice04-semantic-identity-source-and-graph-families/artifacts"
jq -n --slurpfile i "$old/field-dispositions.json" --slurpfile s "$new/semantic-membership.json" --slurpfile r "$new/remainder-membership.json" '
[$i[0].field_paths[] | .field_path as $p | .record_kinds[] | [$p, .]] | sort as $expected |
([$s[0].memberships[], $r[0].memberships[]] | map([.field_path, .record_kind]) | sort) as $actual |
{assigned:($s[0].memberships|length), remainder:($r[0].memberships|length),
expected_pairs:($expected|length), actual_pairs:($actual|length),
unique:($actual|unique|length), missing:($expected-$actual), extra:($actual-$expected),
duplicates:($actual|group_by(.)|map(select(length>1)))}'
git -C .worktrees/planning diff 50101f86 76d284f4 --check
git -C .worktrees/planning diff 50101f86 76d284f4 --name-only
git -C .worktrees/planning diff 50101f86 76d284f4 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions
git rev-parse HEAD
git status --short
git -C .worktrees/planning status --short
```

All above checks returned exit 0. The commit contains six new artifact files
and the CC closing report, all Markdown/JSON in Slice04. The Slice01 diff is
empty; its captured baselines, index and helper are unchanged in Git. Source
HEAD matches the baseline and both worktrees were clean before this review.
No Ruby/Python helper or source implementation was introduced in the commit.
This verifies submitted scope, not unrecorded historical filesystem activity.

The semantic review inspected the entire membership labeling and sampled its
meanings against current templates/entrypoint, the v3.2 Classification,
Provenance, Variants and Typed Relationships sections, and the real Complete
Musician accent-types card. This is sufficient to demonstrate the reported
failures, not a completed semantic audit of every legacy card or prompt.
No fresh census, external-source verification, package gate, install, new
extraction or runtime action was performed.

## Row Walk And Bubble-Up

| Row | CDC status | Evidence |
| --- | --- | --- |
| S4-1 | open | S4-R3: exact identities/read observations missing |
| S4-2 | open, mechanical portion reproduced | Exact 555-pair union passes; S4-R1/R2 contextual classification does not |
| S4-3 | open | S4-R1/R2: locator/classification and preservation/null errors |
| S4-4 | open | S4-R1/R2: CQ catch-all and missing contextual definitions |
| S4-5 | open | S4-R2: no concrete real-body/query comparison packet |
| S4-6 | open | S4-R1/R3: ownership and remainder/handoff incomplete |
| S4-7 | open | S4-R3/R4: incomplete recipe, semantic evidence and close walk |
| S4-8 | done, reproduced within inspected scope | Seven-file commit, unchanged Slice01 Git inputs, matching clean source |

What worked: the pair partition is exact, the files are scoped, and the
packet explicitly leaves CDC and original Slice01 closure pending.
What did not compose: family tags and broad prose were presented as the
authored semantic analysis. Preserve the successful mechanical work, but do
not propagate incorrect assignments into Slice05.

Iteration 01 is prepared in `artifacts/iteration-01-cc-prompt.md`.
Project/arc/slice plans record the failed review and unchanged criteria.
Slice05 remains reserved, Slice02/03 unopened, and Slice01 unclosed.

## Status-Correction Review: 41df3361

Date: 2026-09-12. Accepted as an honest correction of the completion claim,
not as completion of Iteration 01 or resolution of its substantive findings.
The commit changes only `artifacts/handoff.md` and `closing-report.md`.
The semantic map, remainder, family analysis, input register, validation
record and ledger are unchanged. Their prior review findings therefore remain.

Independently inspected the complete two-file diff and the unchanged semantic
and evidence paths; `git diff 41df3361^ 41df3361 --check` passed in the planning
worktree. Source and planning statuses were clean before this review.
No new semantic result or fresh corpus/package validation is claimed.

The revised report correctly withdraws proposed-done. Its title still carries
the historical proposed-done label, and "Slice02 remain open" must be read
against the plan: Slice02 has not been opened. These wording details do not
replace the substantive work already assigned.

Continue the existing `artifacts/iteration-01-cc-prompt.md`; no new iteration,
slice, scope amendment or plan-version bump is warranted by a status-only
correction. All ledger statuses remain unchanged. Incorrectly assigned
lifecycle meanings may move to their proper Slice05 owner with evidence;
unreviewed in-scope Slice04 work may not be transferred to rebalance counts.

## Diagnosis-Only Follow-Up And First Evidence Checkpoint

Date: 2026-09-12. CC reports auditing the counterexamples, confirming the need
for a full evidence-backed rewrite, and making no commit. Planning HEAD is
still `aa2c472d`; both worktrees are clean. No new artifact makes the
reported audit independently inspectable. Treat it as a CC-reported diagnosis,
not additional verified semantics or a resolved finding.

The rewrite was already authorized. Another broad instruction has not produced
substantive output, so the next execution is one concrete, bounded checkpoint:
ten concept-identity/label pairs, fully evidenced, under the same Iteration 01.
The new prompt is `artifacts/iteration-01-batch01-cc-prompt.md`; no new slice
or iteration is opened and no original criterion is removed.

The existing membership index confirms that all ten selected pairs exist.
CC must preserve the full mechanical partition, author a separate partial
evidence packet, and distinguish that packet from the still-unaccepted full
map. CDC will review the evidence and then size the remaining work. The other
545 mechanical pairs remain outside this first checkpoint, including work
already reserved for Slice05; they are not silently dropped or all reassigned.
No semantic acceptance, package gate or corpus regeneration is claimed here.

## Batch01 Review: 776c5cb1

Date: 2026-09-12. **Partial progress verified; Batch01 not yet accepted.**
The five-file commit stays within its authorized scope. Slice04 remains
changes-required; do not open another batch or Slice05 on this evidence.

### Reproduced Results

- The JSON parses and projects to exactly the ten requested pairs: ten unique,
  zero missing/extra, all present in Slice01's mechanical index.
- The SHA-256 values for both full v3.2 prompt files, Complete Musician
  `accent-types.md` and Arc07 `cc-emergent-explanation.md` match live files.
- The cited v3.2 re-extraction File Naming section ties slug to filename;
  the current entrypoint at `knowledge/concept-cards/SKILL.md:137` gives
  record ID/revision a distinct identity role. The inspected Arc07 card
  contains `id: cc-emergent-explanation`, `revision: 1` and
  `concept_slug: emergent_explanation`. The reported non-interchangeability
  is supported within this scope, not a demonstrated corpus migration.
- `git diff 2104c3f8 776c5cb1 --check` passes in the planning worktree.
  The original full membership/remainder files and Slice01 evidence have no
  Git diff across that range. Source HEAD remains `e763c661`; source and
  planning were clean before CDC edits.

### Remaining Batch Gaps

**B1-R1: Required comparison inputs missing.**
`artifacts/batch01-identity-evidence.md:14-21` names only the music and Arc07
examples. It substitutes inventory populations for an inspected Erlang card,
rich-rerun card and teaching-rerun card, all explicitly required in this batch.
The rich set contains usable records as well as the three preserved malformed
ones. Neither lack of coverage nor equivalent meaning across those populations
is settled by the inventory reference. Exact input paths, current definition
hashes, actual execution bases, extraction-prompt observations and predecessor
comparisons are also absent or abbreviated.

**B1-R2: Authored meaning/evidence references do not resolve completely.**
JSON `meaning_id` values `aliases-current`, `aliases-legacy`,
`alias-value-current`, `alias-value-legacy`, `concept-slug-current`,
`record-revision` and `title-display` have no matching named definitions or
explicit alias mapping in the report. The prose has shorter generic labels;
do not infer the missing contextual equivalences from similar spelling.
Evidence values such as `current-template` and `legacy-cards` have no
explicit target registry. Shared definitions remain allowed; they must resolve
and account for the actual value/role distinctions, not just label a group.

The report's artifact description says each entry contains a disposition,
but all ten entries contain only path, kind, meaning ID and evidence tag.
Dispositions may live in referenced authored definitions instead, but that
route must be documented and complete. Currently the generic paragraph does
not establish every member's contextual old/current disposition.

**B1-R3: Required execution evidence missing.**
The report's Checks section asserts that `jq` parses the artifact and its
projection matches. It records no literal commands, actual outputs or exit
statuses, and no definition/evidence-reference verifier or input-hash replay.
CDC reproduced selected checks; that does not make the submitted handoff
reproducible. Supply the already-required record rather than expanding tooling.

### Review Method And Limits

CDC used `jq -e` to sort each `[field_path, record_kind]` pair, compare it
with the explicit ten-pair list in the prompt, and subtract the independently
expanded Slice01 index. Result: 10 pairs, 10 unique, empty missing/extra/
not-in-inventory lists, zero entries with a disposition property.
Matching each JSON meaning ID against the report's backtick-delimited named
definitions produced the seven unresolved identifiers above; the full report
was also read to check for another explicit resolution route.

`shasum -a 256` independently checked the four exact input files identified
above against the four values in the report. The File Naming passage and
actual Arc07 frontmatter were read directly, along with current identity/
placeholder guidance. No full re-reading of both prompts, source-book
semantic verification, corpus regeneration, package test or new extraction
is claimed by this bounded review.

The same Batch01 prompt now lists the concrete completion gaps. The original
criteria and all row statuses remain unchanged; S4-1/S4-3 evidence notes now
distinguish these reproduced improvements from the still-open requirements.
The 545 pairs outside this batch are not the only outstanding work: the ten
inside it still need completion and independent acceptance.
