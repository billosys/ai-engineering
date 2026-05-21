# Core Erlang Idioms

The shared style and structure of idiomatic Erlang: naming, comment levels, formatting, module layout, single-assignment and pattern-matching style, small focused functions, and the discipline of keeping pure code separate from side effects. These idioms underpin every later chapter; topic-specific rules (data types, functions, errors) live in their own guides. This chapter is mostly **SHOULD** — convention, not correctness — but consistency here is what makes a codebase navigable.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: Inaka guidelines (Source Code Layout, Syntax, Naming), the Erlang Programming Rules, the nuex style guide, the Erlang Reference Manual (Modules), and Programming Erlang.

---

## ID-01: Name by Convention — CamelCase Variables, snake_case Everything Else

**Strength**: SHOULD

**Summary**: Variables are `CamelCase`; atoms, function names, and module names are lowercase `snake_case`.

```erlang
%% Bad - camelCase atoms/functions, Under_Score variables
Variable_Name = moduleName:functionName(atomConstant).

%% Good - CamelCase variables; snake_case atoms, functions, modules
VariableName = module_name:function_name(atom_constant).
```

**Rationale**: "Use variables in CamelCase and atoms, function and module names with underscores" (Inaka). The casing split is also enforced by the language itself — a leading uppercase letter *is* what makes a token a variable rather than an atom — so following the convention keeps intent and syntax aligned and makes code instantly readable to any Erlanger.

**See also**: ID-11, `04-data-and-types.md`

---

## ID-02: Use the Three Comment Levels

**Strength**: SHOULD

**Summary**: `%%%` for module-level commentary, `%%` for function-level commentary, `%` for inline/end-of-line notes.

```erlang
%% Bad - a single % for everything, including module- and function-level prose
% accounting helpers
% sum a list of line items
total(L) -> lists:sum(L).

%%% Good - %%% module-level, %% function-level, % inline
%%% Accounting helpers.
%% Sum a list of line items.
total(L) -> lists:sum(L).   % delegates to lists:sum/1
```

**Rationale**: A comment "begins with the character `%` and continues up to… the next end of line" (Reference Manual), but the community convention layers meaning onto the count: `%%%` headers a module/section, `%%` documents a function, `%` annotates a line. The consistent levels let readers (and folding editors) scan structure at a glance.

**See also**: ID-18, `13-documentation.md`

---

## ID-03: Spaces, Not Tabs; Two-Space Indent

**Strength**: SHOULD

**Summary**: Indent with spaces only, two per level; never tabs.

```erlang
%% Bad - a leading tab renders differently in every editor and breaks alignment
init(Args) ->
	{ok, Args}.

%% Good - spaces only, two-space indent
init(Args) ->
  {ok, Args}.
```

**Rationale**: "Spaces over tabs, 2 space indentation" (Inaka); the nuex guide agrees ("2 space indent, no tabs"). Tabs render at different widths across editors, so a tab-indented file that looks aligned for the author is misaligned for everyone else. Spaces make layout absolute.

**See also**: ID-04, ID-05

---

## ID-04: Reasonable Line Length, Spaced Operators, No Trailing Whitespace

**Strength**: SHOULD

**Summary**: Keep lines within ~100 columns, put single spaces around binary operators, and leave no trailing whitespace.

```erlang
%% Bad - no spaces around operators, trailing whitespace, cramped arrow
total(A,B,C)->A+B+C.

%% Good - spaces around operators and after commas; clean line endings
total(A, B, C) -> A + B + C.
```

**Rationale**: "Use single spaces around operators… no spaces after `{`, `(`, `[`" and "keep lines fewer than 80–100 characters… avoid trailing whitespace" (nuex/Inaka). These are small things that, applied consistently, make diffs clean and code uniform. A pre-commit hook or formatter removes the need to think about them.

**See also**: ID-03, ID-05

---

## ID-05: Let the Formatter Decide Layout; Match Existing Style

**Strength**: SHOULD

**Summary**: Run `erlfmt` to enforce layout mechanically, and when editing existing code, follow the style already there rather than imposing your own.

