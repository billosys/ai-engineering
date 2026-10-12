---
project: project10-design-foundations
status: active
depends-on: [project09-design-audit]
blocks: [project11-unified-design-practice]
related: [project08-concept-card-metadata, project13-collab-refinements]
---

# Design Foundations — 1.5 Target

## Purpose and authority

Deliver a corrected, portable `visual-design-system` skill and usable installed
package, preserving relationships, content-led composition, intrinsic layout
and expressive craft. Project10 repairs the existing tool; Project11 owns the
broader design-practice expansion. Planning belongs here on `planning`;
source and package changes belong in the main checkout.

Plan revision **1.46**, authorized by the Operator on 2026-10-12: reduce project
complexity and workload, and shorten the distance between finding an issue and
fixing the source. Arc02/Slices01–05 exposed an evidence-heavy sequence with no
live implementation. This amendment replaces that sequence with end-to-end
review, correction and validation batches. It changes execution and ownership,
not the agreed corpus or release obligations.

Use the shared Project09 [audit](../project09-design-audit/artifacts/audit-results-design.md)
and [synthesis](../project09-design-audit/artifacts/audit-modernization-synthesis.md).
Reuse accepted Arc01/02 evidence at its verified scope; do not regenerate it to
fit a new reporting format. Historical plans, issued prompts and acceptance
records remain evidence. Earlier roadmap and status prose is superseded by this
revision; the previous complete plan remains in Git history.

## Scope and definition of done

The deliverable has portable defaults, supported and appropriately scoped
principles, consistent calculations/examples, usable accessibility/typesetting
procedures, readable card metadata, reliable routes and runnable snippets.
Every DES-001–016 finding receives a checked disposition at the changed revision.
All eight live design files and all 233 baseline cards receive complete review.
The [project ledger](ledger.md) retains all thirteen criteria and their states.
No source fix, semantic acceptance or release is claimed by this plan amendment.

Preserve source originals under `knowledge/design/sources/`, including the
`sources/md/` convention. Do not rewrite historical records, invent card fields,
redesign Project08's schema, or expand into Project11's broader practice.

### Full-corpus review contract

Read every card's complete teaching body, examples, technical mappings,
relationships, prerequisites and competency questions. Review all five dimensions:

1. Source fidelity, including context, qualifications and attribution.
2. Mathematical, technical and domain correctness, distinct from a source's
   historical position.
3. Scope: general principle, contextual advice, historical account or added
   inference/analogy, with appropriate support.
4. Internal and cross-card/guide consistency, retaining legitimate differences.
5. Relationship support/direction, prerequisites and actual question coverage.

Reuse the accepted 233-card manifest, raw index and source/locator records.
Reconcile every addition, split, merge or removal to that baseline. Full reads
and all five outcomes remain explicit per card; claim-level evidence is required
where a summary would hide an unsupported, conflicting, changed or blocked
claim. Sound claims can share a precise source-span assessment when its coverage
is explicit. Do not manufacture five separate records for every markup line.

Correct or qualify supported defects during the same batch. Preserve reasons
and before/after revisions, review revised cards and check affected downstream
claims and relationships. Record source gaps separately from technical outcomes.
Sampling, format-only checks, live-guidance-only review and quarantine cannot
satisfy full-corpus completion. Missing originals still block dependent fidelity
results and full-corpus/release acceptance; they do not block unrelated fixes.

## Arc roadmap

There are **three remaining arcs**, rather than five. IDs and existing paths
stay stable; numerical order does not imply a dependency barrier.

