# CC Prompt: Arc05 Slice03 Package Validation And Install Smoke

You are CC implementing Project05 Arc05 Slice03 in Expedited Mode.

## Required Reading

Read these first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/arc-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/ledger.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice01-package-targets-and-support-directories/cdc-verification.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice02-docs-and-discoverability/cdc-verification.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice03-package-validation-and-install-smoke/slice-plan.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice03-package-validation-and-install-smoke/ledger.md`
- Source files: `Makefile`, `README.md`, `docs/skill-library.md`, `docs/building-and-installing.md`, `docs/knowledge-library-anatomy.md`, `assets/packaging/path-exceptions.tsv`, `knowledge/document-extraction/SKILL.md`, and `knowledge/concept-cards/SKILL.md`.

## Task

Run the package-local and install-oriented acceptance work for
`document-extraction` and `concept-cards`.

At minimum:

- run `make check-package-paths` and record whether hard failures or relevant
  warnings appear;
- inspect both generated package archives after the package-path gate rebuilds
  them;
- run an isolated install smoke with a temporary destination, for example
  `INSTALL_DIR=<temp-dir> make install`;
- inspect installed `document-extraction/` and `concept-cards/` directories
  for entrypoint, sibling `version-history.md`, `guides/`, `templates/`,
  `examples/`, and `concept-cards/references/`;
- reconcile installed/package contents against README/docs claims from Slice02;
- record explicit Arc06 closure inputs, including any accepted package warnings,
  remaining project-level gates, and final validation evidence.

## Out Of Scope

Do not add new skill content, new docs discoverability, or new Makefile package
wiring unless a validation failure requires a narrow correction. Do not add
executable validators, JSON Schema, runtime services, graph/ontology databases,
GraphRAG integration, CCDP services, live-corpus extraction, memory runtime
work, CI/release publishing, `knowledge/concept-card-method/`, or
`knowledge/source-preparation/`.

## Required Validation

Run and record:

- `make check-package-paths`;
- `make check-skills`;
- `make check-skill-versions`;
- `make -s print-skill-zips`;
- direct archive inspection for `target/skills/document-extraction.zip` and
  `target/skills/concept-cards.zip`;
- isolated install smoke with `INSTALL_DIR=<temp-dir> make install`;
- direct installed-tree inspection for both new skills;
- targeted grep over README/docs/source claims for stale package/install or
  runtime overclaims;
- `git diff --check`;
- source and planning `git status --short --untracked-files=all`.

## Commit Discipline

Before committing, inspect `git status --short --untracked-files=all`. Commit
only intended source files with explicit pathspecs. Do not commit generated
`target/`, `build/`, or temporary install artifacts.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

After the source commit, update this slice ledger and add a
`closing-report.md` in this slice directory, then commit only those planning
files with explicit pathspecs. Mark the close as CC proposed-done pending CDC
verification. If no source commit is needed because all validation passes
without source changes, say so explicitly in the closing report.
