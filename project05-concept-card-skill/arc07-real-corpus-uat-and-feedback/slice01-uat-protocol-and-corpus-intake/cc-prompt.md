# CC Prompt: Arc07 Slice01 UAT Protocol And Corpus Intake

You are CC implementing Project05 Arc07 Slice01 in Expedited Mode.

## Required Reading

Read these first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/arc-plan.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/ledger.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/slice-plan.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/ledger.md`
- Source skill entrypoints: `knowledge/document-extraction/SKILL.md` and `knowledge/concept-cards/SKILL.md`
- Source skill guides most likely relevant to intake: `knowledge/document-extraction/guides/01-load-contract.md`, `knowledge/document-extraction/guides/03-output-contract.md`, `knowledge/document-extraction/guides/06-html-and-converted-markdown.md`, `knowledge/concept-cards/guides/01-load-contract.md`, `knowledge/concept-cards/guides/02-operator-workflow.md`, and `knowledge/concept-cards/guides/03-extraction.md`.

## Task

Prepare the real-corpus UAT run before any card generation. Use the
`CompCogNeuro/book` textbook repository at:

```text
https://github.com/CompCogNeuro/book
```

At minimum, write these artifacts under:

```text
project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/artifacts/
```

- `corpus-intake.md`
- `uat-protocol.md`
- `pilot-sampling-plan.md`
- `rag-handoff-assumptions.md`

The artifacts must record:

- source URL and exact commit/ref or supplied snapshot identity;
- license and attribution implications;
- file inventory for chapter Markdown, frontmatter, endmatter, glossary,
  references, metadata, and figures;
- source-preparation approach for already-Markdown input;
- UAT research questions, decisions, measures, evidence to collect, stop
  conditions, known confounds, and limitations;
- pilot sample rationale, including at least one principles section and one
  memory-relevant or memory-protocol-relevant section after inventory;
- RAG/graph/MCP handoff assumptions and boundaries.

Do not vendor the full textbook corpus into the planning tree unless the
operator explicitly approves it. If network access is unavailable, use an
operator-provided local clone/archive or stop with a clear request for one.

## Out Of Scope

Do not generate the full concept-card set in this slice. Do not edit source
skills unless the operator explicitly asks for an immediate correction. Do not
build a production graph database, GraphRAG system, MCP server, memory runtime,
or external release.

This slice may identify those downstream runtime needs, but it must keep them
separate from Project05's current source-skill UAT unless a later slice
explicitly expands scope.

## Required Validation

Run and record:

- direct inspection of the four expected artifacts;
- a check that the source snapshot identity and license are recorded;
- a check that UAT questions/measures are defined before generation;
- a check that RAG handoff assumptions preserve runtime boundaries;
- `git diff --check`;
- source and planning `git status --short --untracked-files=all`.

## Commit Discipline

Before committing, inspect `git status --short --untracked-files=all`. Commit
only intended planning files with explicit pathspecs. Do not commit generated
`target/`, `build/`, temporary clones, or full corpus material.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

After authoring the artifacts, update this slice ledger and add a
`closing-report.md` in this slice directory, then commit only those planning
files with explicit pathspecs. Mark the close as CC proposed-done pending CDC
verification. Do not write `cdc-verification.md`.
