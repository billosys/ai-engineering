---
concept: macro_rules!
slug: macro-rules
category: macro-system
subcategory: null
tier: foundational
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "macro_rules!"
extraction_confidence: high
aliases:
  - "macro_rules"
  - "declarative macros"
  - "macros by example"
  - "MBE"
prerequisites: []
extends: []
related:
  - syntax-extension
  - token-tree
  - macro-matcher
  - macro-expansion
contrasts_with:
  - procedural-macros
answers_questions:
  - "What is macro_rules! in Rust?"
  - "How do you define a declarative macro in Rust?"
  - "What is the basic syntax for macro_rules!?"
  - "How does macro rule matching work?"
---

# Quick Definition

`macro_rules!` is Rust's declarative macro system that defines macros using pattern-matching rules. Each rule has a pattern (matcher) and an expansion (transcriber), and invocations are matched top-to-bottom against the rules.

# Core Definition

`macro_rules!` is itself a syntax extension (technically not part of the Rust syntax) that registers a macro with the compiler. It uses the form:

```rust
macro_rules! $name {
    $rule0 ;
    $rule1 ;
    // ...
    $ruleN ;
}
```

There must be at least one rule, and the semicolon after the last rule can be omitted. Each rule looks like:

```rust
($pattern) => {$expansion}
```

The parens around the pattern and braces around the expansion are conventional but can be any kind of group (`()`, `[]`, `{}`). When a macro is invoked, the interpreter goes through the rules one by one in lexical order, trying to match the input token tree against each rule's pattern. If a pattern matches the entirety of the input, the invocation is replaced by that rule's expansion. If all rules fail, compilation aborts with an error.

The `macro_rules!` invocation itself expands to nothing visible in the AST -- it manipulates compiler-internal structures to register the macro.

# Prerequisites

This is a foundational concept with no prerequisites within this source, though understanding token trees and the Rust compilation pipeline provides important context.

# Key Properties

1. **Pattern-matching rules**: Each rule is a `(pattern) => {expansion}` pair.
2. **Top-to-bottom matching**: Rules are tried in lexical order; first match wins.
3. **Complete match required**: A pattern must match the entirety of the input to be considered a match.
4. **Grouping-token agnostic**: The specific grouping tokens used at invocation (`()`, `[]`, `{}`) are not matched -- only the contents of the input token tree are considered.
5. **At least one rule required**: A `macro_rules!` definition must contain at least one rule.
6. **Not part of Rust syntax**: `macro_rules!` is itself a syntax extension, not a language primitive.
7. **Recursion limit**: The compiler imposes an upper limit (default 32) on recursive macro expansion passes, configurable with `#![recursion_limit="..."]`.

# Construction / Recognition

## Defining a simple macro

```rust
macro_rules! four {
    () => { 1 + 3 };
}
```

This matches only empty input (`four!()`, `four![]`, or `four!{}`).

## Multiple rules with literal matching

```rust
macro_rules! gibberish {
    (4 fn ['spang "whammo"] @_@) => { ... };
}
```

Patterns can contain literal token trees that must be matched exactly.

## Multiple rules with captures

```rust
macro_rules! multiply_add {
    ($a:expr, $b:expr, $c:expr) => { $a * ($b + $c) };
}
```

Captures use `$name:kind` syntax to match grammar categories and bind results to variables.

# Context & Application

`macro_rules!` is the primary way to define macros in stable Rust. It powers ubiquitous macros like `vec![]`, `println!()`, and `assert_eq!()`. Declarative macros operate at the AST level (not the token level like C preprocessor macros), which means they produce structurally valid code and respect Rust's type system. They can appear in place of patterns, statements, expressions, items, and `impl` items.

Unlike C/C++ macros which operate during tokenisation, Rust macros are processed after the AST has been constructed, which provides stronger safety guarantees.

# Examples

**The simplest macro** (from "macro_rules!" section):

```rust
macro_rules! four {
    () => { 1 + 3 };
}
```

Invoked as `four!()`, `four![]`, or `four!{}` -- all produce `1 + 3`.

**A macro with captures** (from "Captures" section):

```rust
macro_rules! times_five {
    ($e:expr) => { 5 * $e };
}
```

**A macro with repetitions** (from "Repetitions" section):

```rust
macro_rules! vec_strs {
    ( $( $element:expr ),* ) => {
        {
            let mut v = Vec::new();
            $( v.push(format!("{}", $element)); )*
            v
        }
    };
}
```

# Relationships

## Builds Upon

- **token-tree** -- Macro input is always a single non-leaf token tree
- **syntax-extension** -- `macro_rules!` is a specific kind of syntax extension

## Enables

- **macro-matcher** -- The pattern-matching side of each rule
- **metavariable** -- Captures within matcher patterns
- **macro-repetition** -- Repetition patterns in matchers and expansions
- **macro-expansion** -- The expansion/transcription side of each rule

## Related

- **macro-hygiene** -- How naming collisions are prevented in expansions
- **macro-scoping** -- How macros are scoped and made visible
- **macro-debugging** -- Tools for debugging macro definitions

# Common Errors

1. **Writing rules in wrong order**: Since rules are matched top-to-bottom and capture parsing cannot backtrack, less-specific rules before more-specific ones can cause unreachable rules or parse errors.
2. **Expecting token-level substitution**: Macro substitution operates on AST nodes, not tokens. Captured expressions become opaque AST nodes that cannot be destructured by subsequent macros.
3. **Exceeding recursion limit**: Deeply recursive macros may hit the default limit of 32 expansion passes.

# Common Confusions

- **Confusion**: Thinking `macro_rules!` works like C preprocessor macros (token substitution).
  **Clarification**: Rust macros operate at the AST level. Expansion produces complete AST nodes, not token sequences. This means `2 * four!()` where `four!` expands to `1 + 3` evaluates as `2 * (1 + 3) = 8`, not `2 * 1 + 3 = 5`.
- **Confusion**: Believing the delimiter used at invocation matters for matching.
  **Clarification**: `four!()`, `four![]`, and `four!{}` all match the same empty pattern. Only the contents of the token tree are matched.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," sections "macro_rules!", "Matching," "Captures," and "Repetitions."

# Verification Notes

- Definition and syntax: directly from the "macro_rules!" section
- Matching behavior: directly from the "Matching" section
- All code examples taken from the source
- Recursion limit details from the "Expansion" section
- Confidence: HIGH -- the source provides explicit, detailed coverage of this concept
