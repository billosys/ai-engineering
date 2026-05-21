# Error Handling

How Erlang represents and routes failure: the three exception classes (`error`/`exit`/`throw`), tagged `{error, Reason}` return values versus exceptions, `try`/`catch`/`after` discipline, validating at the borders, structured logging, and the line between an *expected failure* (a value) and a *bug* (a crash). The recovery side — supervision and let-it-crash design — lives in `09-fault-tolerance.md`.

Target environment: **Erlang/OTP 27+** (logging via the `logger` API; `error_logger` is legacy). Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the Erlang Programming Rules (§4.1, §6.3, §6.4), Programming Erlang (Error Handling), the Erlang Reference Manual (Errors, Expressions/Try), Inaka guidelines, and Erlang and OTP in Action.

---

## EH-01: Signal Failure with Tagged Return Values

**Strength**: SHOULD

**Summary**: Return `{ok, V}` / `{error, Reason}` (or `{value, V}` / `false`) so a successful result can never be confused with a "missing" or error sentinel.

```erlang
%% Bad - bare value on success, sentinel on failure: a real 'undefined'/'false' is ambiguous
find(K, L) -> proplists:get_value(K, L).   %% undefined = "missing" OR a genuine undefined value

%% Good - tag both outcomes so success and failure are always distinguishable
-spec find(term(), list()) -> {ok, term()} | error.
find(K, L) ->
    case lists:keyfind(K, 1, L) of
        {K, V} -> {ok, V};
        false  -> error
    end.
```

**Rationale**: "Use tagged return values" (Programming Rules §6.3): if a function returns a bare value on success and `false` on failure, a stored `false` is indistinguishable from "not found." Tagging makes the two cases disjoint and lets callers pattern-match the outcome — the foundation of the whole `{ok,_}`/`{error,_}` idiom.

**See also**: EH-03, EH-12, `04-data-and-types.md`

---

## EH-02: Know the Three Exception Classes — `error`, `exit`, `throw`

**Strength**: SHOULD

**Summary**: Raise the class that matches intent: `error` for bugs/crashes, `exit` to terminate the process, `throw` for a documented exception a caller may catch.

```erlang
%% Bad - use the classes interchangeably, so callers can't read intent
do() -> throw(database_down).   %% recoverable? a crash? a process exit? unclear

%% Good - class signals intent
parse(B)  -> error({bad_input, B}).   %% a crash-level error / bug, not meant to be handled
stop()    -> exit(normal).            %% terminate this process
lookup(K) -> throw({not_found, K}).   %% documented, the caller may catch it
```

**Rationale**: `error(Why)` denotes crashing errors not expected to be handled (and is the class of all runtime errors); `exit(Why)` terminates the process and, if uncaught, sends `{'EXIT', Pid, Why}` to linked processes; `throw(Why)` is a catchable exception the function should *document* (Programming Erlang). The class is the first thing a `catch` clause matches, so using it consistently makes failure self-describing.

**See also**: EH-06, `09-fault-tolerance.md`

---

## EH-03: Expected Failures Are Values; Exceptions Are for the Exceptional

**Strength**: SHOULD

**Summary**: Return a value for outcomes the caller routinely expects; raise an exception only for genuinely abnormal situations.

```erlang
%% Bad - raise on an ordinary, expected outcome; every caller must wrap the call in try
get(K, M) -> case maps:find(K, M) of {ok, V} -> V; error -> throw(missing) end.

%% Good - expected "missing" is a value the caller can match directly
-spec get(term(), map()) -> {ok, term()} | {error, missing}.
get(K, M) ->
    case maps:find(K, M) of
        {ok, V} -> {ok, V};
        error   -> {error, missing}
    end.
```

**Rationale**: Exceptions are expensive to use as ordinary control flow — they force every caller into a `try` and obscure the normal path. A "not found" or "invalid input" that happens routinely is part of the function's contract and belongs in its return type, where Dialyzer and clause matching can see it.

