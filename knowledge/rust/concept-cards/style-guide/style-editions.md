---
# === CORE IDENTIFICATION ===
concept: Style Editions
slug: style-editions

# === CLASSIFICATION ===
category: style
subcategory: evolution
tier: intermediate

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Style Editions"
chapter_number: 8
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust style editions"
  - "rustfmt style edition"
  - "formatting editions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-style-guide
  - formatting-conventions
extends: []
related:
  - naming-conventions
  - cargo-toml-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Rust style editions?"
  - "How does the Rust formatting style evolve over time?"
  - "What changed in the Rust 2024 style edition?"
  - "Can I update the style edition separately from the Rust edition?"
  - "Which Rust editions share the same style edition?"
  - "What happens when new syntax is added but my style edition predates it?"
  - "How does nightly-only syntax get formatted?"
---

# Quick Definition

Style editions are the mechanism by which the default Rust formatting style evolves over time without breaking existing code or CI pipelines. Each Rust edition has a corresponding style edition (though not all editions introduce style changes), and tools like `rustfmt` allow updating the style edition independently of the Rust language edition. Nightly-only syntax has provisional formatting rules documented separately.

# Core Definition

The default Rust style evolves alongside the language, but changes to formatting rules could break established code style and CI checks. Style editions solve this: "To avoid breaking established code style, and CI jobs checking code style, changes to the default Rust style only appear in *style editions*." (Ch. 8: Style Editions).

Style editions correspond to Rust language editions: "Code written in a given Rust edition uses the corresponding Rust style edition by default." However, "formatting tools such as `rustfmt` allow updating the style edition separately from the Rust edition," making it easier to migrate code style independently from semantic language changes.

Not all Rust editions introduce style changes: "Rust 2015, Rust 2018, and Rust 2021 all use the same style edition." The Rust 2024 style edition is the first to diverge.

For constructs that didn't exist when a style edition was archived, the formatting comes from "the first subsequent style edition providing formatting rules for that construct (without any of the systematic/global changes from that style edition)." This ensures all valid syntax gets formatted regardless of which style edition is active.

**Rust 2024 style edition changes** include (Ch. 8): miscellaneous `rustfmt` bugfixes, version-sort (sorting `x8`, `x16`, `x32`, `x64`, `x128` in that order), and changing "ASCIIbetical" sort to Unicode-aware "non-lowercase before lowercase."

**Rust next style edition** introduces: "Never break within a nullary function call `func()` or a unit literal `()`."

