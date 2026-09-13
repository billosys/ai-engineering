---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
status: active
version: "1.9"
---

# Metadata Research And Requirements

Establish what the historical cards and prompts enabled, what the current skill
represents or loses, and what a general, queryable profile must preserve. Ground
the architecture handoff in actual artifacts and primary-source research.

Consumes the Project08 operator brief, current source skills, historical prompts
and card corpora, and Project05 UAT evidence. Delivers requirements and alternatives
to Arc02; no field layout or particular standard is accepted by this arc merely
because it appears in the initial hypothesis.

## Slice Breakdown

| Slice | Scope | Dependency | State |
| --- | --- | --- | --- |
| `slice01-metadata-inventory-and-research-questions` | Reproduce field/capability inventory, register baseline evidence and formulate research questions | Project brief; final closure consumes Slice04/05 repair evidence | Open pending remediation composition; original eight rows retained |
| `slice04-semantic-identity-source-and-graph-families` | Authored identity, classification, source, locator, claim/support, relationship and CQ semantics with explicit context membership | Frozen Slice01 evidence; consumes Slice06 for its assigned portion | Batch01 ten pairs accepted; remainder and final composition open |
| `slice06-record-identity-and-classification` | Record identity/revision for non-card records, record-type labels, legacy category/subcategory/tier: 37 exact observed pairs | Accepted Slice04 Batch01 plus frozen Slice01 inventory; not Slice04 closure | Open for CC |
| `slice05-semantic-lifecycle-provenance-and-replay` | Remaining lifecycle/provenance semantics, full join/coverage, parser instruction dispositions, exact inputs and literal replay; reconcile Slice01 handoff | Independently reviewed Slice04 semantic packet and Slice01 evidence | Reserved; plan after Slice04 review and sizing |
| `slice02-standards-and-source-model-research` | Primary-source research on classification, source identity/locators, typed relations, provenance and metadata profiles | Reconciled and CDC-closed Slice01, including Slice04/05 | Unopened until remediation composition passes |
| `slice03-requirements-and-acceptance-design` | No-loss requirements, migration/query fixtures and repeated-run quality criteria for architecture/UAT | Slice01/02 | Plan when near |

Add or split slices if inventory or research reveals a larger problem. A complete
inventory does not require every card body to be read in one session: parse all
available frontmatter to discover fields and value shapes, then inspect named
representative and anomalous records. Capture unavailable evidence explicitly.

Research should compare candidate standards such as SKOS, Dublin Core application
profiles, BIBFRAME and PROV-O with the practical needs of plain Markdown/YAML
cards. Examine locator approaches and domain-specific relationship predicates
separately. Keep classification broader/narrower distinct from pedagogical
prerequisites. Consult NeON or other ontology-method sources when relevant to
competency questions or requirements engineering. Seek benefits and costs, not
standards adoption for its own sake.

## Acceptance And Handoff

Current execution: Slice04 Batch01 revision `995c86d6` passes independent
semantic review within its sample scope. CDC corrected and reran only its
replay documentation; the membership registry and semantic prose are unchanged.
The ten-pair checkpoint is accepted, not the full Slice04 or Slice01.

The next unit is sibling Slice06, not another informal batch. Its 37 pairs
are explicit in its open set and all occur in the original Slice04 allocation.
Of the 555 original pairs, ten have accepted contextual evidence, 37 are
assigned to Slice06, and 508 remain outside these two units. Of those 508,
256 remain in the original Slice04 allocation and 252 in the original
Slice05 allocation. These are accounting counts, not approval of the old
misclassified ownership map. Correct later ownership by actual meaning.

Slice04 retains the source/locator, claim/support, graph/CQ and residual
contextual work plus its original complete-artifact and eight-row composition
obligations. After Slice06 review, size and open the next necessary bounded
unit for that remainder. Slice05 retains lifecycle/provenance and final replay
integration. No pair is dropped, no previous slice is falsely closed, and
no existing iteration count is reset. Slice06 depends on accepted evidence,
not Slice04 formal closure, avoiding a dependency cycle.

Previously: Slice04 Batch01 in `776c5cb1` supplies ten exact pairs
and four verified input hashes, but still lacks the required sample coverage,
resolvable meanings/evidence and executed validation record. Finish the same
checkpoint before sizing further execution; no later batch or slice is open.

At checkpoint opening, Slice04's follow-up audit report supplied no new semantic
artifact or commit. Begin with its `artifacts/iteration-01-batch01-cc-prompt.md`:
ten explicit concept-identity/label pairs, with actual contextual evidence.
This is one initial review checkpoint inside Iteration 01, not another slice,
iteration reset or reduced acceptance target. Review the resulting artifact
before sizing the remaining repair; add bounded slices if warranted rather
than concealing a multi-slice workload behind unlimited batches. The original
ledger and all 555-pair coverage requirements remain in force.

Slice04 review of `76d284f4`: CDC reproduces 303 assigned plus 252 remainder
pairs, with no missing, extra or duplicate pairs. Semantic-family assignments
are not accepted: unrelated lifecycle/locator/graph fields are grouped under
CQ coverage, and exact input/context evidence is missing. Follow Slice04's
`artifacts/iteration-01-cc-prompt.md` and `cdc-verification.md`. Slice05 stays
unopened. Correcting ownership may change the 303/252 split; complete, accurate
coverage remains mandatory. Original Slice01 criteria are unchanged.

Current: CDC accepts the two-part sizing direction in `2b26282e` with canonical
stable numeric IDs: proposed `slice01a` becomes Slice04 and `slice01b` becomes
Slice05. Existing Slice02/03 IDs are unchanged. Execution order is Slice04,
Slice05, Slice01 recomposition, Slice02, then Slice03; numeric order is not a
dependency. These are sibling remediation slices, not a new hierarchy.

