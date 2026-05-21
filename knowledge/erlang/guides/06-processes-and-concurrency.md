# Processes and Concurrency

How to model concurrency with Erlang processes: how many processes and what role each plays, the message protocol (tag, hide, correlate), tail-recursive loops, spawning linked or monitored, mailbox discipline, registration, timeouts, and the copy-not-share model. The link/monitor *fault* semantics are developed further in `09-fault-tolerance.md`; the behaviours that wrap these primitives live in `07-otp-behaviours.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the Erlang Programming Rules (§5.4, §5.5, §5.7, §5.9), the Erlang Reference Manual (Processes), Programming Erlang, Learn You Some Erlang, and Designing for Scalability with Erlang/OTP.

---

## PC-01: One Process per Truly Concurrent Activity

**Strength**: SHOULD

**Summary**: Model each genuinely concurrent real-world activity with exactly one process; don't serialise concurrent work, and don't invent concurrency that isn't there.

```erlang
%% Bad - one process handles every connection in turn: one slow client blocks all the others
loop([Conn | Rest]) -> handle_fully(Conn), loop(Rest).

%% Good - one process per real concurrent activity (one per connection)
accept_loop(LSock) ->
    {ok, Sock} = gen_tcp:accept(LSock),
    spawn(fun() -> handle(Sock) end),     %% each connection proceeds concurrently
    accept_loop(LSock).
```

**Rationale**: "Use one parallel process to model each truly concurrent activity in the real world" (Programming Rules §5.4). A one-to-one mapping between processes and real concurrent activities makes the structure of the program mirror the structure of the problem. Processes are cheap, so model the real concurrency — but don't spawn a process for a step that is inherently sequential.

**See also**: PC-02, PC-16

---

## PC-02: One Role per Process

**Strength**: SHOULD

**Summary**: A process should be a client *or* a server, a supervisor *or* a worker — not a combination.

```erlang
%% Bad - one process does risky work AND tries to supervise/restart its peers
loop(State) ->
    do_risky_work(),
    maybe_restart_others(),       %% supervising while also being a fallible worker
    loop(State).

%% Good - separate roles: workers do (and may crash); a supervisor watches and restarts them
%% worker:     loop(State) -> loop(do_work(State)).
%% supervisor: a supervisor behaviour monitoring the workers (chapter 08)
```

**Rationale**: "As far as possible a process should only have one role, i.e. it can be a client or a server but should not combine these roles" (Programming Rules §5.5). Mixing a fallible worker role with a supervising role means the thing that is supposed to recover failures is itself in the blast radius. Clean role separation is what makes the supervision model work.

**See also**: PC-01, `08-supervision-and-applications.md`

---

## PC-03: Implement a Process in One Module

**Strength**: SHOULD

**Summary**: Keep a process's loop and message handling together in a single module, so its protocol lives in one place.

```erlang
%% Bad - a process's receive logic is scattered: another module receives on its behalf

%% Good - the process and its loop are one module; all its messages are handled here
-module(counter).
loop(N) ->
    receive
        {incr, _}    -> loop(N + 1);
        {get, From}  -> From ! {count, N}, loop(N)
    end.
```

**Rationale**: A process is defined by the messages it accepts and the state it threads; spreading that across modules makes the protocol impossible to read or change safely. One module per process keeps the receive clauses, the state shape, and the API functions (PC-05) co-located — the same locality OTP behaviours give you for free.

**See also**: PC-05, PC-16, `01-core-idioms.md` (ID-10)

---

## PC-04: Tag All Messages

**Strength**: SHOULD

**Summary**: Every message carries a leading atom tag, so `receive`-clause order doesn't matter and new message types don't clash.

```erlang
%% Bad - untagged message; adding a new shape below it creates an ambiguous match
loop() -> receive {Mod, Fun, Args} -> apply(Mod, Fun, Args), loop() end.

%% Good - tag every message; clause order is then insignificant and new messages are safe to add
loop() ->
    receive
        {run, Mod, Fun, Args} -> apply(Mod, Fun, Args), loop();
        {status, From, Opt}   -> From ! {status_info, status(Opt)}, loop()
    end.
