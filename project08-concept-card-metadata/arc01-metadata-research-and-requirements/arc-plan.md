---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
status: active
version: "1.21"
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
| `slice06-record-identity-and-classification` | Record identity/revision for non-card records, record-type labels, legacy category/subcategory/tier: 37 exact observed pairs | Accepted Slice04 Batch01 plus frozen Slice01 inventory; not Slice04 closure | CDC closed after e88e6c0b plus attributed census replay completion |
| `slice07-source-identity-and-locator-semantics` | Seven legacy source fields and thirteen source-locator fields: 20 exact pairs | Frozen inventory, accepted Batch01 and Slice06; not Slice04 closure | CDC closed after f82d0524 |
| `slice08-source-support-subjects-and-spans` | Assertion subject, selected source spans and support-status semantics: 27 exact source-support pairs | Frozen inventory and accepted Batch01/Slice06/Slice07; not Slice04 closure | CDC closed after 3436020a; unresolved target components retained |
| `slice09-claim-and-card-linkage-semantics` | Claim assertion/card linkage and card claim/source/support references: 21 exact pairs | Frozen inventory and accepted Batch01/Slice06/Slice07/Slice08; not Slice04 closure | Five criteria reproduced; Iteration 02 for residual S9-R1/R2 evidence |
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

Current Slice09 review (2026-09-13), `0aeaf507`: five criteria reproduced;
R3 and substantive component/target comparisons accepted. Iteration 02
completes only remaining S9-R1/R2 manifest registration and inspection/
preservation replay. Was: broad Iteration 01 correction. No next slice opens;
94 accepted / 21 assigned / 440 others and all parent/research/P-14 gates stand.
Earlier review passages below are historical.

Earlier Slice09 review (2026-09-13), `6eb034a1`: exact 21-pair coverage
and scoped preservation pass. Literal replay/census, target and baseline
mapping evidence, and effective component meanings require S9-R1/R2/R3
corrections in Slice09 artifacts/iteration-01-cc-prompt.md. Was: initial
execution. No next slice opens; 94 accepted / 21 assigned / 440 other pairs,
parent composition, research and P-14 gates remain unchanged. The following
opening/review passages are historical, not a superseding assignment.

Current (2026-09-13): Slice08 `3436020a` is independently CDC-closed
against all seven unchanged criteria. Its 27 field-specific meanings preserve
observed heading/table-row lookup separately from unresolved literal fragments,
embedded-claim/locator revisions and source-record declarations. This accepts
the analysis, not those references as fully resolved or the claims as verified.
Was: Slice08 Iteration 01 pending.

Open sibling Slice09 for 21 exact claim/card assertion and source/support
linkage pairs. The frozen census exposes a claim template but no populated
standalone claim root, alongside cards with empty, absent, populated and
alternate source-snapshot representations. Compare those contexts explicitly;
do not manufacture missing standalone evidence or infer support from membership
in a card's lists. Keep preparation, graph/CQ and lifecycle fields outside
this unit. After 94 accepted and 21 assigned pairs, 440 remain: 188 original
Slice04 and 252 original Slice05. Old ownership labels remain accounting only.
Slice04 integration, Slice05 remaining semantics/final replay, Slice01 closure,
research gates and P-14 remain required. Size the next remainder after Slice09.
Earlier review/opening paragraphs below are historical, not current routes.

Earlier Slice08 review (2026-09-13), `2dfe5577`: exact coverage, bounded
selection/status comparisons and scoped preservation pass. Target agreement,
historical/contextual consequences and full replay require S8-R1/R2/R3
corrections in `artifacts/iteration-01-cc-prompt.md`. Was: initial execution.
No next slice opens; 67 accepted / 27 assigned / 461 other pairs, all parent
and research gates and P-14 remain unchanged. Earlier opening basis follows.

Current (2026-09-13): Slice07 `f82d0524` is independently CDC-closed on
all seven unchanged criteria. Its source/locator and historical directory,
header/null and fallback distinctions are accepted within the recorded
evidence bounds. Was: Slice07 Iteration 03 pending.

