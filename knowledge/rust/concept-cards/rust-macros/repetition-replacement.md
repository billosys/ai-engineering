---
concept: Repetition Replacement
slug: repetition-replacement
category: macro-patterns
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "03-patterns"
chapter_number: 3
pdf_page: null
section: "Repetition replacement"
extraction_confidence: high
aliases:
  - "replace_expr"
  - "token replacement"
  - "repetition substitution"
  - "repetition-driven expansion"
prerequisites:
  - macro-rules
  - macro-repetition
  - fragment-specifier
extends:
  - macro-repetition
related:
  - macro-counting
  - tt-muncher
  - push-down-accumulation
contrasts_with: []
answers_questions:
  - "How do you repeat an expression once for each element in a macro repetition?"
  - "How do you use a matched repetition only to drive the count of output repetitions?"
  - "What is replace_expr and how does it work?"
---

# Quick Definition

Repetition replacement is a pattern where a matched repetition variable is captured but intentionally discarded, used only to drive the number of repetitions in the output. A helper macro `replace_expr!` takes a token tree (which it ignores) and a substitution expression (which it returns), enabling each element of the input repetition to be replaced with a fixed expression.

# Core Definition

"This pattern is where a matched repetition sequence is simply discarded, with the variable being used to instead drive some repeated pattern that is related to the input only in terms of length."

"Here, we are not actually *using* the matched types. Instead, we throw them away and instead replace them with a single, repeated expression. To put it another way, we don't care *what* the types are, only *how many* there are."

# Prerequisites

- **macro_rules!** -- the pattern is implemented using declarative macros
- **Macro repetition** -- understanding `$(...)*` repetition in both matching and substitution
- **Fragment specifiers** -- understanding `tt` and `expr` captures

# Key Properties

1. The core helper is: `macro_rules! replace_expr { ($_t:tt $sub:expr) => {$sub}; }`
2. The first parameter (prefixed with `_` by convention) is matched but discarded
3. The second parameter is the substitution expression that replaces each input element
4. When used inside a repetition, it maps each input token to the same fixed output
5. The input repetition variable must appear inside the `$(...)* ` expansion to satisfy Rust's requirement that all repetition variables are used

# Construction / Recognition

## To Construct:
1. Define the helper: `macro_rules! replace_expr { ($_t:tt $sub:expr) => {$sub}; }`
2. In the outer macro, capture a repetition: `($($items:ty),*)`
3. In the expansion, use `replace_expr!` inside a repetition to map each item to a fixed expression: `$(replace_expr!($items fixed_expression)),*`

## To Recognise:
1. A helper macro that takes two arguments and returns only the second
2. A repetition expansion where the matched variable is only used to "drive" the repetition count
3. The name `replace_expr` (which has become a conventional name for this helper)

# Context & Application

This pattern solves a specific problem: Rust requires that every repetition variable captured in a matcher must appear in the corresponding expansion repetition. If you want to repeat a fixed expression N times where N equals the length of some input sequence, you need a way to "use" the input variable without actually consuming its value. `replace_expr!` provides this by accepting the variable and discarding it.

The pattern is also fundamental to several counting techniques (see macro-counting) and is used wherever the structure of the output depends on the length, not the content, of the input.

# Examples

**Example 1** (Ch. 3, "Repetition replacement"): Constructing a default tuple from a list of types:

```rust
macro_rules! replace_expr {
    ($_t:tt $sub:expr) => {$sub};
}

macro_rules! tuple_default {
    ($($tup_tys:ty),*) => {
        (
            $(
                replace_expr!(
                    ($tup_tys)
                    Default::default()
                ),
            )*
        )
    };
}

assert_eq!(tuple_default!(i32, bool, String), (0, false, String::new()));
```

Note: the types are wrapped in parentheses `($tup_tys)` to form a single `tt` for `replace_expr!`. The types themselves are never used -- only their count matters.

**Example 2** (Ch. 4, "Counting -- Repetition with replacement"): Counting tokens by replacing each with `1usize`:

```rust
macro_rules! replace_expr {
    ($_t:tt $sub:expr) => {$sub};
}

macro_rules! count_tts {
    ($($tts:tt)*) => {0usize $(+ replace_expr!($tts 1usize))*};
}

assert_eq!(count_tts!(0 1 2), 3);
// Expands to: 0usize + 1usize + 1usize + 1usize
```

# Relationships

## Builds Upon
- **macro-repetition** -- the pattern exists specifically to work within repetition expansions
- **fragment-specifier** -- uses `tt` for the discarded input and `expr` for the substitution

## Enables
- **macro-counting** -- the "repetition with replacement" and "slice length" counting techniques both use `replace_expr!`

## Related
- **tt-muncher** -- TT munchers can achieve similar results for more complex transformations
- **push-down-accumulation** -- accumulation patterns sometimes use replacement for uniform output generation

## Contrasts With
- None explicitly -- this is a specialised utility pattern with no direct alternative in `macro_rules!`

# Common Errors

- **Error**: Passing a multi-token type directly to `replace_expr!` without wrapping it in a group.
  **Correction**: Types like `Vec<String>` are multiple tokens. Wrap them in parentheses to form a single `tt`: `replace_expr!(($tup_tys) Default::default())`.

- **Error**: Using `replace_expr!` with very large inputs (500+ tokens) causing compiler crashes.
  **Correction**: The "repetition with replacement" approach produces deeply nested ASTs. For large inputs, use the "slice length" counting technique instead: `<[()]>::len(&[$(replace_expr!($tts ())),*])`.

# Common Confusions

- **Confusion**: Thinking the `$_t` prefix means the variable is somehow special.
  **Clarification**: The underscore prefix is just a naming convention (like `_` in let bindings) to signal that the variable is intentionally unused. It has no effect on macro behaviour.

- **Confusion**: Wondering why you cannot just write `$(Default::default()),*` without referencing the matched variable.
  **Clarification**: Rust requires that every repetition variable captured in the matcher must appear inside the `$()*` expansion in the transcriber. The `replace_expr!` call satisfies this requirement while discarding the actual value.

# Source Reference

Chapter 3: Patterns, "Repetition replacement" section. The `replace_expr!` helper is introduced and demonstrated with the `tuple_default!` example. The counting application is shown in Chapter 4: Building Blocks, "Counting -- Repetition with replacement" section.

# Verification Notes

- Definition source: Direct quotation from "Repetition replacement" section, paragraphs 1-2
- Key Properties: Derived from source examples and explanation
- Confidence rationale: HIGH -- the source clearly defines the pattern with a concrete example and explains the rationale
- Uncertainties: None for the definition
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
