# Slice04 Plan: Package Gates And Arc Closure Inputs

```yaml
project: project05-concept-card-skill
arc: arc09-rich-concept-card-profile
slice: slice04-package-gates-and-arc-closure-inputs
status: cdc-verified
opened: 2026-09-11
depends-on:
  - arc09-rich-concept-card-profile/slice03-regression-examples-and-validation
```

## Goal

Run the final Arc09 source/package gates after the rich-profile source update
and regression proof, inspect generated packages as needed, reconcile Arc09
ledger rows, and prepare the inputs needed for Arc09 closure and Arc10 final
Project05 closure refresh.

## Artifact Home

Durable Slice04 artifacts live under:

```text
arc09-rich-concept-card-profile/slice04-package-gates-and-arc-closure-inputs/artifacts/
```

Expected artifacts:

- `final-gate-evidence.md`
- `package-inspection.md`
- `arc-closure-inputs.md`

## In Scope

- Rerun final repository-local gates needed after Arc09 source/planning work.
- Inspect generated `concept-cards` package contents for the rich template,
  rich-profile example, affected guides, review references, and version
  history.
- Confirm `document-extraction` package shape is not affected by Arc09.
- Reconcile Arc09 ledger rows A9-5 and A9-6.
- Record package-path warnings/exceptions and any accepted caveats, including
  the synthetic example's non-resolving traceability paths and the historical
  Erlang comparison wrapper finding.
- Prepare Arc09 closing-report inputs and Project05/Arc10 handoff notes.

## Out Of Scope

- Additional rich-profile redesign unless a final gate exposes a direct
  blocker.
- Real-corpus semantic verification, operator acceptance, reconciliation,
  memory admission, full-book processing, graph/RAG/MCP runtime work,
  retrieval evaluation, or memory-system writes.
- Formal Project05 closure; Arc10 owns the final project closure refresh after
  Arc09 is independently closed.

## Verification

- Run `make check-skills`.
- Run `make check-skill-versions`.
- Run `make check-package-paths`.
- Run `make all` if package inspection needs freshly generated archives beyond
  the version/path gates.
- Inspect `target/skills/concept-cards.zip` for the Arc09 source surfaces.
- Inspect `target/skills/document-extraction.zip` only to confirm no unintended
  Arc09 coupling.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when final gates and package inspection are recorded, Arc09
package/closure ledger rows have evidence, remaining caveats are explicit, and
the next closure action is ready for CDC arc closure and Arc10 opening.

## CC Outcome

CC proposed-done on 2026-09-12. Fresh package gates and archive inspection
passed without a source blocker. The close artifacts retain the synthetic
traceability, historical wrapper, and non-runtime caveats.

## CDC Outcome

CDC verified this slice on 2026-09-12 by independently reproducing the final
skill, version, package-path, archive-integrity, archive-content, whitespace,
and worktree-hygiene evidence. Arc09 is closed and Arc10 is opened for final
Project05 closure refresh.
