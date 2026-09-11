# Slice02 Plan: Pilot Markdown Preparation And Card Extraction

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
slice: slice02-pilot-markdown-preparation-and-card-extraction
status: cc-proposed-done
opened: 2026-09-11
depends-on:
  - slice01-uat-protocol-and-corpus-intake
```

## Goal

Acquire the pinned `CompCogNeuro/book` source into a temporary workspace,
prepare only the declared Chapter 1 and Chapter 7 pilot sections with
`document-extraction`, generate a small candidate concept-card packet with
`concept-cards`, and record real-use friction without claiming operator
acceptance, memory admission, or runtime retrieval.

## Artifact Home

Durable Slice02 artifacts live under:

```text
arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts/
```

Expected artifact groups:

- `source-acquisition.md`
- `prepared-source-manifest.md`
- `structure-map.md`
- `locator-map.md`
- `validation-readiness.md`
- `candidate-cards/`
- `extraction-run.md`
- `pilot-review-packet.md`
- `friction-log.md`

The temporary checkout or archive must not be committed. Generated card
candidates are planning artifacts for UAT, not admitted memory.

## In Scope

- Obtain the pinned commit
  `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` into a temporary workspace and
  record its identity.
- Prepare only the Slice01 pilot sample:
  - `chapter-01.md`: Introduction, The Computational Approach, Emergent
    Phenomena;
  - `chapter-07.md`: Memory, Episodic Memory, Hippocampus pattern
    separation/completion, and memory consolidation.
- Create source-preparation evidence: manifest, structure map, locator map,
  readiness/caveat record, and dependency notes for citations/figures.
- Generate a deliberately small set of candidate concept-card records,
  source-support records, relationship/CQ candidates when useful, and an
  extraction-run record.
- Record validation findings, unresolved dependencies, friction, missing
  guidance, and candidate review needs.
- Prepare a pilot review packet for the operator, explicitly distinguishing
  candidate cards from operator-accepted cards.

## Out Of Scope

- Whole-corpus extraction or card generation.
- Resolving the entire bibliography or reviewing all figures.
- Treating candidates as verified truth, admitted memory, or accepted operator
  decisions.
- Production graph database, GraphRAG, MCP server, vector store, memory
  runtime, or retrieval evaluation.
- Source-skill edits, unless a blocking defect is discovered and the operator
  explicitly approves a narrow correction in this slice.

## Verification

- Inspect the expected artifacts and candidate-card directory.
- Confirm the acquired source identity matches the pinned commit.
- Confirm only the declared pilot sample was prepared and extracted.
- Confirm locators and source-support records point to inspectable source
  spans or explicit caveats.
- Confirm figures/citations/cross-references are directly inspected or
  explicitly caveated.
- Confirm generated records preserve evidence grade, extraction confidence,
  validation/verification/reconciliation/memory-admission boundaries.
- Confirm the review packet does not claim operator acceptance unless the
  operator actually reviewed the candidates.
- `git diff --check`
- source and planning `git status --short --untracked-files=all`

## Exit Criteria

This slice exits when the pilot source is prepared, a small candidate record
set and review packet are produced, all UAT stop conditions are checked, and
all observed friction is recorded for Slice03 feedback disposition.
