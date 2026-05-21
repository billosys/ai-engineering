# Functions and Pattern Matching

How to write Erlang functions in the grain of the language: dispatch with clause heads and guards instead of `if`/`case`, prefer higher-order functions and comprehensions to hand-rolled recursion, use tail recursion with accumulators where it matters, destructure with the bit syntax, and order clauses correctly. The shared style (small functions, limited nesting, single assignment) is in `01-core-idioms.md`; the type side of specs is in `04-data-and-types.md`. This is a technique chapter — almost all **SHOULD**/**CONSIDER**.

Target environment: **Erlang/OTP 27+** (FP-15 uses `maybe`, OTP 25+). Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: Inaka guidelines (Syntax), the Erlang Reference Manual (Patterns, Guards, Expressions), Programming Erlang, Designing for Scalability with Erlang/OTP, and Learn You Some Erlang.

---

## FP-01: Dispatch in the Function Head, Not a Top-Level `case`

**Strength**: SHOULD

**Summary**: Use multiple clauses with patterns and guards to dispatch, rather than one clause wrapping a `case` on the argument.

```erlang
%% Bad - one clause with a top-level case dispatching on the argument
classify(N) ->
    case N of
        0            -> zero;
        _ when N > 0 -> positive;
        _            -> negative
    end.

%% Good - clauses + guards do the dispatch; each branch is named by its head
classify(0)            -> zero;
classify(N) when N > 0 -> positive;
classify(_N)           -> negative.
```

**Rationale**: "Use pattern-matching in clause functions rather than case's," especially when the `case` is the function's top-level expression (Inaka). Clause heads are Erlang's primary dispatch; they let the compiler check coverage, compose with guards, and read as a rule table. A body `case` adds indentation and hides the structure (ID-07).

**See also**: FP-02, FP-03, FP-12, `01-core-idioms.md` (ID-07)

---

## FP-02: Pattern-Match Instead of Testing Equality

**Strength**: SHOULD

**Summary**: To branch on whether two values are equal, match one against the other directly rather than computing a boolean and switching on it.

```erlang
%% Bad - compute a boolean, then switch on true/false
handle(A, B) ->
    case A =:= B of
        true  -> same;
        false -> different
    end.

%% Good - match one value against the other in the head
handle(A, A)   -> same;
handle(_A, _B) -> different.
```

**Rationale**: "Don't use equality and then switch according to the boolean result… use pattern matching instead" (Inaka). Matching `A` against `A` (a repeated variable) expresses "equal" declaratively and lets the head do the work — clearer than threading a boolean through a `case`.

**See also**: FP-01, FP-04

---

## FP-03: Avoid `if`

**Strength**: SHOULD

**Summary**: Don't use `if`; use guarded `case` or guarded function clauses.

```erlang
%% Bad - if with a true-> catch-all
size_class(N) -> if N > 100 -> big; N > 10 -> medium; true -> small end.

%% Good - guarded clauses
size_class(N) when N > 100 -> big;
size_class(N) when N > 10  -> medium;
size_class(_N)             -> small.
```

**Rationale**: "Don't use `if`" (Inaka). Erlang's `if` only takes guards (no general expressions), needs a `true ->` catch-all to avoid an `if_clause` crash, and is error-prone for newcomers who expect imperative-`if` semantics. Guarded clauses or `case` are more declarative and harder to get subtly wrong.

**See also**: FP-01, FP-04

---

## FP-04: Read Guard Sequences Correctly — `,` is AND, `;` is OR

**Strength**: SHOULD

**Summary**: Within a guard, commas combine expressions with AND; semicolons separate alternative guards with OR. Don't confuse them.

```erlang
%% Bad - semicolons here mean OR: this accepts any integer, OR anything > 0, OR anything < 100
valid(X) when is_integer(X); X > 0; X < 100 -> ok.

%% Good - comma = AND within a guard; semicolon = OR between guards
valid(X) when is_integer(X), X > 0, X < 100 -> ok;   %% all three must hold
valid(X) when is_atom(X)                    -> ok.   %% OR: an atom is valid too
```

**Rationale**: A guard sequence is true if *at least one* guard is true; a single guard is true if *all* its expressions are true (Reference Manual). Mixing up `,` and `;` silently inverts the logic — a guard meant to require three conditions instead accepts any one of them. Keep guards small enough to read at a glance.

**See also**: FP-05, FP-01

---

## FP-05: Guards Are Restricted and Side-Effect-Free

**Strength**: SHOULD

**Summary**: Guards may use only the guard-safe BIFs and operators (`is_*`, comparisons, arithmetic, `andalso`/`orelse`); you cannot call ordinary functions in a guard.

```erlang
%% Bad - calling a user function in a guard is a compile error
process(X) when my_mod:looks_ok(X) -> do(X).

%% Good - use guard BIFs; push richer checks into the body
process(X) when is_integer(X), X >= 0 -> do(X);
process(X) ->
    case my_mod:looks_ok(X) of
        true  -> do(X);
        false -> {error, bad_input}
    end.
```

**Rationale**: Guards must be free of side effects and decidable, so the language restricts them to a fixed set of BIFs and operators; an arbitrary function call won't compile. This keeps clause selection pure and predictable. When a test needs real computation, do it in the body and return a value (EH-03).

**See also**: FP-04, `03-error-handling.md` (EH-03)

---

## FP-06: Prefer Higher-Order Functions over Hand-Rolled Recursion

**Strength**: SHOULD

**Summary**: Reach for `lists:map`/`filter`/`foldl` (or a comprehension) before writing an explicit recursive function.

```erlang
%% Bad - hand-rolled recursion to map over a list
upcase([])      -> [];
upcase([C | T]) -> [string:to_upper(C) | upcase(T)].

%% Good - a higher-order function states "one action per element"
upcase(S) -> lists:map(fun string:to_upper/1, S).
```

**Rationale**: "Occasionally recursion is the best way… but often a fold or a list comprehension will yield safer, more comprehensible code" (Inaka). A `map`/`fold` has known, predictable behaviour; a hand-written recursion must be read carefully to confirm its base case and control flow. Reserve explicit recursion for shapes the standard combinators don't capture.

**See also**: FP-07, FP-08

---

## FP-07: Use List Comprehensions for Map-and-Filter

**Strength**: SHOULD

**Summary**: Express "transform the elements that pass a test" as a comprehension with a generator, tests, and an expression.

```erlang
%% Bad - nested map over filter
evens_doubled(L) ->
    lists:map(fun(X) -> X * 2 end,
              lists:filter(fun(X) -> X rem 2 =:= 0 end, L)).

%% Good - a list comprehension: expression || generator, test
evens_doubled(L) -> [X * 2 || X <- L, X rem 2 =:= 0].
```

**Rationale**: A comprehension `[Expr || Generator, Test]` reads directly as "for each element, if the test passes, produce the expression" (Cesarini & Vinoski). It is more compact and legible than composing `map` and `filter`, and the compiler optimises it well. (Keep control flow out of comprehensions — ID-16.)

**See also**: FP-06, `01-core-idioms.md` (ID-16)

---

## FP-08: Use Tail Recursion with an Accumulator Where It Matters

**Strength**: SHOULD

**Summary**: For large or unbounded input, write a tail-recursive helper with an accumulator so the call runs in constant stack space.

```erlang
%% Bad - body recursion builds a deep stack on large input
sum([])      -> 0;
sum([H | T]) -> H + sum(T).

%% Good - tail-recursive accumulator runs in constant stack space
sum(L) -> sum(L, 0).
sum([], Acc)      -> Acc;
sum([H | T], Acc) -> sum(T, Acc + H).
%% (for small/bounded data, body recursion or lists:sum/1 is perfectly clear)
```

**Rationale**: A tail call reuses the current stack frame, so a tail-recursive loop processes arbitrarily long input without growing the stack — essential for server loops (PC-06) and large collections. Body recursion is fine and often clearer for short, bounded lists; reach for the accumulator when input size is large or unbounded.

**See also**: FP-09, `06-processes-and-concurrency.md` (PC-06)

---

## FP-09: Build Accumulators by Prepending, Then Reverse

**Strength**: CONSIDER

**Summary**: Accumulate results by prepending (`O(1)`) and `lists:reverse/1` once at the end — never append to the tail in a loop.

```erlang
%% Bad - append to the end of the accumulator: O(n^2)
collect([], Acc)      -> Acc;
collect([H | T], Acc) -> collect(T, Acc ++ [f(H)]).

%% Good - prepend (O(1)) and reverse once at the end
collect(L) -> collect(L, []).
collect([], Acc)      -> lists:reverse(Acc);
collect([H | T], Acc) -> collect(T, [f(H) | Acc]).
```

**Rationale**: `++` copies its entire left operand, so appending inside a loop is quadratic. Prepending is constant-time, and a single final `lists:reverse/1` restores order in linear time. This "build reversed, reverse once" idiom is the standard shape of a tail-recursive list builder.

**See also**: FP-08, `04-data-and-types.md` (DT-11), `10-performance.md`

---

## FP-10: Capture Functions Directly with `fun Name/Arity`

**Strength**: CONSIDER

**Summary**: Pass an existing function as `fun Name/Arity` (or `fun Mod:Name/Arity`) instead of wrapping it in a needless anonymous fun.

```erlang
%% Bad - wrap a named function in an anonymous fun for no reason
lists:map(fun(X) -> double(X) end, L).

%% Good - capture it directly
lists:map(fun double/1, L),
lists:foreach(fun io:format/1, Lines).
```

**Rationale**: The capture syntax is shorter, avoids introducing a parameter name, and makes the intent ("apply this function") explicit. Reserve anonymous funs for genuine closures (capturing surrounding variables) or inline logic that has no name worth giving.

**See also**: FP-06, FP-07

---

## FP-11: Destructure Binaries in the Function Head

**Strength**: SHOULD

**Summary**: Match binary structure with the bit syntax in the clause head rather than slicing with offsets in the body.

```erlang
%% Bad - receive a binary, then pick it apart with offset arithmetic
handle(Pkt) ->
    Version = binary:at(Pkt, 0),
    Len     = binary:decode_unsigned(binary:part(Pkt, 1, 2)),
    Body    = binary:part(Pkt, 3, Len).

%% Good - destructure in the head; bind fields and the remainder at once
handle(<<Version:8, Len:16, Body:Len/binary, _Rest/binary>>) ->
    {Version, Body}.
```

**Rationale**: Bit-syntax matching expresses binary layout declaratively, binds every field and the remainder in one pattern, and is heavily optimised by the compiler (and lets a clause not match cleanly fall through to the next). It is the idiomatic way to parse protocols and framed data (DT-12).

**See also**: FP-01, `04-data-and-types.md` (DT-12)

---

## FP-12: Order Clauses from Specific to General

**Strength**: SHOULD

**Summary**: Put specific clauses first and any catch-all last; clause selection is first-match, so a misplaced catch-all shadows everything after it.

```erlang
%% Bad - the catch-all is first, so the specific clauses are dead code
area(_Other)      -> {error, unsupported};
area({circle, R}) -> 3.14159 * R * R.        %% never reached

%% Good - specific clauses first, catch-all last
area({circle, R}) -> {ok, 3.14159 * R * R};
area({square, S}) -> {ok, S * S};
area(_Other)      -> {error, unsupported}.
```

**Rationale**: Erlang tries clauses top-to-bottom and commits to the first whose head and guard match. A general clause placed early intercepts inputs meant for later clauses (the compiler warns about the resulting unreachable clauses). Specific-to-general ordering keeps every clause live and the dispatch correct.

**See also**: FP-01, FP-13

---

## FP-13: Use `_` / `_Name` for Ignored Bindings

**Strength**: SHOULD

**Summary**: Bind values you don't use to `_` (don't care) or `_Name` (documented but unused) to silence warnings and signal intent.

```erlang
%% Bad - bind a name you never use (compiler warns) — or worse, use a _-prefixed one
handle({event, Type, Payload}) -> log(Type).   %% Payload unused -> warning

%% Good - _ for don't-care, _Name to document what is ignored
handle({event, Type, _Payload}) -> log(Type).
```

**Rationale**: An unused ordinary variable triggers a compiler warning that hides real ones; `_` and `_Name` say "intentionally ignored." Keep the promise (ID-11): if you actually use the value, give it a real name. `_Name` is preferred over bare `_` when the position's meaning aids the reader.

**See also**: FP-12, `01-core-idioms.md` (ID-11)

---

## FP-14: Bind the Whole Term and Its Parts with the `=` Pattern

**Strength**: CONSIDER

**Summary**: Use the compound pattern `Var = Pattern` to capture both the whole term and its pieces, instead of rebuilding the term.

```erlang
%% Bad - destructure, then reconstruct the same record to pass it on
update(#user{id = Id}) ->
    save(#user{id = Id}).      %% rebuilds a record you already had

%% Good - bind the whole term and its fields at once
update(#user{id = Id} = U) ->
    save(U#user{seen = erlang:system_time(second)}, Id).
```

**Rationale**: The compound pattern operator matches a term against two patterns simultaneously, so you can name the whole value *and* extract fields without reconstructing it (and without the `=` implying any evaluation order between the sub-patterns). It avoids both duplication and the bugs that come from rebuilding a term slightly differently.

**See also**: FP-01, `04-data-and-types.md`

---

## FP-15: Thread `{ok, _}` Pipelines with `maybe`

**Strength**: CONSIDER

**Summary**: Use the `maybe` expression (OTP 25+, enabled by default in 27) to sequence fallible `{ok, _}`-returning steps without a nested-`case` staircase.

```erlang
%% Bad - a staircase of nested case to thread {ok, _} values
load(F) ->
    case read(F) of
        {ok, B} ->
            case parse(B) of
                {ok, T} -> validate(T);
                E       -> E
            end;
        E -> E
    end.

%% Good - maybe short-circuits on the first non-matching step
load(F) ->
    maybe
        {ok, B} ?= read(F),
        {ok, T} ?= parse(B),
        validate(T)
    end.
```

**Rationale**: `maybe ... end` evaluates each `Pattern ?= Expr` in turn and, if a match fails, yields that non-matching value as the result of the whole block — collapsing the classic `{ok,_}`/`{error,_}` pyramid into a flat sequence. It keeps the happy path readable (EH-04) without exceptions. Available since OTP 25 as a feature; default on OTP 27.

**See also**: FP-01, `03-error-handling.md` (EH-04)

---

## FP-16: Tie Inputs to Outputs with Type Variables and Overloaded Specs

**Strength**: CONSIDER

**Summary**: Use a `when T :: ...` type variable to express that output relates to input, and overloaded specs to give distinct argument types distinct results.

```erlang
%% Bad - a loose spec loses the relationship between argument and result
-spec first([term()]) -> term().

%% Good - a type variable ties them; overloaded clauses narrow distinct cases
-spec first([T]) -> T when T :: term().
-spec convert(integer()) -> binary();
             (atom())    -> binary().
```

**Rationale**: A type variable lets Dialyzer know `first/1` returns an element *of the list it was given*, not just any term, so it can catch more misuse at call sites. Overloaded specs document genuinely different argument/result pairings precisely. Both make the contract (API-07/DT-16) carry real information.

**See also**: `04-data-and-types.md` (DT-16), `02-api-design.md` (API-07)

---

## FP-17: Don't Put Runtime Expressions in Patterns

**Strength**: CONSIDER

**Summary**: Patterns may contain literals and compile-time constants only; move any runtime computation into a guard.

```erlang
%% Bad - a runtime arithmetic expression in a pattern (not allowed)
match(N, {result, N + 1}) -> ok.

%% Good - bind, then test the relationship in a guard
match(N, {result, M}) when M =:= N + 1 -> ok.
%% (a compile-time constant such as ?THRESHOLD + 1 IS permitted inside a pattern)
```

**Rationale**: A pattern can only contain bound-variable matches, literals, and arithmetic on *compile-time* constants (DT: expressions-in-patterns); a term like `N + 1` where `N` is a runtime value is not a valid pattern. Express the relationship with a guard instead, where runtime arithmetic is allowed.

**See also**: FP-04, `04-data-and-types.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| FP-01 Dispatch in the head | SHOULD | Clauses + guards over a top-level `case` |
| FP-02 Match, don't test equality | SHOULD | `f(A, A)` over `A =:= B` then switch |
| FP-03 Avoid `if` | SHOULD | Guarded clauses/`case` instead |
| FP-04 Guard `,` vs `;` | SHOULD | Comma = AND, semicolon = OR |
| FP-05 Guards are restricted | SHOULD | Only guard BIFs; no side effects |
| FP-06 Higher-order over recursion | SHOULD | `map`/`fold`/comprehension first |
| FP-07 List comprehensions | SHOULD | Map-and-filter in one expression |
| FP-08 Tail recursion + accumulator | SHOULD | Constant stack for large/unbounded input |
| FP-09 Prepend then reverse | CONSIDER | Avoid `O(n^2)` tail-append |
| FP-10 `fun Name/Arity` | CONSIDER | Capture directly; no wrapper fun |
| FP-11 Bit syntax in the head | SHOULD | Destructure binaries declaratively |
| FP-12 Specific clauses first | SHOULD | First-match; catch-all last |
| FP-13 `_`/`_Name` for ignored | SHOULD | Silence warnings, signal intent |
| FP-14 Compound `=` pattern | CONSIDER | Bind whole + parts; don't rebuild |
| FP-15 `maybe` pipelines | CONSIDER | Flatten `{ok,_}` staircases (OTP 25+) |
| FP-16 Type vars / overloaded specs | CONSIDER | Tie outputs to inputs for Dialyzer |
| FP-17 No expressions in patterns | CONSIDER | Runtime tests go in guards |

## Related Guidelines

- **Core idioms**: See `01-core-idioms.md` — head-matching (ID-07), nesting (ID-08), small functions (ID-09), and ignored bindings (ID-11).
- **Data & types**: See `04-data-and-types.md` for bit syntax (DT-12), iolist/append cost (DT-11), specs and type variables (DT-16).
- **Error handling**: See `03-error-handling.md` — `maybe` (FP-15) and guard-vs-body checks (FP-05) connect to EH-03/EH-04.
- **Processes & concurrency**: See `06-processes-and-concurrency.md` (PC-06) for why server loops in particular must be tail-recursive.
- **Performance**: See `10-performance.md` for the cost model behind FP-08/FP-09.

## External References

- [Erlang Reference Manual — Patterns](https://www.erlang.org/doc/system/patterns.html)
- [Erlang Reference Manual — Guard Sequences](https://www.erlang.org/doc/system/expressions.html#guard-sequences)
- Inaka Erlang Guidelines — Syntax (avoid `if`, functions over `case`, prefer pattern matching, favour higher-order functions)
- *Programming Erlang* (Joe Armstrong) — functions, guards, higher-order functions
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — list comprehensions (pp. 27–28)
