---
concept: Incremental TT Muncher
slug: tt-muncher
category: macro-patterns
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "03-patterns"
chapter_number: 3
pdf_page: null
section: "Incremental TT munchers"
extraction_confidence: high
aliases:
  - "TT muncher"
  - "token tree muncher"
  - "incremental token tree muncher"
  - "recursive macro parsing"
prerequisites:
  - macro-rules
  - token-tree
  - macro-repetition
  - macro-matcher
extends:
  - macro-rules
related:
  - push-down-accumulation
  - internal-rules
  - callback-pattern
  - macro-parsing
contrasts_with: []
answers_questions:
  - "How do you parse complex input grammars in a macro?"
  - "What is the most powerful macro parsing technique?"
  - "How do you process input one piece at a time in a macro?"
  - "Why is the unprocessed tail captured as $($tail:tt)* ?"
---

# Quick Definition

A TT muncher is a recursive `macro_rules!` macro that processes its input one step at a time. At each step, it matches and removes ("munches") some tokens from the start of its input, generates intermediate output, then recurses on the remaining tail captured as `$($tail:tt)*`.

# Core Definition

"This pattern is perhaps the *most powerful* macro parsing technique available, allowing one to parse grammars of significant complexity. A 'TT muncher' is a recursive macro that works by incrementally processing its input one step at a time. At each step, it matches and removes (munches) some sequence of tokens from the start of its input, generates some intermediate output, then recurses on the input tail."

"The reason for 'TT' in the name specifically is that the unprocessed part of the input is *always* captured as `$($tail:tt)*`. This is done as a `tt` repetition is the only way to *losslessly* capture part of a macro's input."

# Prerequisites

- **macro_rules!** -- TT munchers are built using declarative macro definitions
- **Token trees** -- the `$($tail:tt)*` capture is the foundation of the pattern
- **Macro repetition** -- understanding `$(...)*` repetition syntax is required
- **Macro matchers** -- each "munch" step is a matcher rule that peels off specific token patterns

# Key Properties

1. Input tail is always captured as `$($tail:tt)*` -- this is the only lossless way to capture remaining input
2. Each rule matches a specific prefix pattern and recurses on the tail
3. A terminating rule (typically matching empty input `()`) stops the recursion
4. Can only match against literals and grammar constructs capturable by `macro_rules!`
5. Cannot match unbalanced groups (parentheses, brackets, braces)
6. Subject to the macro recursion limit (default 128) -- no tail recursion optimisation exists
7. Multiple rules can handle different input variants, enabling complex grammar parsing

# Construction / Recognition

## To Construct:
1. Define a terminating rule that matches empty input: `() => { ... }`
2. For each grammar construct to recognise, define a rule that matches the construct followed by `$($tail:tt)*`
3. Each rule processes the matched construct and recurses: `my_macro!($($tail)*)`
4. Consider matching multiple tokens per step to reduce recursion depth

## To Recognise:
1. A macro with multiple rules that all end with `$($tail:tt)*` captures
2. Each rule recursively invokes the same macro with `$($tail)*`
3. There is a base case rule matching empty input

# Context & Application

TT munchers are the workhorse pattern for any macro that needs to parse structured or mixed-format input. They are commonly combined with push-down accumulation (to build up results) and internal rules (to organise the parsing logic). The source warns to keep recursion "as limited as possible" by adding rules for common variations rather than recursing through intermediate layers, or by making input syntax compromises to leverage standard repetitions instead.

# Examples

**Example 1** (Ch. 3, "Incremental TT munchers"): Parsing a mixed trace/assign DSL:

```rust
macro_rules! mixed_rules {
    () => {};
    (trace $name:ident; $($tail:tt)*) => {
        {
            println!(concat!(stringify!($name), " = {:?}"), $name);
            mixed_rules!($($tail)*);
        }
    };
    (trace $name:ident = $init:expr; $($tail:tt)*) => {
        {
            let $name = $init;
            println!(concat!(stringify!($name), " = {:?}"), $name);
            mixed_rules!($($tail)*);
        }
    };
}

fn main() {
    let a = 42;
    let b = "Ho-dee-oh-di-oh-di-oh!";
    mixed_rules!(
        trace a;
        trace b;
        trace b = "They took her where they put the crazies.";
        trace b;
    );
}
```

**Example 2** (Ch. 5, "Ook!" -- opcode parsing): The Ook! implementation uses TT munching to parse pairs of tokens as opcodes:

```rust
// Each rule matches two-token opcode, emits Rust code, recurses on tail
(@e $syms:tt; (Ook. Ook? $($tail:tt)*)) => {
    $i = ($i + 1) % MEM_SIZE;
    Ook!(@e $syms; ($($tail)*));
};
(@e $syms:tt; (Ook. Ook. $($tail:tt)*)) => {
    $inc($a, $i);
    Ook!(@e $syms; ($($tail)*));
};
```

# Relationships

## Builds Upon
- **macro-rules** -- TT munchers are declarative macros using `macro_rules!`
- **token-tree** -- the `tt` fragment specifier is fundamental to the pattern
- **macro-repetition** -- `$($tail:tt)*` is a repetition capture

## Enables
- **macro-parsing** -- TT munchers are the primary mechanism for parsing structured macro input
- **push-down-accumulation** -- TT munchers frequently accumulate results as they parse

## Related
- **callback-pattern** -- TT munchers often invoke a callback with their final result
- **internal-rules** -- complex TT munchers use `@`-prefixed rules to organise parsing phases
- **repetition-replacement** -- can sometimes replace TT munching when input has uniform structure

## Contrasts With
- None explicitly -- the alternative is standard repetition matching, which cannot handle mixed grammars

# Common Errors

- **Error**: Exceeding the macro recursion limit with large inputs.
  **Correction**: Match multiple tokens per step (e.g., match 5 or 10 at a time for uniform input), or add rules for common multi-token patterns to reduce recursion depth. You can also raise the limit with `#![recursion_limit = "256"]` but this is a band-aid.

- **Error**: Forgetting the terminating base case `() => {}` rule.
  **Correction**: Always include a rule that matches empty input to stop recursion. Without it, the macro will fail to match when input is exhausted.

# Common Confusions

- **Confusion**: Thinking `$($tail:tt)*` can be replaced with another fragment specifier like `$($tail:expr),*`.
  **Clarification**: Only `tt` losslessly captures arbitrary remaining input. Other fragment specifiers impose parsing constraints that would reject valid input or alter token grouping.

- **Confusion**: Expecting TT munchers to benefit from tail-call optimisation like recursive functions.
  **Clarification**: "`macro_rules!` does not have *any* form of tail recursion elimination or optimisation." Each recursive step adds to the expansion depth, which is bounded by the recursion limit.

# Source Reference

Chapter 3: Patterns, "Incremental TT munchers" section. The pattern is introduced with the `mixed_rules!` example and described as "perhaps the *most powerful* macro parsing technique available." Also demonstrated extensively in Chapter 5's Ook! implementation.

# Verification Notes

- Definition source: Direct quotation from "Incremental TT munchers" section, paragraphs 1-2
- Key Properties: All from explicit statements in the same section, including restrictions and performance guidance
- Confidence rationale: HIGH -- the source gives a thorough definition, rationale, and practical guidance
- Uncertainties: The recursion limit default and optimisation status may evolve in future Rust versions
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
