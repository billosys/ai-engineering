# CDC Review: Slice06 Initial Delivery

Latest review: [Iteration 02 closure](#iteration-02-closure-e88e6c0b) below.
All four findings are resolved and all seven rows CDC-closed, with an explicitly
CDC-authored census replay completion. Earlier reviews remain historical.

Date: 2026-09-13. Reviewed planning commit `6a6b1661` against the
unchanged seven-row contract. Source remains `e763c661`; comparison planning
base is `285933a6`. Both checkouts were clean before review.

Verdict: **changes required**. Exact mechanical coverage and scoped preservation
pass independently. The contextual comparison is incomplete; no Slice06
semantic packet is accepted for Slice04 composition yet. CC's original report
and four authored artifacts are preserved unchanged by this review.

## Findings

### S6-R1: Required populated-record and definition evidence is missing

Serious; S6-1, S6-3, S6-5.

`artifacts/semantic-membership.json` registers twelve templates, two legacy
cards and one historical prompt. All 34 current-record pairs cite template
frontmatter lines 2-4. Those lines establish type labels and null placeholders,
not the complete identity/reference contract. No operation guide, field-group
reference or populated current record is registered.

`artifacts/semantic-evidence.md:26-30` mentions available examples through
the inventory, but gives no inspected example paths/values or explicit per-kind
evidence boundary. The frozen inventory has populated source-support records
and synthetic CQ, extraction-run, admission, reconciliation and edge records.
For example, CDC inspected `knowledge/concept-cards/examples/relationship-edge.md`:
root `edge-prepared-provenance-precedes-support` differs from the two endpoint
IDs. The extraction-run example also distinguishes its root ID from inputs
and outputs. These are concrete comparisons the assignment required, not
additional scope.

Supply shared normative rules with per-kind contextual applications and
available populated evidence. Name which kinds have only template evidence
within the inspected scope; distinguish embedded records from root-frontmatter
census observations. Do not generate new records to fill an evidence gap.

### S6-R2: Classification analysis omits observed shapes and anomalies

Serious; S6-1, S6-4, S6-5.

`artifacts/semantic-evidence.md:34-49` describes two non-null examples but
omits the requested census of types/values, historical prerequisite-depth
definitions, and an inspected current-card comparison. CDC queried the frozen
inventory: all 2,054 legacy records have these three keys; category and tier
are strings, while subcategory is a string in 1,974 and null in 80. These
null observations must not be conflated with missing keys or assumed
inapplicability. Category has 26 distinct values, subcategory 408 including
null, and tier three.

There is an anomaly already in CC's chosen sample: `accent-types.md` has
`tier: foundational`, `prerequisites: [meter]`, and a body explaining that
metric accent depends on meter. Historical prompt 0009's Classification section
(lines 111-124) defines foundational as no prerequisites within the source;
0010 lines 214-216 gives the same rule. Record this tension with its limits,
rather than merely listing both values. Check the named dependency's source
identity before asserting a within-source violation; no full graph is needed.
An inspected Erlang null example is
`knowledge/erlang/concept-cards/otp-design-principles/behaviour.md:7-9`.

CDC also inspected the teaching rerun's `cc-pattern-completion.md`: its
frontmatter lacks all three fields. That is generated absence for this
sample, distinct from template omission, not proof of loss through migration.
Complete the required historical/current comparison and concrete consequences
without choosing the future classification architecture.

### S6-R3: A new mandatory lookup rule is presented as observed semantics

Serious; S6-3, S6-5.

The eleven root-ID meaning dispositions, beginning at
`artifacts/semantic-membership.json:102`, and their memberships say lookup
"must pair it with record type and applicable revision".
`knowledge/concept-cards/SKILL.md:138-143` instead requires stable IDs and
revisions, describes references with ID/revision/path, and adds record_type
or an anchor when disambiguation is needed. It does not establish a mandatory
type-qualified lookup key. The registered null templates do not supply one.

Correct the observed contract and distinguish any proposed future key policy
as a design question. Do not infer global uniqueness either. Preserve the
valid root-versus-referenced-identity distinction.

### S6-R4: Replay passes but does not prove every claimed check

Correctness-grade; S6-6 (with S6-1/S6-5 input checks).

Every command in `artifacts/validation-evidence.md` executes successfully.
However, its reference test checks memberships only, not meaning evidence
references. Its hash command prints twelve template hashes; it neither
compares them to the registry nor checks the three other registered inputs.
The text claims exact command output but substitutes "12 registered template
hashes matched" for the actual digest output. The prior-evidence diff is
against the working tree only, so a committed alteration would go undetected.

CDC's stronger checks below pass on this delivery. Repair the durable replay
to assert both reference layers, all registered hashes, and preservation
against an explicit pre-delivery base. Label summaries as summaries. Complete
the seven-ID closing-report walk and disclose the actual missing scope rather
than representing a generic all-rows sentence as completed comparison evidence.

## Reproduced Checks

All commands below ran from `/Users/oubiwann/lab/billosys/ai-engineering`.
No source/package/install action was performed.

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice06-record-identity-and-classification"
i="$a/slice01-metadata-inventory-and-research-questions"
b="$a/slice04-semantic-identity-source-and-graph-families"

# Replay the original single-line commands, without claiming their output summaries are literal.
sed -n 's/^\$ //p' "$s/artifacts/validation-evidence.md" | bash -e

# Independently project the selection from the frozen inventory.
jq -en --slurpfile i "$i/artifacts/field-dispositions.json" --slurpfile s "$s/artifacts/semantic-membership.json" --slurpfile b "$b/artifacts/batch01-identity-membership.json" '
  ([$i[0].field_paths[] | .field_path as $p | .record_kinds[] |
    select((($p=="id" or $p=="revision") and .!="concept-card") or
      $p=="record_type" or
      (($p=="category" or $p=="subcategory" or $p=="tier") and .=="untyped")) |
    [$p,.]] | sort) as $expected |
  ([$s[0].memberships[]|[.field_path,.record_kind]]|sort) as $actual |
  ([$b[0].memberships[]|[.field_path,.record_kind]]) as $batch |
  ($expected|length)==37 and $expected==$actual and
  ($actual|unique|length)==37 and ($actual-($actual-$batch)|length)==0'

jq -e '.evidence as $e | .meanings as $m |
  all(.memberships[]; ($m[.meaning_id] != null) and
    all(.evidence_ids[]; $e[.] != null) and (.disposition|length>0)) and
  all(.meanings[]; all(.evidence_ids[]; $e[.] != null))' "$s/artifacts/semantic-membership.json"
jq -r '.evidence[] | [.sha256,.path] | join("  ")' "$s/artifacts/semantic-membership.json" | shasum -a 256 -c -

jq '[.records[] | select(.path|contains("complete-musician/") or
  contains("knowledge/erlang/concept-cards/"))] as $r |
  ["category","subcategory","tier"] | map(. as $f |
  {field:$f,total:($r|length),present:([$r[]|select(.values|has($f))]|length),
   types:([$r[]|select(.values|has($f))|.values[$f]|type]|group_by(.)|
     map({type:.[0],count:length})),
   distinct_values:([$r[]|select(.values|has($f))|.values[$f]]|unique|length)})' "$i/artifacts/frontmatter-inventory.json"