```

**Rationale**: "All messages should be tagged. This makes the order in the receive statement less important and the implementation of new messages easier" (Programming Rules §5.7). An untagged `{Mod, Fun, Args}` greedily matches three-tuples, so a later `{status, From, Opt}` is shadowed. Tag synchronous replies with a *distinct* atom from the request, which also aids debugging.

**See also**: PC-05, PC-10

---

## PC-05: Hide the Message Protocol Behind API Functions

**Strength**: SHOULD

**Summary**: Callers should invoke functions, not send raw messages; wrap each send/receive in an API function so the wire format stays private.

```erlang
%% Bad - callers send raw messages and must know the wire format
account ! {withdraw, self(), Amt},
receive {ok, Bal} -> Bal end.

%% Good - the protocol is encapsulated in a named API function
withdraw(Amt) ->
    account ! {withdraw, self(), Amt},
    receive {ok, Bal} -> Bal end.
```

**Rationale**: Exposing the message format couples every caller to it, so it can never change; an API function gives the interaction a name, a spec, and a single point of change. This is the hand-rolled equivalent of BEH-03 (encapsulate `gen_server` calls) — and a strong reason to just use a behaviour (PC-16).

**See also**: PC-04, PC-16, `07-otp-behaviours.md` (BEH-03)

---

## PC-06: Make Server Loops Tail-Recursive

**Strength**: MUST

**Summary**: The recursive call that continues a process loop must be in tail position; anything else grows the stack without bound.

```erlang
%% Bad - the loop call is used in a cons, so it is NOT a tail call; the stack grows per message
loop(State) ->
    receive
        {req, From} ->
            From ! compute(State),
            [done | loop(State)]      %% loop/1 inside a cons -> a frame is kept on every iteration
    end.

%% Good - the recursive loop call is the last action in the clause
loop(State) ->
    receive
        {req, From} ->
            From ! compute(State),
            loop(State)
    end.
```

**Rationale**: "All servers must be tail-recursive, otherwise the server will consume memory until the system runs out of it" (Programming Rules §5.9). A long-lived loop runs effectively forever, so a single non-tail call per iteration leaks a stack frame per message until the node dies. Keep the loop call last (a generic server library guarantees this automatically — PC-16).

**See also**: PC-16, `01-core-idioms.md`

---

## PC-07: Spawn Linked or Monitored, Not Bare

**Strength**: SHOULD

**Summary**: For any process whose life you care about, use `spawn_link` (shared fate) or `spawn_monitor` (observe) — not bare `spawn`.

```erlang
%% Bad - bare spawn: if the child crashes, nobody is notified and nothing cleans up
Pid = spawn(fun() -> work() end).

%% Good - link for shared fate, or monitor to observe; both atomic at spawn time
Pid       = spawn_link(fun() -> work() end),       %% child crash propagates to us
{P, Ref}  = spawn_monitor(fun() -> work() end).    %% {'DOWN', Ref, ...} on crash; no trap_exit needed
```

**Rationale**: A bare `spawn`'d process is invisible after creation — its crash is silent and unrecoverable. `spawn_link` ties lifetimes together (the basis of supervision); `spawn_monitor` returns `{Pid, Ref}` and sends `{'DOWN', Ref, process, Pid, Why}` on death without requiring the parent to trap exits. Both establish the relationship atomically, closing the spawn-then-link race (FT-08).

**See also**: PC-10, `09-fault-tolerance.md` (FT-08, FT-09)

---

## PC-08: Always Drain Unexpected Messages

**Strength**: SHOULD

**Summary**: Give every long-lived `receive` a catch-all clause that logs and discards unknown messages, or they accumulate in the mailbox forever.

```erlang
%% Bad - no catch-all: any message that doesn't match stays in the mailbox indefinitely
loop(S) -> receive {work, X} -> loop(do(X, S)) end.

