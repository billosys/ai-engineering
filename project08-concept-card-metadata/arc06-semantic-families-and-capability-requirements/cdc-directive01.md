# CDC Directive 01: Bounded Mode And Role Units

Date: 2026-09-17. From CDC to CRC through the Operator.
Response to: [crc-escalation01.md](./crc-escalation01.md).
Status: issued; awaiting CRC acknowledgement in this arc's Design Handoff History.
This is the arc-level exchange 01, distinct from the unchanged project-level
cdc-directive01.md assigning the three contributor seats.

## Decision And Authority

Approve Option 2: two kind-aligned mode/role units, eight pairs then twelve.
Keep the two fields together to compare operation mode with activity role;
keep record-kind groups separate so shared spelling does not supply semantics.
This uses the Operator's established authorization for bounded semantic-family
slicing and CDC's design responsibility. The relay of this escalation is not
treated as a new approval to expand scope, weaken acceptance or adopt a schema.

The response settles sizing/ownership only. It does not review Slice14 again,
accept a new pair, open a CC assignment, or perform arc composition. Its
existing CRC acceptance remains the relevant slice verdict.

| CRC request | Disposition |
| --- | --- |
| 1. Family boundary, exact next set and remainder owners | Approved as Slice15 eight pairs, Slice16 twelve pairs, and explicit Slice17 retained scope below. Reject an all-in-one twenty-plus-provenance execution packet for this opening. |
| 2. Who does pre-opening recount and minimum evidence | CRC owns pre-opening preparation. CDC has freshly reproduced the sizing census below; CRC checks it against actual opening inputs and reads witnesses before issuing. CC later independently reproduces the substantive census and evidence, not a return-only preliminary assignment. |
| 3. Plan/ledger/coverage amendments and new prompt | CDC updates project/arc direction now. After acknowledgement and author readiness, CRC may write Slice15's full open set and initial cc-prompt.md using the current prompt-authoring guide, update factual ledgers and assign exactly eight pairs in live coverage. No accepted-pair change until independent CRC acceptance. |

## Exact Boundaries

Retain the planned Slice15 slug for continuity:
slice15-provenance-roles-runs-and-shared-references.
Its binding assignment is now ONLY:

~~~json
[
  ["actor.mode","claim"],
  ["actor.mode","competency-question"],
  ["actor.mode","concept-card"],
  ["actor.mode","extraction-run"],
  ["actor.role","claim"],
  ["actor.role","competency-question"],
  ["actor.role","concept-card"],
  ["actor.role","extraction-run"]
]
~~~

Slice16, slice16-supporting-record-actor-mode-and-role, owns exactly:

~~~json
[
  ["actor.mode","memory-admission"],
  ["actor.mode","preservation-decision"],
  ["actor.mode","relationship-edge"],
  ["actor.mode","source-locator"],
  ["actor.mode","source-support"],
  ["actor.mode","validation-result"],
  ["actor.role","memory-admission"],
  ["actor.role","preservation-decision"],
  ["actor.role","relationship-edge"],
  ["actor.role","source-locator"],
  ["actor.role","source-support"],
  ["actor.role","validation-result"]
]
~~~

Slice16 opens only after Slice15 acceptance and its own current recount/readiness.
CRC may detail that approved boundary without a new CDC sizing decision if
evidence introduces no material change. Its handoff must compare both groups:
shared observations, per-kind applicability, exceptions and unresolved
differences. It must not import all Slice15 meanings mechanically.

Slice17, slice17-run-preparation-method-and-reference-provenance, inherits
every other former Slice15 provenance obligation:

| Retained interface | Primary owner / boundary |
| --- | --- |
| Run identity, operation, intended/actual scope, workers, prior runs and output provenance | Slice17; distinguish run metadata from actor mappings and output identity |
| Source preparation records, prepared-source/snapshot linkage and extraction handoff provenance | Slice17; source locator/address and support semantics already accepted stay historical inputs |
| Method/prompt identity/settings and creation/time provenance | Slice17; no inferred actor identity or new global timestamp policy |
| Shared provenance reference components, target/revision/path applicability and cross-record inheritance questions | Slice17; compare kind-specific contracts, not a universal reference schema |
| Remaining CQ provenance interfaces, including run/method/preparation context | Slice17; accepted CQ coverage/answerability meaning is not reassigned or double-counted |
| Evidence/confidence; validation/verification; reconciliation; preservation; admission meanings | Existing Slices04,05,06,07,08 respectively; cross-references to Slice17 where needed |
| Full inventory join/replay; standards synthesis; requirements and schema/spec discussion handoff | Existing Slices09,10,11 respectively |

