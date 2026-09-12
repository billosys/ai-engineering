# CC Prompt: Project05 Arc09 Slice04

You are working in Expedited Mode on Project05:

```text
project05-concept-card-skill
arc09-rich-concept-card-profile
slice04-package-gates-and-arc-closure-inputs
```

## Read First

Read these planning files before doing any work:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/arc-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/cdc-verification.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/cdc-verification.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/artifacts/rich-profile-regression-review.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/artifacts/validation-check-record.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice04-package-gates-and-arc-closure-inputs/slice-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice04-package-gates-and-arc-closure-inputs/ledger.md`

## Goal

Run final Arc09 gates, inspect generated packages, record accepted warnings and
caveats, and prepare closure inputs for Arc09 and the Arc10 final Project05
closure refresh.

## Required Artifacts

Write these files under:

```text
project05-concept-card-skill/arc09-rich-concept-card-profile/slice04-package-gates-and-arc-closure-inputs/artifacts/
```

- `final-gate-evidence.md`
- `package-inspection.md`
- `arc-closure-inputs.md`

`final-gate-evidence.md` must record commands, results, warning summaries,
and any accepted exceptions.

`package-inspection.md` must inspect `target/skills/concept-cards.zip` for the
Arc09 rich-profile surfaces and confirm `document-extraction` was not silently
coupled to Arc09. Use fresh or verified-current archives.

`arc-closure-inputs.md` must summarize what Arc09 delivered, what caveats
remain, which ledger rows are ready to close, and what Arc10 must refresh.

## Required Gates

Run:

- `make check-skills`
- `make check-skill-versions`
- `make check-package-paths`
- `make all` if needed to refresh archives for inspection
- `git diff --check`
- source and planning `git status --short --untracked-files=all`

## Required Caveats To Preserve

Do not lose these caveats:

- the rich-profile example is synthetic and its traceability paths are
  intentionally non-resolving;
- the historical Erlang comparison card contains a trailing `</content>`;
- Slice03 was same-context structural/comparative review, not semantic
  verification;
- no card was operator-accepted, reconciled, preserved, admitted to memory,
  or written to any runtime;
- no graph/RAG/MCP runtime, retrieval evaluation, or full-book extraction was
  implemented.

## Boundaries

Do not redesign the rich profile unless a final gate exposes a direct blocker.
Do not edit `document-extraction` unless a direct package/scope blocker is
evidenced. Do not claim final Project05 closure; Arc10 owns the final closure
refresh after Arc09 is independently closed.

## Closing

Update the Slice04 ledger rows, write `closing-report.md`, and commit with
explicit pathspecs. Leave the slice as CC proposed-done for CDC verification.
