---
concept: Library Building Guidelines
slug: library-building-guidelines
category: guidelines
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "02-libraries"
chapter_number: 2
pdf_page: null
section: "Building"
extraction_confidence: high
aliases:
  - "building guidelines"
  - "crate compilation"
  - "OOBE"
  - "out of the box experience"
  - "sys crates"
  - "feature flags"
prerequisites:
  - library-interop-guidelines
extends: []
related:
  - library-resilience-guidelines
  - library-ux-guidelines
contrasts_with: []
answers_questions:
  - "How do I ensure a Rust crate works out of the box on all platforms?"
  - "How should native -sys crates be structured for cross-platform builds?"
  - "What rules should Cargo features follow in a library crate?"
  - "Why must features be additive in Rust?"
---

# Quick Definition

Building guidelines for Rust libraries covering three areas: libraries must compile and work out of the box on all Tier 1 platforms without extra prerequisites (M-OOBE), native `-sys` crates must embed sources and avoid external build tool dependencies (M-SYS-CRATES), and all Cargo features must be strictly additive with any combination working (M-FEATURES-ADDITIVE).

# Core Definition

The building guidelines ensure that Rust libraries are easily adoptable. M-OOBE requires that crates build on all Tier 1 platforms with only `cargo` and `rust` installed, no additional tools or environment variables required. M-SYS-CRATES provides a detailed checklist for `-sys` crates wrapping native libraries: govern the build from `build.rs` using the `cc` crate, embed upstream source code, make external tools optional, pre-generate bindgen glue, and support both static and dynamic linking. M-FEATURES-ADDITIVE requires all features to be purely additive: no `no-std` features (use a `std` feature instead), no feature that disables or modifies public items, no features requiring manual co-enablement. (Ch. 2, "Libraries / Building Guidelines")

# Prerequisites

- **library-interop-guidelines** -- understanding type leaking and platform compatibility feeds into building guidelines

# Key Properties

1. **M-OOBE**: Crates must build on all Tier 1 platforms without prerequisites beyond `cargo` and `rust` (plus the default `cc` and linker)
2. Non-platform crates must not require additional tools or environment variables to compile
3. If tools are needed (e.g., `.proto` to `.rs` generation), run them during the publishing workflow and ship the artifacts in the published crate
4. Platform-specific dependencies must use conditional compilation or opt-in feature gates
5. Libraries are responsible for their entire dependency tree's build requirements
6. **M-SYS-CRATES**: Native `-sys` crates should govern the build via `build.rs` with hand-crafted `cc` compilation, not Makefiles or external scripts
7. External tools (e.g., `nasm`) must be optional; upstream source should be embedded and verifiable (Git URL + hash)
8. Pre-generate `bindgen` glue if possible; support both static linking and dynamic linking via `libloading`
9. **M-FEATURES-ADDITIVE**: Use `std` features instead of `no-std` features; adding any feature must not disable or modify public items
10. Features must not rely on other features being manually enabled or on parent crates skip-enabling child features

# Construction / Recognition

## To Apply M-OOBE:
1. Test that `cargo build` succeeds on a fresh machine with only Rust installed for all Tier 1 platforms
2. Audit dependencies for external tool requirements (protobuf compilers, perl scripts, etc.)
3. Pre-generate any artifacts that would require external tools at build time
4. Use conditional compilation for platform-specific dependencies

## To Apply M-SYS-CRATES:
1. Embed upstream source code in the crate with verifiable provenance
2. Use `cc` crate in `build.rs` for compilation, not Makefiles
3. Make external tools optional with fallback code paths
4. Pre-generate bindgen output; support both static and dynamic linking

## To Apply M-FEATURES-ADDITIVE:
1. Name the feature `std` not `no-std`
2. Verify every feature combination compiles and no public items change
3. Ensure features are self-contained and do not require manual co-enablement

# Context & Application

