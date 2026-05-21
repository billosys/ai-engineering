# Project Structure

How to lay out an Erlang project: OTP applications as the unit of code, the standard application directory layout, `rebar3` for building and dependencies, locked dependencies, umbrella projects for multi-app systems, releases via `relx`, and version control. The supervision/application *runtime* model is in `08-supervision-and-applications.md`; the build/analysis tooling is in `17-tooling.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the OTP Design Principles (Applications, Releases), Inaka guidelines (dependencies), the Erlang Programming Rules (§8.12), Designing for Scalability with Erlang/OTP, and Erlang and OTP in Action.

---

## PS-01: Structure Code as OTP Applications

**Strength**: SHOULD

**Summary**: The unit of organisation is the OTP application — a callback module plus an `.app` resource file — not a loose pile of modules.

```erlang
%% Bad - loose modules on the code path; nothing defines the unit, its deps, or its version
%% src/foo.erl, src/util.erl, src/server.erl  (no .app file)

%% Good - an OTP application with a resource file
%% src/my_app.app.src:
{application, my_app,
 [{description, "My app"}, {vsn, "0.1.0"},
  {applications, [kernel, stdlib]},
  {mod, {my_app_app, []}}]}.
```

**Rationale**: An application can be started/stopped as a unit, declares its dependencies and version, and is what releases and dependency resolution operate on (SUP-11). Organising by application gives the project a spine; loose modules have no boundary, no dependency declaration, and can't be packaged or released cleanly.

**See also**: PS-02, PS-13, `08-supervision-and-applications.md` (SUP-11)

---

## PS-02: Follow the Standard Application Directory Layout

**Strength**: SHOULD

**Summary**: Use the conventional directories — `src/`, `include/`, `priv/`, `test/`, with `ebin/` produced by the build.

```erlang
%% Bad - ad-hoc layout the tools don't recognise
%% code/, headers/, compiled/   (rebar3/OTP won't find these)

%% Good - the conventional OTP/rebar3 layout
%% my_app/
%%   src/        *.erl, my_app.app.src
%%   include/    *.hrl
%%   priv/       non-Erlang resources
%%   test/       *_SUITE.erl, *_tests.erl
%%   rebar.config
%%   (_build/ and ebin/ are generated)
```

**Rationale**: "When packaging code using systools, the code for each application is placed in `lib/Application-Vsn`" with `ebin` holding the `.beam` and `.app` files (OTP Design Principles). `rebar3` and OTP both assume `src`/`include`/`priv`/`ebin`; following the layout means the tools, releases, and other developers all find things where expected.

**See also**: PS-03, PS-04, PS-08

---

## PS-03: Put Non-Erlang Resources in `priv/`

**Strength**: SHOULD

**Summary**: Data files, port programs, NIF shared objects, and templates go in `priv/`; locate them at runtime with `code:priv_dir/1`.

```erlang
%% Bad - hardcode a path to a resource relative to the cwd
File = "priv/data.csv".            %% breaks once the app is released/installed elsewhere

%% Good - resolve priv/ via the code path, wherever the app is installed
File = filename:join(code:priv_dir(my_app), "data.csv").
```

**Rationale**: "The normal location for external programs… is the `priv` directory; `code:priv_dir/1` returns the `priv` directory of any application by searching the code path" (Erlang and OTP in Action). A relative path assumes a working directory that won't hold once the app is one of many under `lib/` in a release. `code:priv_dir/1` is location-independent.

**See also**: PS-02, `17-tooling.md`

---

## PS-04: Use rebar3 as the Build Tool

**Strength**: SHOULD

**Summary**: Drive compilation, dependencies, tests, and releases with `rebar3`.

```erlang
%% Bad - hand-rolled compilation and ad-hoc dependency fetching
%% erlc -o ebin src/*.erl ; git clone ... deps by hand

%% Good - rebar3 with a rebar.config
%% $ rebar3 compile | eunit | ct | dialyzer | release
%% rebar.config drives all of it
```

**Rationale**: rebar3 is "the recommended tool for greenfield projects" (Designing for Scalability) — it handles compilation, dependency management, test running, and release generation (via `relx`), and is extensible with plugins. Hand-rolled builds reinvent dependency resolution and release assembly, usually incompletely.

**See also**: PS-05, PS-09, `17-tooling.md` (TL-07)

---

## PS-05: Configure the Project in `rebar.config`

**Strength**: SHOULD

**Summary**: Declare dependencies, compiler options, profiles, and release config in `rebar.config`.

```erlang
%% Bad - scatter settings across ad-hoc scripts and environment variables

%% Good - one rebar.config with the project's build settings
{erl_opts, [debug_info, warnings_as_errors]}.
{deps, [{cowboy, "2.10.0"}]}.
{profiles, [{test, [{deps, [{proper, "1.4.0"}]}]}]}.
{relx, [{release, {my_app, "0.1.0"}, [my_app, sasl]}]}.
```

**Rationale**: `rebar.config` is the single, version-controlled source of truth for how the project builds: `erl_opts` (compiler flags), `deps`, `profiles` (per-environment overrides, PS-10), and `relx` (release spec). Centralising it makes builds reproducible and reviewable.

**See also**: PS-04, PS-06, PS-10

---

## PS-06: Lock Dependencies to a Tag or Commit

**Strength**: SHOULD

**Summary**: Pin every dependency to an immutable tag or commit (and commit `rebar.lock`); never depend on a moving branch.

```erlang
%% Bad - depend on a moving branch: the build changes underneath you
{deps, [{mylib, {git, "https://github.com/x/mylib.git", {branch, "master"}}}]}.

%% Good - pin to a tag (or commit); commit rebar.lock for reproducibility
{deps, [{mylib, {git, "https://github.com/x/mylib.git", {tag, "1.2.0"}}}]}.
%% (Hex deps pin by version: {mylib, "1.2.0"})
```

**Rationale**: "Specify a tag or commit, but not master" (Inaka). A branch reference means a dependency's content can change without any change on your side, breaking reproducibility and making "works on my machine" bugs. A pinned ref plus the committed `rebar.lock` guarantees everyone (and CI) builds the same tree.

**See also**: PS-05, PS-12, PS-14

---

## PS-07: Use an Umbrella Project for Multi-Application Systems

**Strength**: CONSIDER

**Summary**: For a system of several applications, use a rebar3 umbrella with each app under `apps/`.

```erlang
%% Bad - cram several distinct responsibilities into one giant application

%% Good - an umbrella project, one application per responsibility
%% my_system/
%%   apps/
%%     web/      (src/, web.app.src)
%%     core/     (src/, core.app.src)
%%     storage/  (src/, storage.app.src)
%%   rebar.config
```

**Rationale**: An umbrella keeps each application a clean, separately-versioned unit with its own deps and supervision tree, while building and releasing them together. It is the project-level expression of "one responsibility per module/app" (ID-10/API-11/SUP-15). For a single cohesive library, a flat single-app project is simpler — don't over-structure.

**See also**: PS-01, PS-13, `08-supervision-and-applications.md` (SUP-15)

---

## PS-08: Keep Tests in `test/`, Separate from `src/`

**Strength**: SHOULD

**Summary**: Test suites and test helpers live in `test/`, not mixed into `src/`.

```erlang
%% Bad - test code in src/, shipped in the release and analysed as production code
%% src/my_thing.erl
%% src/my_thing_tests.erl   <- ships to production, confuses xref/dialyzer

%% Good - tests under test/, compiled only for the test profile
%% src/my_thing.erl
%% test/my_thing_tests.erl
%% test/my_thing_SUITE.erl
```

**Rationale**: Keeping tests in `test/` (where rebar3 compiles them only under the test profile) keeps them out of the shipped release and out of production xref/dialyzer analysis, and keeps the production surface clean. It also pairs with "no debug calls in `src/`" (OPS-01).

**See also**: PS-02, `15-testing.md`, `14-production-ops.md` (OPS-01)

---

## PS-09: Build Releases with `relx`/rebar3

**Strength**: SHOULD

**Summary**: Produce deployable artifacts with `rebar3 release` (relx), not by copying beams around.

```erlang
%% Bad - deploy by copying ebin/*.beam onto a host (no ERTS, no boot script, no config)

%% Good - rebar3 release builds a self-contained, bootable target system
%% rebar.config: {relx, [{release, {my_app, "0.1.0"}, [my_app, sasl]},
%%                        {dev_mode, false}, {include_erts, true}]}.
%% $ rebar3 release   ->   _build/default/rel/my_app/bin/my_app start
```

**Rationale**: rebar3 uses `relx` to assemble releases — pinning app and ERTS versions, generating a boot script, and bundling config (SUP-17). The result starts reproducibly on a target host. Loose-beam deployment has no version pinning, no bundled runtime, and no boot/upgrade story.

**See also**: PS-04, PS-10, `08-supervision-and-applications.md` (SUP-17)

---

## PS-10: Use Profiles for Per-Environment Configuration

**Strength**: CONSIDER

**Summary**: Use rebar3 `profiles` (e.g. `dev`, `test`, `prod`) for dependencies and options that differ by environment.

```erlang
%% Bad - test-only deps and dev tools listed as normal deps (shipped to production)
{deps, [cowboy, proper, meck]}.

%% Good - environment-specific deps/options under profiles
{deps, [cowboy]}.
{profiles, [{test, [{deps, [proper, meck]}]},
            {prod, [{relx, [{dev_mode, false}, {include_erts, true}]}]}]}.
```

**Rationale**: Profiles keep test and dev dependencies (PropEr, meck, formatters) out of production builds and let the release config differ between development and production. Mixing everything into top-level `deps` bloats the release and ships test scaffolding.

**See also**: PS-05, PS-09

---

## PS-11: Publish Reusable Libraries to Hex, with Docs

**Strength**: CONSIDER

**Summary**: Package genuinely reusable libraries for Hex, with metadata and generated documentation.

```erlang
%% Bad - share a library only as a git URL with no version discipline or docs

%% Good - Hex package metadata + published docs
{hex, [{description, "A small queue library"}]}.
%% src/my_queue.app.src: {licenses, ["Apache-2.0"]}, {links, [...]}
%% $ rebar3 hex publish    (and rebar3 ex_doc for HexDocs)
```

**Rationale**: Hex is the Erlang/Elixir package registry; publishing there gives consumers version resolution, immutable releases, and HexDocs-hosted documentation (DC-12). It is the natural endpoint for a library with a clean facade (API-13). Reserve it for code actually meant to be reused — not application-internal code.

**See also**: PS-06, `13-documentation.md` (DC-12), `02-api-design.md` (API-13)

---

## PS-12: Use Version Control; Commit the Lock File

**Strength**: SHOULD

**Summary**: Track everything in source control, commit `rebar.lock`, and ignore generated artifacts.

```erlang
%% Bad - no VCS discipline; rebar.lock uncommitted; _build/ checked in

%% Good - commit sources + rebar.lock; ignore generated output
%% .gitignore:
%%   _build/
%%   *.beam
%%   erl_crash.dump
%% (rebar.lock IS committed)
```

**Rationale**: "All non-trivial projects must use a source code control system" (Programming Rules §8.12). Committing `rebar.lock` makes dependency resolution reproducible across machines and CI (PS-06); ignoring `_build/` and `*.beam` keeps generated artifacts out of history. Version control is also the archive that lets you delete dead code rather than comment it out (DC-11).

**See also**: PS-06, `13-documentation.md` (DC-11)

---

## PS-13: Separate Library Applications from Active Applications

**Strength**: CONSIDER

**Summary**: Keep pure-library apps (no supervision tree) distinct from active apps (with a `{mod, ...}` and a tree), one responsibility each.

```erlang
%% Bad - one application mixes a runnable service and reusable helpers

%% Good - split: an active app for the service, a library app for the helpers
%% apps/service/  -> {mod, {service_app, []}} + supervision tree
%% apps/helpers/  -> library app, no {mod, ...}
```

**Rationale**: A library application only provides code; an active application runs processes (SUP-15). Splitting them lets the library be reused (and Hex-published, PS-11) without dragging in a service's supervision tree, and keeps each application's responsibility clear. This is API-11/ID-10 at the project level.

**See also**: PS-07, PS-11, `08-supervision-and-applications.md` (SUP-15)

---

## PS-14: Keep Dependencies Few and Tree-Shaped

**Strength**: CONSIDER

**Summary**: Minimise direct dependencies and avoid pulling in heavy or overlapping libraries; favour the standard library first.

```erlang
%% Bad - a dependency for every small task, with overlapping/transitive bloat
{deps, [jsx, jiffy, thoas, lager, ...]}.   %% three JSON libs; a logger OTP already provides

%% Good - standard library first; few, deliberate dependencies
{deps, [cowboy]}.
%% JSON: the OTP 27 json module; logging: OTP logger; small helpers: write them
```

**Rationale**: Every dependency is code you don't control, a version to track (PS-06), and a potential security and maintenance burden. Erlang/OTP's standard library is large (now including a `json` module and `logger`), so reach for it first. Few, tree-shaped dependencies (API-12) keep builds fast and the supply chain small.

**See also**: PS-06, `02-api-design.md` (API-12)

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| PS-01 OTP applications | SHOULD | The unit of code, deps, and version |
| PS-02 Standard layout | SHOULD | `src`/`include`/`priv`/`test`; tools expect it |
| PS-03 `priv/` for resources | SHOULD | Locate via `code:priv_dir/1` |
| PS-04 Use rebar3 | SHOULD | Build, deps, tests, releases |
| PS-05 `rebar.config` | SHOULD | One source of truth for the build |
| PS-06 Lock dependencies | SHOULD | Tag/commit + committed `rebar.lock` |
| PS-07 Umbrella projects | CONSIDER | One app per responsibility under `apps/` |
| PS-08 Tests in `test/` | SHOULD | Out of `src/` and the release |
| PS-09 Releases via relx | SHOULD | Self-contained bootable artifact |
| PS-10 Profiles | CONSIDER | Per-environment deps/options |
| PS-11 Publish to Hex | CONSIDER | Versioned packages + HexDocs |
| PS-12 VCS + lock file | SHOULD | Commit `rebar.lock`; ignore `_build/` |
| PS-13 Library vs active apps | CONSIDER | Separate reusable code from services |
| PS-14 Few, tree-shaped deps | CONSIDER | Standard library first |

## Related Guidelines

- **Supervision & applications**: See `08-supervision-and-applications.md` — the `.app` file, the application callback, releases (SUP-11/SUP-17), and library-vs-active apps (SUP-15).
- **Tooling**: See `17-tooling.md` — rebar3, dialyzer, xref, and the CI build/check loop the layout feeds.
- **Testing**: See `15-testing.md` for what goes in `test/` (PS-08).
- **API design**: See `02-api-design.md` — tree-shaped dependencies (API-12) and library facades (API-13).
- **Documentation**: See `13-documentation.md` — generated docs for Hex (DC-12) and deleting dead code (DC-11).

## External References

- [OTP Design Principles — Applications](https://www.erlang.org/doc/system/applications.html) and [Releases](https://www.erlang.org/doc/system/release_structure.html)
- [rebar3 documentation](https://rebar3.org/docs/)
- [Hex package manager](https://hex.pm/)
- Erlang Programming Rules and Conventions — §8.12 (use source code control)
- Inaka Erlang Guidelines — lock your dependencies
- *Designing for Scalability with Erlang/OTP* (Cesarini & Vinoski) — rebar3 (pp. 303–310)
