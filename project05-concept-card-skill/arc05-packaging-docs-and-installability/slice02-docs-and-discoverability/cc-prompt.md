# CC Prompt: Arc05 Slice02 Docs And Discoverability

You are CC implementing Project05 Arc05 Slice02 in Expedited Mode.

## Required Reading

Read these first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/arc-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/cdc-verification.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice02-docs-and-discoverability/slice-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice02-docs-and-discoverability/ledger.md`
- Source files: `README.md`, `docs/skill-library.md`, `docs/building-and-installing.md`, `docs/knowledge-library-anatomy.md`, `Makefile`, `knowledge/document-extraction/SKILL.md`, and `knowledge/concept-cards/SKILL.md`.

Treat historical Project03 and early Project05 names as evidence only. The live
skill names are `document-extraction` and `concept-cards`.

## Task

Update the public repository docs so both new method skills are discoverable as
current installable packages with accurate package/build/install boundaries.

At minimum, make sure the docs cover:

- `document-extraction.zip` sourced from `knowledge/document-extraction/SKILL.md`;
- `concept-cards.zip` sourced from `knowledge/concept-cards/SKILL.md`;
- the focused targets `make document-extraction` and `make concept-cards`;
- the aggregate `make skills`, `make all`, `make print-skill-zips`, and
  `make install` behavior where those docs discuss package building or
  installation;
- support-directory shape: entrypoint, sibling `version-history.md`, `guides/`,
  `templates/`, `examples/`, and explicitly packaged support directories such
  as `concept-cards/references/`;
- the boundary that Slice03 still owns package-path validation, isolated
  install smoke, installed-content inspection, and final package/docs
  reconciliation.

Remove or replace stale planned-method language. In particular, public docs
must not leave readers thinking `concept-card-method` or `source-preparation`
are the live implementation destinations, or that the Project05 method skills
are still merely planned.

## Out Of Scope

Do not redo Slice01 Makefile package wiring unless a docs check exposes a
narrow necessary correction. Do not complete Slice03 package-path validation,
isolated install smoke, installed-content inspection, or final package
reconciliation in this slice.

Do not add executable validators, JSON Schema, runtime services, graph/ontology
databases, GraphRAG integration, CCDP services, live-corpus extraction, memory
runtime work, CI/release publishing, `knowledge/concept-card-method/`, or
`knowledge/source-preparation/`.

## Required Validation

Run and record:

- a targeted grep over README/docs for stale `concept-card-method`,
  `source-preparation`, `planned method`, `not packaged`, `future Arc05`, or
  equivalent wording, with explicit disposition of any historical references;
- a source Markdown link check or repository-native equivalent for changed docs;
- `make check-skills`;
- `make check-skill-versions`;
- `git diff --check`.

If you edit `SKILL.md` files, also run the relevant
`scripts/check-skill-description.sh` checks and update sibling
`version-history.md` according to the repository skill-version contract.

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
