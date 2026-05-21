# Extraction Log — Designing for Scalability with Erlang/OTP

> Source: "Designing for Scalability with Erlang/OTP" — Francesco Cesarini & Steve Vinoski
> source_slug: `design-scale-erlang-otp`  ·  KB: `erlang`
> Process: `docs/dev/concept-cards/0009` (howto) + `0010` (parallel extraction), v3.2.

## Type

Fresh extraction — no pre-existing card inventory for this source.

## Chapter Inventory

| Ch | Title | pdf_page |
|----|-------|----------|
| 1 | Introducing Erlang | 40 |
| 2 | Behaviors | 72 |
| 3 | Generic Servers | 96 |
| 4 | Controlling OTP Behaviors | 120 |
| 5 | Finite State Machines | 136 |
| 6 | Event Handlers | 166 |
| 7 | Supervisors | 188 |
| 8 | Applications | 222 |
| 9 | Special Processes and Your Own Behaviors | 260 |
| 10 | System Principles and Release Handling | 282 |
| 11 | Release Upgrades | 336 |
| 12 | Distributed Architectures | 378 |
| 13 | Systems That Never Stop | 402 |
| 14 | Scaling Out | 424 |
| 15 | Monitoring and Preemptive Support | 444 |

## Agent Assignments (Phase 1)

| Agent | Chapters | Theme |
|-------|----------|-------|
| 1 | 1–3 | Erlang foundations, behaviors, generic servers |
| 2 | 4–6 | Controlling behaviors, FSMs, event handlers |
| 3 | 7–9 | Supervisors, applications, special processes |
| 4 | 10–11 | System principles, release handling & upgrades |
| 5 | 12–15 | Distribution, resilience, scaling, monitoring |

## Results (Phase 2)

| Agent | Chapters | Cards |
|-------|----------|-------|
| 1 | 1–3 | 44 |
| 2 | 4–6 | 30 |
| 3 | 7–9 | 36 |
| 4 | 10–11 | 39 |
| 5 | 12–15 | 75 |
| **Total** | | **224** |

Cards per chapter: 1→20, 2→9, 3→15, 4→9, 5→12, 6→9, 7→17, 8→13, 9→6,
10→21, 11→18, 12→28, 13→22, 14→18, 15→7.

`distributed-erlang` was extracted by both Agent 1 (ch.1 refresher) and Agent 5
(ch.12, full treatment) — one concept, one card; the ch.12 version is canonical.
Agents 1+5 reported 45+75=120 but 119 distinct files survive after this de-dup,
hence 224 total rather than 225.

## Phase 3 Validation

- Card count: 224.
- Frontmatter: all required fields present in every card.
- Body: all 12 v3 sections present in every card.
- Slug/filename: all consistent.
- Cross-references: all relationship slugs resolve (after fixing `otp-behaviour`
  → `otp-behaviors` in 7 cards and dropping 2 dangling `reltool` refs).
- LLM artifacts: none.
- Confidence distribution: 215 high / 9 medium / 0 low — genuinely high-skewed;
  this book defines concepts explicitly with worked examples.

## Status

- Phase 0: complete (CQs, taxonomy shared, notation shared)
- Phase 1: complete (assignments above)
- Phase 2: complete (224 cards)
- Phase 3: complete (validated)
