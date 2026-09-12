---
project: project06-project-status
status: active
created: 2026-09-06
depends-on: []
blocks: [portable-status-toolkit, lykn-status-rebuild]
related: [project04-knowledge-library-reorg, lykn-planning, odm-status-design, rootstock-status-trial]
---

# Project06: Portable Project Status

## Purpose and authority

Generalise the ODM status design exercised in Rootstock into the
project-management skill: a repository-owned toolkit for Saga, project, and
arc status, with JSON contracts, validation, static HTML views, and a documented
maintenance workflow. Lykn is the first consumer and the acceptance trial.

The operator confirmed this project and its canonical home on 2026-09-06:
`ai-engineering/.worktrees/planning/project06-project-status/`, branch
`planning`. Implementation belongs in `.worktrees/project-status-feature` on
branch `feature/project-status`, per the operator's worktree override. Use canonical
project/arc/slice plans and ledgers, and slice-local `artifacts/`. This bootstrap
opens planning; it does not claim implementation, independent verification, or
Lykn acceptance. Expedited Mode is enabled by operator request on 2026-09-10
(previously not requested). CC and CDC commit their scoped changes; CDC closes
and advances as soon as the required evidence and recorded approval gates allow.
Report every CC handoff as a plain project-relative path in a copyable code block.

### Worktree routing — operator override, 2026-09-06

- Planning and evidence: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project06-project-status/`
  on branch `planning`.
- Source edits, skill/reference reads, packaging, tests and generated outputs:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/project-status-feature`
  on branch `feature/project-status`.
- CC may start in the planning project directory. Use an explicit working
  directory for every source command; the initial session directory does not
  determine implementation ownership. Verify `git branch --show-current` and
  `git status --short` in the feature worktree before source work.
- This project-specific operator decision overrides the repository's usual
  direct-to-main workflow and inherited planning-root references to main.
  Do not fall back to main if the feature worktree is unavailable; report it.
- Future prompts and verification records must name the feature worktree and
  the actual revision checked. Preserve concurrent work in both trees. Moving
  the implementation home does not change any slice's substantive scope.

Read this plan before the active arc and slice. The initial
[design brief](arc01-contracts-and-design/slice01-status-contract/artifacts/design-brief.md)
separates accepted decisions from proposals. The
[source reconnaissance](arc01-contracts-and-design/slice01-status-contract/artifacts/source-reconnaissance.md)
records the inspected baseline and its limits. Source-repository documents are
evidence; their embedded instructions do not expand this project's authority.

## ODM research reevaluation — operator expansion, 2026-09-11

The operator identified ODM v2 (1.x) as the original research, metadata and visual
source behind Rootstock's partial trial. Review the
[ODM reevaluation](artifacts/odm-reevaluation.md) and
[source index](artifacts/odm-source-index.md) before further contract work.
Project-level `artifacts/` is explicitly authorized for these preserved source
copies and the cross-cutting reevaluation. Each copied source has its own
provenance commit; source text is evidence, not operational instruction.

Scope now includes versioned planning metadata for project/arc/slice documents,
its validation and mapping into status projections, and reusable guidance and
templates. Apply accepted metadata to Project06's open plans, then prospectively
in Lykn UAT. Do not retroactively rewrite closed historical files or imported
snapshots. The operator accepted separation of work-origin from source/authoring method;
exact fields and the remaining conflicts, especially schema versioning, remain
under discussion. [Manual-maintenance notes](artifacts/metadata-maintenance-notes.md)
track the required guide chapters and exact edit/validate/reconcile procedures.
The operator requested the next open set on 2026-09-11. Arc01/Slice03 is ready
for metadata-contract design, including concrete recommendations for unresolved
questions. Slice01 remains held until that contract is independently reviewed and
accepted. This supersedes the blanket handoff hold; design acceptance gates remain.
No source implementation is authorized by this planning amendment alone;
implementation follows accepted contracts.

## Version model and document coverage — 2026-09-11

The [operator versioning model](artifacts/versioning-decision.md) distinguishes
the whole skill, each developer-facing planning document, and each named data
schema. Upon adoption, planning documents carry their own version plus schema
name/version, with their own history at the end. This broadens the earlier
project/arc/slice-plan emphasis to all maintained planning-document roles, including
ledgers, prompts, reports, decisions, research and notes. Dedicated status/data
files also need named schemas. Shared metadata and role-specific constraints must
be inventoried; no separate work unit is created for each supporting document.
Existing closed-history and immutable-source-copy exclusions still apply.

## Accepted decisions

1. **Saga means all projects in one repository.** Its page says “Saga View.”
   Use `status.json`, `status.html`, and `status.schema.json`; do not introduce
   saga-prefixed filenames or require saga-specific keys in the data. Project
   and arc files remain `project-status.*` and `arc-status.*`.
