---
# === CORE IDENTIFICATION ===
concept: API Necessities Guidelines
slug: api-necessities-guidelines

# === CLASSIFICATION ===
category: api-design
subcategory: crate-publishing
tier: intermediate

# === PROVENANCE ===
source: "Rust API Guidelines"
source_slug: api-guidelines
authors: "The Rust Library Team"
chapter: "11-necessities"
chapter_number: 11
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C-STABLE"
  - "C-PERMISSIVE"
  - "Rust crate stability requirements"
  - "Rust crate licensing"
  - "public dependency stability"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - api-guidelines-overview
extends: []
related:
  - api-interoperability-guidelines
  - api-future-proofing-guidelines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can a stable crate depend on an unstable crate?"
  - "What is a public dependency in Rust?"
  - "How can public dependencies sneak into a crate's public API?"
  - "What license should I use for a Rust crate?"
  - "Why does the Rust project use dual MIT/Apache-2.0 licensing?"
  - "How do I set up dual licensing in Cargo.toml?"
  - "Why is Apache-2.0-only licensing not recommended for Rust crates?"
  - "Do my dependency licenses affect my crate's distribution?"
---

# Quick Definition

Two prerequisites for publishing a quality Rust crate: all public dependencies of a stable crate (>=1.0.0) must themselves be stable (C-STABLE), and crates should use a permissive license -- ideally dual MIT/Apache-2.0 to match the Rust project itself (C-PERMISSIVE). These guidelines ensure crates are reliable for downstream consumers and maximally compatible with the Rust ecosystem.

# Core Definition

The Rust API Guidelines define two baseline requirements for crate publishing.

**C-STABLE**: "A crate cannot be stable (>=1.0.0) without all of its public dependencies being stable." Public dependencies are defined as "crates from which types are used in the public API of the current crate." The source warns that public dependencies "can sneak in at unexpected places" -- for example, implementing `From<other_crate::Error>` for your error type makes `other_crate` a public dependency even if the error enum variant referencing it is private.

**C-PERMISSIVE**: "The software produced by the Rust project is dual-licensed, under either the MIT or Apache 2.0 licenses. Crates that simply need the maximum compatibility with the Rust ecosystem are recommended to do the same." The source explicitly recommends against Apache-2.0-only licensing because "the Apache license, though it is a permissive license, imposes restrictions beyond the MIT and BSD licenses that can discourage or prevent their use in some scenarios." Additionally, "the license of a crate's dependencies can affect the restrictions on distribution of the crate itself."

# Prerequisites

- **API Guidelines Overview** -- understanding the overall API Guidelines framework and its applicability to crate publishing

# Key Properties

1. **Stable crates require stable public dependencies**: A crate at version >=1.0.0 must not expose types from pre-1.0.0 crates in its public API
2. **Public dependency definition**: Any crate whose types appear in your public API -- function signatures, public struct fields, trait implementations
3. **Hidden public dependencies**: `From` and `Into` implementations can make a dependency public even when the underlying type is in a private enum variant
4. **Dual MIT/Apache-2.0 recommended**: Maximum compatibility with the Rust ecosystem
5. **Cargo.toml license field**: Use `license = "MIT OR Apache-2.0"` (SPDX expression)
6. **License files required**: Include both `LICENSE-APACHE` and `LICENSE-MIT` in the repository root
7. **Single permissive license acceptable**: MIT-only or BSD-only is compatible with Rust's MIT license
8. **Apache-2.0-only discouraged**: "Imposes restrictions beyond the MIT and BSD licenses" that prevent use in some scenarios
9. **Transitive license impact**: "A permissively-licensed crate should generally only depend on permissively-licensed crates"
10. **README license section**: Document the dual license with links and a contribution clause

# Construction / Recognition

## Public dependency example (C-STABLE):
```rust
// other_crate is a public dependency here:
pub fn do_my_thing(arg: other_crate::TheirThing) { /* ... */ }
```

## Hidden public dependency (C-STABLE):
```rust
pub struct Error {
    private: ErrorImpl,
}

enum ErrorImpl {
    Io(io::Error),
    // Seems okay because ErrorImpl is private...
    Dep(other_crate::Error),
}

// But this puts other_crate into the public API!
impl From<other_crate::Error> for Error {
    fn from(err: other_crate::Error) -> Self {
        Error { private: ErrorImpl::Dep(err) }
    }
}
```

## Cargo.toml license configuration (C-PERMISSIVE):
```toml
[package]
name = "..."
version = "..."
authors = ["..."]
license = "MIT OR Apache-2.0"
```

## README contribution clause (C-PERMISSIVE):
```text
Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
```

# Context & Application