Slice17 is an explicit retained owner, NOT an approved unbounded CC task.
Before it opens, CRC enumerates the relevant remaining pairs, resolves
cross-family primary ownership, and proposes a bounded split to CDC. Its exact
subdivision is deliberately unresolved until that evidence exists. This is
in-project sequencing, not deferral out of Project08. All 335 non-mode/role
remaining pairs stay Arc06-owned across these families, not all assigned to
Slice17. Do not infer ownership solely from matching suffixes or field names.

## Checked State And Sizing Evidence

Inspected planning HEAD: ee12e88cab1220d97a3bc35a329d13629245b226.
Source HEAD: 76a69fd9c295e78f23faa651746c2e36646e0ebd. Both clean.
Escalation refers to arc 1.15 at acceptance; arc 1.16 additionally records the
escalation. This response advances arc to 1.17 and project from 1.29 to 1.30.
Closed Slice14 plan 1.4, its CRC verdict and all CC artifacts remain unchanged.
CRC-accepted endpoints b10bb1ec / a4a7047c and acceptance febbd787 are retained.

CDC inspected the escalation, final Slice14 CRC review and handoff, current
plans/ledgers and frozen inventory. This is a fresh sizing check, not a
duplicated routine acceptance replay or a claim to have completed mode/role
semantic analysis. Source concept-cards/document-extraction trees have no
diff between 02026824 and current source HEAD.

Checked identities:
- Frozen inventory SHA-256:
  afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b.
- Current coverage SHA-256:
  cf2a8cb5455b48d9803bde3d6f8d41b7f3c577398d44f2141644d49dd9f382d7.
- Coverage: 555 total / 200 accepted / 355 remaining / zero assigned.
  Exactly twenty remaining mode/role pairs; none in accepted coverage.
  The two sets above are disjoint and exhaust those twenty.

Native object-valued records, independently recounted from inventory.records:

| Group | Records by kind | Both fields: parent absent | Both fields: template null | Populated mode / role |
| --- | --- | ---: | ---: | --- |
| Slice15 | claim 1; CQ 2; card 31; run 3 (37 total) | 12 | 4 | 21 agent-direct / extractor |
| Slice16 | admission 2; preservation 1; edge 2; locator 1; support 5; validation 1 (12 total) | 2 | 6 | 4 agent-direct / extractor |

Slice15 absent parents: six synthetic and six expanded Arc07 cards/records;
more precisely the synthetic six are one CQ, three cards and two runs.
Populated cards: four pilot, seven rich rerun, ten teaching rerun.
Slice16 absent parents: synthetic edge/admission; populated records: four pilot
supports. The remainder of each group is its one-template-per-kind population.
No other native mode/role state was observed in these selected parsed mappings.
Three malformed rich-rerun cards remain outside the parsed population; their
exact exclusion set must be carried into the next acceptance census.

The repeated strings justify a bounded work packet, not authority equivalence,
a complete vocabulary, requiredness or proof that recorded mode describes all
human/agent activity. Compare source guide definitions and full record/body
context before writing effective meanings. Slice14's three CC runs are a
headroom warning, not a causal model/effort ranking. No model change is ordered.

### Recount Route

From the canonical planning checkout, the existing-tool route used for sizing
is below. It is read-only; path-family grouping is a sizing aid to verify
against raw witnesses, not a new semantic authority.

~~~bash
set -euo pipefail
p=project08-concept-card-metadata
inventory=$p/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions/artifacts/frontmatter-inventory.json
coverage=$p/artifacts/semantic-coverage-current.json
jq -e '.counts=={full:555,accepted:200,remaining:355,next_slice:0,not_yet_sliced:355} and (.accepted_pairs|length==200) and (.remaining_pairs|length==355) and ((.accepted_pairs+.remaining_pairs)|unique|length==555)' "$coverage"
jq '[.remaining_pairs[] | select(.[0]=="actor.mode" or .[0]=="actor.role")]' "$coverage"
jq '
 def groupname: if (.record_kind|IN("claim","competency-question","concept-card","extraction-run")) then "first-four-kinds" else "other-six-kinds" end;
 def family: if (.path|contains("/templates/")) then "template" elif (.path|contains("/examples/")) then "synthetic" elif (.path|contains("slice02-pilot")) then "pilot" elif (.path|contains("slice04-expanded")) then "expanded" elif (.path|contains("teaching")) then "teaching" elif (.path|contains("rich")) then "rich" else "other" end;
 def state($f): .values as $v | if ($v|has("actor")|not) then "parent-absent" elif $v.actor==null then "parent-null" elif ($v.actor|type)!="object" then "parent-unexpected" elif ($v.actor|has($f)|not) then "child-absent" elif $v.actor[$f]==null then "child-null" else ("child-"+($v.actor[$f]|type)+":"+($v.actor[$f]|tojson)) end;
 [.records[] | select(.record_kind|IN("claim","competency-question","concept-card","extraction-run","memory-admission","preservation-decision","relationship-edge","source-locator","source-support","validation-result")) | select(.values|type=="object") |
 {group:groupname,kind:.record_kind,family:family,path,mode:state("mode"),role:state("role")}] |
 group_by(.group) | map({group:.[0].group,records:length, by_kind:(group_by(.kind)|map({kind:.[0].kind,n:length})), cells:(group_by([.family,.mode,.role])|map({family:.[0].family,mode:.[0].mode,role:.[0].role,n:length}))})