| Arc | Delivery and current state | Actual prerequisites |
|---|---|---|
| [Arc01 — portable contract](arc01-portable-contract/arc-plan.md) | Closed; accepted contract, baseline and explicit source-readiness carryover | Operator composition acceptance at `38b66d0d` |
| [Arc02 — review and fix](arc02-theory-and-evidence/arc-plan.md) | Active; apply accepted corrections, remove C&B coupling, review/fix cards and guides, and implement/test the accessibility/typesetting floor | Accepted contract and evidence for each changed claim; originals only for dependent fidelity checks |
| [Arc06 — metadata and rendering](arc06-card-metadata-and-rendering/arc-plan.md) | Queued, independently ready; select contract, pilot and normalize all existing metadata, then prove GitHub rendering | Accepted mapping and pilot before bulk changes; no book-original dependency |
| Arc04 — package and release readiness (`arc04-guides-and-package`) | Plan near execution; complete routes/snippets, isolated package, final specimens and Project11 handoff | Accepted input revisions for each task; full Arc02/06 completion and Project09 acceptance before release |

**Was:** a separate Arc03 accessibility/typesetting phase and Arc05 final
validation phase. **Now:** Arc03's entire delivery and browser-proof obligations
belong to Arc02; Arc05's entire composition, final validation and release-readiness
obligations belong to Arc04. Neither arc had a detailed plan or issued slice.
Do not create those two planning trees. Their work is reassigned, not accepted
or dropped. Arc04 no longer waits for full Arc02 closure to begin useful package
work; its final acceptance still does.

| Finding ownership after consolidation | Findings | Closure evidence |
|---|---|---|
| Arc02 | DES-001–009, DES-011–013, DES-015–016 | Corrected source, complete review/support, relevant numerical/browser checks and cross-file reconciliation |
| Arc04 | DES-010, DES-014 | Usable installed routes/examples and brief → guidance → choice → review demonstration |
| Arc04 final composition | All DES-001–016; P10-01–13 | Complete final package, finding/corpus accounting, independent review and Operator release-readiness acceptance |
| Arc06 | P10-12/13 metadata/rendering; coordinate DES-016 with Arc02 | No-loss field normalization, preserved bodies and actual final-revision GitHub views |

This table supersedes owners in the historical Arc01 allocation; retain that
artifact unchanged. Accessibility findings DES-005/006/009/011 retain actual
behavior checks, not merely revised prose. Arc02 owns substantive body repairs;
Arc06 owns lossless representation. Arc04 checks package preservation and final
revision applicability for both.

## Immediate sequence and working method

1. Slice05 Iteration02 is independently closed under its original contract.
   Preserve its evidence and remaining configuration/runtime follow-up in Arc02.
2. Execute [Arc02/Slice06](arc02-theory-and-evidence/slice06-colour-pipeline-source-fixes/slice-plan.md):
   correct three live colour-pipeline assertions using accepted Slice02 evidence,
   update the skill history and check the package in that same slice. Resolve
   remaining fluid-scale configuration choices before their later mutation batch.
3. Remove C&B coupling in a bounded source batch using the accepted portable
   contract. Then take the next ready content cohort or Arc06 normalization
   batch according to evidence, dependencies and context headroom. Original-input
   blockers do not impose an all-project wait.
4. Continue complete card/guide review in coherent source/topic cohorts, fixing
   supported defects and checking dependent claims in each slice. Add the
   accessibility/typesetting procedures and browser checks where they are used.
   Plan only the next executable batch, not a tree for every review dimension.
5. Build and inspect the package once useful corrected inputs are accepted;
   reserve Arc04's final pass for composition, remaining gaps and release gates.

A new content slice normally delivers **read → decide → edit → check → review**.
Evidence-only work is exceptional: a missing input or genuinely unresolved
question must prevent a responsible edit. State that reason and its next action.
A batch finding that is safe and in scope is fixed before that batch returns;
cross-batch or uncertain findings retain an owner and next ready assignment.
Do not create another analysis/handoff slice solely to pass an already-resolved
correction to a later implementation phase.

## Evidence and workload economy

Use the existing canonical plans, ledgers, preserved prompts and review records.
For new slices, prefer one compact supporting batch record for coverage,
exceptions, before/after pointers, validation and unresolved work. Create another
artifact only when it serves a distinct deliverable or reproducible check.
The source diff and usable result are primary outputs, not a new evidence packet.
Existing issued output contracts remain binding.

