# CC Prompt: Project05 Arc09 Slice03

You are working in Expedited Mode on Project05:

```text
project05-concept-card-skill
arc09-rich-concept-card-profile
slice03-regression-examples-and-validation
```

## Read First

Read these planning files before doing any work:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/arc-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/validation-regression-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/cdc-verification.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/artifacts/source-update-summary.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/artifacts/validation-evidence.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/slice-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/ledger.md`

## Goal

Prove that the Slice02 rich profile restores the useful v3.2-style card
affordances while preserving v4 controls. This is a regression and validation
slice, not a broad source redesign.

## Required Comparisons

Use these as comparison evidence, not schemas:

- `/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/applied-chord.md`
- `knowledge/erlang/concept-cards/design-scale-erlang-otp/application-behaviour.md`
- at least one Arc07 candidate card from
  `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/`

Compare against:

- `knowledge/concept-cards/templates/concept-card.md`
- `knowledge/concept-cards/examples/rich-profile-card.md`
- any Slice02 guide/reference source needed to verify boundaries.

## Required Artifacts

Write these files under:

```text
project05-concept-card-skill/arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/artifacts/
```

- `rich-profile-regression-review.md`
- `validation-check-record.md`

`rich-profile-regression-review.md` must report:

- required-section coverage;
- comparison with `complete-musician/applied-chord.md`;
- comparison with Erlang `application-behaviour.md`;
- comparison with at least one Arc07 candidate shape;
- what is improved, what remains out of scope, and any direct source blocker.

`validation-check-record.md` must report:

- source-specific example traceability;
- wrapper-artifact scan results for `Wait`, `Let me recalculate`, `I apologize`,
  `As an AI`, and whole-card response envelopes;
- typed relationship/CQ discipline;
- lifecycle/evidence separation;
- limits: no semantic verification, no operator acceptance, no memory
  admission, no graph/RAG/MCP runtime, and no full-book claim.

## Source Edits

This slice should be evidence-first. Make source edits only for a narrow,
direct blocker found by the regression checks. If you edit source, update
version/history and run the required gates. If no source edit is needed, say so
explicitly in the closing report.

## Verification

Run:

- focused artifact/path checks;
- wrapper-artifact searches over the checked rich-profile files;
- `git diff --check`;
- source and planning `git status --short --untracked-files=all`;
- if source changed: `make check-skills`, `make check-skill-versions`, and
  `make check-package-paths`.

## Boundaries

Do not regenerate Arc07 cards, process the full book, accept cards,
semantically verify a real corpus, reconcile or admit memory, edit
`document-extraction`, build graph/RAG/MCP/runtime infrastructure, or claim
retrieval quality.

## Closing

Update the Slice03 ledger rows, write `closing-report.md`, and commit with
explicit pathspecs. Leave the slice as CC proposed-done for CDC verification.
