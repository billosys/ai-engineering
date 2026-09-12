# CC Prompt: Project05 Arc09 Slice01

You are working in Expedited Mode on Project05:

```text
project05-concept-card-skill
arc09-rich-concept-card-profile
slice01-v32-richness-gap-and-design
```

## Read First

Read these planning files before doing any work:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/arc-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/slice-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/ledger.md`

Also read the Arc08 CDC verification so you understand why Project05 remains
active after the post-UAT closure baseline:

- `project05-concept-card-skill/arc08-post-uat-closure-refresh/cdc-verification.md`

## Evidence To Inspect

Inspect the historical and sample evidence without treating old prompts as
current instructions wholesale:

- `project05-concept-card-skill/artifacts/source-v32/source-0009-howto-concept-card-extraction-with-llms-v3.2.md`
- `project05-concept-card-skill/artifacts/source-v32/source-0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`
- `project05-concept-card-skill/artifacts/project03-concept-card-method/arc02-method-inventory/slice02-v40-gap-analysis/artifacts/v32-to-v40-carry-forward-change-matrix.md`
- representative cards from `/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/`
- representative cards from `knowledge/erlang/concept-cards/design-scale-erlang-otp/`
- Arc07 candidate cards under `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/`
- current source files under `knowledge/concept-cards/`

## Goal

Produce a durable design for restoring the useful v3.2 rich-card output
profile inside the live `concept-cards` skill while preserving the v4
lifecycle, provenance, evidence, validation, verification, reconciliation,
review, and memory-admission controls implemented in Project05.

The operator accepted the finding that the current Arc07 candidate cards are
auditable but too thin compared with prior v3.2-style cards. The next source
slice needs a precise design, not another broad rediscovery pass.

## Required Artifacts

Write these files under:

```text
project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/
```

- `rich-profile-gap-analysis.md`
- `rich-profile-design.md`
- `implementation-scope.md`
- `validation-regression-plan.md`

## Artifact Requirements

`rich-profile-gap-analysis.md` must:

- summarize the relevant v3.2 prompt requirements;
- compare at least a few `complete-musician`, Erlang v3.2, and Arc07
  candidate cards;
- identify the useful old sections to carry forward;
- identify retired or unsafe old behaviors, including wrapper artifacts and
  weak lifecycle/provenance separation.

`rich-profile-design.md` must:

- name the required rich-card sections;
- explain how each section coexists with v4 frontmatter, source support,
  claims/evidence, validation, verification, reconciliation, and memory
  admission;
- keep raw document preparation routed to `document-extraction`;
- avoid runtime, graph/RAG/MCP, memory-admission, operator-acceptance, or
  full-book-extraction claims.

`implementation-scope.md` must:

- name the `knowledge/concept-cards` files or file groups expected to change
  in Slice02;
- identify version-history and package/discoverability implications;
- state any `document-extraction` touchpoints as optional follow-up only
  unless the evidence shows a direct blocker;
- leave source edits for Slice02.

`validation-regression-plan.md` must:

- define checks or review criteria for missing rich sections, generic examples,
  wrapper artifacts, and v4 lifecycle/evidence regressions;
- include at least one regression comparison against prior rich-card examples;
- define what Slice03 should prove after Slice02 implementation.

## Boundaries

Do not edit source skill files in this slice. Do not generate new
CompCogNeuro cards. Do not claim full-book extraction, operator acceptance,
semantic verification, memory admission, graph/RAG/MCP runtime implementation,
or retrieval quality.

## Verification

Before closing:

- confirm every required artifact exists;
- confirm the artifacts cite concrete evidence from prompts, samples, and the
  current skill;
- run `git diff --check`;
- inspect source and planning `git status --short --untracked-files=all`;
- update the Slice01 ledger rows;
- write `closing-report.md`.

Leave the slice as CC proposed-done for CDC verification.