These two guidelines represent the minimum requirements for a well-published Rust crate. C-STABLE addresses a real ecosystem problem: if a stable crate exposes types from an unstable dependency, downstream consumers are subject to breaking changes from a crate they may not even know they depend on. The hidden public dependency example (via `From` implementation) is a particularly subtle case that library authors often miss. C-PERMISSIVE reflects the Rust ecosystem's strong convention toward permissive licensing. The dual MIT/Apache-2.0 approach is nearly universal among Rust ecosystem crates and is the default for `cargo new`. These are not just style recommendations -- they have practical consequences for crate adoption and compatibility.

# Examples

**Example 1** (Ch. 11, C-STABLE): Direct public dependency:
> A function `pub fn do_my_thing(arg: other_crate::TheirThing)` makes `other_crate` a public dependency. "A crate containing this function cannot be stable unless `other_crate` is also stable."

**Example 2** (Ch. 11, C-STABLE): Sneaky public dependency via `From`:
> "Oh no! This puts other_crate into the public API of the current crate." Even though `ErrorImpl::Dep(other_crate::Error)` is inside a private enum, the `impl From<other_crate::Error> for Error` trait implementation exposes it publicly.

**Example 3** (Ch. 11, C-PERMISSIVE): Why Apache-only is discouraged:
> "The Apache license, though it is a permissive license, imposes restrictions beyond the MIT and BSD licenses that can discourage or prevent their use in some scenarios, so Apache-only software cannot be used in some situations where most of the Rust runtime stack can."

**Example 4** (Ch. 11, C-PERMISSIVE): Transitive license considerations:
> "The license of a crate's dependencies can affect the restrictions on distribution of the crate itself, so a permissively-licensed crate should generally only depend on permissively-licensed crates."

# Relationships

## Builds Upon
- **API Guidelines Overview** -- these guidelines are part of the overall API Guidelines checklist

## Enables
- Safe adoption of crates by downstream consumers
- Consistent licensing across the Rust ecosystem
- Reliable semver guarantees for the dependency graph

## Related
- **api-interoperability-guidelines** -- trait implementations (like `From`) interact with public dependency analysis
- **api-future-proofing-guidelines** -- stability and future-proofing are complementary concerns for crate evolution

## Contrasts With
- None within this source

# Common Errors

- **Error**: Publishing a 1.0.0 crate that uses types from a 0.x dependency in its public API.
  **Correction**: "A crate cannot be stable (>=1.0.0) without all of its public dependencies being stable." Either wait for the dependency to stabilize or wrap its types behind your own types. (C-STABLE)

- **Error**: Implementing `From<dep::Error>` for your error type without realizing it makes `dep` a public dependency.
  **Correction**: "Be careful because public dependencies can sneak in at unexpected places." Trait implementations on external types create public dependencies. (C-STABLE)

- **Error**: Using only Apache-2.0 licensing for a Rust crate.
  **Correction**: "Crates that desire perfect license compatibility with Rust are not recommended to choose only the Apache license" because it "imposes restrictions beyond the MIT and BSD licenses." Use dual MIT/Apache-2.0. (C-PERMISSIVE)

- **Error**: Depending on a GPL-licensed crate from a permissively-licensed crate.
  **Correction**: "A permissively-licensed crate should generally only depend on permissively-licensed crates" because dependency licenses affect distribution restrictions. (C-PERMISSIVE)

# Common Confusions

- **Confusion**: Thinking private enum variants cannot create public dependencies.
  **Clarification**: The source demonstrates that `impl From<other_crate::Error> for Error` makes `other_crate` public even when the variant `ErrorImpl::Dep(other_crate::Error)` is private. The `From` implementation is the public surface, not the enum variant.

- **Confusion**: Thinking MIT and Apache-2.0 are interchangeable.
  **Clarification**: Apache-2.0 "imposes restrictions beyond the MIT and BSD licenses." Dual licensing ensures compatibility with both the minimal MIT requirements and the patent-protection benefits of Apache-2.0.

- **Confusion**: Thinking the `license` field in `Cargo.toml` is sufficient documentation.
  **Clarification**: The source recommends including `LICENSE-APACHE` and `LICENSE-MIT` files in the repository root plus a license section in the README with the contribution clause.

- **Confusion**: Thinking only function parameter types create public dependencies.
  **Clarification**: Public dependencies include any crate whose types appear in public API surfaces: function signatures, return types, public fields, trait implementations, re-exports, and more.

# Source Reference

Chapter 11: Necessities -- guidelines C-STABLE (public dependencies of a stable crate are stable), C-PERMISSIVE (crate and its dependencies have a permissive license). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 11 of the Rust API Guidelines
- Confidence rationale: HIGH -- guidelines are clearly stated with concrete examples and specific recommendations
- Uncertainties: The Rust FAQ link for licensing details may change; licensing advice may evolve as the ecosystem matures
- Cross-reference status: api-guidelines-overview referenced but not in this extraction set; will be created by another agent