```erlang
%% Bad - reformat to personal taste mid-change, leaving two layouts in one module
new_entry() -> {elem3,3}.        %% different spacing/commas than the existing list

%% Good - match the surrounding style; let erlfmt normalise the whole project
new_entry() -> {elem3, 3}.
```

**Rationale**: "When editing a module written by someone else, stick to the style in which it was written. If a project has an overall style, stick to that" (Inaka). The unit of consistency is the module first, then the project — local consistency beats personal preference. A formatter (`erlfmt`) removes most of the argument by making layout deterministic.

**See also**: ID-03, ID-04, `17-tooling.md`

---

## ID-06: Bindings Are Immutable — Introduce a New Name, Don't Rebind

**Strength**: SHOULD

**Summary**: A variable is bound once; to express a "changed" value, introduce a new name (`X1`), don't try to reassign.

```erlang
%% Bad - attempt to mutate a bound variable
X = compute(),
X = X + 1.            %% badmatch: X is already bound to compute()'s result

%% Good - single assignment; a new value gets a new name
X  = compute(),
X1 = X + 1.
```

**Rationale**: "Erlang has single-assignment variables… once it gets a value, it keeps it forever" (Programming Erlang, ch. 3). `=` is pattern match, not assignment: `X = X + 1` tries to match a bound `X` against `X + 1` and fails. Immutability is what makes Erlang code easy to reason about and safe to run concurrently; lean into it with fresh names (or, better, by passing values through function calls).

**See also**: ID-07, ID-15

---

## ID-07: Match in the Function Head, Not with a Body `case`

**Strength**: SHOULD

**Summary**: Dispatch on the shape of arguments with multiple function clauses, rather than a single clause wrapping a `case`.

```erlang
%% Bad - one clause that destructures with a nested case
handle(Msg) ->
    case Msg of
        {ok, V}    -> use(V);
        {error, R} -> log(R)
    end.

%% Good - one clause per shape; the head does the matching
handle({ok, V})    -> use(V);
handle({error, R}) -> log(R).
```

**Rationale**: Clause heads are Erlang's primary dispatch mechanism; they read as a set of rules, compose with guards, and let the compiler check coverage. Pushing the same distinction into a body `case` adds a level of indentation and hides the structure. Reserve `case` for decisions that genuinely belong inside one clause.

**See also**: ID-08, `05-functions-and-pattern-matching.md`

---

## ID-08: Don't Nest More Than About Three Levels Deep

**Strength**: SHOULD

**Summary**: Deeply nested `case`/`try`/`receive` signals too many decisions in one function; extract inner blocks into named functions.

```erlang
%% Bad - four levels of case/try/receive in one function
f(X) ->
    case a(X) of
        {ok, Y} ->
            case b(Y) of
                {ok, Z} -> try c(Z) of R -> R catch _:_ -> err end;
                E       -> E
            end;
        E -> E
    end.

%% Good - flatten; push inner steps into their own functions
f(X) ->
    case a(X) of
        {ok, Y} -> step_b(Y);
        E       -> E
    end.
```

**Rationale**: "Try not to nest more than 3 levels deep" (Inaka); deep nesting hinders readability, testing, and debugging. Each extracted function gets a name (documentation) and becomes independently testable and traceable. Nesting depth is a reliable smell for "this function does too much" (ID-09).

**See also**: ID-09, ID-16

---

## ID-09: Keep Functions Small and Single-Purpose

**Strength**: SHOULD

**Summary**: A function should do one thing; roughly 12 expressions is a good ceiling (integration tests excepted).

```erlang
%% Bad - one function finds-or-creates, cleans, stores, and delivers, all inline
handle(User, Raw) ->
    %% ~40 lines doing four unrelated things with nested cases
    ok.

%% Good - delegate each step to a small, named, single-purpose helper
handle(User, Raw) ->
    U   = find_or_create(User),
    Msg = clean(Raw),
    ok  = store(U, Msg),
    deliver(U, Msg).
```

