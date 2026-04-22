---
# === CORE IDENTIFICATION ===
concept: Compiler CLI and Drivers
slug: compiler-cli-and-drivers

# === CLASSIFICATION ===
category: compiler-internals
subcategory: driver-and-interface
tier: advanced

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "CLI and Drivers"
chapter_number: 16
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc_driver"
  - "rustc_interface"
  - "rustc command-line arguments"
  - "Callbacks trait"
  - "rustc_private"
  - "external rustc drivers"
  - "compiler as a library"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - compiler-syntax-and-ast
  - compiler-hir
  - compiler-mir
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is rustc_driver and how does it relate to rustc_interface?"
  - "How do you use the Callbacks trait to hook into compilation phases?"
  - "What are the guidelines for adding new command-line flags to rustc?"
  - "How do you use rustc_interface to drive the compiler programmatically?"
  - "What is rustc_private and how do external tools use compiler internals?"
  - "How do you get the type of an expression using rustc_driver?"
  - "How do you intercept diagnostics using rustc_interface?"
  - "What components are needed to use rustc_private with official toolchains?"
---

# Quick Definition

The Rust compiler's entry point and programmatic interface are provided by two crates: `rustc_driver` (essentially `rustc`'s `main` function, which orchestrates compilation phases in the correct order) and `rustc_interface` (a low-level API that allows third parties to manually drive the compilation process). Command-line flag design follows specific guidelines (orthogonality, no `no-` prefixes, long descriptive names, experimental flags behind `-Z unstable-options`). External tools can access compiler internals through the `rustc_private` feature, with the `rustc-dev` and `llvm-tools` components providing the necessary libraries.

# Core Definition

**`rustc_driver`** acts as the glue for running the compiler's phases in order, using the interface defined in `rustc_interface`. Its main entry point is `rustc_driver::run_compiler`, which accepts command-line arguments (the same ones `rustc` accepts), an implementation of `Callbacks`, and optional configuration. The `Callbacks` trait allows custom compiler configuration and execution of custom code after different compilation phases. Where possible, using `rustc_driver` is recommended over `rustc_interface`.

**`rustc_interface`** provides a lower-level API for manually driving compilation. Its entry point, `rustc_interface::run_compiler`, takes a configuration and a closure receiving an unresolved `Compiler`. Inside the closure, the `Compiler` can be used to invoke various compilation functions. This is used when `rustc_driver` is not flexible enough -- for example, `rustdoc` uses it to compile code and serve custom output. The reference implementation is in `rustc_driver_impl::run_compiler`.

**Command-line flag guidelines** specify: flags should be orthogonal (prefer `--json` over `--foo-json` and `--bar-json`); avoid `no-` prefixes (use `parse_bool` like `-C embed-bitcode=no`); consider behavior when a flag is passed multiple times (accumulate, override, or error); always give long descriptive names; experimental flags must be guarded behind `-Z unstable-options`.

**`rustc_private`** allows external crates to use compiler internals. With official toolchains, this requires installing `rustc-dev` (compiler libraries) and `llvm-tools` (LLVM libraries for linking). Without `llvm-tools`, linking fails with `error: linking with cc failed ... unable to find library -lLLVM-{version}`. For `rust-analyzer` support in out-of-tree `rustc_private` projects, configure `rust-analyzer.rustc.source` to `"discover"` and add `rustc_private = true` to `[package.metadata.rust-analyzer]`.

The compiler's internal APIs are inherently unstable, though the team tries not to break things unnecessarily.

# Prerequisites

General understanding of the Rust compiler pipeline. Familiarity with the query system is helpful for understanding how compilation phases are driven.

# Key Properties

1. **Two-tier architecture**: `rustc_driver` provides a high-level compilation orchestrator; `rustc_interface` provides low-level, phase-by-phase control
2. **Callbacks trait**: Allows external code to hook into compilation at specific phases (e.g., `after_analysis` for accessing `TyCtxt`)
3. **Flag orthogonality**: Command-line flags should be composable and independent, not creating combinatorial variants
4. **Experimental flag gating**: Unstable flags require `-Z unstable-options`
5. **Multiple-pass behavior**: Flags must define semantics for repeated use -- accumulate (ordered), override, or error
6. **rustc_private requires two components**: `rustc-dev` for compiler libraries and `llvm-tools` for LLVM linking libraries
7. **Unstable internal APIs**: All compiler internals accessed via `rustc_private` are unstable and subject to change

# Construction / Recognition

## Using rustc_driver for type checking:
The `after_analysis` callback provides access to `TyCtxt`, enabling type queries on HIR expressions. This is the standard way to interact with analyzed Rust code programmatically.

## Using rustc_interface for diagnostics:
Configure `rustc_interface::Config` to output diagnostics to a buffer, then run `TyCtxtEnsureOk::typeck` for each item to collect diagnostics programmatically rather than printing to stderr.

## Setting up rustc_private:
```console
$ rustup component add rustc-dev llvm-tools
```

## Configuring rust-analyzer for rustc_private:
In VS Code settings:
```json
{ "rust-analyzer.rustc.source": "discover" }
```
In each crate's `Cargo.toml`:
```toml
[package.metadata.rust-analyzer]
rustc_private = true
```

