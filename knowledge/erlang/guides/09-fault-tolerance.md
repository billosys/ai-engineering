# Fault Tolerance and Let-It-Crash

How to build Erlang systems that stay up by *embracing* failure rather than preventing it: the error-kernel and let-it-crash philosophy, process isolation, links and monitors, exit trapping, and the supervision and recovery patterns that turn a crash into a non-event. This chapter is doctrine plus mechanics; the structural how-to of supervisors and applications lives in `08-supervision-and-applications.md`, and the runtime diagnosis of failures in production lives in `14-production-ops.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: Erlang Programming Rules (§3.13, §4.2, §5.12), Programming Erlang (ch. 13), Learn You Some Erlang (Errors & Links chapters), Erlang in Anger (ch. 2), Designing for Scalability with Erlang/OTP, and the OTP Design Principles.

---

## FT-01: Let It Crash — Don't Program Defensively

**Strength**: SHOULD

**Summary**: Write code assuming its input is correct. A function given bad input should crash, not silently invent a result; recovery happens elsewhere.

```erlang
%% Bad - defensive: swallow any failure and invent a value, hiding the real bug
to_int(Bin) ->
    try binary_to_integer(Bin) of
        N -> N
    catch _:_ -> 0            %% a malformed value silently becomes 0
    end.

%% Good - assume correct input; a bad value crashes this (supervised) process
to_int(Bin) -> binary_to_integer(Bin).
```

**Rationale**: "In general one should not test input data to functions for correctness" (Programming Rules §3.13). Defensive code that patches over bad data produces systems that are a nightmare to debug, because the symptom surfaces far from the cause. A crash, by contrast, is precise and is recovered by a supervisor (FT-11). Defensiveness has exactly one proper home — the system boundary (FT-02).

**See also**: FT-02, FT-03, FT-07, `08-supervision-and-applications.md`

---

## FT-02: Validate Once, at the Boundary

**Strength**: SHOULD

**Summary**: Check data exactly once, where it first enters the system — ideally as a guard on the client/API function — then trust it everywhere inside.

```erlang
%% Bad - no validation at the edge; bad input rides into the server and crashes it
add(X) -> gen_server:call(?MODULE, {add, X}).

%% Good - guard at the API/client boundary; the caller fails fast, the server stays clean
add(X) when is_integer(X) -> gen_server:call(?MODULE, {add, X}).
%% internal functions then trust X and never re-check it
```

**Rationale**: Data is validated once, when it first enters the system; after that it is assumed correct (Programming Rules §3.13). When you *do* program defensively, do it on the outermost (client-side) layer (Inaka guidelines): a guard on the API head rejects bad input before a round-trip to the `gen_server`, so the *caller* crashes instead of the server. Re-validating already-checked data in every internal function is noise that hides the real contract.

**See also**: FT-01, `02-api-design.md`, `05-functions-and-pattern-matching.md`

---

## FT-03: Fail Fast and Noisily

**Strength**: SHOULD

**Summary**: The instant an error is detected, crash with a meaningful, logged reason — do not patch the state and limp on.

```erlang
%% Bad - catch, patch, continue: corrupt state propagates and the bug surfaces far away
handle(Data) ->
    case parse(Data) of
        {ok, V} -> store(V);
        _Err    -> store(default())   %% limp on with a guessed value
    end.

%% Good - crash immediately with a meaningful reason; the supervisor restarts cleanly
handle(Data) ->
    {ok, V} = parse(Data),            %% a badmatch crashes here, loudly
    store(V).
```

**Rationale**: "We should fail as soon as an error occurs, and we should fail noisily… we crash immediately so as not to make matters worse" (Programming Erlang, ch. 13). A loud, immediate crash with a meaningful term is debuggable; a silently patched state is not. Never return a value for an invalid argument — raise.

**See also**: FT-01, FT-04, `03-error-handling.md`

---

## FT-04: Fail Politely at the User Boundary

**Strength**: CONSIDER

**Summary**: Let code crash internally, but at the outermost user-facing layer translate the crash into a safe message and log the detail.

```erlang
%% Bad - raw internal error leaks to the end user
handle_request(Req) ->
    Result = process(Req),            %% may crash; the user sees a stack trace
    {200, Result}.