**Rationale**: "Write functions with a small number of expressions, that do only one thing — 12 expressions per function… is a good measure" (Inaka). Small functions are easier to read, name, test, trace, and reuse, and they make stack traces meaningful. Length is a proxy; the real target is one responsibility per function.

**See also**: ID-08, ID-10, ID-17

---

## ID-10: Keep Modules Focused

**Strength**: SHOULD

**Summary**: One module, one responsibility; group related functions and split unrelated concerns into separate modules.

```erlang
%% Bad - a single sprawling module mixing HTTP, persistence, and auth
-module(everything).   %% thousands of lines, three unrelated concerns

%% Good - one concern per module
-module(http_api).     %% routing and handlers
-module(user_store).   %% persistence
-module(auth).         %% credentials
```

**Rationale**: A focused module is easier to understand, test, and reuse, and its name documents what it is for. Giant catch-all modules accrete unrelated functions, blur ownership, and make every change risky. Group functions logically and let module boundaries follow responsibilities (see also project structure, `12`).

**See also**: ID-09, `12-project-structure.md`

---

## ID-11: A Leading Underscore Means "Deliberately Unused" — Honour It

**Strength**: SHOULD

**Summary**: `_`-prefixed variables are still real bindings; the underscore promises you won't use them. If you use it, drop the underscore.

```erlang
%% Bad - an "ignored" variable that is actually used
double(_Number) -> 2 * _Number.

%% Good - if you use it, name it without the underscore
double(Number) -> 2 * Number.
```

**Rationale**: "Variables beginning with `_` are still variables… the `_` just keeps the compiler from warning when you don't use them. If you add the `_`, don't use it" (Inaka). The leading underscore is a signal to the reader and the compiler; using such a binding contradicts the signal and confuses anyone scanning for what a clause actually depends on.

**See also**: ID-01, ID-07

---

## ID-12: Don't Use `-import`; Always Module-Qualify Calls

**Strength**: SHOULD

**Summary**: Never import functions into the local namespace; call them with their module prefix.

```erlang
%% Bad - -import hides where a function comes from
-import(lists, [map/2]).
f(L) -> map(fun double/1, L).        %% looks local; isn't

%% Good - always module-qualify
f(L) -> lists:map(fun double/1, L).
```

**Rationale**: "Do not use the `-import` directive" (Inaka). An imported call looks identical to a local one, so readers can't tell where `map/2` lives, and a later local function of the same name silently clashes. The module prefix is a few characters that make every call's origin obvious and greppable.

**See also**: ID-13, ID-14

---

## ID-13: Avoid Dynamic Calls Unless You Actually Need Them

**Strength**: SHOULD

**Summary**: Calling `Mod:Fun(...)` where the module or function comes from a variable defeats static analysis; use explicit calls unless dynamic dispatch is genuinely required.

```erlang
%% Bad - module/function from a variable: xref and the compiler can't see the call graph
run(Mods, Arg) -> [M:handle(Arg) || M <- Mods].

%% Good - explicit calls when the set is known; reserve dynamic dispatch for real plugin needs
run(Arg) -> [mod_a:handle(Arg), mod_b:handle(Arg), mod_c:handle(Arg)].
```

**Rationale**: "If there is no specific need for it, don't use dynamic function calling" (Inaka) — dynamic calls "can't be checked by xref, one of the most useful tools in the Erlang world." Static calls let xref find dead code, missing functions, and unintended dependencies. Dynamic dispatch is the right tool for true plugin systems and behaviours, not for ordinary calls.

**See also**: ID-12, `17-tooling.md`

---

## ID-14: Avoid Macros — Use Functions for Code, Macros Only for Constants

**Strength**: SHOULD

**Summary**: Don't use macros except the predefined ones (`?MODULE`, `?LINE`, …) and literal constants; replace code-block macros with real functions.

