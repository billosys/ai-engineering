# Arc05 validation command inventory

## Purpose

This inventory records validation commands for Arc05 vocabulary work. Slice01
is read-only, so only source status and planning validation are required to
close this slice. Later source wording slices should run the source validation
set proportional to their edit scope.

## Read-Only Slice01 Commands

Source status:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short --untracked-files=all
```

Result for Slice01 inventory: clean output.

Planning whitespace check:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

Result: run after artifact creation and before commit.

Ledger verifier commands:

```sh
rg -n "public language surface map|README.md|docs/|SKILL.md|knowledge/.*/SKILL|package metadata|protocol|support|current wording" artifacts/current-public-language-surface-map.md
rg -n "classification evidence synthesis|external ontology rubric|Arc01|Arc02|Arc03|Arc04|skill kind|topology|atomic|composite|evidence status|not accepted taxonomy" artifacts/classification-evidence-synthesis.md
rg -n "terminology decision question register|skill kind|topology|atomic|composite|examples|avoid-list|planned surfaces|re-entry conditions|Slice02" artifacts/terminology-decision-question-register.md
rg -n "source edit impact map|README.md|docs/|SKILL.md|package-facing|source-files-edited: false|no source edit|authorization boundary|later slices" artifacts/source-edit-impact-map.md
rg -n "Arc05 validation command inventory|git status --short|wording scan|README/docs links|make check-skills|make check-package-paths|make all|make ccdp-package|make check-ccdp-package|planning git diff --check" artifacts/arc05-validation-command-inventory.md
test -f closing-report.md && rg -n "Rows: 6|Done: 6|source checkout|planning checkout|Bubble-Up to Arc05|Slice02|silent-drop|no source commit" closing-report.md
```

## Wording Scan Commands

Current wording scan:

```sh
rg -n "skill|skills|domain|tooling|framework|operational|method|protocol|support|template|atomic|composite|package|knowledge|docs/|CCDP|collaboration-framework|concept-card|Biome|Rust" README.md docs SKILL.md protocols/ccdp/README.md templates/GUIDE.md
```

Entrypoint and package metadata scan:

```sh
rg -n "^(name|description|version|metadata|license):|INSTALL_ZIPS|ALL_SKILL_FILES|CF_FILES|pack_skill|\\.zip|ccdp" Makefile SKILL.md knowledge/*/SKILL*.md protocols/ccdp/README.md templates/GUIDE.md
```

Focused heading / route wording scan:

```sh
rg -n "^#|^##|skill kind|topology|atomic|composite|domain|tooling|framework|operational|method|protocol|support|template|package" docs/*.md README.md
```

## README/docs Links

README/docs links should be checked after any source wording edit that changes
links or route labels:

```sh
rg -n "\[[^\]]+\]\([^\)]+\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs
```

Run the local Markdown link checker used in Arc04 if links change.

## Package and Build Gates

For README/docs-only wording with no package-input changes:

```sh
git diff --check
make check-skills
```

For SKILL.md, knowledge/*/SKILL*.md, Makefile, package-facing wording, or
package-link changes:

```sh
make check-skills
make check-package-paths
make all
```

For CCDP protocol wording or package-facing CCDP changes:

```sh
make ccdp-package
make check-ccdp-package
```

## Final Checks for Source-Edit Slices

Later Arc05 source-edit slices should finish with:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short --untracked-files=all
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning status --short --untracked-files=all
```

planning git diff --check is the required planning-side whitespace gate for
Slice01 and later planning packets.
