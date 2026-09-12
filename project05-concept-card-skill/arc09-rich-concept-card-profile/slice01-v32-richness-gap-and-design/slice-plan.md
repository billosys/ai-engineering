# Slice01 Plan: V3.2 Richness Gap And Design

```yaml
project: project05-concept-card-skill
arc: arc09-rich-concept-card-profile
slice: slice01-v32-richness-gap-and-design
status: open
opened: 2026-09-11
depends-on:
  - arc08-post-uat-closure-refresh
```

## Goal

Design the rich concept-card profile that Project05 now needs before final
closure. This slice compares the live `concept-cards` skill against the
original v3.2 prompts and representative rich card corpora, then records the
exact source updates needed to combine v3.2 usefulness with v4 rigor.

## Artifact Home

Durable Slice01 artifacts live under:

```text
arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/
```

Expected artifacts:

- `rich-profile-gap-analysis.md`
- `rich-profile-design.md`
- `implementation-scope.md`
- `validation-regression-plan.md`

## In Scope

- Re-read the original v3.2 concept-card extraction and re-extraction prompts.
- Re-read the Project03 v3.2-to-v4.0 carry-forward matrix.
- Inspect representative cards from `complete-musician` and Erlang
  `design-scale-erlang-otp`.
- Inspect current `knowledge/concept-cards` templates, guides, examples, and
  references.
- Identify which rich sections should become the default for real-corpus
  concept cards.
- Identify which old behaviors must not return, especially wrapper artifacts,
  weak cleanup, and unclear lifecycle/provenance semantics.
- Produce an implementation plan for Slice02 and a validation/regression plan
  for Slice03.

## Out Of Scope

- Editing source skill files.
- Generating new CompCogNeuro cards.
- Running full-book extraction.
- Performing operator acceptance, semantic verification, reconciliation,
  memory admission, graph/RAG/MCP implementation, or retrieval evaluation.
- Changing `document-extraction` except to identify a future source-preparation
  support need if the design uncovers one.

## Verification

- Confirm every required artifact exists and cites concrete evidence.
- Confirm the design explicitly preserves v4 lifecycle, evidence,
  validation, verification, reconciliation, and memory-admission boundaries.
- Confirm the design routes raw document/source preparation to
  `document-extraction`.
- Confirm implementation scope names the owning files or file groups for
  Slice02.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when Arc09 has an operator-inspectable design for rich
concept-card output and an implementation plan that is ready for CC to execute
without rediscovering the whole Project05 history.
