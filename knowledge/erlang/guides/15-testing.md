# Testing

How to test Erlang: EUnit for fast unit tests, Common Test for integration and system tests, PropEr for property-based testing, fixtures for setup/teardown, and a discipline of testing the public API with fast, deterministic tests. Where tests live in the project is in `12-project-structure.md`; doctests on `-doc` examples are in `13-documentation.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the EUnit and Common Test user guides, Learn You Some Erlang (testing), Inaka guidelines, and the Erlang Programming Rules.

---

## TE-01: Use EUnit for Unit Tests

**Strength**: SHOULD

**Summary**: Write fast, in-process unit tests with EUnit; functions ending in `_test`/`_test_` are discovered automatically.

```erlang
%% Bad - "test" by hand in the shell and eyeball the result
%% 1> my_math:add(2, 2).   %% did that pass? who knows tomorrow

%% Good - an EUnit test the runner discovers and checks
-include_lib("eunit/include/eunit.hrl").

add_test() ->
    ?assertEqual(4, my_math:add(2, 2)).
%% $ rebar3 eunit
```

**Rationale**: EUnit is the lightweight, built-in unit-test framework: a function named `name_test/0` is a test, `name_test_/0` is a test *generator*, and `rebar3 eunit` finds and runs them. Codifying expectations as tests makes them repeatable and regression-proof, unlike shell experiments that are forgotten the moment the shell closes.

**See also**: TE-02, TE-03, `13-documentation.md` (DC-07)

---

## TE-02: Assert with the EUnit Macros

**Strength**: SHOULD

**Summary**: Use `?assertEqual`, `?assertMatch`, `?assertError`, etc.; they produce informative failure messages.

```erlang
%% Bad - a bare match as the "assertion": failure just says badmatch, no expected/actual
ok_test() -> {ok, 4} = my_math:checked_add(2, 2).

%% Good - assertion macros report expected vs actual on failure
checked_add_test() ->
    ?assertEqual({ok, 4}, my_math:checked_add(2, 2)),
    ?assertMatch({ok, _}, my_math:checked_add(1, 1)),
    ?assertError(badarith, my_math:add(1, a)).
```

**Rationale**: The assertion macros (`?assertEqual/2`, `?assertMatch/2`, `?assertError/2`, `?assertExit/2`, `?assertThrow/2`) capture the expression, the expected value, and the line, so a failure tells you *what* differed and *where*. A bare `=` match only raises `badmatch` with no context, making failures slow to diagnose.

**See also**: TE-01, TE-04

---

## TE-03: Name and Place Tests Conventionally

**Strength**: SHOULD

**Summary**: Put unit tests in `test/` (or a `_tests` companion module) and CT suites as `*_SUITE.erl`; keep tests out of `src/`.

```erlang
%% Bad - tests interleaved in the production module, shipped and analysed as production code
%% src/my_math.erl  contains add/2 AND add_test/0

%% Good - tests beside the code under test/, named by convention
%% src/my_math.erl
%% test/my_math_tests.erl     (EUnit)
%% test/my_math_SUITE.erl     (Common Test)
```

**Rationale**: Keeping tests in `test/` (compiled only under the test profile, PS-08) keeps them out of the production release and out of production xref/dialyzer. The naming conventions — `_tests.erl` modules, `_test`/`_test_` functions, `_SUITE.erl` suites — are what the runners discover automatically.

**See also**: TE-01, `12-project-structure.md` (PS-08)

---

## TE-04: Use Fixtures for Setup and Teardown

**Strength**: SHOULD

**Summary**: When a test needs state set up and torn down, use an EUnit fixture (`{setup, Setup, Cleanup, Tests}`) so cleanup runs even on failure.

```erlang
%% Bad - set up and tear down inline; a failing assertion skips the cleanup, leaking state
db_test() ->
    {ok, Pid} = my_db:start_link(),
    ?assertEqual(ok, my_db:put(Pid, k, v)),   %% if this fails, the db is never stopped
    my_db:stop(Pid).