%% Good - let it crash internally, but translate at the user boundary
handle_request(Req) ->
    try process(Req) of
        Result -> {200, Result}
    catch
        Class:Reason:Stack ->
            logger:error("request failed: ~p", [{Class, Reason, Stack}]),
            {500, <<"Something went wrong. Please try again.">>}
    end.
```

**Rationale**: "Fail politely means that only the programmer should see the detailed error messages" — detail goes to a permanent log, the user gets an alert and a remedy (Programming Erlang, ch. 13). This is the *one* legitimate place for a catch-all: the top-level request handler, a politeness boundary — not internal defensive code (contrast FT-01).

**See also**: FT-03, `03-error-handling.md`, `14-production-ops.md`

---

## FT-05: Identify the Error Kernel

**Strength**: SHOULD

**Summary**: Decide which part of the system *must* be correct, keep it small and well-tested, and push risky work outside it.

```erlang
%% Bad - one process holds critical state AND does risky parsing; a parse crash loses the state
loop(State) ->
    receive {parse, Raw} -> loop(do_risky_parse(Raw, State)) end.

%% Good - the kernel guards the state; risky work runs in a worker whose crash can't reach it
loop(State) ->
    receive
        {parse, Raw, From} ->
            spawn(fun() -> From ! {parsed, do_risky_parse(Raw)} end),
            loop(State)
    end.
```

**Rationale**: "One of the basic elements of system design is identifying which part of the system has to be correct and which part does not" (Programming Rules §4.2). As with an OS kernel, correctness effort concentrates in a minimal core that holds essential state; a failure in the larger, riskier outer layer is contained. This is the "onion-layered" design: each layer shields the more critical one inside it.

**See also**: FT-06, FT-07, `08-supervision-and-applications.md`

---

## FT-06: Isolate Independent Work in Separate Processes

**Strength**: SHOULD

**Summary**: Give each independent unit of work its own process so one failure cannot take down unrelated work.

```erlang
%% Bad - one process runs every job in sequence; one crashing job aborts the whole batch
serve(Jobs) -> lists:foreach(fun do_job/1, Jobs).

%% Good - isolate each job; a crash is contained to that one job
serve(Jobs) ->
    [spawn(fun() -> do_job(J) end) || J <- Jobs].
```

**Rationale**: Erlang processes share nothing, so a crash cannot corrupt another process's memory — failure stops at the process boundary. Isolating independent jobs prevents one bad input from causing a cascading failure across the batch. (Pair isolation with supervision, FT-11, so the isolated work is also restarted when appropriate.)

**See also**: FT-05, FT-08, `06-processes-and-concurrency.md`

---

## FT-07: Handle Errors Remotely — Let Another Process Fix It

**Strength**: SHOULD

**Summary**: Don't make a process recover its own crash in place. Let it die; an observing process detects the death and takes corrective action.

```erlang
%% Bad - the worker tries to recover its own crash in-place
work(X) ->
    try risky(X) catch _:_ -> self() ! retry, work(X) end.   %% tangled self-healing

%% Good - the worker just does the work; an observer (supervisor) decides what to do on crash
work(X) -> risky(X).
```

**Rationale**: Erlang's concurrent error handling is built on *remote* detection and handling: "Let some other process fix the error" (Programming Erlang, ch. 13). Self-healing logic entangles the happy path with recovery and tends to loop on the same fault. A separate observer (ultimately a supervisor) has the context to restart, escalate, or fail over. A genuinely fault-tolerant system needs at least two machines, since a whole machine can crash (FT-15).

**See also**: FT-08, FT-09, FT-11

---

## FT-08: Create Links Atomically with `spawn_link`

**Strength**: MUST

**Summary**: When two processes should share fate, link them at spawn time with `spawn_link` — never `spawn` followed by `link`.

```erlang
%% Bad - spawn then link: a race window where the child can die before the link exists
Pid = spawn(fun child/0),
link(Pid).                 %% if the child already crashed, no exit signal is delivered

