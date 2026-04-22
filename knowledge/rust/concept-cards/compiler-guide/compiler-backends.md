---
concept: "Backend Tooling: Libraries, PGO, Coverage, and Sanitizers"
slug: compiler-backends
category: compiler-internals
subcategory: backend-tooling
tier: advanced
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "25-backend-tooling"
chapter_number: 25
pdf_page: null
section: "Libraries and metadata, Profile-guided optimization, LLVM source-based code coverage, Sanitizers support"
extraction_confidence: high
aliases:
  - "rlib"
  - "dylib"
  - "rmeta"
  - "crate metadata"
  - "PGO"
  - "profile-guided optimization"
  - "instrument-coverage"
  - "sanitizers"
  - "AddressSanitizer"
  - "MemorySanitizer"
  - "ThreadSanitizer"
  - "crate loading"
  - "pipelining"
prerequisites: []
extends: []
related:
  - compiler-code-generation
  - compiler-mir-optimizations
contrasts_with: []
answers_questions:
  - "What are rlib, dylib, and rmeta file formats?"
  - "What does crate metadata contain?"
  - "How does crate loading and dependency resolution work?"
  - "How does cargo pipelining work with rmeta files?"
  - "How is profile-guided optimization implemented in rustc?"
  - "How does LLVM source-based code coverage work?"
  - "What sanitizers does rustc support and how are they implemented?"
  - "What is the Strict Version Hash (SVH) and Stable Crate Id?"
  - "How do I enable a sanitizer on a new target?"
  - "What is the PGO workflow and what are its runtime aspects?"
---

# Quick Definition

Rustc's backend tooling encompasses crate library formats (`rlib`, `dylib`, `rmeta`) and their metadata, profile-guided optimization (PGO) via LLVM IR-level instrumentation, source-based code coverage via `llvm.instrprof.increment`, and sanitizer support (Address, Memory, Thread, CFI, and more). These features rely almost entirely on LLVM infrastructure, with rustc serving as the integration point for compile-time instrumentation passes and runtime libraries from LLVM's `compiler-rt`.

# Core Definition

Crate libraries: "A crate dependency can be loaded from an `rlib`, `dylib`, or `rmeta` file. A key point of these file formats is that they contain `rustc`-specific metadata. This metadata allows the compiler to discover enough information about the external crate to understand the items it contains, which macros it exports, and much more." (Ch. 25, Libraries and metadata)

PGO: "The basic concept of PGO is to collect data about the typical execution of a program (e.g. which branches it is likely to take) and then use this data to inform optimizations such as inlining, machine-code layout, register allocation, etc." (Ch. 25, Profile-guided optimization)

Sanitizers: "The implementation of sanitizers (except CFI) relies almost entirely on LLVM. The rustc is an integration point for LLVM compile time instrumentation passes and runtime libraries." (Ch. 25, Sanitizers support)

# Prerequisites

None listed, though understanding of the codegen pipeline and LLVM basics is helpful.

# Key Properties

1. **rlib format**: Archive file containing per-codegen-unit `.o` files (skippable with `-C linker-plugin-lto`), LLVM bitcode embedded in `.o` sections (removable with `-C embed-bitcode=no`), metadata in `lib.rmeta`, and a symbol table
2. **dylib format**: Platform-specific shared library with rustc metadata in a special `.rustc` link section
3. **rmeta format**: Custom binary format with metadata only -- no compiled object files, cannot be linked; used by `cargo check`, `cargo doc`, and for build pipelining
4. **Metadata contents**: Compiler version, Strict Version Hash (SVH), Stable Crate Id, source file info, exported macros/traits/types/items, and optionally encoded MIR (skipped by `cargo check`)
5. **SVH (Strict Version Hash)**: 64-bit hash of HIR node hashes, upstream crate hashes, source filenames, and certain CLI flags; used to ensure correct dependency loading and for incremental compilation session filenames
6. **Stable Crate Id**: 64-bit hash of crate name plus `-C metadata` CLI options; used in symbol name mangling, crate loading; Cargo auto-generates `-C metadata` from package version, source, and target kind
7. **Crate loading**: `CStore` uses `CrateLocator` to find dependencies; direct deps from `--extern` flags, transitive deps from `-L` directories by scanning metadata for matching crate name and SVH
8. **Build pipelining**: Cargo saves `rmeta` early (before codegen finishes), sends a JSON message so dependent crates can begin compilation; works for libraries but not binaries (linking requires full codegen)
9. **PGO workflow**: Four steps -- (1) compile with `-C profile-generate`, (2) run to produce `.profraw`, (3) convert with `llvm-profdata` to `.profdata`, (4) recompile with `-C profile-use=merged.profdata`
10. **PGO implementation**: IR-level instrumentation via LLVM `PassManagerBuilder` flags (`EnablePGOInstrGen`, `PGOInstrGen`, `PGOInstrUse`); runtime from `compiler-rt` wrapped in `library/profiler_builtins`
11. **Coverage instrumentation**: `-C instrument-coverage` injects `llvm.instrprof.increment` intrinsic calls at MIR-based control flow branches; auto-enables `v0` symbol mangling; Coverage Map encodes source locations mapping counter IDs to file positions
12. **Sanitizer support**: Seven sanitizers (Address, CFI, HWAddress, KCFI, Leak, Memory, Thread); functions marked with LLVM attributes (`SanitizeAddress`, etc.); instrumentation passes run after optimization; runtimes from `compiler-rt` statically linked; granularity is per-function via `#[sanitize(xyz = "on|off")]`

