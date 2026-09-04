# Current Component Layout and Reference Map

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice01-component-entrypoint-contract
status: proposed-done
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source_edits: none
```

## Scope

This current component layout map records root SKILL.md, named component roots,
adjacent testing/work-verification surfaces, README/docs/root-SKILL
references, Makefile CF_FILES/ALL_SKILL_FILES, and package-path exception
surfaces before any Arc07 source move.

## Source Status

Pre-work source status:

```text
git status --short --untracked-files=all
<clean>
```

This slice is read-only against the source checkout.

## Current Component Roots

Live source files under the operator-named component roots:

| Root | Current files | Current legacy dirs | Initial classification |
| --- | --- | --- | --- |
| repository root | `SKILL.md` | none | Current collaboration-framework package/source entrypoint. Move source entrypoint to `knowledge/collaboration-framework/SKILL.md`; package must still expose `collaboration-framework/SKILL.md`. |
| `knowledge/agent-coordination/` | `docs/SUBAGENT-DELEGATION-POLICY.md` | `docs/` | Component has long policy material but no component-root `SKILL.md`. |
| `knowledge/code-auditing/` | `docs/CODE-AUDIT.md` | `docs/` | Component has long working-practice prompt but no component-root `SKILL.md`. |
| `knowledge/collaboration-framework/` | `docs/AI-CONSTITUTION-SUPPLEMENT.md` | `docs/` | Component/root should own the relocated collaboration-framework `SKILL.md`; long supplement should become guide material. |
| `knowledge/contribution-style/` | `docs/CONTRIBUTION-STYLE.md`; `templates/CONTRIBUTION-TICKET.md` | `docs/`, `templates/` | Component has long style guide and reusable ticket template; no component-root `SKILL.md`. |
| `knowledge/engineering-methods/` | `docs/AI-ENGINEERING-METHODOLOGY.md` | `docs/` | Component has long methodology guide but no component-root `SKILL.md`. |
| `knowledge/project-management/` | `docs/PROJECT-MANAGEMENT.md`; `docs/pm/*.md` | `docs/`, `docs/pm/` | Component has a wayfinder plus detailed PM files. Target should use component-root `SKILL.md` plus `guides/`. |

Adjacent surfaces requested by the prompt:

| Root | Current files | Recommendation |
| --- | --- | --- |
| `knowledge/testing/` | `docs/CODE-COVERAGE.md` | Include in the same contract because `testing` is part of the collaboration-framework package and has the same stale `docs/` holdover shape. Add a concise component-root `SKILL.md`; move long material to `guides/CODE-COVERAGE.md`. |
| `knowledge/work-verification/` | `templates/LEDGER-DISCIPLINE.md` | Include only for component-root entrypoint addition and reference updates. Keep `templates/LEDGER-DISCIPLINE.md` because it is explicitly routed as a reusable verification template/protocol surface and is not a `docs/` holdover. |

## Makefile Package Surfaces

Current Makefile package facts:

- `ZIP_OUTPUT_DIR := target/skills`
- `PACKAGE_PATH_EXCEPTIONS := assets/packaging/path-exceptions.tsv`
- `ALL_SKILL_FILES` currently includes repository-root `SKILL.md` plus domain
  and linter entrypoints; it does not include component-root entrypoints
  because they do not exist yet.
- `CF_FILES` currently starts with repository-root `SKILL.md`.
- `CF_FILES` currently includes these framework component paths:
  - `knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md`
  - `knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md`
  - `knowledge/project-management/docs/PROJECT-MANAGEMENT.md`
  - `knowledge/project-management/docs/pm/01-scales-of-work.md`
  - `knowledge/project-management/docs/pm/02-canonical-planning-worktree.md`
  - `knowledge/project-management/docs/pm/03-planning-top-down.md`
  - `knowledge/project-management/docs/pm/04-closing-slices.md`
  - `knowledge/project-management/docs/pm/05-closing-arcs.md`
  - `knowledge/project-management/docs/pm/06-confirmation-protocol.md`
  - `knowledge/project-management/docs/pm/07-anti-patterns.md`
  - `knowledge/project-management/docs/pm/08-maintenance.md`
  - `knowledge/project-management/docs/pm/09-worked-example-odm.md`
  - `knowledge/project-management/docs/pm/version-history.md`
  - `knowledge/code-auditing/docs/CODE-AUDIT.md`
  - `knowledge/testing/docs/CODE-COVERAGE.md`
  - `knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md`
  - `knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md`
  - `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
  - `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

## README/docs/root-SKILL References

Current public and source references requiring later repair:

- `README.md` links to `./SKILL.md` and labels repository-root `SKILL.md` as
  the collaboration-framework skill entrypoint.
- `docs/skill-library.md` links `collaboration-framework.zip` to `../SKILL.md`.
- `docs/knowledge-library-anatomy.md` says the top-level collaboration
  framework entrypoint remains `SKILL.md` and routes to `knowledge/`
  component roots.
- `docs/repository-overview.md` describes `SKILL.md` as the top-level
  collaboration-framework composite framework/operational entrypoint.
- `docs/collaboration-framework.md` links the composer skill to `../SKILL.md`
  and links component material under `knowledge/*/docs/` or `templates/`.
- `docs/ORIGINS.md` links to several component `docs/` paths and to
  `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`.
- Root `SKILL.md` links internally to the current component `docs/` paths and
  `templates/` paths.

## Package-Path Exceptions

Current package-path exceptions live at:

`assets/packaging/path-exceptions.tsv`

Current collaboration-framework package exceptions:

- `collaboration-framework.zip`,
  `knowledge/code-auditing/docs/CODE-AUDIT.md`,
  `knowledge/<slug>/SKILL*.md`: explicit exception for a source-clone skill
  discovery placeholder.
- `collaboration-framework.zip`, `SKILL.md`,
  `knowledge/<domain>/SKILL.md`: explicit exception for a source-clone domain
  skill layout placeholder.

Later source moves must update these rows if the owning documents move to
`guides/` or if the relocated collaboration-framework source entrypoint changes
the package-local document path.

## Read-Only Verification

Final source status after inspection:

```text
git status --short --untracked-files=all
<clean>
```

No source edits, package generation, or generated artifact commits were made in
this slice.

