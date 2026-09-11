# Manual metadata and status maintenance: design notes and guide requirements

Started: 2026-09-11. Living Project06 notes; not yet shipped guidance.
Authority: operator discussion during the ODM research reevaluation.
Read alongside [the reevaluation](odm-reevaluation.md) and
[preserved sources](odm-source-index.md). Update these notes as decisions land;
keep open proposals visibly distinct from accepted requirements.

## Accepted decisions

- Separate **why work arose** (`planned`, `discovered`, `amendment`) from
  **how/where its content was created** (including `authored`). An item may
  be discovered work authored locally. Exact field names/shapes remain design work.
- Preserve source/import lineage after a document becomes locally maintained.
  Unknown provenance is not the same as authored here.
- Versioning is an open discussion; no independent-per-type/global-counter
  choice has been accepted for the new metadata contracts yet.
- Ship additional project-management guide chapters with concise, explicit manual
  maintenance instructions for both planning metadata and status JSON. A CLI such
  as ODM cannot be a prerequisite for correct maintenance.
- Adopt prospectively in Project06's open plans, reusable framework material, then
  Lykn UAT. Do not retroactively fill metadata in old/closed files or source copies.

## What every maintenance procedure must answer

1. **Trigger:** when this operation is needed.
2. **Authority:** which file/field owns the fact; which values are derived or copies.
3. **Edit:** exact before/after examples using accepted field names and schemas.
4. **Related changes:** parents, dependencies, references, coverage assertions,
   source citations and status JSON affected by this edit.
5. **Validate:** the shipped command, what success means, expected diagnostics and
   the manual semantic check the command cannot perform.
6. **Record:** evidence, assessment/review time, reason, plan history and the scoped
   commit needed to leave a durable, reviewable change.

Do not publish invented command names while CLI design is unsettled. Final chapters
must use commands actually implemented and tested from a vendored consumer copy.
Before the toolkit exists, these are procedure requirements, not executable runbooks.

## Core maintenance loop to teach

Read the current plan and supported schema. Identify the authoritative record.
Edit the smallest relevant metadata/body region while preserving unrelated content.
Recheck affected relationships, coverage and evidence applicability. Update any
manually maintained status projection from the same facts and identify its source
revision/assessment. Validate the complete affected tree, regenerate HTML, inspect
the result and commit the intended files. A passing schema check proves structure;
the author/reviewer still checks that the assertions match the evidence.

The guide must distinguish three modes explicitly:

- **Authored planning record:** the plan and its metadata own the work facts.
- **Manually maintained status JSON:** a cited projection/assessment, with a clear
  reconciliation procedure when its source changes. Editing it cannot silently
  override the plan or promote evidence.
- **Generated status JSON/HTML:** edit the inputs and regenerate; do not hand-edit
  generated facts. If some status fields are authored annotations, identify their
  separate owner and preservation rules in the contract.

This is single authority with explicit projections, not two competing editable
sources of truth. Sparse/historical consumers may use a supported reported-source
mode with visible uncertainty; they must not fabricate a complete metadata record.

## Operation coverage matrix