**See also**: EH-01, EH-05, EH-09

---

## EH-04: Separate Error Handling from the Normal Path

**Strength**: SHOULD

**Summary**: Program the normal case cleanly; don't interleave it with defensive checks and `try` wrappers.

```erlang
%% Bad - the happy path is buried under defensive nesting and a blanket try
handle(Req) ->
    try
        case validate(Req) of
            ok -> case process(Req) of {ok, R} -> R; _ -> default end;
            _  -> default
        end
    catch _:_ -> default end.

%% Good - write the normal case; let failure crash and be handled elsewhere
handle(Req) ->
    ok      = validate(Req),    %% crashes loudly on bad input
    {ok, R} = process(Req),
    R.
```

**Rationale**: "Don't clutter code for the 'normal case' with code designed to handle exceptions… as far as possible only program the normal case" (Programming Rules §4.1). If the normal case fails, the process should report and crash, with recovery in a separate process. Clean separation of recovery from normal-case logic greatly simplifies the design.

**See also**: EH-05, EH-13, `09-fault-tolerance.md`

---

## EH-05: Crash on Bugs, Return on Expected Failures

**Strength**: SHOULD

**Summary**: Don't catch a programmer error to hand back a fallback; let bugs crash, and represent expected failures as values.

```erlang
%% Bad - swallow a bug (an unsupported shape) by returning a fallback value
area(Shape) ->
    try compute_area(Shape) catch _:_ -> 0 end.   %% an unknown shape is a BUG, hidden as 0

%% Good - expected outcomes are values; an unhandled shape crashes (a bug to fix), not silently 0
-spec area(shape()) -> {ok, number()} | {error, unsupported}.
area({circle, R}) -> {ok, 3.14159 * R * R};
area({square, S}) -> {ok, S * S};
area(_Other)      -> {error, unsupported}.
```

**Rationale**: Masking a bug with a default produces a system that limps along in a wrong state — the failure resurfaces later, far from its cause (this is the let-it-crash argument, FT-01/FT-03). Reserve crashing for programmer errors and represent the failures you genuinely anticipate as part of the return contract.

**See also**: EH-03, EH-04, `09-fault-tolerance.md` (FT-01)

---

## EH-06: Use `try` and Capture the Stacktrace; Avoid the Old `catch`

**Strength**: SHOULD

**Summary**: Prefer `try…catch` with an explicit `Class:Reason:Stack` over the standalone `catch` expression, which conflates classes and value and loses the stacktrace.

```erlang
%% Bad - the old catch conflates error/exit/value and drops the stacktrace
case catch risky() of
    {'EXIT', Reason} -> handle(Reason);   %% ambiguous if risky() legitimately returns {'EXIT', _}
    Value            -> Value
end.

%% Good - try...catch with explicit class and bound stacktrace
try risky() of
    Value -> Value
catch
    error:Reason:Stack -> handle(Reason, Stack)
end.
```

**Rationale**: The standalone `catch` returns either the value or `{'EXIT', Reason}`, so it can't distinguish a real `{'EXIT', _}` result from a failure and gives no class. `try…catch` matches the class explicitly and binds the stacktrace via the `Class:Pattern:Stacktrace` form (the third element must be a plain variable) — essential for diagnosis.

**See also**: EH-07, EH-08

---

## EH-07: Catch Specific Exceptions, Not `_:_`

**Strength**: SHOULD

**Summary**: Match the class and reason you actually expect; let everything else propagate.

```erlang
%% Bad - a blanket catch hides bugs (a badmatch, a typo) along with the error you meant to handle
try connect(Host) catch _:_ -> retry end.

%% Good - catch only the expected failure; unexpected errors crash and are seen
try connect(Host) of
    {ok, C} -> {ok, C}
catch
    error:econnrefused -> retry
end.
```

