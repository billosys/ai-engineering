# CQ-to-Chapter Mapping — Stuff Goes Bad: Erlang in Anger

> Phase 1 deliverable per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 1.2.
> Maps each competency question to the source chapter(s) that answer it and
> the concept cards needed. Chapter files live in
> `knowledge/erlang/sources/md/erlang-in-anger/`.

## Chapter inventory

| File | Ch # | Title | Agent |
|------|------|-------|-------|
| 001-introduction.md | null | Introduction | 1 |
| 101-diving.md | 1 | How to Dive into a Code Base | 1 |
| 102-building.md | 2 | Building Open Source Erlang Software | 1 |
| 103-overload.md | 3 | Planning for Overload | 1 |
| 104-connecting.md | 4 | Connecting to Remote Nodes | 2 |
| 105-runtime-metrics.md | 5 | Runtime Metrics | 2 |
| 106-crash-dumps.md | 6 | Reading Crash Dumps | 2 |
| 107-memory-leaks.md | 7 | Memory Leaks | 3 |
| 108-cpu.md | 8 | CPU and Scheduler Hogs | 3 |
| 109-tracing.md | 9 | Tracing | 3 |
| 201-conclusion.md | null | Conclusion (no extractable concepts) | — |

## Definitional

- D1 let-it-crash → Introduction (concepts: `let-it-crash`)
- D2 OTP application → Ch 1, 2 (`otp-application`)
- D3 library vs regular app → Ch 1 (`library-application`, `regular-application`)
- D4 OTP release → Ch 1, 2 (`otp-release`)
- D5 app file → Ch 1 (`app-file`)
- D6 back-pressure → Ch 3 (`back-pressure`)
- D7 load-shedding → Ch 3 (`load-shedding`)
- D8 true bottleneck → Ch 3 (`true-bottleneck`)
- D9 crash dump → Ch 6 (`crash-dump`)
- D10 refc binary → Ch 7 (`refc-binary`)
- D11 reduction → Ch 5 (`reduction`)
- D12 scheduler wall time → Ch 5 (`scheduler-utilization`)
- D13 port datatype → Ch 5 (`port`)
- D14 JCL → Ch 4 (`job-control-mode`)
- D15 memory fragmentation → Ch 7 (`memory-fragmentation`)

## Relational

- R1 restart strategies ↔ child relationships → Ch 1 (`supervisor-restart-strategy`)
- R2 app vs release structure → Ch 2 (`project-structure`)
- R3 back-pressure ↔ load-shedding → Ch 3 (`back-pressure`, `load-shedding`)
- R4 pid specs ∩ trace patterns → Ch 9 (`tracing-principles`)
- R5 scheduler utilization ↔ OS CPU → Ch 5, 8 (`scheduler-utilization`)
- R6 erlang:memory ↔ OS memory → Ch 5, 7 (`vm-memory-reporting`, `memory-fragmentation`)
- R7 sub-allocators ↔ mseg/sys_alloc → Ch 7 (`erlang-memory-model`)
- R8 process memory ↔ binary leaks → Ch 7 (`refc-binary-leak`, `process-memory-inspection`)

## Procedural

- P1 dive into code base → Ch 1 (`diving-into-a-code-base`)
- P2 build a release → Ch 2 (`rebar3`, `relx-release-assembly`)
- P3 specify deps → Ch 2 (`dependency-specification`)
- P4 connect to remote node → Ch 4 (`remote-shell-connection` + 4 methods)
- P5 global memory view → Ch 5 (`vm-memory-reporting`, `recon-alloc-memory`)
- P6 top memory processes → Ch 5, 7 (`recon-proc-count`, `recon-proc-window`)
- P7 read a crash dump → Ch 6 (`crash-dump-analysis`)
- P8 detect binary leak → Ch 7 (`refc-binary-leak`)
- P9 monitor long GC → Ch 7, 8 (`gc-system-monitor`)
- P10 find CPU hogs → Ch 8 (`reduction-counting`, `profiling-tools`)
- P11 trace in production → Ch 9 (`recon-trace`)
- P12 inspect a process safely → Ch 5 (`process-inspection`)
- P13 control crash dump path → Ch 6 (`crash-dump`)
- P14 random drop → Ch 3 (`random-drop`)

## Prerequisite

- PR1 before supervision-tree navigation → Ch 1 (`otp-application`, `behaviour-as-navigation-clue`)
- PR2 before memory-leak diagnosis → Ch 5, 7 (`vm-memory-reporting`, `runtime-metrics`)
- PR3 before synchronous back-pressure → Ch 3 (`back-pressure`, `timeout-selection`)
- PR4 before allocator tuning → Ch 7 (`erlang-memory-model`, `allocation-strategy`)
- PR5 before tracing production → Ch 9 (`tracing-principles`, `trace-rate-limiting`)

## Diagnostic

- DG1 raw vs OTP application → Ch 1 (`raw-erlang-code-base`, `otp-application`)
- DG2 back-pressure vs load-shedding → Ch 3 (`back-pressure`, `load-shedding`)
- DG3 queue vs stack buffer → Ch 3 (`queue-buffer`, `stack-buffer`)
- DG4 leak vs fragmentation → Ch 7 (`memory-leak-detection`, `memory-fragmentation`)
- DG5 permanent/transient/temporary → Ch 2 (`application-start-types`)
- DG6 proc_count vs proc_window → Ch 5 (`recon-proc-count`, `recon-proc-window`)
- DG7 ProcBin vs refc binary → Ch 7 (`refc-binary`)
- DG8 top/htop unreliable for Erlang → Ch 5, 8 (`scheduler-utilization`)

## Coverage notes

- Every CQ maps to at least one chapter. No orphan CQs.
- Cross-chapter concepts (shared, agents must use identical slugs):
  `otp-application`, `otp-release` (Ch 1 & 2); `recon-proc-window`,
  `scheduler-utilization`, `vm-memory-reporting` (Ch 5, 7, 8);
  `gc-system-monitor` (Ch 7 & 8); `recon-trace`/tracing (Ch 5 refs Ch 9).