%% Good - a fixture guarantees teardown
db_test_() ->
    {setup,
     fun() -> {ok, Pid} = my_db:start_link(), Pid end,   %% setup
     fun(Pid) -> my_db:stop(Pid) end,                    %% cleanup, always runs
     fun(Pid) -> [?_assertEqual(ok, my_db:put(Pid, k, v))] end}.
```

**Rationale**: A fixture separates setup, the cleanup that must run regardless of outcome, and the tests themselves. Inline teardown after assertions is skipped when an assertion fails, leaking processes, ports, or ETS tables into later tests. Fixtures keep tests isolated and repeatable.

**See also**: TE-05, TE-12

---

## TE-05: Generate Data-Driven Tests with Test Generators

**Strength**: CONSIDER

**Summary**: Use `_test_` generator functions returning a list of `?_assert*` instances to run the same logic over many cases.

```erlang
%% Bad - copy-paste a near-identical test per case
add_0_test() -> ?assertEqual(0, my_math:add(0, 0)).
add_1_test() -> ?assertEqual(2, my_math:add(1, 1)).
add_2_test() -> ?assertEqual(5, my_math:add(2, 3)).

%% Good - a generator builds one assertion per data row
add_cases_test_() ->
    [?_assertEqual(Want, my_math:add(A, B)) || {A, B, Want} <-
        [{0, 0, 0}, {1, 1, 2}, {2, 3, 5}]].
```

**Rationale**: A test generator (`_test_`, returning test instances built with the `?_assert*` forms) lets you table-drive cases instead of duplicating a test body, so adding a case is one line and each case still reports independently. It's the EUnit analogue of Go/Rust table-driven tests.

**See also**: TE-04, TE-09

---

## TE-06: Use Common Test for Integration and System Tests

**Strength**: SHOULD

**Summary**: Test multi-process, stateful, or whole-application behaviour with Common Test suites, not EUnit.

```erlang
%% Bad - drive a full application's lifecycle from a single EUnit test with sleeps
app_test() -> application:start(my_app), timer:sleep(1000), ?assert(running()).

%% Good - a Common Test suite with proper init/end hooks
-module(my_app_SUITE).
-export([all/0, init_per_suite/1, end_per_suite/1, smoke/1]).
all() -> [smoke].
init_per_suite(Cfg) -> {ok, _} = application:ensure_all_started(my_app), Cfg.
end_per_suite(_Cfg) -> ok = application:stop(my_app).
smoke(_Cfg) -> {ok, _} = my_app:ping().
%% $ rebar3 ct
```

**Rationale**: Common Test is built for integration/system testing — it manages suites, configuration, logging (HTML reports), and the lifecycle of applications and external resources. EUnit is for fast, in-process unit tests; pushing whole-system scenarios (with `sleep`-based synchronisation) into it produces slow, flaky tests.

**See also**: TE-07, TE-11

---

## TE-07: Structure CT into Suites, Groups, and Hooks

**Strength**: SHOULD

**Summary**: Organise Common Test with `all/0`, test groups, and `init/end_per_suite`/`per_group`/`per_testcase` hooks for shared setup.

```erlang
%% Bad - one giant test case doing setup, several scenarios, and teardown inline

%% Good - groups + lifecycle hooks scope setup to where it's needed
all() -> [{group, crud}].
groups() -> [{crud, [parallel], [create, read, update, delete]}].
init_per_group(crud, Cfg) -> [{conn, connect()} | Cfg].
end_per_group(crud, Cfg) -> disconnect(?config(conn, Cfg)).
create(Cfg) -> ?assertMatch({ok, _}, store:create(?config(conn, Cfg), item)).
```

**Rationale**: Groups let you scope setup/teardown to a set of related cases and run independent cases in `parallel`; the per-suite/group/testcase hooks put expensive setup (starting apps, opening connections) at the right granularity. This keeps each case focused on one scenario and shares fixtures cleanly via the `Config`.

**See also**: TE-06, TE-08

---

## TE-08: Keep CT Test Data in the `data_dir`

**Strength**: CONSIDER

**Summary**: Read fixture files from the suite's `data_dir` (resolved via `?config(data_dir, Config)`), not from hardcoded paths.

```erlang
%% Bad - hardcode a path to a fixture file relative to the cwd
parse(_Cfg) -> {ok, B} = file:read_file("test/my_SUITE_data/sample.json"), ...