## Getting nightly-specific internal documentation:
```console
$ rustup toolchain install nightly-2025-11-08
$ rustc +nightly-2025-11-08 --version --verbose
# Use the commit-hash to check out rust-lang/rust at that revision
# Then build docs locally
```

# Context & Application

Understanding `rustc_driver` and `rustc_interface` is essential for:
- Building custom linting tools that leverage the full compiler pipeline
- Creating analysis tools that need type information, borrow-checker results, or other compiler outputs
- Building alternatives to `rustdoc` or other documentation tools
- Implementing language servers or IDE integrations that need deep compiler access
- Understanding how `rustdoc`, `clippy`, and other official tools interface with the compiler

The CLI guidelines matter for anyone proposing new compiler flags, ensuring consistency across the `rustc` interface.

# Examples

**Example 1** (Ch. 16, "Getting the type of an expression"): Using `rustc_driver` with the `after_analysis` callback to obtain a `TyCtxt` and query expression types:
```rust,ignore
// Use the after_analysis callback:
impl Callbacks for MyCallbacks {
    fn after_analysis(&mut self, compiler: &Compiler) -> Compilation {
        // Access TyCtxt here to query types
        Compilation::Continue
    }
}
```

**Example 2** (Ch. 16, "Intercepting diagnostics"): Using `rustc_interface::Config` to redirect diagnostics to a buffer instead of stderr, then running `typeck` for each item to collect type-checking diagnostics programmatically.

**Example 3** (Ch. 16, "CLI guidelines"): Prefer `-C embed-bitcode=no` (using `parse_bool`) over introducing a separate `--no-embed-bitcode` flag. Prefer a single `--json` flag over `--foo-json` and `--bar-json`.

**Example 4** (Ch. 16, "Common linking error without llvm-tools"):
```text
error: linking with `cc` failed: exit status: 1
  = note: rust-lld: error: unable to find library -lLLVM-{version}
```
This is resolved by installing the `llvm-tools` component via `rustup`.

# Relationships

## Builds Upon
(none -- `rustc_driver` is the top-level entry point that orchestrates everything else)

## Enables
- **compiler-syntax-and-ast** -- the driver triggers parsing and macro expansion
- **compiler-hir** -- the driver triggers AST lowering
- **compiler-mir** -- the driver triggers MIR construction and optimization

## Related
- **rustdoc-internals** -- rustdoc uses `rustc_interface` to drive compilation before taking over for documentation generation

## Contrasts With
(none within this source)

# Common Errors

- **Error**: Using `rustc_private` without installing `llvm-tools`, resulting in linker errors about missing LLVM libraries.
  **Correction**: Run `rustup component add rustc-dev llvm-tools` to install both required components.

- **Error**: Creating compiler flags with `no-` prefixes.
  **Correction**: Use the `parse_bool` function to allow flags like `-C embed-bitcode=no` instead of creating separate `--no-embed-bitcode` flags.

- **Error**: Not guarding experimental flags behind `-Z unstable-options`.
  **Correction**: All experimental flags and options must require `-Z unstable-options` to be passed first.

# Common Confusions

- **Confusion**: `rustc_driver` and `rustc_interface` are interchangeable.
  **Clarification**: `rustc_driver` is the higher-level API that orchestrates compilation phases in order. `rustc_interface` is the lower-level API for manual, fine-grained control. The recommendation is to prefer `rustc_driver` unless its flexibility is insufficient.

- **Confusion**: `rustc_private` provides a stable API for accessing compiler internals.
  **Clarification**: All internal compiler APIs accessed via `rustc_private` are inherently unstable and may change without notice. The team tries to avoid unnecessary breakage, but stability is not guaranteed.

- **Confusion**: The nightly-rustc documentation always matches your toolchain version.
  **Clarification**: The nightly-rustc docs are only published for the latest nightly. If you depend on an older nightly, you must generate documentation locally by checking out `rust-lang/rust` at the specific commit hash for your toolchain version.

# Source Reference

Chapter 16 of the Rust Compiler Dev Guide (213 lines). Covers: command-line argument guidelines (orthogonality, no `no-` prefix, `parse_bool`, multiple-pass behavior, experimental flag gating), `rustc_driver` (entry point, `run_compiler`, `Callbacks` trait), `rustc_interface` (low-level API, `run_compiler`, `Compiler` type), external drivers and `rustc_private` (overview, `rustc-dev`/`llvm-tools` components, common linking errors, `rust-analyzer` configuration, nightly documentation generation), and examples of type checking and diagnostic interception through the driver APIs.

# Verification Notes

- Definition source: Directly extracted from Chapter 16 sections on CLI arguments, rustc_driver, rustc_interface, and rustc_private
- Key Properties: All derived from explicit descriptions in the source text
- Confidence rationale: HIGH -- official compiler team documentation describing the stable driver architecture
- Uncertainties: The internal APIs are explicitly described as unstable; specific API signatures may change
- Cross-reference status: This is the orchestration layer that drives all other compiler stages
