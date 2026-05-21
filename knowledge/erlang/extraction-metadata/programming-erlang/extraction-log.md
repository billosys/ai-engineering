# Extraction Log — Programming Erlang, Second Edition

> Source: "Programming Erlang, Second Edition" — Joe Armstrong
> source_slug: `programming-erlang`  ·  KB: `erlang`
> Process: `docs/dev/concept-cards/0009` (howto) + `0010` (parallel extraction), v3.2.

## Type

Fresh extraction — no pre-existing card inventory for this source.
EPUB-origin source: `pdf_page` is `null` on all cards; citations use chapter
title + section heading.

## Scope

Chapters 1–27 plus the unnumbered Introduction (28 files). The 3 appendices
(OTP Templates, A Socket Application, A Simple Execution Environment) are
**out of scope** by request — they are reference code listings with little
distinct conceptual content.

## Agent Assignments (Phase 1) — 8 agents

| Agent | Files | Theme |
|-------|-------|-------|
| 1 | 01–05 | Introduction, concurrency, tour, basic concepts, modules & functions |
| 2 | 06–09 | Records & maps, sequential error handling, binaries, rest of sequential |
| 3 | 10–13 | Types, compiling & running, real-world concurrency, concurrent programming |
| 4 | 14–17 | Concurrent errors, distributed programming, interfacing, files |
| 5 | 18–20 | Sockets, websockets, ETS & DETS |
| 6 | 21–22 | Mnesia, profiling/debugging/tracing |
| 7 | 23–24 | Introducing OTP, making a system with OTP |
| 8 | 25–28 | Idioms, third-party programs, multicore, Sherlock's Last Case |

(File numbers 01–28; file 02 = book chapter 1, file N = chapter N−1.)

## Results (Phase 2)

243 concept cards in `concept-cards/programming-erlang/`. The first launch of
the 8 agents was hit by a transient server-side rate limit; agents 4, 7, 8
completed, and agents 1, 2, 3, 5, 6 were re-run to completion. Re-runs
overwrote any partial cards with complete fresh extractions.

Cards per chapter_number: 1→4, 2→1, 3→12, 4→13, 5→7, 6→9, 7→7, 8→27, 9→10,
10→9, 11→1, 12→11, 13→9, 14→8, 15→7, 16→11, 17→19, 18→6, 19→9, 20→13, 21→10,
22→10, 23→11, 24→5, 25→3, 26→6, 27→4, null (Introduction)→1.

(Chapter 2 "A Whirlwind Tour of Erlang" yields a single card by design — it
is a preview chapter; its concepts are carded where later chapters develop
them, per the no-card-previews rule.)

## Phase 3 Validation

- Card count: 243.
- Frontmatter: all required fields present in every card.
- Body: all 12 v3 sections present in every card.
- Slug/filename: all consistent.
- `pdf_page`: `null` on every card (EPUB-origin source).
- Cross-references: all relationship slugs resolve (after fixing `include-file`
  → `include-files` and dropping 3 dangling refs to uncarded concepts
  `defensive-programming` ×2 and `socket-interfacing` ×1).
- LLM artifacts: none.
- Confidence distribution: 230 high / 13 medium / 0 low.

## Status

- Phase 0: complete (CQs; taxonomy & notation shared via erlang-taxonomy.md)
- Phase 1: complete (assignments above)
- Phase 2: complete (243 cards)
- Phase 3: complete (validated)