%% Good - resolve the suite's data_dir from the Config
parse(Cfg) ->
    File = filename:join(?config(data_dir, Cfg), "sample.json"),
    {ok, B} = file:read_file(File).
%% files live in test/my_SUITE_data/
```

**Rationale**: Common Test gives each suite a `data_dir` (`<suite>_data/`) and exposes it through the `Config`; reading fixtures from there makes the suite runnable regardless of the working directory the runner uses. Hardcoded relative paths break under `rebar3 ct`, CI, or release-style layouts.

**See also**: TE-07, `12-project-structure.md` (PS-03)

---

## TE-09: Test Invariants with PropEr (Property-Based Testing)

**Strength**: CONSIDER

**Summary**: For logic with general invariants, write properties over generated inputs with PropEr instead of (or alongside) example-based tests.

```erlang
%% Bad - a handful of hand-picked examples that miss edge cases
rev_test() -> ?assertEqual([3,2,1], lists:reverse([1,2,3])).

%% Good - a property checked over many generated inputs
-include_lib("proper/include/proper.hrl").

prop_reverse_twice_is_identity() ->
    ?FORALL(L, list(integer()),
            lists:reverse(lists:reverse(L)) =:= L).
%% $ rebar3 proper
```

**Rationale**: Property-based testing states a general truth ("reversing twice is the identity") and lets PropEr generate hundreds of inputs — including the awkward edge cases hand-written examples miss — and *shrink* a failing case to a minimal counterexample. It excels for parsers, serializers, and stateful models. Use it where invariants exist; keep example tests for specific known cases.

**See also**: TE-05, TE-11

---

## TE-10: Measure Coverage, but Don't Chase 100%

**Strength**: CONSIDER

**Summary**: Use `cover` (via `rebar3 eunit --cover` / `ct --cover`) to find untested code, treating coverage as a guide, not a target.

```erlang
%% Bad - write vacuous tests purely to push a coverage number to 100%
just_call_it_test() -> _ = my_mod:complex_thing(), ?assert(true).   %% asserts nothing

%% Good - use coverage to find gaps; write meaningful tests for the important ones
%% $ rebar3 eunit --cover && rebar3 cover
%% (inspect which branches are untested; test the ones that matter)
```

**Rationale**: Coverage reveals code no test exercises, which is genuinely useful for finding blind spots. But coverage measures *execution*, not *verification* — a test that runs code without asserting anything raises the number without adding value. Aim for meaningful coverage of important paths, not a vanity 100%.

**See also**: TE-02, TE-09

---

## TE-11: Test the Public API; Observe Outputs, Not Internals

**Strength**: SHOULD

**Summary**: Prefer black-box tests through the public interface; integration tests should assert on observable behaviour, not internal state.

```erlang
%% Bad - reach into internals: assert on a record field / private process state
?assertEqual(5, element(2, sys:get_state(counter))).   %% couples the test to the layout

%% Good - exercise the public API and assert on what it returns
ok = counter:increment(C),
?assertEqual(5, counter:value(C)).
```

**Rationale**: Tests coupled to internal representation break on every refactor even when behaviour is unchanged, discouraging the refactoring (DT-04/API-04) that internals exist to allow. Driving the public API and asserting on its results tests the contract that actually matters and survives implementation changes. Integration tests in particular should observe the system the way a real client does.

**See also**: TE-06, TE-09, `02-api-design.md` (API-04)

---

## TE-12: Keep Tests Fast and Deterministic — No `sleep` for Synchronisation

**Strength**: SHOULD

**Summary**: Don't synchronise tests with `timer:sleep/1`; wait on an actual signal (a monitor, a reply, a poll with timeout).

```erlang
%% Bad - sleep and hope the async work finished: flaky and slow
worker:start_job(W),
timer:sleep(500),
?assertEqual(done, worker:status(W)).