# Construction / Recognition

## To Use Profile-Guided Optimization:
1. Compile with instrumentation: `rustc -C profile-generate main.rs`
2. Run the instrumented binary to generate `default-<id>.profraw`
3. Convert: `llvm-profdata merge -o merged.profdata default-*.profraw`
4. Recompile with profiling data: `rustc -C profile-use=merged.profdata main.rs`
5. Ensure `profiler = true` is set in bootstrap.toml for building profiler_builtins

## To Enable Coverage Instrumentation:
1. Set `build.profiler = true` in bootstrap.toml
2. Compile with `-C instrument-coverage`
3. Run the program; it writes `default.profraw` (or custom path via `LLVM_PROFILE_FILE`)
4. Use `llvm-profdata merge` and `llvm-cov show`/`llvm-cov report` for analysis
5. Recommended: use `profile = "codegen"` in bootstrap.toml for debug assertions in LLVM

## To Enable a Sanitizer on a New Target:
1. Add to `supported_sanitizers` in the target definition
2. Build the runtime and include it in the libdir
3. Teach compiletest about the new target support
4. Run `./x test --force-rerun tests/ui/sanitize/` to verify
5. Enable `--enable-sanitizers` in CI configuration for release distribution

## To Use Build Pipelining:
1. Cargo does this automatically -- no manual configuration needed
2. Rustc emits `rmeta` early, sends JSON notification to Cargo
3. Dependent crates start building with `rmeta` before `rlib` is complete
4. Only works for library dependencies; binaries must wait for full codegen of all deps

# Context & Application

This chapter covers four related but distinct backend features that share a common dependency on LLVM infrastructure. The library/metadata section explains the crate ecosystem's binary formats -- understanding `rlib`, `dylib`, and `rmeta` is essential for anyone working on the build system, incremental compilation, or cross-crate optimization.

The PGO and coverage sections demonstrate rustc's strategy of leveraging LLVM's infrastructure with minimal Rust-side maintenance. For PGO, rustc simply sets two flags on the LLVM PassManagerBuilder; for coverage, the MIR-based control flow analysis provides counter placement decisions while LLVM handles the instrumentation mechanics and runtime. The `profiler_builtins` crate packages LLVM's `compiler-rt` profiling runtime as a Rust crate.

The sanitizer section is similarly LLVM-delegated, but with more Rust-specific integration: per-function sanitizer control via attributes, inlining inhibition at both MIR and LLVM levels when sanitizer decisions differ between functions, and runtime discovery through sysroot scanning with fallback to default sysroot.

Build pipelining is a clever optimization that exploits the separation between metadata and object code: since a dependent crate only needs metadata (types, traits, macros) to proceed through its own front-end, it can begin compilation as soon as the `rmeta` file is available, without waiting for the expensive codegen phase of its dependency.

# Examples

**Example 1** (Ch. 25, PGO compile-time instrumentation): LLVM PassManager configuration:
```c
// For instrumented binary generation:
unwrap(PMBR)->EnablePGOInstrGen = true;
unwrap(PMBR)->PGOInstrGen = PGOGenPath;

// For optimized binary using profile data:
unwrap(PMBR)->PGOInstrUse = PGOUsePath;
```

