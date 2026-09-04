# Current Work-Verification Surface Map

## Current Surface Before Editing

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

The pre-edit work-verification component had three files:

- `knowledge/work-verification/SKILL.md`
- `knowledge/work-verification/version-history.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`

`knowledge/work-verification/SKILL.md` was a thin component entrypoint. It
routed directly to `templates/LEDGER-DISCIPLINE.md` and named the component as
the owner of ledger discipline, row-by-row verification, evidence levels, and
the proposed-done versus independently verified distinction.

`knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` was the single
live protocol surface. It contained:

- ledger-discipline overview and lineage;
- Notes for Codex and the CC/CDC/Operator role route;
- invariant ledger format;
- final-status rules;
- evidence strength vocabulary;
- slice/arc/project adaptation table;
- slice-level CC and CDC protocol;
- iteration budget;
- known structural limitation;
- copyable slice ledger template;
- arc-level ledger protocol and copyable arc template;
- project-level ledger protocol and copyable project template;
- failure modes prevented and not prevented;
- component-history pointer.

`knowledge/work-verification/version-history.md` was already normalized as the
sibling component history by Arc08 Slice05.

## Route And Package Surfaces

Pre-edit live routes and package surfaces found by targeted `rg`:

- `Makefile` `CF_FILES` included `knowledge/work-verification/SKILL.md`,
  `knowledge/work-verification/version-history.md`, and
  `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`.
- `knowledge/collaboration-framework/SKILL.md` routed ledgered work to
  `../work-verification/templates/LEDGER-DISCIPLINE.md`.
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
  routed verification protocol work to the same template path.
- `docs/collaboration-framework.md` exposed work verification through the
  template path.
- `docs/ORIGINS.md` linked ledger discipline to the template path.
- `knowledge/project-management/guides/01-scales-of-work.md`,
  `02-canonical-planning-worktree.md`, `03-planning-top-down.md`,
  `04-closing-slices.md`, and `05-closing-arcs.md` contained live
  ledger-discipline links to the template.
- `knowledge/engineering-methods/guides/04-operational-routing.md` and
  `06-source-package-release-gates.md` contained live work-verification links
  to the template.
- `AGENTS.md` discussed ledger evidence but had no focused
  work-verification route.
- `workbench/release-notes/RELEASE-0.5.0.md` described `SKILL.md` as routing
  directly to the template.

## Package Baseline

Slice06 CDC verification recorded the post-Slice06 collaboration-framework
package shape as 62 entries, with project-management worked example under
`knowledge/project-management/examples/01-worked-example-odm.md`.

Slice07 changed that package shape by adding five work-verification guides and
retaining the template as a support asset.
