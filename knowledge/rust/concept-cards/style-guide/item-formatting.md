---
# === CORE IDENTIFICATION ===
concept: Item Formatting
slug: item-formatting

# === CLASSIFICATION ===
category: style
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Rust Style Guide"
source_slug: style-guide
authors: "The Rust Style Team"
chapter: "Items"
chapter_number: 1
pdf_page: null
section: "Function definitions, Structs, Enums, Traits, Impls, Generics, Where clauses, Imports"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "item style rules"
  - "function formatting"
  - "struct formatting"
  - "enum formatting"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - type-formatting
  - statement-formatting
  - expression-formatting
  - rust-style-guide
  - formatting-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Rust function signatures be formatted?"
  - "How should structs and enums be formatted in Rust?"
  - "How should traits and impls be formatted?"
  - "How should generics and where clauses be formatted?"
  - "How should use/import statements be ordered?"
---

# Quick Definition

Items are the top-level constructs in a Rust module (functions, structs, enums, traits, impls, type aliases, extern items, use statements). The Rust Style Guide prescribes specific formatting rules for each, emphasizing searchability (e.g., `fn [name]`), consistent block-indentation for multi-line signatures, and trailing commas on multi-line parameter/field lists.

# Core Definition

Items must follow a strict ordering at the top of a file: `extern crate` statements first (alphabetically), then `use` statements before module declarations (`mod foo;`), each group version-sorted with `self` and `super` first. Function signatures use the format `[pub] [unsafe] [extern ["ABI"]] fn foo(args) -> ReturnType { ... }`, breaking after the opening parenthesis when a signature does not fit one line, with each argument block-indented and a trailing comma on the last argument. Structs, enums, traits, and impls follow consistent rules: opening brace on the same line, fields/variants/items block-indented with trailing commas, and closing brace on its own line. Generics prefer single-line formatting, and where clauses place each bound on its own block-indented line with a trailing comma.

# Prerequisites

None -- this is a foundational style reference for Rust item formatting.

# Key Properties

1. **File ordering**: `extern crate` (alphabetical) -> `use` statements -> `mod` declarations -> other items
2. **Function signatures**: break after `(` and before `)` when multi-line; each argument on its own block-indented line with trailing comma
3. **Structs/Unions**: fields block-indented with trailing commas; if a field type is too long, indent it on the next line
4. **Enums**: each variant on its own line; struct variants follow struct formatting; small struct variants may be single-line with spaces around braces and no trailing comma
5. **Traits/Impls**: empty bodies use `{}` on one line; otherwise break after `{` and before `}`; trait bounds use spaces around `+` and after `:`
6. **Generics**: prefer single-line; no spaces before/after `<` or before `>`; space after `>` only before words or `{`, not `(`; prefer `where` clause for complex bounds
7. **Where clauses**: each predicate on its own block-indented line with trailing comma; block following where clause starts on a new line
8. **Imports**: single-line where possible; no spaces around braces; version-sorted within groups; nested imports force multi-line form

# Construction / Recognition

## Function Signature Formatting:
1. Write the signature on one line if it fits: `fn foo(arg1: T1, arg2: T2) -> R {`
2. If it does not fit, break after `(`, put each arg on its own block-indented line with trailing comma, then `) -> R {`
3. Avoid comments within the signature itself

## Where Clause Formatting:
1. If immediately after a closing bracket, write `where` on the same line with a space before it
2. Otherwise, put `where` on a new line at the same indentation level
3. Each predicate on its own block-indented line with trailing comma
4. If a predicate contains `+`, break before each `+` with further block indentation
5. The block or body following the where clause starts on a new line

## Import Formatting:
1. Format on one line where possible, no spaces around braces: `use a::b::{foo, bar};`
2. For multi-line imports, break after `{`, block-indent names, trailing comma, break before `}`
3. Nested imports force multi-line form; non-nested imports grouped on as few lines as possible
4. Version-sort within groups; `self`/`super` come first; groups separated by blank lines are not reordered

# Context & Application

These rules are enforced by `rustfmt` and represent the official Rust style. People often search for functions with `fn [function-name]`, so consistent formatting of the `fn` keyword and signature is critical for discoverability. The rules optimize for readability at a glance: single-line when possible, consistent block-indentation when line-breaking is needed, and trailing commas to minimize diffs when adding items.

