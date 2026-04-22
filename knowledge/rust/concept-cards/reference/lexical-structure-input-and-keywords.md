---
concept: Lexical Structure - Input Format and Keywords
slug: lexical-structure-input-and-keywords
category: language-specification
subcategory: lexical-structure
tier: foundational
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: null
section: "Input format / Shebang / Keywords / Identifiers / Comments / Whitespace"
extraction_confidence: high
aliases:
  - "Rust keywords"
  - "strict keywords"
  - "reserved keywords"
  - "weak keywords"
  - "raw identifiers"
  - "Rust comments"
  - "doc comments"
  - "identifier normalization"
  - "UTF-8 source encoding"
prerequisites:
  - rust-reference-overview
extends: []
related:
  - lexical-structure-tokens-and-literals
  - reference-macros-by-example
contrasts_with: []
answers_questions:
  - "What encoding must Rust source files use?"
  - "What preprocessing happens before tokenization?"
  - "What are Rust's three categories of keywords?"
  - "What keywords are strict, reserved, and weak?"
  - "How do raw identifiers work?"
  - "What Unicode characters are allowed in identifiers?"
  - "How does identifier normalization work?"
  - "What are the different kinds of Rust comments?"
  - "What characters count as whitespace in Rust?"
---

# Quick Definition

Rust source files are UTF-8 encoded and undergo preprocessing (BOM removal, CRLF normalization, shebang removal) before tokenization. The language divides keywords into strict (always reserved), reserved (for future use), and weak (context-dependent). Identifiers follow Unicode UAX #31 with NFC normalization, and raw identifiers (`r#keyword`) allow using keywords as names. Comments follow C++ style with nested block comments supported, and doc comments (`///`, `//!`, `/** */`, `/*! */`) are syntactic sugar for `#[doc]` attributes.

# Core Definition

## Input Processing

Source files must be valid UTF-8. Before tokenization, three transformations occur in order: (1) a leading `U+FEFF` byte order mark is removed; (2) each CR+LF pair is replaced by a single LF (applied once, not repeatedly); (3) a shebang line (`#!...`) is removed if present. A shebang starts with `#!` and extends through the first LF or EOF, but is not recognized if `#!` is followed by `[` (ignoring whitespace and comments), to avoid ambiguity with inner attributes like `#![...]`. The shebang may appear immediately at the start or after an optional BOM.

## Keywords

Rust divides keywords into three categories:

**Strict keywords** cannot be used as names of items, variables, parameters, fields, variants, type parameters, lifetime parameters, loop labels, macros, attributes, macro placeholders, or crates. The full list includes: `_`, `as`, `async`, `await`, `break`, `const`, `continue`, `crate`, `dyn`, `else`, `enum`, `extern`, `false`, `fn`, `for`, `if`, `impl`, `in`, `let`, `loop`, `match`, `mod`, `move`, `mut`, `pub`, `ref`, `return`, `self`, `Self`, `static`, `struct`, `super`, `trait`, `true`, `type`, `unsafe`, `use`, `where`, `while`. The keywords `async`, `await`, and `dyn` were added as strict keywords in the 2018 edition.

**Reserved keywords** have the same restrictions as strict keywords but are not yet used -- they are reserved for forward compatibility: `abstract`, `become`, `box`, `do`, `final`, `gen`, `macro`, `override`, `priv`, `try`, `typeof`, `unsized`, `virtual`, `yield`. The keyword `try` was reserved in the 2018 edition; `gen` was reserved in the 2024 edition.

**Weak keywords** have special meaning only in certain contexts: `'static` (the static lifetime, cannot be used as a generic lifetime parameter or loop label), `macro_rules` (used to create macros), `raw` (used for raw borrow operators like `&raw const expr`), `safe` (meaningful in external blocks), and `union` (only a keyword in union declarations). In the 2015 edition, `dyn` was a weak keyword before being promoted to strict in 2018.

## Identifiers

Identifiers follow Unicode Standard Annex #31 (Unicode 17.0) with the profile: Start = `XID_Start` plus underscore (`U+005F`), Continue = `XID_Continue`. Zero-width non-joiner (`U+200C`) and zero-width joiner (`U+200D`) are not allowed. Identifiers are normalized using NFC (Normalization Form C) -- two identifiers are equal if their NFC forms are equal. Procedural and declarative macros receive normalized identifiers.

