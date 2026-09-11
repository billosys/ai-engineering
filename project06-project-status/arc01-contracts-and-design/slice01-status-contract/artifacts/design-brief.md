---
version: "1.1.0"
---

# Initial design brief

## Current research and contract scope — 2026-09-11

This expands the original status-only brief. Read the project-level
[ODM source index](../../../artifacts/odm-source-index.md),
[reevaluation](../../../artifacts/odm-reevaluation.md),
[version model](../../../artifacts/versioning-decision.md), and
[manual-maintenance notes](../../../artifacts/metadata-maintenance-notes.md).
Rootstock is a partial trial of ODM's design, not the complete metadata spec.

The design now includes metadata for all maintained planning-document roles,
not only plan-of-record files. Adopted documents have their own content version
and history plus named-schema identity/version. Distinguish work-origin from
source/authoring method, and retain imported provenance. Specify common metadata
and role-specific constraints without making supporting docs into work units.

Planned Slice03 defines the metadata contract, schema dialect/identity and
source-to-status ownership. Resumed Slice01 defines the status projection and
cases, including accepted hierarchical progress and R-01. Slice02 specifies
runtime/commands, original ODM visual inventory, distribution, guide chapters
and maintenance/UAT scenarios. The handoff stays held during this discussion.

Guide examples must explain exact manual edits, dependent updates, document
revision/history, source reconciliation, validation and regeneration without ODM.
Adopt prospectively in Project06 and Lykn; leave closed history and source snapshots
unchanged. Exact schema fields, compatibility and migration details remain design
work. The status tree and existing consumer requirements below still apply.


Date: 2026-09-06. Status: accepted constraints plus proposed architecture;
not the completed Slice01 contract. Authority: operator conversation and
[project plan](../../../project-plan.md).

## Accepted shape

```text
<planning-worktree>/status/
  status.json
  status.html                 # Saga View: all projects in this repository
  scripts/
  templates/
  schemas/
  <project-id>/
    project-status.json
    project-status.html
    <arc-id>/
      arc-status.json
      arc-status.html
```

The consuming repository owns the entire toolkit copy, including its runtime
dependency declaration. Source lives under `knowledge/project-management/` in
ai-engineering. Examples already have a sibling directory there. Project names
need not encode release versions; arc IDs are opaque stable identities, not a
number parser or dependency order. Saga is a collection/view, not an implied
new saga ledger or automatic parent acceptance operation.

## Proposed design to resolve in Arc01

- A shared schema vocabulary plus `status.schema.json`,
  `project-status.schema.json`, and `arc-status.schema.json`. Choose a schema
  dialect, explicit identity/version mechanism and local resolution rules.
  Schema-format versions describe the format; the owning skill version remains
  exclusively in metadata and sibling history under the repository contract.
- Status records supply meaning, not arbitrary CSS classes. Template logic
  selects color, labels, evidence pips and gate displays from defined semantics.
  Preserve the original visual language without copying every trial field.
- Model evidence strength and source references explicitly. Allow unknown or
  unassessed states; define reported versus independently verified observations.
  A render timestamp cannot stand in for the date evidence was checked.
- Compute quantities where the source collection is complete. Where details
  are optional or unknown, define explicit coverage and avoid false precision.
  A parent has its own closure criteria; a count of completed children cannot
  establish them. Standalone slices may contribute directly to a project.
- Discover every `*status.json` under the selected root. Define how document
  kind is resolved and how unsupported names, duplicate IDs, references,
  optional child pages, cycles and inconsistent parent summaries are reported.
- Validation checks structure and consistency; it does not infer world truth
  from Markdown or run arbitrary commands contained in evidence fields.
- Render static navigable HTML from validated data with shared local templates.
  Define missing-field errors, escaping, optional sections, deterministic output,
  freshness checking, and safe handling of links and customisation. Keep the
  current font choices optional for offline use. Preserve Frontier, Instrument,
  Spine and arc detail; remove unsupported “computed” or “all clear” claims.
- Candidate command responsibilities: initialise/copy a complete toolkit;
  validate a selected tree; render all/selected pages; check output freshness;
  inspect provenance and an explicit upgrade. Exact command names and whether
  upgrade is documentation or executable tooling remain design decisions.
- Use a source revision and file manifest for copied-toolkit provenance, with
  documented local modifications. Do not add a duplicate skill-version authority
  inside guides, scripts, or templates. Pin dependency expectations and define
  compatible/incompatible upgrade and migration behavior.

## First-consumer acceptance matrix

These are required cases; concrete records and expected outcomes belong in the
Slice01 contract cases and later executable fixtures/UAT packet.

| Observed Lykn case | Required truthful representation |
| --- | --- |
| Historical MVP with approximate arcs and no reconstructed slices | Archive/provenance qualification; unknown counts; no invented verified closure |
| Active alignment project with 19 top-level arcs | Dense project views; clear drilldown and dependencies without hiding rows |
| Decimal IDs such as arc16.1 and arc16.2 | Preserve IDs; do not infer dependency or chronology from numeric sorting |
| Language evolution with three direct slices and no arcs | Project status works without manufactured arc wrappers or arc pages |
| C-target research seed with no slice implementation yet | Research/scoped state without promising a delivery date or treating zero work as complete |
| Hardware track with live measurements and partially edited records | Evidence type/provenance remains explicit; record snapshot state; never trigger operations |
| Migration implemented while operator review remains pending | Mechanical evidence and acceptance state remain visibly distinct |
| Planned releases shared by projects, and an explicit null target | Release is metadata, not identity or project ordering |
| Evidence in release branches or another repository | Explicit qualified references; no hidden dependence on one author's absolute paths |
| All projects and all open arcs at adoption | Refresh census, distinguish archived/closed/no-detail cases, disclose unresolved classifications |

## UAT and feedback loop

Arc04 opens with a pinned consumer/toolkit baseline, refreshed scope census,
adoption instructions, and a finding/request register in its opening slice's
`artifacts/`. Record ID, date, reporter, consumer and toolkit revisions, affected
view/record/command, expected/observed behavior, evidence, defect versus feature
request, impact, disposition/rationale, destination slice or arc, and retest
result. Sanitize any consumer evidence before including it in public packages.

Triage can accept a fix or extension, seek clarification, reject with rationale,
or defer with a destination and re-entry condition. Accepted changes amend the
relevant plan/ledger and get scoped implementation plus regression coverage.
If larger than a slice, bubble to the project roadmap; no fixed trial slice
count suppresses feature requests. After a changed toolkit is copied into Lykn,
record migration/local-modification handling and rerun affected validation,
rendering, and operator UAT. Preserve the old snapshot for comparison.

The first successful render is an adoption milestone. Project closure requires
the agreed UAT cases, disposition of all requests, retesting of accepted changes,
final package checks, and explicit operator acceptance. Do not claim consumer
acceptance from synthetic examples or schema validity alone.

## Version history

### 1.0.0 — 2026-09-06

Initial design/review record; subsequent operator notices were added during the
2026-09-10 discussion. Historical checks apply to their recorded inputs only.

### 1.1.0 — 2026-09-11

Expanded the live brief with ODM research, all-document metadata, separate version
axes, manual-maintenance guides and the Slice03 → Slice01 → Slice02 dependency order.
