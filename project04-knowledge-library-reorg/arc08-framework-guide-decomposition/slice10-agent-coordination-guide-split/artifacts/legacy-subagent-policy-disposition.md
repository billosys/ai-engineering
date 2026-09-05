# Legacy Subagent Policy Disposition

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
artifact: legacy-subagent-policy-disposition
source_commit: 9e2d5d055712efb53028ef250091d70487a257a0
```

## Disposition

`knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md` was moved
with an explicit `git mv` to:

- `knowledge/agent-coordination/guides/01-when-to-delegate.md`

The moved file was then semantically extracted into three companion guides.
Because the moved file was heavily rewritten during extraction, Git records the
committed diff as an old-path deletion plus new guide additions rather than as
a high-similarity rename. The operation still used the required explicit move
path before editing.

No copy of the old path was retained.

## Live Route Status

The old `SUBAGENT-DELEGATION-POLICY.md` path is not a live source route after
Slice10.

Remaining source mentions are limited to:

- explicit standing guidance that the old path is not live;
- current release-note disposition text;
- collaboration-framework version-history disposition text;
- old `RELEASE-0.2.0.md` historical release-note text.

## Package Disposition

The rebuilt `target/skills/collaboration-framework.zip` contains:

- `collaboration-framework/knowledge/agent-coordination/guides/01-when-to-delegate.md`
- `collaboration-framework/knowledge/agent-coordination/guides/02-context-packets.md`
- `collaboration-framework/knowledge/agent-coordination/guides/03-result-integration.md`
- `collaboration-framework/knowledge/agent-coordination/guides/04-anti-patterns.md`

It does not contain:

- `collaboration-framework/knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`

No package-path exception was needed for the old path.
