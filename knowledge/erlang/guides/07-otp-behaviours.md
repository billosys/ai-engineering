# OTP Behaviours

How to use the standard OTP behaviours — `gen_server`, `gen_statem`, `gen_event` — and how to write your own: the behaviour contract, callback design, state management, `call`/`cast`/`info` semantics, and the traps (blocking callbacks, synchronous deadlocks, heavy `init`). The structural placement of behaviours under supervisors lives in `08-supervision-and-applications.md`; the let-it-crash reasoning behind their callbacks lives in `09-fault-tolerance.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the OTP Design Principles (Behaviours, gen_server, gen_statem, gen_event), Programming Rules (§5.6), Inaka guidelines (OTP), Designing for Scalability with Erlang/OTP, Programming Erlang, and Learn You Some Erlang.

---

## BEH-01: Build Servers on OTP Behaviours, Not Hand-Rolled Loops

**Strength**: SHOULD

**Summary**: Implement long-lived processes as OTP behaviours rather than writing your own `receive` loop; you inherit `call`/`cast`, system messages, introspection, code change, and clean supervision.

```erlang
%% Bad - hand-rolled server loop: no sys/debug support, no code upgrade, ad-hoc protocol
loop(State) ->
    receive
        {From, Req} -> From ! {self(), handle(Req, State)}, loop(State)
    end.

%% Good - a gen_server gives you call/cast, sys introspection, code_change and supervision for free
-behaviour(gen_server).
init(Args) -> {ok, init_state(Args)}.
handle_call(Req, _From, State) -> {reply, handle(Req, State), State}.
```

**Rationale**: "Consistent use of a small set of generic servers will greatly simplify the total system structure" (Programming Rules §5.6). A behaviour separates the generic part (message loop, system messages, debugging via `sys`, hot code change) from your callback code, and integrates with supervision. Hand-rolled loops re-implement all of this — usually incompletely (see `proc_lib`/special processes only when no behaviour fits).

**See also**: BEH-02, BEH-05, `08-supervision-and-applications.md`

---

## BEH-02: Declare `-behaviour` So the Compiler Checks Your Callbacks

**Strength**: SHOULD

**Summary**: Put a `-behaviour(...)` attribute in every callback module so the compiler warns about missing or mis-specified callbacks.

```erlang
%% Bad - callback module with no -behaviour attribute; a missing/typo'd callback is found only at runtime
-module(my_server).
-export([init/1, handle_call/3]).

%% Good - declare the behaviour; the compiler warns on missing or mis-typed callbacks
-module(my_server).
-behaviour(gen_server).
```

**Rationale**: The `-behaviour` attribute ties the module to the behaviour's `-callback` contract, so the compiler flags absent or wrongly-arity'd callbacks at compile time instead of letting them fail in production. It also documents intent and helps tools (and humans) navigate (Erlang in Anger calls the attribute a "navigation clue").

**See also**: BEH-01, BEH-17

---

## BEH-03: Encapsulate Every `call`/`cast` Behind an API Function

**Strength**: SHOULD

**Summary**: Never make raw `gen_server:call`/`cast` across module boundaries; wrap each in a named, `-spec`'d API function in the module that implements the matching callback.

```erlang
%% Bad - raw call from another module: the message format leaks and there's no searchable contract
%% client_mod.erl:
Reply = gen_server:call(account_server, {withdraw, Id, Amt}).

%% Good - wrap it beside its handle_call, behind a named API function with a spec
%% account_server.erl:
-spec withdraw(id(), money()) -> {ok, money()} | {error, term()}.
withdraw(Id, Amt) -> gen_server:call(?MODULE, {withdraw, Id, Amt}).
handle_call({withdraw, Id, Amt}, _From, State) -> %% ...
```

**Rationale**: "Never do raw `gen_server` calls across module boundaries; the call should be encapsulated in an API function in the same module that implements the corresponding `handle_call`" (Inaka). The API function gives the message a name, a spec, and a single place to change the wire format — even the behaviour itself — without touching callers.

**See also**: BEH-04, `02-api-design.md`

---

## BEH-04: `call` for Replies and Back-Pressure, `cast` for Fire-and-Forget

**Strength**: SHOULD

**Summary**: Use `call` (synchronous) when you need a reply or flow control; use `cast` (asynchronous) only for genuine fire-and-forget. Don't fake one with the other.

```erlang
%% Bad - cast where the caller needs the answer, then waits on an ad-hoc reply message
ok = gen_server:cast(?MODULE, {compute, Job}),
receive {result, R} -> R end.