The [remediation decision](./slice01-metadata-inventory-and-research-questions/artifacts/remediation-decomposition.md)
assigns every open row and residual instruction. No row is closed by splitting
it. Slice04/05 consume captured Slice01 evidence without depending on its
formal closure, so the recomposition gate introduces no dependency cycle.
Slice01 closes only after CDC verifies the combined evidence against its eight
unchanged criteria. Research cannot start merely because the new slices have
individual proposed-done reports.

The current index has 308 distinct normalized paths across 13 record-kind labels,
yielding 555 observed path/kind pairs, not 308 contextual memberships. This is a
mechanical coverage floor: corpus, role or historical/current differences may
require finer authored contexts, especially within `untyped`. No global
schema or fixed semantic-family count follows from these counts.

Size each new slice with review headroom. If evidence demands another bounded
slice, report named remaining families/criteria for a tracked amendment. Do not
reset the old iteration counter or use the split to abandon difficult meanings.

### Earlier Assessments (Historical)

At Iteration 04 opening: the focused repairs in `b5ed9dd1` pass independent assertions. R2's
semantic-family map and R4's literal portable reproduction route remain open,
as CC explicitly reports. Iteration 04 makes these the primary deliverables:
`artifacts/iteration-04-cc-prompt.md` in Slice01. Previously requested codec
library/EOF handling must be resolved or explicitly dispositioned too. Earlier
assessment paragraphs below are historical.

At Iteration 04, use a fresh executing context and size the remaining authored
analysis before doing more helper work. If it cannot fit with review headroom,
return a concrete semantic-family remainder and proposed slice split for CDC
to incorporate into this arc, preserving every project requirement. The
five-iteration limit is not permission to declare unreviewed fields done.

Current: Iteration 02 now reproduces the typed fixture and all 308 normalized
paths. Iteration 03 repairs JSON/control-character and framing classification
failures, finishes the semantic crosswalk and supplies working verification
commands. Current assignment: Slice01 `artifacts/iteration-03-cc-prompt.md`.
The earlier Iteration 01/02 assessment below is historical.

Slice01 Iteration 01 removed Ruby and corrected headline populations, but CDC
reproduction found boolean/type loss and omitted null/empty field paths. All
307 semantic dispositions still contain the same deferred-decision placeholder.
Iteration 02 repairs these failures and finishes the original crosswalk and
reproduction requirements. Current review and assignment live in Slice01
`cdc-verification.md` and `artifacts/iteration-02-cc-prompt.md`. Was:
Iteration 01 pending. Slice02 remains unopened until this evidence is corrected
and independently verified.

The [arc ledger](./ledger.md) requires both child verification and a composition
check: trace every operator concern through observed examples, research questions,
evidence and a testable requirement. Include unresolved alternatives and an Arc02
decision agenda. The later trial rubric must measure usable output, not only
template conformance. Architecture, implementation and actual extraction remain
later work, with evidence ownership recorded rather than presumed complete.

## Version History

- 1.9 (2026-09-12): Accepts Slice04 Batch01's ten-pair sample analysis,
  recording CDC's tested documentation-only replay correction. Opens sibling
  Slice06 for a bounded 37-pair subset; retains the other 508 pairs and
  original composition requirements with explicit owners. Was: same checkpoint
  incomplete. Further remainder sizing follows real output, not an unbounded
  series of batches.

- 1.8 (2026-09-12): Slice04 Batch01 review verifies pair coverage and four
  hashes, while contextual evidence and reproducibility remain incomplete.
  Keeps the same ten-pair checkpoint active. No scope or criterion changes.

- 1.7 (2026-09-12): Slice04 diagnosis-only follow-up prompts a bounded first
  identity-evidence checkpoint. Was: another whole-packet correction handoff.
  Requires concrete authored output before further sizing; no row closure,
  new hierarchy, or transfer to Slice05.

- 1.6 (2026-09-12): Slice04 CDC review finds incorrect family assignments,
  unsupported semantic claims and incomplete input/validation/row evidence
  despite exact pair coverage. Opens Slice04 Iteration 01; no new slice or
  scope reduction. Was: Slice04 open for its initial run.

- 1.5 (2026-09-12): Adopts Slice01 Iteration 04's sizing proposal as new
  sibling Slice04/05, preserving stable Slice02/03 names and all original
  requirements. Opens Slice04; reserves Slice05 and requires original Slice01
  recomposition before research. Was: all remediation within Iteration 04.
  Corrects the sizing unit to 308 paths / 555 observed path-kind pairs.

- 1.4 (2026-09-12): Slice01 Iteration 03 delivers its declared focused repair,
  while R2/R4 remain explicitly open. Opens a fresh-context Iteration 04
  centered on authored semantics and replay; records the sizing check.

- 1.3 (2026-09-12): Slice01 Iteration 02 independently reproduces the census
  and path coverage, resolving R6/R7's original data failures. Remaining
  R2/R4 and new R8/R9 require Iteration 03. Slice02 remains unopened.

- 1.2 (2026-09-12): Slice01 post-Iteration-01 CDC checks require Iteration 02:
  type preservation, complete path coverage, semantic dispositions and reconciled
  evidence. Ruby removal and deterministic runs are retained as demonstrated
  improvements. No scope reduction or advancement to Slice02.

- 1.1 (2026-09-12): Slice01 CDC findings R1-R5 require a follow-up iteration
  within the existing slice. Was: initial open set ready for CC. No slice-order
  change; research must consume corrected, complete evidence.

- 1.0 (2026-09-12): Initial three-slice hypothesis. Opens inventory first so
  research and acceptance design respond to actual field/capability gaps.
