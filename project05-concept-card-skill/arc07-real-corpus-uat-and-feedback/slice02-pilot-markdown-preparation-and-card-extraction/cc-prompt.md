# CC Prompt: Arc07 Slice02 Pilot Markdown Preparation And Card Extraction

You are CC implementing Project05 Arc07 Slice02 in Expedited Mode.

## Required Reading

Read these first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/arc-plan.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/ledger.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/cdc-verification.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/artifacts/corpus-intake.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/artifacts/uat-protocol.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/artifacts/pilot-sampling-plan.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/artifacts/rag-handoff-assumptions.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/slice-plan.md`
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/ledger.md`
- Source skills: `knowledge/document-extraction/SKILL.md` and `knowledge/concept-cards/SKILL.md`, plus the relevant guides/templates they route to for Markdown preparation, output contracts, extraction, source support, validation, and review packets.

## Task

Run the bounded pilot against the pinned `CompCogNeuro/book` source. Acquire
commit:

```text
e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d
```

Use a temporary checkout or archive outside the planning tree. Do not vendor
the full corpus. Prepare and extract only the declared pilot sample:

- `chapter-01.md`: Introduction, The Computational Approach, Emergent
  Phenomena;
- `chapter-07.md`: Memory, Episodic Memory, Hippocampus pattern
  separation/completion, and memory consolidation.

Write durable artifacts under:

```text
project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/
```

Expected artifacts:

- `source-acquisition.md`
- `prepared-source-manifest.md`
- `structure-map.md`
- `locator-map.md`
- `validation-readiness.md`
- `candidate-cards/`
- `extraction-run.md`
- `pilot-review-packet.md`
- `friction-log.md`

Generate a deliberately small, reviewable candidate set. Preserve source
identity, locators, evidence grade, extraction confidence, validation state,
verification state, reconciliation state, and memory-admission boundaries.
Figures, citations, and cross-references must be directly inspected or
explicitly caveated; do not silently promote them to support.

The candidate set is not operator-accepted unless the operator actually
reviews it. If no operator review occurs in this slice, mark candidates as
requiring operator review and prepare the review packet.

## Out Of Scope

Do not run the whole corpus. Do not resolve the entire bibliography or review
all figures. Do not edit source skills unless the operator explicitly approves
a narrow correction. Do not build a graph database, GraphRAG flow, MCP server,
vector store, memory runtime, retrieval evaluation, or memory write.

## Required Validation

Run and record:

- source identity check for the temporary checkout/archive;
- artifact inspection for all expected files/directories;
- a scope check showing only the declared pilot sample was prepared/extracted;
- a locator/support check over generated candidates;
- a dependency check for figures/citations/cross-references;
- a review-boundary check showing candidates are not operator-accepted,
  verified, or admitted unless that actually occurred;
- `git diff --check`;
- source and planning `git status --short --untracked-files=all`.

## Commit Discipline

Before committing, inspect `git status --short --untracked-files=all`. Commit
only intended planning artifacts with explicit pathspecs. Do not commit
temporary checkouts, downloaded full-corpus material, generated package
artifacts, or unrelated planning work.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

After authoring artifacts, update this slice ledger and add a
`closing-report.md` in this slice directory, then commit only those planning
files with explicit pathspecs. Mark the close as CC proposed-done pending CDC
verification. Do not write `cdc-verification.md`.