Use result-oriented acceptance rows; avoid separate closure criteria for routine
receipt formatting. Record required intake and provenance concisely. Keep failed,
blocked and unrun checks visible. Do not require receipt-only commit chains,
copied historical datasets, repeated whole-project narratives or bespoke checker
frameworks for each slice. Reuse existing checks; write a maintained helper only
when repeated transformations or a consequential failure need one. Meaningful
negative controls remain necessary for claimed transformation/validator safety.

Independent review covers the delivered source, scope, substantive evidence and
affected dependencies in one pass. Reuse unchanged accepted evidence with an
explicit applicability check; rerun changed/affected checks. Preserve history and
correctness while avoiding cosmetic-only handoff cycles. Parent plans receive
material scope/ownership/sequence changes and child closure links, not a fresh
copy of every iteration's counts. These are Project10 execution choices, not a
general framework change or an extension of Project13's completed trial.

## Recorded Operator decisions

The 2026-10-08 decisions remain binding: remove C&B-specific material from the
live skill/package, retain it only in Git history, and treat the coupling as a
bug requiring no compatibility bridge. Preserve portable method and supplied
project identity. Review all 233 cards across the agreed five dimensions and use
`sources/md/`. The 2026-10-12 amendment authorizes the reduced execution structure
and earlier fixes; it does not waive these deliverables.

## Operator deferral — 2026-10-09

S02-08/A01-02 remain Operator-deferred, not done. Arc02 CDC and the Operator own
[P10-11 input re-entry](arc01-portable-contract/slice02-source-and-review-readiness/artifacts/source-input-actions.md):
exact Arnheim/Cleland/Tschichold editions/page bases, Butterick/article captures,
conversion lineage and adequate original/prepared completeness/fidelity evidence.
Each dependent result needs sufficient inputs; unrelated work may proceed.
Acquisition/conversion needs an exact separately authorized input/output scope.
Do not call the complete corpus or release verified while this work is unresolved.

## Planning choices and dependent implementation

The accepted [Arc01 composed contract](arc01-portable-contract/slice03-contract-composition-and-handoff/artifacts/composed-contract.md)
and diagnostic example are inputs, not adopted live teaching. New source
assignments pin the current main revision, inspect drift, name exact mutation
paths and settle consequential choices before handoff. Preserve old/new locator
bridges and assess which prior evidence still applies after edits.

## Operator metadata and rendering addition — 2026-10-10

Normalize existing fields only; never invent absent IDs, facts, null/default
placeholders or review states. Use the historical 3.2 definitions unless Project08
has an explicitly accepted unified replacement at contract selection. A skill
release number is not a schema version. Preserve extensions, typed values,
null/empty distinctions, list order and bodies. Arc06 uses an accepted contract
and representative pilot before bulk mutation and must demonstrate actual
GitHub rendering for the complete reconciled population. Its former four-stage
sequence is replaced by the combined batches in its current arc plan.

## Operator methodology pilot — 2026-10-10

Project13's two-run pilot is complete at `dc7b0732`; comparative benefit was
inconclusive. Preserve its records and earlier trial assignments. No third run,
new measurement project or general framework adoption follows from this amendment.

## Workflow and acceptance

CDC Sofie plans and independently reviews separate CC execution, with Operator
relay: Two-Contributor Workflow, no CRC. Expedited Mode remains enabled. Preserve
issued prompts and existing acceptance scopes. Slice05's current return is
accepted by its independent record. Independent slice reviews use
`cdc-verification.md`. Reviewer-authored source repairs need another verifier.

Prepare a complete source-scoped slice open set and author-readiness check before
mutation; Operator relay/acceptance of that prompt remains the implementation
handoff. Commit explicit assigned paths with both required trailers. Close and
advance when evidence permits. Missing inputs stop dependent claims, not unrelated
slices or package preparation. Arc/project composition and Operator gates remain.

Run applicable source/version/package checks from main, beginning with `make help`:
`make check-skills`, `make check-skill-versions`, `make check-package-paths` and
fresh `make design` as relevant. Test actual retained examples in named browser
conditions; local parsing is not GitHub rendering or accessibility conformance.
Final release readiness requires all thirteen project criteria, complete corpus
coverage, accepted Project09 input and independently checked final composition.
Hand Project11 the accepted source/package revisions and explicit limitations.
Publication remains a separate Operator decision.