```erlang
%% Bad - a macro that wraps a block of code (opaque to tools, no stack frame)
-define(LOG_ERROR(E), error_logger:error_msg("~p~n", [E])).
f(R) -> ?LOG_ERROR(R).

%% Good - a real function for behaviour; macros only for literal constants
-define(DEFAULT_TIMEOUT, 5000).
log_error(Reason) -> logger:error("~p", [Reason]).
```

**Rationale**: "Don't use macros, except for very specific cases" (Inaka): the predefined macros and literal constants. A code macro is invisible to Dialyzer and xref, produces no stack frame, and can't be traced — a function does the same job while remaining a first-class, analysable, debuggable thing.

**See also**: ID-13, `04-data-and-types.md`

---

## ID-15: Keep Pure Code Separate from Side Effects

**Strength**: SHOULD

**Summary**: Push computation into pure, referentially-transparent functions and keep I/O and other effects at the edges.

```erlang
%% Bad - computation and I/O tangled: hard to test, non-deterministic
report(Id) ->
    Data = db:fetch(Id),
    io:format("total: ~p~n", [lists:sum(Data)]).

%% Good - a pure core with effects at the boundary
total(Data) -> lists:sum(Data).                       %% pure, testable
report(Id)  -> io:format("total: ~p~n", [total(db:fetch(Id))]).
```

**Rationale**: A pure function's output depends only on its inputs, so it is trivial to test, reason about, and reuse, and it never surprises a caller with hidden effects. Concentrating side effects (I/O, messaging, time, randomness) at the boundaries keeps the bulk of the code deterministic — and makes the effectful parts easy to find.

**See also**: ID-06, ID-16

---

## ID-16: Don't Write Spaghetti — Extract Nested Comprehensions and Blocks

**Strength**: SHOULD

**Summary**: Avoid list comprehensions with a `case` inside, or `begin…end` blocks doing real work; lift the logic into a named function.

```erlang
%% Bad - a comprehension with a case (and a begin/end) buried inside
[begin case f(X) of {ok, Y} -> g(Y); _ -> skip end end || X <- Xs].

%% Good - name the per-element step
[process(X) || X <- Xs].
process(X) ->
    case f(X) of
        {ok, Y} -> g(Y);
        _       -> skip
    end.
```

**Rationale**: "Don't write spaghetti code — a list comprehension with a case inside, or blocks with begin/end, and nested stuff" (Inaka). A comprehension should read as "transform each element"; embedding control flow makes it dense and unreadable. Extracting a named function restores both the comprehension's clarity and the step's testability.

**See also**: ID-08, ID-09

---

## ID-17: Don't Repeat Yourself — Abstract Common Patterns

**Strength**: CONSIDER

**Summary**: Factor repeated logic into a shared function (or a higher-order function), and genuinely common code into a library.

```erlang
%% Bad - the same validation copy-pasted into every entry point
create(U) -> case valid(U) of true -> do_create(U); false -> {error, invalid} end.
update(U) -> case valid(U) of true -> do_update(U); false -> {error, invalid} end.

%% Good - capture the shared shape once
with_valid(U, Fun) ->
    case valid(U) of
        true  -> Fun(U);
        false -> {error, invalid}
    end.
create(U) -> with_valid(U, fun do_create/1).
update(U) -> with_valid(U, fun do_update/1).
```

**Rationale**: Duplicated logic drifts out of sync and multiplies the cost of every change. Higher-order functions make Erlang especially good at capturing a shared control shape while leaving the varying part as a `fun`. Apply judgement (hence CONSIDER): a little duplication is better than the wrong abstraction.

**See also**: ID-09, ID-10

---

## ID-18: Follow the Canonical Module Layout

**Strength**: CONSIDER

**Summary**: Order a module predictably: `-module`, `-behaviour`, `-export`/`-export_type`, defines/records/types, then function bodies.

```erlang
%% Bad - attributes, exports, and functions interleaved arbitrarily
foo() -> ok.
-export([foo/0]).
-module(m).

%% Good - canonical top-to-bottom order
-module(m).
-behaviour(gen_server).
-export([start_link/0]).
-export([init/1, handle_call/3]).
%% -define / -record / -type declarations
%% ... then the function bodies
```

