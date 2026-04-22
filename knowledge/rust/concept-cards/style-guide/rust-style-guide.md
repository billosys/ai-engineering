---
# === CORE IDENTIFICATION ===
concept: Rust Style Guide
slug: rust-style-guide

# === CLASSIFICATION ===
category: style
subcategory: overview
tier: foundational

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Introduction"
chapter_number: 0
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust formatting guide"
  - "rustfmt style guide"
  - "default Rust style"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - formatting-conventions
  - naming-conventions
  - cargo-toml-conventions
  - style-editions
  - item-formatting
  - statement-formatting
  - expression-formatting
  - type-formatting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Rust Style Guide?"
  - "Why should I use an automatic formatting tool like rustfmt?"
  - "What is the default Rust style?"
  - "What is the relationship between the style guide and rustfmt?"
  - "What guiding principles drive Rust style decisions?"
  - "What should I do if rustfmt and the style guide disagree?"
---

# Quick Definition

The Rust Style Guide defines the official default formatting style for Rust code. It serves as the reference for tools like `rustfmt` and establishes community-consistent formatting conventions that reduce cognitive load, eliminate style debates, and produce clean diffs.

# Core Definition

The Rust Style Guide is the authoritative document defining the default Rust style. As stated in the introduction: "The Rust Style Guide defines the default Rust style, and *recommends* that developers and tools follow the default Rust style. Tools such as `rustfmt` use the style guide as a reference for the default style." (Ch. 0: Introduction). Everything in the guide, including imperative instructions like "insert a space" or "break the line after," refers to the default style, not a mandatory requirement -- developers are not forbidden from following a non-default style, and tools may offer configuration options.

The guide exists because formatting is "a mostly mechanical task which takes both time and mental effort." By using an automatic formatting tool, programmers are freed to focus on more important things. The deeper benefit is community consistency: "By ensuring that all Rust code has similar formatting, less mental effort is required to comprehend a new project, lowering the barrier to entry for new developers."

When the style guide and `rustfmt` disagree, that represents a bug in one or both -- it should be reported to the style team and/or the rustfmt team for investigation.

The style team follows four guiding principles in rough priority order (Ch. 7: Principles): (1) **Readability** -- scan-ability, avoiding misleading formatting, accessibility across hardware and non-visual interfaces, readability in plain-text contexts like diffs and error messages; (2) **Aesthetics** -- sense of beauty, consistency with other languages/tools; (3) **Specifics** -- compatibility with version control (preserving diffs, merge-friendliness), preventing rightward drift, minimizing vertical space; (4) **Application** -- ease of manual application, ease of implementation in tools, internal consistency, simplicity of formatting rules.

# Prerequisites

- None. The style guide is a foundational resource for all Rust development.

# Key Properties

1. **Recommends, not mandates**: The guide defines the default style but does not forbid non-default styles or tool configuration options
2. **Tool-backed**: `rustfmt` is the primary tool implementing the guide; the guide serves as its reference
3. **Community consistency**: The primary value proposition -- reducing cognitive overhead across the entire Rust ecosystem
4. **Pattern matching**: Consistent formatting enables humans to comprehend new codebases faster through familiar visual patterns
5. **Bug parity**: Discrepancies between the guide and `rustfmt` are considered bugs to be reported and fixed
6. **Corpus-tested**: New formatting tools should be tested against existing Rust code to avoid widespread breakage
7. **Principled decisions**: Style choices are driven by readability, aesthetics, VCS compatibility, and implementation simplicity (in that priority order)
8. **Small item heuristic**: The guide references the concept of *small* items (e.g., `Foo { f1, f2 }` on one line vs. multi-line) but leaves the exact definition to individual tools

# Construction / Recognition

## Applying the Default Style:
1. Install `rustfmt`: comes with the standard Rust toolchain via `rustup`
2. Run `cargo fmt` to format all source files in a project
3. Optionally configure via `rustfmt.toml` for non-default settings

## Recognizing Default-Styled Code:
- 4-space indentation (never tabs)
- 100-character maximum line width
- Block indent style (not visual indent)
- Trailing commas in multi-line lists
- No trailing whitespace on any line
- Version-sorted items where sorting is specified

## Recognizing Non-Default Style:
- Tab indentation or non-4-space indentation
- Visual indent alignment (arguments aligned to opening parenthesis)
- Missing trailing commas in multi-line constructs
- Line widths significantly exceeding 100 characters

# Context & Application