' "$inventory"
shasum -a 256 "$inventory" "$coverage"
git rev-parse HEAD
~~~

## CRC Preparation And Issue Conditions

1. Read/acknowledge this response in arc Design Handoff History, recording
   actual context identity, state and next action. Do not edit either issued
   directive or the escalation. Project-level seat acknowledgement stays intact.
2. Recount the selected exact sets against current accepted/remaining and the
   frozen full denominator, and verify the registered inventory identity. If
   material state differs, stop affected opening and return a bounded escalation.
   Source-wide HEAD motion alone is not a mismatch in relevant evidence.
3. Inspect the four selected templates, relevant concept-cards mode/role
   guidance and synthetic/generated witnesses in full record/body context.
   Native prior census plus hashes is not sufficient author reconnaissance.
   Identify documented versus observed versus unknown semantics per kind,
   concrete operational consequences and remaining decision owners.
4. In Slice15 slice-plan.md, record concise pre-opening census/witness evidence,
   exact allowed outputs, applied guidance, inspection/replay design and
   prompt-author readiness. Reuse existing slice artifact conventions; no new
   helper framework or standalone ceremonial reading artifact is needed.
5. Author the open set and initial CC prompt using source
   knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md
   and the current project-management/work-verification routes. Include a
   bounded required-reading manifest with full/section/conditional distinctions,
   revision-qualified ranges, intake/readback instructions and an allowed
   existing evidence home. The author must load and apply required source
   guidance, not merely tell CC to do it. Budget reading plus implementation
   and recovery; do not issue an oversized packet or permit silent skimming.
6. After readiness, assign exactly eight pairs and commit explicit files;
   provide the new prompt to the Operator for fresh CC. No separate CDC approval
   is needed when these issue conditions pass. CC executes the evidence work
   and returns to CRC; your preparation does not count as CC implementation.

Minimum acceptance remains the established family contract: exact set and
ownership; native kind/family/parent-child census with malformed exclusions and
bounded legacy comparison; field-specific evidence-backed meanings; native
diagnostics with independent oracles, wrong-value/state controls and actual
error versus no-match; both reference layers, all registered hashes/ranges,
fail-closed pinned recipe/contribution replay and preservation; concrete handoff
with all outside owners and P-15 retained. Design exact tests at authoring.
Compare mode and role separately; a test that selects the wrong child or treats
absence as null must fail. Do not treat receipts, hashes or expected-as-observed
fixtures as semantic proof. Reading-range and recipe defects from Slice14
remain useful regression cases, not a demand to replay all historical repairs.

At issue, if unchanged, live counts become 200 accepted / 355 remaining /
8 assigned / 347 outside. This response leaves them at 200/355/0/355.
After actual Slice15 acceptance and later Slice16 opening, expected counts
would be 208/347/12/335. These are prospective arithmetic, never acceptance.
Update only current coverage on assignment/acceptance; frozen coverage stays
immutable. CRC can update factual parent status/ledgers/version histories within
this decision, not independently choose another boundary or waive a criterion.

## Holds, Return And Closure

Held until CRC acknowledgement/readiness: Slice15 issuance. Held until Slice15
closure and fresh readiness: Slice16 issuance. Held for another sizing decision:
Slice17 execution. No other slice, source skill, schema, package/install,
runtime, corpus extraction or memory changes are authorized by this directive.
Use existing Bash/jq/Git/hash tools; no new Ruby/Python/helper/parser work.

All A6 and P rows remain open, including P-15 discussion before normative
schema/spec adoption and Operator output-quality/full-book gates. No prior
slice reopening is required solely for this split; surface actual contradictions
explicitly. Slice14 R1-R5 and its two executed corrective refinements remain
historical evidence. Neither this exchange nor new slice IDs reset a repair
budget or remove unfinished obligations.

Return acknowledgement/readiness and scoped planning commit with the exact
new CC prompt path through the Operator, or an explicit blocker/escalation if
a condition fails. Keep CRC routine acceptance and CDC arc/project composition
separate. The Operator should relay this directive to CRC, not CC.
