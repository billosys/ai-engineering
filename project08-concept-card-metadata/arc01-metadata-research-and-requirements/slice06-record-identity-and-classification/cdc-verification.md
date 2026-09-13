# CDC Review: Slice06 Initial Delivery

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
