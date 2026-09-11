# Slice01 Plan: UAT Protocol And Corpus Intake

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
slice: slice01-uat-protocol-and-corpus-intake
status: cc-proposed-done
opened: 2026-09-11
depends-on:
  - arc06-gate-evidence-and-project-closure
```

## Goal

Prepare a real-corpus UAT run before generating cards. Pin or acquire the
`CompCogNeuro/book` source snapshot, record its license and structure, define
the UAT questions and measures, select the pilot sample, and capture initial
RAG/graph/MCP handoff assumptions for the memory-protocol effort.

## Artifact Home

Durable Slice01 artifacts live under:

```text
arc07-real-corpus-uat-and-feedback/slice01-uat-protocol-and-corpus-intake/artifacts/
```

Expected artifacts:

- `corpus-intake.md`
- `uat-protocol.md`
- `pilot-sampling-plan.md`
- `rag-handoff-assumptions.md`

Do not vendor the whole textbook corpus into the planning tree unless the
operator explicitly approves it. Preserve the source URL and exact snapshot
identity instead; if network access is unavailable, request or use an
operator-provided local clone/archive and record its identity.

## In Scope

- Inspect the `CompCogNeuro/book` repository or supplied clone/archive.
- Record URL, commit/ref or snapshot identity, license, file inventory, and
  relevant source structure.
- Identify which files count as source material for the UAT: chapter Markdown,
  frontmatter/endmatter, glossary, references, metadata, and figures as
  relevant.
- Define UAT questions and measures before generation, including extraction
  friction, locator quality, source-support quality, concept-card completeness,
  validation/verification burden, operator review burden, and RAG usefulness.
- Choose a pilot sample that includes at least one principles section and one
  memory-relevant or downstream-memory-protocol section after corpus inventory.
- Record RAG/graph/MCP handoff assumptions without claiming a production
  runtime exists.

## Out Of Scope

- Full card generation.
- Skill source edits.
- Production graph database, GraphRAG, MCP server, memory runtime, or external
  release work.
- Treating the textbook as admitted memory or verified domain truth merely
  because it is open source.

## Verification

- Inspect the four expected artifacts.
- Confirm the corpus snapshot identity and license are recorded.
- Confirm UAT questions, measures, and stop conditions are written before
  pilot generation.
- Confirm the pilot sample rationale is explicit.
- Confirm RAG handoff assumptions preserve the Project05 runtime boundary.
- `git diff --check`
- source and planning `git status --short --untracked-files=all`

## Exit Criteria

This slice exits when corpus intake, UAT protocol, pilot sampling plan, and
RAG handoff assumptions are complete enough for Slice02 to run a pilot without
inventing hidden context.