%% Good - call when you need a reply or back-pressure; cast only when you truly don't
R = gen_server:call(?MODULE, {compute, Job}),     %% synchronous + back-pressured
gen_server:cast(?MODULE, {log, Event}).           %% genuinely fire-and-forget
```

**Rationale**: `call` blocks the caller until the server replies, which both delivers the result and applies natural back-pressure (a slow server slows its callers rather than growing an unbounded mailbox). `cast` returns immediately and drops that feedback — fine for notifications, dangerous for work the caller depends on or that can outpace the server.

**See also**: BEH-05, BEH-06

---

## BEH-05: Keep Callbacks Fast — Never Block `handle_call`

**Strength**: MUST

**Summary**: A `gen_server` handles one message at a time; doing slow or blocking work inside a callback serialises every client. Offload it and reply asynchronously.

```erlang
%% Bad - slow work inside handle_call serialises all clients and risks the 5s call timeout
handle_call({fetch, Url}, _From, State) ->
    {reply, slow_http_get(Url), State}.            %% every other caller is blocked meanwhile

%% Good - hand the work to a task and reply later with gen_server:reply/2
handle_call({fetch, Url}, From, State) ->
    spawn(fun() -> gen_server:reply(From, slow_http_get(Url)) end),
    {noreply, State}.
```

**Rationale**: The behaviour's loop is single-threaded over the mailbox: while a callback runs, no other request is served and the mailbox grows. Blocking in `handle_call` turns one slow dependency into a stalled server and a cascade of `call` timeouts. Return `{noreply, State}` and answer with `gen_server:reply/2` from a spawned worker, or use a separate pool.

**See also**: BEH-04, BEH-06, `09-fault-tolerance.md`

---

## BEH-06: Avoid Synchronous Call Cycles; Respect the `call` Timeout

**Strength**: CONSIDER

**Summary**: Two servers that synchronously call each other in a cycle deadlock until the `call` timeout fires. Break cycles by replying asynchronously or calling only "older" processes.

```erlang
%% Bad - A calls B which (transitively) calls back into A: both block until the 5s timeout
handle_call(work, _From, S) ->
    Sub = gen_server:call(server_b, sub_work),     %% server_b ends up calling server_a -> deadlock
    {reply, Sub, S}.

%% Good - break the cycle: defer the reply and let B answer the original caller later
handle_call(work, From, S) ->
    gen_server:cast(server_b, {sub_work, From}),   %% B replies to From; A doesn't block on B
    {noreply, S}.
```

**Rationale**: "This problem is resolved not through complex deadlock-prevention algorithms, but through timeouts… A standard practice is to allow synchronous calls only to processes that were started before the process making the call; calls from older to younger processes may only be asynchronous" (Designing for Scalability, pp. 94–95). The default 5 s `call` timeout is a safety net, not a design — avoid the cycle.

**See also**: BEH-04, BEH-05

---

## BEH-07: Implement `handle_info` and Tolerate Unexpected Messages

**Strength**: SHOULD

**Summary**: Any message that isn't a `call`/`cast` lands in `handle_info`; handle the ones you expect and log-and-ignore the rest rather than crashing on noise.

```erlang
%% Bad - crash on any unrecognised message; one stray message kills the server
handle_info(Msg, _State) -> exit({unexpected, Msg}).

%% Good - handle expected messages, log and ignore the rest
handle_info({'DOWN', Ref, process, _Pid, _Reason}, State) ->
    {noreply, forget(Ref, State)};
handle_info(Info, State) ->
    logger:warning("~p got unexpected message: ~p", [?MODULE, Info]),
    {noreply, State}.
```

**Rationale**: A `gen_server` receives `'DOWN'` messages, `'EXIT'` signals (when trapping), timer messages, and stray sends to its pid; all arrive via `handle_info/2` (OTP Design Principles). Crashing on an unexpected message turns harmless noise into downtime. Match what you depend on; log the rest so it's visible without being fatal.

**See also**: BEH-05, `09-fault-tolerance.md`

---

## BEH-08: Keep Server State in a Named, Typed Record

**Strength**: SHOULD

**Summary**: Represent a behaviour's state as a `#state{}` record (typed fields), not a bare tuple, so callbacks read clearly and the compiler catches field mistakes.

```erlang
%% Bad - positional tuple as state; every callback must remember the field order
init(_) -> {ok, {[], 0, undefined}}.

%% Good - a named, typed record makes state self-documenting and typo-safe
-record(state, {queue = []    :: list(),
                count = 0      :: non_neg_integer(),
                conn           :: pid() | undefined}).
init(_) -> {ok, #state{}}.
```

