# CDC Directive 02: Five Bounded Provenance Units

Date: 2026-09-18. From CDC to CRC through the Operator.
Response to: [crc-escalation02.md](./crc-escalation02.md).
Predecessor: arc [cdc-directive01.md](./cdc-directive01.md).
Status: issued; awaiting CRC acknowledgement in arc Design Handoff History.
This is a CDC design response, not a CC assignment or a slice verdict.

## Decisions And Authority

Approve Option 2 using the Operator's existing semantic-family and bounded-slice
planning authorization. This divides retained work within Project08; it does
not expand or reduce its capability, evidence or acceptance contract. Relaying
the escalation is not treated as blanket approval of new scope.

| Request | Disposition |
| --- | --- |
| 1. Exact provenance boundary and remainder | Approve the exact 87 pairs in escalation Sets A-E, with the explicit remainder ownership below. All 248 other pairs remain Arc06 obligations; none is waived or accepted. |
| 2. Split and numbering | Approve Slice17=A (18), Slice18=B (22), Slice19=C (19), Slice20=D (11), Slice21=E (17), sequentially with fresh readiness for each. Reject the combined 87-pair task and broader 40/47-pair alternative at this opening. |
| 3. CQ boundary | Approve only CQ run_refs in Set C and created_at in Set D as new provenance memberships. CQ evidence/confidence, retrieval, revision and lifecycle work retain the explicit owners below. |
| 4. CRC authority | CDC amends the project/arc roadmap and arc ledger now. After acknowledgement and fresh author readiness, CRC may detail/open Slice17, assign exactly Set A and issue its initial CC prompt. No additional CDC pre-opening return is required if these conditions pass. Later approved units follow the same rule after predecessor acceptance. |
| 5. P-15 and normative decisions | Retain the Operator schema/specification discussion gate. No global requiredness, timestamp policy, actor inheritance, reference schema, vocabulary or migration policy is adopted by these units. |

This directive supersedes only directive01's unsized Slice17 boundary and
another-CDC-sizing hold for these exact groups. Preserve directive01 and the
escalation unedited. Slice15/16 acceptance and earlier evidence remain intact;
actual contradictory findings require an explicit affected-evidence review.

## Exact Ownership And Order

The five JSON arrays under escalation02's "Exact Candidate Sets" are incorporated
as exact pair boundaries, not prefix rules. Authority is the preserved file at
planning commit dee3052c88e0fd9361e74200fd1eea26ade76435, SHA-256
7fbb27267077eee831673fe688c60ad8f2e0e96975cf301227f65a037afcb592.
Compare exact sets when creating assignments; do not regenerate them from a
field-name heuristic.

| Slice directory | Set | Operational question |
| --- | --- | --- |
| slice17-run-preparation-method-and-reference-provenance | A: 18 | What operation ran, on which source/prepared/old-card inputs, with what method, settings, prior-run and time context? Stable earlier slug retained; scope is now only A. |
| slice18-run-scope-workers-and-outputs | B: 22 | What was intended, actually covered and produced, and how was worker scope represented? |
| slice19-cross-record-run-references | C: 19 | What does each kind's run linkage identify, and what can actually be resolved? |
| slice20-cross-record-creation-time | D: 11 | What record-local creation assertion is documented or observed, with which precision and unknowns? |
| slice21-cross-record-preparation-and-method-references | E: 17 | What prepared representation or method does each kind reference, with which component applicability and limitations? |

At this response no unit is open and coverage is unchanged: 220 accepted /
335 remaining / zero assigned. If unchanged at Slice17 opening, counts become
220/335/18/317; those are prospective assignment counts, not acceptance.
Do not pre-create Slice18-21 open sets. Detail the next unit only when near.

All remaining non-provenance pairs retain primary semantic owners in Slices04-08;
Slices09-11 own recomposition, research and requirements, not blanket semantic
acceptance of an unexplained remainder. Clarify the less obvious interfaces:

- Slice04: evidence-grade and extraction-confidence fields, including the untyped
  extraction_confidence membership; synthetic and surface_class markers across
  their observed kinds. Compare marker meaning and applicability without
  converting synthetic labels or surface categories into evidence warrant.
- Slice05: validation/verification results, states and references, including
  verifier/validator identity, review context, method/settings and result-local
  source/snapshot/support references; card_status as a lifecycle marker to
  compare with, not collapse into, actual validation/verification. CQ
  retrieval_probe_use, retrieval_state
  and retrieval_result_refs belong here as observed evaluation, NOT admission
  or proof of answerability. Consult accepted CQ findings without reaccepting them.
