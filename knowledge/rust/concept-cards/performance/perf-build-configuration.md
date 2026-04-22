---
concept: Build Configuration for Performance
slug: perf-build-configuration
category: performance
subcategory: build-settings
tier: foundational
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Build Configuration"
chapter_number: 2
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Cargo profile optimization"
  - "release build configuration"
  - "LTO"
  - "link-time optimization"
  - "codegen-units"
  - "PGO"
  - "profile-guided optimization"
  - "cargo-wizard"
prerequisites:
  - perf-overview
extends: []
related:
  - perf-profiling
  - perf-heap-allocations
contrasts_with: []
answers_questions:
  - "How do I configure Cargo for maximum runtime speed?"
  - "What is LTO and should I enable it?"
  - "How do I reduce Rust binary size?"
  - "What alternative allocators are available for Rust?"
  - "How do I speed up Rust compile times?"
  - "What does codegen-units = 1 do?"
  - "Should I use jemalloc or mimalloc?"
  - "What is PGO and how do I use it with Rust?"
---

# Quick Definition

Rust build configuration can drastically change program performance without code changes. Key settings include optimization level, codegen units, LTO, alternative allocators, CPU-specific instructions, PGO, panic strategy, symbol stripping, linker choice, and debug info settings -- each trading off between compile time, runtime speed, binary size, and debuggability.

# Core Definition

"You can drastically change the performance of a Rust program without changing its code, just by changing its build configuration. There are many possible build configurations for each Rust program. The one chosen will affect several characteristics of the compiled code, such as compile times, runtime speed, memory use, binary size, debuggability, profilability, and which architectures your compiled program will run on." (Ch. 2, Build Configuration introduction)

The single most important choice is using release builds (`--release`): "Dev builds are the default. They are good for debugging, but are not optimized... 10-100x speedups over dev builds are common!" Release builds enable optimizations, omit debug assertions and integer overflow checks, and omit debug info. (Ch. 2, Release Builds)

Cargo only reads profile settings from the root workspace `Cargo.toml` -- profile settings in dependencies are ignored, making these options primarily relevant for binary crates. The `cargo-wizard` tool can help choose an appropriate build configuration. (Ch. 2, introduction)

# Prerequisites

- **perf-overview** -- understanding the benchmarking and measurement approach is important because "performance-related choices should be validated with benchmarking"

# Key Properties

1. **Release vs. dev**: The most important choice; release builds are 10-100x faster than dev builds
2. **Codegen units**: Setting `codegen-units = 1` in `[profile.release]` may improve runtime speed and reduce binary size at the cost of longer compile times
3. **LTO** comes in four forms: thin local (default for release, `lto = false`), thin (`lto = "thin"`), fat (`lto = "fat"`), and fully off (`lto = "off"`). Fat LTO can improve runtime speed by 10-20% or more
4. **Alternative allocators**: jemalloc (`tikv-jemallocator`) and mimalloc can provide large improvements in speed and memory usage depending on the program and platform
5. **CPU-specific instructions**: `-C target-cpu=native` generates instructions specific to the build machine's CPU, enabling AVX SIMD and similar optimizations
6. **PGO**: Profile-guided optimization compiles, profiles, then recompiles -- can improve speed by 10% or more but requires setup effort
7. **Optimization level**: `opt-level = "z"` minimizes binary size (most aggressively); `opt-level = "s"` is slightly less aggressive but allows loop vectorization
8. **Panic strategy**: `panic = "abort"` can reduce binary size and slightly increase speed when `catch_unwind` is not needed
9. **Symbol stripping**: `strip = "symbols"` reduces binary size but makes debugging and profiling harder
10. **Linker**: lld (default on Linux since Rust 1.90), mold, and wild are faster linkers with no trade-offs when they work correctly
11. **Debug info**: `debug = false` in `[profile.dev]` can improve dev build times by 20-40%
12. **Cranelift**: An experimental codegen backend (nightly only) that may reduce compile times at the cost of lower quality generated code

# Construction / Recognition

## To Maximize Runtime Speed:
1. Ensure you're using `cargo build --release` (not dev builds)
2. Add to `Cargo.toml`:
   ```toml
   [profile.release]
   codegen-units = 1
   lto = "fat"
   panic = "abort"  # if catch_unwind is not needed
   ```
3. Consider an alternative allocator (jemalloc or mimalloc)
4. Use `RUSTFLAGS="-C target-cpu=native"` if binary portability is not needed
5. Consider PGO via `cargo-pgo` if the setup effort is justified

## To Minimize Binary Size:
1. Add to `Cargo.toml`:
   ```toml
   [profile.release]
   opt-level = "z"
   codegen-units = 1
   lto = "fat"
   panic = "abort"
   strip = "symbols"
   ```
