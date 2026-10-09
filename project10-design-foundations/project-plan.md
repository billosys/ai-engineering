---
project: project10-design-foundations
status: active
depends-on: [project09-design-audit]
blocks: [project11-unified-design-practice]
related: [project08-concept-card-metadata]
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

Arc01 is open with its first slice issued. Remaining arcs are planned; detail
each near execution after resolving its dependencies. The active
[Arc01 plan](arc01-portable-contract/arc-plan.md) supplies the slice breakdown.

| Arc | Capability | Dependencies | Audit coverage |
|---|---|---|---|
| arc01-portable-contract | Separate reusable method from adopting-project identity; specify C&B removal and the full-corpus review method, manifest and source needs | Project09 evidence intake | DES-001, DES-010, DES-013, DES-015 |
| arc02-theory-and-evidence | Correct theory and arithmetic; verify and reconcile the complete card corpus against sources and guides with claim-level evidence | Arc01 contract | DES-002–005, DES-007–009, DES-012, DES-013, DES-015, DES-016 |
| arc03-accessibility-and-typesetting | Add usable accessibility obligations and transferable typography procedures | Arc01–02 decisions | DES-005, DES-006, DES-009, DES-011 |
| arc04-guides-and-package | Compose corrected guides, brief-to-review routing, runnable examples and isolated package | Arc01–03 | DES-010, DES-013, DES-014; all repeated claims |
| arc05-validation-and-release-readiness | Exercise cross-context specimens, reconcile every finding and demonstrate the complete package | Arc01–04; accepted Project09 baseline | DES-001–016 |

Current status: active; Arc01 Slice01 remains open after independent CDC review
of CC completion at `0e0c1d0a`. Current assignment:
`arc01-portable-contract/slice01-scope-and-portability-contract/cc-prompt-iteration01.md`.
The Operator relays this bounded evidence correction to the separate CC context.
See the [CDC record](arc01-portable-contract/slice01-scope-and-portability-contract/cdc-verification.md);
no later slice has opened. Project09 may be consulted for planning
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

## Decisions before dependent implementation

1. Adopt the revised principle formulations and concrete example configuration;
   the synthesis contains proposals, not final normative wording.
2. Specify the full-corpus review packet, source acquisition needs and slice
   boundaries without reducing the approved population or review dimensions.

## Workflow and acceptance

Default Two-Contributor Workflow: Sofie in this chat performs CDC planning with
the Operator; CC is the separate context receiving the prompt through the Operator.
No three-contributor or Expedited selection is inferred. Source work requires
a complete slice open set and the Operator's
implementation handoff under the standing planning instructions. Slices use
`cdc-verification.md`; any work implemented by the reviewer needs another
verifier. Project closure requires independent composition review and Operator
acceptance recorded when performed, not pre-filled success files.

Keep slice-produced evidence under the owning slice's `artifacts/`. Project09
retains the shared audit. At close, Project11 receives the actual accepted
package/source revision, finding dispositions, compatibility decision and
remaining limitations. Publication remains a distinct Operator decision.

## Version History

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
