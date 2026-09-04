# Source Reference Repair Report

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice02-collaboration-framework-entrypoint-relocation
status: proposed-done
source_commit: a97aaa6a0682791304bd62cbbeee0b7e4d63fc6f
```

## README And Docs Repairs

Direct source references caused by the moved entrypoint were repaired in:

- `README.md`
- `docs/skill-library.md`
- `docs/knowledge-library-anatomy.md`
- `docs/repository-overview.md`
- `docs/collaboration-framework.md`

Those files now point readers to
`knowledge/collaboration-framework/SKILL.md` when referring to the source
entrypoint.

`docs/skill-library.md`, `docs/knowledge-library-anatomy.md`, and
`docs/collaboration-framework.md` preserve package-local language that the
generated package exposes `collaboration-framework/SKILL.md`.

## Moved Source Entrypoint Links

`knowledge/collaboration-framework/SKILL.md` was repaired for source-local
links after relocation:

- same-component material uses `./docs/...`;
- sibling framework components use `../<component>/...`;
- sibling domain/tooling examples use paths such as `../rust/SKILL.md`,
  `../js/SKILL.md`, and `../biome/SKILL-js-linter.md`.

The file version was bumped to `1.4.8`, and Version History records the source
entrypoint move and package entrypoint preservation.

## Package-Local Link Repair

Package-local link repair was handled in `scripts/stage-skill-entrypoint`.
The generated `collaboration-framework/SKILL.md` uses package-local
`./knowledge/...` links, while source-local links in
`knowledge/collaboration-framework/SKILL.md` remain valid in the source
checkout.

One dependency package-local link was repaired through staging behavior because
the source file is outside this slice's authorized edit list:

`knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md`

## Path-Exception Disposition

`assets/packaging/path-exceptions.tsv` was inspected and left unchanged.
The collaboration-framework exception row still applies to package document
`SKILL.md`, because the generated package entrypoint path remains
`collaboration-framework/SKILL.md`.

No path-exception row was added or widened for this slice.

`docs/ORIGINS.md` was inspected and left unchanged because it did not contain a
direct moved-entrypoint source link requiring repair.
