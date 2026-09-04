# Source Validation Results

Source commit: `d3d1f5a` (`Clarify expedited mode and move PM history`)

## Commands

All commands were run from `/Users/oubiwann/lab/billosys/ai-engineering`
unless noted.

### `git diff --check`

Result: passed.

Output: no output.

### Local README/docs/AGENTS/SKILL Link Validation

Checked touched Markdown routes in:

- `AGENTS.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/project-management/SKILL.md`
- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `knowledge/project-management/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

Result: passed.

Output:

```text
local link check: checked 67 local links, 0 missing
```

### `make check-skills`

Result: passed.

Output:

```text
>> all skill descriptions within limit
```

### `make collab-framework`

Result: passed.

Key package evidence:

```text
collaboration-framework/knowledge/project-management/version-history.md
```

The old package path
`collaboration-framework/knowledge/project-management/guides/version-history.md`
was absent from the generated archive listing.

### `make check-package-paths`

Result: passed.

Summary:

```text
package path check
zips scanned: 12
markdown files scanned: 178
hard failures: 0
warnings: 339
explicit exceptions: 3
skipped external URLs: 656
parser-suppressed material: omitted by Markdown parser
```

The warnings are existing warning-class package-path findings accepted by the
validator; the required gate result is zero hard failures.

## Final Source Status

After source commit `d3d1f5a`, `git status --short --ignored=no` in the source
checkout produced no output.

