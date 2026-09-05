# Current Testing Surface Map

## Current Surface Before Editing

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

The pre-edit testing component had three files:

- `knowledge/testing/SKILL.md`
- `knowledge/testing/version-history.md`
- `knowledge/testing/guides/CODE-COVERAGE.md`

`knowledge/testing/SKILL.md` was a thin component entrypoint for test coverage
hardening. It routed directly to `guides/CODE-COVERAGE.md`.

`knowledge/testing/guides/CODE-COVERAGE.md` was the single live guide surface.
It contained:

- hard 95%+ coverage objective;
- Notes for Codex and repository-native command adaptation;
- warnings, lint, and formatting pressure;
- tests-must-pass rule;
- root-cause repair discipline;
- systematic module, integration, edge-case, and error-path coverage process;
- progress reporting template;
- code-type testing strategies;
- obstacle handling;
- coverage report interpretation;
- completion checklist;
- anti-patterns;
- sample test-development session.

`knowledge/testing/version-history.md` was already normalized as the sibling
component history by Arc08 Slice05.

## Route And Package Surfaces

Pre-edit live routes and package surfaces found by targeted `rg`:

- `Makefile` `CF_FILES` included `knowledge/testing/SKILL.md`,
  `knowledge/testing/version-history.md`, and
  `knowledge/testing/guides/CODE-COVERAGE.md`.
- `knowledge/collaboration-framework/SKILL.md` routed hard coverage work to
  `../testing/guides/CODE-COVERAGE.md`.
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
  routed hard coverage work to the same old guide path.
- `knowledge/engineering-methods/guides/04-operational-routing.md` routed
  testing and validation coverage to the old guide path.
- `docs/collaboration-framework.md` exposed Testing through the old guide path.
- `AGENTS.md` had validation rules but no focused testing route guidance.
- `workbench/release-notes/RELEASE-0.5.0.md` already described testing as
  discipline, coverage hardening, and validation gates, but its detailed route
  list did not yet include the three split testing guide paths.

## Package Baseline

Slice07 CDC verification recorded the post-Slice07 collaboration-framework
package shape as 68 entries, with five work-verification guides and retained
`templates/LEDGER-DISCIPLINE.md`.

Slice08 changes that package shape by replacing the single old coverage guide
entry with three numbered testing guide entries.
