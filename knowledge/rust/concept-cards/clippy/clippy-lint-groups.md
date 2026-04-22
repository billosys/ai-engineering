---
# === CORE IDENTIFICATION ===
concept: Clippy Lint Groups
slug: clippy-lint-groups

# === CLASSIFICATION ===
category: configuration
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Clippy Documentation"
source_slug: clippy
authors: "The Clippy Contributors"
chapter: "01-getting-started"
chapter_number: 1
pdf_page: null
section: "Usage"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "lint categories"
  - "clippy::all"
  - "clippy::pedantic"
  - "clippy::restriction"
  - "lint group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clippy
  - clippy-lint-levels
extends: []
related:
  - cargo-clippy
  - clippy-configuration
  - lint-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What lint groups does Clippy provide?"
  - "What is the difference between clippy::all and clippy::pedantic?"
  - "Which lint groups are warn-by-default and which are allow-by-default?"
  - "Should I enable clippy::restriction for my whole project?"
  - "How do I disable an entire lint group?"
  - "What is the clippy::nursery group?"
---

# Quick Definition

Clippy organizes its lints into named groups based on their purpose and opinionatedness. The main groups are `clippy::all` (warn-by-default collection), `clippy::pedantic` (opinionated but production-ready), `clippy::restriction` (cherry-pick only), `clippy::style`, `clippy::correctness`, `clippy::complexity`, `clippy::perf`, `clippy::suspicious`, `clippy::cargo`, and `clippy::nursery`.

# Core Definition

Clippy lints are organized into groups that reflect their category and default severity:

**Warn-by-default groups** (included in `clippy::all`):
- **clippy::correctness** -- Lints that catch outright bugs or definitely wrong code
- **clippy::suspicious** -- Lints that catch code which is very likely wrong or useless
- **clippy::style** -- The most opinionated warn-by-default group; catches non-idiomatic patterns
- **clippy::complexity** -- Lints that catch unnecessarily complex code that can be simplified
- **clippy::perf** -- Lints that catch code that can be made more performant

**Allow-by-default groups** (must be explicitly enabled):
- **clippy::pedantic** -- Opinionated lints ready for production use, but may have intentional false positives to prevent false negatives. Clippy itself uses this group for self-linting.
- **clippy::restriction** -- Lints that "restrict" the language. Not meant to be enabled as a whole group; cherry-pick individual lints. Some lints in this group contradict other Clippy lints.
- **clippy::cargo** -- Lints related to Cargo manifest best practices
- **clippy::nursery** -- Lints that are still being developed; may have more false positives

The meta-group `clippy::all` encompasses all warn-by-default groups. Running `cargo clippy` without extra flags applies `clippy::all`.

# Prerequisites

- **clippy** -- Lint groups are a core organizational concept of Clippy
- **clippy-lint-levels** -- Groups are configured using the same allow/warn/deny levels as individual lints

# Key Properties

1. `clippy::all` is the default group applied by `cargo clippy` -- it includes correctness, suspicious, style, complexity, and perf
2. `clippy::pedantic` is allow-by-default but production-ready; expect to need `#[allow(..)]` attributes when enabling it
3. `clippy::restriction` should never be enabled as a whole group -- cherry-pick individual lints instead
4. Some restriction lints contradict other Clippy lints (e.g., one lint forbids `unwrap`, another might suggest it)
5. `clippy::style` is the most opinionated warn-by-default group; some teams prefer to disable it and cherry-pick
6. The warn-by-default groups are kept free from false positives (FPs) -- report any FPs found
7. Groups can be enabled or disabled just like individual lints: `#![warn(clippy::pedantic)]` or `-W clippy::pedantic`

# Construction / Recognition

## To Enable Additional Lint Groups:
1. Enable pedantic lints: `cargo clippy -- -W clippy::pedantic`
2. Enable both all and pedantic via attribute: `#![warn(clippy::all, clippy::pedantic)]`
3. Cherry-pick from restriction: `#![deny(clippy::unwrap_used, clippy::expect_used)]`

