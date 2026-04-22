---
concept: Metavariable
slug: metavariable
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
  - "capture"
  - "macro capture"
  - "macro variable"
  - "$name:kind"
prerequisites:
  - macro-rules
  - token-tree
extends: []
related:
  - fragment-specifier
  - macro-matcher
  - macro-expansion
contrasts_with: []
answers_questions:
  - "What are captures/metavariables in Rust macros?"
  - "How do you capture input in a macro_rules! pattern?"
  - "How are captured values substituted into macro expansions?"
  - "Why can't captured expressions be destructured?"
---

# Quick Definition

A metavariable (or capture) in `macro_rules!` is written as `$name:kind` in a pattern, where `$name` is the variable name and `kind` is a fragment specifier (like `expr`, `ident`, `tt`). It matches input according to the grammar category and binds the result for substitution in the expansion via `$name`.

# Core Definition

Captures allow input to be matched based on a general grammar category, with the result captured to a variable which can then be substituted into the output. They are written as a dollar (`$`) followed by an identifier, a colon (`:`), and the kind of capture (the fragment specifier).

For example:

```rust
macro_rules! one_expression {
    ($e:expr) => { ... };
}
```

Captures leverage the Rust compiler's parser, ensuring that they are always "correct." An `expr` capture will always capture a complete, valid expression for the version of Rust being compiled.

A capture `$name:kind` can be substituted into the expansion by writing `$name`. Much like macro expansion, captures are substituted as complete AST nodes. This means that no matter what sequence of tokens is captured by `$e`, it will be interpreted as a single, complete expression.

Critically, substitution is not token-based despite looking like it. Once tokens are captured by any fragment specifier other than `tt` or `ident`, the result becomes an opaque AST node. It cannot be examined, destructured, or matched against by subsequent macros.

# Prerequisites

- **macro-rules** -- Metavariables are part of `macro_rules!` pattern syntax
- **token-tree** -- Understanding token trees helps explain why captured AST nodes become opaque

# Key Properties

1. **Syntax**: `$name:kind` in the pattern, `$name` in the expansion.
2. **Parser-backed**: Captures use the Rust compiler's parser, guaranteeing correctness.
3. **AST node substitution**: Captured values are substituted as complete AST nodes, not as token sequences.
4. **Opaque after capture**: Once captured (except by `tt` or `ident`), the value becomes an opaque AST node that cannot be destructured or re-matched.
5. **Multiple captures**: A single pattern can contain multiple captures, e.g., `($a:expr, $b:expr, $c:expr)`.
6. **No backtracking**: Once the parser begins consuming tokens for a capture, it cannot stop or backtrack.

# Construction / Recognition

## Basic capture and substitution

```rust
macro_rules! times_five {
    ($e:expr) => { 5 * $e };
}
```

`$e:expr` captures any valid expression, and `$e` in the expansion substitutes it as a complete AST node.

## Multiple captures

```rust
macro_rules! multiply_add {
    ($a:expr, $b:expr, $c:expr) => { $a * ($b + $c) };
}
```

## Mixing literal tokens and captures

Patterns can combine literal tokens with captures:

```rust
macro_rules! do_thing {
    (let $name:ident = $value:expr) => { let $name = $value + 1 };
}
```

# Context & Application

Metavariables are the primary mechanism for making macros flexible. They allow macros to accept varying input and produce parameterized output. The fragment specifier determines what kind of Rust syntax the capture will match, which has important implications:

- Using `expr` captures complete expressions but makes the result opaque
- Using `tt` preserves the ability to destructure but doesn't validate syntax
- Using `ident` captures a single identifier and preserves re-matchability

The opaque-AST-node property is one of the most surprising aspects of the macro system. It means that a macro which captures an expression and passes it to another macro will produce different results than directly passing the same tokens to the second macro.

# Examples

**Capture opacity demonstration** (from "Captures and Expansion Redux" section):

```rust
macro_rules! capture_expr_then_stringify {
    ($e:expr) => {
        stringify!($e)
    };
}

fn main() {
    println!("{:?}", stringify!(dummy(2 * (1 + (3)))));
    println!("{:?}", capture_expr_then_stringify!(dummy(2 * (1 + (3)))));
}
```

Output:
```text
"dummy ( 2 * ( 1 + ( 3 ) ) )"
"dummy(2 * (1 + (3)))"
```

The first stringifies token trees (with spaces around each token). The second stringifies an AST expression node (preserving original grouping).

**Captured values cannot be re-matched** (from "Captures and Expansion Redux" section):

```rust
macro_rules! capture_then_match_tokens {
    ($e:expr) => { match_tokens!($e) };
}

macro_rules! match_tokens {
    ($a:tt + $b:tt) => { "got an addition" };
    (($i:ident)) => { "got an identifier" };
    ($($other:tt)*) => { "got something else" };
}

fn main() {
    println!("{}", match_tokens!(3 + 6));           // "got an addition"
    println!("{}", capture_then_match_tokens!(3 + 6)); // "got something else"
}
```

Direct input `3 + 6` matches the addition pattern, but when captured as `$e:expr` first, it becomes an opaque AST node that only matches the catch-all `$($other:tt)*` pattern.

# Relationships

## Builds Upon

- **macro-rules** -- Metavariables are part of macro rule patterns
- **token-tree** -- Captures consume token trees from the input

## Enables

- **macro-expansion** -- Captured values are substituted into expansions
- **macro-repetition** -- Captures can appear within repetition patterns

## Related

- **fragment-specifier** -- The `kind` part that determines what grammar category is matched
- **macro-matcher** -- The overall pattern that contains captures

# Common Errors

1. **Expecting token-level substitution**: Captured values are AST nodes, not token sequences. Passing a captured `$e:expr` to another macro produces different results than passing the same tokens directly.
2. **Trying to destructure a captured value**: Once captured by anything other than `tt` or `ident`, a value is opaque and cannot be matched against by subsequent macros.
3. **No-backtracking surprise**: Writing `($e:expr)` as the first rule will eagerly consume tokens and never fall through to more specific rules.

# Common Confusions

- **Confusion**: Thinking `$e` in the expansion substitutes the original tokens.
  **Clarification**: `$e` substitutes a complete AST node. Even `stringify!($e)` produces different output than `stringify!` applied directly to the same tokens, because one stringifies an AST node while the other stringifies token trees.
- **Confusion**: Believing you can match against a captured expression in a downstream macro.
  **Clarification**: Once captured as `expr`, `ty`, `pat`, etc., the value is "un-destructible." The only way to preserve the ability to match contents is to use `tt` or `ident` captures.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "Captures" and "Captures and Expansion Redux."

# Verification Notes

- Capture syntax and semantics: directly from "Captures" section
- Opacity behavior and stringify example: directly from "Captures and Expansion Redux" section with exact code examples and output
- The "un-destructible" characterization is a direct quote from the source
- Confidence: HIGH -- the source provides explicit definitions and detailed demonstrations
