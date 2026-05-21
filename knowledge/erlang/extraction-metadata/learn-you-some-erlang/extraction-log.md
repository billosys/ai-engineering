# Extraction Log — Learn You Some Erlang for Great Good!

Fresh extraction (no prior card inventory). Process: the 4-phase parallel
structure of `docs/dev/concept-cards/0010-...-v3.2.md` with the fresh-source
workflow of `docs/dev/concept-cards/0009-...-v3.2.md`. 5 parallel Opus agents
(doc-0010 default — appropriate for a 30-chapter book).

| Date | Phase | Agent | Cards | Notes |
|------|-------|-------|-------|-------|
| 2026-05-20 | 0 | coordinator | — | 54 competency questions written; shared `erlang-taxonomy.md` reused. |
| 2026-05-20 | 1 | coordinator | — | CQ-to-chapter mapping (`cq-chapter-mapping.md`); 5 agent assignments balanced by source size (~280 KB each). |
| 2026-05-20 | 2 | Agent 1 (Opus) | 50 | Ch 1-7 — Sequential Erlang (data, modules, functions, recursion, errors). |
| 2026-05-20 | 2 | Agent 2 (Opus) | 60 | Ch 8-14 — problem-solving, data structures, concurrency, OTP intro. |
| 2026-05-20 | 2 | Agent 3 (Opus) | 60 | Ch 15-21 — OTP behaviours, applications, releases. |
| 2026-05-20 | 2 | Agent 4 (Opus) | 42 | Ch 22-26 — scaling/code-upgrades, sockets, EUnit, ETS, distributed Erlang. |
| 2026-05-20 | 2 | Agent 5 (Opus) | 32 | Ch 27-30 + Appendix B — distributed OTP, Common Test, Mnesia, Dialyzer. |
| 2026-05-20 | 3 | coordinator | 244 | Validation passed (see below). |

## Notes

- Agents 2 and 3 hit a transient server-side rate limit when emitting their
  final report messages; both had already finished writing all cards to disk.
  Coverage verified post-hoc: every chapter 8-21 is represented with healthy
  card counts.
- Appendix A (Afterword) and Appendix C (Updates) yielded no extractable
  concepts and were skipped; Appendix B (On Erlang's Syntax) → 1 card.
- The book uses `gen_fsm`; cards flag that OTP 27+ supersedes it with
  `gen_statem` (Context & Application / Common Confusions) without forking
  the book's examples.

## Phase 3 validation results

- **Total cards**: 244, in `knowledge/erlang/concept-cards/learn-you-some-erlang/`.
- **Per chapter**: ch1 13, ch2 7, ch3 6, ch4 4, ch5 4, ch6 7, ch7 9, ch8 3,
  ch9 11, ch10 12, ch11 7, ch12 9, ch13 5, ch14 13, ch15 12, ch16 10, ch17 11,
  ch18 4, ch19 11, ch20 4, ch21 8, ch22 5, ch23 9, ch24 5, ch25 7, ch26 16,
  ch27 4, ch28 7, ch29 9, ch30 11; Appendix B 1. (Worked-example-heavy
  chapters — 8, 13, 22 — are intentionally low; agents were told not to pad
  example narration into cards.)
- **Frontmatter**: all required fields present in all 244 cards. ✓
- **Slug/filename**: all 244 match. ✓
- **Cross-references**: 203 unique referenced slugs; after one fix, all
  resolve. Fixed: `rolling-upgrade` (a concept the book does not cover, no
  card) removed from the `contrasts_with` of `relup.md` and
  `hot-code-loading.md`. ✓
- **LLM artifacts**: none. ✓
- **CQ coverage**: every card lists ≥1 competency question; all 54 CQs map to
  ≥1 chapter (see `cq-chapter-mapping.md`). ✓
- **Confidence distribution**: 233 high / 10 medium / 1 low. Skewed high — the
  source is a thorough didactic tutorial with explicit definitions throughout;
  agents flagged the genuinely synthesis-heavy concepts as medium/low.
