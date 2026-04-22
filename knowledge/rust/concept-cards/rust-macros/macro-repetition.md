---
concept: Macro Repetition
slug: macro-repetition
category: macro-system
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "01-methodical-introduction"
chapter_number: 1
pdf_page: null
section: "Repetitions"
extraction_confidence: high
aliases:
  - "repetition pattern"
  - "macro repeat"
  - "$(...)* pattern"
  - "$(...)+ pattern"
prerequisites:
  - macro-rules
  - metavariable
extends: []
related:
  - macro-matcher
  - fragment-specifier
  - macro-expansion
contrasts_with: []
answers_questions:
  - "How do you match repeated patterns in macro_rules!?"
  - "What is the syntax for macro repetitions?"
  - "What is the difference between * and + in macro repetitions?"
  - "How do repetitions work in macro expansions?"
---

# Quick Definition

Macro repetitions allow patterns to match a sequence of tokens zero or more (`*`) or one or more (`+`) times, with an optional separator. The syntax is `$( ... ) sep rep` in both the matcher and the expansion. Captures inside repetitions can be substituted in corresponding expansion repetitions.

# Core Definition

Repetitions in `macro_rules!` have the general form `$( ... ) sep rep`:

- `$` is a literal dollar token.
- `( ... )` is the paren-grouped pattern being repeated.
- `sep` is an optional separator token. Common examples are `,` and `;`.
- `rep` is the required repeat control: either `*` (zero or more) or `+` (one or more). You cannot write "zero or one" or any other specific count or range.

Repetitions can contain any other valid pattern, including literal token trees, captures, and other repetitions (nesting).

Repetitions use the same syntax in the expansion as in the matcher. Each repetition in the expansion corresponds to its counterpart in the matcher, and captured variables within the repetition are substituted once per repetition iteration.

# Prerequisites

- **macro-rules** -- Repetitions are part of the `macro_rules!` pattern and expansion syntax
- **metavariable** -- Captures within repetitions bind values per iteration

# Key Properties

1. **Two repeat controls**: `*` (zero or more) and `+` (one or more). No "zero or one" or bounded counts.
2. **Optional separator**: A single token (commonly `,` or `;`) that must appear between repetitions.
3. **Nestable**: Repetitions can contain other repetitions, captures, and literal tokens.
4. **Symmetric syntax**: The same `$(...)sep*` syntax is used in both the matcher and the expansion.
5. **Per-iteration substitution**: Captures inside a repetition are substituted once per iteration in the expansion.
6. **No adjacent repetitions**: `macro_rules!` generally forbids a repetition from being followed by another repetition, even if the contents do not conflict.

# Construction / Recognition

## Basic repetition with separator

```rust
macro_rules! vec_strs {
    (
        $(
            $element:expr
        )
        ,       // separator
        *       // zero or more
    ) => {
        {
            let mut v = Vec::new();
            $(
                v.push(format!("{}", $element));
            )*
            v
        }
    };
}
```

This matches zero or more comma-separated expressions. In the expansion, `$( v.push(...); )*` repeats the push statement once for each captured `$element`.

## Invocation

```rust
let s = vec_strs![1, "a", true, 3.14159f32];
assert_eq!(&*s, &["1", "a", "true", "3.14159"]);
```

## One or more (`+`)

```rust
macro_rules! at_least_one {
    ( $( $item:expr ),+ ) => { ... };
}
// at_least_one!()  -- would NOT match (requires at least one)
// at_least_one!(1) -- matches
// at_least_one!(1, 2, 3) -- matches
```

# Context & Application

Repetitions are what make `macro_rules!` powerful enough to handle variadic-style patterns. Without repetitions, macros could only accept a fixed number of arguments. With repetitions, macros like `vec![]`, `println!()`, and custom DSL macros can accept varying numbers of inputs.

The separator token is important for usability -- it allows natural-looking syntax like `vec![1, 2, 3]` where commas separate the elements, or statement-like macros where semicolons separate entries.

Nested repetitions enable advanced patterns but require care: each level of repetition nesting in the expansion must correspond to the same nesting level in the matcher, and the captured variables must be at the correct repetition depth.

The restriction against adjacent repetitions and the limited repeat controls (`*` and `+` only) are notable limitations compared to regex-style repetition. More sophisticated patterns (like optional elements or counted repetitions) must be achieved through multiple rules or recursive macro invocations.

# Examples

**Complete `vec_strs` macro** (from "Repetitions" section):

```rust
macro_rules! vec_strs {
    (
        $(
            $element:expr
        )
        ,
        *
    ) => {
        {
            let mut v = Vec::new();
            $(
                v.push(format!("{}", $element));
            )*
            v
        }
    };
}

fn main() {
    let s = vec_strs![1, "a", true, 3.14159f32];
    assert_eq!(&*s, &["1", "a", "true", "3.14159"]);
}
```

The matcher `$( $element:expr ),*` captures zero or more comma-separated expressions. The expansion `$( v.push(format!("{}", $element)); )*` generates one push statement per captured element.

# Relationships

## Builds Upon

- **metavariable** -- Captures within repetitions bind per-iteration values
- **macro-rules** -- Repetitions are part of the `macro_rules!` syntax

## Enables

- **tt-muncher** -- Advanced pattern that processes token trees one at a time using repetitions
- **push-down-accumulation** -- Pattern that accumulates results through repeated macro calls
- **macro-counting** -- Counting techniques using repetition expansion

## Related

- **macro-matcher** -- Repetitions appear within matchers
- **macro-expansion** -- Repetitions in expansion generate repeated code

# Common Errors

1. **Adjacent repetitions**: Placing `$($a:expr),* $($b:expr),*` in a pattern is generally forbidden by `macro_rules!`.
2. **Mismatched repetition depth**: Using a capture from a repetition outside of a corresponding repetition in the expansion causes a compile error.
3. **Trailing separator confusion**: `$($e:expr),*` matches `1, 2, 3` but not `1, 2, 3,` (trailing comma). Some macros use `$($e:expr,)*` or `$($e:expr),* $(,)?` to handle trailing separators.

# Common Confusions

- **Confusion**: Thinking `*` and `+` work exactly like regex quantifiers with backtracking.
  **Clarification**: Macro repetitions are greedy and non-backtracking, like captures. The parser commits to the repetition and cannot backtrack if later matching fails.
- **Confusion**: Expecting "zero or one" (`?`) or bounded repetitions (`{n,m}`).
  **Clarification**: Only `*` (zero or more) and `+` (one or more) are available. Optional elements must be handled through separate rules or other patterns.

# Source Reference

"The Little Book of Rust Macros" by Daniel Keep et al., Chapter 1: "Methodical Introduction," section "Repetitions."

# Verification Notes

- Repetition syntax and semantics: directly from the "Repetitions" section
- `vec_strs` example: directly from the source including the test assertion
- The restriction on adjacent repetitions: stated in "Captures and Expansion Redux"
- The available repeat controls (`*` and `+` only): explicitly stated in the source
- Confidence: HIGH -- explicit definition with complete working example
