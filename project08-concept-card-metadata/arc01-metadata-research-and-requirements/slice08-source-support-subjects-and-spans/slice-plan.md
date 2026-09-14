---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
slice: slice08-source-support-subjects-and-spans
status: closed
version: "1.2"
---

# Source Support Subjects And Spans

Explain how source-support records identify the assertion being supported and
the selected material used for that support. Preserve the distinction between
finding an address, selecting a span and assessing its relation to an assertion.
This is authored inventory/comparison work, not new card verification.

CDC closure of `3436020a` (2026-09-13): all seven criteria pass;
see cdc-verification.md for the row walk, pinned replay and retained target
limitations. Arc01 now routes next execution to Slice09. Was: Iteration 01
pending. The following correction passage is historical, not an active prompt.

Earlier CDC review of `2dfe5577` (2026-09-13): S8-2/S8-4/S8-7 pass independently.
Reference consistency, historical/contextual consequences and full replay
remain open under S8-R1/R2/R3. Follow `artifacts/iteration-01-cc-prompt.md`.
Was: initial CC execution. All 27 pairs and seven criteria remain unchanged;
no pilot repair, scope reduction or new slice is authorized by this correction.

## Basis And Sizing

Consumes the frozen Slice01 inventory, accepted Batch01 and CDC-closed
Slice06/Slice07. Source baseline e763c661; planning entry baseline must be
recorded at execution. All inputs are read-only.

Twenty-seven pairs form a coherent part of the source-support construct:
subject linkage, embedded span selection/identity/references and the support
status label. The frozen census has five source-support roots: the template
and four populated Arc07 support records. Inspect those five plus relevant
guidance, cited targets and bounded historical/synthetic contexts, leaving
headroom for semantic review. Do not expand to every claim, graph or lifecycle
field just because they coexist in these records.

## Exact Pair Selection

The table is exhaustive. All pairs occur in the original Slice04 allocation
and are disjoint from the 67 accepted pairs. Kind is the frozen observed label,
not a future schema or semantic-family decision.

| Field path | Record kind |
| --- | --- |
| `source_spans` | `source-support` |
| `source_spans[]` | `source-support` |
| `source_spans[].checksum_or_edition_note` | `source-support` |
| `source_spans[].content_or_description` | `source-support` |
| `source_spans[].context` | `source-support` |
| `source_spans[].locator_refs` | `source-support` |
| `source_spans[].locator_refs[]` | `source-support` |
| `source_spans[].locator_refs[].id` | `source-support` |
| `source_spans[].locator_refs[].path` | `source-support` |
| `source_spans[].locator_refs[].revision` | `source-support` |
| `source_spans[].quote_policy` | `source-support` |
| `source_spans[].selection_boundaries` | `source-support` |
| `source_spans[].source_ref` | `source-support` |
| `source_spans[].source_ref.id` | `source-support` |
| `source_spans[].source_ref.path` | `source-support` |
| `source_spans[].source_ref.revision` | `source-support` |
| `source_spans[].source_snapshot_ref` | `source-support` |
| `source_spans[].source_snapshot_ref.id` | `source-support` |
| `source_spans[].source_snapshot_ref.path` | `source-support` |
| `source_spans[].source_snapshot_ref.revision` | `source-support` |
| `source_spans[].span_id` | `source-support` |
| `source_support_status` | `source-support` |
| `subject_ref` | `source-support` |
| `subject_ref.id` | `source-support` |
| `subject_ref.path` | `source-support` |
| `subject_ref.record_type` | `source-support` |
| `subject_ref.revision` | `source-support` |

Container and element memberships remain distinct; nested id/path/revision
belong to their referenced constructs, not the root support record. Accepted
root record identity and locator fields are context, not new memberships.
Exclude all other support fields (including assessments, prepared_source_refs,
actor/run, validation/verification, preservation, reconciliation and admission),
and all memberships in claim/card/edge/CQ records. source_support_status is
included only as the observed assertion-to-span relation label; do not absorb
assessment or verification-state ownership.

## Required Comparison

Read the project/arc/slice plans and ledgers, Project08 AGENTS.md, current
framework/project-management/work-verification guidance and concept-cards.
Use concept-cards' identity/reference rules, source-support template/body,
extraction and evidence-lifecycle guides, and focused validation guidance.
Read claim/edge/CQ templates only as needed to distinguish support subject
roles; their memberships remain elsewhere.

