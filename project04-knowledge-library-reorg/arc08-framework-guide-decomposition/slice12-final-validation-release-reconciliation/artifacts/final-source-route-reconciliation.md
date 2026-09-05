# Final Source Route Reconciliation

## Scope

Validated the final Arc08 route surfaces in the source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering` after the Slice12 source repair
commit `6ff611b71ddb5f5a2290966ac8ae139fa81cea07`.

Surfaces read or scanned:

- `README.md`
- `AGENTS.md`
- `Makefile`
- `docs/*.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- sibling component `SKILL.md` and `version-history.md` files for
  `collaboration-framework`, `engineering-methods`, `project-management`,
  `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
  `contribution-style`
- component `guides/`, `templates/`, and `examples/` directories under those
  eight framework component roots
- `assets/packaging/path-exceptions.tsv`
- `protocols/ccdp/README.md`
- `protocols/ccdp/composite-cognition-dispatch-protocol.md`
- `protocols/ccdp/src/README.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

## Current Surface

The current surface is the selective-load guide layout:

- `knowledge/collaboration-framework/SKILL.md` remains the composed framework
  entrypoint and routes through `knowledge/collaboration-framework/guides/`.
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
  routes the eight component roots.
- `project-management`, `work-verification`, `testing`, `code-auditing`,
  `agent-coordination`, and `contribution-style` each route through focused
  component-owned guides, templates, or examples.
- `Makefile` still declares 12 installable skill zips through
  `SKILL_ZIP_NAMES` and keeps `INSTALL_ZIPS` separate from CCDP.
- CCDP remains under `protocols/ccdp/` and is packaged through the protocol
  package targets, not through the skill install set.
- Release notes now describe the final Arc08 guide split, component map,
  package validation, install smoke, and CCDP state.

## Local Markdown Link Validation

Command: local Python Markdown link checker over README, AGENTS, docs,
framework component route files, component guides/templates/examples, and CCDP
README files.

Result:

- local Markdown link validation files: 69
- local Markdown links checked: 428
- skipped links: 1
- missing links: 0

## Source Whitespace Check

Command: `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check`

Result: pass, no whitespace errors reported.

## Source Repair

Concrete defect found: `workbench/release-notes/RELEASE-0.5.0.md` still
reported the older package-path baseline of 171 Markdown files and 310
warnings, and its framework update list lacked the final contribution-style
route bullet.

Repair committed in source:

- Source commit: `6ff611b71ddb5f5a2290966ac8ae139fa81cea07`
- Source file list: `workbench/release-notes/RELEASE-0.5.0.md`
- Change: update package baseline to 208 Markdown files and 366 warnings; add
  contribution-style guide/template route reconciliation.

## Verdict

Pass. README/docs/AGENTS/SKILL/component route surfaces point at the current
selective-load guide layout after the release-note repair.