## Current status

Arc01 is Operator-accepted and closed. Arc02/Slices01–05 are independently
closed for bounded evidence; Slice05 I2 at `8d0a10c2`/`9541e4cf` closes all nine
child criteria. Slice06 is open for actual colour-pipeline source corrections;
no live change is claimed before its execution/review. Arc06 is queued with no
prompt issued. Arc04 is a roadmap entry, not an opened arc. P10-01 remains done;
P10-02–13 open. Full-corpus, source-readiness and release gates remain.

## Version History

- 1.46 (2026-10-12): Independently accepted Slice05 I2 and closed its nine
  criteria; opened Arc02/Slice06 for the first actual live colour-pipeline fixes.
  Reuse accepted proof and retain endpoint/attribution/runtime work in Arc02.
  Execution amendment and all parent/corpus/release criteria are unchanged.

- 1.45 (2026-10-12): Operator requested less complexity/workload and earlier
  fixes after Arc02/Slices01–05 exposed a long evidence-to-implementation delay.
  Consolidated Arc03 into Arc02 and Arc05 into Arc04; introduced end-to-end
  review/fix batches, combined metadata stages and compact evidence reuse.
  Preserved all corpus, finding, source-fidelity, rendering and release criteria,
  issued assignments, accepted evidence and completed Project13 trial.

- 1.44 (2026-10-12): Slice05 I1 review accepts four rows and issues I2 for five
  open; recorded external SOURCE movement, protected valid model/primary evidence.
  Scope/parent criteria/readiness/later gates remain unchanged.

- 1.43 (2026-10-12): Arc02/Slice05 initial CDC review accepts S05-03/08 and
  issues I1 for seven open rows; full scope/parent gates preserved, no advancement.

- 1.42 (2026-10-12): Arc02/Slice05 opened after Slice04 closure and completed
  Project13 two-run comparison; retained DES-005 technical/model concern with
  actual behavior later. Ordinary work, no trial extension or scope/gate change.

- 1.41 (2026-10-12): Arc02/Slice04 C4/H4/H4b independently closed, all nine
  child criteria done; bounded handoff accepted, full scope/parent/later gates
  retained. T02 final comparison due before any trial extension.

- 1.40 (2026-10-12): Slice04 C3/H3 original warrants accepted; six done/
  three open. Four-path Iteration04 addresses heading, competing registries,
  regressed guards and intake. Scope/criteria/readiness/later gates unchanged.

- 1.39 (2026-10-12): Arc02/Slice04 C2/H2 primary comparison accepted, five
  done/four open; bounded Iteration03 issued for residual warrants, literal
  joins, actual control routes and reporting. Parent criteria/scope/gates retained.

- 1.38 (2026-10-11): Slice04 C1/H1 independently reviewed, four done/five
  open; bounded Iteration02 issued after exercised recurrence repair. Parent
  criteria/full corpus/families/readiness and release gates unchanged.

- 1.37 (2026-10-11): Slice04 initial independent review accepts preservation
  only (one done/eight open); consolidated Iteration01 issued, T02 initial
  observations recorded. No parent criterion, corpus or gate change.

- 1.36 (2026-10-11): Opened next ready Arc02/Slice04 under Expedited Mode after
  Slice03 closure and completed T01 checkpoint; prospectively registered T02.
  Complete bounded context/semantic contract; all parent/input/release gates retained.

- 1.35 (2026-10-11): Arc02/Slice03 Iteration04 at3817d83c independently accepted;
  all nine child rows done and slice closed. T01 checkpoint precedes next trial
  issue; full project scope and later gates remain unchanged.


- 1.34 (2026-10-11): Arc02/Slice03 c51a21ad reviewed; eight done/one reporting
  row open. Issued reporting-only Iteration04; substantive evidence, full scope,
  independence, T01 checkpoint and later gates retained.


