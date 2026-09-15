# CDC Verification: Slice02

Date: 2026-09-15. Reviewed CC endpoint:
`753bacb051c041a75d0c4d36595cfbadd5a9b5eb`.
Opening planning endpoint: `a27c4d33a02d3e6047656b9ae0c17a145aa3f208`.
Source: `e763c661592ff1097a94bb470db9cf924524579d`.

## Decision

**Changes required.** S2-1 and S2-5 pass at their stated scope. S2-2, S2-3,
S2-4 and S2-6 remain open. No part of the 30-pair assignment is added to
accepted coverage yet: 150 accepted / 405 remaining, including these 30 and
375 outside. Slice03 is not opened. P-15 remains open.

The useful work is retained: exact ownership, readable legacy question lookup,
separate CQ/reference/lifecycle concerns, populated-versus-template contrasts,
and concrete downstream questions. Passing structural checks does not cure
incorrect census prose or native-result checks that supply their own answers.

## Independent Checks

Before CDC edits, both worktrees were clean. The complete published block
reproduced twice with `CC_COMMIT=753bacb0`, exit 0. The second invocation was:

~~~bash
# cwd: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
CC_COMMIT=753bacb0 bash <(
  awk '/^~~~bash$/{p=1;next} /^~~~$/{p=0} p' \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/artifacts/validation-evidence.md
)
~~~

Observed tools: Bash 5.3.9, jq 1.6, ripgrep 15.2.0. All 25 registered
input hashes matched. Exact seven-file CC diff and whitespace passed.
Independent checks also established 30 unique memberships, remaining-set
inclusion, accepted-set disjointness, both meaning/member evidence-ID
resolution, and preservation of all Arc01, project artifacts and accepted
Slice01/Slice12 packets between the recorded endpoints.

Read the actual source guide, CQ template, field-group reference, populated
synthetic CQ, declared cases, registry and handoff. Compared their meanings
with the prescribed slice criteria. The frozen original hashes for the three
model-data-constraints pilot/rich/teaching witnesses match the registered
originals. This does not supply the omitted original/copy mapping.

## Findings

Line references below identify files at the reviewed CC endpoint, not a later
repair. All findings retain the existing acceptance criteria.

### R1: Census Results And Context Traceability Need Reconciliation

`artifacts/semantic-evidence.md:73` reports cq_refs as 12 absent / 1 empty /
18 populated. Its own six family rows, and the frozen inventory independently,
give **8 absent / 5 empty / 18 populated**. The parsed denominator stays 31.

Lines 81-84 replace one malformed card with INDEX.md. The three excluded card
paths are cc-memory-forms.md, cc-priming-forms.md and
cc-recognition-dual-process.md in the rich-rerun candidate directory.
All three have YAML parser errors. INDEX.md is not the third malformed card.

The replay's lines 58-71 check totals and selected anchors, not the advertised
six-family state/type tables or all selected CQ component fields. Independent
legacy checks confirm 2,054 populated arrays with string items; that retained
result does not validate the incorrect current-card summary.

The plan also asks to reuse original/copy mapping for the embedded generated
witnesses. `semantic-membership.json:39` has an empty baseline_mappings array,
and neither manifest is registered. Originals are real and their hashes match;
the gap is the promised traceability/replay, not an accusation of changed data.

Repair the table and exact exclusions, derive and compare every advertised
selected-field census value, and register/replay the existing bounded
original/copy mapping for the two generated witnesses. Do not reread all
2,054 bodies or recreate the frozen inventory.

### R2: Diagnostic Replay Does Not Establish All Recorded Observations

`artifacts/validation-evidence.md:78-81`: the purported wrong-question lookup
passes an unused q argument to `.records[]`. It emits every inventory record
(2,124), discards that output and checks successful execution. It does not
establish the recorded empty match array. The missing-input control also does
not execute the actual selection. Use the same lookup operation for positive,
wrong-value and failure cases, compare returned values and measured statuses.

CDC separately executed the positive-case selection with the wrong question
and observed [] / exit 0. The expected no-match is plausible and reproducible;
the defect is that the submitted negative control does not test it.

Lines 85-89 verify literal ID/path strings and parent-directory absence, then
construct the entire rich_native result, including revision and lookup status,
from constants. It is not a native-derived tuple/result comparison.
Lines 99-108 similarly hardcode parent-card revisions and tuple values in
the embedded result. Some tuple/headings are independently asserted and the
question/answer text is read: preserve those successes, but compute the full
claimed observation from registered values and actual lookup outcomes.

The missing rich target parent is established with a directory predicate.
That alone is not a measured tool failure. `test ! -d ...` succeeds here;
the reported status 1 is inserted as a constant. Keep a successful bounded
filesystem absence observation distinct from an actual failed search against
a nonexistent root (rg exit 2). Neither establishes global absence or
answerability. Correct the matching prose/case/handoff interpretation.

Reconcile all four case objects and controls with their executed operations.
Negative controls must exercise native-result comparison, not merely search
for unrelated text elsewhere. Deliberately wrong requested IDs/revisions must
not pass as the original expected result; real lookup errors must not pass as
no-match. Do not infer embedded target revisions from parent-card revisions.
Preserve raw source text or explicitly label any presentation normalization.