The Rust Style Guide is relevant whenever writing, reviewing, or reading Rust code. It is the single source of truth for the default formatting conventions used across the Rust ecosystem. Library authors publishing to crates.io typically follow the default style to make contributions easier. Teams adopt it to eliminate style discussions in code review. CI pipelines commonly enforce it via `cargo fmt -- --check`. The guide covers items, statements, expressions, types, comments, attributes, and `Cargo.toml` formatting.

# Examples

**Example 1** (Ch. 0): Block indent preferred over visual indent:
```rust
// Block indent (preferred)
a_function_call(
    foo,
    bar,
);

// Visual indent (not preferred)
a_function_call(foo,
                bar);
```
Block indent produces smaller diffs (e.g., renaming `a_function_call` only changes one line) and prevents rightward drift.

**Example 2** (Ch. 0): Trailing commas in multi-line lists:
```rust
function_call(
    argument,
    another_argument,
);
```
Trailing commas make appending or removing items a single-line diff change.

**Example 3** (Ch. 0): Comment formatting:
```rust
// A comment on an item.
struct Foo { ... }

fn foo() {} // A comment after an item.

pub fn foo(/* a comment before an argument */ x: T) {...}
```
Comments should usually be complete sentences starting with a capital letter and ending with a period. Comment-only lines are limited to 80 characters (excluding indentation) or the 100-character maximum (including indentation), whichever is smaller.

**Example 4** (Ch. 0): Small vs. normal formatting:
```rust
// Normal formatting
Foo {
    f1: an_expression,
    f2: another_expression(),
}

// "small" formatting
Foo { f1, f2 }
```

# Relationships

## Builds Upon
- None -- the style guide is a foundational resource

## Enables
- **formatting-conventions** -- the core formatting rules defined by the guide
- **naming-conventions** -- naming rules for types, functions, variables, and constants
- **cargo-toml-conventions** -- formatting and metadata rules for Cargo.toml files
- **style-editions** -- how the style evolves over time with Rust editions
- **item-formatting** -- detailed formatting rules for module-level items
- **statement-formatting** -- formatting rules for statements
- **expression-formatting** -- formatting rules for expressions
- **type-formatting** -- formatting rules for types

## Related
- **formatting-conventions** -- the specific core rules (indentation, line width, etc.)
- **style-editions** -- how the default style evolves across edition boundaries

## Contrasts With
- None within this source

# Common Errors

- **Error**: Treating the style guide as a strict mandate that forbids any deviation.
  **Correction**: The guide defines the *default* style and recommends it. Developers and tools may follow non-default styles; the guide explicitly states "This should not be interpreted as forbidding developers from following a non-default style."

- **Error**: Assuming `rustfmt` output is always correct when it conflicts with the style guide.
  **Correction**: Discrepancies between `rustfmt` and the style guide represent bugs that should be reported. Neither is automatically authoritative when they disagree.

- **Error**: Applying formatting rules inside string literals (e.g., removing trailing whitespace from multiline strings).
  **Correction**: The guide notes that "avoiding trailing whitespace in string literals requires care to preserve the value of the literal." String content is not subject to formatting rules.

# Common Confusions

- **Confusion**: Thinking the guide only matters if you use `rustfmt`.
  **Clarification**: The guide defines community-standard formatting. Even without `rustfmt`, following these conventions improves readability and reduces friction for contributors. The guide explicitly mentions ease of manual application as a design principle.

- **Confusion**: Equating the style guide with `rustfmt` configuration.
  **Clarification**: `rustfmt` implements the guide but also offers configuration options for non-default styles. The guide is the specification; `rustfmt` is an implementation with additional flexibility.

- **Confusion**: Thinking readability is subjective and therefore the guide's rules are arbitrary.
  **Clarification**: The style team follows explicit guiding principles -- readability (including accessibility and plain-text contexts), aesthetics, VCS compatibility, and ease of implementation -- applied in that priority order.

# Source Reference

Chapter 0: Introduction (Motivation, The default Rust style, Bugs, Formatting conventions); Chapter 7: Principles and Rationale. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 0 -- "The Rust Style Guide defines the default Rust style, and *recommends* that developers and tools follow the default Rust style."
- Principles source: Directly from Ch. 7 -- readability, aesthetics, specifics, application in priority order
- Confidence rationale: HIGH -- the source provides clear definitions and motivations
- Uncertainties: None for the overview
- Cross-reference status: formatting-conventions, naming-conventions, cargo-toml-conventions, style-editions are in this extraction set; item-formatting, statement-formatting, expression-formatting, type-formatting are from Agent B
