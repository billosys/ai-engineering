---
# === CORE IDENTIFICATION ===
concept: Formatting Conventions
slug: formatting-conventions

# === CLASSIFICATION ===
category: style
subcategory: core-rules
tier: foundational

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Introduction"
chapter_number: 0
pdf_page: null
section: "Formatting conventions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust formatting rules"
  - "rustfmt conventions"
  - "Rust code formatting"
  - "Rust indentation rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-style-guide
extends: []
related:
  - naming-conventions
  - cargo-toml-conventions
  - item-formatting
  - statement-formatting
  - expression-formatting
  - type-formatting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many spaces should I use for indentation in Rust?"
  - "What is the maximum line width for Rust code?"
  - "Should I use block indent or visual indent in Rust?"
  - "When should I use trailing commas in Rust?"
  - "How do blank lines work in Rust formatting?"
  - "How should comments be formatted in Rust?"
  - "How should attributes be formatted in Rust?"
  - "What sorting order does the Rust style guide use?"
  - "How wide should comment lines be in Rust?"
---

# Quick Definition

The core formatting conventions of the Rust Style Guide specify 4-space indentation, 100-character maximum line width, block indent over visual indent, trailing commas in multi-line lists, version-sorting for ordered items, and specific rules for blank lines, comments, and attributes.

# Core Definition

The formatting conventions form the foundation of the default Rust style. Every other section of the style guide builds upon these rules. The key rules are:

**Indentation and line width**: "Use spaces, not tabs. Each level of indentation must be 4 spaces (that is, all indentation outside of string literals and comments must be a multiple of 4). The maximum width for a line is 100 characters." (Ch. 0: Indentation and line width).

**Block indent over visual indent**: The guide prefers block indent, where continuation lines are indented one level deeper than the opening construct, over visual indent, where continuation lines align with the opening delimiter. Block indent "makes for smaller diffs (e.g., if `a_function_call` is renamed) and less rightward drift."

**Trailing commas**: "In comma-separated lists of any kind, use a trailing comma when followed by a newline." This applies to function arguments, array elements, struct fields, and any other comma-separated construct. The rationale: "appending or removing items does not require modifying another line to add or remove a comma."

**Blank lines**: "Separate items and statements by either zero or one blank lines (i.e., one or two newlines)." No more than one blank line between any two items or statements.

**Trailing whitespace**: "Do not include trailing whitespace on the end of any line. This includes blank lines, comment lines, code lines, and string literals." (With care for preserving string literal values.)

**Sorting**: When the style specifies sorting, use "version sorting" -- a Unicode-aware algorithm that sorts `x8` before `x16` (numeric chunks compared by value), underscores immediately after spaces, and non-lowercase characters before lowercase characters.

# Prerequisites

- **rust-style-guide** -- understanding the overall style guide and its purpose

# Key Properties

1. **Spaces, never tabs**: All indentation uses spaces, with each level being exactly 4 spaces
2. **100-character line width**: The hard maximum for any line of code
3. **Block indent preferred**: Continuation lines indented one level (4 spaces) from the containing construct, not aligned to a delimiter
4. **Trailing commas in multi-line**: Every comma-separated list uses a trailing comma when the closing delimiter is on a new line
5. **Zero or one blank lines**: Items and statements separated by at most one blank line
6. **No trailing whitespace**: On any line, including blank lines and inside comments
7. **Version sorting**: Numeric-aware sorting that handles identifiers like `u8`, `u16`, `u32` naturally
8. **80-character comment lines**: Comment-only lines limited to 80 characters (excluding indentation) or the 100-character maximum (including indentation), whichever is smaller
9. **Line comments preferred**: `//` preferred over `/* ... */`; `///` preferred over `/** ... */` for doc comments
10. **Single derive attribute**: Multiple `#[derive(...)]` attributes must be combined into one, preserving order

# Construction / Recognition

## Applying Block Indent:
1. When a construct's arguments or elements don't fit on one line, place opening delimiter at end of first line
2. Indent all items one level (4 spaces) deeper than the opening line
3. Place closing delimiter on its own line at the same level as the opening line
4. Add trailing comma after the last item

## Applying Comment Rules:
1. Use `//` for line comments with a single space after the sigil
2. Start comments with a capital letter, end with a period
3. Limit comment-only lines to 80 characters (excluding indentation)
4. Put comments on their own line where possible; use a single space before inline comments
5. Put doc comments (`///`) before attributes

## Applying Attribute Rules:
1. Place each attribute on its own line, indented to the item's level
2. For inner attributes (`#!`), indent to the level of the item's interior
3. Format attribute argument lists like function calls (block indent if multi-line)
4. Use a single space before and after `=` in attributes like `#[foo = 42]`

# Context & Application

