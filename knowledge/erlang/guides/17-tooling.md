# Tooling

The day-to-day Erlang toolchain and the loop that ties it together: `rebar3` to build, `dialyzer` for static discrepancy analysis, `xref` for call-graph checks, `erlfmt` to format, `elvis` to lint, the right profiler when you need one, and treating all of it as CI gates. The build/release/dependency side overlaps `12-project-structure.md`; the type language `dialyzer` consumes is in `04-data-and-types.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: Programming Erlang (Types, cross-referencing), the Dialyzer/xref documentation, Designing for Scalability with Erlang/OTP (rebar3), and Inaka guidelines.

---

## TL-01: Run Dialyzer (and Build a PLT Once)

**Strength**: SHOULD

**Summary**: Use Dialyzer to find type and logic discrepancies; build the persistent lookup table (PLT) once, then run it routinely.

```erlang
%% Bad - never run static analysis; discover type mismatches only at runtime in production

%% Good - build the PLT once, then analyse on every change
%% $ rebar3 dialyzer        (rebar3 builds/caches the PLT and runs dialyzer)
%% or raw:
%% $ dialyzer --build_plt --apps erts kernel stdlib
%% $ dialyzer --src src/
```

**Rationale**: Dialyzer ("DIscrepancy AnaLYZer") "finds discrepancies in Erlang code" and is conservative — "if it complains, then there really is an inconsistency" (Programming Erlang). It needs a PLT (a cached analysis of the standard libraries) built once. `rebar3 dialyzer` manages the PLT for you; running it routinely catches mismatched calls, dead clauses, and contract violations before they ship.

**See also**: TL-02, TL-03, `04-data-and-types.md` (DT-18)

---

## TL-02: Understand Dialyzer as Success Typing — Not Soundness

**Strength**: CONSIDER

**Summary**: Dialyzer reports no false positives but does miss real errors; a clean run is strong evidence, not proof of correctness.

```erlang
%% Bad - treat a green Dialyzer run as "the types are proven correct" and skip tests

%% Good - use Dialyzer as a zero-false-positive gate AND keep tests for behaviour
%% a clean `rebar3 dialyzer` means "no provable discrepancies", not "no bugs"
```

**Rationale**: Dialyzer computes *success typings* — the types under which a function *can* succeed — and flags a call only when it *cannot* match (Programming Erlang). That makes it conservative (no false alarms, so every warning is real and worth fixing) but incomplete: a permissive success typing lets logically-wrong calls through. Enforce it, but pair it with tests (chapter 15); it is a discrepancy finder, not a proof system (DT-18).

**See also**: TL-01, TL-03, `15-testing.md`

---

## TL-03: Add Specs and Types to Strengthen Analysis

**Strength**: SHOULD

**Summary**: Dialyzer works with no annotations, but `-spec`/`-type` make its analysis sharper; add them, especially on exported functions.

```erlang
%% Bad - no specs, so Dialyzer can only infer permissive success typings and misses misuse
get(K, M) -> maps:get(K, M).

%% Good - specs narrow the contract Dialyzer propagates to callers
-spec get(atom(), map()) -> {ok, term()} | error.
get(K, M) -> case maps:find(K, M) of {ok, V} -> {ok, V}; error -> error end.
```

**Rationale**: Annotations "improve the quality of [Dialyzer's] analysis" (Programming Erlang). Without specs, Dialyzer infers the widest types that could succeed and so catches less; an explicit `-spec` gives it a tighter contract to check every call site against (DT-16/API-07). Specs are the highest-leverage way to make Dialyzer find more real bugs.

**See also**: TL-01, `04-data-and-types.md` (DT-16), `02-api-design.md` (API-07)

---

## TL-04: Run `xref` to Check the Call Graph

**Strength**: SHOULD

**Summary**: Use `xref` to find calls to missing functions, unused exports, and deprecated calls; compile with `debug_info`.

```erlang
%% Bad - rename/remove a function and find the broken callers only at runtime

