---
# === CORE IDENTIFICATION ===
concept: Cargo Build Scripts
slug: cargo-build-scripts

# === CLASSIFICATION ===
category: package-management
subcategory: build-system
tier: foundational

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "08-build-scripts"
chapter_number: 8
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "build.rs"
  - "build script"
  - "Cargo build script"
  - "cargo:: instructions"
  - "build-time code generation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-manifest-reference
  - cargo-environment-variables
extends: []
related:
  - cargo-features
  - cargo-profiles
  - cargo-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a build script and when does Cargo run it?"
  - "How does a build script communicate with Cargo?"
  - "What cargo:: instructions are available and what does each do?"
  - "How do I link native C/C++ libraries from a build script?"
  - "How do I generate Rust code from a build script?"
  - "What is the links manifest key and how does it enable inter-crate metadata?"
  - "What is the *-sys package convention?"
  - "How do I control when a build script re-runs (change detection)?"
  - "How do I override a build script via configuration?"
  - "What environment variables are available to build scripts?"
  - "How do build dependencies differ from regular dependencies?"
  - "How does the jobserver protocol work with build scripts?"
  - "How do I set custom cfg flags from a build script?"
  - "How do I use CARGO_CFG_* for cross-compilation in build scripts?"
---

# Quick Definition

A build script is a Rust file named `build.rs` at the package root that Cargo compiles and executes before building the package. Build scripts communicate with Cargo by printing `cargo::` prefixed instructions to stdout, enabling native library linking (`rustc-link-lib`, `rustc-link-search`), conditional compilation (`rustc-cfg`, `rustc-check-cfg`), environment variable injection (`rustc-env`), linker flag passing (`rustc-link-arg`), and inter-crate metadata exchange (`metadata`). The `links` manifest key declares native library dependencies and enables the `DEP_<links>_<key>` metadata system. Change detection is controlled via `rerun-if-changed` and `rerun-if-env-changed` instructions.

# Core Definition

The source introduces build scripts as the mechanism for packages that "need to compile third-party non-Rust code, for example C libraries" or "need facilities for functionality such as code generation before building" (Ch. 8). Cargo integrates with these tasks: "Placing a file named `build.rs` in the root of a package will cause Cargo to compile that script and execute it just before building the package."

**Life cycle**: "Cargo will compile a build script into an executable... It will then run the script, which may perform any number of tasks. The script may communicate with Cargo by printing specially formatted commands prefixed with `cargo::` to stdout." The script exits with non-zero to halt the build. Output is hidden during normal compilation; use `-vv` to see it. All output is saved to `target/debug/build/<pkg>/output`.

**Instruction system** (MSRV 1.77 for `cargo::KEY=VALUE` syntax): The key instructions are:
- `cargo::rustc-link-lib=LIB` -- link a native library (supports `dylib`, `static`, `framework` kinds)
- `cargo::rustc-link-search=[KIND=]PATH` -- add library search path
- `cargo::rustc-link-arg=FLAG` -- pass linker flags to supported targets
- `cargo::rustc-cfg=KEY[="VALUE"]` -- enable conditional compilation
- `cargo::rustc-check-cfg=CHECK_CFG` -- register expected cfg values (MSRV 1.80)
- `cargo::rustc-env=VAR=VALUE` -- set compile-time environment variable (accessible via `env!`)
- `cargo::rerun-if-changed=PATH` -- control change detection
- `cargo::rerun-if-env-changed=VAR` -- re-run if env var changes
- `cargo::metadata=KEY=VALUE` -- pass metadata to dependent packages via `DEP_<links>_<key>`
- `cargo::warning=MESSAGE` / `cargo::error=MESSAGE` -- emit diagnostics

The **`links` manifest key** declares that a package links to a native library, enforcing "at most one package per `links` value" to prevent duplicate symbols. Metadata from `cargo::metadata` is passed to immediate dependents as `DEP_<LINKS>_<KEY>` environment variables.

