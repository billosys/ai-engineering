---
project: project10-design-foundations
status: active
depends-on: [project09-design-audit]
blocks: [project11-unified-design-practice]
related: [project08-concept-card-metadata, project13-collab-refinements]
---

# Design Foundations — 1.5 Target

## Purpose and authority

Make `visual-design-system` trustworthy, portable and internally coherent while
preserving its compositional ethos. The Operator assigned the 1.5 effort to
Project10 on 2026-10-08. Planning lives on branch `planning`, under
`.worktrees/planning/project10-design-foundations/`; source/package work belongs
in the main checkout. The Operator opened Arc01/Slice01 on 2026-10-09 for a
bounded contract/evidence assignment, not a source rewrite or release.

The shared design input is Project09's
[release synthesis](../project09-design-audit/artifacts/audit-modernization-synthesis.md),
especially the five 1.5 workstreams. The
[audit](../project09-design-audit/artifacts/audit-results-design.md) owns DES-001–016
and the original evidence limits. Link to those records rather than copying them.
The initial source baseline is `dffa504e851b03b8e4746f1941068e4cc850b612`;
refresh it before issuing source work and pin the audit revision consumed.

## Scope and definition of done

Deliver a corrected live skill and isolated installable package: project-specific
identity separated from portable method; scoped and supported principles;
consistent numerical examples; an accessibility/typesetting floor; usable routes
and snippets; and an explicit claim/source boundary. Preserve deliberate
relationships, content-led composition, intrinsic layout and expressive craft.

Every DES finding must have a checked disposition. All claims admitted into live
guidance and the complete concept-card corpus must be reviewed; unresolved
material cannot silently become authority. Run the applicable source/version/package
gates and task demonstrations
against the composed package, with independent review and Operator acceptance.
The [ledger](ledger.md) holds those release-level criteria.

The full research-to-validation design practice belongs to Project11. This
project does not automatically redesign the concept-card schema, overwrite
historical evidence, or claim product conformance from examples. Full semantic
review and reconciliation of all 233 existing design cards is binding scope,
alongside the live skill and guides. Anything short of the agreed review is a
project defect, not an acceptable smaller interpretation of the 1.5 deliverable.

### Full-corpus review contract

For every card, read its complete teaching body, examples, technical mappings,
relationships and attributed competency questions. Identify substantive claims
and inspect the relevant original passages with enough context to assess:

1. Source fidelity, including qualifications, exceptions and attribution.
2. Mathematical, technical and domain correctness, distinguished from faithful
   reporting of a source's historical position.
3. Scope: general principle, contextual advice, historical account, or added
   analogy/inference, with the appropriate support for each.
4. Internal consistency and consistency with relevant cards and live guides,
   retaining legitimate contextual differences rather than manufacturing agreement.
5. Whether relationships, prerequisites and claimed question coverage actually
   hold and make the card useful for its stated purpose.

Preserve sound content; correct or qualify errors; remove unsupported additions
with recorded reasons; and review revised cards plus affected downstream guidance.
Track findings, source support, corrections and review outcomes at the claim level
where card-level summaries would hide partial coverage. Keep prior revisions and
the reasons for changes traceable. This does not require indiscriminate rewriting,
whole-book re-extraction, or a concept-card schema migration.

Pin a manifest of all 233 existing cards before execution. Any additions, splits,
merges or removals must map back to that baseline and appear in the final coverage
accounting; they cannot silently shrink the denominator. Sampling, format-only
checks, or checking only claims reused in the live skill cannot satisfy this scope.

Establish source availability early and obtain the necessary evidence. Missing
sources leave affected checks unresolved; absence of evidence does not establish
falsity. Record those gaps and continue independent work, but do not call the full
corpus verified or the project complete while required review remains blocked.
Quarantining unreviewed cards is not a substitute for this work. Any proposed
deferral or scope reduction returns explicitly to the Operator.

Markdown source material uses `knowledge/design/sources/md/`, with collection
subdirectories as appropriate, not `sources-md/`. The existing design tree already
uses this convention. Preserve source provenance and original files; do not infer
a bulk relocation or transformation merely from the naming clarification.

## Arc roadmap

Arc01 is closed with Operator-accepted composition and explicit source-readiness
carryover. [Arc02](arc02-theory-and-evidence/arc-plan.md) is active; detail each
remaining arc near execution. The closed
[Arc01 plan](arc01-portable-contract/arc-plan.md) supplies the slice breakdown.