| Operation | Required manual guidance | Failure the example/check must catch |
| --- | --- | --- |
| Create a project/arc/slice | Required metadata, identity allocation, parent, purpose/DoD, source kind, schema, initial known/unknown state | Duplicate identity; fake parent wrapper; default completed or accepted |
| Introduce discovered work | Set work-origin and creation-source independently; record reason and scope impact | `authored` erases `discovered` |
| Rename or relocate | Preserve identity; update locators/references explicitly; keep history | Path/display number silently becomes a new identity |
| Reparent | Change containment owner, update affected populations, inspect dependency and evidence references | Stale parent coverage or duplicate counting |
| Add/change a dependency | Record typed target and required predicate/gate; check cycles and external assessment | Prose-only dependency or priority mistaken for readiness |
| Record/remove a block | Name reason/target, current assessment and evidence; recompute eligibility | Removing a label silently clears an unsatisfied prerequisite |
| Change delivery state | Scope the claim, retain evidence and assessment date; update affected views | Delivery automatically grants verification/acceptance |
| Record a gate result | Name gate and environment/revision, result, actor and evidence; define unmet/unknown/waived | Historical pass shown as current after relevant changes |
| Verify or accept work | Follow existing independent verification and operator authority; update only supported fields | Self-attestation treated as independently reproduced evidence |
| Change scope/DoD | Record what changed and why, reassess criteria, child set, progress and old evidence applicability | Existing evidence silently proves new scope |
| Defer, exclude, retire or supersede | Preserve identity/history; record disposition, affected entity, rationale and re-entry/lineage | Deferred work disappears or increases delivered numerator |
| Affirm coverage | Define population and current members; record assertion/evidence; recheck after adds/removes | Known IDs mistaken for known progress or semantic completeness |
| Update progress | Use scale-specific denominator and unrounded inputs; four-arc 25%/12.5% examples | Global leaf denominator, unknown treated as zero, or rounded child inputs |
| Refresh status JSON | Trace source changes, update only owned fields and truthful assessment dates, validate entire affected tree | Fresh render timestamp disguises stale assessments |
| Change schemas/toolkit snapshot | Inspect supported versions, explicit field mapping and local changes; validate/re-render/review | Blind version restamp or installed update changes consumer behavior |
| Handle malformed/unknown metadata | Preserve original content, diagnose unsupported fields/versions, repair with evidence | Parser/formatter silently drops metadata or makes guesses |

## Proposed guide chapters

Titles and final filenames are provisional; assign final routes with the source
impact map. Prefer focused chapters over one large metadata appendix.

1. **Planning metadata: ownership and first records.** Field dictionary routes,
   identity/locator distinction, work-origin versus source, new project/arc/slice.
2. **Maintaining relationships and scope.** Containment, dependency gates, blocks,
   rename/reparent, decomposition assertions, changes and deferrals.
3. **Maintaining status and evidence.** Delivery/verification/acceptance, named
   gate results, source revisions and environments, freshness, corrections.
4. **Coverage and progress.** The required complete/partial/unknown table, JIT
   planning, changing roadmaps, worked hierarchical arithmetic and sparse records.
5. **Maintaining status JSON and regenerating views.** Authority map, manual versus
   generated fields, source reconciliation, validation/render loop and diagnostics.
6. **Schema and toolkit upgrades.** Version axes, compatibility rules, preservation,
   explicit upgrades, local customizations and rollback/review boundaries.

Every chapter should contain at least one realistic before/after edit and a common
mistake with its correction. JSON/YAML snippets must validate against the shipped
contracts; placeholders must be unmistakable and never look like real evidence.
Reuse framework closure guidance rather than inventing a competing closure protocol.

## Acceptance and handoff requirements

- Source guides are routed from the project-management entrypoint/wayfinder and
  included in both packages, with coherent templates and examples.
- A fresh reader can maintain a fictional project using a text editor plus the
  copied validator/renderer, without ODM, undocumented commands or this conversation.
- Exercise creation, discovered work, changed dependency, stale gate evidence,
  scope/coverage edit, status refresh and an explicit snapshot upgrade. Record
  ambiguities and feed them back into the guide and tooling design.
- Lykn UAT includes manual maintenance after initial setup, not just importing
  records or checking a successful render. Capture requests for clearer instructions
  and additional maintenance support as normal UAT findings.
- Body/unrelated metadata preservation and unchanged closed-history files are
  demonstrated. No broad retrospective metadata migration is implied.

## Decision log

- 2026-09-11: Operator accepted work-origin/source separation; reserved versioning
  for discussion; explicitly required concise manual maintenance guide chapters.
  Created these durable chapter/procedure notes before implementation.