%% Good - spawn_link is atomic: the link exists before the child can run
Pid = spawn_link(fun child/0).
```

**Rationale**: A link is bidirectional; when either participant terminates it sends an exit signal carrying the exit reason to the other (Reference Manual, "Links"). Doing `spawn` then `link` opens a race: if the child dies in the gap, the link is never established and its death goes unnoticed — exactly the bug that makes hand-rolled keep-alive code unreliable (FT-11). `spawn_link` closes the window.

**See also**: FT-09, FT-11, `06-processes-and-concurrency.md`

---

## FT-09: Monitor to Observe Without Sharing Fate

**Strength**: SHOULD

**Summary**: To watch a process you don't want to die with, use a monitor (unidirectional) and handle its `'DOWN'` message — not a link.

```erlang
%% Bad - link to a process you only want to observe: its crash now kills you too
link(Server),
ok = do_request(Server).

%% Good - monitor for one-off observation; handle DOWN, then demonitor with flush
Ref = erlang:monitor(process, Server),
Server ! {self(), Ref, request},
receive
    {Ref, Reply}                      -> erlang:demonitor(Ref, [flush]), Reply;
    {'DOWN', Ref, process, _, Reason} -> {error, Reason}
end.
```

**Rationale**: A monitor is unidirectional and informational: when the monitored process dies, the watcher receives `{'DOWN', Ref, process, Pid, Reason}` (and `noproc` immediately if it was already dead) — without the watcher itself being killed (Reference Manual, "Monitors"). Use a **link** for shared lifetime (supervised workers), a **monitor** for "tell me if it dies but don't take me down" (a client awaiting a reply). This monitor-and-`'DOWN'` pattern is exactly how `gen_server:call` detects a dead server.

**See also**: FT-08, FT-10, `07-otp-behaviours.md`

---

## FT-10: Trap Exits Sparingly, and Never Toggle

**Strength**: SHOULD

**Summary**: As few processes as possible should trap exits; a process either traps exits for its whole life or it doesn't. Toggling is an anti-pattern.

```erlang
%% Bad - a worker toggles trap_exit around a risky call: AVOID
risky(F) ->
    process_flag(trap_exit, true),
    R = F(),
    process_flag(trap_exit, false),   %% toggling makes exit semantics unpredictable
    R.

%% Good - only long-lived system processes trap, set once at startup and left fixed
init(Args) ->
    process_flag(trap_exit, true),    %% fixed for the life of this system process
    {ok, init_state(Args)}.
```

**Rationale**: "As few processes as possible should trap exit signals… it is usually very bad practice for a process to 'toggle' trapping exits" (Programming Rules §5.12). Trapping converts exit signals into `{'EXIT', Pid, Reason}` messages so a system process (e.g. a supervisor) can react instead of dying; that is its job. Toggling creates windows where an exit is handled inconsistently. Note `kill` exit signals are untrappable by design.

**See also**: FT-08, FT-11, `08-supervision-and-applications.md`

---

## FT-11: Don't Hand-Roll Keep-Alive — Supervise

**Strength**: SHOULD

**Summary**: To keep a process alive, place it under a supervisor. Do not write your own register/restart loop.

```erlang
%% Bad - hand-rolled keep-alive: a race between register and observe; reinvents OTP badly
keep_alive(Name, Fun) ->
    Pid = spawn(Fun),
    register(Name, Pid),              %% the process can die here, before we observe it
    on_exit(Pid, fun(_) -> keep_alive(Name, Fun) end).

