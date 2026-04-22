---
# === CORE IDENTIFICATION ===
concept: Cargo Profiles
slug: cargo-profiles

# === CLASSIFICATION ===
category: package-management
subcategory: compilation-settings
tier: foundational

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "05-profiles"
chapter_number: 5
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "build profiles"
  - "compiler profiles"
  - "optimization profiles"
  - "release profile"
  - "dev profile"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-manifest-reference
extends: []
related:
  - cargo-configuration
  - cargo-build-cache
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Cargo's built-in profiles and when is each used?"
  - "How do I configure optimization levels, debug info, and LTO in Cargo?"
  - "What are the default settings for the dev and release profiles?"
  - "How do I create a custom profile that inherits from an existing one?"
  - "How do I override profile settings for specific dependencies?"
  - "What is the build-override table and when should I use it?"
  - "What are the tradeoffs between thin LTO and fat LTO?"
  - "How do codegen-units affect compile time and runtime performance?"
  - "Why might overriding optimization for a generic-heavy crate not help?"
  - "How does the panic setting interact with tests and build scripts?"
  - "What profile settings can be overridden per-package vs globally?"
  - "How do I use --profile to select a custom profile?"
---

# Quick Definition

Cargo profiles control compiler settings like optimization level, debug info, LTO, and panic strategy. There are four built-in profiles -- `dev` (for builds/runs), `release` (for `--release` and `cargo install`), `test` (inherits dev), and `bench` (inherits release) -- plus support for user-defined custom profiles via the `[profile]` table in `Cargo.toml`. Profile settings can be overridden per-package with `[profile.<name>.package.<pkg>]` and for build scripts/proc macros with `[profile.<name>.build-override]`.

# Core Definition

The source defines profiles as providing "a way to alter the compiler settings, influencing things like optimizations and debugging symbols" (Ch. 5). Profiles are declared in `Cargo.toml` with the `[profile]` table, and "Cargo only looks at the profile settings in the `Cargo.toml` manifest at the root of the workspace. Profile settings defined in dependencies will be ignored."

The four **built-in profiles** map to commands: `dev` is the default for `cargo build`/`cargo run`/`cargo check`; `release` for `cargo install` and `--release`; `test` inherits `dev` settings; `bench` inherits `release` settings. Each profile configures a comprehensive set of compiler flags: `opt-level`, `debug`, `split-debuginfo`, `strip`, `debug-assertions`, `overflow-checks`, `lto`, `panic`, `incremental`, `codegen-units`, `rpath`, and `frame-pointers`.

**Custom profiles** require an `inherits` key specifying which built-in profile to extend: `[profile.release-lto] inherits = "release"`. Output goes to `target/<profile-name>/`.

The **override system** has a clear precedence: (1) named package `[profile.dev.package.name]`, (2) wildcard `[profile.dev.package."*"]` for non-workspace members, (3) `build-override` for build scripts and proc macros, (4) the profile in `Cargo.toml`, (5) built-in defaults. Overrides cannot specify `panic`, `lto`, or `rpath`.

# Prerequisites

- **Cargo Manifest Reference** -- profiles are declared in the `[profile]` table of `Cargo.toml`

# Key Properties

1. **opt-level**: 0 (none), 1 (basic), 2 (some), 3 (all), "s" (size), "z" (size, no loop vectorization); dev defaults to 0, release to 3
2. **debug**: controls `-C debuginfo`; false/"none", "line-tables-only", "limited", true/"full"; dev defaults to true, release to false
3. **lto**: false (thin local), true/"fat" (whole-program), "thin" (faster than fat, similar gains), "off" (disabled)
4. **panic**: "unwind" (default) or "abort"; tests/benchmarks/build scripts/proc macros ignore this and always use unwind
5. **incremental**: enabled by default for dev, disabled for release; overridable via `CARGO_INCREMENTAL` env var
6. **codegen-units**: 256 for incremental, 16 for non-incremental; more units = faster compile but potentially slower code
7. **debug-assertions**: enables `cfg(debug_assertions)` and `debug_assert!`; on for dev, off for release
8. **overflow-checks**: runtime integer overflow panics; on for dev, off for release
9. **strip**: "none", "debuginfo", or "symbols" (true = "symbols"); removes data from binaries
10. **split-debuginfo**: controls whether debug info is embedded or placed adjacent; default is `unpacked` on macOS
11. **frame-pointers**: "force-on", "force-off", or "default"; useful for profiling
12. **build-override defaults**: opt-level=0, codegen-units=256, debug=false by default for all profiles to keep build scripts fast

# Construction / Recognition

## Basic Profile Configuration:
```toml
[profile.dev]
opt-level = 1               # Use slightly better optimizations.
overflow-checks = false     # Disable integer overflow checks.
```

## Custom Profile:
```toml
[profile.release-lto]
inherits = "release"
lto = true
```

```console
cargo build --profile release-lto
```

## Per-Package Override:
```toml
# The `foo` package will use the -Copt-level=3 flag.
[profile.dev.package.foo]
opt-level = 3
```

## Wildcard Override for All Dependencies:
```toml
# Set the default for dependencies.
[profile.dev.package."*"]
opt-level = 2
```

## Build Script Override:
```toml
# Set the settings for build scripts and proc-macros.
[profile.dev.build-override]
opt-level = 3
```

## Release Profile with Strip:
```toml
[profile.release]
strip = "debuginfo"
```

# Context & Application

