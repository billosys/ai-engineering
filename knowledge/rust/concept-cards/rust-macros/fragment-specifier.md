---
concept: Fragment Specifier
slug: fragment-specifier
category: macro-system
subcategory: null
tier: foundational
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Captures"
extraction_confidence: high
aliases:
  - "fragment spec"
  - "capture kind"
  - "matcher kind"
prerequisites:
  - metavariable
extends: []
related:
  - macro-matcher
  - macro-rules
  - token-tree
contrasts_with: []
answers_questions:
  - "What fragment specifiers are available in macro_rules!?"
  - "What does each fragment specifier match?"
  - "What tokens can follow each fragment specifier?"
  - "Which fragment specifiers produce opaque AST nodes?"
---

# Quick Definition

Fragment specifiers are the `kind` part of a `$name:kind` capture in `macro_rules!`. They determine what grammar category the capture will match. Available specifiers include `expr`, `ty`, `ident`, `tt`, `pat`, `item`, `block`, `stmt`, `path`, and `meta`. Each has specific follow-set restrictions on what tokens may appear after it.

# Core Definition

When writing captures in macro patterns, the fragment specifier tells the compiler's parser what kind of syntactic construct to expect. The complete list of fragment specifiers (as of the source's writing) is:

| Specifier | Matches |
|-----------|---------|
| `item` | An item (function, struct, module, etc.) |
| `block` | A block (statements and/or expression, surrounded by braces) |
| `stmt` | A statement |
| `pat` | A pattern |
| `expr` | An expression |
| `ty` | A type |
| `ident` | An identifier |
| `path` | A path (e.g., `foo`, `::std::mem::replace`, `transmute::<_, int>`) |
| `meta` | A meta item (things inside `#[...]` and `#![...]` attributes) |
| `tt` | A single token tree |

Each specifier leverages the Rust compiler's parser, ensuring that captures are always syntactically correct for the version of Rust being compiled.

# Prerequisites

- **metavariable** -- Fragment specifiers are the kind component of metavariable captures

# Key Properties

1. **Parser-backed**: Each specifier uses the actual Rust parser, guaranteeing syntactic correctness.
2. **Follow-set restrictions**: Each specifier has a restricted set of tokens that may follow it, to guard against future syntax changes.
3. **Opacity gradient**: `tt` and `ident` captures preserve the ability to destructure; all others produce opaque AST nodes.
4. **`tt` is most flexible**: The `tt` specifier matches any single token tree and has no follow-set restrictions.
5. **`ident` matches keywords**: The `ident` specifier can match `self` (which is both a keyword and an identifier), leading to edge cases.

# Construction / Recognition

## Follow-set restrictions (as of Rust 1.3)

| Specifier | Allowed followers |
|-----------|-------------------|
| `item` | anything |
| `block` | anything |
| `stmt` | `=>` `,` `;` |
| `pat` | `=>` `,` `=` `if` `in` |
| `expr` | `=>` `,` `;` |
| `ty` | `,` `=>` `:` `=` `>` `;` `as` |
| `ident` | anything |
| `path` | `,` `=>` `:` `=` `>` `;` `as` |
| `meta` | anything |
| `tt` | anything |

Additionally, `macro_rules!` generally forbids a repetition from being followed by another repetition, even if the contents do not conflict.

## Using different specifiers

```rust
macro_rules! example {
    ($e:expr) => { ... };        // matches any expression
    ($i:ident) => { ... };       // matches any identifier
    ($t:tt) => { ... };          // matches any single token tree
    ($p:pat => $e:expr) => { ... }; // pattern followed by expression
}
```

# Context & Application

Choosing the right fragment specifier is one of the most important decisions when writing macros. The choice involves a trade-off:

- **Specific specifiers** (like `expr`, `ty`, `pat`) provide strong validation but produce opaque AST nodes that cannot be further processed by other macros.
- **Generic specifiers** (like `tt`) provide maximum flexibility and preserve destructurability but perform no validation.
- **`ident`** is a special case: it matches identifiers and certain keywords (like `self`), and the captured value can be re-matched.