Open sibling Slice08 for 27 exact source-support subject/span/status pairs.
Its five frozen root records and focused guidance/examples form a coherent
comparison with review headroom. Claim, graph/CQ, actor/run, preparation and
assessment/lifecycle memberships remain outside this unit. After 67 accepted
pairs and 27 assigned to Slice08, 461 remain: 209 original Slice04 and 252
original Slice05. Those allocation labels are accounting, not endorsement of
the old semantic map. Slice04 retains full integration; Slice05 retains its
remaining semantics/final replay. Slice01, research gates and P-14 remain
unchanged. Size further remainder work after Slice08 evidence.
Earlier review and execution passages below are historical, not current routes.

Earlier Slice07 review (2026-09-13), `e99fddbb`: five rows reproduced;
S7-R3 resolved and current locator meanings accepted. Only historical
directory/header/null conventions and source-family comparison remain under
`artifacts/iteration-03-cc-prompt.md`. Was: broad Iteration 02 repair.
No next slice opens until this comparison closes. Pair accounting, original
criteria, parent gates and P-14 are unchanged. Earlier review follows.

Earlier Slice07 review (2026-09-13), `d077bbe8`: contextual prose improves,
but the unchanged registry and incomplete evidence/replay keep all three
findings open. Follow Slice07 `artifacts/iteration-02-cc-prompt.md`.
Was: Iteration 01. Two reproduced rows stand; no new remainder slice opens.
Pair accounting, parent gates and P-14 are unchanged. Prior review follows.

Initial Slice07 review (2026-09-13), `d8a3a6c0`: exact twenty-pair coverage
and preservation pass independently. Per-field meanings, required contextual
comparisons and complete replay/closeout remain open. Follow Slice07
`artifacts/iteration-01-cc-prompt.md` and `cdc-verification.md`.
Was: initial CC execution. No next remainder slice opens before correction
review; the 47 accepted / 20 assigned / 488 other pairs and all composition
gates remain unchanged. Earlier Slice06/Slice07 opening text below records
the allocation basis, not a superseding execution assignment.

Operator addition (2026-09-13): Slice03's trial requirements must include
Project08's Complete Musician same-chapter track (P-14), using the exact
prepared-Markdown and historical-card roots recorded in the project plan.
Specify frozen chapter/baseline selection, predeclared source-grounded measures,
fresh repeated extraction, bias-controlled independent comparison, metadata/
query checks, historical confounds and refinement/rerun decisions. Arc04
executes it when the profile is ready. This adds a trial requirement, not
source/extraction work to Slice07 or a shortcut past inventory/research gates.

Current (2026-09-13): Slice06's seven rows are CDC-closed after `e88e6c0b`.
CDC added and ran an explicitly attributed literal census command; CC's
semantic report and registry remain unchanged. Source remains `e763c661`.
With Batch01, 47 of 555 pairs have accepted bounded contextual evidence.
This is not corpus-wide equivalence, migration or semantic source verification.

Open sibling Slice07 for twenty exact source/locator pairs drawn entirely
from the original Slice04 allocation. Its table and seven-row open set define
the boundary. Of the 508 remaining after Slice06, twenty are assigned there;
488 remain outside accepted/assigned work: 236 original Slice04 and 252
original Slice05 pairs. Original allocations are accounting, not accepted
family semantics. Actor/run/lifecycle and inline support/graph/CQ memberships
are not absorbed merely because inspected sources contain them.

Slice04 retains complete-artifact integration and its eight criteria;
Slice05 retains remaining lifecycle/provenance and final replay integration.
Size the next unit after Slice07 evidence. Slice01 and research Slice02/03
retain their existing composition gates. Was: Slice06 Iteration 02 pending.
The following review history is superseded as a current assignment.

