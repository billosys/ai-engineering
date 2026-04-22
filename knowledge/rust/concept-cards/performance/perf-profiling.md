---
concept: Profiling Rust Programs
slug: perf-profiling
category: performance
subcategory: methodology
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Profiling"
chapter_number: 4
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Rust profiling"
  - "performance profiling"
  - "perf tool"
  - "Cachegrind"
  - "DHAT"
  - "flamegraph"
  - "samply"
prerequisites:
  - perf-overview
  - perf-build-configuration
extends: []
related:
  - perf-heap-allocations
  - perf-inlining
  - perf-type-sizes
contrasts_with: []
answers_questions:
  - "Which profilers work with Rust programs?"
  - "How do I profile a Rust release build?"
  - "How do I get debug info in release builds for profiling?"
  - "What is symbol demangling and how do I fix it?"
  - "How do I enable frame pointers for better stack traces?"
---

# Quick Definition

Profiling identifies which parts of a Rust program are "hot" (executed frequently enough to affect runtime). The Rust ecosystem supports many profilers including perf, Cachegrind, DHAT, samply, flamegraph, and platform-specific tools. Effective profiling of release builds requires enabling debug info and potentially frame pointers.

# Core Definition

"When optimizing a program, you also need a way to determine which parts of the program are 'hot' (executed frequently enough to affect runtime) and worth modifying. This is best done via profiling." (Ch. 4, Profiling introduction)

The chapter catalogs profiling tools with their strengths, platform support, and use cases, then covers three practical setup concerns: enabling debug info in release builds, preserving frame pointers for stack trace quality, and handling Rust's symbol name mangling. (Ch. 4, all sections)

# Prerequisites

- **perf-overview** -- understanding the overall optimization methodology (benchmark, profile, optimize, measure)
- **perf-build-configuration** -- profiling requires specific build configuration choices (debug info, frame pointers)

# Key Properties

1. **perf**: General-purpose profiler using hardware performance counters; viewed with Hotspot or Firefox Profiler; Linux only
2. **Instruments**: General-purpose profiler bundled with Xcode; macOS only
3. **Intel VTune Profiler** and **AMD uProf**: Vendor-specific general-purpose profilers
4. **samply**: Sampling profiler with Firefox Profiler output; works on Mac, Linux, and Windows
5. **flamegraph**: Cargo command using perf/DTrace to produce flame graphs; works on Linux and DTrace platforms
6. **Cachegrind** and **Callgrind**: Provide instruction counts and simulated cache/branch prediction data per function and per source line; Linux and some Unixes
7. **DHAT**: Identifies hot allocation sites, allocation rates, and peak memory usage; can identify hot `memcpy` calls; Linux and some Unixes (dhat-rs works on all platforms)
8. **heaptrack** and **bytehound**: Heap profiling tools; Linux only
9. **counts**: Ad hoc profiling combining `eprintln!` statements with frequency post-processing; all platforms
10. **Coz**: Causal profiler measuring optimization potential; Linux only via coz-rs
11. Release builds need `debug = "line-tables-only"` in `[profile.release]` for source-level profiling
12. Frame pointers may be optimized away; use `-C force-frame-pointers=yes` to preserve stack trace quality

# Construction / Recognition

## To Profile a Rust Release Build:
1. Enable debug info by adding to `Cargo.toml`:
   ```toml
   [profile.release]
   debug = "line-tables-only"
   ```
2. Optionally force frame pointers for better stack traces:
   ```bash
   RUSTFLAGS="-C force-frame-pointers=yes" cargo build --release
   ```
3. Choose a profiler appropriate to your platform and the type of information needed
4. Run the profiler against your program with representative workloads
5. Identify hot functions and allocation sites
6. If symbol names appear mangled (starting with `_ZN` or `_R`), use `rustfilt` to demangle them