| Arc | Capability | Dependencies | Audit coverage |
|---|---|---|---|
| arc01-portable-contract | Separate reusable method from adopting-project identity; specify C&B removal and the full-corpus review method, manifest and source needs | Project09 evidence intake | DES-001, DES-010, DES-013, DES-015 |
| arc02-theory-and-evidence | Correct theory and arithmetic; verify and reconcile the complete card corpus against sources and guides with claim-level evidence | Arc01 contract | DES-002–005, DES-007–009, DES-012, DES-013, DES-015, DES-016 |
| [arc06-card-metadata-and-rendering](arc06-card-metadata-and-rendering/arc-plan.md) | Harmonize existing metadata across all cards without filling missing fields; demonstrate GitHub rendering | Arc01 baseline; accepted local contract/pilot before mutation; queued | Operator addition 2026-10-10; supplements full-corpus obligations |
| arc03-accessibility-and-typesetting | Add usable accessibility obligations and transferable typography procedures | Arc01–02 decisions | DES-005, DES-006, DES-009, DES-011 |
| arc04-guides-and-package | Compose corrected guides, brief-to-review routing, runnable examples and isolated package | Arc01–03 plus Arc06 | DES-010, DES-013, DES-014; all repeated claims |
| arc05-validation-and-release-readiness | Exercise cross-context specimens, reconcile every finding and demonstrate the complete package | Arc01–04 plus Arc06; accepted Project09 baseline | DES-001–016 |