**Rationale**: `catch _:_` is the error-handling equivalent of defensive programming — it turns every bug in the protected expression into a silent `retry`/fallback. Catching the specific class and reason keeps the safety net tight, so genuine bugs still crash loudly and reach a supervisor.

**See also**: EH-05, EH-06, EH-13

---

## EH-08: Don't Nest `try…catch`

**Strength**: SHOULD

**Summary**: Use one `try` with multiple `catch` clauses, or delegate the inner risky work to a function that handles itself — never a `try` inside a `try`.

```erlang
%% Bad - a try nested inside a try
try a() of A ->
    try b(A) of B -> B catch _:E2 -> handle2(E2) end
catch _:E1 -> handle1(E1) end.

%% Good - one try, multiple catch clauses
try
    A = a(),
    b(A)
catch
    error:E1 -> handle1(E1);
    throw:E2 -> handle2(E2)
end.
```

**Rationale**: "Don't nest `try…catch` clauses" (Inaka) — nesting defeats their purpose, which is to isolate error handling from the normal path. A single `try` with several `catch` clauses handles multiple failure modes without re-introducing the nesting that EH-04 and ID-08 warn against.

**See also**: EH-04, `01-core-idioms.md` (ID-08)

---

## EH-09: Use `throw`/`catch` Sparingly, and Document Throws

**Strength**: CONSIDER

**Summary**: Reserve `throw`/`catch` for escaping deep, messy parsing of unreliable external input; document every exception a function may throw.

```erlang
%% Bad - throw used as ordinary internal control flow
find(K, T) -> throw({found, do_find(K, T)}).

%% Good - throw to escape deep parsing of untrusted input; documented and caught at the boundary
%% @doc Parse untrusted input. May throw {parse_error, Reason}.
parse(Bin) ->
    try tokens(Bin) of
        Toks -> {ok, build(Toks)}
    catch
        throw:{parse_error, _} = E -> {error, E}
    end.
```

**Rationale**: "Do not use catch and throw unless you know exactly what you are doing… use them as little as possible" (Programming Rules §6.4); the legitimate case is complicated, unreliable external input that can fail deep in the code (a compiler is the canonical example). When you do throw, document it so callers know to catch it.

**See also**: EH-03, EH-16

---

## EH-10: Validate at the Borders, Then Trust

**Strength**: SHOULD

**Summary**: Check untrusted data once, where it crosses into your code; don't re-validate it in every internal function.

```erlang
%% Bad - re-validate the same data at every layer
store(User)  when is_map(User) -> validate(User), insert(User).
insert(User) when is_map(User) -> validate(User), do_insert(User).   %% checked again

%% Good - validate once at the boundary; internal code assumes correctness
handle_request(Raw) ->
    User = decode_and_validate(Raw),   %% the single validation point
    store(User).
store(User) -> insert(User).           %% trusts User
```

**Rationale**: "Checking data as it passes from the untrusted world into the trusted inner sanctum… is a fundamental design principle" (Erlang and OTP in Action). Validate once at the border, then code for the correct case; the reduction in size and in masked errors is significant, and any remaining fault shows up as a logged process restart rather than corrupt state.

**See also**: EH-05, `04-data-and-types.md`, `09-fault-tolerance.md` (FT-02)

---

## EH-11: Use `after` for Cleanup That Must Always Run

**Strength**: SHOULD

**Summary**: Release resources in an `after` clause so they're freed whether or not the body raises.

```erlang
%% Bad - the resource leaks if the body raises before the close
F = open(File),
Data = parse(F),       %% if this throws, F is never closed
close(F),
Data.

%% Good - after runs on both the success and the exception path
F = open(File),
try parse(F)
after close(F)
end.
```

**Rationale**: The `after` section of a `try` is guaranteed to run regardless of whether an exception was raised (its return value is discarded). It is the right place for `close`, `unlock`, or `demonitor` cleanup that must happen on every path — the Erlang analogue of `finally`. Note for process-owned resources, links/monitors (chapter 06/09) often handle cleanup more robustly than `after`.