git -C .worktrees/planning diff --exit-code 285933a6 -- project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families
git -C .worktrees/planning show --format= --check 6a6b1661
git -C .worktrees/planning diff --name-only 6a6b1661^ 6a6b1661
~~~

Results: exits 0; original projection reports 37 expected/actual with empty
missing, extra, not-in-inventory and overlap sets. Independent projection and
reference assertions return true. All 15 registered inputs report OK.
Classification results are reported under S6-R2. Prior Slice01/Slice04
comparison and commit whitespace check are empty. Commit paths are exactly
the four declared artifacts, ledger and CC closing report; no new helper.
These checks establish structure and preservation, not semantic completeness.

## Seven-Row Walk

| Row | CDC status | Evidence and remaining condition |
| --- | --- | --- |
| S6-1 | open | Fifteen hashes resolve; required inspected comparison inputs are incomplete (R1/R2). |
| S6-2 | done | Independently reproduced exact 37-pair equality, uniqueness, inventory inclusion and Batch01 disjointness. |
| S6-3 | open | Root distinctions are promising; populated/definition evidence and lookup-rule correction remain (R1/R3). |
| S6-4 | open | Two legacy observations do not deliver census/anomaly/current-card comparison (R2). |
| S6-5 | open | Structural references resolve, but supported dispositions and contextual consequences remain incomplete (R1-R3). |
| S6-6 | open | Stronger CDC checks pass; durable replay, honest scope reconciliation and full row walk need repair (R4). |
| S6-7 | done | Reproduced scoped six-file commit, unchanged prior packets/source, clean starting states and whitespace. |