%% Good - xref reports missing/unused/deprecated calls across the project
%% $ rebar3 xref
%% (raw: xref:d('.') on debug_info-compiled beams -> undefined/unused/deprecated lists)
```

**Rationale**: Cross-reference analysis "finds out whether we have any missing code and who calls what… it detects calls to functions that do not exist" and works on `debug_info`-compiled code (Programming Erlang). `rebar3 xref` surfaces undefined-function calls, unused exports, and deprecated-API usage across the whole project — and it's exactly why ID-13 forbids dynamic calls (which xref can't see).

**See also**: TL-12, `01-core-idioms.md` (ID-13)

---

## TL-05: Format Code with `erlfmt`

**Strength**: SHOULD

**Summary**: Let `erlfmt` enforce layout mechanically; don't hand-format or argue about whitespace in review.

```erlang
%% Bad - hand-format every file to personal taste; review comments about commas and indentation
total(A,B)->A+B.

%% Good - run the formatter; layout is deterministic and not a review topic
%% $ rebar3 fmt        (erlfmt; check in CI with `rebar3 fmt --check`)
total(A, B) -> A + B.
```

**Rationale**: A formatter makes layout deterministic and removes whitespace debates from code review, which is the mechanical backstop behind the style rules in chapter 01 (ID-03/ID-04/ID-05). Run it on save and as a `--check` gate in CI so every file is consistent regardless of who wrote it.

**See also**: TL-06, TL-09, `01-core-idioms.md` (ID-05)

---

## TL-06: Lint with `elvis`

**Strength**: CONSIDER

**Summary**: Use `elvis` to enforce style/structure rules (line length, nesting depth, `god` modules, naming) that a formatter doesn't.

```erlang
%% Bad - rely on review alone to catch deep nesting, huge modules, dynamic calls

%% Good - codify the rules in elvis.config and run them automatically
%% $ rebar3 lint     (or elvis rock)
%% rules: line_length, no_nested_try_catch, no_god_modules, module/function naming, ...
```

**Rationale**: `elvis` is the Erlang style reviewer; it mechanically checks many of the conventions in chapters 01–03 (nesting depth ID-08, god modules API-11, naming ID-01, no nested try EH-08) that formatting alone can't enforce. Encoding them in `elvis.config` and running in CI keeps the codebase consistent without relying on human reviewers to remember every rule.

**See also**: TL-05, TL-09, `01-core-idioms.md`

---

## TL-07: Drive Everything with `rebar3`

**Strength**: SHOULD

**Summary**: Use `rebar3` as the single entry point for compiling, testing, analysing, and releasing — with plugins for the rest.

```erlang
%% Bad - a different ad-hoc command (and remembered flag set) for each task

%% Good - one tool, consistent commands, configured in rebar.config
%% $ rebar3 compile | eunit | ct | dialyzer | xref | fmt | release
%% {project_plugins, [erlfmt, rebar3_lint, rebar3_proper]}.
```

**Rationale**: `rebar3` is the recommended general build tool (Designing for Scalability) and the common front end for the whole toolchain — compilation, deps, EUnit/CT, Dialyzer, xref, releases (via relx) — extended by plugins (erlfmt, elvis/lint, proper). One consistent interface (also what CI runs) beats a pile of bespoke scripts.

**See also**: TL-08, TL-09, `12-project-structure.md` (PS-04)

---

## TL-08: Compile with Warnings as Errors and Useful Options

**Strength**: SHOULD

**Summary**: Turn compiler warnings into errors and keep `debug_info` on, so problems fail the build instead of being ignored.

```erlang
%% Bad - tolerate a wall of warnings; real ones (unused vars, unmatched returns) get lost in the noise

%% Good - warnings_as_errors plus debug_info (rebar.config)
{erl_opts, [debug_info, warnings_as_errors, warn_unused_import,
            warn_export_vars, warn_missing_spec]}.
