---
# === CORE IDENTIFICATION ===
concept: Cargo Environment Variables
slug: cargo-environment-variables

# === CLASSIFICATION ===
category: package-management
subcategory: build-environment
tier: foundational

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "07-environment-variables"
chapter_number: 7
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cargo env vars"
  - "CARGO_PKG variables"
  - "build script environment"
  - "compile-time environment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-manifest-reference
  - cargo-configuration
extends: []
related:
  - cargo-profiles
  - cargo-build-scripts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What environment variables does Cargo read to control its behavior?"
  - "What environment variables does Cargo set for crates during compilation?"
  - "What environment variables does Cargo set specifically for build scripts?"
  - "How do I access CARGO_PKG_VERSION and other package metadata at compile time?"
  - "How do configuration keys map to CARGO_ environment variable names?"
  - "What is the difference between env! and std::env::var for Cargo-set variables?"
  - "What dynamic library path variables does Cargo set for cargo run and cargo test?"
  - "How do CARGO_CFG_* variables work in build scripts?"
  - "What variables are available during cargo test execution?"
  - "How do I use RUSTFLAGS vs CARGO_ENCODED_RUSTFLAGS?"
  - "What is CARGO_HOME and what does it contain?"
  - "What environment variables are set for third-party subcommands?"
---

# Quick Definition

Cargo uses environment variables in four distinct contexts: variables Cargo reads to control its own behavior (like `CARGO_HOME`, `RUSTC`, `RUSTFLAGS`), variables Cargo sets for crates during compilation (like `CARGO_PKG_VERSION`, `CARGO_MANIFEST_DIR`, `OUT_DIR`), variables Cargo sets specifically for build scripts (like `TARGET`, `HOST`, `OPT_LEVEL`, `CARGO_CFG_*`), and variables set during test execution. Compile-time variables are accessed via `env!()`, while build script variables use `std::env::var()` since they are not available at the build script's compile time.

# Core Definition

The source organizes environment variables into five categories (Ch. 7):

**Variables Cargo reads**: These override Cargo's behavior, including `CARGO_HOME` (cache/registry location, defaults to `$HOME/.cargo`), `RUSTC`/`RUSTDOC` (compiler overrides), `RUSTFLAGS`/`RUSTDOCFLAGS` (extra compiler flags), `RUSTC_WRAPPER`/`RUSTC_WORKSPACE_WRAPPER` (build cache tools like sccache), and `CARGO_INCREMENTAL` (force incremental compilation on/off). Configuration environment variables follow the pattern `CARGO_FOO_BAR` for config key `foo.bar`.

**Variables Cargo sets for crates**: Available at compile time via `env!("CARGO_PKG_VERSION")`. These include all `CARGO_PKG_*` variables from the manifest (version, name, authors, description, homepage, etc.), `CARGO_MANIFEST_DIR`, `CARGO_CRATE_NAME`, `OUT_DIR`, `CARGO_BIN_EXE_<name>` for integration tests, and `CARGO_PRIMARY_PACKAGE`.

**Variables Cargo sets for build scripts**: Must use `std::env::var()` at runtime. These include `TARGET` and `HOST` triples, `OUT_DIR`, `OPT_LEVEL`, `DEBUG`, `PROFILE`, `NUM_JOBS`, `CARGO_CFG_<cfg>` for all target configuration values, `CARGO_FEATURE_<name>` for enabled features, `DEP_<links>_<key>` for metadata from dependency build scripts, and `CARGO_ENCODED_RUSTFLAGS`.

**Dynamic library paths**: Cargo sets platform-specific library paths (`LD_LIBRARY_PATH` on Unix, `DYLD_FALLBACK_LIBRARY_PATH` on macOS, `PATH` on Windows) to include build output directories.

# Prerequisites

- **Cargo Manifest Reference** -- many env vars are derived from manifest fields
- **Cargo Configuration** -- configuration keys have corresponding env var names

# Key Properties