## To Disable a Lint Group:
1. Disable style entirely: `cargo clippy -- -A clippy::style`
2. Disable via attribute: `#![allow(clippy::style)]`
3. Disable all, then re-enable specifics: `cargo clippy -- -A clippy::all -W clippy::useless_format`

## To Identify a Lint's Group:
1. Check the lint list at https://rust-lang.github.io/rust-clippy/master/index.html
2. Each lint page shows its group membership

# Context & Application

The lint group system is Clippy's primary organizational mechanism. Understanding which groups are warn-by-default vs. allow-by-default is essential for configuring Clippy appropriately for a project.

**Common adoption patterns:**
- **Conservative**: Use defaults (`clippy::all`) only
- **Moderate**: Enable `clippy::pedantic` and allow specific false positives
- **Strict**: Enable `clippy::pedantic` plus cherry-picked `clippy::restriction` lints
- **Customized**: Disable `clippy::style`, cherry-pick from all groups to build a custom lint set

The documentation notes that Clippy uses `clippy::pedantic` on its own codebase, which serves as a signal that the group is considered production-ready despite being allow-by-default.

# Examples

**Example 1**: Enabling pedantic lints for an entire crate via source attribute:
```rust
#![warn(clippy::all, clippy::pedantic)]
```

**Example 2**: Disabling the style group and cherry-picking specific lints via CLI:
```bash
cargo clippy -- -A clippy::style -W clippy::needless_return -W clippy::redundant_closure
```

**Example 3**: Cherry-picking from the restriction group (the recommended approach):
```rust
#![deny(clippy::unwrap_used)]
#![deny(clippy::expect_used)]
```

**Example 4**: Allowing all Clippy lints and selectively enabling specific ones:
```bash
cargo clippy -- -A clippy::all -W clippy::useless_format -W clippy::needless_return
```

# Relationships

## Builds Upon
- **clippy** -- Lint groups are Clippy's organizational structure
- **clippy-lint-levels** -- Groups are controlled using the same allow/warn/deny levels

## Related
- **cargo-clippy** -- Groups are specified via CLI flags or affect the default behavior
- **clippy-configuration** -- Some group behaviors can be further tuned via `clippy.toml`
- **lint-declaration** -- Internal lint declarations include group membership

# Common Errors

- **Error**: Enabling `clippy::restriction` as a whole group and getting contradictory lint warnings.
  **Correction**: Never enable the restriction group wholesale. Cherry-pick individual restriction lints that fit your project's requirements.

- **Error**: Expecting `clippy::pedantic` to have zero false positives.
  **Correction**: The pedantic group intentionally accepts some false positives to avoid false negatives. Use `#[allow(..)]` attributes to suppress individual false positives in your code.

# Common Confusions

- **Confusion**: Thinking `clippy::all` includes every Clippy lint.
  **Clarification**: `clippy::all` only includes the warn-by-default groups (correctness, suspicious, style, complexity, perf). It does not include pedantic, restriction, cargo, or nursery.

- **Confusion**: Believing the `clippy::nursery` group is unstable or dangerous to use.
  **Clarification**: Nursery lints are still being refined and may have more false positives, but they can be useful. They are allow-by-default because they have not yet met the quality bar for warn-by-default inclusion.

# Source Reference

Chapter 1 (Getting Started), "Usage" section, subsections "Even more lints" (lines 82-118 of 01-getting-started.md) and "Too many lints" (lines 113-121). Group descriptions for pedantic and restriction are directly from the source.

# Verification Notes

- Group names: All groups listed are documented in the Clippy lint list and referenced in the source
- Default behavior: Source states `clippy::all` is the default group for `cargo clippy`
- Pedantic description: Directly quoted -- "really opinionated lints, that may have some intentional false positives"
- Restriction warning: Directly from source -- "You shouldn't enable the whole lint group, but cherry-pick lints"
- Self-linting note: Source states "Clippy uses the whole group to lint itself" about pedantic
- Confidence: HIGH -- group descriptions directly from official documentation
- Cross-references: All slugs verified against planned extractions