**See also**: EH-06, `06-processes-and-concurrency.md`

---

## EH-12: Make the Error Reason a Structured, Matchable Term

**Strength**: SHOULD

**Summary**: Return `{error, StructuredReason}` with atoms/tuples a caller can match — not a flattened human-readable string.

```erlang
%% Bad - stringly-typed error: callers must string-match it, machines can't dispatch on it
{error, lists:flatten(io_lib:format("user ~p not found", [Id]))}.

%% Good - a structured reason term; format it for humans only at the edge
{error, {user_not_found, Id}}.
```

**Rationale**: A reason term like `{user_not_found, Id}` lets callers pattern-match the specific failure and lets you attach data (the offending id) for diagnosis; a pre-formatted string forces brittle substring matching and throws away structure. Render reasons to text only at the logging or user boundary (EH-14, FT-04).

**See also**: EH-01, EH-14

---

## EH-13: Don't Catch What a Supervisor Should Handle

**Strength**: SHOULD

**Summary**: Don't wrap a worker's main loop in a catch-all to keep it alive; let it crash so a supervisor can restart it to a known-good state.

```erlang
%% Bad - a catch-all so the process "never dies": corrupt state persists, supervision is defeated
loop(State) ->
    try handle_next(State) of
        S -> loop(S)
    catch _:_ -> loop(State)    %% keeps looping with the same (possibly bad) state
    end.

%% Good - let the process crash; the supervisor restarts it to a clean state
loop(State) ->
    S = handle_next(State),
    loop(S).
```

**Rationale**: Catching everything to avoid a crash keeps a process running with state that may be corrupt, and hides the fault from the supervision tree that exists to fix it (FT-07). The Erlang model is to detect and recover *remotely*: let the process die and let its supervisor restart it.

**See also**: EH-05, EH-07, `09-fault-tolerance.md` (FT-07)

---

## EH-14: Log with the `logger` API, Using Levels and Structured Metadata

**Strength**: SHOULD

**Summary**: Emit diagnostics through the `logger` API with an appropriate severity and structured metadata; let SASL capture supervisor and crash reports.

```erlang
%% Bad - print to stdout: no severity, unstructured, lost on restart
io:format("error: ~p~n", [Reason]).

%% Good - logger with a level and structured metadata
logger:error("request failed", #{reason => Reason, request_id => ReqId}).
%% SASL/Kernel logger captures supervisor progress and crash reports automatically.
```

**Rationale**: `logger` (the OTP 21+ logging API, the default on OTP 27) provides severity levels, structured metadata maps, and configurable handlers/filters — far more useful than `io:format` to a console that vanishes on restart. Crash and supervisor reports are captured for you; your job is to log the application-level events with the right level and enough structure to query later.

**See also**: EH-12, `14-production-ops.md`

---

## EH-15: Deserialize Untrusted Binaries with `binary_to_term(_, [safe])`

**Strength**: MUST

**Summary**: Never call `binary_to_term/1` on data from outside the trust boundary; pass `[safe]` so it cannot mint new atoms or unsafe terms.

```erlang
%% Bad - binary_to_term/1 on network input can create arbitrary atoms (table exhaustion) and unsafe terms
Term = binary_to_term(PacketFromNetwork).

%% Good - the [safe] option refuses to create new atoms or other unsafe constructs
Term = binary_to_term(PacketFromNetwork, [safe]).
```

**Rationale**: `binary_to_term/1` will create atoms and other terms encoded in the input; on untrusted data that is a denial-of-service (the atom table is bounded and never collected — DT-13) and a decoding-safety hazard. The `[safe]` option rejects creation of new atoms and unsafe terms, raising `badarg` instead. Treat any externally-sourced binary as hostile.

**See also**: EH-10, `04-data-and-types.md` (DT-13), `11-anti-patterns.md`

---

## EH-16: Don't Use `throw` for Non-Local Returns

**Strength**: CONSIDER

