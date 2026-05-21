# Production Operations

How to operate and diagnose a live Erlang system: connect to a running node, introspect with `observer`/`recon`, trace safely in production, find the process behind a memory or mailbox problem, read a crash dump, watch VM metrics, and shed load under overload. This is the *Erlang in Anger* material. The performance cost model is in `10-performance.md`; the supervision behaviour that recovers failures is in `08`/`09`.

Target environment: **Erlang/OTP 27+** (tracing via `recon`; logging via `logger`). Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: *Erlang in Anger* (Fred Hébert), Inaka guidelines, Designing for Scalability with Erlang/OTP, and the OTP runtime/observer documentation.

---

## OPS-01: Don't Debug with `io:format` in Production

**Strength**: SHOULD

**Summary**: Keep `io:format`/`ct:pal` debug calls out of `src/`; use structured `logger` events and live tracing instead.

```erlang
%% Bad - io:format scattered through production code: unstructured, unleveled, and easy to leave behind
handle(Req) -> io:format("got ~p~n", [Req]), process(Req).

%% Good - a structured logger event (and live tracing when you need call-level detail)
handle(Req) ->
    logger:debug("request received", #{request => Req}),
    process(Req).
```

**Rationale**: "There should be no `io:format` nor `ct:pal` calls in your production code" (Inaka). Console prints are unstructured, carry no severity, vanish on restart, and can flood stdout. `logger` gives levels and metadata (EH-14); for ad-hoc, call-level investigation on a running node, use rate-limited tracing (OPS-04), not print statements.

**See also**: OPS-04, `03-error-handling.md` (EH-14)

---

## OPS-02: Connect to a Running Node with a Remote Shell

**Strength**: SHOULD

**Summary**: Inspect a live system by attaching a remote shell to the node, rather than restarting it to add instrumentation.

```erlang
%% Bad - to investigate, restart the node with extra logging (destroying the very state you wanted)

%% Good - attach a remote shell to the running node
%% $ erl -name debug@host -setcookie SECRET -remsh myapp@host
%% (or the release's `bin/myapp remote_console`)
%% then inspect: recon:proc_count(memory, 5), sys:get_state(some_proc), ...
```

**Rationale**: A node's interesting state is in its running processes; restarting to add a log line discards it. A remote shell (`-remsh`, or the release's `remote_console`) joins the live VM so you can introspect and trace it in place. It requires a named node and a matching cookie — and therefore a trusted network (DIST-05).

**See also**: OPS-03, `16-distribution.md` (DIST-05)

---

## OPS-03: Introspect the Live System with `observer` and Runtime BIFs

**Strength**: SHOULD

**Summary**: Use `observer` (or its CLI equivalents) and the runtime introspection BIFs to see processes, memory, and the supervision tree.

```erlang
%% Bad - guess at what the system is doing from logs alone

%% Good - look directly
1> observer:start().                       %% GUI: processes, memory, tables, app tree
2> erlang:system_info(process_count).      %% headline counts
3> erlang:memory().                        %% memory breakdown by category
4> sys:get_state(my_server).               %% a behaviour's current state
```

**Rationale**: `observer` visualises processes, ETS tables, memory allocators, and the application/supervision trees; the underlying BIFs (`system_info`, `memory`, `process_info`) and `sys:get_state/1` give the same data programmatically for a headless node. Direct introspection turns "the system feels slow" into specific numbers.

**See also**: OPS-02, OPS-06, OPS-13

---

## OPS-04: Trace in Production with `recon_trace` (Rate-Limited)

**Strength**: SHOULD

**Summary**: Use `recon_trace:calls/3` with a hard limit to trace function calls on a live node; don't enable raw, unbounded tracing in production.

