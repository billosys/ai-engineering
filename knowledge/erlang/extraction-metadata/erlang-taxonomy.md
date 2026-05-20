# Erlang Knowledge Base — Domain Taxonomy & Notation Conventions

Phase 0 deliverable (per `docs/dev/concept-cards/0010-...-v3.2.md`, Steps 0.2 & 0.3).
Shared across **all** Erlang source-slugs so categories and notation stay consistent.

Target baseline: **Erlang/OTP 27+**.

---

## Categories

Primary `category:` values for the `erlang` KB. Mutually exclusive, collectively
exhaustive. Each maps to one or more downstream guide chapters.

| category | covers | guide chapter(s) |
|----------|--------|------------------|
| `core-idioms` | naming, module layout, comment levels, formatting, expression style | 01 |
| `api-design` | exported surfaces, return conventions, opaque types | 02 |
| `error-handling` | errors/exits/throws, try/catch, logging, error values | 03 |
| `data-types` | records, maps, proplists, tuples, binaries/iolists, typespecs | 04 |
| `functions-pattern-matching` | clauses, guards, recursion, comprehensions, HOFs | 05 |
| `processes-concurrency` | spawn, messages, selective receive, links, monitors | 06 |
| `otp-behaviours` | gen_server, gen_statem, gen_event callbacks & contracts | 07 |
| `applications-releases` | supervisors, app behaviour, child specs, releases | 08, 12 |
| `fault-tolerance` | let-it-crash, error kernel, isolation, trapping exits | 09 |
| `performance` | BEAM scheduling, ETS, binaries, memory, profiling | 10 |
| `anti-patterns` | cross-cutting traps with fixes | 11 |
| `documentation` | EDoc, `-doc`/`-moduledoc`, doc-tests | 13 |
| `production-ops` | tracing, recon, crash dumps, overload, live debugging | 14 |
| `testing` | eunit, common_test, PropEr, mocking | 15 |
| `distribution` | distributed Erlang, registries, partitions, cookies | 16 |
| `tooling` | rebar3, dialyzer, xref, elvis, erlfmt | 17 |

> A card's `category` records the *concept's* home; a guide chapter may pull cards
> from several categories. The two axes are orthogonal (see PLAN.md §"Two axes").

## Tiers

- `foundational` — no prerequisites within its source (e.g. *atom*, *tuple*, *pattern matching*)
- `intermediate` — requires foundational concepts (e.g. *gen_server*, *selective receive*)
- `advanced` — requires intermediate concepts (e.g. *gen_statem state-enter calls*, *refc-binary leak diagnosis*, *distributed partition handling*)

---

## Notation Conventions

### Identifiers
- **Variables**: `CamelCase` (`UserId`, `MaxRetries`); leading `_` for deliberately unused (`_Ref`).
- **Atoms, functions, modules**: `snake_case` (`handle_call`, `user_store`).
- **Macros**: `?UPPER_SNAKE` (`?TIMEOUT`).
- **Records**: `#snake_case{}`; record fields `snake_case`.

### Comments (the three levels — Inaka/Programming Rules)
- `%%%` — module-level commentary (file header, big-picture).
- `%%`  — function-level commentary (immediately above a function).
- `%`   — inline / end-of-line commentary.

### Specs & types
- `-spec name(Arg :: arg_type()) -> return_type().`
- `-type foo() :: ... .` / `-opaque handle() :: ... .`
- One `-spec` for every exported function (dialyzer-checkable).

### GOOD / BAD example convention (the house contract)
Inside ` ```erlang ` fences, mark the two halves with **function-level comments**,
which are idiomatic Erlang *and* greppable:

```erlang
%% Bad - blocks the gen_server; every other caller waits on this one
handle_call(fetch, _From, State) ->
    Result = slow_http_get(State),      %% synchronous I/O inside the callback
    {reply, Result, State}.

%% Good - do the slow work in the caller (or a spawned task), keep the server snappy
handle_call({fetch, Url}, From, State) ->
    spawn(fun() -> gen_server:reply(From, slow_http_get(Url)) end),
    {noreply, State}.
```

Rules:
1. **Both** a `%% Bad` and a `%% Good` block are REQUIRED in every guide pattern.
2. Show **Bad first, then Good** (matches `templates/GUIDE.md`).
3. For runtime-failure patterns (mailbox growth, atom-table exhaustion, refc-binary
   leaks, blocking callbacks), the Bad block carries a one-line `%%` annotation
   stating *what actually happens at runtime*.
4. Prose may additionally use the house ✅ GOOD / ❌ BAD emoji subheads; the linter
   (`tools/lint_examples.py`) accepts `%% Good`/`%% Bad`, `% Good`/`% Bad`, or ✅/❌.

### Strength labels
`MUST` · `SHOULD` · `CONSIDER` · `AVOID` (uppercase bold; the anti-patterns chapter
uses `AVOID` on every entry).

### OTP-27+ call-outs
Flag version-gated features explicitly where they appear:
`-doc`/`-moduledoc` attributes, the native `json` module, `maybe ... end`
expressions, triple-quoted strings & sigils, and `proc_lib` process labels.
Note OTP 24/26 differences inline rather than forking examples.
