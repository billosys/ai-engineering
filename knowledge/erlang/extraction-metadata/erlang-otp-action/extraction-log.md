# Extraction Log — "Erlang and OTP in Action"

Source slug: `erlang-otp-action`
Source: `knowledge/erlang/sources/md/erlang-otp-action/` (EPUB-origin, 14 chapters + 2 appendices)
Output: `knowledge/erlang/concept-cards/erlang-otp-action/`

| Date       | Phase | Agent       | Cards | Notes |
|------------|-------|-------------|-------|-------|
| 2026-05-20 | 0     | coordinator | —     | Fresh extraction (no pre-existing cards). 45 competency questions written; taxonomy from shared `erlang-taxonomy.md`. |
| 2026-05-20 | 1     | coordinator | —     | Chapter inventory built from section headings. 5 balanced agent assignments (sequential chapter groups). |
| 2026-05-20 | 2     | 5x opus     | 250   | Parallel fresh extraction (Ch1-2: 64, Ch3-6: 56, Ch7-9: 52, Ch10-12: 46, Ch13-14+app: 32). EPUB-origin: `pdf_page: null`; citations use section headings. Agents were rate-limited at the end of their runs; all card writes completed (only the final summary messages were lost). |
| 2026-05-20 | 3     | coordinator | 250   | Validation passed: 0 missing frontmatter fields, 0 slug/filename mismatches, 0 missing body sections, 0 duplicate concept names, 0 LLM artifacts. Confidence: 240 high / 9 medium / 1 low. Fixed 11 stray cross-reference slugs (renamed `process`→`erlang-process`, `release`→`erlang-release`, `erlang-port`→`port`, `erlang-list`→`list`; pruned 7 refs to concepts not given their own card). All cross-references now resolve. |

## Agent Assignments (Phase 1)

- Agent 1 — Ch 1-2: The Erlang/OTP platform; Erlang language essentials.
- Agent 2 — Ch 3-6: TCP-based RPC service; OTP applications & supervision;
  graphical introspection tools; implementing a caching system.
- Agent 3 — Ch 7-9: Logging & event handling; distributed Erlang/OTP;
  adding distribution with Mnesia.
- Agent 4 — Ch 10-12: Packaging & deployment; HTTP interface to the cache;
  integrating foreign code with ports and NIFs.
- Agent 5 — Ch 13-14 + Appendices A-B: Erlang/Java via Jinterface;
  optimization & performance; installing Erlang; referential transparency.

## Adaptation Notes

- The book is EPUB-origin, so there are no PDF page numbers: every card has
  `pdf_page: null` and cites by chapter + section heading.
- Each concept is extracted once, in the chapter that primarily defines it;
  later chapters reference the slug rather than re-extracting.
