# CC Prompt: Arc05 Slice01 Package Targets And Support Directories

You are CC implementing Project05 Arc05 Slice01 in Expedited Mode.

## Required Reading

Read these first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/arc-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/slice-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/ledger.md`
- Source files: `Makefile`, `README.md`, `docs/skill-library.md`, `docs/building-and-installing.md`, `knowledge/document-extraction/SKILL.md`, `knowledge/document-extraction/version-history.md`, `knowledge/concept-cards/SKILL.md`, `knowledge/concept-cards/version-history.md`, and `knowledge/concept-cards/references/README.md`.

Treat historical Project03/early Project05 artifacts as evidence only. The live
skill names are `document-extraction` and `concept-cards`.

## Task

Wire `document-extraction` and `concept-cards` into the Makefile package
surface so both produce generated zips and are included in aggregate build and
install lists.

The generated packages must include:

- `document-extraction/SKILL.md`
- `document-extraction/version-history.md`
- `document-extraction/guides/`
- `document-extraction/templates/`
- `document-extraction/examples/`
- `concept-cards/SKILL.md`
- `concept-cards/version-history.md`
- `concept-cards/guides/`
- `concept-cards/templates/`
- `concept-cards/examples/`
- `concept-cards/references/`

Update Makefile helper behavior conservatively. Prefer a general rule for
local support directories already used by source skills over a one-off special
case, but keep package contents bounded to intended support directories. Do not
copy `sources/`, `workbench/`, or planning artifacts.

Update source wording only where the new package targets make existing text
false. It is acceptable, and likely necessary, to change "not packaged yet" to
a narrower boundary such as "docs/discoverability and install smoke remain
later Arc05 work." If you edit `SKILL.md`, update the sibling
`version-history.md` according to the repository skill-version contract.

## Out Of Scope

Do not complete README/docs discoverability in this slice unless a small source
wording change is strictly required to avoid a false package claim. Do not run
or claim isolated install smoke as complete. Do not add executable validators,
JSON Schema, runtime services, graph/ontology databases, GraphRAG integration,
CCDP services, live-corpus extraction, or memory runtime work.

## Required Validation

Run and record:

- `scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md`
  if that entrypoint changes.
- `scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md` if
  that entrypoint changes.
- `make document-extraction`
- `make concept-cards`
- `unzip -l target/skills/document-extraction.zip`
- `unzip -l target/skills/concept-cards.zip`
- `make check-skills`
- `make check-skill-versions`
- `git diff --check`

Use the zip listings to confirm the expected support directories are present,
especially `concept-cards/references/`.

## Commit Discipline

Before committing, inspect `git status --short --untracked-files=all`. Commit
only intended source files with explicit pathspecs. Do not commit generated
`target/` or `build/` artifacts.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

After the source commit, update this slice ledger and add a
`closing-report.md` in this slice directory, then commit only those planning
files with explicit pathspecs. Mark the close as CC proposed-done pending CDC
verification.