## To Get Standard Library Debug Info:
1. Build your own compiler and standard library with `debuginfo-level = 1` in `bootstrap.toml` (most reliable method)
2. Or use the unstable `build-std` feature (limited: source filenames won't point to actual source files)

# Context & Application

The profiling landscape for Rust is rich but fragmented across platforms. Linux has the best tooling support (perf, Cachegrind, DHAT, heaptrack, Coz), macOS has Instruments and samply, and Windows has limited options (Intel VTune, samply). The `dhat-rs` crate provides a cross-platform alternative to DHAT with slightly less power.

A key practical challenge is that shipped Rust standard library binaries lack debug info. The most complete workaround is building your own compiler/stdlib, which is "a hassle, but may be worth the effort in some cases."

Symbol demangling can be addressed by switching from the default legacy mangling format to v0 format with `-C symbol-mangling-version=v0`. This may help profilers that struggle with Rust's default name encoding.

Iai-Callgrind provides `cargo bench` integration for Valgrind-based profilers (Cachegrind, Callgrind, DHAT), bridging the gap between benchmarking and profiling workflows.

# Examples

**Example 1** (Ch. 4, Debug Info): To enable source-level profiling of release builds:
```toml
[profile.release]
debug = "line-tables-only"
```

**Example 2** (Ch. 4, Frame Pointers): Force frame pointers via RUSTFLAGS:
```bash
RUSTFLAGS="-C force-frame-pointers=yes" cargo build --release
```
Or via `config.toml`:
```toml
[build]
rustflags = ["-C", "force-frame-pointers=yes"]
```

**Example 3** (Ch. 4, Symbol Demangling): Mangled names like `_ZN3foo3barE` or `_RMCsno73SFvQKx_1cINtB0_3StrKRe616263_E` can be demangled with `rustfilt`, or the v0 mangling format can be enabled:
```bash
RUSTFLAGS="-C symbol-mangling-version=v0" cargo build --release
```

# Relationships

## Builds Upon
- **perf-overview** -- profiling is the second step in the optimize-measure cycle after benchmarking
- **perf-build-configuration** -- profiling requires specific build settings

## Enables
- **perf-inlining** -- Cachegrind output reveals whether functions are inlined
- **perf-heap-allocations** -- DHAT identifies hot allocation sites
- **perf-type-sizes** -- DHAT's copy profiling mode identifies hot `memcpy` calls from oversized types

## Related
- All other performance cards -- profiling is used to validate all optimization techniques

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Profiling a dev build instead of a release build.
  **Correction**: Profile release builds with `debug = "line-tables-only"` enabled. Dev builds have different optimization characteristics and hot spots may not match production.

- **Error**: Expecting complete stack traces without enabling frame pointers.
  **Correction**: The Rust compiler may optimize away frame pointers. Use `-C force-frame-pointers=yes` when stack trace quality matters.

- **Error**: Expecting standard library functions to appear in source-level profiling output.
  **Correction**: Shipped Rust standard library binaries lack debug info. Build your own compiler/stdlib with `debuginfo-level = 1` for complete profiling.

# Common Confusions

- **Confusion**: Thinking one profiler covers all needs.
  **Clarification**: Different profilers serve different purposes: perf/samply for CPU sampling, Cachegrind for instruction counts and cache analysis, DHAT for allocation profiling, heaptrack for heap analysis, Coz for optimization potential. Choose based on what you need to measure.

- **Confusion**: Thinking `build-std` is a complete solution for standard library debug info.
  **Clarification**: `build-std` compiles the standard library with your configuration, but "filenames present in the debug info for the standard library will not point to source code files" because it doesn't download source code. It won't help profilers like Cachegrind and samply that need source.

# Source Reference

Chapter 4: Profiling -- all sections: Profilers (tool catalog), Debug Info (release build configuration), Frame pointers, Symbol Demangling.

# Verification Notes

- Definition source: Direct quotation from Ch. 4 introduction
- Tool catalog: Complete enumeration from the Profilers section with platform support
- Build configuration: Direct from Debug Info, Frame pointers, and Symbol Demangling sections
- Confidence rationale: HIGH -- the chapter provides a comprehensive, explicit catalog of tools and configuration with clear instructions
- Uncertainties: None