```erlang
%% Bad - raw dbg tracing with no rate limit can flood the tracer and stall/kill the node
dbg:tracer(), dbg:p(all, call), dbg:tpl(my_mod, my_fun, []).

%% Good - recon_trace with a max message count and argument match
recon_trace:calls({my_mod, my_fun, '_'}, 100),                %% at most 100 traces
recon_trace:calls({my_mod, my_fun, fun([arg]) -> ok end}, 10),
recon_trace:clear().                                          %% turn it all off
```

**Rationale**: `recon_trace:calls(TSpec, Max, Opts)` is "production-safe… with built-in rate limiting" (*Erlang in Anger*) — it caps how many trace messages are produced so a popular function can't drown the node. Raw `dbg` with a broad pattern and no limit is a known way to take a busy node down.

**See also**: OPS-05, `10-performance.md`

---

## OPS-05: Tracing Targets the Intersection of Pids and Patterns

**Strength**: SHOULD

**Summary**: A call is traced only if its process is in the pid specification *and* its call matches a trace pattern; scope both, and never trace too widely.

```erlang
%% Bad - trace every function in every process: the intersection is "everything"
recon_trace:calls({'_', '_', '_'}, 1000).    %% recon refuses this for good reason

%% Good - narrow the pattern (and pids) to the intersection you actually need
recon_trace:calls({my_mod, handle_call, '_'}, 50, [{pid, [SuspectPid]}]).
```

**Rationale**: "Tracing works in two parts: pid specifications and trace patterns… what defines whether a call gets traced is the intersection of both" (*Erlang in Anger*). A pattern that matches everything (`{'_','_','_'}`) traces the whole VM and will overwhelm it — recon forbids the widest patterns precisely to stop this. Always narrow to the module/function (and the suspect pids) you're investigating.

**See also**: OPS-04

---

## OPS-06: Find Offenders by Metric with `recon:proc_count`/`proc_window`

**Strength**: SHOULD

**Summary**: Rank processes by a runtime attribute (memory, `message_queue_len`, reductions) to find the one causing trouble.

```erlang
%% Bad - scan the whole process list by hand looking for "the big one"
[process_info(P, memory) || P <- processes()].   %% noisy, racy, no ranking

%% Good - recon ranks them for you (snapshot, or over a time window)
recon:proc_count(memory, 5),                 %% top 5 by memory now
recon:proc_window(reductions, 5, 1000).      %% top 5 by reductions over 1s
```

**Rationale**: `recon:proc_count/2` gives an instantaneous top-N by an attribute; `proc_window/3` measures change over an interval, which is what you want for "who is busy *right now*" rather than "who has run a lot since boot." This turns process diagnosis from manual scanning into a one-liner.

**See also**: OPS-03, OPS-07, `10-performance.md` (PF-15)

---

## OPS-07: Diagnose Overload by Finding the Growing Mailbox

**Strength**: SHOULD

**Summary**: When a system is overloaded or leaking memory, look first for a process with a large, growing `message_queue_len`.

```erlang
%% Bad - assume "out of memory" means a binary/ETS leak and chase that first

%% Good - rank by mailbox size; a process that can't keep up shows here
recon:proc_count(message_queue_len, 5).
%% then inspect the offender: process_info(Pid, [current_function, message_queue_len])
```

**Rationale**: A process that receives faster than it processes accumulates an unbounded mailbox — the messages hold memory and every selective receive gets slower (PC-08/PC-09). It is one of the most common production failure modes, and ranking by `message_queue_len` finds it immediately. The fix is back-pressure or load-shedding (OPS-12).

**See also**: OPS-06, OPS-12, `06-processes-and-concurrency.md` (PC-08)

---

## OPS-08: Diagnose Refc-Binary Leaks with `recon:bin_leak`

**Strength**: SHOULD

**Summary**: Suspected binary memory growth: use `recon:bin_leak/1` to find the holding processes, then fix by copying small slices, hibernating, or scoping work to short-lived processes.

