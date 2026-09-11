# CC Iteration 01 Prompt: Arc05 Slice01 Stale Package-Boundary Wording

You are CC for Project05 Arc05 Slice01. Slice01 did not pass CDC verification.
Do not create `cdc-verification.md`; CDC owns that after the next
proposed-done report.

## Read First

Read:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/arc-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/slice-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/closing-report.md`
- `Makefile`
- `knowledge/document-extraction/SKILL.md`
- `knowledge/document-extraction/version-history.md`
- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/version-history.md`

## CDC Findings

CDC reproduced the package-target and archive evidence:

- `make document-extraction` passed and produced `target/skills/document-extraction.zip`.
- `make concept-cards` passed and produced `target/skills/concept-cards.zip`.
- Serial archive inspection found `document-extraction/` has `SKILL.md`,
  `version-history.md`, `guides/`, `templates/`, and `examples/`.
- Serial archive inspection found `concept-cards/` has `SKILL.md`,
  `version-history.md`, `guides/`, `templates/`, `examples/`, and
  `references/`.
- `make check-skills` passed.
- `make check-skill-versions` passed with 22 source skills, 22 packages, and
  0 errors.
- `git diff --check` passed.

CDC initially saw an empty `concept-cards/templates/` directory only because
CDC incorrectly ran the two focused Make targets in parallel; both targets
share `build/`. The serial rerun corrected that. Do not chase that as a source
bug unless you intentionally choose to make parallel package builds safe in a
later, separately scoped change.

The actual Slice01 blocker is stale live-guide wording. Row S1-4 requires
source/package wording to stop falsely saying package targets, generated zips,
or `concept-cards/references/` package support remain future after this slice.
The following live guide hits still say or imply that broader package support
remains future Arc05 work:

```text
knowledge/document-extraction/guides/01-load-contract.md
knowledge/document-extraction/guides/04-pdf-source-preparation.md
knowledge/document-extraction/guides/05-epub-source-preparation.md
knowledge/concept-cards/guides/01-load-contract.md
knowledge/concept-cards/guides/03-extraction.md
knowledge/concept-cards/guides/04-re-extraction-preservation.md
knowledge/concept-cards/guides/08-validation-verification.md
```

Historical `version-history.md` entries can retain what was true at the time;
do not rewrite history merely to satisfy the grep. Current live guide wording
must distinguish what Slice01 actually delivered from what remains:

- package targets and generated zips now exist for both skills;
- `concept-cards/references/` is now included in the generated
  `concept-cards.zip`;
- README/docs discoverability remains Slice02 work;
- package-path validation, isolated install smoke, and final package
  reconciliation remain Slice03 work;
- no executable validator, JSON Schema, runtime service, live-corpus
  extraction, graph/ontology database, GraphRAG integration, CCDP service, or
  memory runtime work has been added.

## Required Fix

Update only the stale live guide wording needed to satisfy S1-4. Keep the edit
bounded; do not do Slice02 docs/discoverability, Slice03 install smoke, package
path validation, or runtime work in this iteration.

Because guide text changes are skill changes, update the affected skill
metadata and sibling histories according to the repository skill-version
contract. Use conservative micro bumps unless you find a reason for a larger
change.

## Required Verification

Run and record:

```text
scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md
scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/document-extraction
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/concept-cards
make document-extraction
make concept-cards
unzip -l target/skills/document-extraction.zip
unzip -l target/skills/concept-cards.zip
make check-skills
make check-skill-versions
git diff --check
```

Also run a targeted stale-wording grep over the live guide files, excluding
historical version entries, and confirm no live guide still says package
targets, generated zips, or `references/` package support remain future.

## Required Report

Update `ledger.md` and `closing-report.md` in this slice directory with the
new attested evidence.

In the closing report, add an Iteration 01 note that includes:

- the CDC finding;
- the exact files changed;
- the new skill versions;
- the commands rerun;
- whether any ledger row disposition changed;
- whether the Bubble-up to the arc changed.

Then report back to CDC with revised proposed-done status and the source and
planning commit hashes.
