# Source Validation Results

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
artifact: source-validation-results
created-by: CC
created-on: 2026-09-05
source_commit: f96c30266b892fa67185f03046b6662326df0481
```

## Validation Summary

| Check | Result |
|---|---|
| Source `git diff --check` | Pass. |
| `make check-skills` | Pass: all skill descriptions within limit. |
| Focused local Markdown link validation | Pass: 13 touched Markdown files checked, 139 local links checked, 0 missing. |
| `make collab-framework` | Pass after sandbox escalation allowed normal `build/` and `target/skills/` writes. |
| `make check-package-paths` | Pass: 12 zips scanned, 208 Markdown files scanned, 0 hard failures, 366 warnings, 3 explicit exceptions, 656 skipped external URLs. |
| `collaboration-framework.zip` focused inspection | Pass: both contribution-style guides and retained ticket template are present; old `CONTRIBUTION-STYLE.md` package entry is absent. |

## Package Inspection

`target/skills/collaboration-framework.zip` contains 78 files after the
Slice11 split.

Focused zip inspection found:

- `collaboration-framework/knowledge/contribution-style/guides/01-contribution-style.md`
- `collaboration-framework/knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`
- `collaboration-framework/knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

Focused zip inspection did not find:

- `collaboration-framework/knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`

## Source Commit

Source commit:

`f96c30266b892fa67185f03046b6662326df0481`

Commit message includes required trailers:

- `Co-authored-by: Codex <noreply@openai.com>`
- `Co-authored-by: Billo AI <ai-engineering@billo.systems>`