**Example 2** (Ch. 25, bootstrap.toml for coverage work):
```toml
# Enable debug assertions in LLVM to detect malformed coverage mappings
profile = "codegen"

# IMPORTANT: Build the LLVM profiler runtime
build.profiler = true

# Enable debug assertions in the compiler
rust.debug-assertions = true
```

**Example 3** (Ch. 25, Sanitizer usage): Enabling AddressSanitizer:
```bash
rustc -Z sanitizer=address my_program.rs
```
The compiler marks functions with the `SanitizeAddress` LLVM attribute, LLVM runs the AddressSanitizer instrumentation pass after optimization, and the sanitizer runtime from `compiler-rt` is statically linked into the binary.

# Relationships

## Builds Upon
- LLVM's compiler-rt (provides profiling and sanitizer runtimes)
- LLVM's instrumentation passes (IR-level PGO and coverage)
- The codegen pipeline (metadata is generated alongside code)

## Enables
- Fast `cargo check` (uses rmeta without codegen)
- Build pipelining for faster parallel compilation
- Production performance tuning via PGO
- Memory safety validation via sanitizers
- Code coverage analysis for testing

## Related
- **compiler-code-generation** -- the codegen pipeline that produces the library artifacts and invokes LLVM
- **compiler-mir-optimizations** -- MIR-level analysis feeds into coverage counter placement

## Contrasts With
- Sampling-based PGO (using external profilers like `perf`) -- rustc uses IR-level instrumentation instead
- GCOV-based coverage -- rustc uses the more modern LLVM source-based coverage

# Common Errors

- **Error**: Forgetting to set `profiler = true` in bootstrap.toml when working on coverage.
  **Correction**: "Without it, the compiler can't produce coverage-instrumented binaries, and many of the coverage tests will be skipped." The profiler_builtins crate won't be built without this setting.

- **Error**: Expecting sanitizer tests to run on all platforms.
  **Correction**: "When a sanitizer is unsupported on a given target, sanitizer tests will be ignored. This behaviour is controlled by compiletest `needs-sanitizer-*` directives." Check the target's `supported_sanitizers` list.

- **Error**: Trying to link against an `rmeta` file.
  **Correction**: "rmeta files do not support linking, since they do not contain compiled object files." They are for `cargo check`, `cargo doc`, and build pipelining only.

# Common Confusions

- **Confusion**: Thinking rustc implements PGO from scratch.
  **Clarification**: "rustc's current PGO implementation relies entirely on LLVM." Rustc just sets flags on the LLVM PassManagerBuilder and ensures profiling runtime symbols are exported. LLVM does the actual instrumentation and profile-guided optimization.

- **Confusion**: Thinking build pipelining works for binary crates.
  **Clarification**: "This pipelining isn't possible for binaries, because the linking phase will require the code generation of all its dependencies." Only library dependencies benefit from pipelining.

- **Confusion**: Thinking the SVH and Stable Crate Id are the same thing.
  **Clarification**: SVH is a hash of HIR nodes, upstream hashes, filenames, and tracked CLI flags -- it validates correct dependency loading. Stable Crate Id is a hash of just the crate name and `-C metadata` options -- it disambiguates crates with the same name in symbol mangling.

# Source Reference

Chapter 25: Libraries and metadata (rlib/dylib/rmeta formats, metadata contents, SVH, Stable Crate Id, crate loading via CStore/CrateLocator, build pipelining), Profile-guided optimization (IR-level instrumentation, four-step workflow, compile-time PassManager flags, runtime via profiler_builtins/compiler-rt, testing), LLVM source-based code coverage (instrument-coverage flag, llvm.instrprof.increment intrinsic, Coverage Map, v0 symbol mangling, profiler runtime, testing with coverage/mir-opt/codegen suites), Sanitizers support (seven sanitizers, LLVM attribute marking, per-function granularity, compiler-rt runtimes, inlining inhibition, enabling on new targets).

# Verification Notes

- Definition source: Direct quotations from Ch. 25 sections on libraries/metadata, PGO, and sanitizers
- Key Properties: Covers all four major sections across 607 lines
- Confidence rationale: HIGH -- well-structured chapter with clear separation of concerns and specific implementation references
- Uncertainties: PGO code references point to specific rustc versions (1.34.1, 1.55.0) that may have changed; sanitizer CI configuration evolves
- Cross-reference status: `compiler-code-generation` and `compiler-mir-optimizations` are in this extraction set
