---
concept: Internal Rules
slug: internal-rules
category: macro-patterns
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "03-patterns"
chapter_number: 3
pdf_page: null
section: "Internal rules"
extraction_confidence: high
aliases:
  - "@ rules"
  - "at-prefixed rules"
  - "macro internal dispatch"
  - "macro helper rules"
prerequisites:
  - macro-rules
  - macro-matcher
extends:
  - macro-rules
related:
  - push-down-accumulation
  - tt-muncher
  - callback-pattern
  - macro-hygiene
contrasts_with: []
answers_questions:
  - "How do you avoid polluting the global macro namespace with helper macros?"
  - "Why do macros use @ as a prefix in their rules?"
  - "How do you make internal helper macros private to an exported macro?"
  - "How do you combine utility macros into a single exported macro?"
---

# Quick Definition

Internal rules are `@`-prefixed rules within a `macro_rules!` definition that serve as private helper dispatches. Instead of defining separate public helper macros (like `as_expr!`), you embed them as rules of the main macro prefixed with `@`, avoiding namespace pollution and dependency issues when exporting macros.

# Core Definition

"Because macros do not interact with regular item privacy or lookup, any public macro *must* bring with it all other macros that it depends on. This can lead to pollution of the global macro namespace, or even conflicts with macros from other crates. It may also cause confusion to users who attempt to *selectively* import macros: they must transitively import *all* macros, including ones that may not be publicly documented."

"A good solution is to conceal what would otherwise be other public macros *inside* the macro being exported."

"The reason for using `@` is that, as of Rust 1.2, the `@` token is *not* used in prefix position; as such, it cannot conflict with anything. Other symbols or unique prefixes may be used as desired, but use of `@` has started to become widespread, so using it may aid readers in understanding your code."

# Prerequisites

- **macro_rules!** -- internal rules are defined within a `macro_rules!` block
- **Macro matchers** -- internal rules are distinguished by their `@`-prefixed matcher patterns

# Key Properties

1. Internal rules use `@` (or another unique prefix) as the first token in their matcher pattern
2. `@` was chosen because it is not used in prefix position in Rust, so it cannot conflict with valid input
3. Internal rules should come *before* "bare" rules to avoid incorrect parsing attempts
4. Multiple utility macros can be consolidated into a single exported macro using different `@` prefixes
5. Internal rules are not truly private -- they can still be called externally -- but the `@` convention signals they are not part of the public API

# Construction / Recognition

## To Construct:
1. Identify helper macros that the main macro depends on (e.g., `as_expr!`, `as_item!`, `count_tts!`)
2. Move each helper's rules into the main macro, prefixed with `@helper_name`: `(@as_expr $e:expr) => {$e};`
3. Update all internal invocations to call the main macro with the `@` prefix: `my_macro!(@as_expr $tokens)`
4. Place `@`-prefixed rules before any "bare" catch-all rules in the macro definition

## To Recognise:
1. Macro rules whose patterns begin with `@` followed by an identifier
2. Recursive macro calls that pass `@something` as the first token
3. A single macro that contains multiple logically distinct sections distinguished by `@` prefixes

# Context & Application

Internal rules are ubiquitous in complex macros. The source notes that if exporting at least one internal macro is unavoidable (e.g., many macros share a common set of utility rules), you can combine all internal macros into a single "uber-macro" with different `@` prefixes. This is visible in the Ook! implementation in Chapter 5, which uses `@start`, `@e` (execute), `@x` (extract), and `@s` (skip) as internal rule sections.

The ordering requirement is important: "internal rules will often come *before* any 'bare' rules, to avoid issues with `macro_rules!` incorrectly attempting to parse an internal invocation as something it cannot possibly be, such as an expression."

# Examples

**Example 1** (Ch. 3, "Internal rules"): Embedding `as_expr!` as an internal rule:

```rust
#[macro_export]
macro_rules! foo {
    (@as_expr $e:expr) => {$e};

    ($($tts:tt)*) => {
        foo!(@as_expr $($tts)*)
    };
}

fn main() {
    assert_eq!(foo!(42), 42);
}
```

**Example 2** (Ch. 3, "Internal rules"): Combining multiple utility macros into one:

```rust
macro_rules! crate_name_util {
    (@as_expr $e:expr) => {$e};
    (@as_item $i:item) => {$i};
    (@count_tts) => {0usize};
    // ...
}
```

**Example 3** (Ch. 5, "Ook!"): The Ook! macro uses internal rules for distinct processing phases:

```rust
macro_rules! Ook {
    (@start $($Ooks:tt)*) => { /* set up execution environment */ };
    (@e $syms:tt; ($input)) => { /* execute/parse opcodes */ };
    (@x $syms:tt; $depth:tt; $buf:tt; $tail:tt) => { /* extract loop body */ };
    (@s $syms:tt; $depth:tt; $tail:tt) => { /* skip past loop */ };
    ($($Ooks:tt)*) => { Ook!(@start $($Ooks)*) };
}
```

# Relationships

## Builds Upon
- **macro-rules** -- internal rules are a structural convention within `macro_rules!` definitions

## Enables
- **push-down-accumulation** -- accumulation macros use `@accum` and `@as_expr` internal rules
- **tt-muncher** -- complex TT munchers organise their phases using internal rules

## Related
- **callback-pattern** -- callbacks are an alternative for inter-macro composition; internal rules handle intra-macro composition
- **macro-hygiene** -- internal rules help manage the namespace hygiene that `macro_rules!` lacks

## Contrasts With
- None explicitly -- the alternative is separate public helper macros, which pollute the namespace

# Common Errors

- **Error**: Placing internal `@` rules after a catch-all `$($tts:tt)*` rule.
  **Correction**: Put `@`-prefixed rules first. A `$($tts:tt)*` pattern matches everything, including tokens starting with `@`, so the internal rules would never be reached.

- **Error**: Using a prefix that could conflict with valid input tokens.
  **Correction**: Use `@` as the prefix, since it is not used in prefix position in Rust syntax. Alternatively, use a distinctive identifier like `__internal` that users would not accidentally provide.

# Common Confusions

- **Confusion**: Thinking `@`-prefixed rules are actually private or enforced by the compiler.
  **Clarification**: There is no compiler enforcement. External code can call `my_macro!(@as_expr 42)` and it will work. The `@` prefix is a convention that signals "internal use only" -- it relies on user discipline, not access control.

- **Confusion**: Thinking the `@` token has special meaning in macros.
  **Clarification**: `@` has no special meaning in macro matchers. It is just a regular token that happens to not conflict with any prefix usage in Rust syntax. Its current language purpose is only as an infix operator for binding names to patterns (e.g., `name @ pattern`).

# Source Reference

Chapter 3: Patterns, "Internal rules" section. The pattern is motivated by namespace pollution concerns, demonstrated with the `foo!` macro embedding `as_expr!`, and extended with the uber-macro consolidation approach. Also extensively used in Chapter 5's Ook! implementation.

# Verification Notes

- Definition source: Direct quotation from "Internal rules" section, paragraphs 1-3
- Key Properties: All from explicit statements in the source, including the historical note about `@`
- Confidence rationale: HIGH -- the source clearly defines the pattern, its motivation, and its conventions
- Uncertainties: The note about `@` not being used in prefix position was true "as of Rust 1.2" -- this remains true in current Rust
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