%% Good - declare the worker as a supervised child; OTP restarts it correctly
init([]) ->
    Child = #{id => worker,
              start => {worker, start_link, []},
              restart => permanent, shutdown => 5000, type => worker},
    {ok, {#{strategy => one_for_one, intensity => 5, period => 10}, [Child]}}.
```

**Rationale**: Hand-written keep-alive has a subtle race — the process can die between `register/2` and installing the observer, so the restart never fires (Programming Erlang, ch. 13). Supervisors solve this correctly and uniformly, with restart strategies, shutdown discipline, and intensity limits. Reach for OTP rather than reimplementing it.

**See also**: FT-08, FT-12, FT-13, `08-supervision-and-applications.md`

---

## FT-12: Supervisor Init Provides Guarantees, Not Best Effort

**Strength**: MUST

**Summary**: A supervised process's `init` must reach a stable, known state *no matter what happens*. Only guarantee what you can actually ensure — never a remote dependency.

```erlang
%% Bad - guarantee a remote dependency in init; a transient netsplit crashes the whole boot
init(_) ->
    {ok, Conn} = db:connect("remote-host"),   %% expected to fail sometimes -> boot loop
    {ok, #state{conn = Conn}}.

%% Good - guarantee only what's dependable; connect asynchronously and degrade until ready
init(_) ->
    self() ! connect,                         %% trigger connection after init returns
    {ok, #state{conn = undefined}}.
%% calls return {error, not_connected} until the connection is established
```

**Rationale**: "Supervised processes provide guarantees in their initialization phase, not a best effort" (Erlang in Anger, ch. 2). Config files, local resources, and restoring stable state belong in `init`; connections to remote databases and external services do not, because their failure is *expected* during normal operation and would turn every transient outage into a crash-loop. If a guarantee genuinely cannot be met, crashing the node is the correct system-wide assertion failure — but don't manufacture guarantees you can't keep.

**See also**: FT-11, FT-13, FT-16, `08-supervision-and-applications.md`

---

## FT-13: Bound Restarts and Let Cyclic Failures Escalate

**Strength**: SHOULD

**Summary**: Set a sane restart intensity/period so that a fault a restart can't fix trips the limit and escalates to a supervisor that *can* fix it.

```erlang
%% Bad - intensity so high a cyclic crash spins forever, never escalating the real fault
{ok, {#{strategy => one_for_one, intensity => 1000000, period => 1}, Children}}.

%% Good - sane limits: a persistent fault trips the threshold and escalates to the parent
{ok, {#{strategy => one_for_one, intensity => 5, period => 10}, Children}}.
```

**Rationale**: A cyclic restart happens when restarting doesn't address the underlying fault, so the child crashes and restarts in a loop (Designing for Scalability, p. 172). When restart intensity is exceeded within the period, the supervisor terminates with `shutdown` and escalates upward — where a higher supervisor may resolve the real cause (e.g. restarting a different worker whose corrupt data was to blame). Set intensity absurdly high and you defeat this escalation; the system spins instead of healing.

**See also**: FT-11, FT-12, `08-supervision-and-applications.md`, `14-production-ops.md`

---

## FT-14: Make Operations Idempotent so Retries Are Safe

**Strength**: SHOULD

**Summary**: Message delivery is at-most-once and retries can duplicate work; design operations so applying them more than once has the same effect as once.

```erlang
%% Bad - retry after a timeout re-applies a non-idempotent effect (double charge)
charge(Account, Amount) ->
    ok = bank:debit(Account, Amount).         %% a retry debits twice

%% Good - tag the request so duplicates are recognized; the op becomes safe to retry
charge(Account, Amount, ReqId) ->
    case bank:already_applied(ReqId) of
        true  -> ok;                          %% duplicate: no additional observable effect
        false -> bank:debit(Account, Amount, ReqId)
    end.
```

**Rationale**: An idempotent operation "can be applied multiple times with the same effect as applying it once" (Designing for Scalability, p. 409). Because a crashed-and-restarted client may resend, and message delivery offers no exactly-once guarantee, idempotence (often via a unique request id) is what makes retry safe in the presence of transient failures — the foundation of practical exactly-once semantics.

**See also**: FT-07, FT-15, `06-processes-and-concurrency.md`

---

## FT-15: Remove Single Points of Failure with Redundancy

**Strength**: CONSIDER

**Summary**: A truly fault-tolerant service needs more than one node; use distributed application failover/takeover so a surviving node continues the service.

```erlang
%% Bad - a single registered server on one node: that node dies, the service is gone
start() -> register(svc, spawn(fun loop/0)).

%% Good - a distributed application with a failover node (sys.config)
{kernel, [{distributed, [{my_app, 5000, ['a@host', 'b@host']}]},
          {sync_nodes_mandatory, ['b@host']},
          {sync_nodes_timeout, 30000}]}.
%% my_app runs on a@host; if a@host dies, it starts on b@host after 5s
```

**Rationale**: "A genuinely fault-tolerant system needs at least two machines, since one whole machine may crash" (Programming Erlang, ch. 13). Supervision recovers process and subtree failures within a node; surviving a node or hardware failure requires redundancy across nodes, via OTP distributed applications (failover/takeover) or an application-level replication strategy. This is a design-cost trade-off, hence CONSIDER.

**See also**: FT-14, `16-distribution.md`, `08-supervision-and-applications.md`

---

## FT-16: Back Off When Restarting or Reconnecting to External Resources

**Strength**: CONSIDER

**Summary**: When retrying a connection to a downed external dependency, use capped exponential back-off — never a tight loop.

```erlang
%% Bad - tight reconnect loop hammers a downed dependency and floods the logs
reconnect(Host) ->
    case db:connect(Host) of
        {ok, C}    -> C;
        {error, _} -> reconnect(Host)         %% no delay: busy-spins on failure
    end.

%% Good - capped exponential back-off (add jitter in production)
reconnect(Host, Delay) ->
    case db:connect(Host) of
        {ok, C}    -> C;
        {error, _} ->
            timer:sleep(Delay),
            reconnect(Host, min(Delay * 2, 30000))
    end.
```

**Rationale**: A connection that belongs *outside* `init` (FT-12) still needs a retry policy. A tight loop turns a dependency outage into a CPU-and-log storm and can prevent the dependency from recovering. Capped exponential back-off (ideally with jitter) spaces attempts out. Note this is a deliberate, bounded retry at a boundary — not internal defensive coding (FT-01).

**See also**: FT-12, FT-14, `14-production-ops.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| FT-01 Let it crash | SHOULD | Don't test input for correctness; crash and recover elsewhere |
| FT-02 Validate at the boundary | SHOULD | Check once, at the client/API edge; trust thereafter |
| FT-03 Fail fast and noisily | SHOULD | Crash immediately with a meaningful, logged reason |
| FT-04 Fail politely | CONSIDER | User sees an alert; the log gets the detail |
| FT-05 Identify the error kernel | SHOULD | Keep the must-be-correct core small; push risk outward |
| FT-06 Isolate work in processes | SHOULD | Shared-nothing processes contain failure |
| FT-07 Handle errors remotely | SHOULD | Let an observer fix it, not the failing process |
| FT-08 `spawn_link` atomically | MUST | Avoid the spawn-then-link race |
| FT-09 Monitor to observe | SHOULD | Unidirectional `'DOWN'`; don't share fate when you only watch |
| FT-10 Trap exits sparingly | SHOULD | Few processes trap; never toggle the flag |
| FT-11 Supervise, don't keep-alive | SHOULD | OTP supervisors beat hand-rolled restart loops |
| FT-12 Init = guarantees | MUST | Never guarantee a remote dependency in `init` |
| FT-13 Bound & escalate restarts | SHOULD | Sane intensity lets cyclic faults escalate upward |
| FT-14 Idempotent operations | SHOULD | Make retries safe; recognize duplicates |
| FT-15 Remove single points of failure | CONSIDER | Real fault tolerance needs ≥2 nodes |
| FT-16 Back off on reconnect | CONSIDER | Capped exponential back-off, not a tight loop |

## Related Guidelines

- **Supervision & applications**: See `08-supervision-and-applications.md` for supervisor structure, restart strategies, child specs, and releases — the machinery FT-11…FT-13 rely on.
- **Error handling**: See `03-error-handling.md` for errors vs exits vs throws and `try`/`catch` discipline behind FT-03/FT-04.
- **Processes & concurrency**: See `06-processes-and-concurrency.md` for the link/monitor/exit-signal primitives used in FT-08…FT-10.
- **OTP behaviours**: See `07-otp-behaviours.md` for how `gen_server`/`gen_statem` callbacks embody FT-01 and FT-12.
- **Production ops**: See `14-production-ops.md` for diagnosing crashes, restart storms, and overload at runtime.

## External References

- Erlang Programming Rules and Conventions — §3.13 (don't program defensively), §4.2 (error kernel), §5.12 (trapping exits)
- [OTP Design Principles — Supervisor Behaviour](https://www.erlang.org/doc/system/sup_princ.html)
- [Erlang Reference Manual — Processes (Links, Monitors, Exit Signals)](https://www.erlang.org/doc/system/ref_man_processes.html)
- *Erlang in Anger* (Fred Hébert), ch. 2 — "It's About the Guarantees"
- *Programming Erlang* (Joe Armstrong), ch. 13 — Error Handling Philosophy
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — cyclic restart (p. 172), idempotence (p. 409)
- [Learn You Some Erlang — Errors and Processes / Building an Application](https://learnyousomeerlang.com/content)
