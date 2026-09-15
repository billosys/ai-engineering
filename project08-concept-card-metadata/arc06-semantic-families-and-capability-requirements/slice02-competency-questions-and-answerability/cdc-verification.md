# CDC Verification: Slice02

Current status: independently closed after Iteration 01; see the final
closure section below. The initial review is preserved, not current routing.

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

## Iteration 01 Independent Closure

Reviewed 2026-09-15: ca1df9264c13925f7550b3cbce3a63eaf576f3cc, based on
f15c896bfeec4c3618387413e63c95dfe9fc6771. **All six rows are now done.**
The initial changes-required review above remains historical evidence.
R1-R4 are resolved with the limited CDC completion explicitly described below.

### Reproduction And Semantic Review

The submitted current block passed independently with the full repair SHA
as CC_COMMIT, exit 0: 29 registered hashes, both original/copy manifests,
two direct byte comparisons, full family/root census, native comparisons,
ten controls, JSON, preservation and exact seven-file CC scope.
The source remains at e763c661 with no changes.

- R1: correct 8/5/18 card states and three named YAML-error exclusions;
  source/copy mappings and two manifests reproduce. The original values and
  the preserved-copy roles remain distinct.
- R2: actual question selection now handles positive, wrong-value and missing
  input. Native tuples and parent-card revisions come from parsed originals;
  literal headings and answer text come from source bodies. ID/revision
  negative comparisons reject altered expectations. Directory absence is
  no longer mislabeled rg failure.
- R3: source guide 06 and the CQ template support separate required answer
  components, mapped constructs and coverage assertions. Both registry layers
  now preserve these distinctions and the null-encoding limitation.
  The synthetic component list is not proof of a populated answer-component
  mapping or conformance; acceptance is of this bounded inventory distinction.
- R4: historical plan and ledger bytes are read from pinned commits; live
  status no longer supplies their authoritative hashes. Accepted earlier
  packets are explicitly preserved in the repair's committed diff.

CDC independently injected exit 2 into the real native support lookup
(the anchored support-synthetic-claim-001 search, not merely its test control).
The replay rejected it with exit 1 instead of accepting no-match. A nonzero
validator rejection is the observation; it does not claim the validator
propagates the injected status unchanged.

### Attributed CDC Completion

Two already-advertised scalar facts were checked separately, then added as
assertions: all 18 populated card CQ references request revision 1, and the
synthetic question text matches its source. Both checks passed before editing.
The other checks already cover the surrounding types, counts and states.

The repair pins plan/ledger, but still read the current coverage register live.
Accepting this slice necessarily changes that register from 150/405 to 180/375.
CDC therefore pinned currentCoverage's existing bytes at ca1df926, retaining
its existing digest, and made the replay read that committed snapshot through
a temporary file. The file is removed by an EXIT trap. These are bounded
replay/authority corrections, not new field meanings or altered expected cases.
The completed block passed again, including after the live coverage and
slice plan/ledger closure updates. Current coverage independently checks as
180 unique accepted / 375 unique remaining, disjoint, with the same complete
555-pair union as the frozen transition. The 40 actor-family sizing count
also reproduces from the remaining set.

This is not a claim that CC supplied the final replay untouched, or that CDC
independently verified its own authorship. The CC-authored semantics and
original replay were independently reviewed first. The attributed additions
preserve observed values and were executed as reviewer-authored completions.

Two stale report phrases are explicitly superseded here without editing CC's
attestation: all three rich exclusions are YAML parse errors, not missing
opening frontmatter; the synthetic body identifies an inaccessible synthetic
locator, not a blanket claim that every reference is fictional. No extra
source-truth inference is accepted from those phrases. The CC report's initial
pending-endpoint wording is resolved by the full SHA above.

### Final Row Walk And Bubble-Up

| Row | Independent disposition |
| --- | --- |
| S2-1 | done: exact 30 unique pairs and outside ownership preserved |
| S2-2 | done: corrected contextual census, source/copy provenance and hashes |
| S2-3 | done: role-specific meanings, authority limits and encoding uncertainty |
| S2-4 | done: four native comparisons, ten controls and independent error injection |
| S2-5 | done: concrete questions/owners/P-15 retained; path/tool prose corrected |
| S2-6 | done: committed replay plus attributed scalar/snapshot completion and preservation |

Accept these 30 inventory pairs once: 180 accepted and 375 remaining.
This is not schema adoption, source-truth endorsement, new extraction,
operator card-quality acceptance or memory admission. All project gates remain.

The next step separates reusable evidence/replay mechanics (Slice03) from
provenance-family semantic analysis (new Slice13, to size before opening).
The original combined Slice03 workload is preserved across those owners;
nothing is discarded. Slice03 accepts zero additional semantic pairs and
does not build a production schema, parser, database or runtime.

### Current Invocation

From the planning root, run the completed current block with the original
full CC SHA. Its committed-diff scope deliberately excludes later CDC edits.

~~~bash
CC_COMMIT=ca1df9264c13925f7550b3cbce3a63eaf576f3cc bash <(
  awk '/^~~~bash$/{p=1;next} /^~~~$/{p=0} p' \
    project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice02-competency-questions-and-answerability/artifacts/validation-evidence.md
)
~~~
