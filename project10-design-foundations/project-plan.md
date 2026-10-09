---
project: project10-design-foundations
status: planned
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
in the main checkout. This establishes the project and initial roadmap, not an
issued implementation assignment or an approved release.

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
guidance must be reviewed; unresolved historical material cannot silently become
authority. Run the applicable source/version/package gates and task demonstrations
against the composed package, with independent review and Operator acceptance.
The [ledger](ledger.md) holds those release-level criteria.

The full research-to-validation design practice belongs to Project11. This
project does not automatically redesign the concept-card schema, overwrite
historical evidence, or claim product conformance from examples. Full semantic
reconciliation of all 233 cards is an explicit scope decision still to be made;
the narrower live-skill boundary is a proposal, not a silently accepted reduction.

## Initial arc roadmap

These are candidate arc boundaries derived from the accepted direction. No arc
directories, slice open sets or CC prompts are issued yet. Detail each arc near
execution, after resolving its dependencies and scope decisions.

| Arc | Capability | Dependencies | Audit coverage |
|---|---|---|---|
| arc01-portable-contract | Separate reusable method from adopting-project identity; specify C&B removal and settle corpus scope | Project09 evidence intake | DES-001, DES-010 |
| arc02-theory-and-evidence | Correct theory, arithmetic and source interpretation; establish claim register and historical-card boundary | Arc01 contract | DES-002–005, DES-007–009, DES-012, DES-013, DES-015, DES-016 |
| arc03-accessibility-and-typesetting | Add usable accessibility obligations and transferable typography procedures | Arc01–02 decisions | DES-005, DES-006, DES-009, DES-011 |
| arc04-guides-and-package | Compose corrected guides, brief-to-review routing, runnable examples and isolated package | Arc01–03 | DES-010, DES-013, DES-014; all repeated claims |
| arc05-validation-and-release-readiness | Exercise cross-context specimens, reconcile every finding and demonstrate the complete package | Arc01–04; accepted Project09 baseline | DES-001–016 |

Current status: planned; no active arc. Project09 may be consulted for planning
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

These decisions supersede the corresponding options in the historical Project09
synthesis. They authorize the planned correction, not a claim that source edits
have already been made. Corpus scope remains under discussion: the Operator asked
for a concrete explanation of full semantic card reconciliation before choosing.

## Decisions before dependent implementation

1. Define whether full self-consistency includes semantic reconciliation of the
   entire historical corpus, or the live skill plus explicitly bounded archives.
2. Adopt the revised principle formulations and concrete example configuration;
   the synthesis contains proposals, not final normative wording.

## Workflow and acceptance

Default Two-Contributor Workflow: Sofie in this chat performs CDC planning with
the Operator; CC is unassigned. No three-contributor or Expedited selection is
inferred. Source work requires a complete slice open set and the Operator's
implementation handoff under the standing planning instructions. Slices use
`cdc-verification.md`; any work implemented by the reviewer needs another
verifier. Project closure requires independent composition review and Operator
acceptance recorded when performed, not pre-filled success files.

Keep slice-produced evidence under the owning slice's `artifacts/`. Project09
retains the shared audit. At close, Project11 receives the actual accepted
package/source revision, finding dispositions, compatibility decision and
remaining limitations. Publication remains a distinct Operator decision.

## Version History

- 1.1 (2026-10-08): Operator selected removal of C&B material with Git-only
  historical retention and classified the original coupling as a bug requiring
  no compatibility bridge. Corpus scope remains undecided pending clarification.
- 1.0 (2026-10-08): Established Project10 for the 1.5 foundation repair;
  linked the Project09 audit, mapped all findings, and recorded provisional
  arcs, explicit scope decisions, verification and Project11 handoff requirements.