**Summary**: Express early exits with ordinary recursion, clauses, or guards — not `throw`/`catch` as a `goto`.

```erlang
%% Bad - throw/catch used as a non-local "return" to break out of a fold
sum_until(Limit, L) ->
    try lists:foldl(fun(X, A) when A + X > Limit -> throw(A);
                       (X, A) -> A + X end, 0, L)
    catch throw:A -> A end.

%% Good - express the early exit with recursion and clause heads
sum_until(_Limit, [])                     -> 0;
sum_until(Limit, [X | _]) when X > Limit  -> 0;
sum_until(Limit, [X | T])                 -> X + sum_until(Limit - X, T).
```

**Rationale**: Using `throw` to jump out of a loop hides control flow inside an exception mechanism, making the code hard to follow and easy to break (a stray matching `catch` elsewhere can intercept it). Erlang's clause heads, guards, and recursion express early termination directly and legibly.

**See also**: EH-09, `05-functions-and-pattern-matching.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| EH-01 Tagged returns | SHOULD | `{ok,_}`/`{error,_}`; no ambiguous sentinels |
| EH-02 Three classes | SHOULD | `error`=bug, `exit`=stop, `throw`=catchable |
| EH-03 Values vs exceptions | SHOULD | Expected failure is a value, not an exception |
| EH-04 Separate the paths | SHOULD | Program the normal case; recover elsewhere |
| EH-05 Crash on bugs | SHOULD | Don't mask programmer errors with fallbacks |
| EH-06 `try` over `catch` | SHOULD | Explicit class + bound stacktrace |
| EH-07 Specific catches | SHOULD | Never blanket `_:_` |
| EH-08 No nested `try` | SHOULD | One `try`, many `catch` clauses |
| EH-09 `throw` sparingly | CONSIDER | Only for messy external input; document it |
| EH-10 Validate at borders | SHOULD | Check once at entry, then trust |
| EH-11 `after` cleanup | SHOULD | Guaranteed resource release |
| EH-12 Structured reasons | SHOULD | Matchable terms, not strings |
| EH-13 Don't out-catch the supervisor | SHOULD | Let it crash; don't loop on bad state |
| EH-14 Use `logger` | SHOULD | Levels + structured metadata, not `io:format` |
| EH-15 Safe deserialization | MUST | `binary_to_term(_, [safe])` on untrusted data |
| EH-16 No non-local returns | CONSIDER | Recursion/clauses over `throw` as `goto` |

## Related Guidelines

- **Fault tolerance**: See `09-fault-tolerance.md` — EH-04/EH-05/EH-13 are the let-it-crash philosophy; EH-10 is FT-02.
- **Data & types**: See `04-data-and-types.md` — tagged returns (EH-01), structured reasons (EH-12), and the atom-table risk behind EH-15 (DT-13).
- **Core idioms**: See `01-core-idioms.md` — nesting (ID-08) and pure/effect separation (ID-15) underlie EH-04/EH-08.
- **Functions & pattern matching**: See `05-functions-and-pattern-matching.md` for the clause/guard style that replaces non-local returns (EH-16).
- **Production ops**: See `14-production-ops.md` for reading crash reports and logs produced by EH-14.

## External References

- Erlang Programming Rules and Conventions — §4.1 (separate error handling), §6.3 (tagged return values), §6.4 (use catch/throw with care)
- [Erlang Reference Manual — Errors and Error Handling](https://www.erlang.org/doc/system/errors.html)
- [Erlang Reference Manual — Expressions (Try/Catch)](https://www.erlang.org/doc/system/expressions.html)
- [Kernel — logger (logging API)](https://www.erlang.org/doc/apps/kernel/logger.html)
- *Programming Erlang* (Joe Armstrong) — Error Handling in Sequential Programs
- *Erlang and OTP in Action* — "Check the borders"; Logging in Erlang/OTP
- Inaka Erlang Guidelines — Syntax (avoid nested try/catches)