- Slice06: reconciliation results/states/references, reconciler and revision
  effects; CQ prior_cq_refs, replacement_cq_ref and reentry_condition. Preserve
  prior-value and authority interfaces to Slices07/08.
- Slice07: preservation results/states/references, prior value, destinations
  and preservation-local review/re-entry/decision boundaries.
- Slice08: admission/reliance, operator authority, runtime-write declarations
  and admission-local subjects, targets, criteria and summaries.
- Generic local names such as evidence_refs, target_refs, prior_result_refs,
  source_support_refs and state_effects require their owning result/decision
  context; accepted source-support or record identity does not accept their new
  roles. A reference to another family's result links to that family but does
  not transfer the containing record's scope or authority to it.
- Slice09 reconciles the complete join and original obligations, Slice10 the
  standards alternatives, and Slice11 no-loss requirements and P-15. They must
  expose any unmatched pair, not silently absorb it as a mechanical no-op.

These are planning owners, not evidence-backed field dispositions. CRC must
enumerate each later family's exact boundary and size it before execution;
the above is not authorization to issue an oversized Slice04-08 packet.
Any unresolved primary-owner collision returns to CDC. The full 248-pair
complement remains in the current register and cannot disappear between slices.

## CDC Sizing Evidence

Checked source HEAD: ce3f77103eff5e07b3533a03c65f158684fc1039.
Checked planning HEAD: dee3052c88e0fd9361e74200fd1eea26ade76435; both clean.
Read project plan 1.34, arc plan 1.23 (1.22 at acceptance), both ledgers,
prior directive, escalation, Slice16 CRC record and handoff. This response
advances project to 1.35 and arc to 1.24; no acceptance criterion changes.

Independently reproduced exact counts 18/22/19/11/17, 87 unique pairs,
inclusion in current remaining and frozen full sets, disjointness from the
220 accepted pairs, and a 248-pair complement. Inspected the complete complement
grouped by record kind, including discovery markers and CQ retrieval/revision
fields omitted from the escalation's short owner summary.

Read all three extraction-run records, including their bodies, and compared
their frozen parsed objects. They are one template and two synthetic examples,
not three real extraction traces. The template uses mapping-valued output_refs;
only extraction-run-trace supplies a populated sequence, while the parallel
example has output_refs absent. Both synthetic records have singular source/
prepared mappings and worker_scope; the parallel example omits reference paths.
Template nulls and empty collections do not establish global requiredness.
The parallel example's worker count and the template's additional-worker count
must not be silently equated. These distinctions justify separate A/B work.

Also read the CQ template/example and live concept-cards record conventions
to check the CQ boundary. Broad reference conventions must be compared with
field-specific and populated contexts, not treated as an already accepted
universal schema. This is sizing reconnaissance, NOT completion of the 87
semantic comparisons or a second routine Slice16 acceptance.

Checked SHA-256 identities:
- Current coverage: 5c87682b78b412dfd12018a6da91db2c29cde753d53cf34aaa09437a6eb1377c.
- Frozen transition: 3f1bf740a1c74f0e6c668b57d5c3eef5ba9ce936e56746817c2171a19daf17bd.
- Frozen inventory: afc1985f1998da0d1df0bdc5800aada9842e77873271fc65f3ae190c0e057b1b.

### Read-Only Sizing Replay

Run from the canonical planning checkout. This checks the decision baseline,
not future live assignment/acceptance counts.

~~~bash
set -euo pipefail
p=project08-concept-card-metadata
a=$p/arc06-semantic-families-and-capability-requirements
base=dee3052c88e0fd9361e74200fd1eea26ade76435
sets=$(git show "$base:$a/crc-escalation02.md" |
  awk '/^~~~json$/{p=1;next} p && /^~~~$/{p=0;next} p' | jq -s .)
coverage=$(git show "$base:$p/artifacts/semantic-coverage-current.json")
frozen=$(git show "$base:$p/artifacts/semantic-transition-coverage.json")
jq -n -e --argjson s "$sets" --argjson c "$coverage" --argjson f "$frozen" '
  ($s|add) as $u | ($f.accepted_pairs+$f.remaining_pairs) as $full |
  ($s|map(length))==[18,22,19,11,17] and
  ($u|length)==87 and ($u|unique|length)==87 and
  ($u-$c.remaining_pairs|length)==0 and
  ($u-$full|length)==0 and
  ($u-($u-$c.accepted_pairs)|length)==0 and
  $c.counts=={full:555,accepted:220,remaining:335,next_slice:0,not_yet_sliced:335} and
  ($c.remaining_pairs-$u|length)==248 and
  (($c.accepted_pairs+$c.remaining_pairs)|sort)==($full|sort)'