- 1.33 (2026-10-11): Arc02/Slice03c2f36b62 reviewed; six done/three open.
  Issued focused Iteration03; accepted coverage/actions/checker retained.
  T01 observations updated; no population, source, parent or release gate change.

- 1.32 (2026-10-10): Arc02/Slice03 Iteration01 reviewed at578e68f8; three done/six
  open retained, Iteration02 issued. T01 persistence/new-discovery observations
  recorded; full scope, parent criteria and all gates unchanged.


- 1.31 (2026-10-10): Arc02/Slice03 initial return reviewed at `2eee292c`;
  three child rows done/six open, Iteration01 issued. First T01 observations
  recorded; parent criteria, full populations and all later gates retained.

- 1.30 (2026-10-10): Opened Arc02/Slice03 token-system evidence after Slice02
  closure; registered Project13 T01 under current protocol revision 2 before
  issue. Full parent scope/criteria, source gates and queued Arc06 are retained.

- 1.29 (2026-10-10): Arc02/Slice02 I04 candidate19dd5385 independently
  reviewed; six independently done, then Operator approved direct two-field
  CDC repair and actual slice closure. Nine child rows done; I05 unused.
  Next-slice preparation retains full scope, readiness and trial gates.


- 1.28 (2026-10-10): Operator-requested Project13 case study and prospective
  two-slice methodology trial, with meta-review checkpoints. Added scoped local
  instructions; current Slice02 assignment, all criteria and quality gates retained.

- 1.27 (2026-10-10): Slice02 Iteration03 reviewed at `6a016960`; intake accepted,
  four done/five open. Issued five-output Iteration04; numeric evidence protected.
  All project criteria/gates and queued Arc06 addition retained.

- 1.26 (2026-10-10): Operator adds Arc06 metadata harmony/GitHub rendering and
  P10-12/13. Uses historical 3.2 fallback while Project08 design is unadopted;
  forbids missing-field population and preserves all prior scope/gates. Arc06
  is queued before package freeze; current Arc02 handoff remains active.

- 1.25 (2026-10-10): Arc02/Slice02 Iteration02 reviewed at `590b263c`; three child
  rows done/six open. Issued bounded Iteration03; all project criteria/gates retained.

- 1.24 (2026-10-10): Arc02/Slice02 Iteration01 reviewed at `73c8180b`; complete
  stage numerics accepted, three child rows done/six open. Iteration02 issued
  for residual literal evidence/replay/portability defects; all project gates retained.

- 1.23 (2026-10-10): Recorded partial Arc02/Slice02 review and Iteration01;
  two child rows done/seven open, no higher criterion or readiness gate closed.

- 1.22 (2026-10-09): Opened Arc02/Slice02 colour-pipeline evidence automatically
  after independent Slice01 closure. Full corpus, source readiness, live fixes,
  package and release scope/gates remain unchanged.

- 1.21 (2026-10-09): Arc02/Slice01 c3d68d7d independently closed; bounded
  arithmetic/occurrence/handoff evidence accepted, A02-01 done. Next T-family
  preparation retains complete corpus/input/live/release and Operator gates.

- 1.20 (2026-10-09): Operator-accepted Arc01 close surfaced Arc02 opening;
  detailed full theory/evidence roadmap and issued its bounded arithmetic
  Slice01 under Expedited Mode. No original/source mutation or semantic waiver.

- 1.19 (2026-10-09): Arc01 Operator composition gate accepted at `38b66d0d`;
  closed the arc, accepted P10-01 planning authority and advanced preparation to
  Arc02 under Expedited Mode. P10-11/full-corpus/live/release obligations unchanged.

- 1.18 (2026-10-09): Arc01 final-child closure surfaced formal composition;
  linked the assembled report and pending independent/Operator gate. Existing
  P10-11 deferral ownership and all release criteria remain unchanged.

- 1.17 (2026-10-09): Slice03 iteration02 `0b55afd5` independently accepted;
  all nine rows done and child closed. All three Arc01 children now closed; formal arc
  composition/gate next, while Operator-deferred readiness and release scope remain.

