# Entrypoint Relocation Report

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice02-collaboration-framework-entrypoint-relocation
status: proposed-done
source_commit: a97aaa6a0682791304bd62cbbeee0b7e4d63fc6f
```

## Entrypoint Relocation

Source commit `a97aaa6a0682791304bd62cbbeee0b7e4d63fc6f` implements the
entrypoint relocation with an explicit `git mv`:

`SKILL.md -> knowledge/collaboration-framework/SKILL.md`

The repository root `SKILL.md` is absent after the move, and
`knowledge/collaboration-framework/SKILL.md` is present as the canonical
collaboration-framework source entrypoint.

## Source Commit

Source commit:

`a97aaa6a0682791304bd62cbbeee0b7e4d63fc6f`

Subject:

`Relocate collaboration framework source entrypoint`

The source commit includes both required co-author trailers:

- `Co-authored-by: Codex <noreply@openai.com>`
- `Co-authored-by: Billo AI <ai-engineering@billo.systems>`

## Authorized Source Files

Changed source files:

- `Makefile`
- `README.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/repository-overview.md`
- `docs/skill-library.md`
- `SKILL.md -> knowledge/collaboration-framework/SKILL.md`
- `scripts/stage-skill-entrypoint`

No component docs moved in this slice. No component-root `SKILL.md` files were
added for other framework components. `docs/ORIGINS.md` and
`assets/packaging/path-exceptions.tsv` were inspected but unchanged because no
direct moved-entrypoint source link or stale exception row required edits.

Generated zips and `build/` output were excluded from the source commit.