1. **CARGO_HOME**: defaults to `$HOME/.cargo`; contains registry index, git checkouts, installed binaries
2. **RUSTC/RUSTDOC**: override the compiler and doc generator executables
3. **RUSTC_WRAPPER**: wraps all rustc invocations (for sccache etc.); first arg is path to actual rustc
4. **RUSTC_WORKSPACE_WRAPPER**: wraps rustc only for workspace members; affects filename hash for separate caching
5. **RUSTFLAGS/CARGO_ENCODED_RUSTFLAGS**: extra compiler flags; encoded version uses `0x1f` separator for robust multi-arg encoding
6. **CARGO_PKG_***: compile-time metadata -- VERSION, VERSION_MAJOR/MINOR/PATCH/PRE, NAME, AUTHORS, DESCRIPTION, etc.
7. **CARGO_MANIFEST_DIR**: directory containing the package manifest; also build script's starting working directory
8. **OUT_DIR**: build script output directory; not cleaned between builds; used with `include!` macro
9. **CARGO_CFG_***: target configuration in build scripts -- TARGET_OS, TARGET_ARCH, TARGET_FAMILY, TARGET_FEATURE, etc.; multi-valued cfgs are comma-delimited
10. **CARGO_FEATURE_<name>**: present in build scripts for each enabled feature; name is uppercased with `-` as `_`
11. **DEP_<links>_<key>**: metadata from dependency build scripts using the `links` manifest key; only immediate dependents
12. **CARGO_BIN_EXE_<name>**: absolute path to binary executable; only set during integration tests and benchmarks
13. **CARGO_PRIMARY_PACKAGE**: set when the package being built was selected by the user (not a dependency)
14. **Dynamic library paths**: platform-specific (PATH/DYLD_FALLBACK_LIBRARY_PATH/LD_LIBRARY_PATH) for cargo run/test

# Construction / Recognition

## Accessing Compile-Time Variables in Code:
```rust
let version = env!("CARGO_PKG_VERSION");
let name = env!("CARGO_PKG_NAME");
```

## Accessing Variables in Build Scripts (runtime):
```rust
use std::env;
let out_dir = env::var("OUT_DIR").unwrap();
let target = env::var("TARGET").unwrap();
let target_os = env::var("CARGO_CFG_TARGET_OS").unwrap();
```

## Including Generated Code via OUT_DIR:
```rust
include!(concat!(env!("OUT_DIR"), "/generated.rs"));
```

## Checking Features in Build Scripts:
```rust
// CARGO_FEATURE_MY_FEATURE is set if "my-feature" is enabled
if env::var("CARGO_FEATURE_MY_FEATURE").is_ok() {
    println!("cargo::rustc-cfg=has_my_feature");
}
```

## Overriding Cargo Behavior via Env Vars:
```console
RUSTC_WRAPPER=sccache cargo build
CARGO_INCREMENTAL=0 cargo build --release
CARGO_TARGET_DIR=/tmp/build cargo build
```

## Configuration Env Var Pattern:
```console
# config key: build.jobs -> env var: CARGO_BUILD_JOBS
CARGO_BUILD_JOBS=4 cargo build

# config key: target.x86_64-unknown-linux-gnu.runner
CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_RUNNER="my-runner" cargo test
```

# Context & Application

This card covers the environment variable system as specified in Chapter 7 of the Cargo Reference. The environment variable system serves as both a communication mechanism between Cargo and the code it compiles, and as an override mechanism for Cargo's own configuration. The compile-time variables (`CARGO_PKG_*`) are essential for embedding version information and metadata in binaries. The build script variables (`CARGO_CFG_*`, `TARGET`, `DEP_*`) are the primary way build scripts make platform-aware decisions during cross-compilation -- critically, the source warns that `cfg!` and `#[cfg]` in build scripts check the *host* platform, not the target, making `CARGO_CFG_*` the correct choice. The wrapper variables (`RUSTC_WRAPPER`, `RUSTC_WORKSPACE_WRAPPER`) enable build caching tools like sccache. The configuration env vars provide a twelve-factor-app style override mechanism for CI/CD pipelines.

# Examples

**Example 1** (Ch. 7): Accessing package version at compile time:
```rust
let version = env!("CARGO_PKG_VERSION");
```
> "Note that if one of these values is not provided in the manifest, the corresponding environment variable is set to the empty string."

**Example 2** (Ch. 7): Build script reading target configuration for cross-compilation:
> "`CARGO_CFG_TARGET_OS=macos` --- The target operating system. `CARGO_CFG_TARGET_ARCH=x86_64` --- The CPU target architecture. `CARGO_CFG_TARGET_FAMILY=unix,wasm` --- The target family."

**Example 3** (Ch. 7): Wrapper nesting when both are set:
> "If both `RUSTC_WRAPPER` and `RUSTC_WORKSPACE_WRAPPER` are set, then they will be nested: the final invocation is `$RUSTC_WRAPPER $RUSTC_WORKSPACE_WRAPPER $RUSTC`."

