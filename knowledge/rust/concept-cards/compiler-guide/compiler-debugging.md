---
# === CORE IDENTIFICATION ===
concept: Debugging and Profiling the Rust Compiler
slug: compiler-debugging

# === CLASSIFICATION ===
category: compiler-development
subcategory: debugging
tier: foundational

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Debugging the Compiler, Tracing, Profiling"
chapter_number: 3
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "debugging rustc"
  - "RUSTC_LOG"
  - "tracing in rustc"
  - "profiling rustc"
  - "perf profiling"
  - "-Z flags"
  - "treat-err-as-bug"
  - "rustc_attrs"
  - "self-profile"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - building-rustc
extends: []
related:
  - compiler-guide-overview
  - compiler-testing
  - contributing-to-rustc
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I debug the Rust compiler with GDB or LLDB?"
  - "How do I get the compiler to print debugging/tracing output?"
  - "What is RUSTC_LOG and how do I filter its output?"
  - "How do I get a backtrace for a specific compiler error?"
  - "What -Z flags are useful for debugging?"
  - "How do I profile the compiler's performance?"
  - "How do I use perf to analyze rustc?"
  - "How do I use self-profiling (-Z self-profile)?"
  - "What internal attributes (#[rustc_*]) help with debugging?"
  - "How do I bisect compiler regressions?"
---

# Quick Definition

Debugging rustc involves three main techniques: **tracing** (structured logging via the `tracing` crate, controlled by `RUSTC_LOG`), **debugger-based debugging** (GDB/LLDB with `rust.debug = true` and `rust.debuginfo-level = 2`), and **profiling** (using `perf`, `-Z self-profile`, `samply`, `cachegrind`, or `cargo-llvm-lines`). The compiler also provides numerous `-Z` flags for unstable debugging features and internal `#[rustc_*]` attributes for dumping compiler state. Regression bisection uses `cargo-bisect-rustc` to automatically identify the PR that caused a change.

# Core Definition

## Tracing / Logging

The compiler uses the `tracing` crate for structured logging, controlled by the `RUSTC_LOG` environment variable. The logging system supports three levels of filtering:

**Function-level filters** use `#[instrument]` annotations:
```
RUSTC_LOG=[foo]                              # log all calls to foo with arguments
RUSTC_LOG=rustc_borrowck[do_mir_borrowck]    # only borrowck calls to do_mir_borrowck
RUSTC_LOG=[do_mir_borrowck{id=\.\*from_utf8_unchecked\.\*}]  # filter by argument regex
```

**Query-level filters** leverage automatic tracing spans on every query:
```
RUSTC_LOG=[typeck]                           # everything during type checking
RUSTC_LOG=[typeck{key=.*name_of_item.*}]     # typeck for a specific item
```

**Module-level filters** use traditional log-style filtering:
```
RUSTC_LOG=rustc_middle::traits=debug         # debug+ output from a module
RUSTC_LOG=rustc_codegen_ssa=info             # info+ output from codegen
```

Key environment variables: `RUSTC_LOG` (filter), `RUSTC_LOG_COLOR` (always/never/auto), `RUSTC_LOG_ENTRY_EXIT` (span enter/exit), `RUSTC_LOG_BACKTRACE` (capture backtraces on matching targets), `RUSTC_LOG_FORMAT_JSON` (JSON output), `RUSTC_LOG_OUTPUT_TARGET` (redirect to file).

**Important**: `debug!` and `trace!` calls are only compiled in when `rust.debug-logging=true` in `bootstrap.toml`. Without this, only `error!`, `warn!`, and `info!` are available.

## Debugging with GDB/LLDB

Enable debug info in `bootstrap.toml`:
```toml
rust.debug = true
rust.debuginfo-level = 2   # full debuginfo (default with debug=true is level 1)
```

Level 1 provides execution path tracking; level 2 adds full symbol information but uses significantly more disk space (~35GB+). GDB v10.2+ is required for the default v0 symbol mangling.

## -Z Flags and Internal Attributes

- `-Z treat-err-as-bug=n` -- panics on the nth error, enabling backtrace capture for the error site
- `-Z eagerly-emit-delayed-bugs` -- converts delayed bugs to immediate errors for debugging
- `-Z track-diagnostics` -- prints the source location where each diagnostic was created
- `-Z verbose-internals` -- enables more verbose output generally
- `#[rustc_dump_layout]`, `#[rustc_dump_def_parents]`, `#[rustc_dump_predicates]`, `#[rustc_dump_vtable]`, etc. -- internal attributes (behind `#![feature(rustc_attrs)]`) that dump compiler state