The follow-set restrictions are a forward-compatibility measure. They prevent macros from relying on parsing behavior that might change if Rust's grammar evolves. For example, `$e:expr` can only be followed by `=>`, `,`, or `;` -- this ensures that new expression syntax won't break existing macros.

The `self` keyword deserves special mention: it matches as an `ident` specifier but retains its keyword status in some contexts, leading to confusing behavior where `self` is simultaneously a keyword and an identifier.

# Examples

**Basic specifier usage** (from "Captures" section):

```rust
macro_rules! one_expression {
    ($e:expr) => { ... };
}
```

Captures a complete, valid expression.

**Multiple specifiers** (from "Captures" section):

```rust
macro_rules! multiply_add {
    ($a:expr, $b:expr, $c:expr) => { $a * ($b + $c) };
}
```

**The `self` edge case** (from "Non-Identifier Identifiers" section):

```rust
macro_rules! what_is {
    (self) => { "the keyword `self`" };
    ($i:ident) => { concat!("the identifier `", stringify!($i), "`") };
}

fn main() {
    println!("{}", what_is!(self)); // "the keyword `self`"
}
```

`self` matches as a literal keyword in the first rule. But it also matches the `$i:ident` capture, and when captured, retains its keyword nature -- leading to surprising behavior when used in positions expecting a "true" identifier.

**`_` is NOT an identifier** (from "Non-Identifier Identifiers" section):

```rust
macro_rules! example {
    ($i:ident) => { ... };
}
// example!(_);  // ERROR: expected ident, found _
```

Despite looking like an identifier, `_` is a keyword that does not match the `ident` specifier.

# Relationships

## Builds Upon

- **metavariable** -- Fragment specifiers are the kind component of captures

## Related

- **macro-matcher** -- Fragment specifiers define what each capture in a matcher accepts
- **token-tree** -- The `tt` specifier captures a single token tree
- **macro-rules** -- Fragment specifiers are part of the `macro_rules!` system

# Common Errors

1. **Violating follow-set restrictions**: Placing `$e:expr $other:tt` fails because `tt` is not in the follow set for `expr`. Use a separator like `$e:expr, $other:tt`.
2. **Using `ident` to capture `_`**: The underscore `_` is a keyword, not an identifier, and will not match `$i:ident`.
3. **Expecting `expr` captures to be re-matchable**: Captured expressions become opaque AST nodes. Use `tt` if you need to pass the value to another macro for pattern matching.

# Common Confusions

- **Confusion**: Thinking all specifiers behave the same way in terms of opacity.
  **Clarification**: Only `tt` and `ident` captures preserve the ability to destructure the captured content. All other specifiers (`expr`, `ty`, `pat`, `stmt`, `block`, `item`, `path`, `meta`) produce opaque AST nodes.
- **Confusion**: Believing `self` and `_` behave identically with respect to `ident`.
  **Clarification**: `self` matches the `ident` specifier (while retaining keyword status); `_` does not match `ident` at all. The workaround for accepting both is to use the `tt` specifier.
- **Confusion**: Thinking follow-set restrictions are arbitrary limitations.
  **Clarification**: They protect forward compatibility. If Rust adds new expression syntax, existing macros with `$e:expr` won't break because they can't rely on specific tokens following the expression.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "Captures," "Captures and Expansion Redux," and "Non-Identifier Identifiers."

# Verification Notes

- Specifier list: directly enumerated in the "Captures" section
- Follow-set table: directly from the source, stated as being "as of Rust 1.3"
- The `self`/`_` edge cases: directly from "Non-Identifier Identifiers" section with exact code examples
- Opacity behavior: from "Captures and Expansion Redux" section
- Confidence: HIGH -- explicit enumeration and detailed examples in the source