```

**Rationale**: Compiler warnings flag real problems — unused variables (ID-11), unmatched returns, shadowed bindings — but a noisy build trains people to ignore them. `warnings_as_errors` keeps the warning count at zero by making each one fail the build; `debug_info` is required by xref (TL-04), Dialyzer, and tracing. Opt into the stricter `warn_*` flags that match your conventions.

**See also**: TL-04, TL-09

---

## TL-09: Make the Whole Loop a CI Gate

**Strength**: SHOULD

**Summary**: Run compile → format-check → xref → dialyzer → eunit/ct in CI on every change, and fail the build on any of them.

```erlang
%% Bad - run tools occasionally on a developer's laptop; merge whatever compiles

%% Good - one pipeline gates every merge
%% $ rebar3 fmt --check
%% $ rebar3 compile        (warnings_as_errors)
%% $ rebar3 xref
%% $ rebar3 dialyzer
%% $ rebar3 eunit && rebar3 ct
```

**Rationale**: Tools only help if they run consistently; a check that's optional is a check that rots. Wiring format, compile, xref, Dialyzer, and tests into CI as required gates means every merged change is formatted, warning-free, call-graph-clean, discrepancy-free, and tested — turning the conventions throughout this skill from advice into enforced policy.

**See also**: TL-05, TL-07, TL-08

---

## TL-10: Use `escript` for Small Standalone Tools

**Strength**: CONSIDER

**Summary**: Write small CLI utilities and scripts as `escript`s rather than spinning up a full application/release.

```erlang
%% Bad - build a whole OTP release just to run a one-shot maintenance script

%% Good - an escript: a single executable Erlang script
#!/usr/bin/env escript
main(Args) ->
    io:format("processing ~p~n", [Args]),
    ok.
%% $ ./tool.escript foo bar
```

**Rationale**: `escript` runs an Erlang source file as a script with a `main/1` entry point — ideal for build helpers, data-munging, and one-off maintenance tools where a full application and release would be overkill. (It is also the one place the "no `io:format` in production" rule, OPS-01, doesn't apply — escripts are CLIs.)

**See also**: TL-07, `14-production-ops.md` (OPS-01)

---

## TL-11: Reach for the Right Profiler

**Strength**: CONSIDER

**Summary**: Match the profiler to the question — `tprof`/`eprof` for call time/counts, `fprof` for detailed call graphs, `lcnt` for lock contention, `recon` on live nodes.

```erlang
%% Bad - sprinkle timer:tc/1 everywhere and eyeball the numbers

%% Good - use the tool that answers your question
%% tprof / eprof : where is time spent across function calls?
%% fprof         : detailed (slow) call-graph timing
%% lcnt          : lock contention across schedulers
%% recon         : profile/inspect a live production node (chapter 14)
```

**Rationale**: Each profiler has a different cost/detail trade-off: `eprof`/`tprof` give call-time/count summaries cheaply, `fprof` gives a detailed call graph but slows the system significantly, `lcnt` finds scheduler lock contention, and `recon` is the production-safe choice. Picking the right one (after PF-01 says *where* to look) gets you the answer without distorting it.

**See also**: TL-07, `10-performance.md` (PF-01), `14-production-ops.md`

---

## TL-12: Keep the Module Dependency Graph Acyclic

**Strength**: CONSIDER

**Summary**: Use `xref` (and design) to keep modules from forming circular dependencies; cycles can't be understood or tested in isolation.

```erlang
%% Bad - a <-> b mutual dependency: neither module can be reasoned about or tested alone
%% a.erl calls b:f(); b.erl calls a:g()

