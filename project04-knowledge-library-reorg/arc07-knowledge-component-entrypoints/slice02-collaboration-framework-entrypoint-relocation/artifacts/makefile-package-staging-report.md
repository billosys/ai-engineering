# Makefile Package Staging Report

```yaml
project: project04-knowledge-library-reorg
arc: arc07-knowledge-component-entrypoints
slice: slice02-collaboration-framework-entrypoint-relocation
status: proposed-done
source_commit: a97aaa6a0682791304bd62cbbeee0b7e4d63fc6f
```

## Makefile Updates

`Makefile` now uses the moved source entrypoint in `ALL_SKILL_FILES`:

`knowledge/collaboration-framework/SKILL.md`

`CF_FILES` no longer lists repository-root `SKILL.md`. The
`collab-framework` target validates the moved source entrypoint with
`check-skills` behavior via:

`./scripts/check-skill-description.sh knowledge/collaboration-framework/SKILL.md`

The target stages the moved source entrypoint explicitly as the package root
entrypoint:

`./scripts/stage-skill-entrypoint knowledge/collaboration-framework/SKILL.md "$(CF_STAGE)/SKILL.md"`

The remaining `CF_FILES` are still copied under the generated
`collaboration-framework/knowledge/...` package root.

## Package Root Preservation

`make collab-framework` generated `target/skills/collaboration-framework.zip`
with package root:

`collaboration-framework/`

and package entrypoint:

`collaboration-framework/SKILL.md`

The zip does not contain `collaboration-framework/knowledge/collaboration-framework/SKILL.md`.

## Staging Helper Updates

`scripts/stage-skill-entrypoint` now handles the moved collaboration-framework
source entrypoint as a source/package dual-view file:

- source view uses component-relative links such as `./docs/...` and
  `../engineering-methods/...`;
- package view rewrites those links to package-local `./knowledge/...` links
  when staging `collaboration-framework/SKILL.md`.

The helper also performs one narrow package-only dependency transform for
`knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md`:

- source text remains untouched because that file is outside Slice02's
  authorized source edit list;
- package staging rewrites the dependency's `../SKILL.md` link to
  `../../../SKILL.md`, which points at the generated package root
  `collaboration-framework/SKILL.md`.