Current status: Arc01 closed by Operator composition acceptance at `38b66d0d`; Slice01 closed and Slice02 closed with eight
independently done criteria and S02-08 Operator-deferred. Local acceptance remains
`759ce2dd`/`88c1298f`; the Operator ordered Slice03 opening on 2026-10-09.
Slice03 is closed: all nine criteria independently done at `0b55afd5` with seven
prior dispositions retained after delta review; see its
[CDC acceptance](arc01-portable-contract/slice03-contract-composition-and-handoff/cdc-verification.md#iteration02-independent-verification-and-slice03-closure--2026-10-09).
All three Arc01 slices are closed; the [composition packet](arc01-portable-contract/closing-report.md)
was accepted by the Operator on 2026-10-09 (“yup, accepted!”). A01-04/05
are done; A01-02 stays deferred. Arc02 is active;
[Slice01](arc02-theory-and-evidence/slice01-fluid-scale-arithmetic/slice-plan.md)
is independently closed at `c3d68d7d` for bounded fluid-scale evidence.
[Slice02](arc02-theory-and-evidence/slice02-nonlinear-colour-pipeline/slice-plan.md)
is closed for bounded nonlinear colour-pipeline evidence and selected uniformity/
analogy claims under DES-007/002.
Slice02 is closed after independent I04 review at19dd5385 and the Operator's
explicit approval of a two-field CDC-authored repair and actual closure.
All nine child rows done; no I05 issued. [Final gate](arc02-theory-and-evidence/slice02-nonlinear-colour-pipeline/cdc-verification.md#operator-acceptance-and-slice02-closure--2026-10-10)
separates independent review, direct repair/self-check and Operator acceptance.
Queued Arc06 remains unchanged. Arc02
[Slice03](arc02-theory-and-evidence/slice03-token-system-conventions/slice-plan.md)
is independently closed for bounded token-system conventions (DES-008 and
bounded DES-002) at3817d83c; [final verification](arc02-theory-and-evidence/slice03-token-system-conventions/cdc-verification.md#iteration04-independent-review-and-slice03-closure--2026-10-11)
records all nine child rows done. Initial and four correction assignments are
preserved; Project13 T01 checkpoint is complete at370cfc8f (comparative benefit
inconclusive). T02 is registered before the next ready Slice04 initial issue. The earlier current Iteration04 pending state is
superseded by this acceptance; no source implementation is accepted.
Complete R/T/C/L/G
and original-source/full-corpus/release gates remain.
After T01 closes or reaches a recorded blocked/escalation stop, complete its
meta-review before the next trial prompt. R/T/C/L/G execution
families preserve the complete semantic scope and input re-entry. No
source-fidelity or release gate is closed.
The former “no Slice03 until source readiness acceptance” rule is superseded for
planning composition. Source readiness carries to Arc02/P10-11 before dependent
source-fidelity acceptance and full-corpus/release completion. Expedited Mode
remains enabled; no release gate or complete semantic review is accepted.
See the [CDC acceptance](arc01-portable-contract/slice01-scope-and-portability-contract/cdc-verification.md#iteration02-independent-verification-and-acceptance);
this evidence/proposal acceptance does not adopt final teaching formulations or
close any release criterion. Project09 may be consulted for planning
before its formal acceptance, with its limits visible. The accepted baseline is
required at release readiness. Coordinate any card-format/schema changes with
Project08 rather than importing its scope by association.

## Recorded Operator decisions

On 2026-10-08, the Operator resolved the C&B and compatibility questions:

- Remove the C&B-specific material from the live skill and package. Do not retain
  an opt-in C&B profile or case study; use Git history if that material is needed
  later. Preserve portable design knowledge when separating it from the branding.
- Tight C&B coupling was an original bug, not an intended feature. Removing it
  is a correction within the 1.5 effort. No compatibility bridge, legacy behavior
  or migration obligation is required for that coupling. This decision does not
  waive version/history requirements or classify unrelated changes in advance.
- The full semantic card review described above is required for all 233 cards.
  The Operator considers anything short of that agreed review a bug; the narrower
  live-guidance-only option is rejected.
- Use the current `sources/md/` subdirectory convention rather than `sources-md/`.

These decisions supersede the corresponding options in the historical Project09
synthesis. They authorize the planned correction, not a claim that source edits
have already been made. Corpus scope, C&B retention and the coupling's compatibility
treatment are settled; execution detail remains to be prepared in Arc01.

## Operator deferral — 2026-10-09

The Operator explicitly ordered: “let's defer S02-08 by order of operator and
continue to open slice 3”. This supersedes the previous requirement to satisfy
S02-08 before Slice02 closure and Slice03 planning. S02-08 is **deferred**, not
done: no source identity, original fidelity or semantic review is accepted by
this decision. The full 233-card/five-dimension scope remains binding.

Carryover owner: Arc02 CDC, with the Operator supplying/selecting exact originals
and capture inputs; Project10 **P10-11** tracks the unresolved readiness gate.
Slice03 must explicitly map every affected card and the existing input-action
register into its Arc02 handoff. Re-entry is required before accepting a dependent
source-fidelity result and before full-corpus/project release acceptance: exact
Arnheim/Cleland/Tschichold editions/translation and page bases, 37 Butterick
page captures and four article captures, conversion lineage and adequate
original/prepared completeness/fidelity mappings, with independent CDC review.
Any acquisition/conversion requires a separate exact input/output assignment.
This is a sequencing deferral, with no source mutation or private-search authority.

## Planning choices and dependent implementation

The formerly pending wording/profile/example choices are selected by CDC for
Slice03 in [its design](arc01-portable-contract/slice03-contract-composition-and-handoff/slice-plan.md#cdc-selected-design-for-this-assignment):
seven scoped formulations with their full caveats, a short contextual profile
before styling, the accepted local claim-result method, and one diagnostic
20–80rem configuration. These are planning decisions for composition, not new
scientific evidence or adopted live teaching. Independent slice composition and the Operator's Arc01 composition gate
are satisfied at their stated planning scope; source/semantic/release gates remain. Slice03 allocates all 233 cards,
eight live files and relevant finding/reconciliation work without source mutation.

## Operator metadata and rendering addition — 2026-10-10

The Operator adds [Arc06](arc06-card-metadata-and-rendering/arc-plan.md): reconcile
existing concept-card fields with the standardized representation and make
metadata plus Markdown render correctly on GitHub. Use the historical 3.2
contract if the unified replacement is not ready. Project08's replacement is
still provisional/P-15 open; select the preserved 3.2 field definitions now.
Skill version 4.8.1 is not a ready card-schema 4.0. Reassess only through an
explicit recorded contract amendment before affected mutation.

Never fill missing fields: no guessed facts, null/empty defaults, generated
provenance, IDs, dates or review states. Preserve existing extensions and values;
record absent/ambiguous fields separately. Alignment of available fields does
not imply full schema conformance, semantic verification or source-fidelity.
This explicitly expands the prior format/schema boundary for this bounded
normalization and rendering correction. Broader schema redesign remains
Project08-owned; its gates and existing plans are unchanged.

Arc06 has four planned slices: contract/full field inventory, book metadata,
web metadata, and complete GitHub rendering/revision handoff. Exact rollout
batches/pilot are prepared from the inventory; split oversized cohorts without
losing any of the 233 baseline identities. New P10-12/13 criteria track this
addition independently of all existing project rows.

Arc02's issued assignment continues. Arc06 is queued, with no CC prompt issued;
its read-only contract work can be activated at a later handoff without missing
book originals. Metadata mutation needs the accepted local contract/pilot and
fresh exact source scope. Arc06 must compose before Arc04 package freeze;
Arc04/05 own package and final-revision checks. Arc numbers remain stable;
roadmap dependencies, not numeric sorting, govern execution.

## Operator methodology pilot — 2026-10-10

The Operator requested that the Slice02 retrospective become Project13 evidence
and that we try revised preparation/review methods on one or two slices before
comparing results. [Project13](../project13-collab-refinements/project-plan.md)
owns the case study and [Experiment01 protocol](../project13-collab-refinements/artifacts/experiment01-methodology-pilot/protocol.md).
This is a bounded local methodology trial, not a change to design deliverables,
source-readiness requirements, contributor roles, or acceptance criteria.

Apply the trial to the next two **newly opened** Project10 slices, chosen in
normal roadmap/readiness order and registered before their initial prompts are
issued. The current Arc02/Slice02 Iteration04 is already issued and remains
under its existing contract; its in-flight work is excluded from treatment.
No issued prompt is modified. [Project-local instructions](AGENTS.md) carry the
prospective approach: source-grounded examples, inventory before judgment,
explicit verification coverage, comprehensive reviewer checks, changed approach
on recurring defects, and compact current records with preserved history.

After the first registered slice closes or reaches a recorded blocked/escalation
stop, CDC performs the protocol's meta-review before the next trial handoff.
After the second, perform the final comparison before extending the trial.
These are the Operator-requested measurement checkpoints within Expedited Mode;
normal closure, source, independent-review and Operator gates still apply.
Follow the protocol's explicit early-stop/deviation rules if only one slice
can be evaluated. No trial work is executed or accepted by this plan update.

## Workflow and acceptance

Default Two-Contributor Workflow: Sofie in this chat performs CDC planning with
the Operator; CC is the separate context receiving the prompt through the Operator.
The Operator selected Expedited Mode for remaining Project10 work on 2026-10-09;
the Two-Contributor Workflow remains selected, with no CRC role. Source work requires
a complete slice open set and the Operator's
implementation handoff under the standing planning instructions. Slices use
`cdc-verification.md`; any work implemented by the reviewer needs another
verifier. Project closure requires independent composition review and Operator
acceptance recorded when performed, not pre-filled success files.

In Expedited Mode, CC commits the explicitly named assigned files after changes;
CDC commits after review or planning changes. Close a slice as soon as its full
evidence permits, then automatically open the next planned slice and give the
Operator its CC prompt path as plain project-relative copy/paste text. After an
arc's last slice, complete formal arc closure and open the next planned arc and
its first slice. Unresolved escalations, source-readiness requirements, independent
review and Operator gates still stop dependent advancement. This selection changes
cadence only: no shortcuts, skipped validation, weaker evidence/review, inferred
source scope, scope changes or timeline interpretation. It does not select a mode
for other projects.

Keep slice-produced evidence under the owning slice's `artifacts/`. Project09
retains the shared audit. At close, Project11 receives the actual accepted
package/source revision, finding dispositions, compatibility decision and
remaining limitations. Publication remains a distinct Operator decision.

Arc02 Slice04 is independently closed at b6acb22f with nine rows done.
Project13 final comparison dc7b0732 completes the two-run pilot; benefit remains
inconclusive and no third run/general adoption is authorized. Current
[Slice05](arc02-theory-and-evidence/slice05-fluid-type-accessibility-limits/cc-prompt.md)
is the next ordinary retained T concern: fluid-type/accessibility limits, DES-005,
seven contexts/98 lines/five files. I1 C5bb54471/Hb418607d is independently
reviewed: four child rows done/five open. Current [Iteration02](arc02-theory-and-evidence/slice05-fluid-type-accessibility-limits/cc-prompt-iteration02.md)
repairs residual source coverage, actual pair results, prose joins and input/control
guards. SOURCE/main advanced externally to 314e5802; assigned design blobs still
equal dffa504e. Arc03 retains actual accessibility/typesetting proof; all parent
criteria, R/T/C/L/G,233/eight/16, P10-11, metadata/live/package/release gates remain.

## Version History

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