This card covers compilation profiles as specified in Chapter 5 of the Cargo Reference. Profiles are the primary mechanism for controlling the performance-vs-debuggability tradeoff in Rust builds. The dev profile prioritizes fast compilation and debugging (opt-level 0, full debug info, incremental compilation, 256 codegen units), while release prioritizes runtime performance (opt-level 3, no debug info, 16 codegen units). The override system is particularly important for optimizing development builds -- the common pattern of `[profile.dev.package."*"] opt-level = 2` speeds up dependencies while keeping your own code at opt-level 0 for fast recompiles. The generic code instantiation caveat is a subtle but important design consideration: raising a dependency's opt-level may not help if its generic functions are monomorphized in your crate. Custom profiles enable CI/CD workflows like separate profiles for profiling (with frame pointers) or distribution (with LTO and stripping).

# Examples

**Example 1** (Ch. 5): Default dev profile settings showing the fast-compile-friendly defaults:
```toml
[profile.dev]
opt-level = 0
debug = true
split-debuginfo = '...'  # Platform-specific.
strip = "none"
debug-assertions = true
overflow-checks = true
lto = false
panic = 'unwind'
incremental = true
codegen-units = 256
rpath = false
```

**Example 2** (Ch. 5): Default release profile settings showing the performance-oriented defaults:
```toml
[profile.release]
opt-level = 3
debug = false
strip = "none"
debug-assertions = false
overflow-checks = false
lto = false
panic = 'unwind'
incremental = false
codegen-units = 16
rpath = false
```

**Example 3** (Ch. 5): Custom profile inheriting from release with LTO enabled:
```toml
[profile.release-lto]
inherits = "release"
lto = true
```
> "The output for each profile will be placed in a directory of the same name as the profile in the `target` directory."

**Example 4** (Ch. 5): Override precedence for package-specific settings:
> "1. `[profile.dev.package.name]` --- A named package. 2. `[profile.dev.package."*"]` --- For any non-workspace member. 3. `[profile.dev.build-override]` --- Only for build scripts, proc macros, and their dependencies. 4. `[profile.dev]` --- Settings in `Cargo.toml`. 5. Default values built-in to Cargo."

**Example 5** (Ch. 5): Frame pointers for profiling in release builds:
```toml
[profile.release]
frame-pointers = "force-on"
```

# Relationships

## Builds Upon
- **Cargo Manifest Reference** -- profiles are configured in the `[profile]` table of the package manifest

## Enables
- Optimized release builds with LTO and stripping
- Fast development iteration with incremental compilation and low optimization
- Per-dependency optimization tuning for development builds
- Custom profiles for CI/CD pipelines (profiling, distribution, testing variants)

## Related
- **cargo-configuration** -- profiles can also be specified and overridden via config files and environment variables
- **cargo-build-cache** -- profile selection affects the target directory structure and caching behavior

## Contrasts With
- None within this source

# Common Errors

- **Error**: Setting a high optimization level for a generic-heavy dependency and expecting speedup.
  **Correction**: "If you attempt to raise the optimization level of a dependency which defines generic functions, those generic functions may not be optimized when used in your local crate" because generic code is instantiated where it is used, not where it is defined. Consider opt-level 1 which still allows sharing monomorphized generics.

- **Error**: Trying to override `panic`, `lto`, or `rpath` in per-package overrides.
  **Correction**: "Overrides cannot specify the `panic`, `lto`, or `rpath` settings." These are whole-program settings that must be set at the profile level.

- **Error**: Assuming `panic = "abort"` applies to tests.
  **Correction**: "Tests, benchmarks, build scripts, and proc macros ignore the `panic` setting. The `rustc` test harness currently requires `unwind` behavior."

- **Error**: Expecting opt-level 3 to always be faster than 2.
  **Correction**: "There may be surprising results, such as level `3` being slower than `2`, or the `\"s\"` and `\"z\"` levels not being necessarily smaller." The source recommends experimenting.

# Common Confusions

- **Confusion**: Thinking the `test` and `bench` profiles are independent.
  **Clarification**: "The `test` profile inherits the settings from the `dev` profile" and "The `bench` profile inherits the settings from the `release` profile." They share their parent's defaults unless explicitly overridden.

- **Confusion**: Thinking `lto = false` means "no LTO."
  **Clarification**: `lto = false` "Performs 'thin local LTO' which performs 'thin' LTO on the local crate only across its codegen units." Use `lto = "off"` to fully disable LTO.

- **Confusion**: Thinking dependency profile overrides in non-root packages are respected.
  **Clarification**: "Cargo only looks at the profile settings in the `Cargo.toml` manifest at the root of the workspace. Profile settings defined in dependencies will be ignored."

- **Confusion**: Thinking build dependencies use the same optimization as the main profile.
  **Clarification**: "All profiles, by default, do not optimize build dependencies (build scripts, proc macros, and their dependencies)." The default build-override sets opt-level=0 and codegen-units=256.

# Source Reference

Chapter 5: Profiles -- sections on profile settings (opt-level, debug, split-debuginfo, strip, debug-assertions, overflow-checks, lto, panic, incremental, codegen-units, rpath, frame-pointers), default profiles (dev, release, test, bench, build dependencies), custom profiles, profile selection, overrides, and overrides and generics. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 5 -- "Profiles provide a way to alter the compiler settings, influencing things like optimizations and debugging symbols"
- Confidence rationale: HIGH -- the source provides complete default values for all profiles, all available settings with their valid options, and detailed override precedence rules
- Uncertainties: Platform-specific defaults for split-debuginfo; the `panic-abort-tests` unstable flag may change test behavior in the future
- Cross-reference status: References cargo-manifest-reference (Ch. 1), cargo-configuration (Ch. 6), cargo-build-cache (Ch. 9)
