# Anti-Patterns

The cheap safety net: the concrete traps that recur in Erlang code, each with the fix. This chapter is a hybrid — standalone entries (`AP-NN`) for the cross-cutting, security/correctness traps that don't belong to one chapter, plus an **AI-misuse** section for the mistakes LLM-generated Erlang specifically tends to make, plus a Summary Table that indexes both these entries and the traps covered fully in their home chapters. **Load this chapter first on any Erlang task.**

Every entry's strength is **AVOID** — the entry's title is the thing not to do. A few are flagged **(security)** or **(correctness)**: those are the bright lines, equivalent to a MUST-NOT.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Synthesized across all sources (the `%% Bad` halves and "Common Errors" of every chapter) plus an AI-audit corpus.

---

## AP-01: `binary_to_term/1` on Untrusted Data

**Strength**: AVOID

**Summary**: **(security)** Decoding an externally-sourced binary without `[safe]` lets it mint atoms and unsafe terms — a DoS and decoding-safety hole.

```erlang
%% Bad - untrusted input can create arbitrary atoms (table exhaustion) and unsafe terms
Term = binary_to_term(PacketFromNetwork).

%% Good - [safe] refuses to create new atoms or unsafe constructs (raises badarg instead)
Term = binary_to_term(PacketFromNetwork, [safe]).
```

**Rationale**: `binary_to_term/1` reconstructs whatever terms are encoded in the input; on hostile data that exhausts the bounded, never-collected atom table and decodes unsafe constructs. Treat every externally-sourced binary as hostile. See EH-15, DT-13.

**See also**: AP-02, `03-error-handling.md` (EH-15)

---

## AP-02: Building Atoms from Untrusted or Unbounded Input

**Strength**: AVOID

**Summary**: **(security)** `list_to_atom`/`binary_to_atom` on user-influenced data fills the bounded, uncollected atom table and crashes the node.

```erlang
%% Bad - a new atom per request value; the atom table fills and the node dies (DoS)
route(Name) -> handler(list_to_atom(Name)).

%% Good - only resolve atoms that already exist; keep dynamic keys as binaries
route(Name) -> handler(binary_to_existing_atom(Name, utf8)).
```

**Rationale**: Atoms are interned and never garbage-collected, with a hard table limit (~1M default). Minting them from unbounded input is a classic denial-of-service. Use `*_to_existing_atom`, or keep dynamic keys as binaries/tuples. See DT-13, PF-14.

**See also**: AP-01, `04-data-and-types.md` (DT-13)

---

## AP-03: Exposing Erlang Distribution to an Untrusted Network

**Strength**: AVOID

**Summary**: **(security)** A connected node can execute arbitrary code on its peers; the cookie is a weak secret, not access control.

```erlang
%% Bad - a publicly reachable node + guessable cookie = remote code execution for anyone
%% erl -name n@public-ip -setcookie monster   (epmd/dist ports open to the internet)

%% Good - distribution only on a private network, TLS-encrypted, ports firewalled
%% vm.args: -proto_dist inet_tls -ssl_dist_optfile /etc/dist_ssl.conf   (strong secret cookie)
```

**Rationale**: Any node that completes the distribution handshake can `spawn`/`rpc` arbitrary code on its peers, and the cookie is a plaintext shared atom. Keep distribution on a trusted network, encrypt with `inet_tls`, and firewall epmd plus the dist ports. See DIST-05.

**See also**: `16-distribution.md` (DIST-05)

---

## AP-04: Unbounded Mailbox Growth

**Strength**: AVOID

**Summary**: **(correctness)** Accepting work faster than you process it (no back-pressure, no catch-all) grows a mailbox until the node runs out of memory.

```erlang
%% Bad - async intake with no limit and no catch-all: the mailbox grows without bound
handle_cast({job, J}, S) -> {noreply, enqueue(J, S)}.

%% Good - synchronous (back-pressured) intake with a bound; shed load when full
handle_call({job, J}, _From, S) ->
    case full(S) of
        true  -> {reply, {error, overloaded}, S};
        false -> {reply, ok, enqueue(J, S)}
    end.
```

**Rationale**: Erlang's async messaging makes it easy to outpace a consumer, turning a load spike into unbounded memory growth — the most common production OOM (OPS-07). Use `call` for natural back-pressure, bound queues, and drain unmatched messages (PC-08). See BEH-04, PF-18.

**See also**: AP-05, `06-processes-and-concurrency.md` (PC-08), `10-performance.md` (PF-18)