## What Worked

The exact-set boundary, resolvable registry and explicit no-runtime/no-admission
scope are useful. All registered hashes match; the distinction between record
identity and referenced identities is worth retaining. No new scripting
language or corpus rewrite was introduced.

## Bubble-Up To Arc01

Scope specified: 37 pairs with contextual evidence, observed value/shape
comparison and literal validation. Scope delivered: complete mechanical
projection, template identity observations, two historical classification
observations, and partial replay. The missing comparison work stays in
Slice06 Iteration 01; the original seven criteria are unchanged.

Arc plan updated to route the correction. No new slice or reassignment is
justified by this review. The 508 pairs outside accepted Batch01 and assigned
Slice06 retain their owners; Slice04, Slice01 and Arc01 remain open.
Slice02/03 research and requirements remain behind remediation composition.
Project outcomes and version intent do not change.

## Iteration 01 Review: a416c2a2

Date: 2026-09-13. Source remains `e763c661`; planning delivery is
`a416c2a2`, following CDC `e6ec28e7`. Both checkouts started clean.
Verdict: **changes required, limited to the remaining classification evidence**.
No new finding or acceptance criterion is introduced.

### Finding Dispositions

- **S6-R1 resolved for current-record identity evidence.** The register now
  connects the identity convention, per-kind field groups, templates and
  populated examples. CDC inspected the CQ, extraction-run, admission,
  reconciliation, edge and generated source-support examples: their root IDs
  denote records, not the referenced concepts, claims, endpoints or sources.
  The named five template-only root kinds agree with the frozen census.
  This does not claim that no embedded populated examples exist elsewhere.
- **S6-R3 resolved.** Both meanings and memberships now describe conditional
  type/anchor disambiguation, consistent with SKILL.md lines 138-144.
  Neither a mandatory composite key nor global uniqueness is asserted.
- **S6-R4's original defects resolved.** The literal route executes, checks
  both reference layers, compares all 25 registered hashes, and compares
  Slice01/Slice04 against 285933a6. Results are honestly labeled summaries.
  The closing report now names every row. The additional missing
  classification inputs/replay below remain part of S6-R2, not a reason to
  reopen the successful original checks.
- **S6-R2 partially resolved, still open.** Null versus missing,
  foundational/prerequisite tension and actual generated-card absence are
  now distinguished. But semantic-evidence.md lines 36-39 gives only merged
  totals and distinct-value counts. Iteration 01 explicitly required observed
  vocabulary with corpus distinctions; neither that comparison nor its
  executable census query is in the delivery. The input register omits the
  frozen inventory, the Meter card used at lines 47-48, and any v3.1
  classification input or checked inherited read. This prevents a complete
  trace from the reported comparison to its declared inputs.

### Why The Remaining Distinction Matters

CDC's independent frozen-inventory query finds:

| Corpus | Records | Category distinct | Subcategory shapes | Subcategory distinct | Tier distinct |
| --- | --- | --- | --- | --- | --- |
| Complete Musician | 390 | 10 strings | 390 strings, no nulls | 67 | 3 strings |
| Erlang | 1,664 | 16 strings | 1,584 strings, 80 nulls | 341 including null | 3 strings |

All three keys are present in every record in both populations. Category
vocabulary differs by domain: music includes counterpoint/harmony/rhythm-meter;
Erlang includes otp-behaviours/distribution/tooling. A merged total of 26
labels cannot by itself describe either domain's observed classification.
This matters for later domain-sensitive discovery and preservation design,
without establishing any replacement taxonomy now.