```erlang
%% Bad - call erlang:garbage_collect() on every process and hope memory drops

%% Good - identify the leakers, then apply a targeted fix
recon:bin_leak(10).        %% top processes by binary memory freed after a GC
%% fixes: binary:copy/1 a retained small fragment; hibernate idle holders;
%%        do the work in a one-off process that dies (and frees its refc binaries)
```

**Rationale**: Refc binaries live off-heap and are freed only when the last reference is GC'd, so a process holding a small slice of a large binary pins the whole thing (PF-07). `recon:bin_leak/1` GCs processes and reports who freed the most binary memory — the leakers. *Erlang in Anger* lists the fixes: `binary:copy/1` a small fragment, hibernate, scope work to dying processes, or (last resort) manual GC.

**See also**: OPS-07, `10-performance.md` (PF-07)

---

## OPS-09: Analyse Crash Dumps Methodically

**Strength**: CONSIDER

**Summary**: After a node dies, start from its `erl_crash.dump` — get a summary first, then correlate figures to the cause.

```erlang
%% Bad - skim the raw multi-megabyte erl_crash.dump by eye and guess

%% Good - summarise first, then drill in
%% $ ./recon/script/erl_crashdump_analyzer.sh erl_crash.dump
%% (then open the dump for the flagged area: process count, memory, the slogan/reason)
```

**Rationale**: "Reading the crash dump is useful to figure out why a node died *a posteriori*… recon's `erl_crashdump_analyzer.sh` gives a quick look" (*Erlang in Anger*). The dump records the death reason ("slogan"), process and memory totals, and per-process state; the analyzer summarises the totals so you know whether to chase process count, mailbox, binary memory, or ETS — instead of reading megabytes by hand.

**See also**: OPS-07, OPS-08

---

## OPS-10: Arm `system_monitor` for Pathological Conditions

**Strength**: CONSIDER

**Summary**: Use `erlang:system_monitor/2` to get alerted about long garbage collections, large heaps, busy ports/dist, and long-scheduled processes.

```erlang
%% Bad - discover only from latency graphs that some process GCs for 500ms

%% Good - subscribe to system-level warnings and log/act on them
erlang:system_monitor(self(),
    [{long_gc, 100}, {large_heap, 5_000_000}, busy_port, busy_dist_port]).
%% receive {monitor, Pid, long_gc, Info} -> logger:warning(...) end
```

**Rationale**: `system_monitor` delivers a message when a process exceeds a GC time, grows past a heap threshold, or a port/dist blocks — the early symptoms of latency spikes and overload. Wiring it into a monitoring process surfaces these conditions as actionable events rather than mysterious tail-latency. (`recon` and various metrics libraries wrap this.)

**See also**: OPS-13, `10-performance.md`

---

## OPS-11: Use `logger` Levels and Guard Against Log Overload

**Strength**: SHOULD

**Summary**: Log through `logger` at appropriate levels, and ensure logging itself can't take the node down under a flood.

```erlang
%% Bad - log every request at error level with no protection against a burst
logger:error("request ~p", [Req]).      %% a spike floods the log and the logger process

%% Good - level-appropriate logging; rely on logger's overload protection / rate limits
logger:info("request handled", #{id => Id}),
logger:error("payment failed", #{reason => Reason, id => Id}).
%% configure handler overload protection (drop/burst limits) in sys.config
```

**Rationale**: Levels let operators dial verbosity (default `info`; `debug` when investigating). Equally important, a logging subsystem that can't keep up becomes the bottleneck — the legacy `error_logger` was a classic overload point. `logger` supports handler overload protection (burst limits, dropping); configure it so a log storm degrades logging, not the node.

**See also**: OPS-01, OPS-12, `03-error-handling.md` (EH-14)

---

## OPS-12: Shed Load and Apply Back-Pressure Under Overload

**Strength**: SHOULD

**Summary**: When demand exceeds capacity, slow producers (synchronous calls) or drop work deliberately — don't let queues grow unbounded.

