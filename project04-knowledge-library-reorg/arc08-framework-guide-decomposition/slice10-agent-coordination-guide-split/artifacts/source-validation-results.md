# Source Validation Results

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
artifact: source-validation-results
source_commit: 9e2d5d055712efb53028ef250091d70487a257a0
```

## Validation Summary

| Check | Result |
|-------|--------|
| Source `git diff --check` | Pass. |
| `make check-skills` | Pass: all skill descriptions within limit. |
| Focused local Markdown link validation | Pass: 15 touched Markdown files checked, 148 local links checked, 0 missing. |
| `make collab-framework` | Pass after sandbox escalation allowed normal `build/` and `target/skills/` writes. |
| `make check-package-paths` | Pass after sequential package rebuild: 12 zips scanned, 207 Markdown files scanned, 0 hard failures, 364 warnings, 3 explicit exceptions, 656 skipped external URLs. |
| Direct `collaboration-framework.zip` package-path scan | Pass: 56 Markdown files scanned, 0 hard failures, 119 warnings, 2 explicit exceptions. |
| `collaboration-framework.zip` focused inspection | Pass: all four agent-coordination guides are present; old `SUBAGENT-DELEGATION-POLICY.md` package entry is absent. |

## Zip Shape Evidence

`target/skills/collaboration-framework.zip` contains 77 files after the
Slice10 split.

Focused inspection found:

- `collaboration-framework/knowledge/agent-coordination/guides/01-when-to-delegate.md`
- `collaboration-framework/knowledge/agent-coordination/guides/02-context-packets.md`
- `collaboration-framework/knowledge/agent-coordination/guides/03-result-integration.md`
- `collaboration-framework/knowledge/agent-coordination/guides/04-anti-patterns.md`

Focused inspection did not find:

- `collaboration-framework/knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`

## Notes

- Generated `build/` and `target/skills/` artifacts were produced for
  validation only and were not committed.
- Package-path warnings are warning-class findings already tracked by the
  package validator. The Slice10 acceptance claim is zero hard failures.
