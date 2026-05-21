# Extraction Log — Erlang Programming Rules and Conventions

Source slug: `programming-rules`
Source: `knowledge/erlang/sources/md/programming-rules/README.md` (single-file mini-book)
Output: `knowledge/erlang/concept-cards/programming-rules/`

| Date       | Phase | Agent       | Cards | Notes |
|------------|-------|-------------|-------|-------|
| 2026-05-20 | 0     | coordinator | —     | Fresh extraction (no pre-existing cards). 40 competency questions written; taxonomy from shared `erlang-taxonomy.md`. |
| 2026-05-20 | 1     | coordinator | —     | Single-file source; no chapter split. Sections 3-10 treated as "chapters" (`chapter_number` = the document's own section number). 56 numbered rules + 1 common-mistakes card + 1 required-documents card = 58 cards. |
| 2026-05-20 | 2     | coordinator | 58    | Single-pass extraction (no parallel agents — single-file mini-book, matching the inaka-guidelines precedent). One card per numbered rule. `pdf_page: null` (HTML-origin source); `chapter` = section title, `section` = rule heading. |
| 2026-05-20 | 3     | coordinator | 58    | Structural validation, slug/filename consistency, cross-reference and LLM-artifact checks. |

## Adaptation Notes

- HTML-origin source (Ericsson document EPK/NP 95:035): `pdf_page` is `null` on
  every card; citations use the document's section numbers.
- `chapter_number` is the document section number (3-10); `chapter` holds the
  section title; `section` holds the individual rule's numbered heading.
- Sections 9 (common mistakes) and 10 (required documents) are condensed into
  one card each — their sub-items are recaps / thin stubs in the source.
- Categories drawn from the shared `extraction-metadata/erlang-taxonomy.md`.
