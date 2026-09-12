# CompCogNeuro Rich-Profile Rerun

## Purpose

This workbench packet reruns the same bounded `CompCogNeuro/book` subset used
in Project05 Arc07, using the post-Arc09 `concept-cards` rich real-corpus
profile. It is an evaluation packet, not a Project05 reopening and not a
runtime/memory-ingestion artifact.

## Source Snapshot

- Upstream: `https://github.com/CompCogNeuro/book`
- Pinned commit: `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`
- Local checkout used: `/private/tmp/project05-compcogneuro-book-e0c697b4`
- Included scope:
  - `chapter-01.md` lines 31-60
  - `chapter-07.md` lines 5-166
- Excluded scope:
  - Chapters 2-6 and 8-10
  - Chapter 7 appendix lines 168-184
  - full bibliography resolution
  - full figure audit
  - operator acceptance, semantic verification, reconciliation, preservation,
    memory admission, RAG/MCP/graph ingestion, and full-book coverage

## Output Set

The rerun produced ten candidate cards under `candidate-cards/`, matching the
Arc07 candidate set boundary:

- `cc-model-data-constraints.md`
- `cc-emergent-explanation.md`
- `cc-memory-forms.md`
- `cc-complementary-learning-systems.md`
- `cc-episodic-binding.md`
- `cc-pattern-separation.md`
- `cc-pattern-completion.md`
- `cc-memory-consolidation.md`
- `cc-recognition-dual-process.md`
- `cc-priming-forms.md`

## Comparison

The comparison against the Arc07 baseline is in
`comparison/subset-comparison.md`.
