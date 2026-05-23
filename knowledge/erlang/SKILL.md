---
name: erlang-guidelines
description: |
  Comprehensive Erlang/OTP best practices, idioms, and anti-patterns grounded
  in the Erlang Programming Rules and Conventions, the OTP Design Principles,
  the Erlang Reference Manual and Efficiency Guide, Inaka's coding guidelines,
  "Erlang in Anger", "Learn You Some Erlang", and the EDoc user's guide.
  Use when: writing new Erlang code, refactoring existing Erlang, reviewing
  Erlang for issues, designing module APIs and return conventions, modelling
  data with records/maps/binaries and dialyzer typespecs, designing processes
  and message protocols, writing OTP
  behaviours, building supervision trees
  and applications/releases, applying let-it-crash fault tolerance, profiling
  and tuning on the BEAM, diagnosing live systems, writing eunit/common_test/PropEr
  tests, documenting with EDoc and OTP-27 -doc attributes, running distributed
  Erlang, or wiring the rebar3 + dialyzer + xref + elvis + erlfmt toolchain.
---

# Erlang Coding Guidelines Skill

> STATUS: complete — all 17 guide chapters are populated (281 patterns), each
> conforming to the GOOD/BAD contract enforced by `tools/lint_examples.py`.
> Load `11-anti-patterns.md` first on any task.

## Overview

This skill condenses the most authoritative Erlang sources — the Programming Rules
and Conventions, the OTP Design Principles, the Reference Manual and Efficiency
Guide, Inaka's and nuex's style guides, *Erlang in Anger*, *Learn You Some Erlang*,
and the EDoc guide — reconciled and pressure-tested against a corpus of AI-generated
anti-patterns. Guides are split by topic into seventeen chapters. Each entry is a
numbered pattern with a strength indicator (MUST / SHOULD / CONSIDER / AVOID), a
one-line summary, paired `%% Good` / `%% Bad` Erlang snippets, a rationale, and
cross-references. Every chapter ends with a Summary Table and a Related Guidelines
list.

The target environment is **Erlang/OTP 27+**, with explicit call-outs where OTP 24
or 26 behaviour differs. The default build tool is **rebar3**, the default static
analysis is **dialyzer + xref**, the default style/format pair is **elvis + erlfmt**,
the default test stack is **eunit + common_test + PropEr**, and the default
documentation mechanism is **EDoc plus the OTP-27 `-doc` / `-moduledoc` attributes**.

## When to Use This Skill

Activate this skill when the task involves:

- Writing, refactoring, or reviewing Erlang code
- Designing module APIs, return conventions (`{ok, _}` / `{error, _}`), opaque types
- Modelling data: records vs maps, proplists, binaries/iolists, dialyzer typespecs
- Designing functions: clause/guard design, recursion, comprehensions, HOFs
- Designing processes and message protocols: spawn, selective receive, links, monitors
- Writing OTP behaviours: `gen_server`, `gen_statem`, `gen_event`
- Building supervision trees, applications, and releases
- Applying let-it-crash fault tolerance and error-kernel design
- Profiling and tuning on the BEAM: ETS, binary handling, memory, schedulers
- Diagnosing live systems: tracing, `recon`, crash-dump and memory-leak analysis, overload
- Writing tests: eunit, common_test, property-based tests with PropEr
- Documenting with EDoc and OTP-27 `-doc` attributes
- Running distributed Erlang: connectivity, registries, cookies, partitions
- Wiring the rebar3 / dialyzer / xref / elvis / erlfmt toolchain
- Triaging AI-generated Erlang for concurrency, fault-tolerance, and idiom regressions

## Document Locations

All guideline documents are in `knowledge/erlang/guides/`:

- `01-core-idioms.md` — Naming, module layout, comment levels, formatting, expression style
- `02-api-design.md` — Exported surfaces, return conventions, opaque types
- `03-error-handling.md` — Errors/exits/throws, `try`/`catch`, logging, error values
- `04-data-and-types.md` — Records, maps, proplists, binaries/iolists, dialyzer typespecs
- `05-functions-and-pattern-matching.md` — Clauses, guards, recursion, comprehensions, HOFs
- `06-processes-and-concurrency.md` — Spawn, messages, selective receive, links, monitors
- `07-otp-behaviours.md` — `gen_server`, `gen_statem`, `gen_event` contracts and callbacks
- `08-supervision-and-applications.md` — Supervisors, restart strategies, applications, releases
- `09-fault-tolerance.md` — Let-it-crash, error kernel, isolation, trapping exits
- `10-performance.md` — BEAM scheduling, ETS, binaries, memory, profiling
- `11-anti-patterns.md` — Concrete traps, each with a fix
- `12-project-structure.md` — rebar3 layout, OTP applications, umbrella projects, Hex
- `13-documentation.md` — EDoc and OTP-27 `-doc` / `-moduledoc` attributes, doc-tests
- `14-production-ops.md` — Tracing, recon, crash dumps, overload, live debugging
- `15-testing.md` — eunit, common_test, PropEr, mocking
- `16-distribution.md` — Distributed Erlang, registries, cookies, partitions
- `17-tooling.md` — rebar3, dialyzer, xref, elvis, erlfmt

**Supporting material:**

- `knowledge/erlang/sources/` — upstream sources by format (`md/` is the canonical extraction input)
- `knowledge/erlang/concept-cards/<source-slug>/` — single-pattern v3 cards distilled from each source
- `knowledge/erlang/extraction-metadata/` — competency questions, extraction logs, and `erlang-taxonomy.md` (categories, tiers, notation)
- `knowledge/erlang/tools/lint_examples.py` — enforces the GOOD/BAD example contract across guides
- `knowledge/erlang/workbench/PLAN.md` — build plan and phased roadmap

Guides are the normative artefact. Concept cards and sources are there when you need
the original wording, deeper rationale, or an edge-case example.

## Document Selection Guide

Anti-patterns (chapter 11) is the cheap safety net — load it first on any Erlang task.

| Task | Load These Documents |
|------|---------------------|
| **Any Erlang code** | `11-anti-patterns.md` (always load first) |
| **New code from scratch** | `11-anti-patterns.md`, `01-core-idioms.md`, `03-error-handling.md` |
| **API / module design** | `02-api-design.md`, `04-data-and-types.md` |
| **Error handling** | `03-error-handling.md`, `09-fault-tolerance.md` |
| **Data modelling / typespecs** | `04-data-and-types.md`, `17-tooling.md` (dialyzer) |
| **Functions, guards, matching** | `05-functions-and-pattern-matching.md` |
| **Processes / message protocols** | `06-processes-and-concurrency.md`, `09-fault-tolerance.md` |
| **OTP behaviour (gen_server etc.)** | `07-otp-behaviours.md`, `06-processes-and-concurrency.md` |
| **Supervision / applications / releases** | `08-supervision-and-applications.md`, `12-project-structure.md` |
| **Fault tolerance / let-it-crash** | `09-fault-tolerance.md`, `07-otp-behaviours.md` |
| **Performance / profiling** | `10-performance.md`, `14-production-ops.md` |
| **Diagnosing a live system** | `14-production-ops.md`, `10-performance.md` |
| **Testing** | `15-testing.md`, `03-error-handling.md` |
| **Documentation** | `13-documentation.md` |
| **Distributed Erlang** | `16-distribution.md`, `06-processes-and-concurrency.md` |
| **Project / build setup** | `12-project-structure.md`, `17-tooling.md` |
| **Code review / audit** | `11-anti-patterns.md`, then topic-specific |

## Critical Rules (Always Apply)

These should hold in ALL Erlang code without loading documents.

### Naming and comments

```erlang
%% Bad - CamelCase atom/function, single % for a function comment
% process the thing
processThing(X) -> doStuff(X).

%% Good - snake_case atoms/functions, CamelCase vars, %% for function comments
process_thing(Value) -> do_stuff(Value).
```

### Don't program defensively — let it crash