---

## AP-05: Blocking a `gen_server` Callback

**Strength**: AVOID

**Summary**: **(correctness)** A `gen_server` handles one message at a time; slow work inside a callback serialises every client and triggers `call` timeouts.

```erlang
%% Bad - slow synchronous work in handle_call blocks every other caller
handle_call({fetch, Url}, _From, S) -> {reply, slow_http_get(Url), S}.

%% Good - offload and reply asynchronously; keep the server responsive
handle_call({fetch, Url}, From, S) ->
    spawn(fun() -> gen_server:reply(From, slow_http_get(Url)) end),
    {noreply, S}.
```

**Rationale**: The behaviour loop is single-threaded over the mailbox, so a blocking callback stalls the whole server and cascades into 5-second `call` timeouts. Return `{noreply, _}` and answer with `gen_server:reply/2`, or use a worker pool. See BEH-05.

**See also**: AP-04, AP-12, `07-otp-behaviours.md` (BEH-05)

---

## AP-06: Swallowing Exceptions with `catch _:_`

**Strength**: AVOID

**Summary**: A blanket catch turns every bug (a `badmatch`, a typo) into a silent fallback, hiding faults and defeating supervision.

```erlang
%% Bad - blanket catch hides real bugs along with the error you meant to handle
try connect(Host) catch _:_ -> retry end.

%% Good - catch only the specific class/reason you expect; let everything else crash
try connect(Host) of
    {ok, C} -> {ok, C}
catch error:econnrefused -> retry
end.
```

**Rationale**: `catch _:_` is defensive programming in disguise — it converts unexpected bugs into a "handled" path with corrupt state. Match the exact class and reason; let unanticipated errors crash so a supervisor restarts a clean state. See EH-07, EH-13.

**See also**: AP-07, `03-error-handling.md` (EH-07)

---

## AP-07: Programming Defensively Instead of Letting It Crash

**Strength**: AVOID

**Summary**: Validating already-checked data everywhere and patching over failures produces brittle code that hides bugs far from their cause.

```erlang
%% Bad - re-validate and "handle" everywhere; bad input silently becomes a default
parse(Bin) -> try binary_to_integer(Bin) of N -> N catch _:_ -> 0 end.

%% Good - validate once at the boundary, then trust; let unexpected input crash
parse(Bin) -> binary_to_integer(Bin).   %% a bad value crashes this supervised process
```

**Rationale**: "In general one should not test input data to functions for correctness" (Programming Rules §3.13). Defensive code masks the real failure and surfaces it far from the cause; validate once at the border (EH-10) and let the supervised process crash on the unexpected. See FT-01, EH-04.

**See also**: AP-06, `09-fault-tolerance.md` (FT-01)

---

## AP-08: Non-Tail-Recursive Server Loop

**Strength**: AVOID

**Summary**: **(correctness)** A long-lived loop whose recursive call isn't in tail position leaks a stack frame per iteration until the node dies.

```erlang
%% Bad - loop call used in a cons -> not a tail call -> a frame kept per message, forever
loop(S) ->
    receive {req, From} -> From ! reply(S), [done | loop(S)] end.

%% Good - the recursive loop call is the last action in the clause
loop(S) ->
    receive {req, From} -> From ! reply(S), loop(S) end.
```

**Rationale**: "All servers must be tail-recursive, otherwise the server will consume memory until the system runs out" (Programming Rules §5.9). A server runs effectively forever, so a single non-tail call per iteration is an unbounded leak. (A behaviour avoids this for you.) See PC-06.

**See also**: `06-processes-and-concurrency.md` (PC-06)

---

## AP-09: `++` with a Growing Accumulator on the Left

**Strength**: AVOID

**Summary**: `++` copies its left operand, so growing the accumulator on the left inside a loop is `O(n²)`.

```erlang
%% Bad - accumulator on the LEFT of ++ : copied every iteration -> O(n^2)
build([], Acc)      -> Acc;
build([H | T], Acc) -> build(T, Acc ++ [f(H)]).

%% Good - prepend (O(1)) and reverse once at the end
build(L) -> lists:reverse(build(L, [])).
build([], Acc)      -> Acc;
build([H | T], Acc) -> build(T, [f(H) | Acc]).
```

**Rationale**: `++` copies all cons cells of its left side; a left-side accumulator is re-copied every iteration. Prepend and `lists:reverse/1` once, or build binaries accumulator-first (PF-05). See PF-04, FP-09.