Query the frozen census for the selected paths, their values and shapes by
actual record/context. Inspect all four populated Arc07 support files and
the template, distinguishing template null/empty placeholders from populated
mappings, arrays and scalars. Explicitly inspect subject_ref's target claim
anchor, source/snapshot refs and locator-map entries where accessible. Check
identity/type/revision consistency as well as path resolution. Report apparent
mismatches and unavailable originals; do not repair or normalize the input.
A reference to a manifest is not automatically proof of immutable byte identity.

For each pair author its meaning, evidence and concrete lookup/preservation/
body consequence. Distinguish:
- support record identity, asserted subject identity and selected span identity;
- referenced source, snapshot and locator IDs/paths/revisions, including
  reference conventions versus values actually used;
- collection, selection boundaries, coordinate addresses, quoted/paraphrased
  content, interpretive context, quote policy and checksum/edition notes;
- unassessed/default status, observed candidate-supported/caveated labels,
  independent verification, evidence grade and admission.

Do not infer a closed status vocabulary from observed labels. No quotation
retained is different from missing content; a quote policy is not proof of
permission or evidence fidelity. A checksum note may be narrative or a pointer,
not the checksum itself. Do not infer globally unique span IDs or uniform
revision types without actual guidance.

Compare direct versus caveated support and text-plus-figure versus text-only
selections using named records. Relate broader locator ranges to narrower
selected spans without assuming their difference is an error. Preserve
qualifications, omissions and inaccessible dependencies. Inspect method claims
against the source-support body and recorded evidence, not the textbook anew:
no new scientific/semantic support verdict is authorized.

Use a bounded historical comparison, reusing Slice07's registered music/OTP
cards and historical Provenance/Source Reference/Verification Notes guidance
where relevant. Explain what body citations and legacy metadata can carry
versus what these explicit subject/span links add or leave unresolved. Do not
claim historical absence or current query equivalence from template shape.
Use synthetic claim/relationship/CQ examples where relevant to the general
support-subject contract; name absent populated evidence. Register every input,
section, role and hash on which a conclusion depends.

## Artifacts And Verification

CC writes four artifacts under artifacts/:
- semantic-membership.json: exactly 27 pairs, field/context-specific meanings,
  dispositions, linked evidence IDs and input path/section/hash/role records.
- semantic-evidence.md: inspected examples, historical/current comparisons,
  operational consequences, unresolved limits and attribution of prior evidence.
- validation-evidence.md: literal executed queries/checks and actual results.
- handoff.md: remaining questions, boundaries and concrete integration/sizing
  consequences. No acceptance through generic preservation slogans.

Independently derive expected pairs from this table, assert exact equality,
uniqueness, frozen inclusion and disjointness from Batch01/Slice06/Slice07.
Resolve both meaning/member evidence layers; inspect content beyond presence.
Run every documented command literally, including census/context comparisons,
all registered hashes and declared target checks. Pin both endpoints of
historical preservation checks, distinguish present-state checks, and preserve
the source, corpus and prior Slice01/04/06/07 packets unchanged.

No new helper is anticipated. Use existing tools/parsers; no Ruby/Python,
source edits, schema implementation, package/install, extraction, runtime,
memory admission or prior-packet repair. Raise a concrete sizing/scope issue
before expanding work; do not substitute a proposal for the assigned evidence.

CC closes with an individual S8-1 through S8-7 attestation, artifact inventory
and scope-as-specified/delivered bubble-up. CDC independently verifies.
After Slice07, 67 pairs are accepted, 27 assigned here, and 461 remain
(209 original Slice04, 252 original Slice05). The old allocation is accounting
only. Slice04/01, Arc01 and the project remain open; P-14 and research gates
are untouched.

## Version History

- 1.2 (2026-09-13): CDC independently closes all seven unchanged criteria
  after 3436020a. Reference limitations are findings, not repaired input or
  verified claims. The CDC record supplies a pinned historical replay;
  CC's four semantic artifacts and closing report remain unchanged.

- 1.1 (2026-09-13): Initial CDC review retains three reproduced criteria
  and opens Iteration 01 for target agreement, contextual dispositions and
  replay corrections. Original acceptance and scope boundaries are unchanged.

- 1.0 (2026-09-13): Opens the 27-pair source-support subject/span comparison
  after Slice07 closure, retaining the remaining semantics and parent gates.