```erlang
%% Bad - absorb all incoming work asynchronously; the mailbox grows until OOM
handle_cast({job, J}, S) -> {noreply, enqueue(J, S)}.

%% Good - bounded intake: back-pressure via call, or shed load when full
handle_call({job, J}, _From, S) ->
    case queue_len(S) < max() of
        true  -> {reply, ok, enqueue(J, S)};
        false -> {reply, {error, overloaded}, S}   %% shed; let the caller back off
    end.
```

**Rationale**: Erlang's asynchronous messaging makes it easy to accept work faster than you can do it, converting a spike into unbounded memory growth (OPS-07). Synchronous calls apply natural back-pressure (BEH-04/PF-18); explicit load-shedding (reject, sample, or drop) keeps the system degrading gracefully instead of collapsing. Decide the policy before overload, not during.

**See also**: OPS-07, `10-performance.md` (PF-18), `07-otp-behaviours.md` (BEH-04)

---

## OPS-13: Watch VM Metrics for Anomalies

**Strength**: SHOULD

**Summary**: Continuously track process count, port count, memory, run-queue length, and reductions; alert on anomalies.

```erlang
%% Bad - no visibility; find out about a process/port leak only when the node dies

%% Good - sample key VM metrics into your monitoring system
#{process_count => erlang:system_info(process_count),
  port_count    => erlang:system_info(port_count),
  run_queue     => erlang:statistics(run_queue),
  memory        => erlang:memory(total)}.
%% feed these to telemetry/metrics; alert on sustained growth
```

**Rationale**: A steadily climbing process or port count is a leak (PC-07/PC-11); a growing run queue means the schedulers can't keep up (PF-15); rising memory with stable load is often a binary or ETS leak. Trending these metrics turns silent resource exhaustion into an alert hours before the node dies. Libraries (telemetry, recon) make collection easy.

**See also**: OPS-06, OPS-10

---

## OPS-14: Protect Sensitive Data in Logs and Dumps

**Strength**: CONSIDER

**Summary**: Keep secrets (tokens, passwords, PII) out of logs, crash dumps, and process state that introspection or dumps expose.

```erlang
%% Bad - secrets sit in plain state and get logged / dumped verbatim
-record(state, {api_key :: binary()}).
logger:info("state", #{state => State}).        %% leaks api_key into logs

%% Good - keep secrets out of logged state; redact at the boundary
logger:info("authenticated", #{user => User}),  %% no secret
%% store secrets so they aren't trivially printed (e.g. opaque wrapper, redacted formatting)
```

**Rationale**: `sys:get_state/1`, crash dumps, and naive `logger` calls all expose process state, so any secret living there can leak to logs or a dump file shipped off-box. Redact or avoid logging secret-bearing state, and consider wrapping secrets so accidental printing doesn't reveal them. This is an operational complement to "fail politely" (FT-04).

**See also**: OPS-11, `09-fault-tolerance.md` (FT-04)

---

## OPS-15: Capacity-Plan Against Known VM Limits

**Strength**: CONSIDER

**Summary**: Know the limits that bite — process count, port/atom tables, ETS tables, file descriptors — and provision/configure headroom before overload.

```erlang
%% Bad - run with defaults and discover the process/port ceiling during a traffic spike

%% Good - know and raise the relevant limits, and measure headroom
1> erlang:system_info(process_limit).   %% default ~262k; raise with +P
2> erlang:system_info(port_limit).      %% raise with +Q
%% set +P/+Q/+t (atoms), ERL_MAX_PORTS, OS file-descriptor limits in vm.args
```

**Rationale**: The BEAM has configurable ceilings — process count (`+P`), ports (`+Q`), atoms (`+t`), plus OS file-descriptor limits — and hitting one mid-incident is an abrupt failure. Capacity planning means knowing your steady-state and peak counts (OPS-13), setting limits with headroom in `vm.args`, and load-testing to the ceiling deliberately rather than discovering it in production.