**See also**: AP-21, `10-performance.md` (PF-04)

---

## AP-10: Refc-Binary Leak

**Strength**: AVOID

**Summary**: Retaining a small slice of a large binary keeps the whole off-heap binary alive — a quiet memory leak.

```erlang
%% Bad - a 10-byte sub-binary pins the entire large refc binary in memory
keep(Big) -> binary:part(Big, 0, 10).

%% Good - copy the small slice so the large binary can be reclaimed
keep(Big) -> binary:copy(binary:part(Big, 0, 10)).
```

**Rationale**: Binaries over 64 bytes are reference-counted and off-heap; a sub-binary references the whole parent, so keeping a tiny piece can pin megabytes. Diagnose with `recon:bin_leak/1` (OPS-08), fix with `binary:copy/1`. See PF-07.

**See also**: `10-performance.md` (PF-07), `14-production-ops.md` (OPS-08)

---

## AP-11: Full ETS Table Scans (`tab2list` + Filter)

**Strength**: AVOID

**Summary**: Copying an entire ETS table to the caller and filtering in Erlang throws away the point of a fast keyed store.

```erlang
%% Bad - copy the whole table out, then scan it in Erlang
[Row || Row <- ets:tab2list(t), element(2, Row) =:= active].

%% Good - keyed lookup, or a match spec that filters inside ETS
ets:lookup(t, Key),
ets:select(t, [{{'_', active, '$1'}, [], ['$1']}]).
```

**Rationale**: `tab2list/1` copies the table to the calling process (`O(n)`) and then you scan it (`O(n)`). `select`/`match` evaluate inside ETS and return only matches. Design the key for the queries you run. See PF-11.

**See also**: `10-performance.md` (PF-11)

---

## AP-12: Synchronous `gen_server` Call Cycles

**Strength**: AVOID

**Summary**: **(correctness)** Two servers that synchronously call each other in a cycle deadlock until the `call` timeout fires.

```erlang
%% Bad - A calls B which (transitively) calls back into A: both block until timeout
handle_call(work, _From, S) -> {reply, gen_server:call(server_b, sub), S}.

%% Good - break the cycle: reply asynchronously, or only call "older" processes synchronously
handle_call(work, From, S) -> gen_server:cast(server_b, {sub, From}), {noreply, S}.
```

**Rationale**: A synchronous call cycle blocks every participant; OTP only breaks it via the 5-second timeout (then a crash). The timeout is a safety net, not a design — avoid the cycle by deferring the reply or ordering calls. See BEH-06.

**See also**: AP-05, `07-otp-behaviours.md` (BEH-06)

---

## AP-13: Guaranteeing a Remote Dependency in `init`

**Strength**: AVOID

**Summary**: Connecting to a remote service in a supervised `init` turns every transient outage into a boot crash-loop.

```erlang
%% Bad - a remote connection in init; a netsplit crashes the whole supervised startup
init(_) -> {ok, Conn} = db:connect("remote-host"), {ok, #state{conn = Conn}}.

%% Good - guarantee only what's dependable; connect after init and degrade until ready
init(_) -> self() ! connect, {ok, #state{conn = undefined}}.
```

**Rationale**: "Supervised processes provide guarantees in their initialization phase, not a best effort" (Erlang in Anger). A remote dependency's failure is *expected*, so guaranteeing it in `init` makes a transient blip a crash-loop. Connect asynchronously; return `{error, not_connected}` until ready. See FT-12, BEH-09.

**See also**: `09-fault-tolerance.md` (FT-12)

---

## AP-14: Toggling `trap_exit`

**Strength**: AVOID

**Summary**: Switching `trap_exit` on and off at runtime makes a process's exit semantics unpredictable.

```erlang
%% Bad - toggle trapping around a risky call: exit handling becomes inconsistent
risky(F) -> process_flag(trap_exit, true), R = F(), process_flag(trap_exit, false), R.

%% Good - decide once at startup (system processes trap; workers don't)
init(Args) -> process_flag(trap_exit, true), {ok, init_state(Args)}.
```

**Rationale**: "It is usually very bad practice for a process to 'toggle' trapping exits" (Programming Rules §5.12) — toggling creates windows where an exit signal is handled inconsistently. Set the flag once and leave it; keep the set of trapping processes small. See FT-10.

**See also**: `09-fault-tolerance.md` (FT-10)

---