**Raw identifiers** (`r#keyword`) allow using strict or reserved keywords as identifiers, except for `_`, `crate`, `self`, `Self`, and `super` which are prohibited as raw identifiers. Identifiers are restricted to the ASCII subset of `XID_Start`/`XID_Continue` in certain contexts: `extern crate` declarations, external crate names in paths, module names loaded from the filesystem, `no_mangle` items, and item names in external blocks.

## Comments

Comments come in six forms: line comments (`//`), block comments (`/* ... */`), outer line doc comments (`///`), outer block doc comments (`/** ... */`), inner line doc comments (`//!`), and inner block doc comments (`/*! ... */`). Block comments support nesting. Non-doc comments are interpreted as whitespace. Doc comments are syntactic sugar for `doc` attributes: `/// Foo` becomes `#[doc=" Foo"]` and `//!` becomes `#![doc="..."]`. The character CR (`U+000D`) is not allowed in doc comments.

## Whitespace

Whitespace in Rust includes: horizontal tab, line feed, vertical tab, form feed, carriage return, space, next line (`U+0085`), left-to-right mark (`U+200E`), right-to-left mark (`U+200F`), line separator (`U+2028`), and paragraph separator (`U+2029`). Rust is a "free-form" language: whitespace only separates tokens and has no semantic significance. A program has identical meaning if each whitespace element is replaced with any other legal whitespace element.

# Prerequisites

- **rust-reference-overview** -- the grammar notation used in formal productions

# Key Properties

1. Source files must be valid UTF-8; invalid UTF-8 is a compilation error
2. BOM removal, CRLF normalization, and shebang removal happen before tokenization, in that order
3. CRLF normalization is applied once, not repeatedly -- "CR CR LF LF" becomes "CR LF" not "LF"
4. Shebang lines starting with `#!` are only recognized if not followed by `[` (after whitespace/comments)
5. Strict keywords cannot be used as names in any naming context
6. Reserved keywords exist solely for forward compatibility with future language versions
7. Weak keywords are context-sensitive: `union` is only a keyword in union declarations
8. Identifier equality is determined by NFC normalization -- visually identical but differently-composed Unicode identifiers are considered equal
9. Raw identifiers (`r#`) cannot use `_`, `crate`, `self`, `Self`, or `super`
10. Doc comments translate directly to `#[doc="..."]` attributes and must appear before an item that accepts attributes
11. Block comments can be nested to arbitrary depth, including nesting different kinds of block doc comments

# Construction / Recognition

## Recognizing Keyword Categories

1. If a keyword is in the strict list and you need to use it as a name, prefix with `r#`
2. If a keyword is reserved, it cannot be used even with `r#` (except via raw identifiers for strict keywords)
3. If a keyword is weak, check the context -- `union` is only reserved in union declarations; `safe` only in external blocks

## Writing Doc Comments

1. Use `///` for outer doc comments on the following item
2. Use `//!` for inner doc comments on the enclosing module
3. Use `/** */` and `/*! */` for block doc comment equivalents
4. Remember that `////` (four slashes) is a regular line comment, not a doc comment
5. Remember that `/*** */` (three asterisks) is a regular block comment, not a doc comment
6. `/***/` (empty two-asterisk block) is a regular block comment, not a doc block

# Context & Application

The lexical structure defines the lowest level of the language: how bytes become tokens. This chapter is the specification-level equivalent of what a lexer implements. Understanding keyword categories is important for macro authors (who may encounter keywords as tokens), for FFI work (where identifiers may need to match external names using `r#`), and for edition migration (where keywords may change categories between editions).

The NFC normalization rule for identifiers means that Rust source code with Unicode identifiers behaves consistently regardless of whether characters are composed or decomposed -- the compiler normalizes before comparison. This is relevant for internationalized codebases.

The `include!` macro applies the same three preprocessing steps (BOM removal, CRLF normalization, shebang removal in item context), while `include_str!` and `include_bytes!` do not apply any transformations.