These guidelines address the practical reality that Rust crates in a large project may pull in hundreds of dependencies. The source cites the `bat` utility pulling ~250 dependencies as a typical example where everything "just works." A single dependency requiring Perl, protobuf, or any non-standard tool breaks the entire compilation chain for all downstream users who may not know or care about that dependency. The additive features rule addresses Cargo's feature unification: in a dependency graph, multiple crates may enable different feature combinations of a shared dependency, and non-additive features cause unpredictable breakage.

# Examples

**Example 1** (Ch. 2, M-OOBE -- Negative example): The source describes a scenario where a `Copilot` crate depends on an `HttpClient` that requires Perl to compile. Every user of `Copilot`, and every user of those users, must install Perl. The source calls this "a self-inflicted death sentence in the open source space."

**Example 2** (Ch. 2, M-SYS-CRATES -- Checklist): For a `foo`/`foo-sys` crate pair wrapping `foo.lib`: (1) govern build from `build.rs` via `cc`, (2) make `nasm` optional, (3) embed upstream source, (4) make sources verifiable via Git URL + hash, (5) pre-generate bindgen glue, (6) support static and dynamic linking via `libloading`.

**Example 3** (Ch. 2, M-FEATURES-ADDITIVE -- Anti-pattern): A `no-std` feature that disables std-dependent items violates additivity because enabling it alongside another feature that expects std items would break compilation.

# Relationships

## Builds Upon
- **library-interop-guidelines** -- platform compatibility and type concerns inform building requirements

## Enables
- Frictionless adoption of libraries across the Rust ecosystem
- Reliable CI/CD pipelines that do not require special tooling

## Related
- **library-resilience-guidelines** -- resilience guidelines complement building with runtime robustness
- **library-ux-guidelines** -- UX guidelines complement building with API ergonomics

## Contrasts With
- Libraries that require manual installation of external tools (protobuf, cmake, perl)
- Feature designs using `no-std` flags or mutually exclusive features

# Common Errors

- **Error**: Using `bindgen` at build time in a `-sys` crate, requiring `libclang` on every user's machine.
  **Correction**: Pre-generate bindgen output and include the generated `.rs` files in the published crate.

- **Error**: Creating a `no-std` feature that removes std-dependent public API items.
  **Correction**: Create a `std` feature (enabled by default) that adds std-dependent items. Without it, only `core`/`alloc` items are available.

- **Error**: Downloading source code from a private or unreliable server in `build.rs` for a `-sys` crate.
  **Correction**: Embed sources in the crate; if download is necessary, use servers with availability comparable to crates.io, verify hashes, and allow alternative source roots via environment variables.

# Common Confusions

- **Confusion**: Thinking "out of the box" means the crate must work on every possible platform.
  **Clarification**: M-OOBE requires Tier 1 platform support. Platform-specific crates are exempted. For unsupported Tier 1 platforms, abstractions (internal HAL with a `dummy` fallback) should be present for future extensibility.

- **Confusion**: Believing mutually exclusive features are acceptable if documented.
  **Clarification**: The source references Cargo's feature unification documentation and explicitly requires all features to be additive. Any combination must work because multiple crates in a dependency graph may independently enable different features.

# Source Reference

Chapter 2: Library Guidelines, "Building" section. Contains three guidelines: M-OOBE (v1.0), M-SYS-CRATES (v0.2), M-FEATURES-ADDITIVE (v1.0). M-OOBE includes the `bat` compilation example and the Perl dependency warning. M-SYS-CRATES provides a detailed checklist with allowable deviations. M-FEATURES-ADDITIVE includes checklist items and references to Cargo documentation on feature unification and mutually exclusive features.

# Verification Notes

- Definition source: Direct from section headings and `<why>` tags for each guideline
- Key Properties: Derived from checklists, examples, and explanatory text
- Confidence rationale: HIGH -- all three guidelines have clear definitions, checklists, and practical examples
- Uncertainties: None
- Cross-reference status: library-interop-guidelines, library-resilience-guidelines are from sibling extraction sets