## AP-15: In-Band Sentinels and Stringly-Typed Errors

**Strength**: AVOID

**Summary**: Returning bare values (with `undefined`/`false` for failure) or formatted error strings makes outcomes ambiguous and unmatchable.

```erlang
%% Bad - in-band sentinel and a human-formatted error string
lookup(K, M) -> maps:get(K, M, undefined).
{error, lists:flatten(io_lib:format("user ~p not found", [Id]))}.

%% Good - tagged returns and structured reason terms
-spec lookup(term(), map()) -> {ok, term()} | error.
lookup(K, M) -> case maps:find(K, M) of {ok, V} -> {ok, V}; error -> error end.
{error, {user_not_found, Id}}.
```

**Rationale**: An in-band `undefined` collides with real data; a formatted string forces brittle substring matching. Tag success/failure (EH-01) and make reasons structured, matchable terms (EH-12); format for humans only at the edge. See DT-01.

**See also**: `03-error-handling.md` (EH-01, EH-12)

---

## AI-Misuse Traps

LLM-generated Erlang carries habits from the imperative, mutable, exception-oriented languages that dominate training data. These are the tells to scan for in generated (or generated-then-edited) code; each has a deeper treatment in its home chapter, but they cluster here because they appear *together* and are worth a dedicated pass.

---

## AP-16: Over-Defensive `try`/`catch` Everywhere

**Strength**: AVOID

**Summary**: Wrapping every operation in `try`/`catch` "to be safe" — the single most common LLM Erlang tell — fights the let-it-crash model.

```erlang
%% Bad - defensive try around code that should just run (and crash on a real bug)
handle(Req) ->
    try
        case validate(Req) of ok -> process(Req); _ -> {error, invalid} end
    catch _:_ -> {error, internal} end.

%% Good - program the normal case; let failures crash and be supervised
handle(Req) -> ok = validate(Req), process(Req).
```

**Rationale**: Models trained on exception-heavy languages reach for `try`/`catch` reflexively; in Erlang this masks bugs and bypasses supervision (AP-06/AP-07). Reserve `try` for genuinely expected, specific failures and the user boundary (EH-04, FT-04).

**See also**: AP-06, AP-07, `03-error-handling.md` (EH-04)

---

## AP-17: Reaching for `if`

**Strength**: AVOID

**Summary**: Using `if` (an imperative habit) where Erlang wants guarded clauses or `case`.

```erlang
%% Bad - if with a true-> catch-all, ported from another language
classify(N) -> if N > 0 -> positive; N < 0 -> negative; true -> zero end.

%% Good - guarded function clauses
classify(N) when N > 0 -> positive;
classify(N) when N < 0 -> negative;
classify(_)            -> zero.
```

**Rationale**: Erlang's `if` only takes guards, needs a `true ->` catch-all, and reads unlike imperative `if`; LLMs use it by reflex. Guarded clauses or `case` are the idiomatic, declarative choice. See FP-03.

**See also**: AP-22, `05-functions-and-pattern-matching.md` (FP-03)

---

## AP-18: Hand-Rolling a Server Loop Instead of Using a Behaviour

**Strength**: AVOID

**Summary**: Writing a bespoke `spawn`/`receive` loop for stateful work that a `gen_server` should handle.

```erlang
%% Bad - a hand-rolled stateful loop: no sys/debug, no code change, ad-hoc protocol
start() -> spawn(fun() -> loop(#{}) end).
loop(S) -> receive {From, {get, K}} -> From ! maps:get(K, S, undefined), loop(S) end.

%% Good - a gen_server: call/cast, introspection, code_change, supervision for free
-behaviour(gen_server).
start_link() -> gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).
handle_call({get, K}, _From, S) -> {reply, maps:get(K, S, undefined), S}.
```

**Rationale**: LLMs often reconstruct an actor loop from first principles instead of using OTP. The behaviour supplies tagged request/reply, tail-recursion, timeouts, `sys` debugging, and supervision integration. See BEH-01, PC-16.

**See also**: AP-08, `07-otp-behaviours.md` (BEH-01)

---

## AP-19: Imperative Indexed Iteration

**Strength**: AVOID

**Summary**: Walking a list by index (`lists:nth/2` in a counted loop) instead of recursion, a comprehension, or a higher-order function.

