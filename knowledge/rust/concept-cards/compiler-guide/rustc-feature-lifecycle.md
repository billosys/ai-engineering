---
# === CORE IDENTIFICATION ===
concept: Rust Feature Lifecycle and Stabilization
slug: rustc-feature-lifecycle

# === CLASSIFICATION ===
category: compiler-internals
subcategory: governance-and-process
tier: intermediate

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Feature Lifecycle"
chapter_number: 5
pdf_page: null
section: "Implementing New Features, Stability Attributes, Stabilization Guide, Feature Gates"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "feature gates"
  - "feature gating"
  - "stabilization"
  - "stability attributes"
  - "unstable features"
  - "#[feature(...)]"
  - "#[stable]"
  - "#[unstable]"
  - "FCP process"
  - "tracking issues"
  - "lang experiments"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rustc-compiler-dev-practices
  - rustc-compiler-overview
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a new language feature go from proposal to stable Rust?"
  - "What are feature gates and how do they work in rustc?"
  - "What is the FCP (Final Comment Period) process?"
  - "How do I implement a new unstable feature in the compiler?"
  - "What are the stability attributes (#[stable], #[unstable]) and how do they work?"
  - "What is the difference between language feature stabilization and library feature stabilization?"
  - "How do I stabilize an existing unstable feature?"
  - "What is a tracking issue and why is every feature required to have one?"
  - "What is a lang experiment?"
  - "How do feature gates interact with editions?"
  - "What is the role of the Rust Reference, rustfmt, and rust-analyzer in feature polishing?"
  - "How do I add, remove, or rename a feature gate?"
---

# Quick Definition

A feature gate is the mechanism by which new language features are kept behind a `#[feature(name)]` attribute so they can only be used on nightly, allowing experimentation and iteration before committing to backward compatibility. The full lifecycle runs: proposal (RFC or lang experiment) -> implementation with feature gate -> nightly experimentation -> call for testing -> polishing (Reference docs, rustfmt, rust-analyzer) -> stabilization via FCP -> stable release. Library features use parallel `#[stable]`/`#[unstable]` attributes rather than feature gates.

# Core Definition

The Rust project "values the stability of Rust" -- code that compiles on stable should not break. To reconcile this with language evolution, all new features are gated behind `#[feature(foo)]` which can only be enabled on the nightly compiler. This ensures users cannot accidentally depend on incomplete features that might change or be removed.

The feature lifecycle has distinct phases. For language features, changes that are small and non-breaking need only an `r+` review. Larger changes require team consensus through the **FCP (Final Comment Period)** process: a team member proposes FCP using `@rfcbot fcp merge`, all team members must sign off, then a 10-day public comment period follows. The compiler team also has a lighter-weight **MCP (Major Change Proposal)** process for compiler-internal changes.

Language features that have user-visible effects require either an accepted RFC or an approved **lang experiment** before landing. Lang experiments are proposed as tracking issues nominated for the lang team, and their feature flags must be marked as `incomplete` until an RFC is accepted.

Library features use a different stability system based on `#[stable]` and `#[unstable]` attributes. The `#[unstable]` attribute "infects" all sub-items -- applying it to a module makes everything in that module unstable. Library stabilization follows a similar FCP process through the `@T-libs-api` team.

Stabilization is the final step where a feature becomes available to all users, at which point backward-incompatible changes are generally no longer permitted per the lang team's defined semver policies.

# Prerequisites

Familiarity with the Rust release train (nightly/beta/stable channels) and basic understanding of the RFC process. Knowledge of the Rust compiler's crate structure is helpful for understanding where feature gates are implemented.

# Key Properties

1. **Feature gate declaration**: Each gate is declared in `rustc_feature/src/unstable.rs` via `declare_features!` using the tuple `(unstable, feature_name, "CURRENT_RUSTC_VERSION", Some(tracking_issue_number))`
2. **Feature gate checking**: Code checks `tcx.features().feature_name()` to test whether a feature is enabled; new syntax uses `GatedSpans` and `gate_all!()` for pre-expansion gating
3. **Tracking issues**: Every feature gate requires a tracking issue using the "Tracking Issue" template, serving as the central point for status tracking and feedback
4. **Incomplete features**: Features can be marked `incomplete` to trigger the `incomplete_features` lint, required for all lang experiments until RFC acceptance
5. **Stability attribute infection**: `#[unstable]` propagates to all sub-items; stable sub-items within unstable modules can be explicitly marked `#[stable]`
6. **Const stability**: `#[rustc_const_unstable]` is separate from regular stability and is *recursive* -- a const-unstable function cannot be called even indirectly from stable code
7. **Stabilization report**: Language features require a formal stabilization report covering design decisions, test coverage, tool changes, and type system interactions
8. **`CURRENT_RUSTC_VERSION` placeholder**: Used instead of explicit version numbers to avoid semantic merge conflicts; the actual version is filled in during release
9. **`allow_internal_unstable`**: Allows stable macros in the standard library to use unstable features internally without exposing them
10. **Feature removal**: Removed features are moved to `rustc_feature/src/removed.rs` with a reason string; renamed features add `old_name` for error message compatibility

# Construction / Recognition

## To Implement a New Unstable Feature:

1. Open or identify the tracking issue (labeled `C-tracking-issue`)
2. Pick a name for the feature gate (use the RFC name if applicable)
3. Add the feature name to `rustc_span/src/symbol.rs` in the `Symbols` block (alphabetical order)
4. Add a feature gate declaration to `rustc_feature/src/unstable.rs`
5. Add enforcement code using `tcx.features().feature_name()` or pre-expansion gating via `GatedSpans`
6. Create a test at `tests/ui/feature-gates/feature-gate-$feature_name.rs`
7. Add an entry to the unstable book at `src/doc/unstable-book/src/language-features/$feature_name.md`
8. Write extensive tests in `tests/ui/$feature_name/`

## To Stabilize a Language Feature:

1. Write a stabilization report using the official template
2. Move the entry from `rustc_feature/src/unstable.rs` to `rustc_feature/src/accepted.rs` (changing `unstable` to `accepted`)
3. Remove `#![feature(...)]` from tests and compiler crates (or change to `#![cfg_attr(bootstrap, feature(...))]`)
4. Remove feature-gate checking code (e.g., remove `gate_all!()` calls)
5. Open the stabilization PR, CC relevant teams, nominate for lang meeting
6. After FCP approval, merge following implementation review

# Context & Application

- **Compiler contributors**: Anyone implementing new syntax, semantics, or compiler behavior must follow the feature gate process
- **Library contributors**: Standard library additions use the parallel `#[stable]`/`#[unstable]` attribute system
- **Edition transitions**: Features can be gated on editions using `span.at_least_rust_20xx()`, optionally combined with feature gates for finer control
- **Tool authors**: rustfmt, rust-analyzer, and the Reference must be updated as part of the "polishing" phase before stabilization
- **Breaking changes**: Even bug fixes that change behavior use this system -- they start as future-compatibility warnings before becoming errors

# Examples

**Example 1**: Declaring a feature gate in `rustc_feature/src/unstable.rs`:
```rust
/// Allows defining identifiers beyond ASCII.
(unstable, non_ascii_idents, "CURRENT_RUSTC_VERSION", Some(55467)),
```

**Example 2**: Marking a feature as incomplete (for lang experiments):
```rust
/// Allows deref patterns.
(incomplete, deref_patterns, "CURRENT_RUSTC_VERSION", Some(87121)),
```

**Example 3**: Library stability attribute with deprecation:
```rust
#[stable(feature = "foo", since = "1.38.0")]
#[deprecated(
    since = "1.38.0",
    note = "explanation for deprecation",
    suggestion = "other_function"
)]
pub fn old_function() { }
```

**Example 4**: Moving a feature to accepted status during stabilization:
```rust
// In accepted.rs:
// pub(restricted) visibilities (RFC 1422)
(accepted, pub_restricted, "CURRENT_RUSTC_VERSION", Some(32409)),
```

# Relationships

## Builds Upon
- None within this extraction set -- this is the governance/process foundation

## Enables
- **rustc-compiler-dev-practices** -- dev conventions exist within the context of these stability processes
- **rustc-compiler-overview** -- the compiler architecture implements feature gating at multiple stages

## Related
- **rustc-compiler-dev-practices** -- breaking change procedures and edition handling are closely related to the feature lifecycle

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using an explicit version number (e.g., `"1.70"`) instead of `"CURRENT_RUSTC_VERSION"` in feature gate declarations.
  **Correction**: Always use `CURRENT_RUSTC_VERSION` to avoid semantic merge conflicts. The actual version is substituted during the release process.

- **Error**: Forgetting to mark a lang experiment's feature flag as `incomplete`.
  **Correction**: "Feature flags related to a lang experiment must be marked as `incomplete` until an RFC is accepted for the feature."

- **Error**: Implementing a user-visible language change without an RFC or approved lang experiment.
  **Correction**: "Features that have user-visible effects on the language (even unstable ones) must either be part of an accepted RFC or an approved lang experiment."

# Common Confusions

- **Confusion**: Language features and library features use the same stabilization mechanism.
  **Clarification**: They use parallel but different systems. Language features use feature gates in `rustc_feature` and the `#[feature(...)]` attribute. Library features use `#[stable]`/`#[unstable]` attributes and the `staged_api` mechanism. Their stabilization processes involve different teams (lang vs. libs-api).

- **Confusion**: Unstable features gain tenure by being unchanged for a long time.
  **Clarification**: The guide explicitly states: "Features do not gain tenure by being unstable and unchanged for long periods of time." Every feature can be changed, rewritten, or removed at any time while unstable.

- **Confusion**: Const stability works the same as regular stability.
  **Clarification**: Const stability (`#[rustc_const_unstable]`) is *recursive* -- "a `#[rustc_const_unstable(...)]` function cannot even be indirectly called from stable code." Regular stability does not have this recursive property.

# Source Reference

Chapter 5: Feature Lifecycle (1078 lines). Covers implementing new language features, the FCP process, stability attributes (`#[stable]`, `#[unstable]`, `#[rustc_const_unstable]`, etc.), the stabilization guide with step-by-step procedures, stabilization report template, and feature gate management (adding, removing, renaming, stabilizing).

# Verification Notes

- Definition source: Direct text from the "Implementing new language features" and "Stability attributes" sections
- Key Properties: All items directly supported by source text with specific file paths and code patterns
- Confidence rationale: HIGH -- canonical procedural documentation from the official rustc dev guide
- Uncertainties: Some version-specific details may shift as the compiler evolves
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
