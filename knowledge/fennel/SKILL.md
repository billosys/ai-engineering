---
name: fennel-guidelines
description: >-
  Source-grounded Fennel practices for writing, reviewing, refactoring and debugging
  .fnl code. Covers Lua runtime semantics, tables, lexical scope, multiple returns,
  pattern matching, modules, expected errors, macros, formatting with fnlfmt,
  embedding and ahead-of-time distribution. Use for Fennel implementation, API
  design, macro hygiene, Lua interoperability or migration from Lua/Clojure.
  Generic Lua-only work needs its host documentation; this skill does not define
  APIs for Neovim, LÖVE, TIC-80 or other embedded hosts.
license: CC-BY-NC-SA-3.0
metadata:
  version: "1.0.0"
  hermes:
    tags: [fennel, lua, lisp, macros, fnlfmt, embedding]
    category: programming-languages
---

# Fennel Guidelines

Use this skill to write clear Fennel with the semantics of the actual Lua host.
The guide structure follows the Rust skill’s task routing, stable pattern IDs,
strength labels, paired good/bad examples, rationale and chapter summaries.
It draws on official Fennel documentation pinned to release 1.6.1; see
[sources, attribution and license](./guides/00-sources-and-license.md).

## Start with the project

Read the project’s instructions and existing code before choosing conventions.
Identify its Fennel compiler, Lua/LuaJIT version, runtime APIs, loading strategy,
formatter and test commands. Preserve these choices unless the task changes them.
The authoring examples were checked on Fennel 1.6.1 and PUC Lua 5.5; a host that
uses Lua 5.1 or LuaJIT needs its own compatibility checks.

Load [anti-patterns](./guides/11-anti-patterns.md) for writing or review, then the
chapters relevant to the actual task. Load [core idioms](./guides/01-values-and-core-idioms.md)
when writing new code or when Lua semantics are unfamiliar. Do not load the
whole source corpus for a routine change.

## Select guides by task

| Task | Guides |
|---|---|
| New code or Lua/Clojure migration | [Core idioms](./guides/01-values-and-core-idioms.md), [style](./guides/02-style-and-naming.md), [tables](./guides/03-tables-and-data.md) |
| Naming, formatting or documentation | [Style and naming](./guides/02-style-and-naming.md), [tooling](./guides/09-setup-tooling-and-testing.md) |
| Data transformations, nil, aliases or iteration | [Tables](./guides/03-tables-and-data.md), [functions](./guides/04-functions-and-control-flow.md) |
| Optional parameters, varargs or extra return values | [Functions and control flow](./guides/04-functions-and-control-flow.md) |
| case/match, guards or shape validation | [Pattern matching](./guides/05-pattern-matching.md) |
| Public API, modules, paths or reloading | [Modules and API design](./guides/06-modules-and-api-design.md), [errors](./guides/07-errors-and-resources.md) |
| Expected failures, exceptions or file handles | [Errors and resources](./guides/07-errors-and-resources.md), [matching](./guides/05-pattern-matching.md) |
| Author or debug macros | [Macros](./guides/08-macros.md), [values](./guides/01-values-and-core-idioms.md), [functions](./guides/04-functions-and-control-flow.md) |
| Compiler/formatter setup or CI checks | [Setup, tooling and testing](./guides/09-setup-tooling-and-testing.md) |
| Lua host integration, AOT build or deployment | [Lua interop and distribution](./guides/10-lua-interop-and-distribution.md), [modules](./guides/06-modules-and-api-design.md) |
| Review generated or existing Fennel | [Anti-patterns](./guides/11-anti-patterns.md), then affected topic chapters |
| Upstream evidence, attribution or licensing | [Sources and license](./guides/00-sources-and-license.md) |

## Workflow recipes

### Implement a module

1. Establish the host and loading strategy. In ordinary Fennel code use file-level
   `local` bindings, grouped imports and small `let` scopes.
2. Define table shapes, mutation ownership, optional arguments and failure returns.
   `local` protects a binding, not its table. Pick `fn` versus `lambda` deliberately.
3. Implement small ordinary functions. Return a minimal export table at the end
   of the module. Make startup effects explicit and keep I/O at boundaries.
4. Check nil versus false, sparse sequences, pattern pinning and multiple-value
   expansion. Add examples that distinguish plausible wrong behavior.
5. Run the project formatter/checks, compile with explicit global checking, execute
   behavior tests and test emitted Lua through the actual consumer when shipping it.

### Design a macro

1. Read the values and macro chapters. Write the desired expansion and call syntax
   before implementing a macro; an ordinary function may already be sufficient.
2. Specify evaluation count/order, exposed bindings and emitted runtime dependencies.
   Use quoted templates, gensyms for internal names and explicit name arguments for
   caller-visible locals. Keep runtime values out of compiler-scope computations.
3. Validate AST inputs with `assert-compile`. Inspect `macrodebug` output.
4. Test effectful arguments, name collisions, invalid syntax and multi-form bodies.
   Prove the intended result and effects, not just compilation with literals.

### Review or debug

1. Trace each binding and each changed table to its owner. Check globals and hidden
   import-time effects, including embedded-host configuration.
2. At every boundary, establish whether failure means nil/error values or a raised
   error. Trace the number of values received by variadic consumers.
3. Check `case` versus `match`, partial table patterns, loop guards and nil holes.
4. For macros, compare actual expansion against the promised behavior. For builds,
   test a clean emitted artifact and the target Lua VM.
5. Cite pattern IDs and exact affected code in findings. Distinguish compiler rules
   from contextual style preferences and untested host assumptions.

## Essential semantic checks

- Tables are mutable; ordinary equality compares identity, not deep contents.
- `:name` is a string. There is no separate keyword type or built-in persistent
  collection layer. Operators are forms, not first-class runtime functions.
- Only nil and false are false. Setting a table field to nil removes it;
  `ipairs` stops at the first hole and `pairs` has no ordering guarantee.
- `fn` permits missing/extra arguments. `lambda` checks required bindings for nil,
  not exact arity or arbitrary types. Last expressions supply function results.
- A final function call can forward multiple values. Explicitly select or pack
  them when the next API’s arity or nil cardinality matters.
- `case` introduces fresh pattern bindings; `match` implicitly pins existing names.
  Empty table patterns match tables with contents as well as empty ones.
- Macros run at compile time. Preserve scope and evaluation count; generated Lua
  needs its own runtime imports. The compiler sandbox is not a security boundary.
- AOT compilation defaults to no global checking. Enable it explicitly and execute
  the result on the real host; no Fennel runtime is needed only when the artifact
  does not itself depend on compiler-library helpers or a Fennel loader.

## Guide conventions

Pattern IDs are stable within their chapter: ID, ST, DT, FN, PM, MD, ER, MC,
TL, LI and AP. Every rule has a strength, examples, rationale and pinned source
references. Chapter summary tables are compressed indexes; read the full rule
when its conditions matter. BAD examples may deliberately fail to compile or
assert an undesirable observed result. Host/module fragments are labelled.

The sibling [version history](./version-history.md) records changes to this skill.
The [source/license guide](./guides/00-sources-and-license.md) carries upstream
attribution and the CC BY-NC-SA license applicable to the adapted prose.
