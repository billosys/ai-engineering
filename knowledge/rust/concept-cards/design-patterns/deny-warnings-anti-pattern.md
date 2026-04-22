---
concept: "#![deny(warnings)] Anti-pattern"
slug: deny-warnings-anti-pattern
category: anti-pattern
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "Anti-patterns"
chapter_number: 3
pdf_page: null
section: "#![deny(warnings)]"
extraction_confidence: high
aliases:
  - "deny warnings"
  - "blanket deny warnings"
  - "deny all warnings anti-pattern"
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Why is #![deny(warnings)] considered an anti-pattern in Rust?"
  - "What should I use instead of #![deny(warnings)]?"
  - "How can new compiler warnings break builds that use deny(warnings)?"
---

# Quick Definition

Annotating a Rust crate with `#![deny(warnings)]` to ensure warning-free builds. While well-intentioned, this converts all compiler warnings into hard errors, which means new warnings introduced by compiler upgrades, new lints, or API deprecations can unexpectedly break the build without any code changes.

# Core Definition

A well-intentioned crate author wants to ensure their code builds without warnings, so they annotate their crate root with `#![deny(warnings)]`. By disallowing the compiler to build with warnings, the crate author opts out of Rust's famed stability. Sometimes new features or old misfeatures need a change in how things are done, and lints are written that `warn` for a certain grace period before being turned to `deny`. The `#![deny(warnings)]` attribute short-circuits this grace period, turning every new warning into an immediate build failure. Furthermore, crates that supply additional lints (e.g., rust-clippy) can no longer be used unless the annotation is removed, though this is mitigated with `--cap-lints`.

# Prerequisites

None -- this is a build configuration concern accessible to all Rust developers.

# Key Properties

1. `#![deny(warnings)]` turns all compiler warnings into hard errors
2. New compiler versions may introduce new lints or change existing ones from `allow` to `warn`, breaking the build
3. Deprecated APIs emit warnings that were previously absent, causing build failures
4. The `overlapping-inherent-impls` lint is cited as an example: it was introduced as a warning grace period before becoming a hard error, but `deny(warnings)` would make it fail immediately
5. Third-party lint tools like rust-clippy may become unusable with blanket deny
6. The `--cap-lints=warn` command line argument can mitigate this by turning all `deny` lint errors back into warnings

# Construction / Recognition

## To Recognize This Anti-Pattern:
1. Look for `#![deny(warnings)]` at the crate root (lib.rs or main.rs)
2. Check if builds break after Rust compiler upgrades with no code changes
3. Note if clippy or other lint tools produce errors instead of warnings

## Alternatives:

**Option 1 -- Environment variable (recommended for CI):**
```
RUSTFLAGS="-D warnings" cargo build
```
This decouples the deny setting from the code itself. Any individual developer or CI tool can use it without requiring a code change.

**Option 2 -- Explicitly deny specific lints:**
```rust
#![deny(
    bad_style,
    dead_code,
    improper_ctypes,
    non_shorthand_field_patterns,
    no_mangle_generic_items,
    overflowing_literals,
    path_statements,
    patterns_in_fns_without_body,
    unconditional_recursion,
    unused,
    unused_allocation,
    unused_comparisons,
    unused_parens,
    while_true
)]
```

Additional lints that may be worth denying:
```rust
#![deny(
    missing_debug_implementations,
    missing_docs,
    trivial_casts,
    trivial_numeric_casts,
    unused_extern_crates,
    unused_import_braces,
    unused_qualifications,
    unused_results
)]
```

The source explicitly notes that the `deprecated` lint should NOT be included in explicit deny lists, as more APIs will certainly be deprecated in the future.

# Context & Application

This anti-pattern affects library authors most severely, since library consumers cannot control the crate root attributes. A library with `#![deny(warnings)]` that builds with Rust 1.X may fail with Rust 1.(X+1) if a new warning is introduced. The RUSTFLAGS approach is preferred for CI pipelines because it achieves the same goal (fail on warnings) without baking the policy into the source code. This keeps the source code compatible across compiler versions while still enforcing strict builds where desired.

# Examples

**Example 1** (Ch. 3, "Description"): A crate author adds `#![deny(warnings)]` to their crate root. Everything compiles cleanly. Then a new Rust version introduces the `overlapping-inherent-impls` lint as a warning (intended as a grace period before it becomes a hard error). With `deny(warnings)`, this new lint immediately breaks the build, even though the code has not changed and the grace period was meant to give authors time to fix it.

**Example 2** (Ch. 3, "Alternatives"): The same goal can be achieved without code changes by running `RUSTFLAGS="-D warnings" cargo build`. This can be configured in CI (e.g., Travis, GitHub Actions) so that warnings fail the CI build while allowing local development with warnings intact.

# Relationships

## Builds Upon
- Rust's lint system and the warn/deny/forbid lint levels

## Enables
- Understanding of `--cap-lints` and RUSTFLAGS for build configuration

## Related
- None in this extraction set

## Contrasts With
- None in this extraction set

# Common Errors

- **Error**: Using `#![deny(warnings)]` in a published library crate.
  **Correction**: Use `RUSTFLAGS="-D warnings"` in CI, or deny specific named lints. Library consumers should not have their builds broken by upstream lint policy.

- **Error**: Including `deprecated` in an explicit lint deny list.
  **Correction**: The source specifically warns against denying `deprecated` since more APIs will be deprecated in the future, leading to the same fragility as blanket `deny(warnings)`.

# Common Confusions

- **Confusion**: Thinking `#![deny(warnings)]` and `RUSTFLAGS="-D warnings"` are equivalent.
  **Clarification**: They achieve the same immediate effect, but `RUSTFLAGS` is external to the code and does not affect downstream users or different development environments. The crate attribute is baked into the source and affects everyone who compiles the crate.

- **Confusion**: Thinking `--cap-lints` fully solves the problem.
  **Clarification**: `--cap-lints=warn` is a mitigation for downstream consumers. The crate author should still not use blanket deny in their source, because it does not help their own CI or contributors.

# Source Reference

Chapter 3: Anti-patterns, "#![deny(warnings)]" section. The anti-pattern is described with the code example, advantages, drawbacks, and two concrete alternatives (RUSTFLAGS and explicit lint lists).

# Verification Notes

- Definition source: Paraphrased from the Description and Drawbacks subsections
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides detailed explanation, concrete alternatives with code, and specific lint lists
- Uncertainties: The specific lint lists shown are noted as being current "as of rustc 1.48.0" and may evolve
- Cross-reference status: No cross-references to other extraction agents' cards
