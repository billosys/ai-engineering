---
version: "1.2.0"
---

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
- The [versioning model](versioning-decision.md) distinguishes skill, planning-document
  and named-schema versions. Schema cadence and detailed compatibility/bump rules
  remain open. All adopted planning-document roles need frontmatter, their own
  version and an end-of-document history; the scope is broader than plan files.
- Ship additional project-management guide chapters with concise, explicit manual
  maintenance instructions for both planning metadata and status JSON. A CLI such
  as ODM cannot be a prerequisite for correct maintenance.
- Adopt prospectively in Project06's open plans, reusable framework material, then
  Lykn UAT. Do not retroactively fill metadata in old/closed files or source copies.

## Status tree and migration guidance — 2026-09-12

Operator report: a separate session migrating an older project misunderstood the
status directory. The operator clarified that status is a collection of projects,
with one overall JSON/HTML pair above the project and arc status directories.
This reaffirms the accepted hierarchy; it does not depend on unresolved schema fields.

```text
<repo>/.worktrees/planning/
  project01-<slug>/                 # authoritative planning documents
    project-plan.md
    arc01-<slug>/
      arc-plan.md
  project02-<slug>/
    project-plan.md
  status/                          # one collection root for this repository
    status.json
    status.html                    # Saga View: the collection of projects
    project01-<slug>/
      project-status.json
      project-status.html
      arc01-<slug>/
        arc-status.json
        arc-status.html
    project02-<slug>/
      project-status.json
      project-status.html
```

The second project illustrates a project without an arc status directory; it does
not require a fabricated arc. Slices remain part of the relevant work/status model;
this layout does not introduce slice-status pages. `projectNN`/`arcNN` are schematic
identifiers, with slugs following the planning convention where adopted. Existing
names (including decimal IDs or legacy slugs) need an explicit locator mapping, not
an automatic rename or a new identity. Use the actual established planning worktree
root rather than creating an extra nested directory literally named `planning`.

The shared `status/` root is a sibling of the project plan directories. Its JSON/HTML
files represent the repository collection, never one project's status under generic
filenames. Project status lives inside that project's status directory; arc status
lives below that project. Relative links must resolve between status views and the
separate authoritative plans. An omitted project's data must be accounted for through
coverage/unknowns, not silently described as a complete Saga. A single-project repo
uses the same collection hierarchy. No saga-plan or saga-ledger is introduced.

Toolkit support directories such as `scripts/`, `templates/` and `schemas/` may also
live at the shared status root under the accepted repository-owned-copy model;
Slice02 specifies their copy/upgrade details. They are support material, not projects.
A guide must explain how discovery distinguishes support directories from work records.

### Verified documentation gap and ownership

CDC inspected main at `e763c661`, the Project06 feature source at `31d96b15`, and
both installed standalone and bundled project-management guide trees on 2026-09-12.
The canonical-worktree guide has no status-tree section; the scales guide still
calls Saga a named but unused multi-version vision. Current engineering-methods
process guidance repeats that unused-tier framing. These are source observations;
the reported confusion in the other session is operator evidence, not a reproduced
migration trial. No source/package or installed-skill edits were made in this check.

Required source handoff:

- Project-management `guides/02-canonical-planning-worktree.md` owns the directory
  tree and plan-versus-status distinction. Link its status section from `SKILL.md`
  and `guides/README.md` for both setup and migration tasks.
- Project-management `guides/01-scales-of-work.md` formally defines Saga as the
  repository's project collection; reconcile the engineering-methods process summary.
- Collaboration-framework should route status setup/migration to project-management;
  avoid another independently maintained layout definition.
- The manual status-maintenance chapter needs a preservation-first migration recipe:
  inventory existing files and project/arc identities, map old paths to the target
  tree, account for every source record and unknown, preserve evidence/history,
  repair references, validate the whole adopted tree, render and inspect navigation.
  JSON/HTML projection files and authoritative planning records have different roles;
  moving one must not silently reclassify the other.
- Each affected skill gets its own version/history update when changed. Arc03 must
  inspect both generated standalone and framework packages, not only source links.

### Acceptance case to carry forward

Starting only from packaged skill guidance, reconstruct the target tree for a
fictional legacy repo with two projects: one with two arcs, one with direct slices.
Identify the overall, project and arc file pairs and their links to source plans.
Account for an unadopted historical project explicitly in collection coverage.
Check preservation of identities/evidence and that support directories are not
counted as projects. Catch misplaced per-project generic `status.*`, flattened arc
folders, an extra nested planning root and stale links. Do not infer acceptance
from successful rendering. Slice02 specifies the trial; Arc03 supplies package
and guide-use evidence, with live consumer feedback retained in Lykn UAT.

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
6. **Document revisions and schema/toolkit upgrades.** Separate document versions
   from named-schema versions; end-of-file histories, compatibility rules, preservation,
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

## Version history

- 1.0.0 — 2026-09-11: Operator accepted work-origin/source separation; reserved versioning
  for discussion; explicitly required concise manual maintenance guide chapters.
  Created these durable chapter/procedure notes before implementation.

- 1.1.0 — 2026-09-11: Recorded the three version axes, named-schema identity and
  all-planning-document scope. Added document-revision guidance and open
  compatibility/bump questions; schema adoption itself remains forthcoming.

### 1.2.0 — 2026-09-12

Recorded the explicit shared status tree, verified current guidance omissions,
source ownership, manual migration procedure requirements and a multi-project
acceptance case after the operator's migration-session report.