CDC inspected `complete-musician/meter.md`: it explicitly identifies
`source_slug: complete-musician`, matching Accent Types. This supports the
bounded within-source prerequisite tension, beyond directory co-location.
The claim is not a source-text correctness judgment. The Meter input is
currently absent from the CC register despite supporting that claim.

The frozen inventory hash is
`afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b`;
Meter is
`944771789c8e1dcf7fcbdb3d20f48e73d9a58a6eba22780e7f23a6b76fbbc221`.
These are CDC observations, not retroactive CC-authored evidence.

### Reproduction

From the source root, CDC ran the entire current
`artifacts/validation-evidence.md` bash block literally: two true results,
25 input hashes OK, no preservation or whitespace diff, exit 0. A separate
assertion checked that all membership dispositions/evidence lists equal their
resolved meaning entries, with nonempty definitions/dispositions/evidence:
true. Commit inspection found exactly the six authorized files, both trailers,
and no whitespace errors.

The following additional commands reproduce CDC's corpus distinction check:

~~~bash
set -eu
a=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice06-record-identity-and-classification"
i="$a/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json"
sed -n '/^~~~bash$/,/^~~~$/p' "$s/artifacts/validation-evidence.md" | sed '1d;$d' | bash -e
jq -e '.meanings as $m | all(.memberships[];
  .disposition==$m[.meaning_id].disposition and
  .evidence_ids==$m[.meaning_id].evidence_ids) and all(.meanings[];
  (.definition|length)>0 and (.disposition|length)>0 and
  (.evidence_ids|length)>0)' "$s/artifacts/semantic-membership.json"
jq '[.records[] | select(.path|contains("complete-musician/") or
  contains("knowledge/erlang/concept-cards/")) |
  . + {corpus:(if (.path|contains("complete-musician/")) then "music" else "erlang" end)}] |
  group_by(.corpus) | map(. as $r | {corpus:.[0].corpus,total:length,
  fields:(["category","subcategory","tier"]|map(. as $f |
  {field:$f,present:([$r[]|select(.values|has($f))]|length),
   types:([$r[]|.values[$f]|type]|group_by(.)|map({type:.[0],count:length})),
   distinct_values:([$r[]|.values[$f]]|unique|length)}))})' "$i"
shasum -a 256 "$i" /Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/meter.md
git -C .worktrees/planning diff --name-only e6ec28e7 a416c2a2
git -C .worktrees/planning show --format= --check a416c2a2
~~~

All commands exit 0; counts and hashes above are reproduced. Missing and null
must still be separated in the final CC census; the present-key counts here
establish that none of these three keys is missing in these populations.

### Updated Seven-Row Walk

| Row | CDC status | Result |
| --- | --- | --- |
| S6-1 | open | All 25 registered hashes match; classification inventory/dependency/historical inputs remain incomplete. |
| S6-2 | done | Exact unique 37-pair projection, inventory inclusion and Batch01 disjointness reproduced again. |
| S6-3 | done | Current root identity/revision/type meanings supported; conditional disambiguation repaired. |
| S6-4 | open | Good null/anomaly/current-card corrections; per-corpus vocabulary and historical evidence remain under S6-R2. |
| S6-5 | open | Current-record meanings accepted; classification comparison lacks complete evidence linkage. |
| S6-6 | open | Original replay defects fixed; complete classification replay/handoff awaits S6-R2 repair. |
| S6-7 | done | Six-file scoped correction, clean source, unchanged prior packets and whitespace reproduced. |

### Bubble-Up And Next Assignment

Iteration 01 delivered the principal identity repair and partial classification
repair, not the complete assigned comparison. Open Slice06 Iteration 02 for
the remaining S6-R2 work only. Keep the accepted current-record meanings stable;
all seven original criteria and the exact 37-pair scope remain in force.
The other 508 pairs keep their existing owners. No next slice, research
advancement, source change or parent closure is authorized by this review.
Project objectives are unchanged; the arc plan routes this narrower correction.

## Iteration 02 Closure: e88e6c0b

