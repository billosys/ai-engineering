# Slice03 Plan: Regression Examples And Validation

```yaml
project: project05-concept-card-skill
arc: arc09-rich-concept-card-profile
slice: slice03-regression-examples-and-validation
status: cc-proposed-done
opened: 2026-09-11
depends-on:
  - arc09-rich-concept-card-profile/slice02-rich-profile-source-updates
```

## Goal

Prove that the rich profile implemented in Slice02 restores the useful
v3.2-style reader/reference shape without weakening v4 lifecycle, evidence,
relationship/CQ, validation, verification, reconciliation, preservation, or
memory-admission boundaries.

## Artifact Home

Durable Slice03 artifacts live under:

```text
arc09-rich-concept-card-profile/slice03-regression-examples-and-validation/artifacts/
```

Expected artifacts:

- `rich-profile-regression-review.md`
- `validation-check-record.md`

## In Scope

- Compare the rich template and synthetic rich-profile example against
  `complete-musician/applied-chord.md` and
  `knowledge/erlang/concept-cards/design-scale-erlang-otp/application-behaviour.md`
  as evidence, not schemas.
- Compare the rich profile against at least one Arc07 thin candidate shape to
  show what improved and what remains out of scope.
- Check required-section presence, applicability reasons, source-specific
  richness, wrapper hygiene, typed relationship/CQ discipline, and
  lifecycle/evidence separation.
- Record findings in durable artifacts that Slice04 can use for package/arc
  closure inputs.
- Make narrow source corrections only if a regression check exposes a direct
  blocking issue in the Slice02 implementation.

## Out Of Scope

- Broad source redesign of `concept-cards`.
- Editing `document-extraction`.
- Regenerating Arc07 cards, processing the full book, or accepting candidate
  cards.
- Independent semantic verification of a real corpus, reconciliation,
  preservation, memory admission, runtime graph/RAG/MCP work, retrieval
  evaluation, or memory-system writes.
- Final package inspection and Arc09 closure; Slice04 owns those gates.

## Verification

- Inspect the rich template and synthetic example for required-section
  coverage and applicability reasons.
- Inspect the named prior rich examples and at least one Arc07 candidate for
  regression comparison evidence.
- Search checked rich-profile source/example material for wrapper artifacts:
  `Wait`, `Let me recalculate`, `I apologize`, `As an AI`, and whole-card
  response envelopes.
- Run focused checks for any source edits.
- Run `make check-skills`, `make check-skill-versions`, `make check-package-paths`
  if source or package-relevant paths change.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.

## Exit Criteria

This slice exits when the regression review and validation check record show
whether the Slice02 implementation restores the intended rich-card affordances
without weakening v4 controls, and when any direct blockers are either fixed
or routed explicitly before Slice04.

## CC Outcome

CC proposed-done on 2026-09-11. The regression artifacts find no direct source
blocker, so no `concept-cards` source file changed. The review records the
historical Erlang wrapper residue and the synthetic example's intentionally
non-resolving traceability paths as bounded evidence/caveats for Slice04.
Independent CDC verification remains pending.