- 1.16 (2026-10-09): Slice03 iteration01 `ee7b8757` accepted for corrected
  handoff rows; seven done/two receipt rows open. Issued iteration02 for F05;
  source readiness, scope and higher-scale/release gates unchanged.

- 1.15 (2026-10-09): Slice03 initial `c58c89e` independently accepted for five
  planning rows; issued iteration01 for four evidence/handoff rows. Arc01 stays
  active; no scope, source, composition or release gate changed.

- 1.14 (2026-10-09): Opened Arc01/Slice03 after Operator-deferred Slice02
  closure `8e0be8d2`; selected bounded planning choices and full gated allocation.
  P10-11/source-fidelity, independent composition and release gates remain.

- 1.13 (2026-10-09): Operator deferred Slice02 S02-08 and ordered Slice03.
  Closed the child with explicit carryover to Arc02/P10-11; superseded only the
  former Slice03 sequencing gate. Full-corpus/release evidence obligations remain.

- 1.12 (2026-10-09): Accepted Slice02 iteration04 `759ce2dd` for the remaining
  local criteria; eight rows done, S02-08 alone input-blocked. Recorded source
  intake as the next dependency, without source authority or Slice03 advance.

- 1.11 (2026-10-09): Reviewed Slice02 iteration03 `80813b2e`; independently
  accepted S02-03/05/06 and issued bounded iteration04 for remaining joins,
  roles and receipts/checker evidence. Original readiness and release gates stay open.

- 1.10 (2026-10-09): Reviewed partial Slice02 iteration02 `bf02e970`; issued
  iteration03 for passage-specific clause evidence, intended targets/completeness
  and committed checker replay. Retained original-readiness and release gates.

- 1.9 (2026-10-09): Reviewed partial Slice02 iteration01 `1c0c8acf`; issued
  iteration02 for all 46 post-card passages and remaining evidence-log gaps.
  Original readiness and independent/release gates remain open; scope unchanged.
- 1.8 (2026-10-09): Reviewed partial Slice02 candidate `db48d863` and issued
  iteration01 for evidence corrections and the complete Butterick passage batch.
  Remaining post-card reads and original readiness stay binding; scope unchanged.
- 1.7 (2026-10-09): Operator enabled Expedited Mode for remaining Project10 work;
  opened Arc01/Slice02 with a bounded source/locator and review-method assignment.
  Two-contributor authority, full-corpus scope and independent/source gates remain.
- 1.6 (2026-10-09): Arc01/Slice01 closed on independently accepted iteration02
  candidate `9cc20338`; recorded progress without closing project release gates
  or changing source/semantic scope. Slice02 remains planned.
- 1.5 (2026-10-09): Arc01/Slice01 iteration01 review resolved the initial defects;
  recorded bounded iteration02 report/link corrections without changing project
  scope, corpus review or downstream source requirements.
- 1.4 (2026-10-09): Recorded independent Slice01 review and iteration01 handoff;
  no project scope or design decision changed.
- 1.3 (2026-10-09): Operator opened Arc01 and Slice01. Issued the bounded
  contract/inventory prompt with exact outputs, source-gap handling, contrasting
  checks, file scope and source-grounded author readiness. Full corpus semantics
  and source implementation remain subsequent work.
- 1.2 (2026-10-08): Operator required full semantic review/reconciliation of all
  233 cards and rejected narrower completion as a defect. Recorded review dimensions,
  coverage/source-gap rules and the `sources/md/` convention; expanded Arc01/02
  and the project ledger without claiming any semantic review completed.
- 1.1 (2026-10-08): Operator selected removal of C&B material with Git-only
  historical retention and classified the original coupling as a bug requiring
  no compatibility bridge. Corpus scope remains undecided pending clarification.
- 1.0 (2026-10-08): Established Project10 for the 1.5 foundation repair;
  linked the Project09 audit, mapped all findings, and recorded provisional
  arcs, explicit scope decisions, verification and Project11 handoff requirements.
