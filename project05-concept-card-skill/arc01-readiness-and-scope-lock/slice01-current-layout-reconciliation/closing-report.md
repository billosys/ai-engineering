# Closing Report: Slice01 Current Layout Reconciliation

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
status: proposed-done
closed-by: Codex CC
closed-on: 2026-09-06
source-files-edited: false
cdc-verification: not-written-by-cc
```

## Summary

Slice01 produced the current Project05 evidence map needed before source
implementation begins. The slice reconciled Project03 and early Project05
artifacts with the post-Project04 source/package layout, locked the accepted
skill names, stated package surface requirements, and refreshed the
implementation roadmap.

This is CC proposed-done. It is not CDC verification.

## Delivered Artifacts

All required artifacts were created under `artifacts/`:

- `project05-current-source-surface-inventory.md`
- `project05-artifact-relevance-register.md`
- `project05-naming-and-scope-register.md`
- `project05-package-surface-requirements.md`
- `project05-implementation-roadmap-update.md`

## Evidence Read

Required context was read from:

- collaboration-framework, project-management, and work-verification skill
  instructions;
- Project05 `project-plan.md`, project `ledger.md`, Arc01 `arc-plan.md`,
  Arc01 `ledger.md`, Slice01 `slice-plan.md`, and Slice01 `ledger.md`;
- Project05 artifact manifest, operator reorientation, source-preparation
  architecture, fresh Codex handoff prompt, v3.2 source packet, Project03
  packet, and release-context packet;
- Project04 closing report, accepted architecture, and package-target plan;
- current source `README.md`, `docs/skill-library.md`,
  `docs/building-and-installing.md`, `Makefile`,
  `scripts/check-package-paths`, `scripts/check-skill-description.sh`,
  representative live skills, and release skill-zips workflow;
- historical PDF and EPUB source-preparation prompts under `old/dev/`.

All expected files and directories named in the Slice01 prompt were present.

## Key Reconciliation Results

- `document-extraction` is the required live replacement for the earlier
  `source-preparation` name.
- `concept-cards` is the required live replacement for the earlier
  `concept-card-method` name.
- `ontology-engineering` remains reserved for a likely future composite skill.
- The source checkout currently has no `knowledge/document-extraction/`,
  `knowledge/concept-cards/`, `knowledge/source-preparation/`, or
  `knowledge/concept-card-method/` roots, so later arcs must create the two
  accepted roots.
- Project04's current sibling support-directory layout supersedes Project03's
  package workaround that placed templates/examples/reference material under
  `guides/`.
- Current package behavior supports standalone component/method packages with
  root `SKILL.md`, sibling `guides/`, `version-history.md`, optional sibling
  `templates/`, and optional sibling `examples/`.
- If `document-extraction` or `concept-cards` need sibling `reference/` or
  `validation/` directories, the package macro and docs should be updated
  openly rather than hiding those files under `guides/`.

## Row Walk

| Row | Status | Evidence |
| --- | --- | --- |
| S1-1 | done | `artifacts/project05-current-source-surface-inventory.md` cites current source files, package behavior, validation scripts, representative skill roots, and `make print-skill-zips`. |
| S1-2 | done | `artifacts/project05-artifact-relevance-register.md` classifies current Project05 inputs, superseded assumptions, provenance, and allowed deferrals. |
| S1-3 | done | `artifacts/project05-naming-and-scope-register.md` records `document-extraction`, `concept-cards`, and reserved `ontology-engineering`. |
| S1-4 | done | `artifacts/project05-package-surface-requirements.md` states required `SKILL.md`, `guides/`, sibling `templates/`, sibling `examples/`, `version-history.md`, docs, Makefile, zips, install, and validation surfaces. |
| S1-5 | done | `artifacts/project05-implementation-roadmap-update.md` preserves the remaining implementation arcs and disallows deferral of the two required skills. |
| S1-6 | done | Source checkout status was clean before and after this planning-only slice. Final planning checkout changes are limited to Project05 Slice01 artifacts, ledger, and closing report. |

Rows: 6. Done: 6. Deferred: 0. No-op: 0.

## Validation

Validation performed:

- Source checkout status before artifact work:
  `git status --short --untracked-files=all` returned empty.
- Planning checkout status before artifact work:
  `git status --short --untracked-files=all` returned empty.
- Source checkout status after artifact work:
  `git status --short --untracked-files=all` returned empty.
- Planning checkout diff hygiene:
  `git diff --check` passed.
- Focused artifact presence check:
  all five required artifact files exist under the Slice01 artifact home.

Source package gates were not run because this slice did not change source or
package files.

## Bubble-Up To Arc01

Arc01 can use these artifacts to satisfy its readiness and scope-lock rows
after CDC verification:

- A1-1 is supported by `project05-current-source-surface-inventory.md`.
- A1-2 is supported by `project05-artifact-relevance-register.md`.
- A1-3 is supported by `project05-naming-and-scope-register.md`.
- A1-4 is supported by `project05-package-surface-requirements.md`.
- A1-5 is supported by `project05-implementation-roadmap-update.md`.

No remediation slice is required from this CC pass.

## Bubble-Up To Project05

Project05's existing arc roadmap remains valid. Later arcs should use the
current accepted source roots and package names:

- `knowledge/document-extraction/` and `document-extraction.zip`;
- `knowledge/concept-cards/` and `concept-cards.zip`.

The Project03 v4.0 method planning remains valuable input, but later arcs must
apply the Project05 names and the current post-Project04 sibling support
directory layout.

## Closure

Slice01 is proposed-done by CC and ready for CDC verification. No
`cdc-verification.md` was written.
