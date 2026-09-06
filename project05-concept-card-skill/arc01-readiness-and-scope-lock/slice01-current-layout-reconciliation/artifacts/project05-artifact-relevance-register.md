# Project05 Artifact Relevance Register

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
artifact: project05-artifact-relevance-register
status: cc-produced
date: 2026-09-06
```

## Purpose

This register classifies Project03, early Project05, Project04, and old PDF/EPUB
inputs by current relevance. Historical artifacts remain preserved as evidence,
but they do not override the Project05 plan-of-record or the current source
layout.

## Authority Order

Current authority order for Project05:

1. `project05-concept-card-skill/project-plan.md`
2. Project05 Arc01 and Slice01 open sets
3. `artifacts/operator-accepted-project05-reorientation.md`
4. Project04 close evidence and the live source tree
5. Older Project03 and early Project05 artifacts as provenance

This matches `project05-concept-card-skill/artifacts/README.md`.

## Register

| Artifact | Classification | Current use | Superseded or deferred assumptions |
| --- | --- | --- | --- |
| `project05-concept-card-skill/project-plan.md` | current plan-of-record | Defines Project05 definition of done, nondeferrable objectives, skill names, current boundary, and arc roadmap. | None for this slice. |
| `project05-concept-card-skill/ledger.md` | current project ledger | Records project-level rows P-1 through P-8. | Rows remain open until child arcs provide evidence. |
| `arc01-readiness-and-scope-lock/arc-plan.md` | current arc plan | Defines Slice01 outputs and Arc01 exit criteria. | None for this slice. |
| `arc01-readiness-and-scope-lock/ledger.md` | current arc ledger | Records Arc01 rows A1-1 through A1-5. | Rows remain open until Slice01 is CDC-verified and Arc01 closes. |
| `slice01-current-layout-reconciliation/slice-plan.md` | current slice plan | Defines this slice's scope, out-of-scope boundary, required artifacts, and exit criteria. | Source edits remain out of scope. |
| `slice01-current-layout-reconciliation/ledger.md` | current slice ledger | Rows S1-1 through S1-6 drive this CC close. | No CDC verification row should be written by CC. |
| `artifacts/operator-accepted-project05-reorientation.md` | current operator decision | Locks `document-extraction`, `concept-cards`, future `ontology-engineering`, sibling support directories, and nondeferrable implementation objectives. | Supersedes `source-preparation` and `concept-card-method` as live skill names. |
| `artifacts/operator-accepted-src-prep-arch.md` | current scope input with renamed surface | Preserves the standalone upstream capability for PDF/EPUB/HTML/converted-source preparation now to be implemented as `document-extraction`. | Its planned source root `knowledge/source-preparation/` and name `source-preparation` are superseded by `knowledge/document-extraction/`. Its fallback option to bury templates/examples under `guides/` is superseded by current package support for sibling `templates/` and `examples/`. |
| `artifacts/fresh-codex-project05-planning-prompt.md` | current handoff context | Summarizes the current Project05 direction and directs later sessions to use the plan-of-record and current layout. | It is a resume prompt, not a substitute for the plan and ledgers. |
| `artifacts/source-v32/` | provenance baseline | Preserves the v3.2 extraction and re-extraction source documents that inform `concept-cards`. | v3.2 is not the live implementation target; Project05 targets v4.0-style `concept-cards`. |
| `artifacts/project03-concept-card-method/` | historical planning evidence | Preserves Project03's method inventory, conceptual model, skill architecture, implementation plan, verification gates, and deferral register. | The name `concept-card-method`, the planned source home `knowledge/concept-card-method/`, and the package-compatible choice to place support material under `guides/` are superseded by Project05 and Project04 evidence. |
| `artifacts/release-context/` | historical release/readme context | Preserves release-context snapshots used during Project05 bootstrap. | Current source `README.md`, docs, Makefile, and release workflow are the live evidence. |
| `../project04-knowledge-library-reorg/closing-report.md` | current layout evidence | Confirms Project04 is closed and that `docs/`, `knowledge/`, and `protocols/` now have distinct roles. | Its final validation counts are historical; current source has since added more package targets. |
| `../project04-knowledge-library-reorg/artifacts/operator-accepted-architecture.md` | current architecture precedent | Confirms component-level `SKILL.md`, sibling `version-history.md`, and sibling `guides/`, `templates/`, and `examples/` layout. | It concerns collaboration-framework components, not Project05 skill names. |
| `../project04-knowledge-library-reorg/artifacts/package-target-plan.md` | partially superseded package planning evidence | Useful for Makefile/package/list/release-gate thinking and CCDP separation. | Its older note that specialist packages may need support material under `guides/` is superseded by current `pack_component_skill` behavior. Its note that `collaboration-framework.zip` should not silently vendor every specialist body is superseded by later operator-accepted packaging work that includes framework support material and `scientific-methods`. |
| `old/dev/concept-cards/0011-prompt-prepare-pdf-converted-source-for-indexing-v2.md` | current source material for document-extraction | Provides PDF preparation logic: preserve raw PDFs, use Marker `book.md` and `metadata.json`, normalize image paths, map TOC/page locators, split chapters, and validate outputs. | Its copy-paste prompt shape, per-source helper scripts, `source-preparation` naming, and concept-extraction-only framing must be modernized. |
| `old/dev/concept-cards/0012-prompt-prepare-epub-converted-source-for-indexing-v2.md` | current source material for document-extraction | Provides EPUB preparation logic: preserve raw EPUBs, use pandoc `book.md` and media outputs, derive structure from headings/anchors, split chapters, and validate outputs. | Its copy-paste prompt shape, per-source helper scripts, `source-preparation` naming, and fixed example patterns must be generalized. |

## Project03 Reuse Boundaries

Reusable Project03 content:

- v4.0 conceptual constructs: concept cards, claims, source support, source
  spans/locators, relationship edges, competency questions, extraction runs,
  validation results, verification results, reconciliation results,
  preservation decisions, and memory admission.
- Thin entrypoint plus focused guide routing.
- Distinct template, example, validation, and support-document surfaces.
- Validation split across deterministic structural candidates, semantic
  audit, human/operator review, and deferred runtime checks.
- Deferral discipline for executable validators, runtime services, GraphRAG,
  graph/ontology databases, memory runtime, CCDP service, live extraction, CI,
  and release publication.

Superseded Project03 content:

- Live skill name `concept-card-method`.
- Source root `knowledge/concept-card-method/`.
- Packaging workaround that placed `templates/`, `examples/`, `validation/`,
  and `reference/` under `guides/`.
- README-only close-prep source edit as sufficient for Project05.

## Project05 Reuse Boundaries

Reusable early Project05 content:

- Source preparation as a standalone upstream capability consumed by concept
  cards and also useful for indexing, reading, source review, and analysis.
- PDF and EPUB-specific processing decisions and caveat discipline.
- Output contract ideas: preserved raw inputs, converted Markdown, split
  files, media normalization, structure maps, manifests, validation reports,
  locator model, and readiness status.

Superseded early Project05 content:

- The name `source-preparation`.
- The source root `knowledge/source-preparation/`.
- Any optional package workaround that hides support directories inside
  `guides/`.

## Absent Expected Inputs

All expected files and directories named in the Slice01 `cc-prompt.md` were
present during this CC pass.
