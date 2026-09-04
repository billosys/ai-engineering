# Source Validation Results

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

Source commit: `657f156c7ad8048e60727275c2eed0d910de7f45`

## Commands

| Check | Result | Evidence |
|-------|--------|----------|
| `git diff --check` | pass | Command exited 0 with no output before source commit. |
| Focused local Markdown link validation | pass | `checked_files=14 checked_links=52 missing_links=0`. |
| `make check-skills` | pass | Output: `>> all skill descriptions within limit`. |
| `make collab-framework` | pass | Rebuilt `target/skills/collaboration-framework.zip`; package listing reported 61 files. |
| `make check-package-paths` | pass | Command exited 0 after sequential package rebuild. Direct validator summary: `zips scanned: 12`, `markdown files scanned: 193`, `hard failures: 0`, `warnings: 358`, `explicit exceptions: 3`, `skipped external URLs: 656`, `parser-suppressed material: omitted by Markdown parser`. |
| Generated zip inspection | pass | `unzip -Z1 target/skills/collaboration-framework.zip` showed sibling histories for `agent-coordination`, `code-auditing`, `collaboration-framework`, `project-management`, `testing`, `engineering-methods`, `work-verification`, and `contribution-style`; no `guides/version-history.md`, `templates/version-history.md`, `AI-CONSTITUTION-SUPPLEMENT`, or `AI-ENGINEERING-METHODOLOGY` package entries were present. |

## Source File List

Source commit `657f156c7ad8048e60727275c2eed0d910de7f45` changed:

- `Makefile`
- `knowledge/agent-coordination/SKILL.md`
- `knowledge/agent-coordination/version-history.md`
- `knowledge/code-auditing/SKILL.md`
- `knowledge/code-auditing/guides/CODE-AUDIT.md`
- `knowledge/code-auditing/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/contribution-style/SKILL.md`
- `knowledge/contribution-style/version-history.md`
- `knowledge/testing/SKILL.md`
- `knowledge/testing/version-history.md`
- `knowledge/work-verification/SKILL.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `knowledge/work-verification/version-history.md`

Generated `build/` and `target/skills/` outputs were not committed.
