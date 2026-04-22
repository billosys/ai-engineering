---
# === CORE IDENTIFICATION ===
concept: Macro Invocation Design
slug: macro-invocation-design

# === CLASSIFICATION ===
category: macro-design
subcategory: syntax-design
tier: intermediate

# === PROVENANCE ===
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "02-practical-introduction"
chapter_number: 2
pdf_page: null
section: "Construction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "macro syntax design"
  - "macro call design"
  - "designing macro invocations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro-rules
  - fragment-specifier
  - macro-matcher
extends: []
related:
  - incremental-macro-development
  - macro-substitution
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decide what the call syntax for a new macro should look like?"
  - "What is the recommended first step when building a new macro?"
  - "How do I validate that a macro syntax is parseable before writing the expansion?"
  - "What do I do when my desired syntax causes parsing ambiguity?"
---

# Quick Definition

Macro invocation design is the process of deciding what the call site of a macro should look like before writing the expansion. Start by writing the ideal invocation, then derive the `macro_rules!` pattern from it, and verify the syntax is parseable before implementing the expansion body.

# Core Definition

> "Usually, when working on a new macro, the first thing I do is decide what the macro invocation should look like." -- Daniel Keep et al., "Macros, A Practical Introduction"

> "From that, we can take a stab at how the macro should be defined, even if we aren't sure of the actual expansion. This is useful because if you can't figure out how to parse the input syntax, then *maybe* you need to change it." -- Daniel Keep et al., "Macros, A Practical Introduction"

The design process is: (1) write the desired invocation syntax, (2) translate it into a `macro_rules!` matcher pattern, (3) test that the pattern parses correctly, and (4) iterate on the syntax if the macro system cannot handle it.

# Prerequisites

- Understanding of `macro_rules!` basic syntax (matchers, captures)
- Knowledge of fragment specifiers (`expr`, `ty`, `ident`, etc.)
- Awareness that `macro_rules!` matching has limitations around ambiguity

# Key Properties

1. **Syntax-first approach**: Design starts with the desired call syntax, not the expansion. The invocation is the user-facing API of the macro.
2. **Parsability check**: Translate the desired syntax into a matcher pattern early to verify the macro system can parse it. Use `/* ... */` as a placeholder expansion.
3. **Ambiguity constraints**: The macro parser cannot always disambiguate between a repetition separator and following literal tokens. For example, a comma separator in `$($inits:expr),+` followed by a literal comma causes "local ambiguity" errors.
4. **Iterative syntax refinement**: When the desired syntax causes parse errors, modify the syntax to avoid ambiguity. The book changes `0, 1, ..., expr` to `0, 1 ... expr` by removing commas around `...`.
5. **Literal tokens as structure**: Use literal tokens (like `[`, `]`, `=`, `...`) freely in matcher patterns to give structure to the invocation. These do not need to be valid Rust syntax -- they just need to be valid tokens.

# Construction / Recognition

**Step 1 -- Write desired invocation:**

```rust,ignore
let fib = recurrence![a[n] = 0, 1, ..., a[n-1] + a[n-2]];
```

**Step 2 -- Derive matcher pattern:**

```rust,ignore
macro_rules! recurrence {
    ( a[n] = $($inits:expr),+ , ... , $recur:expr ) => { /* ... */ };
}
```

**Step 3 -- Discover parsing problem (ambiguity around commas):**

```text
error: local ambiguity: multiple parsing options: built-in NTs expr ('inits') or 1 other options.
```

**Step 4 -- Refine syntax to resolve ambiguity:**

```rust,ignore
macro_rules! recurrence {
    ( a[n]: $sty:ty = $($inits:expr),+ ... $recur:expr ) => { /* ... */ };
}
// Invocation becomes:
let fib = recurrence![a[n]: u64 = 0, 1 ... a[n-1] + a[n-2]];
```

# Context & Application

This design methodology applies whenever you are creating a new `macro_rules!` macro, especially DSL-style macros with custom syntax. The "syntax-first" approach prevents wasted effort: if you cannot express the desired syntax as a parseable matcher, you will discover this before writing hundreds of lines of expansion code. It also ensures the macro has a clean, intuitive user-facing API.

# Examples

The chapter designs a `recurrence!` macro for defining mathematical recurrence relations. The initial syntax `a[n] = 0, 1, ..., a[n-1] + a[n-2]` is refined through several iterations:

1. Adding a type annotation: `a[n]: $sty:ty = ...`
2. Removing ambiguous commas around `...`
3. Generalizing hardcoded identifiers `a` and `n` to captures `$seq:ident` and `$ind:ident` to resolve hygiene issues

The final invocation syntax:

```rust,ignore
let fib = recurrence![a[n]: u64 = 0, 1 ... a[n-1] + a[n-2]];
```

# Relationships

- **macro-rules**: The foundation that this design process targets.
- **fragment-specifier**: Choosing the right specifiers (`expr`, `ty`, `ident`) is a key decision during invocation design.
- **macro-matcher**: The matcher pattern is derived directly from the desired invocation syntax.
- **incremental-macro-development**: Invocation design is the first step of the broader incremental approach.

# Common Errors

1. **Skipping the parsability check**: Writing a large expansion body before verifying the syntax parses, then having to redesign everything.
2. **Ambiguous separators**: Using commas both as repetition separators and literal delimiters (e.g., `$($e:expr),+ , ...`) creates "local ambiguity" errors.
3. **Missing captures for varying parts**: Not noticing that the expansion needs something (like a type) that is not in the invocation syntax. Check the expansion for anything that should vary per invocation.

# Common Confusions

- **Macro syntax vs. Rust syntax**: The tokens inside a macro invocation do not need to be valid Rust syntax. `a[n]: u64 = 0, 1 ... expr` is not valid Rust, but it is a perfectly valid macro input.
- **Parsing limitations are not bugs**: The "local ambiguity" error is a fundamental limitation of how `macro_rules!` works -- it cannot speculatively try to parse an expression and backtrack. The workaround is to design unambiguous syntax.

# Source Reference

The Little Book of Rust Macros, Chapter 2 "Macros, A Practical Introduction", "Construction" section. The design process is demonstrated through lines 75-665 of the source text.

# Verification Notes

Confidence: high. The design methodology and examples are directly from the source material. The syntax refinement steps are explicitly narrated by the author.