2. Consult the `min-sized-rust` repository for advanced techniques

## To Minimize Compile Times:
1. Use a faster linker (lld, mold, or wild) -- no trade-offs
2. Disable debug info: `debug = false` in `[profile.dev]`
3. On nightly: try the parallel front-end (`-Zthreads=8`) or Cranelift backend

# Context & Application

Build configuration is often the highest-leverage optimization because it requires no code changes. The chapter is organized around three goals: maximizing runtime speed, minimizing binary size, and minimizing compile times.

The trade-off structure is consistent: most settings improve one characteristic while worsening another. Faster linkers are the notable exception -- they provide pure compile-time wins with no downsides. Custom Cargo profiles can create intermediate points between `dev` and `release` for development workflows where neither extreme is ideal.

jemalloc on Linux can be further tuned with transparent huge pages (THP) by setting `MALLOC_CONF="thp:always,metadata_thp:always"`, which may speed up programs at the cost of higher memory usage.

PGO is powerful but limited: it is "not supported for binaries hosted on crates.io and distributed via `cargo install`." The BOLT optimizer (accessible via `cargo-pgo`) provides a similar approach.

# Examples

**Example 1** (Ch. 2, Release Builds): The output `Finished dev [unoptimized + debuginfo]` vs. `Finished release [optimized]` indicates which build type was produced.

**Example 2** (Ch. 2, Alternative Allocators): To use jemalloc:
```toml
[dependencies]
tikv-jemallocator = "0.5"
```
```rust
#[global_allocator]
static GLOBAL: tikv_jemallocator::Jemalloc = tikv_jemallocator::Jemalloc;
```

**Example 3** (Ch. 2, CPU Specific Instructions): `RUSTFLAGS="-C target-cpu=native" cargo build --release` generates instructions specific to the build machine's CPU. Compare `rustc --print cfg` vs. `rustc --print cfg -C target-cpu=native` to verify feature detection.

**Example 4** (Ch. 2, Summary): The recommended maximum-speed configuration: `codegen-units = 1`, `lto = "fat"`, an alternative allocator, and `panic = "abort"`, plus `-C target-cpu=native` if portability is not needed.

# Relationships

## Builds Upon
- **perf-overview** -- benchmarking is essential for validating build configuration choices

## Enables
- **perf-profiling** -- profiling requires specific build settings (debug info, frame pointers)
- **perf-heap-allocations** -- alternative allocators are a build-level optimization that affects heap allocation performance

## Related
- **perf-inlining** -- LTO and codegen-units affect cross-crate inlining opportunities

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Benchmarking with dev builds instead of release builds.
  **Correction**: Always use `cargo build --release` or `cargo run --release` for performance testing. Dev builds are 10-100x slower.

- **Error**: Setting `lto = "off"` thinking it is the same as the default `lto = false`.
  **Correction**: `lto = false` leaves thin local LTO enabled (the default for release builds). `lto = "off"` fully disables LTO, likely worsening performance.

- **Error**: Enabling all optimization settings at once without benchmarking each individually.
  **Correction**: "Benchmark all changes, one at a time, to ensure they have the expected effects." Some settings may interact unexpectedly.

# Common Confusions

- **Confusion**: Thinking `opt-level = 3` is always the fastest option.
  **Clarification**: The default release `opt-level` is already 3. For binary size, `opt-level = "z"` or `"s"` targets minimal size. The `"s"` variant allows slightly more inlining and loop vectorization than `"z"`.

- **Confusion**: Believing alternative allocators always improve performance.
  **Clarification**: "The exact effect will depend on the individual program and the alternative allocator chosen... The effect will also vary across platforms, because each platform's system allocator has its own strengths and weaknesses." Always benchmark.

- **Confusion**: Thinking PGO can be used with any distribution method.
  **Clarification**: PGO is "not supported for binaries hosted on crates.io and distributed via `cargo install`," which limits its applicability.

# Source Reference

Chapter 2: Build Configuration -- all sections: Release Builds, Maximizing Runtime Speed (Codegen Units, Link-time Optimization, Alternative Allocators, CPU Specific Instructions, Profile-guided Optimization), Minimizing Binary Size (Optimization Level, Abort on panic!, Strip Symbols, Other Ideas), Minimizing Compile Times (Linking, Disable Debug Info Generation, Experimental Parallel Front-end, Cranelift Codegen Back-end), Custom profiles, Summary.

# Verification Notes

- Definition source: Direct quotations from Ch. 2 introduction and Release Builds section
- Configuration examples: All `Cargo.toml` snippets directly from the source
- Summary recommendations: Directly from the Summary section at the end of Ch. 2
- Confidence rationale: HIGH -- the most detailed chapter in the book, with explicit configuration options and clear trade-off descriptions
- Uncertainties: None; all settings and their effects are explicitly documented
