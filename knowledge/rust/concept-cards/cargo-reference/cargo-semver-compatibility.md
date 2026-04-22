---
# === CORE IDENTIFICATION ===
concept: Cargo SemVer Compatibility
slug: cargo-semver-compatibility

# === CLASSIFICATION ===
category: packaging
subcategory: versioning
tier: advanced

# === PROVENANCE ===
source: "Cargo Reference"
source_slug: cargo-reference
authors: "The Cargo Team"
chapter: "13-semver"
chapter_number: 13
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust semver compatibility"
  - "breaking changes in Rust"
  - "SemVer Compatibility"
  - "Rust API compatibility"
  - "what is a breaking change in Rust"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cargo-publishing
  - cargo-dependencies
extends: []
related:
  - cargo-lints-reference
  - cargo-unstable-features
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What constitutes a breaking (major) change in a Rust crate?"
  - "What changes are safe to make in a minor or patch release?"
  - "When is adding a new enum variant a breaking change?"
  - "How does #[non_exhaustive] affect SemVer compatibility?"
  - "Is adding a public field to a struct a breaking change?"
  - "Can I tighten or loosen generic bounds in a minor release?"
  - "Is changing the minimum Rust version a breaking change?"
  - "How do repr attributes affect SemVer compatibility?"
  - "What Cargo.toml changes are considered breaking?"
  - "Is removing an optional dependency a breaking change?"
  - "What are the categories of SemVer changes in Rust?"
---

# Quick Definition

The Cargo Reference SemVer Compatibility chapter is the definitive guide for what constitutes a compatible or breaking change in Rust crate releases. It categorizes changes into three levels -- major (breaking, requires major version bump), minor (safe, requires minor version bump), and possibly-breaking (judgment call) -- and covers API compatibility (items, types, structs, enums, traits, implementations, generics, functions, attributes), tooling/environment compatibility (MSRV, platform, lints, Cargo features, dependencies), and application compatibility.

# Core Definition

The source states: "This chapter provides details on what is conventionally considered a compatible or breaking SemVer change for new releases of a package." (Ch. 13). It emphasizes that "These are only *guidelines*, and not necessarily hard-and-fast rules that all projects will obey."

The guide organizes changes into a comprehensive taxonomy. **API compatibility** covers items (renaming/removing public items is major; adding new ones is minor), types (changing alignment/layout/size of well-defined types is major), structs (adding private fields to all-public structs is major; adding fields when private fields already exist is minor), enums (adding variants without `non_exhaustive` is major), traits (adding non-defaulted items is major; adding defaulted items is possibly-breaking), generics (tightening bounds is major; loosening is minor), and functions (changing arity is major; generalizing to support original types is minor). **Tooling compatibility** covers MSRV changes (possibly-breaking but conventionally minor), Cargo features (removing is major; adding is minor), and dependencies.

For initial development releases ("0.y.z"), Cargo treats changes in the left-most non-zero component as incompatible: "0.0.z releases are always major changes."

# Prerequisites

- **Cargo Publishing** -- SemVer compatibility matters when publishing crate updates
- **Cargo Dependencies** -- downstream users depend on compatibility guarantees through version requirements

# Key Properties

1. **Three change categories**: Major (requires major bump), Minor (requires minor bump), Possibly-breaking (project judgment)
2. **Removing or renaming any public item is always major**: Absence of a publicly exposed item will cause compilation failure
3. **Adding public items is minor**: But glob imports can cause rare breakage due to name ambiguity
4. **Struct field rules depend on existing visibility**: Adding any field when all fields are public is major; adding/removing private fields when at least one exists is minor
5. **Enum variants without `#[non_exhaustive]` are locked**: Adding variants is major; `non_exhaustive` makes it minor
6. **Trait item changes are major unless defaulted**: Non-defaulted items break all implementors; defaulted items are possibly-breaking due to name conflicts
7. **Generic bound tightening is major, loosening is minor**: Adding defaulted type parameters is always minor
8. **`repr` attribute changes are generally major**: Adding/removing `repr(packed)`, `repr(align)`, changing `repr(C)` layout, or removing `repr(transparent)` are all major
9. **MSRV changes are "possibly-breaking" but conventionally minor**: The community generally treats this as a minor change
10. **Cargo feature removal is major; addition is minor**: Removing optional dependencies is possibly-breaking unless using `dep:` syntax

# Construction / Recognition

## Major Change -- Adding Fields to All-Public Struct:
```rust
// MAJOR: breaks struct literal construction
// Before
pub struct Foo { pub f1: i32 }
// After
pub struct Foo { pub f1: i32, pub f2: i32 }
// Breaks: let x = Foo { f1: 123 }; // Error: missing field `f2`
```

## Minor Change -- Loosening Generic Bounds:
```rust
// MINOR: only expands what is allowed
// Before
pub struct Foo<A: Clone> { pub f1: A }
// After
pub struct Foo<A> { pub f1: A }
```

## Mitigation -- Using `#[non_exhaustive]`:
```rust
// Allows future additions without breaking changes
#[non_exhaustive]
pub enum E { Variant1, Variant2 }

#[non_exhaustive]
pub struct Config { pub timeout: u64 }
```

## Major Change -- Cargo Feature Removal:
```toml
# MAJOR: removing a feature breaks users who enabled it
# Before
[features]
logging = []
# After -- logging removed entirely
```