These conventions are enforced automatically by `rustfmt` and form the baseline that all other formatting rules in the style guide build upon. The indentation and line width rules affect every line of Rust code. The trailing comma and block indent rules shape how function signatures, calls, struct literals, match arms, and all other multi-line constructs are formatted. The sorting rules apply to use declarations, module lists, match arms on integer-like values, and similar ordered constructs.

# Examples

**Example 1** (Ch. 0): Block indent vs. visual indent:
```rust
// Block indent (preferred)
a_function_call(
    foo,
    bar,
);

// Visual indent (avoid)
a_function_call(foo,
                bar);
```

**Example 2** (Ch. 0): Trailing commas in arrays:
```rust
let array = [
    element,
    another_element,
    yet_another_element,
];
```

**Example 3** (Ch. 0): Blank line usage:
```rust
fn foo() {
    let x = ...;

    let y = ...;
    let z = ...;
}

fn bar() {}
fn baz() {}
```

**Example 4** (Ch. 0): Comment width rules:
```rust
// This comment goes up to the ................................. 80 char margin.

{
    // This comment is .............................................. 80 chars wide.
}

{
    {
        {
            {
                {
                    {
                        // This comment is limited by the .......... 100 char margin.
                    }
                }
            }
        }
    }
}
```

**Example 5** (Ch. 0): Attribute formatting:
```rust
#[repr(C)]
#[foo(foo, bar)]
#[long_multi_line_attribute(
    split,
    across,
    lines,
)]
struct CRepr {
    #![repr(C)]
    x: f32,
    y: f32,
}
```

**Example 6** (Ch. 0): Version sorting -- identifiers sort naturally by numeric value:
```
u8, u16, u32, u64, u128, u256
x86, x86_32, x86_64, x86_128, x87
```
Underscores sort immediately after spaces, and non-lowercase characters sort before lowercase characters.

# Relationships

## Builds Upon
- **rust-style-guide** -- these conventions are part of the default style defined by the guide

## Enables
- **item-formatting** -- module-level item formatting builds on these core conventions
- **statement-formatting** -- statement formatting applies these indentation and width rules
- **expression-formatting** -- expression formatting uses block indent and trailing comma rules
- **type-formatting** -- type formatting follows the same indentation and width conventions

## Related
- **naming-conventions** -- the other major set of non-formatting style conventions
- **cargo-toml-conventions** -- applies the same line width and indentation to Cargo.toml

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using tabs instead of spaces, or using 2-space indentation.
  **Correction**: The Rust style requires spaces only, with exactly 4 spaces per indentation level. All indentation outside string literals and comments must be a multiple of 4.

- **Error**: Using visual indent to align arguments with an opening parenthesis.
  **Correction**: Block indent is preferred. Place arguments on the next line indented 4 spaces from the construct's indentation level, not aligned to the opening delimiter.

- **Error**: Omitting trailing commas in multi-line constructs.
  **Correction**: Always use a trailing comma when the closing delimiter (`)`, `]`, `}`) is on a new line. This applies to all comma-separated lists -- function arguments, array elements, struct fields, enum variants, etc.

- **Error**: Adding multiple blank lines between functions or items.
  **Correction**: Use at most one blank line (two newlines) between items or statements. Zero blank lines are also acceptable.

# Common Confusions

- **Confusion**: Thinking the 100-character limit applies to comments the same way as code.
  **Clarification**: Comment-only lines are limited to 80 characters (excluding indentation) or the 100-character maximum (including indentation), whichever is smaller. Code lines use the full 100-character width.

- **Confusion**: Assuming version sorting is the same as alphabetical sorting.
  **Clarification**: Version sorting treats consecutive digits as numeric values, so `x8` sorts before `x16`. Standard alphabetical sorting would put `x16` before `x8` because `1` < `8` character-wise.

- **Confusion**: Thinking trailing commas are always required.
  **Clarification**: Trailing commas are required only "when followed by a newline" -- i.e., in multi-line constructs. Single-line constructs like `Foo { f1, f2 }` do not use trailing commas.

# Source Reference

Chapter 0: Introduction, section "Formatting conventions" -- covers indentation, line width, block indent, trailing commas, blank lines, trailing whitespace, sorting, comments, doc comments, attributes, and small items. No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch. 0 section "Formatting conventions" with exact quotes for indentation, line width, trailing commas, blank lines, and trailing whitespace rules
- Sorting algorithm: Detailed directly from Ch. 0 section "Sorting" including the version-sort specification
- Confidence rationale: HIGH -- these are the explicitly documented core rules of the style guide
- Uncertainties: The exact definition of "small" items is intentionally left to tools
- Cross-reference status: rust-style-guide is in this extraction set; item-formatting, statement-formatting, expression-formatting, type-formatting are from Agent B
