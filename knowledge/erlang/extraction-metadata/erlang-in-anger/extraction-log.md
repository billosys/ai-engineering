# Extraction Log — Stuff Goes Bad: Erlang in Anger

Fresh extraction (no prior card inventory). Process: parallel structure of
`docs/dev/concept-cards/0010-...-v3.2.md` with the fresh-source workflow of
`docs/dev/concept-cards/0009-...-v3.2.md`. 3 parallel Opus agents (book is
small — 9 chapters, ~2,400 lines).

| Date | Phase | Agent | Cards | Notes |
|------|-------|-------|-------|-------|
| 2026-05-20 | 0 | coordinator | — | 48 competency questions written; shared `erlang-taxonomy.md` reused (categories/tiers/notation). |
| 2026-05-20 | 1 | coordinator | — | Source analysis + CQ-to-chapter mapping (`cq-chapter-mapping.md`); 3 balanced agent assignments. |
| 2026-05-20 | 2 | Agent 1 (Opus) | 36 | Introduction + Ch 1-3 ("Writing Applications": Diving / Building / Overload). |
| 2026-05-20 | 2 | Agent 2 (Opus) | 28 | Ch 4-6 (Connecting / Runtime Metrics / Crash Dumps). |
| 2026-05-20 | 2 | Agent 3 (Opus) | 30 | Ch 7-9 (Memory Leaks / CPU & Scheduler Hogs / Tracing). |
| 2026-05-20 | 3 | coordinator | 94 | Validation passed (see below). |

## Phase 3 validation results

- **Total cards**: 94, in `knowledge/erlang/concept-cards/erlang-in-anger/`.
- **Per-chapter**: intro 1; ch1 10; ch2 10; ch3 15; ch4 6; ch5 16; ch6 6; ch7 17; ch8 6; ch9 7.
- **Frontmatter**: all required fields present in all 94 cards. ✓
- **Slug/filename**: all 94 match. ✓
- **Cross-references**: 90 unique referenced slugs; 89 resolve to cards. 1
  intentional cross-source dangling ref — `otp-behaviour` (from
  `sys-module-introspection.md`): a foundational OTP concept this book
  deliberately does not define ("assumes the reader is proficient in basic
  Erlang and the OTP framework"). Left as a planned-card reference owned by
  another erlang source. ✓ (no broken intra-source refs)
- **LLM artifacts**: none. ✓
- **CQ coverage**: every card lists ≥1 competency question; all 48 CQs map to
  ≥1 chapter (see `cq-chapter-mapping.md`). ✓
- **Confidence distribution**: 88 high / 6 medium / 0 low. Skewed high — the
  source is unusually explicit and didactic, so most concepts have clear
  source definitions; agents flagged the genuinely synthesis-heavy ones
  (`included-application`, `time-sensitive-buffer`, `distribution-cookie`,
  `sys-module-introspection`, `match-specification`, `horizontal-scaling-for-cpu`)
  as medium. No low-confidence cards — acceptable for a source of this kind.
- **Category spread**: production-ops 45, performance 14, applications-releases 13,
  distribution 6, anti-patterns 5, tooling 4, data-types 3, fault-tolerance 2,
  otp-behaviours 2.