**Change detection**: "By default, it takes a conservative approach of always re-running the build script if any file within the package is changed." Using `rerun-if-changed` or `rerun-if-env-changed` narrows this. To prevent unnecessary re-runs, "emitting `cargo::rerun-if-changed=build.rs` is a simple way to prevent it from being re-run."

# Prerequisites

- **Cargo Manifest Reference** -- build scripts are configured via `package.build` and `links` in the manifest; dependencies go in `[build-dependencies]`
- **Cargo Environment Variables** -- build scripts receive inputs via environment variables and produce outputs that set new ones

# Key Properties

1. **Location**: `build.rs` at package root by default; configurable via `package.build` manifest key
2. **Execution timing**: compiled and run just before the package is built; rebuilt if source files or dependencies change
3. **Communication**: `cargo::` prefixed lines on stdout; all other output ignored; stderr saved alongside
4. **OUT_DIR**: designated output directory; not cleaned between builds; scripts must manage their own files
5. **rustc-link-lib**: links native libraries with optional KIND (dylib, static, framework); only passed to library target
6. **rustc-link-search**: adds library search paths; paths within OUT_DIR added to dynamic library path
7. **rustc-link-arg variants**: flags for specific target types -- bins, tests, examples, benchmarks, cdylib
8. **rustc-cfg / rustc-check-cfg**: enables conditional compilation flags; check-cfg registers expected values to avoid warnings
9. **rustc-env**: sets compile-time env vars accessible via `env!` macro in the compiled crate
10. **links key**: one package per native library; enables metadata passing via DEP_<LINKS>_<KEY>; allows build script overriding
11. **rerun-if-changed**: narrows change detection to specific files/directories; uses mtime comparison
12. **rerun-if-env-changed**: re-runs if a global environment variable changes (not Cargo-set variables)
13. **build-dependencies**: separate dependency section; not available to the package itself unless also in [dependencies]
14. **Jobserver**: build scripts inherit one job slot; use the `jobserver` crate for parallel work
15. **Instruction order**: the order of cargo:: instructions may affect argument order passed to rustc and the linker
16. **`*-sys` convention**: packages named `foo-sys` provide raw FFI bindings and link to `libfoo`; companion `foo` crate provides safe abstractions

# Construction / Recognition

## Basic Build Script (Code Generation):
```rust
// build.rs
use std::env;
use std::fs;
use std::path::Path;

fn main() {
    let out_dir = env::var_os("OUT_DIR").unwrap();
    let dest_path = Path::new(&out_dir).join("hello.rs");
    fs::write(
        &dest_path,
        "pub fn message() -> &'static str {
            \"Hello, World!\"
        }"
    ).unwrap();
    println!("cargo::rerun-if-changed=build.rs");
}
```

## Including Generated Code:
```rust
// src/main.rs
include!(concat!(env!("OUT_DIR"), "/hello.rs"));

fn main() {
    println!("{}", message());
}
```

## Building Native C Code with cc Crate:
```toml
# Cargo.toml
[build-dependencies]
cc = "1.0"
```

```rust
// build.rs
fn main() {
    cc::Build::new()
        .file("src/hello.c")
        .compile("hello");
    println!("cargo::rerun-if-changed=src/hello.c");
}
```

## Linking System Library with pkg-config:
```toml
[package]
name = "libz-sys"
version = "0.1.0"
links = "z"

[build-dependencies]
pkg-config = "0.3.16"
```

```rust
// build.rs
fn main() {
    pkg_config::Config::new().probe("zlib").unwrap();
    println!("cargo::rerun-if-changed=build.rs");
}
```

## Cross-Compilation Aware Build Script:
```rust
// build.rs
fn main() {
    let target_os = std::env::var("CARGO_CFG_TARGET_OS").unwrap();
    if target_os == "windows" {
        println!("cargo::rustc-link-lib=userenv");
    } else if target_os == "linux" {
        println!("cargo::rustc-link-lib=pthread");
    }
}
```

