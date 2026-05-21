# CQ-to-Chapter Mapping — Learn You Some Erlang for Great Good!

> Phase 1 deliverable per `docs/dev/concept-cards/0010-...-v3.2.md`, Steps 1.2-1.3.
> Source chapter files: `knowledge/erlang/sources/md/learn-you-some-erlang/`.
> 30 chapters + 3 appendices. `00-frontmatter.md` has no extractable concepts.

## Agent assignments (5 agents, balanced by source size ≈280 KB each)

| Agent | Chapters | Files | Theme |
|-------|----------|-------|-------|
| 1 | 1-7 | 01-07 | Sequential Erlang: data, modules, functions, recursion, errors |
| 2 | 8-14 | 08-14 | Problem-solving, data structures, concurrency, OTP intro |
| 3 | 15-21 | 15-21 | OTP behaviours, applications, releases |
| 4 | 22-26 | 22-26 | Scaling, sockets, EUnit, ETS, distributed Erlang |
| 5 | 27-33 | 27-33 | Distributed OTP, Common Test, Mnesia, Dialyzer, appendices |

`chapter_number` = file prefix (1-30) for chapters; `null` for appendices
(31-33), with `chapter` set to "Appendix A. Afterword" etc. `pdf_page: null`
(EPUB-origin source — no page numbers).

## CQ coverage by chapter

- **D1-D4** (atom/tuple/list comprehension/bit syntax) → Ch 1 (Agent 1)
- **D5** (module) → Ch 2 (Agent 1)
- **D6-D7** (pattern matching, guard) → Ch 3 (Agent 1)
- **D8** (tail recursion) → Ch 5 (Agent 1)
- **D9-D10** (fun, closure) → Ch 6 (Agent 1)
- **D11-D12** (record, map) → Ch 9 (Agent 2)
- **D13** (process) → Ch 10 (Agent 2)
- **D14-D16** (link, monitor, selective receive) → Ch 11-12 (Agent 2)
- **D17** (gen_server) → Ch 14 (Agent 2)
- **D18** (FSM behaviour) → Ch 15 (Agent 3)
- **D19** (gen_event) → Ch 16 (Agent 3)
- **D20** (supervisor) → Ch 17 (Agent 3)
- **D21** (OTP application) → Ch 18-20 (Agent 3)
- **D22** (release) → Ch 21 (Agent 3)
- **D23** (ETS) → Ch 25 (Agent 4)
- **D24** (Mnesia) → Ch 29 (Agent 5)
- **D25-D26** (type spec, Dialyzer) → Ch 30 (Agent 5)
- **D27** (distributed node) → Ch 26 (Agent 4)
- **R1** (fold↔map↔filter) → Ch 6 (Agent 1)
- **R2** (links↔monitors) → Ch 12 (Agent 2)
- **R3** (gen_server↔client/server) → Ch 14 (Agent 2)
- **R4** (supervisors↔let-it-crash) → Ch 12, 17 (Agents 2, 3)
- **R5** (application↔release) → Ch 18-21 (Agent 3)
- **R6** (records↔tuples) → Ch 9 (Agent 2)
- **R7** (selective receive↔mailbox) → Ch 11 (Agent 2)
- **R8** (Dialyzer↔type specs) → Ch 30 (Agent 5)
- **R9** (ETS↔Mnesia) → Ch 25, 29 (Agents 4, 5)
- **R10** (tail recursion↔accumulators) → Ch 5 (Agent 1)
- **R11** (behaviour↔callback module) → Ch 14 (Agent 2)
- **P1** (compile module) → Ch 2 (Agent 1)
- **P2** (recursive function) → Ch 5 (Agent 1)
- **P3** (try/catch) → Ch 7 (Agent 1)
- **P4-P5** (spawn/send, stateful process) → Ch 10-11 (Agent 2)
- **P6** (gen_server) → Ch 14 (Agent 2)
- **P7** (supervisor) → Ch 17 (Agent 3)
- **P8** (OTP application) → Ch 18-20 (Agent 3)
- **P9** (release) → Ch 21 (Agent 3)
- **P10** (TCP socket) → Ch 23 (Agent 4)
- **P11** (EUnit) → Ch 24 (Agent 4)
- **P12** (Common Test) → Ch 28 (Agent 5)
- **P13** (ETS) → Ch 25 (Agent 4)
- **P14** (Mnesia) → Ch 29 (Agent 5)
- **P15** (connect nodes) → Ch 26 (Agent 4)
- **P16** (type specs) → Ch 30 (Agent 5)
- **PR1** (before gen_server) → Ch 10-13 (Agent 2)
- **PR2** (before supervisors) → Ch 12, 14 (Agents 2, 3)
- **PR3** (before OTP application) → Ch 14-17 (Agents 2, 3)
- **PR4** (before distributed Erlang) → Ch 10-13, 26 (Agents 2, 4)
- **PR5** (before Dialyzer) → Ch 4, 30 (Agents 1, 5)
- **PR6** (before concurrency) → Ch 1-9 (Agents 1, 2)
- **DG1** (list vs tuple) → Ch 1 (Agent 1)
- **DG2** (error/exit/throw) → Ch 7 (Agent 1)
- **DG3** (link vs monitor) → Ch 12 (Agent 2)
- **DG4** (gen_server vs FSM) → Ch 15 (Agent 3)
- **DG5** (EUnit vs Common Test) → Ch 24, 28 (Agents 4, 5)
- **DG6** (ETS vs DETS) → Ch 25 (Agent 4)
- **DG7** (temporary/transient/permanent) → Ch 17-18 (Agent 3)
- **DG8** (dynamic vs static typing) → Ch 4 (Agent 1)
- **DG9** (spawn vs spawn_link) → Ch 12 (Agent 2)
- **DG10** (list vs binary comprehension) → Ch 1 (Agent 1)

Every CQ maps to ≥1 chapter. No orphan CQs.

## Cross-chapter shared concept slugs (agents must spell identically)

`pattern-matching` (Ch 3, used everywhere), `tail-recursion` (Ch 5),
`process` / `message-passing` / `selective-receive` (Ch 10-12),
`behaviour` (Ch 14, the generic OTP behaviour concept),
`gen-server` (Ch 14), `supervisor` (Ch 17), `otp-application` (Ch 18),
`erlang-release` (Ch 21), `ets-table` (Ch 25), `distributed-node` (Ch 26),
`type-specification` (Ch 30). When a later chapter depends on an
earlier-chapter concept, reference its slug — do not recreate the card.
