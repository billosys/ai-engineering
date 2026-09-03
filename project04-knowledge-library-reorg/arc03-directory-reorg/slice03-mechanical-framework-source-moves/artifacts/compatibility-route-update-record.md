# Compatibility Route Update Record

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
artifact: compatibility-route-update-record
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_commit: 99cebae1e98004164e4ea6735c4a68bc60c233da
source-files-edited: true
```

## Decision Re-Entry

Slice03 re-entered the Slice02 no-shim decision because this slice creates the
`knowledge/collaboration-framework/` composer source target.

Result: no-shim remains selected. Top-level SKILL.md remains the authoritative
entrypoint, and its links now route to the moved framework payload under
`knowledge/collaboration-framework/`.

No validated shim or replacement route was required because validation
preserved route compatibility:

- `make check-skills` passed.
- `make collab-framework` passed.
- `collaboration-framework.zip` still has package root
  `collaboration-framework/`.
- `collaboration-framework.zip` still has entrypoint
  `collaboration-framework/SKILL.md`.
- The packaged entrypoint frontmatter begins with
  `name: collaboration-framework`.

## Source Route Updates

| Surface | Change | Route compatibility result |
|---------|--------|----------------------------|
| top-level `SKILL.md` | Updated links to moved framework docs/templates under `knowledge/collaboration-framework/`; bumped version to `1.4.5`. | Top-level `SKILL.md` remains authoritative under the no-shim path. |
| `README.md` | Not touched. | Existing `/collaboration-framework` and `make collab-framework` route remains valid. |
| `AGENTS.md` | Not touched. | Existing instruction to use current `collaboration-framework` skill remains valid. |
| `CLAUDE.md` | Not touched. | Symlink behavior preserved: `CLAUDE.md -> AGENTS.md`. |
| `Makefile` | Updated `CF_FILES` source paths to the moved payload. | `make collab-framework` packages the moved payload. |

## Re-Entry Condition

The no-shim path remains valid for this slice. Re-entry condition for later
Arc03 work: if Slice04 or later source-edit slices split the composer payload
into Project02 specialist component roots, introduce independent framework
component entrypoints, or change package root behavior, they must revisit
whether top-level `SKILL.md` remains authoritative or whether a validated shim
or replacement route is required.

## Boundary

This compatibility route update is not source-edit authorization beyond this
slice. Arc04 owns end-user docs prose. Arc05 owns public vocabulary.