## Conditional Compilation with Version Detection:
```rust
// build.rs
println!("cargo::rustc-check-cfg=cfg(ossl101,ossl102)");
if let Ok(version) = env::var("DEP_OPENSSL_VERSION_NUMBER") {
    let version = u64::from_str_radix(&version, 16).unwrap();
    if version >= 0x1_00_01_00_0 {
        println!("cargo::rustc-cfg=ossl101");
    }
}
```

## Build Script Override in Config:
```toml
# .cargo/config.toml
[target.x86_64-unknown-linux-gnu.foo]
rustc-link-lib = ["foo"]
rustc-link-search = ["/path/to/foo"]
rustc-cfg = ['key="value"']
```

# Context & Application

This card covers build scripts as specified in Chapter 8 of the Cargo Reference, including the build script examples appendix. Build scripts are one of Cargo's most distinctive features, bridging the Rust build system with native code compilation, system library detection, and code generation. The `links` key and `DEP_<links>_<key>` metadata system creates a principled way for the `*-sys` package ecosystem to work: `libz-sys` declares `links = "z"` and sets `include` metadata, then `openssl-sys` can use `DEP_Z_INCLUDE` to find zlib headers. This pattern prevents duplicate native library symbols while allowing transitive consumers to find headers and configuration. The `cc` crate, `pkg-config` crate, `bindgen`, and `cmake` are the key ecosystem tools that simplify common build script tasks. Change detection via `rerun-if-changed` is critical for build performance -- without it, the build script runs on every file change in the package. The jobserver integration ensures build scripts respect Cargo's parallelism settings. Build script overriding via config enables prebuilt library integration without modifying dependencies.

# Examples

**Example 1** (Ch. 8): Basic build script with the cc crate:
```rust
fn main() {
    println!("cargo::rerun-if-changed=src/hello.c");
    cc::Build::new()
        .file("src/hello.c")
        .compile("hello");
}
```
> "The `cc` crate abstracts a range of build script requirements for C code: It invokes the appropriate compiler (MSVC for windows, `gcc` for MinGW, `cc` for Unix platforms, etc.)."

**Example 2** (Ch. 8): Inter-crate metadata via `links` key:
> "If the package `foo` depends on `bar`, which links `baz`, then if `bar` generates `key=value` as part of its build script metadata, then the build script of `foo` will have the environment variables `DEP_BAZ_KEY=value`."

**Example 3** (Ch. 8): Change detection to prevent unnecessary re-runs:
> "If the build script inherently does not need to re-run under any circumstance, then emitting `cargo::rerun-if-changed=build.rs` is a simple way to prevent it from being re-run."

**Example 4** (Ch. 8): The `*-sys` package convention:
> "Any package named `foo-sys` should provide two major pieces of functionality: The library crate should link to the native library `libfoo`. This will often probe the current system for `libfoo` before resorting to building from source. The library crate should provide **declarations** for types and functions in `libfoo`, but **not** higher-level abstractions."

**Example 5** (Ch. 8): OpenSSL conditional compilation using build script metadata and cfg:
```rust
// openssl crate's build.rs reads version from openssl-sys
if let Ok(version) = env::var("DEP_OPENSSL_VERSION_NUMBER") {
    let version = u64::from_str_radix(&version, 16).unwrap();
    if version >= 0x1_01_01_00_0 {
        println!("cargo::rustc-cfg=ossl111");
    }
}
```
> "These `cfg` values can then be used with the `cfg` attribute or the `cfg` macro to conditionally include code."

# Relationships

## Builds Upon
- **Cargo Manifest Reference** -- `package.build` names the script, `links` declares native deps, `[build-dependencies]` provides build-time deps
- **Cargo Environment Variables** -- build scripts receive all inputs as env vars and produce outputs that set new env vars

## Enables
- Native C/C++ library compilation and linking
- System library detection and probing
- Compile-time code generation (parser generators, FFI bindings, proto compilation)
- Platform-specific conditional compilation for cross-compilation
- Inter-crate native dependency metadata (the `*-sys` ecosystem)
- Custom cfg flags for version-specific API exposure