**See also**: OPS-13, `10-performance.md` (PF-14)

---

## OPS-16: Use Hot Code Loading Deliberately

**Strength**: CONSIDER

**Summary**: Live code upgrades (`release_handler`/`relup`) are powerful but intricate; for most deployments a rolling restart of supervised nodes is simpler and safer.

```erlang
%% Bad - hot-load a module with l(Mod) in production with no plan for in-flight state/processes
1> l(my_server).   %% old processes may crash on the next message if state shape changed

%% Good - either a planned release upgrade with appup/relup, or a rolling restart
%% rolling restart: take a node out, deploy the new release, rejoin; repeat.
%% live upgrade: relup with code_change/3 (BEH-11) and the appup instructions
```

**Rationale**: Hot code loading lets a running system upgrade without downtime, but it requires `code_change/3` (BEH-11), correct `appup`/`relup` instructions (including `changing-a-supervisor`, `module-dependencies`), and care with in-flight processes. Naively `l(Mod)`-ing a changed module can crash processes holding old-shaped state. Unless zero-downtime upgrade is a hard requirement, a rolling restart across a supervised cluster is the lower-risk path.

**See also**: `08-supervision-and-applications.md` (SUP-17), `07-otp-behaviours.md` (BEH-11)

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| OPS-01 No `io:format` in prod | SHOULD | Structured `logger`, not console prints |
| OPS-02 Remote shell | SHOULD | Inspect the live node; don't restart it |
| OPS-03 observer + BIFs | SHOULD | See processes, memory, trees directly |
| OPS-04 `recon_trace` | SHOULD | Rate-limited tracing, not raw `dbg` |
| OPS-05 Pid ∩ pattern | SHOULD | Scope both; never trace everything |
| OPS-06 `recon:proc_count` | SHOULD | Rank processes by metric |
| OPS-07 Growing mailbox | SHOULD | Overload's most common signature |
| OPS-08 `recon:bin_leak` | SHOULD | Find and fix refc-binary leaks |
| OPS-09 Crash-dump analysis | CONSIDER | Summarise first, then drill in |
| OPS-10 `system_monitor` | CONSIDER | Alert on long GC / large heap / busy ports |
| OPS-11 `logger` + overload | SHOULD | Levels; logging can't sink the node |
| OPS-12 Load shedding | SHOULD | Back-pressure or drop; no unbounded queues |
| OPS-13 VM metrics | SHOULD | Trend counts/memory; catch leaks early |
| OPS-14 Protect secrets | CONSIDER | Keep secrets out of logs/dumps/state |
| OPS-15 Capacity planning | CONSIDER | Know and raise VM limits with headroom |
| OPS-16 Hot loading | CONSIDER | Rolling restart unless zero-downtime is required |

## Related Guidelines

- **Performance**: See `10-performance.md` — refc leaks (PF-07), schedulers (PF-15), and back-pressure (PF-18) are the cost model behind these diagnostics.
- **Processes & concurrency**: See `06-processes-and-concurrency.md` — mailbox growth (PC-08/PC-09) and process/name leaks (PC-07/PC-11).
- **Fault tolerance & supervision**: See `09-fault-tolerance.md` and `08-supervision-and-applications.md` — the recovery the ops tooling observes.
- **Error handling**: See `03-error-handling.md` (EH-14) for the `logger` usage OPS-01/OPS-11 build on.
- **Distribution**: See `16-distribution.md` (DIST-05) — the cookie/trusted-network precondition for remote shells.

## External References

- *Erlang in Anger* (Fred Hébert) — tracing, recon, crash dumps, memory leaks, overload
- [recon library](https://ferd.github.io/recon/)
- [Erlang/OTP — observer](https://www.erlang.org/doc/apps/observer/observer_ug.html) and [Runtime Tools](https://www.erlang.org/doc/apps/runtime_tools/)
- Inaka Erlang Guidelines — no debug calls in production