**Nightly-only syntax** (Ch. 9) has provisional formatting rules that are documented in a separate chapter and integrated into the main guide upon stabilization. Currently this includes **frontmatter** (feature gate: `frontmatter`, tracking issue #136889) -- a mechanism for placing metadata before code. Frontmatter fences use the minimum number of dashes necessary (minimum 3), with no blank lines between the frontmatter and the start of the file or a shebang, and zero or one blank lines before following content.

# Prerequisites

- **rust-style-guide** -- understanding the overall style guide and its purpose
- **formatting-conventions** -- the core formatting rules that style editions modify

# Key Properties

1. **Edition-aligned**: Style editions correspond to Rust language editions by default
2. **Independently configurable**: `rustfmt` allows setting the style edition separately from the Rust edition
3. **Non-breaking**: Style changes only take effect when a crate opts into a new style edition
4. **Forward-compatible syntax formatting**: Newer syntax constructs get formatted even on older style editions, using rules from the first subsequent style edition that defines them
5. **Shared editions**: Rust 2015, 2018, and 2021 all share the same style edition
6. **Archived style guides**: Each past style edition has a corresponding archived version of the style guide
7. **Nightly syntax is provisional**: Formatting rules for nightly-only syntax are documented separately and may change without stability guarantees

# Construction / Recognition

## Checking Your Current Style Edition:
1. Check `edition` in `Cargo.toml` -- this determines the default style edition
2. Check `rustfmt.toml` or `.rustfmt.toml` for an explicit `style_edition` override
3. If neither is set, the style edition matches the Rust edition (or 2015 by default)

## Migrating to a New Style Edition:
1. Update the `style_edition` in `rustfmt.toml` (or update the `edition` in `Cargo.toml`)
2. Run `cargo fmt` to reformat all code under the new style edition
3. Review and commit the formatting changes
4. Update CI configuration if it pins a specific style edition

## Identifying Style Edition Differences:
- Version-sort ordering (2024): `u8, u16, u32` instead of ASCIIbetical `u128, u16, u32`
- Non-lowercase before lowercase sorting (2024): `ZYXW` before `zyxw`
- Nullary function calls never broken across lines (next edition): `func()` stays on one line

# Context & Application

Style editions address a real tension in the Rust ecosystem: the desire to improve formatting rules over time versus the need for stable, predictable formatting in CI pipelines and version control. Without style editions, any `rustfmt` update could reformat an entire codebase, producing noisy diffs and failing CI checks. By tying style changes to explicit edition opt-in, teams control when formatting changes are adopted.

The independent configurability is particularly useful during the transition period between Rust editions, allowing teams to adopt new formatting rules before or after adopting new language features. This is relevant for large codebases where formatting changes and semantic changes are best reviewed separately.

Nightly-only syntax formatting (like frontmatter) follows a separate lifecycle: rules are provisional, documented in their own chapter, and only integrated into the main guide upon stabilization. This prevents premature commitment to formatting rules for features that may change.

# Examples

**Example 1** (Ch. 8): The Rust 2024 style edition changes sorting behavior:
```rust
// Rust 2015/2018/2021 style (ASCIIbetical):
// u128, u16, u32, u64, u8

// Rust 2024 style (version-sort):
// u8, u16, u32, u64, u128
```

**Example 2** (Ch. 8): Non-lowercase before lowercase in 2024:
```rust
// Rust 2024 style: uppercase identifiers sort before lowercase
// ABCD, Abcd, abcd
```

**Example 3** (Ch. 9): Nightly frontmatter formatting:
```rust
#!/usr/bin/env cargo
--- cargo
[dependencies]
regex = "1"
---

fn main() {}
```
No blank lines between the shebang and frontmatter fences; frontmatter fences use the minimum number of dashes (3 minimum); zero or one blank lines before following content.

**Example 4**: Configuring style edition independently in `rustfmt.toml`:
```toml
# Use Rust 2024 style formatting even if Cargo.toml says edition = "2021"
style_edition = "2024"
```

# Relationships

## Builds Upon
- **rust-style-guide** -- style editions are how the guide evolves over time
- **formatting-conventions** -- the core rules that style editions selectively modify

## Enables
- Controlled adoption of formatting improvements across the ecosystem
- Stable CI pipelines that don't break on `rustfmt` updates

## Related
- **naming-conventions** -- naming rules are part of the style but not currently edition-dependent
- **cargo-toml-conventions** -- Cargo.toml formatting follows the same edition mechanism

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming that updating the Rust edition in `Cargo.toml` will not change code formatting.
  **Correction**: The Rust edition determines the default style edition. Moving from `edition = "2021"` to `edition = "2024"` will also change the style edition, potentially reformatting code. Run `cargo fmt` after changing editions.

- **Error**: Assuming all Rust editions have distinct style editions.
  **Correction**: Rust 2015, 2018, and 2021 all share the same style edition. Only Rust 2024 introduced style changes.

- **Error**: Expecting nightly syntax formatting to be stable.
  **Correction**: "There is no guarantee of the stability of this chapter in contrast to the rest of the style guide." Nightly formatting rules are provisional and may change.

# Common Confusions

- **Confusion**: Thinking style editions and Rust language editions are the same thing.
  **Clarification**: They correspond by default but can be configured independently. A crate using Rust 2021 can opt into the 2024 style edition via `rustfmt.toml` without changing any language semantics.

- **Confusion**: Thinking older style editions cannot format newer syntax constructs.
  **Clarification**: If a construct didn't exist when a style edition was archived, it uses formatting rules from "the first subsequent style edition providing formatting rules for that construct" -- without applying that edition's global/systematic changes. All valid syntax gets formatted.

- **Confusion**: Thinking the "next" style edition is a released, usable edition.
  **Clarification**: The "Rust next style edition" documents planned changes for a future edition. These rules are not yet active in any released style edition.

# Source Reference

Chapter 8: Style Editions (style edition concept, Rust 2024 changes, Rust 2015/2018/2021 shared edition, next edition); Chapter 9: Nightly-only Syntax (frontmatter formatting). No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 8 -- "changes to the default Rust style only appear in *style editions*"
- Edition sharing: Directly from Ch. 8 -- "Rust 2015, Rust 2018, and Rust 2021 all use the same style edition"
- 2024 changes: Directly from Ch. 8 -- version-sort, Unicode-aware sorting, rustfmt bugfixes
- Nightly frontmatter: Directly from Ch. 9 -- feature gate `frontmatter`, tracking issue #136889
- Confidence rationale: HIGH -- the source provides clear definitions and specific change lists
- Uncertainties: The "next" style edition changes are forward-looking and may evolve
- Cross-reference status: rust-style-guide, formatting-conventions are in this extraction set