%% Good - a one-directional layering xref can confirm
%% a.erl calls b:f(); b.erl depends only on modules "below" it
%% periodically check the call graph with rebar3 xref
```

**Rationale**: Circular module dependencies (API-12) make each module impossible to compile-test or understand on its own and tend to indicate muddled responsibilities. `xref` can surface the call graph so you can spot and break cycles, keeping the dependency structure a tree (or at least a DAG) — easier to reason about, refactor, and reuse.

**See also**: TL-04, `02-api-design.md` (API-12)

---

## TL-13: Integrate Foreign Code via Ports First, NIFs with Care

**Strength**: CONSIDER

**Summary**: Talk to non-Erlang code through a port (isolated OS process) by default; use a NIF only when you need in-VM speed, and keep it short or dirty-scheduled.

```erlang
%% Bad - implement a slow C routine as a plain NIF that blocks its scheduler for the whole call

%% Good - default to a port (crash-isolated); reserve NIFs for short, hot, in-VM work
Port = open_port({spawn_executable, code:priv_dir(my_app) ++ "/helper"},
                 [{packet, 4}, binary]),
Port ! {self(), {command, Request}}.
%% NIFs: keep under ~1ms or use enif_schedule_nif / dirty schedulers (PF-16)
```

**Rationale**: A port runs foreign code in a separate OS process, so a crash there can't take the VM down — the safe default for integrating external programs. A NIF runs native code *inside* the VM (fast, but a crash or a long call corrupts/stalls a scheduler, PF-16). Choose the port for isolation; reach for a NIF only when in-VM performance is essential, and then keep it brief or dirty-scheduled.

**See also**: TL-10, `10-performance.md` (PF-16), `09-fault-tolerance.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| TL-01 Run Dialyzer | SHOULD | Discrepancy analysis; PLT built once |
| TL-02 Success typing | CONSIDER | No false positives, but not soundness |
| TL-03 Specs strengthen it | SHOULD | `-spec`/`-type` make Dialyzer find more |
| TL-04 Run `xref` | SHOULD | Missing/unused/deprecated calls (`debug_info`) |
| TL-05 `erlfmt` | SHOULD | Deterministic layout; no whitespace debates |
| TL-06 `elvis` | CONSIDER | Lint the rules a formatter can't |
| TL-07 Drive with `rebar3` | SHOULD | One front end for build/test/analyse/release |
| TL-08 Warnings as errors | SHOULD | Zero-warning builds; keep `debug_info` |
| TL-09 CI gate the loop | SHOULD | fmt → compile → xref → dialyzer → tests |
| TL-10 `escript` | CONSIDER | Small CLIs without a full release |
| TL-11 Right profiler | CONSIDER | tprof/eprof/fprof/lcnt/recon for the question |
| TL-12 Acyclic deps | CONSIDER | `xref` to find and break module cycles |
| TL-13 Ports before NIFs | CONSIDER | Isolate foreign code; NIFs short/dirty |

## Related Guidelines

- **Data & types**: See `04-data-and-types.md` — `-spec`/`-type` (DT-16) feed Dialyzer; success typing is DT-18.
- **Project structure**: See `12-project-structure.md` — rebar3 as build tool (PS-04), profiles, releases, locked deps.
- **Core idioms**: See `01-core-idioms.md` — formatting (ID-03/05), no dynamic calls (ID-13, why xref works), and the style rules elvis enforces.
- **Performance**: See `10-performance.md` — profiling (PF-01) and NIF discipline (PF-16) behind TL-11/TL-13.
- **Testing**: See `15-testing.md` — the EUnit/CT/PropEr runs the CI loop (TL-09) includes.

## External References

- [Dialyzer](https://www.erlang.org/doc/apps/dialyzer/dialyzer_chapter.html) and [Typer/specs](https://www.erlang.org/doc/system/typespec.html)
- [Tools — xref](https://www.erlang.org/doc/apps/tools/xref_chapter.html)
- [erlfmt](https://github.com/WhatsApp/erlfmt) · [elvis](https://github.com/inaka/elvis)
- [rebar3](https://rebar3.org/docs/)
- *Programming Erlang* (Joe Armstrong) — Types (Dialyzer, success typing), cross-reference analysis