**Rationale**: A consistent layout means any reader knows where to find the module's name, its public surface, and its types without scanning the whole file. Keeping all `-export`s near the top makes the public API reviewable at a glance, and grouping related functions in the body aids navigation.

**See also**: ID-02, ID-10, `13-documentation.md`

---

## ID-19: Principle of Least Astonishment — Name Concepts Consistently

**Strength**: CONSIDER

**Summary**: Use one name for one concept across the whole system, and make functions behave the way their names suggest.

```erlang
%% Bad - the same concept named differently in each module
user_store:get_user(Id),
session_db:fetch_account(Id).        %% user? account? get? fetch?

%% Good - one verb and one noun per concept, used everywhere
user_store:fetch(Id),
session_store:fetch(Id).
```

**Rationale**: Consistent vocabulary lets a reader transfer knowledge from one module to the next, and a function that does what its name implies never traps a caller. Inconsistent naming forces everyone to re-learn each module's private dialect. Decide the terms once (a "user" is always a user, `fetch` always reads) and hold the line.

**See also**: ID-01, ID-10

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| ID-01 Naming convention | SHOULD | CamelCase vars; snake_case atoms/functions/modules |
| ID-02 Comment levels | SHOULD | `%%%` module, `%%` function, `%` inline |
| ID-03 Spaces, 2-indent | SHOULD | No tabs; spaces render uniformly |
| ID-04 Line/operator hygiene | SHOULD | ~100 cols, spaced operators, no trailing whitespace |
| ID-05 Formatter + existing style | SHOULD | `erlfmt`; match the surrounding code |
| ID-06 Single assignment | SHOULD | Immutable bindings; new name for a new value |
| ID-07 Match in the head | SHOULD | Clauses over a body `case` |
| ID-08 Limit nesting | SHOULD | ≤ ~3 levels; extract inner blocks |
| ID-09 Small functions | SHOULD | One thing; ~12 expressions |
| ID-10 Focused modules | SHOULD | One responsibility per module |
| ID-11 Honour `_` | SHOULD | Don't use underscore-prefixed bindings |
| ID-12 No `-import` | SHOULD | Always module-qualify calls |
| ID-13 Avoid dynamic calls | SHOULD | Static calls keep xref useful |
| ID-14 Avoid macros | SHOULD | Functions for code; macros for constants |
| ID-15 Isolate side effects | SHOULD | Pure core, effects at the edges |
| ID-16 No spaghetti | SHOULD | Extract case-in-comprehension logic |
| ID-17 DRY | CONSIDER | Abstract repeats; beware the wrong abstraction |
| ID-18 Module layout | CONSIDER | Predictable top-to-bottom order |
| ID-19 Least astonishment | CONSIDER | One name per concept, system-wide |

## Related Guidelines

- **Functions & pattern matching**: See `05-functions-and-pattern-matching.md` — ID-07/ID-08 expand into clause, guard, and recursion design.
- **Data & types**: See `04-data-and-types.md` for naming and typing of records and types referenced by ID-01/ID-14.
- **Documentation**: See `13-documentation.md` — comment levels (ID-02) and module layout (ID-18) feed EDoc/`-doc`.
- **Project structure**: See `12-project-structure.md` for how focused modules (ID-10) map to applications and directories.
- **Tooling**: See `17-tooling.md` for `erlfmt`, `elvis`, and the `xref` analysis that ID-05/ID-13 rely on.

## External References

- Inaka Erlang Guidelines — Source Code Layout, Syntax, Naming (CamelCase/underscore, spaces over tabs, avoid deep nesting, keep functions small, no macros, no import, avoid dynamic calls, maintain existing style)
- Erlang Programming Rules and Conventions — naming, function/module size, comments
- [Erlang Reference Manual — Modules (Comments)](https://www.erlang.org/doc/system/modules.html)
- *Programming Erlang* (Joe Armstrong), ch. 3 — single-assignment variables
- nuex Erlang Style Guide — file composition, general code style
