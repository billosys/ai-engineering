# Arc09 Final Gate Evidence

## Scope

These CC-run gates cover the source baseline containing the Arc09 rich-profile
change and the current repository package configuration. They do not provide
independent CDC verification, semantic verification of a real corpus, operator
acceptance, reconciliation, preservation, memory admission, retrieval
evaluation, or runtime behavior evidence.

## Commands And Results

| Command | Result |
| --- | --- |
| `make check-skills` | Passed: 22 skills are within the enforced description limit. The command reported 15 descriptions over its non-blocking 300-character editorial target. |
| `make check-skill-versions` | Passed: 22 source skills and 22 freshly generated packages, 0 errors. |
| `make check-package-paths` | Passed: 22 ZIPs and 361 Markdown files scanned, 0 hard failures. The target rebuilt the package set serially before scanning. |
| `unzip -tqq target/skills/concept-cards.zip` | Passed. |
| `unzip -tqq target/skills/document-extraction.zip` | Passed. |
| `git diff --check` | Passed before planning close edits. |
| `git -C .worktrees/planning diff --check` | Passed before planning close edits. |
| source and planning `git status --short --untracked-files=all` | Both worktrees were clean before Slice04 planning artifacts were written. |

`make all` was not run separately: both package-producing gates rebuilt the
entire package set, and the path gate was the latest package-producing command.
The inspected archives therefore are fresh for this gate run.

## Package-Path Warnings And Exceptions

The package-path gate reported 568 warnings, 561 unique warning locations, and
three explicit exceptions. It also reported 662 skipped external URLs and
parser-suppressed material omitted by the Markdown parser. Warning categories:

| Category | Count |
| --- | ---: |
| repository-only/provenance | 170 |
| parser false positive | 149 |
| bundled reference | 122 |
| sibling-skill reference | 64 |
| source-clone reference | 35 |
| example-project path | 28 |

The three accepted exceptions are documented source-clone/provenance examples
in `code-auditing`, `collaboration-framework`, and `go-guidelines`. They are
not Arc09 rich-profile paths. The checker reported no hard failure; this slice
does not claim that the aggregate warning inventory is wholly attributable to
or wholly predates Arc09.

## Archive Identity

The final-gate archives were written at 2026-09-12 00:11:55 local time:

| Archive | Entries | SHA-256 |
| --- | ---: | --- |
| `target/skills/concept-cards.zip` | 44 | `4b30219fd728399221922c07fd1d7d24d43f7e66e71bb72a48e38faa2834cf5f` |
| `target/skills/document-extraction.zip` | 28 | `3ef5fcb2d473f866e96fcc725932d09952eb222e9bf3392c5b5dca3a01009aa8` |