%% Good - drain (and log) anything unexpected so the mailbox can't grow without bound
loop(S) ->
    receive
        {work, X} -> loop(do(X, S));
        Other     -> logger:warning("unexpected message: ~p", [Other]), loop(S)
    end.
```

**Rationale**: A `receive` only removes messages that match a clause; unmatched messages remain queued. Without a catch-all, stray or obsolete messages pile up, growing memory and slowing every selective receive (PC-09). Logging them also surfaces protocol bugs you'd otherwise never see. (`gen_server` routes these to `handle_info/2`, BEH-07.)

**See also**: PC-09, `07-otp-behaviours.md` (BEH-07)

---

## PC-09: Avoid Selective Receive over Large Mailboxes

**Strength**: CONSIDER

**Summary**: Selectively receiving one tag while many other messages sit ahead of it rescans the mailbox each time; keep mailboxes small and drain in order.

```erlang
%% Bad - wait for one specific tag while thousands of unrelated messages queue ahead: O(mailbox) per receive
receive {result, R} -> R end.

%% Good - handle messages as they arrive (don't let unrelated ones accumulate); correlate with a ref
receive
    {result, R} -> R;
    Other       -> handle_other(Other)
end.
```

**Rationale**: A selective `receive` scans the mailbox from the front for a matching message, so a large backlog makes each receive proportionally expensive. The runtime *does* optimise the common case where a `make_ref()` is created just before the receive (it can skip messages older than the ref) — which is exactly the `ref`-correlated pattern (PC-10). Otherwise, keep mailboxes drained.

**See also**: PC-08, PC-10, `10-performance.md`

---

## PC-10: Correlate Synchronous Replies with a Unique Reference

**Strength**: SHOULD

**Summary**: For a request/reply over messages, include a fresh `make_ref()` (and ideally a monitor) so only *this* request's reply matches.

```erlang
%% Bad - reply isn't correlated; a stray or late reply from a prior request can be mismatched
Server ! {req, self()},
receive {reply, R} -> R end.

%% Good - a unique ref ties the reply to this request (and a monitor catches a dead server)
Ref = erlang:monitor(process, Server),
Server ! {req, self(), Ref},
receive
    {reply, Ref, R}                   -> erlang:demonitor(Ref, [flush]), R;
    {'DOWN', Ref, process, _, Reason} -> {error, Reason}
end.
%% better still: gen_server:call/2 does exactly this for you (PC-16)
```

**Rationale**: Without a correlation token, a reply left over from an earlier (timed-out) request can be mistaken for the current one. A unique reference makes the match exact, and pairing it with a monitor turns a dead server into `{error, Reason}` instead of an infinite wait. This *is* what `gen_server:call` implements — another reason to prefer the behaviour.

**See also**: PC-07, PC-09, PC-13

---

## PC-11: Register Only Long-Lived Singletons

**Strength**: CONSIDER

**Summary**: Use a registered name only for a stable, one-per-node service; pass pids for everything transient or multiple.

```erlang
%% Bad - register transient, per-request workers by a synthesised name: clashes, races, leaks
register(list_to_atom("worker_" ++ integer_to_list(N)), Pid).

%% Good - register a single well-known service; pass pids for the rest
register(account_server, Pid).
```

**Rationale**: A registered name is an atom, node-local, unique (only one process per name), and auto-unregistered when the process dies (Reference Manual). That fits a singleton service, not a fleet of workers — synthesising atom names per worker risks clashes, registration races, and atom-table growth (DT-13). For groups, use a registry/`pg` or pass pids.

**See also**: PC-07, `04-data-and-types.md` (DT-13), `16-distribution.md`

---

## PC-12: Avoid the Process Dictionary; Thread State Through the Loop

**Strength**: SHOULD

**Summary**: Keep process state in the loop's arguments (or behaviour state), not in `put`/`get` process-dictionary entries.

```erlang
%% Bad - mutable, invisible state in the process dictionary; breaks referential transparency
handle(Msg) -> put(count, get(count) + 1), reply(Msg).

%% Good - state is an explicit loop argument
loop(Count) ->
    receive
        Msg -> reply(Msg), loop(Count + 1)
    end.
```

**Rationale**: The process dictionary is destructive, per-process mutable storage; "variables in the process dictionary behave pretty much like conventional mutable variables," so using it forfeits the side-effect-free reasoning that makes Erlang code easy to follow and test (Programming Erlang advises using it sparingly). Threading state explicitly keeps it visible, testable, and inspectable via `sys:get_state`.

**See also**: PC-03, `01-core-idioms.md` (ID-15)

---

## PC-13: Put a Timeout on Receives Awaiting External Replies

**Strength**: SHOULD

**Summary**: A `receive` that waits on another process should have an `after` timeout, so a lost reply can't hang the process forever.

```erlang
%% Bad - wait forever for a reply that may never arrive; the process hangs silently
receive {reply, R} -> R end.

%% Good - bound the wait and handle the timeout explicitly
receive
    {reply, R} -> R
after 5000 ->
    {error, timeout}
end.
```

**Rationale**: If the process you're awaiting dies or never answers, an unbounded `receive` blocks indefinitely with no diagnostic. An `after` clause turns that into a handled `{error, timeout}`. (A monitor, PC-10, is the more robust complement — it tells you *why* the peer didn't reply; `gen_server:call` combines both.)

**See also**: PC-10, `09-fault-tolerance.md`

---

## PC-14: Don't Assume Global Message Ordering

**Strength**: CONSIDER

**Summary**: Erlang guarantees message order only pairwise (from one process to one other); never assume an ordering across different senders.

```erlang
%% Bad - assume A's effect is observed before B's because we sent to A first
A ! go, B ! go,
receive first_done -> proceed() end.   %% nothing orders A relative to B

%% Good - rely only on pairwise FIFO; sequence cross-process steps explicitly
A ! {go, self()},
receive {done, a} ->
    B ! {go, self()},
    receive {done, b} -> ok end
end.
```

**Rationale**: Message delivery is guaranteed to preserve order *only* between a single pair of processes (and even then only for messages, not relative to signals). There is no global clock; messages from different senders can interleave arbitrarily. Code that assumes a global order has a race that will surface under load or distribution.

**See also**: PC-10, `16-distribution.md`

---

## PC-15: Mind Message-Copy Cost — Keep Messages Small

**Strength**: CONSIDER

**Summary**: Sending a term copies it into the recipient's heap; avoid broadcasting large terms, and share big read-only data another way.

```erlang
%% Bad - send a huge term to many workers: it is copied into each mailbox
[W ! {data, HugeTerm} || W <- Workers].   %% N full copies

%% Good - keep messages small; share large data via ETS (or send a locator/reference)
ets:insert(shared, {job, HugeTerm}),
[W ! {data_ref, job} || W <- Workers].
```

**Rationale**: Erlang's share-nothing model means most terms are *copied* when sent between processes, so broadcasting a large term multiplies its cost by the number of recipients. (Large binaries — over 64 bytes — are reference-counted and shared rather than copied, which is one reason to prefer binaries for bulk data, DT-10.) Keep hot-path messages small and share bulk read-only data through ETS.

**See also**: PC-01, `10-performance.md`, `04-data-and-types.md` (DT-10)

---

## PC-16: Prefer OTP Behaviours over Hand-Rolled Loops

**Strength**: SHOULD

**Summary**: For anything beyond a trivial process, use a `gen_server`/`gen_statem` instead of a hand-written `spawn`/`receive` loop.

```erlang
%% Bad - hand-roll a stateful server with raw spawn/receive (no sys, no timeouts, no code change)
start() -> spawn(fun() -> loop(#state{}) end).
loop(S) -> receive _ -> loop(S) end.

%% Good - a gen_server gives you call/cast, tail-recursion, timeouts, and supervision for free
-behaviour(gen_server).
start_link() -> gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).
```

**Rationale**: A behaviour supplies the things this chapter spends rules establishing by hand — tagged request/reply (PC-04, PC-10), encapsulated protocol (PC-05), guaranteed tail-recursion (PC-06), mailbox handling (PC-08), and timeouts (PC-13) — plus `sys` introspection, code change, and supervision integration. Reach for raw processes (via `proc_lib` for a proper special process) only when no behaviour fits.

**See also**: PC-05, PC-06, `07-otp-behaviours.md` (BEH-01)

---

## PC-17: Use Message Passing, Not Shared-Memory Thinking

**Strength**: CONSIDER

**Summary**: Don't emulate locks and shared mutable memory; let one process own a piece of state and mutate it only by sending it messages.

```erlang
%% Bad - emulate shared memory with a lock-like acquire/mutate/release dance
Lock ! acquire, V = read(), write(V + 1), Lock ! release.

%% Good - the state lives in exactly one process; you change it by sending a message
counter ! {incr, self()},
receive {ok, _New} -> ok end.
```

**Rationale**: Erlang has no shared memory and no locks by design; concurrency is expressed by isolated processes exchanging messages. Recreating a lock protocol re-introduces the race conditions and deadlocks the model exists to avoid. Make one process the sole owner of each piece of mutable state — then there is nothing to lock.

**See also**: PC-01, PC-12, `09-fault-tolerance.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| PC-01 One process per activity | SHOULD | Model real concurrency, don't invent it |
| PC-02 One role per process | SHOULD | Client or server, supervisor or worker |
| PC-03 Process in one module | SHOULD | Keep loop + protocol co-located |
| PC-04 Tag all messages | SHOULD | Order-independent, extensible receives |
| PC-05 Hide the protocol | SHOULD | API functions over raw send/receive |
| PC-06 Tail-recursive loops | MUST | Non-tail loops leak memory forever |
| PC-07 Spawn linked/monitored | SHOULD | Bare spawn hides crashes |
| PC-08 Drain unknown messages | SHOULD | Catch-all clause or the mailbox grows |
| PC-09 Selective-receive cost | CONSIDER | Large mailboxes make receives O(n) |
| PC-10 Correlate with a ref | SHOULD | Unique ref + monitor for request/reply |
| PC-11 Register singletons only | CONSIDER | Names are node-local atoms; pass pids otherwise |
| PC-12 No process dictionary | SHOULD | Thread state through the loop |
| PC-13 Receive timeouts | SHOULD | `after` so a lost reply can't hang you |
| PC-14 No global ordering | CONSIDER | Only pairwise FIFO is guaranteed |
| PC-15 Small messages | CONSIDER | Sends copy; share bulk data via ETS |
| PC-16 Prefer behaviours | SHOULD | gen_server beats a hand-rolled loop |
| PC-17 No shared memory | CONSIDER | One owner per state; mutate by message |

## Related Guidelines

- **OTP behaviours**: See `07-otp-behaviours.md` — PC-04/05/06/08/10/13 are exactly what `gen_server` provides; PC-16 is BEH-01.
- **Fault tolerance**: See `09-fault-tolerance.md` — links/monitors (PC-07) and their exit semantics (FT-08/FT-09) are the basis of supervision.
- **Supervision & applications**: See `08-supervision-and-applications.md` for the supervisor role referenced by PC-02.
- **Performance**: See `10-performance.md` for mailbox/selective-receive cost (PC-09) and message-copy cost (PC-15).
- **Data & types**: See `04-data-and-types.md` for the atom-table risk behind PC-11 (DT-13) and binaries for bulk data (PC-15/DT-10).

## External References

- Erlang Programming Rules and Conventions — §5.4 (one process per activity), §5.5 (one role), §5.7 (tag messages), §5.9 (tail-recursive servers)
- [Erlang Reference Manual — Processes (Registered Processes, Message Sending)](https://www.erlang.org/doc/system/ref_man_processes.html)
- *Programming Erlang* (Joe Armstrong) — concurrent programming, error-handling primitives, the process dictionary
- *Learn You Some Erlang* — The Hitchhiker's Guide to Concurrency; More on Multiprocessing
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — process design and message protocols