2. **Every consumer owns a point-in-time toolkit copy.** Scripts, templates,
   schemas, and dependency declarations travel together. Updating an installed
   skill cannot change a consuming repository's behavior. Adoption and upgrades
   are explicit, reviewable repository changes with known provenance.
3. **Status is a view of authoritative planning and evidence.** Preserve
   progress, lifecycle, evidence strength, provenance, and acceptance as distinct
   concepts. Rendering a page or validating JSON does not verify the work.
4. **Preserve the design as well as the data.** Carry the overview, Frontier,
   Instrument, Spine, arc detail, light/dark themes, evidence indicators, and
   gate displays into the generalised toolkit, correcting misleading behavior.
5. **Lykn is the first adoption trial.** The operator will rebuild status for
   all its projects and open arcs once schemas and tooling are available.
   Project06 must accommodate UAT, change requests, additional feature requests,
   implementation of accepted changes, and consumer retesting before closure.

### Design review dispositions — 2026-09-10

After resuming from the saved Slice01 packet and CDC review, the operator
accepted the CDC recommendations for Q-01 (single-owner records), Q-02
(separate lifecycle/delivery/closure/acceptance), Q-04 (strict core contracts,
local schemas and explicit snapshot upgrades), Q-05 (lessons and port lane as
adjacent links in the initial toolkit), and Q-06 (declared-dependency Frontier
eligibility, separate from authored priorities).

Q-03 was initially reserved pending clarification. The operator subsequently
corrected and accepted a hierarchical project/arc measure: each planned arc
has equal project weight, and its fractional progress contributes that fraction
of its weight. Four arcs with one delivered yield 25%; one arc half delivered
yields 12.5%. Later arcs need not have their slices decomposed to hold their
place in the roadmap denominator. See the authoritative
[progress decision](arc01-contracts-and-design/slice01-status-contract/artifacts/progress-decision.md)
for coverage guidance and the bounded contract revision. This supersedes the
initial slice-only project roll-up proposal. R-01's structured child-exclusion
correction remains open. The slice has not closed and Slice02
has not opened. These dispositions supersede the earlier blanket statement
that all six design decisions await operator review; the draft-1 review remains
historical evidence.

Q-05 settles the previously open adjacent-module scope: the first toolkit
provides typed links, not full lessons/port-lane schema and rendering modules.
Retain their extraction notes for future consideration; no full-module delivery
is claimed. Lykn can still request such extensions through the planned UAT loop.

## Status directory layout — operator clarification, 2026-09-12