```erlang
%% Bad - index into the list each step: O(n) per access -> O(n^2), and un-Erlang
sum(L) -> sum(L, 1, length(L), 0).
sum(_, I, N, Acc) when I > N -> Acc;
sum(L, I, N, Acc) -> sum(L, I + 1, N, Acc + lists:nth(I, L)).

%% Good - recurse over the structure, or use a fold/comprehension
sum(L) -> lists:foldl(fun(X, Acc) -> Acc + X end, 0, L).
```

**Rationale**: Index-based iteration is an array habit; lists are linked, so `lists:nth/2` is `O(n)` and the loop becomes `O(n²)`. Pattern-match the head/tail, fold, or comprehend. See FP-06, PF-09.

**See also**: AP-09, `05-functions-and-pattern-matching.md` (FP-06)

---

## AP-20: Expecting Mutable Variables

**Strength**: AVOID

**Summary**: Writing code that assumes a variable can be reassigned (`X = X + 1`), or accumulating via rebinding.

```erlang
%% Bad - expect reassignment; this is a badmatch, not an update
count(L) -> N = 0, lists:foreach(fun(_) -> N = N + 1 end, L), N.

%% Good - bindings are immutable; thread state through recursion / a fold
count(L) -> lists:foldl(fun(_, N) -> N + 1 end, 0, L).
```

**Rationale**: `=` is pattern match, not assignment; `X = X + 1` fails on a bound `X`. LLMs from imperative languages write reassignment and mutable accumulators. Use a new name, a fold, or recursion to carry state. See ID-06.

**See also**: AP-19, `01-core-idioms.md` (ID-06)

---

## AP-21: Char-List Strings and `++` as the Default for Text

**Strength**: AVOID

**Summary**: Treating `"..."` char lists and `++` concatenation as the default text type and operation, instead of binaries and iolists.

```erlang
%% Bad - char-list strings concatenated with ++ (copies, converts, scales badly)
Msg = "Hello " ++ binary_to_list(Name) ++ "! Welcome.".

%% Good - binaries for text, iolists for assembly (no copying; IO accepts them directly)
Msg = ["Hello ", Name, "! Welcome."].
```

**Rationale**: Other languages make strings the obvious text type; in Erlang, sizeable text should be binaries, and output should be assembled as iolists (no `++` copying). LLMs default to char lists and `++`. See DT-10, DT-11, PF-04.

**See also**: AP-09, `04-data-and-types.md` (DT-10, DT-11)

---

## AP-22: Nested `case` Staircases for `{ok, _}` Threading

**Strength**: AVOID

**Summary**: Building a pyramid of nested `case`s to thread `{ok, _}`/`{error, _}` results, instead of clauses or `maybe`.

```erlang
%% Bad - a nested-case staircase
load(F) ->
    case read(F) of
        {ok, B} -> case parse(B) of {ok, T} -> validate(T); E -> E end;
        E -> E
    end.

%% Good - the maybe expression (OTP 25+) short-circuits on the first non-match
load(F) ->
    maybe
        {ok, B} ?= read(F),
        {ok, T} ?= parse(B),
        validate(T)
    end.
```

**Rationale**: LLMs reproduce the nested-conditional shape from imperative code. Erlang flattens it with `maybe`, helper-function clauses, or (where exceptions are appropriate) a single boundary `try`. See FP-15, EH-04.

**See also**: AP-17, `05-functions-and-pattern-matching.md` (FP-15)

---

## AP-23: Using Macros for Code (Preprocessor Habit)

**Strength**: AVOID

**Summary**: Reaching for `-define` macros to abstract behaviour, instead of functions; macros are opaque to tools and produce no stack frame.

```erlang
%% Bad - a code macro (C/preprocessor habit): invisible to dialyzer/xref, no stack frame
-define(LOG_ERR(E), logger:error("~p", [E])).
f(R) -> ?LOG_ERR(R).

%% Good - a real function for behaviour; reserve macros for literal constants and ?MODULE/?LINE
-define(DEFAULT_TIMEOUT, 5000).
log_err(R) -> logger:error("~p", [R]).
```

**Rationale**: Models port C-style macro usage into Erlang. A code macro can't be analysed by Dialyzer/xref, can't be traced, and has no stack frame; a function does the same job as a first-class, analysable value. Reserve macros for literal constants. See ID-14.

**See also**: `01-core-idioms.md` (ID-14)

---

## Summary Table

Anti-patterns covered as full entries above, plus traps covered fully in their home chapters. Scan this list on any review; the **See** column is where the affirmative pattern lives.

