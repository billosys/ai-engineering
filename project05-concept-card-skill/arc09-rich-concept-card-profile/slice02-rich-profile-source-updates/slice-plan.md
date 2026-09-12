# Slice02 Plan: Rich Profile Source Updates

```yaml
project: project05-concept-card-skill
arc: arc09-rich-concept-card-profile
slice: slice02-rich-profile-source-updates
status: cdc-verified
opened: 2026-09-11
depends-on:
  - arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design
```

## Goal

Update the live `concept-cards` source surfaces so real-corpus extraction
defaults to a rich readable card body while preserving the v4 control layer for
identity, provenance, claims, source support, evidence grade, extraction
confidence, validation, verification, reconciliation, preservation, review,
and memory admission.

## Artifact Home

Durable Slice02 artifacts live under:

```text
arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/artifacts/
```

Expected artifacts:

- `source-update-summary.md`
- `validation-evidence.md`

## In Scope

- Update the owning `knowledge/concept-cards` source files named by Slice01's
  `implementation-scope.md`.
- Make the rich real-corpus profile discoverable from `SKILL.md`.
- Update guides so the rich body is the default for real-corpus extraction,
  with explicit applicability reasons for empty or unresolved sections.
- Update `templates/concept-card.md` with the required rich sections and
  v4-aware placeholders.
- Add or revise a representative example showing rich body sections alongside
  linked v4 records, without claiming completed review.
- Update references/review surfaces for rich-section checks, source-specific
  examples, wrapper hygiene, and lifecycle/evidence separation.
- Update `knowledge/concept-cards/version-history.md` and
  `metadata.version` consistently if source changes warrant a skill version
  bump.

## Out Of Scope

- Editing `document-extraction` unless a direct blocker is evidenced and
  recorded.
- Regenerating Arc07 candidate cards or processing the full book.
- Operator acceptance, independent semantic verification, reconciliation,
  preservation, memory admission, runtime graph/RAG/MCP work, retrieval
  evaluation, or memory-system writes.
- Executable validator implementation; Slice03 owns regression proof and
  review evidence.
- Final package inspection and Arc10 closure inputs; Slice04 owns those gates.

## Verification

- Run focused checks appropriate to changed files.
- Run `make check-skills` after metadata/description changes.
- Run `make check-skill-versions` after any skill version/history update.
- Run `make check-package-paths` if Markdown paths or package contents change.
- Run `git diff --check`.
- Inspect source and planning `git status --short --untracked-files=all`.
- Confirm changed files stay within Slice02 scope or document the explicit
  reason for any additional file.

## Exit Criteria

This slice exits when the live `concept-cards` source expresses the rich
real-corpus profile, preserves v4 control boundaries, records version/history
updates if needed, passes required gates, and leaves Slice03 with concrete
regression/proof work rather than unresolved source-design questions.

## CDC Outcome

CDC verified Slice02 on 2026-09-11. Source commit `1d6bbd08` implements the
scoped profile update and the required validation evidence is recorded under
`artifacts/`. Slice03 remains required for targeted regression comparison and
usefulness proof, using the protocol in Slice01's
`validation-regression-plan.md`.