### R3: Answer Components Versus Referenced Constructs Are Under-Specified

`semantic-membership.json:57,81` defines coverage_assertions[].component as
a "component target" / "target assignment". That wording does not say whether
this is a required part of the answer or a referenced card/claim/support
construct, despite this being the crucial comparison with component_refs.

The source guide (`knowledge/concept-cards/guides/06-graph-cq.md:92-95`)
first decomposes the question into required answer components, then maps each
to exact constructs. The CQ template's Coverage Assertions And Evidence
section asks for one assertion per component with covered revisions.
Its component value is null, so no populated serialization is demonstrated.

Clarify both meaning and member layers: required answer component, assertion
identity/rationale, and mapped constructs have different roles. State what the
guide supports, what the null/template does not establish, and any remaining
encoding uncertainty. Do not invent a schema or force the synthetic
component_refs list into an equivalent template shape. This is a bounded
semantic clarification, not a redesign of all 30 dispositions.

### R4: Committed Replay Still Hashes Mutable Review Documents

The registry includes the live slice plan and ledger (lines 36-37), and the
replay hashes live paths (lines 52-56). CC_COMMIT bounds the Git scope check,
not these input reads. Normal CDC ledger/plan edits therefore invalidate that
supposed committed-evidence replay even though the corpus is unchanged.
The review reproduced the route before making those edits; no later failure
is evidence of source drift.

After CDC plan/ledger updates, the same CC_COMMIT=753bacb0 invocation exited
1 at slicePlan's live hash, after all preceding 23 hashes passed. This directly
reproduces the review-induced failure; semantic inputs were not edited.

Pin historical planning authority to an explicit commit and read those bytes,
or distinguish immutable evidence from mutable operational status with a
documented current-state check. Do not refresh a mutable ledger digest in a
self-referential loop or silently omit evidence validation. Also validate
both registry evidence layers and preserve accepted Slice01/Slice12 packets
explicitly in the current replay, as required by the original prompt.
No generic replay framework or new helper is needed for this repair.

## Independent Census Probe

This read-only probe reproduced the current-state discrepancy and exclusions.
It supplements, rather than implements, CC's required full census.

~~~bash
# cwd: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
i=project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
jq '{
  cq_states: ([.records[] | select(.record_kind=="concept-card") | .values |
    if (has("cq_refs")|not) then "absent"
    elif .cq_refs==null then "null"
    elif (.cq_refs|length)==0 then "empty" else "populated" end] |
    group_by(.) | map({state:.[0],n:length})),
  malformed: [.records[] | select(.error!=null) |
    select(.path|test("compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-.*[.]md$")) |
    {path,error}]
} | if (.cq_states == [{state:"absent",n:8},{state:"empty",n:5},
                       {state:"populated",n:18}]) and
       (.malformed|length)==3
    then . else error("CDC census mismatch") end' "$i"
~~~

Observed states: absent 8, empty 5, populated 18. Observed excluded paths:
memory-forms, priming-forms, recognition-dual-process; each is a YAML error.
The first transcription of this supplemental probe over-escaped the filename
regex and emitted no exclusions; CDC corrected it to [.] and added assertions,
then reran it successfully. The earlier independent frozen-inventory query
already returned the three actual errors. Retain this reviewer correction as
replay-documentation provenance, not a CC defect or extra corpus observation.

## Row Walk

| Row | CDC status | Evidence and limit |
| --- | --- | --- |
| S2-1 | done | Exact 30 unique pairs; plan equality, current inclusion/disjointness, 150/30/375, explicit outside owners. No semantic acceptance of the assignment yet. |
| S2-2 | open | Hashes and useful contextual reads retained; R1 corrects census/exclusions/mapping. |
| S2-3 | open | Useful identity/state distinctions retained; R3 requires the answer-component/construct distinction in both registry layers. |
| S2-4 | open | Positive legacy and synthetic values reproduce; R2 repairs native derivation and controls/status interpretation. |
| S2-5 | done | Concrete architecture questions, all adjacent owners and P-15 preserved. R2 still corrects the handoff's local path/tool claim; this row's acceptance does not endorse that claim. |
| S2-6 | open | Literal route passes at CC endpoint but omits required assertions; R1/R2/R4 require complete, snapshot-aware replay and aligned attestation. |

## Bubble-Up And Next Work

All five artifacts and the CC closing report are present in the authorized
seven-file packet. Scope/preservation are sound, but the assigned capability
is not fully delivered. No criteria are reduced or transferred. Iteration 01
repairs these four bounded findings in the same seven CC files; CDC does not
write replacement semantic results. Retain the two verified rows, historical
CC report and failed-review provenance in later closeout.

Plans record changes-required and the new prompt, not a new family or schema.
Accepted coverage and all source/package/runtime/admission boundaries stay
unchanged. The workload artifact records this third distinct reviewed slice;
it does not count corrections or heartbeat previews as independent trials.
