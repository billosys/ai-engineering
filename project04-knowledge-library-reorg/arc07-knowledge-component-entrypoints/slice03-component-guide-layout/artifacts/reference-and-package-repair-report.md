# Reference and Package Repair Report

Source commit: `0b0f363a4070df09f1bcf7b225f4cd0db018baeb`

## Reference Repairs

Slice03 reviewed README/docs/AGENTS/component references and repaired the
affected paths to the accepted component entrypoint and guide paths:

- `README.md` was included in the authorized source scope review; no direct
  component path edit was required in the final committed diff.
- `AGENTS.md` now tells planning sessions to read
  `knowledge/project-management/SKILL.md` and
  `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`, then load
  relevant `knowledge/project-management/guides/` files.
- Public docs that reference collaboration-framework component material now
  point to `guides/` paths.
- Component guides and templates were updated from legacy `docs/` and
  `docs/pm/` references to source-valid `guides/` paths.
- The Slice02 bubbled engineering-methods `../SKILL.md` concern is resolved by
  the new `knowledge/engineering-methods/SKILL.md`; the existing relative link
  now resolves to the component-root entrypoint from
  `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`.

## Package Repairs

`Makefile` package lists were updated:

- `ALL_SKILL_FILES` includes the seven new component-root `SKILL.md` files so
  `make check-skills` validates their metadata descriptions.
- `CF_FILES` includes the component `SKILL.md` files, moved `guides/` files,
  and unchanged templates.

`scripts/stage-skill-entrypoint` now stages the collaboration-framework root
entrypoint from source-local `./guides/` paths to package-local
`./knowledge/collaboration-framework/guides/` paths. Sibling component links
remain package-local through the existing collaboration-framework transform
table.

`assets/packaging/path-exceptions.tsv` was updated for the moved code-auditing
guide path. The retained exception is still narrow: it covers a repo-only
provenance placeholder for source-clone skill discovery, not a literal bundled
package path.

## Package-Local Behavior

Generated package inspection confirmed `collaboration-framework.zip` contains:

- `collaboration-framework/SKILL.md`
- `collaboration-framework/knowledge/<component>/SKILL.md`
- moved long component documents under
  `collaboration-framework/knowledge/<component>/guides/`
- unchanged templates under
  `collaboration-framework/knowledge/<component>/templates/`

The generated package has no collaboration-framework component holdovers under
legacy `knowledge/<component>/docs/` paths.