Key formatting decisions: prefer unit structs (`struct Foo;`) over empty structs; prefer named-field structs over long tuple structs; always specify ABI for extern items (`extern "C" fn`, not `extern fn`); use `{}` for `macro_rules!` definitions; prefer single-letter generic parameter names.

# Examples

**Example 1** (Function signatures -- single-line vs multi-line):
```rust
// Single line
fn foo(arg1: i32, arg2: i32) -> i32 {
    ...
}

// Multi-line: break after (, each arg indented, trailing comma
fn foo(
    arg1: i32,
    arg2: i32,
) -> i32 {
    ...
}
```

**Example 2** (Where clause with complex bounds):
```rust
impl<T: ?Sized, Idx> IndexRanges<Idx> for T
where
    T: Index<Range<Idx>, Output = Self::Output>
        + Index<RangeTo<Idx>, Output = Self::Output>
        + Index<RangeFrom<Idx>, Output = Self::Output>
        + Index<RangeFull>,
{
    ...
}
```

**Example 3** (Enum formatting):
```rust
enum FooBar {
    First(u32),
    Second,
    Error {
        err: Box<Error>,
        line: u32,
    },
}
// Small struct variant on one line, spaces around braces, no trailing comma:
enum FooBar {
    Error { err: Box<Error>, line: u32 },
}
```

**Example 4** (Trait with broken bounds):
```rust
pub trait IndexRanges:
    Index<Range<usize>, Output=Self>
    + Index<RangeTo<usize>, Output=Self>
    + Index<RangeFrom<usize>, Output=Self>
{
    ...
}
```

**Example 5** (Import ordering and nested imports):
```rust
use a::b::{
    x, y, z,
    u::{...},
    w::{...},
};
```

# Relationships

## Builds Upon
None -- this is a foundational style reference.

## Enables
- **statement-formatting** -- statements appear within item bodies
- **expression-formatting** -- expressions appear within item bodies

## Related
- **type-formatting** -- type formatting rules apply within item signatures
- **rust-style-guide** -- this card covers Chapter 1 of the official style guide
- **formatting-conventions** -- general formatting conventions that underpin these rules

## Contrasts With
None explicitly stated.

# Common Errors

- **Error**: Omitting the trailing comma on the last argument of a multi-line function signature.
  **Correction**: Always include a trailing comma on the last argument when using multi-line format. This reduces diffs and is the official style.

- **Error**: Putting spaces before or after `<` or before `>` in generics.
  **Correction**: No spaces around angle brackets in generics. Only put a space after `>` if followed by a word or `{`, not `(`.

- **Error**: Breaking a generics clause across lines instead of using a where clause.
  **Correction**: If a generics clause is large enough to need line-breaking, prefer moving bounds to a where clause instead.

# Common Confusions

- **Confusion**: Thinking `where` must always go on a new line.
  **Clarification**: If the `where` immediately follows a closing bracket (e.g., `)` of the parameter list), it goes on the same line with a space before it. Otherwise it goes on a new line at the same indentation level.

- **Confusion**: Thinking small enum struct variants should use trailing commas in their field list.
  **Clarification**: Small struct variants formatted on one line use spaces around braces but no trailing comma: `Error { err: Box<Error>, line: u32 }`.

- **Confusion**: Thinking imports within a group can be in any order.
  **Clarification**: Imports within a group must be version-sorted, with `self` and `super` first. Groups separated by blank lines are not merged or reordered relative to each other.

# Source Reference

Chapter 1: Items. Covers function definitions, tuples and tuple structs, enums, structs and unions, traits, impls, extern crate, modules, macro_rules, generics, where clauses, type aliases, associated types, extern items, and imports (use statements). Rules sourced from the official Rust Style Guide.

# Verification Notes

- Definition source: Direct rules from Chapter 1 "Items" of the Rust Style Guide
- Key Properties: All from explicit formatting prescriptions in the source
- Confidence rationale: HIGH -- the source is the authoritative Rust style guide with explicit, prescriptive rules
- Uncertainties: None for the stated rules
- Cross-reference status: All slugs reference cards in this extraction set or planned cross-references