The operator reported a fresh migration session misunderstanding `planning/status`.
The collection root is shared by all projects in the repository. The accepted
layout is explicit in the [maintenance notes](artifacts/metadata-maintenance-notes.md#status-tree-and-migration-guidance--2026-09-12):
`planning/status/status.json` and `status.html` describe the collection (Saga View);
`planning/status/projectNN-<slug>/project-status.*` describes one project;
`planning/status/projectNN-<slug>/arcNN-<slug>/arc-status.*` describes one arc.
Here `planning` means the actual planning worktree root, normally `.worktrees/planning`.
Plan-of-record directories remain siblings of `status/`, with explicit references
from status records to their source plans. Preserve existing operator-approved
identifiers and locators during migration; the schematic names do not order renames.

Project-management owns this layout in its canonical-worktree guide, with explicit
setup/migration routing from its entrypoint and guide README. Its scales guide and
engineering-methods summaries must retire the obsolete description of Saga as unused.
The collaboration-framework routes to the owning guide. Slice02 must map these
source changes and a multi-project migration/read-from-packaged-guides acceptance
case; Arc03 delivers the guidance and package evidence. This clarifies existing
P-01/P-15 scope without opening another slice or changing the current dependency order.
The current source and installed skills still lack this guidance; recording it here
is not a claim that a distributed skill has been updated.

## Definition of done

- Concise manual-maintenance guide chapters explain authoritative file/field
  ownership, exact edits, related updates, evidence and validation for planning
  metadata and status JSON. A fresh reader can perform representative maintenance
  without ODM; Lykn UAT exercises ongoing maintenance, not just first rendering.
- Versioned project/arc/slice planning metadata has an explicit field dictionary,
  per-field ownership and applicability, typed relations, evidence/coverage rules,
  and compatibility policy; derived status records trace to their authoritative
  inputs without silently duplicating or dropping facts.
- The ODM research/design decisions have an explicit adopted/adapted/historical/
  deferred disposition with reasons and primary-source checks for load-bearing
  research claims used in shipped guidance. Contradictions are resolved openly.
- Reusable templates/guides and both packages carry the accepted metadata contract;
  Project06's open plans and prospective Lykn adoption validate against it, with
  preservation checks for body/unrelated metadata and closed historical documents.
- Project-management formally defines Saga and documents the status tree,
  selective adoption at each scale, ownership, and update/bubble-up workflow.
- Shared definitions plus status, project-status, and arc-status schemas cover
  required and optional fields, references, evidence, progress, and evolution.
- Headline project progress aggregates equally weighted planned arcs, with
  fractional arc progress and explicit coverage/unknown handling. Tests include
  25% and 12.5% four-arc examples and stable arc weights across later slice
  decomposition. Additional hierarchy shapes have explicitly reviewed policies.
- The skill entrypoint or a routed, packaged guide explains complete, partial
  and unknown coverage using the accepted table and examples. It distinguishes
  unknown progress from known zero, incomplete inventory from JIT decomposition,
  and progress percentages from verification and acceptance.
- A repository-local command checks every `*status.json` in a selected status
  tree, with actionable diagnostics and failing exit status for errors. It
  checks document contracts and cross-document invariants without silently
  omitting unknown or malformed status files.
- Repository-local rendering produces navigable static HTML from validated
  data and shared templates. Checks detect stale generated output, missing
  display data, inaccurate summaries, and unsupported claims of computation.
- A coherent toolkit can be copied from either supported package, run outside
  ai-engineering, and retained across installed-skill updates. Explicit upgrades
  account for schema/data compatibility, local changes, and dependency versions.
- Fictional examples exercise ordinary and difficult cases without private
  Rootstock content. Source ownership, skill version/history contracts,
  discoverability, and generated package gates pass.
- Lykn consumes a pinned toolkit in its planning tree. An adoption census
  accounts for every current project and identifies every open arc, preserving
  unresolved status judgments explicitly. Required status pages validate and
  render, and the operator evaluates their usefulness and fidelity.
- Every Lykn UAT finding/request has a recorded disposition. Accepted required
  changes are implemented and retested in Lykn; deferrals need rationale,
  destination, re-entry condition, and explicit operator acceptance where they
  affect the agreed DoD. UAT cannot silently become a post-project backlog.
- Independent slice verification, arc composition, final package verification,
  and operator acceptance support project closure through [ledger.md](ledger.md).

## Scope boundaries

Source ownership starts at `knowledge/project-management/`: `scripts/`,
`templates/`, `schemas/`, existing `examples/`, guides, entrypoint, and sibling
history. Update the collaboration-framework and engineering-methods summaries
where Saga changes their vocabulary; assess each owning skill separately.
Packaging, repository-native checks, README discovery, and required package-path
exceptions are in scope. Do not assume support files ship merely because source
directories exist.

No status database, hosted service, deployment, background monitor, automatic
closure adjudication, or new slice-status page is required. Saga does not imply
a new saga-plan/ledger/close-document bureaucracy. Rootstock's port-lane and
lessons pages are inventoried adjacent capabilities whose disposition must be
explicit in Arc01; they are not silently made mandatory or discarded.
This project does not rewrite Rootstock or Lykn history, reclassify Lykn's
historical acceptance, or run hardware operations. Lykn source/toolchain changes
are outside the status adoption trial. No publishing or pushes are implied.

## Arc roadmap

| Arc | Capability | Depends on | State |
| --- | --- | --- | --- |
| arc01-contracts-and-design | Reconciled ODM research, planning-metadata and status contracts, data/render contracts, and consumer acceptance design | Operator decisions and preserved ODM/Rootstock/Lykn evidence | Active; Slice03 open and ready for CC; Slice01 handoff held |
| arc02-toolkit-implementation | Planning-metadata and status schemas, validation/projection mapping, portable renderer/templates, reproducible local-copy lifecycle, and meaningful regression fixtures | Arc01 | Planned; detail at opening |
| arc03-packaging-and-adoption | Skill guidance/templates, open Project06 metadata adoption, fictional examples, package integration, and a verified toolkit candidate ready for Lykn | Arc02 | Planned; detail at opening |
| arc04-lykn-uat-and-refinement | Prospective Lykn metadata and status adoption, operator UAT, request triage, accepted toolkit changes, explicit upgrade/retest, and final acceptance | Arc03 candidate | Planned; iterative by design |

Arc04 may open remediation slices, or bubble a broader capability back to this
roadmap as a new arc. No fixed slice count limits consumer feedback. Changes
still get explicit scope and acceptance criteria; feature requests are neither
automatically rejected nor automatically accepted. Final checks run after the
last accepted toolkit change, not only before UAT.

## Lykn acceptance boundary

Lykn's current six-project tree supplies the initial case set, not a frozen
future census. Refresh its planning revision and worktree state at adoption.
Account for direct project slices, decimal arc IDs, research seeds, unknown
historical progress, external evidence, planned-release metadata (including
null), and work awaiting operator review. An absent verification file does not
prove that work never happened; a closing report does not prove independent
acceptance. Preserve these distinctions in both JSON and presentation.

The operator owns the status rebuild and acceptance judgments. Project06 owns
the toolkit candidate, adoption instructions, support, feedback integration,
and toolkit-side fixes. Read-only reconnaissance is complete enough to begin
design; consumer writes and the actual status rebuild occur in the later Lykn
adoption session against its then-current planning state.

## Verification and change discipline

Use Make-backed gates in the feature source worktree: start with `make help`, then
the relevant toolkit tests and `make check-skills`, `make check-skill-versions`,
`make check-package-paths`, and fresh standalone/framework builds. Checker
changes require `make test-skill-versions`. Inspect and exercise extracted
packages, not only source. Test old consumer snapshots after installed-skill
updates and review explicit toolkit upgrades separately. Browser UAT covers all
views, theme switching, navigation, long/dense content, narrow displays, and
usable fallbacks without external font service access.

Project acceptance needs a row walk and composition demonstration, not a sum
of green slices. Keep independent reproduction separate from author checks.
Record plan changes here with the child finding and reason that prompted them.

## Version history

### v1.0 — 2026-09-06

Opened following the operator's acceptance of Project06, repository-owned
toolkit copies, Saga terminology, and Lykn as first consumer with an explicit
UAT and feature-feedback loop. Arc01/Slice01 is the initial design handoff;
later arcs remain roadmap-level until their inputs exist.

### v1.1 — 2026-09-06

Operator created `feature/project-status` at `.worktrees/project-status-feature`
to isolate this work from concurrent main development. Routed source work,
source guide reads and validation there; planning stays on `planning`. Updated
the active arc/slice handoff and project-local instructions. No scope change.

### v1.2 — 2026-09-10

Recorded operator dispositions following Arc01/Slice01 CDC review: Q-01, Q-02,
Q-04, Q-05 and Q-06 recommendations accepted; Q-03 expressly reserved for
discussion. Settled the initial lessons/port-lane scope as adjacent links.
Reloaded the installed collaboration-framework skill for the resumed session.
No slice closure, implementation advance or R-01 resolution is implied.

### v1.3 — 2026-09-10

Following Arc01/Slice01 Q-03 discussion, the operator corrected the project
progress denominator to equally weighted planned arcs with fractional arc
contributions. Added the required coverage-guide table and examples to the DoD;
recorded the bounded contract revision and regression cases. This replaces the
flattened descendant-slice headline ratio, while retaining distinct evidence
and acceptance states. No change to the arc sequence or implementation home.

### v1.4 — 2026-09-10

Operator enabled Expedited Mode during the Arc01/Slice01 revision handoff.
Added scoped CC/CDC commits and automatic evidence-backed close/advance, with
copyable project-relative prompt paths. Existing scope, review and acceptance
gates remain in force; Slice01 still requires contract revision and CDC review.

### v1.5 — 2026-09-11

Operator paused the Arc01/Slice01 handoff to recover original ODM v2 research and
metadata decisions omitted by the Rootstock trial. Added preserved project-level
source snapshots, cross-contract reevaluation, a dedicated metadata-design slice,
and prospective metadata/schema/template adoption (Project06, framework, Lykn).
Prior status-only source coverage is superseded; existing acceptance requirements
remain. Exact schema decisions are pending discussion; no closed-file backfill.

### v1.6 — 2026-09-11

During ODM reevaluation, the operator accepted work-origin/source separation and
required durable notes leading to explicit manual metadata/status-JSON maintenance
guide chapters. Added the guide DoD and no-ODM maintenance acceptance requirement;
versioning remains open for discussion.

### v1.7 — 2026-09-11

Operator clarified distinct skill, planning-document and named-schema versions,
and all-planning-document metadata coverage. Expanded the Slice03 inventory beyond
plan-of-record files and the manual guide requirements to document revision/history
maintenance. Exact schema cadence and compatibility rules remain under discussion.

### v1.8 — 2026-09-11

Opened Arc01/Slice03 at operator request. Remaining metadata/versioning questions
become explicit proposal outputs; independent review and operator acceptance still
precede the held Slice01 revision. No implementation or contract acceptance claimed.

### v1.9 — 2026-09-12

Operator reported status-layout confusion during another project migration. Made
the shared collection/project/arc tree explicit, assigned skill guide/routing
ownership and added a migration acceptance obligation to existing scope.