## Profiling

Multiple profiling approaches serve different needs:
- **`-Z self-profile`** -- query-based profiling with `measureme` tools
- **`perf`** -- Linux native profiler for function-level performance data
- **`samply`** -- sampling profiler with graphical interface
- **`cachegrind`** -- detailed simulated execution trace
- **`cargo --timings`** -- visual crate-graph compilation times
- **`cargo-llvm-lines`** -- counts LLVM IR lines per generic instantiation to identify monomorphization bloat
- **WPA (Windows)** -- Windows Performance Analyzer for memory and CPU profiling

# Prerequisites

- A compiler build (stage 1 minimum) configured for the type of debugging needed
- For tracing: `rust.debug-logging = true` in `bootstrap.toml` if `debug!`/`trace!` output is needed
- For GDB: `rust.debug = true` and `rust.debuginfo-level = 2`
- For perf profiling: `perf` installed on Linux; `rust.debuginfo-level = 1` for line info

# Key Properties

1. **RUSTC_LOG is the primary debugging lever**: Function-level, query-level, and module-level filters provide increasingly specific output control
2. **`-Z treat-err-as-bug` converts errors to panics**: This enables `RUST_BACKTRACE=1` to capture a stack trace showing exactly where a specific error was emitted
3. **Debug/trace calls are compiled out by default**: Must set `rust.debug-logging=true` to include `debug!` and `trace!` calls in the binary
4. **`#[instrument(level = "debug")]` is preferred over `debug!("foo(...)")` at function entry**: Convention uses structured tracing fields: `debug!(?variable.field)` instead of `debug!("xyz = {:?}", variable.field)`
5. **Expensive operations in debug logs can impact anyone using that module's logging**: "you should not put anything too expensive or likely to crash" in debug statements
6. **`cargo-bisect-rustc` automates regression finding**: Downloads and tests nightly artifacts to identify exactly which PR caused a behavior change
7. **ICE files can be suppressed**: Set `RUSTC_ICE=0` to prevent creation of `rustc-ice-<timestamp>-<pid>.txt` files
8. **`perf focus` helps analyze perf data**: Allows regex-based queries like "how much time in function F when called from G" on perf recordings
9. **`./x perf` integrates with rustc-perf**: Bootstrap provides built-in benchmarking via `./x perf benchmark`, `./x perf compare`, `./x perf samply`, etc.
10. **Graphviz output from compiler options**: Some debugging options produce `.dot` files viewable with `dot -T pdf file.dot > file.pdf`

# Construction / Recognition

## Getting a Backtrace for a Specific Error:

```bash
RUST_BACKTRACE=1 rustc +stage1 error.rs -Z treat-err-as-bug
```

This panics on the first error and prints the stack trace showing where the error was emitted.

## Filtering Tracing Output:

```bash
# Debug output from a specific module
RUSTC_LOG=rustc_middle::traits=debug rustc +stage1 my-file.rs

# Pipe to file (output can be very large)
RUSTC_LOG=rustc_middle::traits=debug rustc +stage1 my-file.rs 2>traits-log

# With colors in a pager
RUSTC_LOG=debug RUSTC_LOG_COLOR=always rustc +stage1 ... | less -R
```

## Profiling with perf:

```bash
# Record
perf record -F99 --call-graph dwarf cargo +stage1 rustc --profile check --lib
# Analyze
perf report
# Or use perf-focus
perf focus '{do_mir_borrowck}' --tree-callees --tree-min-percent 3
```

## Debugging Type Layouts:

```rust
#![feature(rustc_attrs)]

#[rustc_dump_layout(debug)]
type T<'a> = &'a u32;
```

# Context & Application

- **Investigating compiler bugs**: Tracing and `-Z treat-err-as-bug` pinpoint where errors originate
- **Understanding compiler behavior**: `RUSTC_LOG` at function/query level reveals the compiler's decision-making process
- **Performance optimization**: Self-profiling, perf, and `cargo-llvm-lines` identify hot spots and monomorphization bloat
- **Regression bisection**: `cargo-bisect-rustc` finds the exact PR that introduced a regression
- **Windows development**: WPA provides memory and CPU profiling with Rust symbol support

# Examples

**Example 1**: Finding where a specific error is created:
```bash
$ RUST_BACKTRACE=1 rustc +stage1 error.rs -Z track-diagnostics
error[E0277]: cannot add `()` to `{integer}`
 --> src/error.rs:2:7
  |
2 |     1 + ();
  |       ^ no implementation for `{integer} + ()`
-Ztrack-diagnostics: created at compiler/rustc_trait_selection/src/traits/error_reporting/mod.rs:638:39
```