%% Good - wait for a deterministic signal
Ref = monitor(process, W),
worker:start_job(W),
receive {job_done, W} -> ok after 5000 -> error(timeout) end,
?assertEqual(done, worker:status(W)).
```

**Rationale**: A fixed `sleep` is simultaneously too long (slowing the whole suite) and too short (flaking under load or in CI). Synchronising on a real event — a monitor `'DOWN'`, an expected message, or a bounded poll — makes tests both fast and reliable. Flaky tests erode trust in the suite until people ignore failures.

**See also**: TE-04, `06-processes-and-concurrency.md` (PC-10)

---

## TE-13: Keep Test Scaffolding Out of Production Code

**Strength**: SHOULD

**Summary**: Don't add test-only hooks, mocks, or debug output to `src/`; keep mocking (e.g. `meck`) and helpers in `test/`.

```erlang
%% Bad - a test-only branch baked into production code
charge(I) ->
    case application:get_env(my_app, test_mode, false) of
        true  -> ok;                 %% skip the real charge "for tests"
        false -> real_charge(I)
    end.

%% Good - production code stays clean; tests mock the boundary in test/
%% test/billing_tests.erl:
%%   meck:new(payments, [passthrough]),
%%   meck:expect(payments, charge, fun(_) -> ok end),
%%   ... meck:unload(payments).
charge(I) -> payments:charge(I).
```

**Rationale**: Test-mode branches in production code add untested paths, risk shipping the wrong behaviour, and entangle the contract with the test harness. Keep the production path single and honest (OPS-01); isolate boundaries with a mocking library like `meck` from the test module, and unload it in teardown (TE-04).

**See also**: TE-04, TE-11, `14-production-ops.md` (OPS-01)

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| TE-01 EUnit for unit tests | SHOULD | Codify expectations; `_test`/`_test_` discovered |
| TE-02 Assertion macros | SHOULD | Informative failures (expected vs actual) |
| TE-03 Name/place tests | SHOULD | `test/`, `_tests.erl`, `*_SUITE.erl` |
| TE-04 Fixtures | SHOULD | Setup/cleanup that runs even on failure |
| TE-05 Test generators | CONSIDER | Table-drive cases with `_test_` |
| TE-06 Common Test | SHOULD | Integration/system tests, not EUnit |
| TE-07 Suites/groups/hooks | SHOULD | Scope setup; run independent cases parallel |
| TE-08 CT `data_dir` | CONSIDER | Resolve fixtures via `?config(data_dir, _)` |
| TE-09 PropEr | CONSIDER | Properties + shrinking find edge cases |
| TE-10 Coverage as a guide | CONSIDER | Find gaps; don't chase 100% |
| TE-11 Test the public API | SHOULD | Observe behaviour, not internals |
| TE-12 No `sleep` sync | SHOULD | Wait on a signal; deterministic + fast |
| TE-13 Scaffolding out of `src/` | SHOULD | Mock from `test/`; no test-mode branches |

## Related Guidelines

- **Project structure**: See `12-project-structure.md` (PS-08) for keeping tests in `test/` and test-only deps under the test profile.
- **Documentation**: See `13-documentation.md` (DC-07) for testable doc examples (`ct_doctest`).
- **API design / data**: See `02-api-design.md` (API-04) and `04-data-and-types.md` (DT-04) — black-box testing depends on hidden internals.
- **Processes & concurrency**: See `06-processes-and-concurrency.md` (PC-10) for the monitor/ref synchronisation TE-12 uses.
- **Production ops**: See `14-production-ops.md` (OPS-01) — the no-debug-in-`src/` rule TE-13 extends.

## External References

- [EUnit User's Guide](https://www.erlang.org/doc/apps/eunit/chapter.html)
- [Common Test User's Guide](https://www.erlang.org/doc/apps/common_test/basics_chapter.html)
- [PropEr](https://proper-testing.github.io/) — property-based testing
- [meck](https://github.com/eproxus/meck) — mocking
- *Learn You Some Erlang* — EUnit and Common Test chapters
