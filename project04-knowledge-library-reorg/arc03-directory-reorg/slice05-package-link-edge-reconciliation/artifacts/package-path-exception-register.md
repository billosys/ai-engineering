# Package-Path Exception Register

Date: 2026-09-02
Slice: Arc03 Slice05 package/link edge reconciliation
Source file reviewed: `package-path-exceptions.tsv`

## Register Policy

This package-path exception register records the current persistent warning and
explicit exception disposition after Arc03 Slice04 moves. The Slice05 policy is
repair before exception: do not add a broad exception when a package-local link
or package list can be repaired. Persistent warning families remain an operator
gate for later ownership decisions.

No broad exception was added in Slice05.

## Current Rows

| Package | Kind | Owner | Reason | Validation command | Re-entry condition |
|---------|------|-------|--------|--------------------|--------------------|
| `rust-guidelines.zip` | persistent warning | rust-guidelines | README mentions `guides/cli/09-common-pitfalls.md`, but the package does not currently include that guide. | `make check-package-paths` | `later-rust-guide-maintenance` |
| `rust-guidelines.zip` | persistent warning | rust-guidelines | CLI README mentions `09-common-pitfalls.md`, but the package does not currently include that guide. | `make check-package-paths` | `later-rust-guide-maintenance` |
| `cpp-guidelines.zip` | persistent warning | cpp-guidelines | Param-passing guide references image assets not packaged in the current C++ skill zip. | `make check-package-paths` | `later-cpp-asset-maintenance` |
| `javascript-deno-guidelines.zip` | persistent warning | javascript-deno-guidelines | Deno shorthand reference remains warning-only pending JS guide harmonisation. | `make check-package-paths` | `later-js-guide-harmonisation` |
| `javascript-deno-guidelines.zip` | persistent warning | javascript-deno-guidelines | Biome shorthand reference remains warning-only pending JS guide harmonisation. | `make check-package-paths` | `later-js-guide-harmonisation` |
| `collaboration-framework.zip` | explicit exception | collaboration-framework | `knowledge/code-auditing/CODE-AUDIT.md` intentionally references `knowledge/<slug>/SKILL*.md` as a cross-skill pattern, not a concrete package-local file. | `make check-package-paths` | `none` |
| `collaboration-framework.zip` | explicit exception | collaboration-framework | Top-level `SKILL.md` intentionally references `knowledge/<domain>/SKILL.md` as a pattern. | `make check-package-paths` | `none` |
| `go-guidelines.zip` | explicit exception | go-guidelines | `SKILL.md` preserves workbench skills-accepted historical/source reference. | `make check-package-paths` | `none` |

## Slice05 Disposition

`package-path-exceptions.tsv` required no Slice05 edit. Existing persistent
warning rows and explicit exception rows remain narrow, named, and command
validated by `make check-package-paths`.

Operator gate: any future persistent warning promotion, warning acceptance after
implementation close, or broader path pattern still requires explicit operator
approval.
