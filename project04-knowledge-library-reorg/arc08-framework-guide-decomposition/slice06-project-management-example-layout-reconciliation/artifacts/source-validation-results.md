# Source Validation Results

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

Source commit: `df2c33e0d882aa89dbd42da3b87737a822903979`

## Commands

| Check | Result | Evidence |
|-------|--------|----------|
| `git diff --check` | pass | Command exited 0 with no output before source commit. |
| `git diff --cached --check` | pass | Command exited 0 with no output before source commit, including the staged `git mv` rename. |
| Focused local Markdown link validation | pass | `checked_files=6 checked_links=82 missing_links=0`. |
| `make check-skills` | pass | Output: `>> all skill descriptions within limit`. |
| `make collab-framework` | pass | Rebuilt `target/skills/collaboration-framework.zip`; package listing reported 62 files and included `collaboration-framework/knowledge/project-management/examples/01-worked-example-odm.md`. |
| `make check-package-paths` | pass | Command exited 0 after sequential package rebuild. Direct validator summary: `zips scanned: 12`, `markdown files scanned: 193`, `hard failures: 0`, `warnings: 360`, `explicit exceptions: 3`, `skipped external URLs: 656`, `parser-suppressed material: omitted by Markdown parser`. |
| Generated zip inspection | pass | `unzip -Z1 target/skills/collaboration-framework.zip` showed the accepted project-management example path and the eight project-management guide routes. The old package path `collaboration-framework/knowledge/project-management/guides/09-worked-example-odm.md` was absent. |

## Source File List

Source commit `df2c33e0d882aa89dbd42da3b87737a822903979` changed:

- `Makefile`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/project-management/SKILL.md`
- `knowledge/project-management/examples/01-worked-example-odm.md`
- `knowledge/project-management/guides/09-worked-example-odm.md`
- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `knowledge/project-management/version-history.md`

Generated `build/` and `target/skills/` outputs were not committed.
