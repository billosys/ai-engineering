---
concept: Gen Keyword Reservation
slug: gen-keyword-reservation
category: edition-2024
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "05-rust-2024"
chapter_number: 5
pdf_page: null
section: "gen keyword"
extraction_confidence: high
aliases:
  - "gen keyword"
  - "gen blocks"
  - "generator keyword"
  - "gen reserved keyword"
prerequisites:
  - rust-editions
related:
  - rust-2024-edition
contrasts_with: []
extends: []
answers_questions:
  - "Why is gen a reserved keyword in Rust 2024?"
  - "What are gen blocks in Rust?"
  - "How do I use gen as an identifier in Rust 2024?"
  - "What is RFC 3513?"
---

# Quick Definition

The `gen` keyword is reserved in Rust 2024 (RFC 3513) to enable future "gen blocks" that will provide an easier way to write iterators. Existing identifiers named `gen` must use the raw identifier syntax `r#gen`. This also covers the reserved syntax change for guarded strings (`#"foo"#`) and multi-hash tokens (`###`).

# Core Definition

The `gen` keyword has been reserved as part of RFC 3513 to introduce "gen blocks" in a future release of Rust. Gen blocks will provide a way to make it easier to write certain kinds of iterators, analogous to how `async` blocks provide an easier way to write `Future`s. Reserving the keyword in the 2024 Edition allows stabilization of gen blocks before the next edition.

Any existing identifier named `gen` must be converted to the raw identifier form `r#gen` to avoid conflicts. The `keyword_idents_2024` lint handles this automatically during migration.

**Additionally, the 2024 Edition reserves two new syntax forms (RFC 3593):**

1. One or more `#` characters immediately followed by a string literal (e.g., `#"foo"#`) -- these are "unprefixed guarded strings"
2. Two or more `#` characters in a row not separated by whitespace (e.g., `###`)

These were reserved for possible future language use. Prior editions already reserved *prefixed* guarded strings (e.g., `ident##"foo"##`), and 2024 extends this to unprefixed forms. The `rust_2024_guarded_string_incompatible_syntax` lint handles migration by inserting spaces.

Also, the `expr` macro fragment specifier now matches `const` and `_` expressions in 2024 (it did not in 2021). The `expr_2021` specifier is added for backward compatibility. The `missing_fragment_specifier` lint becomes a hard error.

# Prerequisites

- **Rust editions** -- understanding that editions can reserve new keywords

# Key Properties

1. `gen` is a reserved keyword starting in Rust 2024
2. Gen blocks (the intended use) are not yet stabilized -- only the keyword reservation is in this edition
3. Gen blocks are expected to be analogous to `async` blocks but for iterators
4. The `r#gen` raw identifier syntax allows continued use of `gen` as an identifier
5. The `keyword_idents_2024` lint automatically renames `gen` to `r#gen`
6. Guarded string syntax `#"foo"#` and multi-hash `###` are also reserved in 2024
7. The `expr` fragment specifier now matches `const` and `_` expressions in 2024
8. `expr_2021` is available for backward-compatible macro behavior

# Construction / Recognition

## Migrating `gen` Identifiers:

```rust
// Before (2021):
fn gen() { println!("generating!"); }
fn main() { gen(); }

// After (2024):
fn r#gen() { println!("generating!"); }
fn main() { r#gen(); }
```

## Migrating Macro Fragment Specifiers:

```rust
// In 2021, this matches the second rule for `const { 1 + 1 }`:
macro_rules! example {
    ($e:expr) => { println!("first rule"); };
    (const $e:expr) => { println!("second rule"); };
}

// cargo fix changes $e:expr to $e:expr_2021 to preserve behavior.
// Review whether you want the new behavior (expr matching const expressions).
```

# Context & Application

Keyword reservation is a standard practice in Rust's edition model. The `async` and `await` keywords were similarly reserved in the 2018 Edition before async/await syntax was stabilized. The `gen` reservation follows the same pattern: reserve early, stabilize the feature later, possibly even before the next edition.

Gen blocks are motivated by the difficulty of writing iterator implementations manually. Where `async` blocks desugar to anonymous `Future` types, gen blocks will desugar to anonymous `Iterator` types. The exact syntax and semantics are still being worked out via RFC 3513.

The macro fragment specifier change is a recurring pattern: as new syntax is added to Rust, `expr` is updated to match it, but only at edition boundaries to avoid breaking existing macros. The `expr_2021` variant is provided for macros that need the old matching behavior.

# Examples

**Example 1** (gen identifier migration): `cargo fix --edition` automatically converts `fn gen()` to `fn r#gen()` and all call sites from `gen()` to `r#gen()`.

**Example 2** (guarded string reservation): In a macro `demo!(#"foo"#)`, this was three tokens in 2021 (`#`, `"foo"`, `#`) but is now a reserved syntax error in 2024.

**Example 3** (expr specifier change): A macro with `($e:expr)` will now match `const { 1 + 1 }` in 2024, which it did not in 2021. The auto-fix changes it to `($e:expr_2021)` to preserve old behavior.

# Relationships

## Related
- **rust-2024-edition** -- gen reservation is part of the 2024 edition's reserved syntax changes

# Common Errors

- **Error**: Not running `cargo fix --edition` and manually searching for `gen` identifiers, missing call sites or macro uses.
  **Correction**: Use `cargo fix --edition` which runs the `keyword_idents_2024` lint to find and convert all occurrences automatically.

- **Error**: After `cargo fix` converts `$e:expr` to `$e:expr_2021`, keeping `expr_2021` without reviewing whether the macro should support `const` and `_` expressions.
  **Correction**: In most cases, you want `expr` (the new behavior). Review each macro to determine if there are conflicting rules that would change matching order.

# Common Confusions

- **Confusion**: Thinking gen blocks are available in Rust 2024.
  **Clarification**: Only the keyword reservation is in 2024. Gen blocks themselves are still unstable and under development. The reservation allows stabilization before the next edition.

- **Confusion**: Thinking `expr_2021` is deprecated or temporary.
  **Clarification**: `expr_2021` is a permanent addition that preserves the old matching behavior. It is the correct choice when your macro has rules that would be affected by `expr` matching `const` or `_` expressions.

# Source Reference

Rust Edition Guide, Chapter 5: Rust 2024. Three related sections: "`gen` keyword" (RFC 3513), "Reserved syntax" (RFC 3593), and "Macro Fragment Specifiers." Also covers "Missing macro fragment specifiers" which becomes a hard error.

# Verification Notes

- Gen block purpose (iterator analogy): from source describing RFC 3513
- Reserved syntax details (guarded strings, multi-hash): from "Reserved syntax" section
- Fragment specifier changes: from "Macro Fragment Specifiers" section with the const expression example
- Confidence: HIGH -- all information directly stated in the source
- Cross-references: slugs verified against this extraction set