| Anti-Pattern | Do Instead | See |
|--------------|-----------|-----|
| `binary_to_term/1` on untrusted data | `binary_to_term(_, [safe])` | AP-01 / EH-15 |
| Atoms from untrusted/unbounded input | `*_to_existing_atom`; binaries | AP-02 / DT-13 |
| Distribution on an untrusted network | private net + TLS + firewall | AP-03 / DIST-05 |
| Unbounded mailbox | back-pressure / bounded queue | AP-04 / PF-18 |
| Blocking a `gen_server` callback | reply async (`gen_server:reply`) | AP-05 / BEH-05 |
| `catch _:_` swallowing | match specific class/reason | AP-06 / EH-07 |
| Defensive programming | validate at the border; let it crash | AP-07 / FT-01 |
| Non-tail-recursive loop | recursive call in tail position | AP-08 / PC-06 |
| `++` accumulator on the left | prepend + `lists:reverse/1` | AP-09 / PF-04 |
| Refc-binary leak | `binary:copy/1` small slices | AP-10 / PF-07 |
| Full ETS scans (`tab2list`) | keyed lookup / match spec | AP-11 / PF-11 |
| Synchronous call cycles | defer reply; order calls | AP-12 / BEH-06 |
| Remote dependency in `init` | connect after init; degrade | AP-13 / FT-12 |
| Toggling `trap_exit` | set once at startup | AP-14 / FT-10 |
| In-band/stringly-typed errors | tagged returns; structured reasons | AP-15 / EH-01 |
| Over-defensive `try`/`catch` (AI) | program the normal case | AP-16 / EH-04 |
| Reaching for `if` (AI) | guarded clauses / `case` | AP-17 / FP-03 |
| Hand-rolled server loop (AI) | `gen_server` | AP-18 / BEH-01 |
| Indexed iteration (AI) | recursion / fold / comprehension | AP-19 / FP-06 |
| Expecting mutable variables (AI) | new name; fold; recursion | AP-20 / ID-06 |
| Char-list strings + `++` (AI) | binaries + iolists | AP-21 / DT-10 |
| Nested `case` staircase (AI) | `maybe` / clauses | AP-22 / FP-15 |
| Macros for code (AI) | functions | AP-23 / ID-14 |
| `length/1` in a hot loop | pattern-match the shape | PF-09 |
| Dynamic calls (`M:F` from a var) | static, qualified calls | ID-13 |
| `-import` / `-compile(export_all)` | module-qualify; explicit `-export` | ID-12 / API-02 |
| God modules | one responsibility per module | API-11 |
| `io:format` debugging in prod | `logger` + tracing | OPS-01 |
| Treating "node down" as "node dead" | reconcile; design for partitions | DIST-03 |
| Non-idempotent retries | unique request id; dedupe | FT-14 / DIST-11 |
| Long/blocking NIF | keep short or dirty-schedule | PF-16 |
| Process dictionary for state | thread state through the loop | PC-12 |

## Related Guidelines

- **Error handling**: See `03-error-handling.md` — AP-06/AP-07/AP-15/AP-16 are the negatives of EH-01/EH-04/EH-07/EH-12.
- **Fault tolerance**: See `09-fault-tolerance.md` — let-it-crash (FT-01), init guarantees (FT-12), trap-exit discipline (FT-10).
- **Performance**: See `10-performance.md` — `++` (PF-04), refc leaks (PF-07), ETS scans (PF-11), NIFs (PF-16).
- **OTP behaviours / processes**: See `07-otp-behaviours.md` and `06-processes-and-concurrency.md` — blocking callbacks (BEH-05), call cycles (BEH-06), mailbox/loops (PC-06/PC-08).
- **Data & types / core idioms**: See `04-data-and-types.md` (DT-13, DT-10) and `01-core-idioms.md` (ID-06, ID-13, ID-14) for the AI-misuse fixes.

## External References

- Erlang Programming Rules and Conventions — §3.13 (don't program defensively), §5.9 (tail-recursive servers), §5.12 (trapping exits)
- [Erlang Efficiency Guide](https://www.erlang.org/doc/system/efficiency_guide.html) — `++`, binaries, ETS
- *Erlang in Anger* (Fred Hébert) — mailbox overload, refc-binary leaks, init guarantees
- [Erlang Reference Manual — `binary_to_term/2`](https://www.erlang.org/doc/man/erlang.html#binary_to_term-2) (`safe` option)
- Inaka Erlang Guidelines — defensive programming, macros, dynamic calls
