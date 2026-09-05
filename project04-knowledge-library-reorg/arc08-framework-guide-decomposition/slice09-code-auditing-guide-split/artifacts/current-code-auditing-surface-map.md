# Current Code-Auditing Surface Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice09-code-auditing-guide-split
artifact: current-code-auditing-surface-map
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_basis_before_edit: 120c2ceaf26ca656068d9f2ec34c978eefaf04a5
```

## Current Surface Before Slice09

The code-auditing component started Slice09 with this source shape:

- `knowledge/code-auditing/SKILL.md`
- `knowledge/code-auditing/guides/CODE-AUDIT.md`
- `knowledge/code-auditing/version-history.md`

`CODE-AUDIT.md` was the only live code-auditing guide body. It carried audit
setup, language/tool detection, audit-map construction, all-scale review,
report output contracts, severity classes, file:line finding format,
per-language report structure, top-level index structure, modernization
synthesis, cross-language hunt lists, negative findings, diagnosis-only stance,
and the component-history pointer.

## Live Route References Before Edit

The pre-edit route scan found live references to the old audit guide in:

- `knowledge/code-auditing/SKILL.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/project-management/guides/08-maintenance.md`
- `docs/collaboration-framework.md`
- `docs/ORIGINS.md`
- `workbench/release-notes/RELEASE-0.5.0.md`
- `Makefile` `CF_FILES`
- `assets/packaging/path-exceptions.tsv`

`AGENTS.md` had testing route guidance from Slice08 but no code-auditing route
guidance yet.

## Route Families Checked

The required source route families were checked before editing:

- `code-auditing`: live owner of the monolith.
- `collaboration-framework`: composer route table and component route guide.
- `engineering-methods`: operational route table.
- `project-management`: maintenance guide cross-reference to audit output
  homes.
- `work-verification`: no live `CODE-AUDIT.md` reference found.
- `testing`: no live `CODE-AUDIT.md` reference found.
- public docs and release notes: old path present in current 0.5.0 release
  notes and public framework route table.
- packaging: old path present in `Makefile` `CF_FILES`; old exception present
  for the audit guide's source-clone `knowledge/<slug>/SKILL*.md` placeholder.

## Package Surface Before Edit

Before Slice09, `collaboration-framework.zip` included
`collaboration-framework/knowledge/code-auditing/guides/CODE-AUDIT.md` through
the `CF_FILES` list. The accepted Arc08 target requires replacing that package
entry with the five numbered code-auditing guides.