**Example 2**: Profiling with perf-focus to explore where borrowck spends time:
```bash
$ perf focus '{do_mir_borrowck}' --tree-callees --tree-min-percent 3
Percentage : 43%

Tree
| matched `{do_mir_borrowck}` (43% total, 0% self)
: | rustc_borrowck::nll::compute_regions (20% total, 0% self)
: : | rustc_borrowck::nll::type_check::type_check_internal (13% total, 0% self)
: | rustc::mir::visit::Visitor::visit_mir (8% total, 6% self)
```

**Example 3**: Reducing LLVM IR bloat with `cargo-llvm-lines`:
```bash
./x clean
env RUSTFLAGS=-Csave-temps ./x build --stage 0 compiler/rustc
# Convert bitcode to human-readable LLVM assembly
for f in build/*/stage0-rustc/*/release/deps/rustc_middle-*.no-opt.bc; do
  ./build/*/llvm/bin/llvm-dis "$f"
done
cargo llvm-lines --files ./build/*/stage0-rustc/*/release/deps/rustc_middle-*.ll
```

**Example 4**: VSCode launch configuration for debugging rustc:
```json
{
    "type": "lldb",
    "request": "launch",
    "program": "${workspaceFolder}/build/host/stage1/bin/rustc",
    "args": [],
    "cwd": "${workspaceFolder}",
    "sourceLanguages": ["rust"]
}
```

# Relationships

## Builds Upon
- **building-rustc** -- debugging requires a compiler built with appropriate debug options

## Enables
- **contributing-to-rustc** -- debugging skills are essential for investigating and fixing bugs

## Related
- **compiler-testing** -- test failures often require debugging techniques from this chapter
- **compiler-guide-overview** -- debugging is part of the broader contributor workflow

## Contrasts With
- None within this source

# Common Errors

- **Error**: Not seeing `DEBUG` logs after setting `RUSTC_LOG`.
  **Correction**: "Make sure that `rust.debug-logging=true` is turned on in your bootstrap.toml." Without this, `debug!` and `trace!` calls are compiled out entirely.

- **Error**: Using `debuginfo-level = 2` without sufficient disk space.
  **Correction**: Full debuginfo uses "upwards of 35GB." Use `debuginfo-level = 1` for execution path tracking with lower disk cost.

- **Error**: Running GDB < v10.2 with default symbol mangling.
  **Correction**: Either upgrade GDB or set `rust.new-symbol-mangling = false` in `bootstrap.toml`.

- **Error**: Putting expensive operations inside `debug!` calls.
  **Correction**: Operations in `debug!` execute whenever that module's logging is enabled. "No-one will know it until someone tries to use logging to find another bug."

# Common Confusions

- **Confusion**: `RUSTC_LOG=debug` is a good default for debugging.
  **Clarification**: "This will show the output of all `debug!` calls in the Rust compiler, and there are a lot of them, so it will be hard to find anything." Use specific module or function-level filters instead.

- **Confusion**: `-Z track-diagnostics` and `-Z treat-err-as-bug` do the same thing.
  **Clarification**: `-Z track-diagnostics` prints the creation location of every diagnostic without changing behavior. `-Z treat-err-as-bug` converts errors to panics for backtrace capture. They serve different purposes and can be combined.

- **Confusion**: `MIRI_LOG_COLOR` colors all log output when using Miri.
  **Clarification**: "MIRI_LOG_COLOR will only color logs that come from Miri, not logs from rustc functions that Miri calls. Use `RUSTC_LOG_COLOR` to color logs from rustc."

# Source Reference

Chapter 3 (1291 lines) covering: Debugging the Compiler (configuring debug builds, backtraces, -Z flags, internal attributes, GDB/LLDB setup), Using Tracing to Debug the Compiler (RUSTC_LOG filters, function/query/module filtering, environment variables, logging conventions), Profiling the Compiler (self-profile, perf, cargo-llvm-lines, WPA on Windows), Profiling with perf (detailed perf workflow and perf-focus analysis), and Profiling with rustc-perf (bootstrap integration with benchmarking).

# Verification Notes

- Definition source: Direct content from Chapter 3 debugging and profiling documentation
- Key Properties: All items supported by source text with specific commands, flags, and examples
- Confidence rationale: HIGH -- detailed, practical documentation with concrete command-line examples
- Uncertainties: Tool versions and availability may change; perf-focus may have limited maintenance
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