## Mitigation -- Hiding Optional Dependencies with `dep:`:
```toml
# Using dep: prevents the dependency name from becoming a public feature
[dependencies]
curl = { version = "0.4.31", optional = true }
[features]
networking = ["dep:curl"]
# Now "curl" is not a public feature; only "networking" is
```

# Context & Application

This chapter is the authoritative Rust community reference for SemVer compatibility decisions. It is essential reading for anyone publishing crates to crates.io. The guide's strength is its exhaustive coverage of Rust-specific breaking change scenarios that have no direct parallel in other languages -- such as trait object safety, `repr` attribute interactions, disjoint closure captures affected by `repr(packed)`, and RPIT lifetime capture changes in edition 2024. The "possibly-breaking" category is particularly valuable as it acknowledges that certain changes (like adding defaulted trait items or changing MSRV) are technically breaking but conventionally accepted as minor. The guide consistently provides mitigation strategies: use `#[non_exhaustive]` for extensibility, use sealed traits to prevent external implementations, use `dep:` syntax to hide optional dependencies, and document minimum supported Rust versions via `package.rust-version`.

# Examples

**Example 1** (Ch. 13, Structs): Adding a private field when all fields are public:
> "When a private field is added to a struct that previously had all public fields, this will break any code that attempts to construct it with a struct literal." Mitigation: "Mark structs as `#[non_exhaustive]` when first introducing a struct."

**Example 2** (Ch. 13, Traits): Adding a defaulted trait item is "possibly-breaking":
> "It is usually safe to add a defaulted trait item. However, this can sometimes cause a compile error. For example, this can introduce an ambiguity if a method of the same name exists in another trait."

**Example 3** (Ch. 13, Generics): Capturing more generic parameters in RPIT:
> "It is a breaking change to capture additional generic parameters in an RPIT (return-position impl trait)." Starting in Rust 2024, all lifetime parameters are unconditionally captured by default.

**Example 4** (Ch. 13, Lints): Introducing new lints is minor:
> "Beware that it may be possible for this to technically cause a project to fail if they have explicitly denied the warning." Transitive dependencies are protected by Cargo's `--cap-lints`.

**Example 5** (Ch. 13, Cargo): Optional dependency removal is possibly-breaking:
> "Removing an optional dependency can break a project using your library because another project may be enabling that dependency via Cargo features." The `dep:` syntax mitigates this.

# Relationships

## Builds Upon
- **Cargo Publishing** -- SemVer commitments take effect upon publishing
- **Cargo Dependencies** -- version requirements encode SemVer expectations

## Enables
- Confident decision-making about version bumps
- Proactive use of `#[non_exhaustive]`, sealed traits, and `dep:` for future-proofing

## Related
- **cargo-lints-reference** -- Cargo lints can catch SemVer-related issues
- **cargo-unstable-features** -- unstable features may change SemVer expectations when stabilized

## Contrasts With
- None within this source

# Common Errors

- **Error**: Adding a public field to a struct with all public fields in a minor release.
  **Correction**: This is major because it breaks struct literal construction. Use `#[non_exhaustive]` from the start, or provide a constructor method and `Default` implementation.

- **Error**: Adding enum variants in a minor release without `#[non_exhaustive]`.
  **Correction**: This breaks exhaustive `match` statements. Mark enums as `#[non_exhaustive]` when first introducing them.

- **Error**: Tightening generic bounds (e.g., adding `Clone` requirement) in a minor release.
  **Correction**: This is a major change -- existing users may have types that do not satisfy the new bound.

- **Error**: Removing a Cargo feature or optional dependency in a minor release.
  **Correction**: Feature removal is major. Either leave it as a deprecated no-op, or use `dep:` syntax from the start to avoid exposing dependency names as features.

# Common Confusions

- **Confusion**: Thinking all `repr` changes are breaking.
  **Clarification**: Adding `repr(C)`, `repr(int)`, or `repr(transparent)` to a default-representation type is minor, because users should not assume the layout of default-representation types. Removing these attributes or adding `repr(packed)`/`repr(align)` is major.

- **Confusion**: Thinking adding new public items is always safe.
  **Clarification**: It is generally minor, but can break code using glob imports (`use crate::*`) if a new trait introduces a method that conflicts with existing trait methods on the same type.

- **Confusion**: Thinking MSRV bumps are always major changes.
  **Clarification**: The guide classifies this as "possibly-breaking" and notes: "It is generally recommended to treat this as a minor change, rather than as a major change." The community convention supports this.

- **Confusion**: Thinking making an `unsafe` function safe is a breaking change.
  **Clarification**: This is minor. It may trigger the `unused_unsafe` lint in callers, but introducing new lints is conventionally acceptable.

# Source Reference

Chapter 13: SemVer Compatibility -- sections "Change categories", "API compatibility" (items, types, structs, enums, traits, implementations, generics, functions, attributes), "Tooling and environment compatibility" (MSRV, platform, lints, Cargo features/dependencies), and "Application compatibility". No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 13 opening paragraph and the comprehensive change taxonomy
- Confidence rationale: HIGH -- the source is the official Rust community SemVer reference with detailed code examples for every rule
- Uncertainties: RPIT capture rules changed in Rust 2024 edition; the guide notes this explicitly. Some "possibly-breaking" classifications are inherently judgment calls.
- Cross-reference status: Prerequisites reference cards from the cargo-guide extraction set; related cards are within this extraction set