Date: 2026-09-13. **CDC closed**, with the documentation-only replay
completion explicitly attributed below. Source remains `e763c661`.
The seven original criteria are met within this slice's declared scope.

### Final Finding Disposition And Authorship

S6-R1/R3/R4 remain resolved as reviewed in Iteration 01. S6-R2 now has the
frozen-inventory, Meter and v3.1 inputs connected to classification meanings.
CDC checked the v3.1 Classification section against the v3.2 definitions:
primary domain classification, optional finer classification and source-relative
prerequisite depth agree. Meter's source_slug confirms the bounded same-source
tension. No source-text verification, taxonomy choice or migration result is
implied.

CC's remaining replay omission was literal command text, not missing semantic
analysis. CDC added the explicitly labeled census replay section to
artifacts/validation-evidence.md and pinned its historical preservation endpoint
to e88e6c0b so subsequent authorized parent updates do not break the replay.
CDC executed the completed route. The semantic report,
membership registry, handoff and CC closing report remain byte-identical to
e88e6c0b. CC attestation and CDC-authored documentation are distinguishable.
The full frequency output reproduces both corpora, raw spellings, null states
and all reported totals. This follows the existing Batch01 documentation-repair
precedent, not a lowered criterion or retroactive CC execution claim.

Provenance clarification for downstream readers: the semantic report's phrase
"not real extraction" must not erase its own generated/synthetic distinction.
The five synthetic examples are synthetic; the Arc07 support and teaching card
are real-corpus generated candidates, not independently verified extraction
results. Their registered roles and inspected contents establish this distinction.
This is a CDC clarification, not a new extraction or admission judgment.

### Final Reproduction And Row Walk

From the source root, CDC reran the original validation bash block and the
new CDC census block. Original: two true assertions and all 28 registered
hashes OK; preserved Slice01/Slice04 diff against 285933a6 empty.
Census: exit 0, 390 music plus 1,664 Erlang records, every key present,
frequency totals equal corpus totals. Distinct values are 10/67/3 and
16/341/3 respectively. All 80 present-null subcategories belong to Erlang.
Tier frequencies and named examples match the report.

Registry consistency additionally passes: every membership resolves to the
same evidence list/disposition as its meaning, with nonempty definitions.
The current-record meanings/evidence from a416c2a2 remain unchanged.
The e88e6c0b commit touches only the six authorized files and passes whitespace.
Both starting worktrees were clean; no source/package/install action occurred.

| Row | CDC final status | Evidence |
| --- | --- | --- |
| S6-1 | done | 28 registered hashes and inspected identity/classification sections; exact comparison bases. |
| S6-2 | done | Exact 37 unique pairs, inventory inclusion, Batch01 disjointness reproduced. |
| S6-3 | done | Iteration 01 current-record review retained; no regression in the identity entries. |
| S6-4 | done | Per-corpus raw vocabulary replay, present-null distinction, historical definitions, bounded dependency tension and actual current-card omission. |
| S6-5 | done | Both reference layers resolve; census/dependency/history linked; lookup/discovery consequences and non-equivalence limits inspected. |
| S6-6 | done | Complete literal replay after attributed CDC documentation completion, seven-row walk and bounded handoff. |
| S6-7 | done | Scoped CC commit and preserved source/prior packets; CDC changes separately owned. |

### Bubble-Up And Next Unit

This closes only the assigned 37-pair slice. Combined with Batch01, 47 of 555
observed pairs have accepted bounded contextual evidence, not corpus-wide
migration or semantic-support verification. The remaining 508 are unchanged.

Next: sibling Slice07, source identity and locator semantics, exactly 20 pairs
from the original Slice04 allocation. That leaves 488 outside the accepted
47 and assigned 20: 236 original Slice04 and 252 original Slice05 pairs.
These accounting allocations are not endorsement of the old family labels.

Slice04 still owns full integration and its eight-row closure, including all
remaining source/support/graph/CQ contexts. Slice05 retains lifecycle/provenance
and final replay/composition work. Slice01, Arc01 and Project08 stay open;
research Slice02/03 remain gated. No scope reduction or version change.
The arc/project plans and Slice04 route are updated before opening Slice07.