```erlang
%% Bad - defensive wrapping hides bugs and corrupts the error; returns nonsense on bad input
parse(Bin) ->
    try binary_to_integer(Bin) of
        N -> {ok, N}
    catch _:_ -> {ok, 0}        %% a parse failure silently becomes 0
    end.

%% Good - match what you expect; let unexpected input crash the (supervised) process
parse(Bin) -> {ok, binary_to_integer(Bin)}.
```

### Return conventions

```erlang
%% Bad - in-band sentinel; caller can't tell "not found" from a real value
lookup(Key, Map) -> maps:get(Key, Map, undefined).

%% Good - tagged tuple; the contract is explicit and matchable
-spec lookup(term(), map()) -> {ok, term()} | error.
lookup(Key, Map) ->
    case maps:find(Key, Map) of
        {ok, V} -> {ok, V};
        error   -> error
    end.
```

### Never build atoms from untrusted input

```erlang
%% Bad - atom table is bounded and never garbage-collected; this can crash the node
handle(Name) -> Pid = whereis(list_to_atom(Name)).

%% Good - keep dynamic keys as binaries; only use existing atoms
handle(Name) -> Pid = whereis(binary_to_existing_atom(Name, utf8)).
```

### Keep gen_server callbacks fast

```erlang
%% Bad - slow synchronous work inside handle_call serialises every client
handle_call({fetch, Url}, _From, State) ->
    {reply, slow_http_get(Url), State}.

%% Good - reply asynchronously; the server stays responsive
handle_call({fetch, Url}, From, State) ->
    spawn(fun() -> gen_server:reply(From, slow_http_get(Url)) end),
    {noreply, State}.
```

### Spec every exported function

```erlang
%% Good - dialyzer-checkable contract on every public function
-spec start_link(config()) -> {ok, pid()} | {error, term()}.
```

## Pattern ID Reference

| Prefix | Chapter |
|--------|---------|
| `ID`   | `01-core-idioms.md` |
| `API`  | `02-api-design.md` |
| `EH`   | `03-error-handling.md` |
| `DT`   | `04-data-and-types.md` |
| `FP`   | `05-functions-and-pattern-matching.md` |
| `PC`   | `06-processes-and-concurrency.md` |
| `BEH`  | `07-otp-behaviours.md` |
| `SUP`  | `08-supervision-and-applications.md` |
| `FT`   | `09-fault-tolerance.md` |
| `PF`   | `10-performance.md` |
| `AP`   | `11-anti-patterns.md` |
| `PS`   | `12-project-structure.md` |
| `DC`   | `13-documentation.md` |
| `OPS`  | `14-production-ops.md` |
| `TE`   | `15-testing.md` |
| `DIST` | `16-distribution.md` |
| `TL`   | `17-tooling.md` |

## Strength Indicators

| Indicator | Meaning | Action |
|-----------|---------|--------|
| **MUST** | Required for correctness, safety, or OTP-compliance | Always follow |
| **SHOULD** | Strong community/OTP convention | Follow unless specifically justified |
| **CONSIDER** | Context-dependent recommendation | Evaluate case by case |
| **AVOID** | Anti-pattern | Do not use |

The anti-patterns chapter (`11-anti-patterns.md`) uses **AVOID** on every entry.

## Integration Notes

- **Code blocks use `erlang` syntax** with the `%% Good` / `%% Bad` comment
  convention (Bad shown first). Shell snippets use `bash`, config uses `erlang`/`toml`.
- **Pattern IDs are `PREFIX-NN`** (e.g. `BEH-04`, `AP-12`); numbers are stable within a chapter.
- **Cross-references in-guide** use `See also: BEH-04, PC-09` style.
- **Each chapter ends with a Summary Table** and a Related Guidelines list.
- **Strength labels are uppercase bold** so they're greppable by severity.
- **`tools/lint_examples.py`** enforces that every pattern carries both a Good and a
  Bad example plus **Strength**/**Summary** — run it in CI / pre-commit.
- **OTP-27 features** (`-doc`/`-moduledoc`, `json`, `maybe`, sigils, process labels)
  are flagged inline where they appear, with the OTP 24/26 difference noted.