**Rationale**: State threads through every callback; a positional tuple forces each one to know the layout and breaks silently when it changes. A conventionally-named `#state{}` record (Inaka recommends the explicit `state` name) gives typed fields, defaults, and selector access (see DT-02/DT-03 in `04-data-and-types.md`).

**See also**: BEH-11, `04-data-and-types.md`

---

## BEH-09: Keep `init` Light — `start_link` Is Synchronous

**Strength**: SHOULD

**Summary**: `start_link` does not return until `init/1` returns, so heavy or blocking work in `init` stalls the whole supervised startup. Return fast and continue heavy work afterwards.

```erlang
%% Bad - heavy/blocking work in init: start_link can't return; the supervisor's boot stalls or times out
init(_) ->
    Data = load_everything_from_remote(),          %% blocks the entire startup chain
    {ok, #state{data = Data}}.

%% Good - return quickly, then do heavy work in handle_continue (or via a self-sent message)
init(_) ->
    {ok, #state{data = undefined}, {continue, load}}.
handle_continue(load, State) ->
    {noreply, State#state{data = load_everything()}}.
```

**Rationale**: `gen_server:start_link/4` is synchronous — it blocks until `init/1` completes (OTP Design Principles), and a supervisor starts its children in order, so a slow `init` delays or fails the boot of everything after it. `handle_continue/2` runs immediately after `init` but off the critical start path. This is the behaviour-level expression of FT-12: only guarantee in `init` what you can guarantee quickly and reliably.

**See also**: BEH-05, `09-fault-tolerance.md` (FT-12)

---

## BEH-10: `terminate` Is Best-Effort — Don't Rely on It for Critical Cleanup

**Strength**: SHOULD

**Summary**: `terminate/2` is not guaranteed to run (e.g. on `kill`, or when not trapping exits); persist critical data as you go, not at shutdown.

```erlang
%% Bad - rely on terminate to flush critical data; it may never run (brutal kill, untrapped exit)
terminate(_Reason, State) -> persist_everything(State), ok.

%% Good - persist incrementally during operation; terminate is best-effort cleanup only
handle_cast({write, X}, State) -> ok = persist(X), {noreply, State};
terminate(_Reason, _State) -> ok.
```

