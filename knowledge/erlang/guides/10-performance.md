# Performance

How to make Erlang fast without guessing: profile first, then attack real bottlenecks — the `++` and `length/1` traps, efficient binary construction and refc-binary leaks, ETS over a single-process bottleneck, small messages, scheduler/reduction awareness, NIF discipline, hibernation, and back-pressure. The data-structure choices that affect speed are introduced in `04-data-and-types.md`; runtime diagnosis of a live system is in `14-production-ops.md`. Almost everything here is **SHOULD**/**CONSIDER** — measure before you act on any of it.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the Erlang Efficiency Guide (Profiling, Common Caveats, Constructing and Matching Binaries, List Handling, Tables and Databases), the ERTS User's Guide (Time and Time Correction in Erlang), Designing for Scalability with Erlang/OTP, and Erlang in Anger.

---

## PF-01: Measure, Don't Guess — Profile Before Optimising

**Strength**: SHOULD

**Summary**: Find bottlenecks by profiling, not intuition; even experienced developers guess wrong.

```erlang
%% Bad - guess the hot spot and rewrite a function that profiling would show is cold
%% (hand-optimise parse/1 because it "feels slow", with no measurement)

%% Good - profile, then optimise only what dominates
%% 1> tprof:profile(fun() -> my_app:run() end, #{type => call_count}).
%% (then concentrate on the few functions the profiler flags)
```

**Rationale**: "Even experienced software developers often guess wrong about where the performance bottlenecks are… profile your program to see where the bottlenecks are and concentrate on optimizing them" (Efficiency Guide). OTP ships `tprof` (call count/time/heap), `fprof` (detailed, slow), `dbg`, and `lcnt` (lock contention). Optimising un-profiled code wastes effort and adds complexity where it isn't needed.

**See also**: PF-02, PF-03, `14-production-ops.md`

---

## PF-02: Don't Optimise Prematurely

**Strength**: SHOULD

**Summary**: Write the clear version first; optimise only the measured hot path.

```erlang
%% Bad - contort code for a micro-optimisation with no evidence it matters
sum(L) -> sum(L, 0, length(L)).   %% unclear, and length/1 is itself O(n)

%% Good - write the obvious version; revisit only if profiling says so
sum(L) -> lists:sum(L).
```

**Rationale**: Clarity is the default (ID-09, ID-15); premature optimisation trades readability for speed the program may never need. Most code is not on a hot path, and the BEAM's compiler already optimises common patterns. Reserve clever, less-readable implementations for the small fraction PF-01 proves is hot.

**See also**: PF-01, PF-08, `01-core-idioms.md`

---

## PF-03: Benchmark Fairly

**Strength**: CONSIDER

**Summary**: Run each candidate in its own fresh process, for several seconds, and don't over-generalise across machine architectures.

```erlang
%% Bad - both implementations timed once, briefly, in the same shell process
{T1, _} = timer:tc(fun impl_a/0),
{T2, _} = timer:tc(fun impl_b/0).   %% too short; shared heap/GC state skews the later one

%% Good - fresh process per test, enough iterations to last seconds, repeated
Bench = fun(F) -> timer:tc(fun() -> [F() || _ <- lists:seq(1, 1_000_000)] end) end,
spawn(fun() -> io:format("a: ~p~n", [Bench(fun impl_a/0)]) end).
```

**Rationale**: "Benchmarking is far from an exact science" (Efficiency Guide): background tasks, caches, and multiple cores all add noise. Run each test in a newly created process (otherwise later tests start with larger heaps and do fewer GCs), make each measurement last seconds, and don't assume the fastest implementation on one architecture wins on another.

**See also**: PF-01

---

## PF-04: Avoid `O(n²)` `++` — Keep the Growing List on the Right

**Strength**: SHOULD

**Summary**: `++` copies its left operand; never put a growing accumulator on the left in a loop. Prepend and reverse instead.

```erlang
%% Bad - growing accumulator on the LEFT of ++ : copied every iteration -> O(n^2)
build([], Acc)      -> Acc;
build([H | T], Acc) -> build(T, Acc ++ [f(H)]).

%% Good - prepend (O(1)) and reverse once at the end
build(L) -> lists:reverse(build(L, [])).
build([], Acc)      -> Acc;
build([H | T], Acc) -> build(T, [f(H) | Acc]).
```

**Rationale**: "`++` copies the left-hand side operand… if a growing accumulator is on the left side inside a recursive loop, the accumulator is re-copied on every iteration, resulting in O(n²)" (Efficiency Guide). The right side is never copied, and the compiler turns `[H] ++ Acc` into `[H | Acc]`, so single-element left operands are free. This is FP-09 stated as a cost model.

**See also**: PF-05, `05-functions-and-pattern-matching.md` (FP-09)

---

## PF-05: Build Binaries Accumulator-First

**Strength**: SHOULD

**Summary**: Append by making the accumulator the *first* segment (`<<Acc/binary, New/binary>>`); never prepend to a binary in a loop.

```erlang
%% Bad - prepend to a binary accumulator: forces a full copy of Acc every iteration
add(New, Acc) -> <<New/binary, Acc/binary>>.

%% Good - accumulator first; the runtime optimises the append without copying
add(New, Acc) -> <<Acc/binary, New/binary>>.
```

**Rationale**: "Binaries can be efficiently built by placing the binary to be appended to as the first segment… specially optimized by the runtime to avoid copying the accumulator. Prepending forces a full copy each iteration" (Efficiency Guide). The append optimisation reuses the same off-heap allocation; prepending defeats it. This is the binary analogue of PF-04.

**See also**: PF-04, PF-06, `04-data-and-types.md` (DT-11)

---

## PF-06: Know What Forces a Binary Copy

**Strength**: CONSIDER

**Summary**: Sending, ETS-inserting, matching, or keeping an old version of a binary marks it so the *next* append must copy. Finish building before you share it.

```erlang
%% Bad - share a binary, then keep appending: the share forced the later append to copy
ets:insert(t, {k, Acc}),
Acc2 = <<Acc/binary, More/binary>>.   %% Acc was marked by the insert -> this append copies

%% Good - finish the binary, then send/store it
Acc2 = <<Acc/binary, More/binary>>,   %% all appends first
ets:insert(t, {k, Acc2}).
```

**Rationale**: The append optimisation needs a single ProcBin with a single reference, because the binary may be reallocated and the pointer updated; operations that create another reference (send, ETS insert, match) mark the binary so any future append copies it (Efficiency Guide, "Circumstances That Force Copying"). Order your code to complete construction before sharing.

**See also**: PF-05, PF-07

---

## PF-07: Watch for Refc-Binary Leaks

**Strength**: SHOULD

**Summary**: A small sub-binary referencing a large refc binary keeps the whole thing alive; copy out the part you retain.

```erlang
%% Bad - a 10-byte sub-binary pins the entire large off-heap binary in memory
keep(Big) -> binary:part(Big, 0, 10).

%% Good - copy the slice you need so the large binary can be reclaimed
keep(Big) -> binary:copy(binary:part(Big, 0, 10)).
```

**Rationale**: Binaries over 64 bytes are reference-counted and stored off-heap; a sub-binary holds a reference to the whole parent, so retaining a tiny slice can pin megabytes (Efficiency Guide, "Refc Binaries"). This is a classic Erlang memory leak — diagnose it with `recon:bin_leak/1` (chapter 14) and fix it by `binary:copy/1`-ing the retained portion.

**See also**: PF-06, PF-13, `14-production-ops.md`

---

## PF-08: Tail Recursion for Non-List Loops; Clarity for List Builders

**Strength**: CONSIDER

**Summary**: A function that *doesn't* build a list should be tail-recursive (constant stack); for list builders, body- and tail-recursion now perform comparably, so write the clearer one.

```erlang
%% Bad - assume tail recursion is always faster and contort a list builder for "speed"
%% (modern BEAM: body- and tail-recursive list builders are comparable)

%% Good - non-list-building loop: tail-recursive accumulator (constant stack)
sum([], Acc)      -> Acc;
sum([H | T], Acc) -> sum(T, Acc + H).
%% list-building: write the clearest form; measure only if it's a proven hot path
```

**Rationale**: "In modern Erlang there is usually not much difference between a body-recursive list function and a tail-recursive one that reverses at the end… concentrate on writing beautiful code" (Efficiency Guide). The exception is functions that don't construct a list: tail recursion runs in constant space, body recursion uses stack proportional to input. This nuances FP-08 with the cost model.

**See also**: PF-02, `05-functions-and-pattern-matching.md` (FP-08)

---

## PF-09: Avoid `length/1` on Long Lists in Hot Paths

**Strength**: SHOULD

**Summary**: `length/1` is `O(n)`; in time-critical code over potentially long lists, pattern-match the shape instead of computing the length.

```erlang
%% Bad - length/1 in a hot guard over a possibly-huge list: O(n) every call
serve(L) when length(L) > 0 -> hd(L).

%% Good - match the shape; O(1)
serve([H | _]) -> {ok, H};
serve([])      -> empty.
```

**Rationale**: "The time for calculating the length of a list is proportional to the length of the list, as opposed to `tuple_size/1`, `byte_size/1`, and `bit_size/1`, which all execute in constant time" (Efficiency Guide). Usually `length/1` is fine (it's C-implemented), but a per-iteration `length/1` over a long list is a quiet `O(n²)`. Match `[_|_]`/`[]` to test emptiness, or carry a count.

**See also**: PF-04, `05-functions-and-pattern-matching.md`

---

## PF-10: Use ETS for Shared or Large In-Memory State

**Strength**: SHOULD

**Summary**: When many processes read shared state, put it in an ETS table (with the right type and concurrency options) instead of funnelling every read through one process.

```erlang
%% Bad - one gen_server holds a big map; every reader calls it, serialising all lookups
%% state = #{key => val, ...}; reads bottleneck on the single process

%% Good - a shared ETS table serves concurrent reads directly
T = ets:new(cache, [set, public, named_table, {read_concurrency, true}]),
ets:insert(T, {Key, Val}),
[{Key, Val}] = ets:lookup(T, Key).
```

**Rationale**: A single process is a serialisation point — every reader waits behind every other (and behind writes). An ETS table allows concurrent access with `O(1)` keyed lookups, and `{read_concurrency, true}` / `{write_concurrency, true}` tune it for the access pattern. Choose the table type (`set`, `ordered_set`, `bag`) for how you query.

**See also**: PF-11, PF-12, `04-data-and-types.md` (DT-14)

---

## PF-11: Don't Scan Whole ETS Tables — Query with Keys and Match Specs

**Strength**: CONSIDER

**Summary**: Avoid `ets:tab2list/1` and Erlang-side filtering; use keyed lookups or `select`/`match` specs so ETS does the work in C.

```erlang
%% Bad - pull the entire table into a list and filter in Erlang
[Row || Row <- ets:tab2list(t), element(2, Row) =:= active].

%% Good - keyed lookup, or a match spec that filters inside ETS
ets:lookup(t, Key),
ets:select(t, [{{'_', active, '$1'}, [], ['$1']}]).
```

**Rationale**: `tab2list/1` copies the whole table to the calling process and then you scan it — `O(n)` copy plus `O(n)` scan, defeating the point of a fast keyed store. `ets:select/2` / `match/2` evaluate the pattern inside ETS and return only matches. Design the key (and any secondary indexes) for the queries you actually run.

**See also**: PF-10, PF-12

---

## PF-12: Prefer ETS over Mnesia for Non-Persistent Storage

**Strength**: CONSIDER

**Summary**: For purely in-memory, non-replicated data, use ETS; reach for Mnesia only when you need transactions, replication, or persistence.

```erlang
%% Bad - Mnesia for transient, single-node, non-persistent data
mnesia:dirty_write({cache, Key, Val}).   %% replication/index checks on every write

%% Good - ETS for non-persistent storage
ets:insert(cache, {Key, Val}).
```

**Rationale**: "Ets writes are always faster than Mnesia writes… Mnesia must check if the table is replicated or has indices, which involves at least one Ets lookup for each `dirty_write`" (Efficiency Guide). Mnesia is built on ETS, so its operations cost an ETS operation plus overhead. Pay that overhead only for the features (transactions, distribution, disk) you actually use.

**See also**: PF-10, PF-11, `16-distribution.md`

---

## PF-13: Keep Messages Small

**Strength**: SHOULD

**Summary**: Sending a term copies it into the recipient; don't broadcast large terms — share bulk data via ETS or send a locator.

```erlang
%% Bad - send a large term to many workers: copied into each mailbox
[W ! {data, HugeTerm} || W <- Workers].

%% Good - keep messages small; share the bulk via ETS (or a reference)
ets:insert(shared, {job, HugeTerm}),
[W ! {job_ref, job} || W <- Workers].
```

**Rationale**: Erlang's share-nothing model copies most terms on send, so a large message multiplies its cost by the number of recipients (and grows mailboxes, PC-09). Large binaries (>64 bytes) are the exception — they're refc-shared (PF-07) — which is another reason to prefer binaries for bulk data. This is PC-15 as a performance rule.

**See also**: PF-07, `06-processes-and-concurrency.md` (PC-15)

---

## PF-14: Don't Create Atoms Dynamically

**Strength**: SHOULD

**Summary**: Don't build atoms from runtime or external data; the atom table is bounded and never garbage-collected.

```erlang
%% Bad - mint an atom per id: the atom table fills and the node eventually crashes
Key = list_to_atom("user_" ++ integer_to_list(Id)).

%% Good - keep dynamic keys as binaries/integers/tuples; only ever resolve existing atoms
Key = {user, Id}.
```

**Rationale**: Atoms are interned and never reclaimed, with a hard table limit; minting them from unbounded data is both a memory exhaustion and a stability hazard (and a DoS vector at a trust boundary — DT-13, EH-15). Use binaries or compound terms for dynamic keys, and `binary_to_existing_atom/2` when you must reach an atom that already exists.

**See also**: `04-data-and-types.md` (DT-13), `03-error-handling.md` (EH-15)

---

## PF-15: Mind Schedulers and Reductions — Don't Block a Scheduler

**Strength**: CONSIDER

**Summary**: The BEAM preempts processes by reduction count across one scheduler per core; long uninterrupted work (tight loops, long NIFs/BIFs) starves a scheduler.

```erlang
%% Bad - a tight loop that does little measurable work can monopolise a scheduler
busy() -> busy().

%% Good - do bounded work per step; push heavy CPU work onto its own process/pool
work(0) -> done;
work(N) -> step(), work(N - 1).
%% the scheduler preempts on reduction count; keep individual operations bounded
```

**Rationale**: "For every core the BEAM starts a scheduler thread… processes are preempted based on a reduction count" (Designing for Scalability). Fairness depends on processes accumulating reductions and yielding; a long-running native or busy operation that doesn't yield holds its scheduler and hurts latency for everything in that run queue. Spread CPU-heavy work across processes so the scheduler can interleave it.

**See also**: PF-16, `06-processes-and-concurrency.md`

---

## PF-16: Keep NIFs Short or Yielding

**Strength**: CONSIDER

**Summary**: A NIF runs on its caller's scheduler thread with no preemption; keep it under ~1 ms, or use a dirty scheduler / yielding NIF for long work.

```erlang
%% Bad - a long-running NIF blocks its scheduler for the entire call
%% slow_nif(BigInput) -> ... 500 ms of C with no yield ...

%% Good - bound NIF work, or mark CPU/IO-bound NIFs to run on a dirty scheduler
%% (enif_schedule_nif to chunk work, or the dirty-NIF flags for long native calls)
```

**Rationale**: A NIF executes as native code on the scheduler that called it and cannot be preempted by the reduction mechanism, so a long NIF directly stalls a scheduler (PF-15) and breaks the soft-real-time guarantees of the VM. Keep NIFs brief, chunk long work with `enif_schedule_nif`, or run genuinely long native work on a dirty scheduler.

**See also**: PF-15, `09-fault-tolerance.md`

---

## PF-17: Hibernate Idle Long-Lived Processes

**Strength**: CONSIDER

**Summary**: For many mostly-idle long-lived processes, hibernate between messages to compact the heap and reclaim memory.

```erlang
%% Bad - thousands of idle long-lived processes each retain a grown heap

%% Good - hibernate when idle; the heap is minimised until the next message
handle_info(timeout, State) ->
    {noreply, State, hibernate}.
%% (or proc_lib:hibernate/3 in a hand-written loop)
```

**Rationale**: Hibernation garbage-collects the process and discards its call stack, shrinking it to a minimal heap until the next message wakes it (at the cost of a GC on wake). For large fleets of idle processes (connections, sessions), the memory saved dwarfs the occasional wake-up GC. Don't hibernate hot processes — the GC churn would cost more than it saves.

**See also**: PF-15, `07-otp-behaviours.md`

---

## PF-18: Apply Back-Pressure Under Overload

**Strength**: CONSIDER

**Summary**: Don't accept work faster than you can process it; use synchronous calls or a bounded queue so producers slow down instead of the mailbox growing unbounded.

```erlang
%% Bad - accept jobs via async cast with no limit: under overload the mailbox grows until OOM
handle_cast({job, J}, S) -> {noreply, enqueue(J, S)}.

%% Good - synchronous accept with a bound; reject or block producers when full
handle_call({job, J}, _From, S) ->
    case full(S) of
        true  -> {reply, {error, overloaded}, S};
        false -> {reply, ok, enqueue(J, S)}
    end.
```

**Rationale**: An unbounded `cast`-fed queue converts a load spike into unbounded memory growth and eventual node death. Synchronous `call` applies back-pressure automatically (BEH-04) — a slow consumer slows its producers; an explicit bound lets you shed load (reject) instead. Load regulation keeps a system degrading gracefully rather than collapsing.

**See also**: PF-13, `07-otp-behaviours.md` (BEH-04), `14-production-ops.md`

---

## PF-19: Measure Elapsed Time with Monotonic Time

**Strength**: SHOULD

**Summary**: Time durations with `erlang:monotonic_time/1`, never by subtracting two system-time (wall-clock) samples — system time can warp and the difference becomes meaningless.

```erlang
%% Bad - subtract wall-clock samples to time work: a backward time warp corrupts the result
T0 = erlang:system_time(millisecond),
Result = do_work(),
Elapsed = erlang:system_time(millisecond) - T0.   %% can be wrong, even negative

%% Good - monotonic time never warps; it is the correct clock for durations
T0 = erlang:monotonic_time(millisecond),
Result = do_work(),
Elapsed = erlang:monotonic_time(millisecond) - T0.
```

**Rationale**: Erlang monotonic time is "a monotonically increasing time" that never leaps, whereas Erlang system time tracks POSIX wall-clock and "may or may not align with OS system time" — it can warp forwards or backwards (ERTS User's Guide, *Time and Time Correction in Erlang*). A difference of two system-time samples therefore does **not** reliably correspond to elapsed time. Use `erlang:monotonic_time/1` with an explicit time unit; for benchmarking (PF-03), take `erlang:monotonic_time(native)` and convert with `erlang:convert_time_unit/3` for the best available resolution. (A negative value from `monotonic_time/0` is not a bug — it is a documented memory optimisation; only the *difference* is meaningful.)

**See also**: PF-03, PF-20, PF-21

---

## PF-20: Replace `erlang:now/0` with the Modern Time API

**Strength**: SHOULD

**Summary**: `erlang:now/0` is deprecated, serialises through a global lock, and can *freeze for years* on a backward time warp; split its uses across the purpose-built time functions.

```erlang
%% Bad - erlang:now/0: a global lock, time-warp-unsafe, and overloaded for three unrelated jobs
Ts     = erlang:now(),   %% used as a wall-clock timestamp...
Uniq   = erlang:now().   %% ...and as a monotonically increasing unique value

%% Good - pick the function built for each job
Wall   = erlang:system_time(millisecond),      %% wall-clock / POSIX time (or erlang:timestamp/0)
Dur0   = erlang:monotonic_time(),              %% durations (PF-19)
Uniq2  = erlang:unique_integer([monotonic]).   %% strictly increasing unique values
```

**Rationale**: `erlang:now/0` was three things at once — a wall-clock timestamp, a source of strictly increasing unique values, and a globally serialised counter — and the source states plainly: "Do not use `erlang:now/0`" (ERTS User's Guide, *Time and Time Correction*). Because it must never go backwards, a backward OS time leap can make it stall — the guide warns it can freeze "for years, decades, and even longer." The global lock also caps throughput on multicore systems. The new API separates the concerns: `system_time/1` (or `timestamp/0`) for wall-clock, `monotonic_time/1` for durations, and `unique_integer/1` for unique values.

**See also**: PF-19, PF-21

---

## PF-21: Reconstruct Wall-Clock Time with the Contemporaneous Offset

**Strength**: CONSIDER

**Summary**: Erlang system time = monotonic time + time offset; since the offset can move (multi-time-warp is the OTP-26 default), don't add the *current* offset to an *old* monotonic stamp — capture the offset together, or store system time directly.

```erlang
%% Bad - store a monotonic stamp, later add the current offset: the offset may have moved
Mono = erlang:monotonic_time(),
%% ...much later, in another mode/run...
Wall = Mono + erlang:time_offset().   %% wrong wall-clock once the offset has changed

%% Good - capture the offset at the same instant (or just store system time if that is all you need)
Mono   = erlang:monotonic_time(),
Offset = erlang:time_offset(),         %% taken together with Mono
Wall   = Mono + Offset.                %% reconstructs the wall-clock at that instant
```

**Rationale**: "Current Erlang system time is determined by adding the current Erlang monotonic time with current time offset" (ERTS User's Guide, *Time and Time Correction*). Since OTP 26 the default is multi-time-warp mode, in which "the time offset can change at any time without limitations." Reconstructing wall-clock by adding *today's* offset to a monotonic value captured earlier therefore yields the wrong answer once the offset has shifted. If you need both a warp-immune duration and a wall-clock label for the same event, record the monotonic value and the offset together; if you only need wall-clock, store `erlang:system_time/1` directly. (Legacy code that is not time-warp-safe can be run with `erl +C no_time_warp`, but the source strongly encourages making code time-warp-safe instead.)

**See also**: PF-19, PF-20, `16-distribution.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| PF-01 Profile first | SHOULD | Measure; don't guess the bottleneck |
| PF-02 No premature optimisation | SHOULD | Clarity first; optimise the measured hot path |
| PF-03 Benchmark fairly | CONSIDER | Fresh process, seconds-long, arch-specific |
| PF-04 `++` is O(n) on the left | SHOULD | Prepend and reverse; never grow on the left |
| PF-05 Binaries accumulator-first | SHOULD | `<<Acc/binary, New>>` is optimised |
| PF-06 What forces a copy | CONSIDER | Finish building before sharing a binary |
| PF-07 Refc-binary leaks | SHOULD | Copy small slices of large binaries |
| PF-08 Tail vs body recursion | CONSIDER | Tail for non-list loops; clarity for builders |
| PF-09 `length/1` is O(n) | SHOULD | Pattern-match shape in hot paths |
| PF-10 ETS for shared state | SHOULD | Avoid the single-process read bottleneck |
| PF-11 No full ETS scans | CONSIDER | Keyed lookups / match specs, not `tab2list` |
| PF-12 ETS over Mnesia | CONSIDER | Mnesia only for its extra features |
| PF-13 Small messages | SHOULD | Sends copy; share bulk via ETS |
| PF-14 No dynamic atoms | SHOULD | Atom table is bounded, never collected |
| PF-15 Schedulers/reductions | CONSIDER | Don't monopolise a scheduler |
| PF-16 Short/yielding NIFs | CONSIDER | Long NIFs stall a scheduler |
| PF-17 Hibernate idle processes | CONSIDER | Reclaim heap across large idle fleets |
| PF-18 Back-pressure | CONSIDER | Bound queues; `call` over unbounded `cast` |
| PF-19 Monotonic time for durations | SHOULD | System time warps; monotonic time does not |
| PF-20 Retire `erlang:now/0` | SHOULD | Split into `system_time`/`monotonic_time`/`unique_integer` |
| PF-21 Wall-clock from monotonic | CONSIDER | Capture the offset together; it can move |

## Related Guidelines

- **Data & types**: See `04-data-and-types.md` — binaries (DT-10), iolists/`++` (DT-11), collection choice (DT-14), and the atom risk (DT-13).
- **Functions & pattern matching**: See `05-functions-and-pattern-matching.md` — FP-08/FP-09 are the technique behind PF-04/PF-08.
- **Processes & concurrency**: See `06-processes-and-concurrency.md` — message-copy cost (PC-15) and mailbox/selective-receive cost (PC-09).
- **OTP behaviours**: See `07-otp-behaviours.md` — back-pressure via `call` (BEH-04) and not blocking callbacks (BEH-05).
- **Production ops**: See `14-production-ops.md` for profiling and memory diagnosis (`recon`, allocators) on a live system.

## External References

- [Erlang Efficiency Guide](https://www.erlang.org/doc/system/efficiency_guide.html) — Profiling; Common Caveats (`++`, `length/1`); Constructing and Matching Binaries; List Handling; Tables and Databases
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — schedulers and reductions (pp. 33–34)
- *Erlang in Anger* (Fred Hébert) — memory, refc-binary leaks, `recon`