## Related
- **cargo-features** -- features are visible to build scripts via `CARGO_FEATURE_<name>` env vars
- **cargo-profiles** -- profile settings like `OPT_LEVEL` and `DEBUG` are available to build scripts
- **cargo-configuration** -- build scripts can be overridden via `[target.<triple>.<links>]` in config

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `cfg!` or `#[cfg(target_os = "...")]` in a build script for target platform detection.
  **Correction**: "When checking configuration options like `target_os` or `target_arch` in a build script, do not use the `cfg!` macro or `#[cfg]` attribute, these check the **host** machine (where the build script runs), not the **target** platform." Use `CARGO_CFG_*` environment variables instead.

- **Error**: Modifying files outside of `OUT_DIR` from a build script.
  **Correction**: "In general, build scripts should not modify any files outside of `OUT_DIR`." Cargo requires immutability of `.cargo/registry` sources and "won't allow such scripts when packaging."

- **Error**: Expecting `OUT_DIR` to be empty at the start of each build.
  **Correction**: "Cargo does not clean or reset `OUT_DIR` between builds. The contents of this directory may persist across rebuilds." Build scripts "should not rely on `OUT_DIR` being empty."

- **Error**: Assuming build dependencies are available to the package's runtime code.
  **Correction**: "The build script **does not** have access to the dependencies listed in the `dependencies` or `dev-dependencies` section (they're not built yet!). Also, build dependencies are not available to the package itself unless also explicitly added in the `[dependencies]` table."

- **Error**: Omitting `rerun-if-changed` and wondering why the build script runs on every change.
  **Correction**: "By default, it takes a conservative approach of always re-running the build script if any file within the package is changed." Add `rerun-if-changed` instructions to narrow the trigger.

# Common Confusions

- **Confusion**: Thinking `rustc-cfg` can enable Cargo features or optional dependencies.
  **Clarification**: "Note that this does *not* affect Cargo's dependency resolution. This cannot be used to enable an optional dependency, or enable other Cargo features." It only affects `#[cfg]` conditional compilation.

- **Confusion**: Thinking `links` metadata propagates transitively.
  **Clarification**: "Metadata is only passed to immediate dependents, not transitive dependents." Only direct dependents receive `DEP_<links>_<key>` values.

- **Confusion**: Thinking `cargo::warning` messages always appear.
  **Clarification**: "Warnings are only shown for `path` dependencies (that is, those you're working on locally)." Warnings from crates.io crates are suppressed by default; use `-vv` to see them.

- **Confusion**: Thinking `rerun-if-env-changed` works with Cargo-set variables like `TARGET`.
  **Clarification**: "The environment variables here are intended for global environment variables like `CC` and such, it is not possible to use this for environment variables like `TARGET` that Cargo sets for build scripts."

# Source Reference

Chapter 8: Build Scripts -- sections on life cycle of a build script, inputs (environment variables), outputs (cargo:: instructions), all instruction types (rustc-link-arg variants, rustc-link-lib, rustc-link-search, rustc-flags, rustc-cfg, rustc-check-cfg, rustc-env, error, warning), build dependencies, change detection (rerun-if-changed, rerun-if-env-changed), the links manifest key, `*-sys` packages, overriding build scripts, jobserver. Also includes Build Script Examples: code generation, building a native library, linking to system libraries, using another sys crate, reading target configuration, and conditional compilation. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 8 -- "Placing a file named `build.rs` in the root of a package will cause Cargo to compile that script and execute it just before building the package"
- Confidence rationale: HIGH -- comprehensive coverage of the complete build script system with instruction reference, lifecycle, change detection, metadata system, and multiple real-world examples (cc, pkg-config, openssl-sys, libz-sys)
- Uncertainties: MSRV requirements (1.77 for `cargo::` syntax, 1.80 for `rustc-check-cfg`, 1.84 for `cargo::error`); OUT_DIR cleanup behavior may evolve per GitHub issues #16427 and #9661
- Cross-reference status: References cargo-manifest-reference (Ch. 1), cargo-environment-variables (Ch. 7), cargo-configuration (Ch. 6), cargo-features (Ch. 4)