jq -n --argjson s "$sets" --argjson c "$coverage" '
  ($c.remaining_pairs-($s|add)) | group_by(.[1]) |
  map({kind:.[0][1],count:length,paths:map(.[0])})'
~~~

## CRC Readiness, Issuance And Review

1. Read and acknowledge this directive against current state in arc Design
   Handoff History, recording actual CRC identity, revisions and next action.
   CDC does not acknowledge on CRC's behalf. Reconcile material drift first.
2. Before each open set, recount its exact pair set, kind/family populations
   and malformed/excluded inputs. Inspect relevant guidance, full native
   template/generated/synthetic witnesses and historical comparisons. Reuse
   accepted evidence only with explicit applicability and preserved limits.
3. Complete engineering-methods guide07 author readiness. Budget text reading,
   structured-data queries, semantic analysis, diagnostics, replay and repair
   headroom, not just pair count. C/D span eleven record kinds; a small pair
   total is not proof of a small context packet.
4. Put the required-reading manifest in the new prompt: required-full active
   prompt/plan/ledger and binding text, bounded required-section guidance,
   required-data projections with complete outputs, and conditional versus
   reference-only dependencies. Name the existing allowed evidence home for
   intake and source-cited readback. Recover truncation; do not silently skim.
5. Supply a concrete evidence method and discriminating native tests. Retain
   absence/null/empty/malformed/populated distinctions and parent-child states,
   independent expected results, wrong-field/shape/target/revision controls as
   applicable, and match/no-match/search-error outcomes. Do not prescribe
   conclusions where the evidence is insufficient.
6. Reuse the shared replay contract only after checking its actual coverage.
   Validate each registered authority, hash and range; unknown descriptors and
   wrong-authority mutations must fail through the real predicates. Keep
   registry/contribution and recipe endpoints explicit; inherited passing
   checkers do not automatically validate this new slice.
7. Record scope, field-specific consequences, unresolved questions/owners,
   author readiness and assignment history in the existing open set. Assign
   only the next exact set in current coverage; freeze remains unchanged.
   Commit explicit files with required trailers; relay the new prompt through
   the Operator to a fresh CC context.
8. CRC independently reviews the returned packet, including semantic context,
   not only replay success. Acceptance alone moves its exact set into accepted
   coverage. Update factual parent status/history, then assess the next unit.

Minimum family evidence and all A6/P criteria remain unchanged. B must compare
mapping/sequence/absent outputs and worker-count meanings; C must distinguish
run linkage from authority inheritance; D must distinguish creation from run
time or approval time without inventing precision/timezone policy; E must
compare each reference's actual kind-specific role. A uses the three native
run contexts but does not repair their source templates or missing targets.

Keep workload observations in the existing slice readiness/return records:
required-read size, context recovery/compaction where observable, correction
categories and actual model/effort if available. Slice16's one focused repair
is encouraging, not a causal model ranking or proof these units fit. Do not
change model/effort automatically. Re-escalate sizing pressure before exhausting
headroom; five repair iterations is a safeguard, not a target or resettable
allowance. No quality waiver follows from a larger packet.

## Holds And Return

CRC may open Slice17 only after acknowledgement/readiness, then Slice18-21
sequentially after each predecessor is independently accepted and fresh
readiness passes. No additional routine CDC approval is needed within these
bounds. Scope changes, unsupported ownership, contradictions affecting accepted
evidence, exhausted iterations or an oversized next packet return to CDC.

No source, schema, helper/parser, package/install, runtime, extraction/UAT or
memory mutation is authorized. Use existing Bash/jq/Git/hash tools. No new
Ruby/Python scripts. All A6 and P rows remain open; P-15 and repeated real-run,
Complete Musician, conditional full-book and Operator quality gates remain.

Return acknowledgement/readiness, the scoped planning commit and exact next
CC prompt path to the Operator, or an explicit blocker/escalation. Operator:
relay this directive to CRC, not CC. Arc/project composition remains a later,
separate CDC gate.
