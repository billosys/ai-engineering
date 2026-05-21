# Extraction Log — Inaka's Erlang Coding Guidelines

Source slug: `inaka-guidelines`
Source: `knowledge/erlang/sources/md/inaka-guidelines/README.md` (single-file mini-book)
Output: `knowledge/erlang/concept-cards/inaka-guidelines/`

| Date       | Phase | Agent       | Cards | Notes |
|------------|-------|-------------|-------|-------|
| 2026-05-20 | 0     | coordinator | —     | Renamed source dir `erlang-guidelines` → `inaka-guidelines` for slug consistency; populated 48 competency questions. |
| 2026-05-20 | 1     | coordinator | —     | Single-file source; no chapter split. Adapted the parallel re-extraction guide: 8 H3 sections treated as "chapters", 64 named guidelines = 64 concept cards. Fresh extraction (no pre-existing cards). |
| 2026-05-20 | 2     | coordinator | 64    | Single-pass extraction (no parallel agents, per user request). One card per `#####` guideline. `chapter_number: null`, `pdf_page: null` (markdown-origin source); `chapter` = section name, `section` = guideline name. |
| 2026-05-20 | 3     | coordinator | 64    | Structural validation, slug/filename consistency, cross-reference and LLM-artifact checks. |

## Adaptation Notes

- The source has no PDF/chapters: `pdf_page` is `null` on every card and
  `chapter_number` is `null` (the doc's divisions are unnumbered sections).
- The `chapter` field carries the H3 section name (e.g. "Source Code Layout"),
  and `section` carries the individual guideline's H5 heading.
- Categories are drawn from the shared `extraction-metadata/erlang-taxonomy.md`.
- Guidelines under "Conventions & Rules" are PR-blocking; those under
  "Suggestions & Great Ideas" are advisory — noted in each card's
  Context & Application section.
