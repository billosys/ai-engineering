# Project-Management Version-History Move Map

Source commit: `d3d1f5a` (`Clarify expedited mode and move PM history`)

## Move

Moved with `git mv`:

```text
knowledge/project-management/guides/version-history.md
-> knowledge/project-management/version-history.md
```

The old `guides/version-history.md` file is absent after the move. The new
sibling `version-history.md` file lives beside
`knowledge/project-management/SKILL.md`, matching the approved framework
component history rule.

## Source Route Repairs

Updated routes:

- `knowledge/project-management/SKILL.md`
  - `[Version History](./guides/version-history.md)`
  - became `[Version History](./version-history.md)`.
- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
  - maintenance route now points to `../version-history.md`;
  - split-file index item 10 now points to `../version-history.md`;
  - Version History section now points to `../version-history.md`.
- `Makefile`
  - `CF_FILES` now includes `knowledge/project-management/version-history.md`.
- `workbench/release-notes/RELEASE-0.5.0.md`
  - historical framework document list now names
    `knowledge/project-management/version-history.md`.

## Package Evidence

`make collab-framework` passed after the move. The generated archive contains:

```text
collaboration-framework/knowledge/project-management/version-history.md
```

The generated archive does not list:

```text
collaboration-framework/knowledge/project-management/guides/version-history.md
```

`make check-package-paths` passed with zero hard failures after the route move.

