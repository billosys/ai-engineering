# Legacy CODE-AUDIT Disposition

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice09-code-auditing-guide-split
artifact: legacy-code-audit-disposition
source_commit: 1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6
```

## Disposition

`knowledge/code-auditing/guides/CODE-AUDIT.md` was moved with an explicit
`git mv` to:

- `knowledge/code-auditing/guides/01-audit-scope-and-map.md`

The moved file was then semantically extracted into four companion guides.
Because the moved file was heavily rewritten during extraction, Git records the
committed diff as an old-path deletion plus new guide additions rather than as
a high-similarity rename. The operation still used the required explicit move
path before editing.

No copy of the old path was retained.

## Live Route Status

The old `CODE-AUDIT.md` path is not a live source route after Slice09.

Remaining source mentions are limited to:

- explicit standing guidance that the old path is not live;
- current release-note disposition text;
- component version-history lineage;
- old `RELEASE-0.1.0.md` historical release-note text.

## Package Disposition

The rebuilt `target/skills/collaboration-framework.zip` contains:

- `collaboration-framework/knowledge/code-auditing/guides/01-audit-scope-and-map.md`
- `collaboration-framework/knowledge/code-auditing/guides/02-findings-and-severity.md`
- `collaboration-framework/knowledge/code-auditing/guides/03-scale-aware-auditing.md`
- `collaboration-framework/knowledge/code-auditing/guides/04-modernization-synthesis.md`
- `collaboration-framework/knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md`

It does not contain:

- `collaboration-framework/knowledge/code-auditing/guides/CODE-AUDIT.md`

The package-path exception for the `knowledge/<slug>/SKILL*.md` source-clone
placeholder was moved from the old path to
`knowledge/code-auditing/guides/01-audit-scope-and-map.md`.