Current Slice06 review of `a416c2a2`: S6-R1/R3/R4 are resolved; S6-R2
retains the missing per-corpus vocabulary comparison and exact supporting
inputs/replay. Follow Slice06 `artifacts/iteration-02-cc-prompt.md`.
Was: four-finding Iteration 01. Current-record semantics and structural
successes stand; no slice closes, pair changes owner, or criterion is reduced.
The following initial review is historical.

Slice06 `6a6b1661` review (2026-09-13): exact 37-pair coverage and scoped
preservation pass independently. Required contextual examples/classification
comparison, lookup-rule correction and complete durable replay remain in
Slice06 Iteration 01. Follow its `cdc-verification.md` and
`artifacts/iteration-01-cc-prompt.md`. Was: initial CC execution.
Do not size/open the next remainder unit until this correction is reviewed.
No pair changes owner, no acceptance criterion is reduced, and Slice04/01
remain open.

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

- 1.21 (2026-09-13): Slice09 Iteration 01 review accepts five criteria
  and resolves R3; opens narrow Iteration 02 for residual R1/R2 evidence
  registration/replay. No semantic scope, membership or parent/UAT change.

- 1.20 (2026-09-13): Slice09 review of 6eb034a1 retains two reproduced
  criteria and opens Iteration 01 for S9-R1/R2/R3 evidence corrections.
  Was: initial execution. No membership, source, parent or UAT scope change.

- 1.19 (2026-09-13): Closes Slice08 after independent 3436020a review
  resolves S8-R1/R2/R3. Opens bounded 21-pair Slice09 with 94 accepted and
  440 other pairs. Preserves target limitations and all parent/UAT obligations;
  was: Slice08 correction pending, not a schema or reference repair.

- 1.18 (2026-09-13): Slice08 review of 2dfe5577 retains three reproduced
  criteria and opens Iteration 01 for S8-R1/R2/R3. Records required evidence
  correction only; no target repair, allocation, parent or UAT scope change.

- 1.17 (2026-09-13): Closes Slice07 after independent f82d0524 review and
  opens 27-pair Slice08 for source-support subjects/spans. Records 67 accepted,
  27 assigned and 461 remaining without reducing parent or UAT requirements.

- 1.16 (2026-09-13): Slice07 Iteration 02 review of e99fddbb accepts five
  criteria and resolves S7-R3. Opens narrowly scoped Iteration 03 for historical
  conventions and source-family comparison under S7-R1/R2, without scope loss.

- 1.15 (2026-09-13): Slice07 Iteration 01 review of d077bbe8 accepts partial
  prose improvements but keeps S7-R1/R2/R3 open in Iteration 02. No scope,
  allocation, acceptance or parent/UAT requirement change.

- 1.14 (2026-09-13): Slice07 CDC review of d8a3a6c0 requires S7-R1/R2/R3
  correction within the unchanged slice. Retains mechanical/preservation
  successes, P-14 trial requirement and all parent/remainder obligations.

- 1.13 (2026-09-13): Operator's same-chapter Complete Musician comparison
  adds P-14 to Slice03's UAT design/handoff obligations. Execution remains
  Arc04; existing Slice07 scope and remediation/research dependencies unchanged.

- 1.12 (2026-09-13): CDC closes Slice06 after its classification evidence
  and an attributed replay-documentation completion. Opens twenty-pair
  Slice07, preserving the other 488 pairs and original parent criteria.
  Was: Slice06 Iteration 02 pending; no semantic allocation endorsement.

- 1.11 (2026-09-13): Slice06 Iteration 01 CDC accepts current-record
  evidence, lookup correction and original replay repair. Iteration 02
  completes only remaining S6-R2 classification evidence. No roadmap scope,
  ownership or composition-gate change.

- 1.10 (2026-09-13): Slice06 initial CDC review accepts mechanical coverage
  and preservation but requires S6-R1 through S6-R4 corrections in the same
  slice. Was: open for initial CC execution. Remainder ownership, research
  gates and original composition obligations are unchanged.

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