# Examples

**Example 1** (Keywords): Using a raw identifier to use a strict keyword as a variable name:
```rust
let r#true = 42;  // OK: raw identifier
let r#fn = "hello";  // OK: raw identifier
// let true = 42;  // ERROR: strict keyword
```

**Example 2** (Comments): Different comment forms and their semantics:
```rust
//! Module-level inner doc comment (becomes #![doc="..."])

/// Outer doc comment on the following item (becomes #[doc="..."])
pub mod outer_module {
    //  Regular line comment (whitespace)
    /// Outer line doc (exactly 3 slashes)
    //// Not a doc comment (4 slashes = regular comment)
    /**  Outer block doc (exactly 2 asterisks) */
    /*** Not a doc comment (3 asterisks = regular comment) */
    pub mod inner {}
}
```

**Example 3** (Weak Keywords): `union` is only a keyword in union declarations:
```rust
let union = 42;  // OK: union is a weak keyword
fn union() {}    // OK: can name a function "union"

union MyUnion {  // Here "union" acts as a keyword
    i: i32,
    f: f32,
}
```

**Example 4** (Identifiers): NFC normalization makes these equivalent:
```rust
// These would be the same identifier if both used:
// U+00E9 (LATIN SMALL LETTER E WITH ACUTE) -- precomposed
// U+0065 U+0301 (e + COMBINING ACUTE ACCENT) -- decomposed
// Both normalize to the same NFC form
```

# Relationships

## Builds Upon
- **rust-reference-overview** -- grammar notation used throughout this chapter

## Enables
- **lexical-structure-tokens-and-literals** -- tokens build on the keyword and identifier definitions
- **reference-macros-by-example** -- macro matchers use keywords and identifiers as tokens

## Related
- **lexical-structure-tokens-and-literals** -- the companion card covering tokens, literals, and punctuation

## Contrasts With
(none)

# Common Errors

- **Error**: Attempting to use `r#` with `_`, `self`, `Self`, `crate`, or `super`.
  **Correction**: These are reserved raw identifiers and cannot be used even with the `r#` prefix. They have special meaning in the language that cannot be overridden.

- **Error**: Writing `////` (four slashes) expecting an outer doc comment.
  **Correction**: Only exactly three slashes (`///`) produce an outer doc comment. Four or more slashes produce a regular (non-doc) line comment.

# Common Confusions

- **Confusion**: Thinking weak keywords are always reserved and cannot be used as names.
  **Clarification**: Weak keywords are only keywords in specific syntactic positions. `union` can freely be used as a variable name, function name, or method name -- it is only treated as a keyword when declaring a union type.

- **Confusion**: Thinking CRLF normalization converts all CR characters to LF.
  **Clarification**: Only CR immediately followed by LF pairs are replaced. Standalone CR characters are left in place and treated as whitespace. Also, the normalization is applied once, so "CR CR LF" becomes "CR LF", not "LF".

- **Confusion**: Thinking doc comments are a special syntactic form separate from attributes.
  **Clarification**: Doc comments are syntactic sugar for `#[doc="..."]` attributes. They must appear where an attribute would be valid (before an item for outer doc comments, inside a module for inner doc comments).

# Source Reference

Chapter 2 (Lexical Structure): Input format -- UTF-8 encoding, BOM removal, CRLF normalization, shebang removal, tokenization. Keywords -- strict (39 keywords), reserved (14 keywords), weak (5 keywords), edition-specific changes. Identifiers -- UAX #31 profile, NFC normalization, raw identifiers, ASCII restrictions. Comments -- six comment forms, doc comment semantics, nesting rules. Whitespace -- 10 whitespace characters, free-form language semantics.

# Verification Notes

- Definition source: Direct synthesis from Ch. 2, sections on input format (72 lines), shebang (37 lines), keywords (160 lines), identifiers (90 lines), comments (147 lines), whitespace (37 lines)
- Key Properties: All items are directly stated in the source text or grammar productions
- Confidence rationale: HIGH -- the source provides explicit formal definitions with grammar productions
- Uncertainties: None significant; these are stable language specifications
- Cross-reference status: All slugs reference cards in this Reference extraction set