**Rationale**: `terminate/2` runs only when the process exits "cleanly" — it is skipped on `exit(Pid, kill)` and only runs on supervisor shutdown if the process traps exits (and within the child's shutdown timeout). Treat it as a flush-buffers/close-sockets nicety, never as the durability mechanism for state you cannot lose.

**See also**: BEH-09, `08-supervision-and-applications.md`

---

## BEH-11: Implement `code_change` for State Migrations

**Strength**: CONSIDER

**Summary**: If a hot release changes the shape of your server state, migrate the old representation in `code_change/3`.

```erlang
%% Bad - no code_change; after changing the #state{} shape, a hot upgrade leaves callbacks
%% matching the new record against an old-format state term -> crash on the next message

%% Good - migrate the old state representation to the new one in code_change/3
code_change(_OldVsn, {state, Q, C}, _Extra) ->     %% old 3-tuple state
    {ok, #state{queue = Q, count = C, conn = undefined}}.
```

**Rationale**: During a release upgrade, the running process keeps its existing state term while the new code expects the new shape; `code_change/3` is the hook that rewrites the term so subsequent callbacks match. Only relevant if you do hot upgrades (`08`/`12`); for restart-based deploys, a clean restart re-runs `init` instead.

**See also**: BEH-08, `08-supervision-and-applications.md`

---

## BEH-12: Use `gen_statem` for State Machines — `gen_fsm` Is Gone

**Strength**: SHOULD

**Summary**: Implement event-driven state machines with `gen_statem`; `gen_fsm` was deprecated and removed, so don't start new work on it.

```erlang
%% Bad - gen_fsm is deprecated/removed; don't base new state machines on it
-behaviour(gen_fsm).

%% Good - use gen_statem; pick a callback mode and write state callbacks
-behaviour(gen_statem).
callback_mode() -> state_functions.
locked(cast, {button, Code}, Data) -> %% ...
    {next_state, locked, Data}.
```

**Rationale**: `gen_statem` superseded `gen_fsm`, adding event postponing, inserted events, state-enter calls, and richer timeouts, modelling `State × Event -> Actions, State'` (OTP Design Principles). `gen_fsm` is no longer available in current OTP. New FSMs use `gen_statem`; legacy `gen_fsm` modules should be migrated.

**See also**: BEH-13, BEH-14

---

## BEH-13: Choose the `gen_statem` Callback Mode Deliberately

**Strength**: CONSIDER

**Summary**: `state_functions` (one callback per state, states must be atoms) suits distinct-per-state handling; `handle_event_function` (one callback) suits complex state terms or mostly-shared handling.

```erlang
%% Bad - use handle_event_function, then reinvent per-state dispatch with a giant case on State
handle_event(cast, Event, State, Data) ->
    case State of locked -> %% ...
                ; open   -> %% ...
    end.

%% Good - state_functions gives you per-state dispatch directly (one function per state)
callback_mode() -> state_functions.
locked(cast, {button, C}, Data) -> %% ...
    ;
open(cast, _Event, Data) -> %% ...
    .
%% reserve handle_event_function for non-atom states or handling shared across all states
```

**Rationale**: The callback mode is set by the mandatory `callback_mode/0` and decides dispatch (OTP Design Principles). `state_functions` reads naturally when each state has its own logic and the state is an atom; `handle_event_function` is the right tool when states carry data (any term) or most events are handled the same way regardless of state. Picking by habit leads to either a `case`-on-state sprawl or awkward atom-only states.

**See also**: BEH-12, BEH-15

---

## BEH-14: Use `gen_statem` Timeouts, Not Hand-Rolled Timers

**Strength**: SHOULD

**Summary**: Express inactivity and deadline logic with state/event/generic timeouts; the behaviour cancels a state timeout automatically on state change.

```erlang
%% Bad - manual timer you must track and cancel across every transition
locked(cast, _Tick, Data) ->
    erlang:send_after(30000, self(), too_long),    %% leaks if you forget to cancel on transition
    {next_state, locked, Data}.

%% Good - a state timeout is auto-cancelled when the state changes
locked(cast, _Tick, Data) ->
    {next_state, locked, Data, [{state_timeout, 30000, locked_too_long}]};
locked(state_timeout, locked_too_long, Data) ->
    {next_state, alarm, Data}.
```

**Rationale**: `gen_statem` offers state timeouts (cancelled on any state change), event timeouts (cancelled by any event), and generic named timeouts (OTP Design Principles). Hand-rolled `send_after` timers force you to store and cancel timer references on every transition — a classic source of stale-timer bugs. Let the behaviour manage timer lifecycles.

**See also**: BEH-12, BEH-15

---

## BEH-15: Co-locate Entry Actions with `state_enter`; Use `postpone` Instead of Buffering

**Strength**: CONSIDER

**Summary**: Enable `state_enter` to put per-state entry actions in one place, and `postpone` events that can't be handled yet rather than stashing them by hand.

```erlang
%% Bad - duplicate the same entry side-effect at every transition into 'open'
locked(cast, {button, ok}, Data) -> unlock_door(), {next_state, open, Data};
timer(cast, reopen,        Data) -> unlock_door(), {next_state, open, Data}.

%% Good - enable state_enter and write the entry action once
callback_mode() -> [state_functions, state_enter].
open(enter, _OldState, _Data) -> unlock_door(), keep_state_and_data;
open(cast, _Event, Data) -> %% ...
    keep_state_and_data.
```

**Rationale**: With `state_enter` in `callback_mode/0`, `gen_statem` calls the state callback with `(enter, OldState, ...)` on every state change, so entry actions live beside the state's other rules instead of being copied across transitions (OTP Design Principles). Likewise, returning `postpone` re-queues an event for after the next state change — cleaner and less error-prone than maintaining your own pending-event list.

**See also**: BEH-13, BEH-14

---

## BEH-16: Use `gen_event` for Swappable Handlers — and Mind Its Caveats

**Strength**: CONSIDER

**Summary**: Use a `gen_event` manager for event/notification streams with installable, swappable handlers; remember that a plain handler that crashes is silently removed.

```erlang
%% Bad - bespoke pub/sub loop: no supervision, no handler swap, a crashing subscriber is just lost
notify(Subs, Event) -> [Pid ! Event || Pid <- Subs].

%% Good - a gen_event manager with installable handlers
{ok, _Mgr} = gen_event:start_link({local, log_man}),
gen_event:add_handler(log_man, file_logger, _Args = []),
gen_event:notify(log_man, {log, Event}).
%% caveat: a plain handler that crashes is removed silently; use add_sup_handler to be told,
%% or wrap with a supervised handler pattern, when you need to know it died.
```

**Rationale**: `gen_event` provides an event manager that fans events out to a list of handler modules you can add, delete, and swap at runtime (OTP Design Principles). Its sharp edge: a handler that crashes is simply removed and the manager keeps running, so failures can vanish silently — use `add_sup_handler/3` (which sends you a message on removal) or a supervised-handler pattern when a lost handler matters.

**See also**: BEH-01, `09-fault-tolerance.md`

---

## BEH-17: Define Custom Behaviours with `-callback` Attributes

**Strength**: SHOULD

**Summary**: When you create your own behaviour, declare its required callbacks with `-callback` attributes (with specs), not the deprecated `behaviour_info/1`.

```erlang
%% Bad - the deprecated behaviour_info/1 mechanism: name/arity only, no type information
behaviour_info(callbacks) -> [{handle, 2}, {format, 1}];
behaviour_info(_) -> undefined.

%% Good - -callback attributes carry full specs and let the compiler check implementers
-callback handle(Event :: term(), State :: term()) -> {ok, NewState :: term()}.
-callback format(State :: term()) -> iodata().
```

**Rationale**: "Use `-callback` instead of `behaviour_info/1`" (Inaka). `-callback` declares each required callback with a complete type spec, which both documents the contract and lets the compiler (and Dialyzer) check that `-behaviour` modules implement it correctly. `behaviour_info/1` is the deprecated predecessor and carries only name/arity.

**See also**: BEH-02, `04-data-and-types.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| BEH-01 Use behaviours | SHOULD | Don't hand-roll the server loop |
| BEH-02 Declare `-behaviour` | SHOULD | Compiler checks the callback contract |
| BEH-03 Encapsulate call/cast | SHOULD | Wrap each in an API fn beside its callback |
| BEH-04 call vs cast | SHOULD | call = reply + back-pressure; cast = fire-and-forget |
| BEH-05 Fast callbacks | MUST | Never block `handle_call`; reply async |
| BEH-06 No call cycles | CONSIDER | Synchronous cycles deadlock; the timeout isn't a design |
| BEH-07 Handle `handle_info` | SHOULD | Tolerate unexpected messages; don't crash on noise |
| BEH-08 Named state record | SHOULD | `#state{}` over a positional tuple |
| BEH-09 Light `init` | SHOULD | `start_link` is synchronous; defer heavy work |
| BEH-10 `terminate` best-effort | SHOULD | Persist as you go; terminate may not run |
| BEH-11 `code_change` | CONSIDER | Migrate state shape on hot upgrade |
| BEH-12 `gen_statem` not `gen_fsm` | SHOULD | `gen_fsm` is removed |
| BEH-13 Callback mode | CONSIDER | `state_functions` vs `handle_event_function` |
| BEH-14 Statem timeouts | SHOULD | Built-in timeouts beat manual timers |
| BEH-15 `state_enter`/`postpone` | CONSIDER | Co-locate entry actions; re-queue events |
| BEH-16 `gen_event` | CONSIDER | Swappable handlers; crashes vanish silently |
| BEH-17 `-callback` attributes | SHOULD | Define custom behaviours with specs |

## Related Guidelines

- **Supervision & applications**: See `08-supervision-and-applications.md` — behaviours are started as supervised children; `start_link`, child specs, and shutdown tie directly to BEH-09/BEH-10.
- **Fault tolerance**: See `09-fault-tolerance.md` — BEH-05/BEH-09 are the behaviour-level forms of let-it-crash and init-as-guarantee.
- **Processes & concurrency**: See `06-processes-and-concurrency.md` for the message-passing and link/monitor primitives behaviours wrap.
- **Data & types**: See `04-data-and-types.md` for the `#state{}` record discipline (BEH-08) and `-callback`/`-spec` typing (BEH-17).
- **Production ops**: See `14-production-ops.md` for `sys`-module introspection and tracing of running behaviours.

## External References

- [OTP Design Principles — gen_server Behaviour](https://www.erlang.org/doc/system/gen_server_concepts.html)
- [OTP Design Principles — gen_statem Behaviour](https://www.erlang.org/doc/system/statem.html)
- [OTP Design Principles — gen_event Behaviour](https://www.erlang.org/doc/system/events.html)
- Erlang Programming Rules and Conventions — §5.6 (use generic server functions)
- Inaka Erlang Guidelines — OTP (encapsulate OTP APIs, use `-callback` attributes, use behaviours)
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — gen_server deadlocks (pp. 94–95)
- *Programming Erlang* (Joe Armstrong) — gen_server, behaviours