**Example 4** (Ch. 7): Dynamic library paths per platform:
> "Windows: `PATH`, macOS: `DYLD_FALLBACK_LIBRARY_PATH`, Unix: `LD_LIBRARY_PATH`, AIX: `LIBPATH`"

**Example 5** (Ch. 7): Build script runtime variable access (not compile-time):
```rust
use std::env;
let out_dir = env::var("OUT_DIR").unwrap();
```
> "Because these variables are not yet set when the build script is compiled, the above example using `env!` won't work and instead you'll need to retrieve the values when the build script is run."

# Relationships

## Builds Upon
- **Cargo Manifest Reference** -- `CARGO_PKG_*` variables are derived from manifest fields
- **Cargo Configuration** -- config keys map to `CARGO_` env vars with a systematic naming convention

## Enables
- Compile-time embedding of package metadata via `env!` macro
- Platform-aware build scripts via `CARGO_CFG_*` variables
- Build caching integration via `RUSTC_WRAPPER`
- CI/CD configuration via env var overrides
- Inter-crate build metadata communication via `DEP_<links>_<key>`

## Related
- **cargo-profiles** -- profile settings are accessible in build scripts via `OPT_LEVEL`, `DEBUG`, `PROFILE`
- **cargo-build-scripts** -- build scripts are the primary consumer of the build-time env vars

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `env!("OUT_DIR")` in a build script to get the output directory.
  **Correction**: "Because these variables are not yet set when the build script is compiled, the above example using `env!` won't work and instead you'll need to retrieve the values when the build script is run" using `std::env::var("OUT_DIR")`.

- **Error**: Using `cfg!` or `#[cfg(target_os = "...")]` in a build script for cross-compilation decisions.
  **Correction**: The `cfg!` macro and `#[cfg]` attributes in build scripts check the *host* platform. Use `CARGO_CFG_TARGET_OS` and other `CARGO_CFG_*` variables which reflect the *target* platform.

- **Error**: Setting `RUSTFLAGS` in the environment and wondering why `CARGO_ENCODED_RUSTFLAGS` in build scripts does not reflect them.
  **Correction**: Since Rust 1.55, "`RUSTFLAGS` is removed from the environment; scripts should use `CARGO_ENCODED_RUSTFLAGS` instead."

- **Error**: Expecting `CARGO_BIN_EXE_<name>` to be available during regular compilation.
  **Correction**: "This is only set when building an integration test or benchmark."

# Common Confusions

- **Confusion**: Thinking `CARGO_PKG_RUST_VERSION` contains the current Rust compiler version.
  **Clarification**: "This is the minimum Rust version supported by the package, not the current Rust version." It comes from the `rust-version` field in the manifest.

- **Confusion**: Thinking `DEP_<links>_<key>` metadata propagates transitively.
  **Clarification**: "Metadata is only passed to immediate dependents, not transitive dependents." Only direct dependents of a `links`-declaring package see its metadata.

- **Confusion**: Thinking `PROFILE` in build scripts reliably indicates optimization settings.
  **Clarification**: The source states: "Using this environment variable is not recommended. Using other environment variables like `OPT_LEVEL` provide a more correct view of the actual settings being used."

- **Confusion**: Thinking `CARGO_CFG_*` variables with multiple values are separate env vars.
  **Clarification**: "Configurations with multiple values are joined to a single variable with the values delimited by `,`." For example, `CARGO_CFG_TARGET_FAMILY=unix,wasm`.

# Source Reference

Chapter 7: Environment Variables -- sections on environment variables Cargo reads (including configuration env vars), variables Cargo sets for crates, dynamic library paths, variables Cargo sets for build scripts, variables Cargo sets for `cargo test`, and variables Cargo sets for 3rd party subcommands. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 7 -- "Cargo sets and reads a number of environment variables which your code can detect or override"
- Confidence rationale: HIGH -- exhaustive enumeration of all env vars across all contexts with clear descriptions of when and how each is set
- Uncertainties: The `CARGO_CFG_*` set varies by target triple; some cfg values like `test` are not available in build scripts; RUSTFLAGS removal behavior since 1.55
- Cross-reference status: References cargo-configuration (Ch. 6), cargo-profiles (Ch. 5), cargo-build-scripts (Ch. 8)
