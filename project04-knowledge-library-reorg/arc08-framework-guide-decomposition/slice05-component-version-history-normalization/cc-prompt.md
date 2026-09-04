# CC Prompt: Arc08 Slice05 Component Version-History Normalization

You are CC working in Project04 Arc08 Slice05.

## Required Reading

Read these before editing:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice05-component-version-history-normalization/slice-plan.md`
- `arc08-framework-guide-decomposition/slice05-component-version-history-normalization/ledger.md`
- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/cdc-verification.md`
- `arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- Source `AGENTS.md`
- Source `knowledge/collaboration-framework/SKILL.md`

## Assignment

Implement Slice05 exactly as scoped: normalize remaining framework component
version histories for:

- `knowledge/work-verification/`
- `knowledge/testing/`
- `knowledge/code-auditing/`
- `knowledge/agent-coordination/`
- `knowledge/contribution-style/`

For each component, inspect current `SKILL.md`, `guides/`, `templates/`, and
`examples/` surfaces before editing. Create or update the sibling
`version-history.md` file at the component root, move or reconcile embedded
`## Version History` material there, and update routes/package lists only where
the normalization makes that necessary.

Do not split guide bodies in this slice. In particular, do not split:

- `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
- `knowledge/code-auditing/guides/CODE-AUDIT.md`
- `knowledge/testing/guides/CODE-COVERAGE.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`

Instead, record those broader split proposals in
`artifacts/deferred-guide-decomposition-register.md` for later operator review.
This is intentional: Expedited Mode means no inferred source scope and no
reduction or other change in scope.

## Required Artifacts

Create these planning artifacts:

- `artifacts/current-remaining-history-surface-map.md`
- `artifacts/version-history-normalization-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/deferred-guide-decomposition-register.md`
- `artifacts/source-validation-results.md`

Update:

- `ledger.md`

Create:

- `closing-report.md`

Do not create `cdc-verification.md`.

## Validation

Run the slice ledger verifier commands and record results in
`artifacts/source-validation-results.md` and `closing-report.md`.

At minimum, source validation must include:

- source `git diff --check`
- focused local Markdown link validation for touched route surfaces
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- generated `collaboration-framework.zip` inspection confirming expected
  sibling histories are present and no new guide-local component history files
  were created

Run package builds sequentially. Do not commit generated zips, `build/`, or
`target/skills`.

## Commit Requirements

Use explicit file lists for commits.

If source files change, commit only the exact source files you changed with a
message like:

```text
Normalize component version histories

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit only the exact Slice05 planning files you changed with a message
like:

```text
Complete Project04 Arc08 Slice05

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Final report should include source commit hash if one was created, planning
commit hash, validation summary, any deferred guide-decomposition notes, and
final source/planning cleanliness.
