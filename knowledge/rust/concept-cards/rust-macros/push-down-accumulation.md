---
concept: Push-down Accumulation
slug: push-down-accumulation
category: macro-patterns
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "03-patterns"
chapter_number: 3
pdf_page: null
section: "Push-down Accumulation"
extraction_confidence: high
aliases:
  - "pushdown accumulation"
  - "macro accumulator"
  - "accumulation buffer"
  - "push-down macro"
prerequisites:
  - macro-rules
  - token-tree
  - macro-expansion
  - internal-rules
extends:
  - macro-rules
related:
  - tt-muncher
  - internal-rules
  - ast-coercion
  - callback-pattern
contrasts_with: []
answers_questions:
  - "How do you incrementally build up a result in a macro?"
  - "Why can't macros expand to partial syntax constructs?"
  - "How do you accumulate tokens across recursive macro calls?"
  - "What does the ($input) -> ($output) convention mean in macros?"
---

# Quick Definition

Push-down accumulation is a pattern where a recursive macro incrementally builds up a sequence of tokens in an accumulation buffer (captured as `$($body:tt)*`) without requiring any intermediate step to produce a complete syntax construct. Only the final terminating rule emits the accumulated tokens as a valid Rust expression, item, or other grammar element.

# Core Definition

"All macros in Rust **must** result in a complete, supported syntax element (such as an expression, item, *etc.*). This means that it is impossible to have a macro expand to a partial construct."

"Push-down, however, allows us to incrementally build up a sequence of tokens without needing to actually have a complete construct at any point prior to completion. [...] As you can see, each layer adds to the accumulated output until the terminating rule finally emits it as a complete construct."

"The only critical part of the above formulation is the use of `$($body:tt)*` to preserve the output without triggering parsing. The use of `($input) -> ($output)` is simply a convention adopted to help clarify the behaviour of such macros."

# Prerequisites

- **macro_rules!** -- push-down accumulation uses recursive declarative macros
- **Token trees** -- the accumulation buffer is captured as `$($body:tt)*` to avoid premature parsing
- **Macro expansion** -- understanding that each expansion must produce complete syntax motivates this pattern
- **Internal rules** -- push-down accumulation typically uses `@`-prefixed internal rules for its phases

# Key Properties

1. The accumulation buffer uses `$($body:tt)*` to hold tokens without triggering the parser
2. Each recursive step appends tokens to the buffer and recurses
3. Only the final (terminating) rule emits the buffer as a complete syntax construct
4. Intermediate expansions never need to be valid Rust syntax
5. The `($input) -> ($output)` notation is a conventional (not required) way to structure the rules
6. Frequently combined with TT munchers, where the muncher feeds parsed tokens into the accumulator

# Construction / Recognition

## To Construct:
1. Define internal rules with an accumulation parameter: `(@accum ($input) -> ($($body:tt)*))`
2. In each recursive rule, append new tokens to `$body` and recurse: `my_macro!(@accum ($rest) -> ($($body)* new_tokens))`
3. Define a terminating rule that emits the accumulated buffer as a complete construct: `(@accum () -> ($($body:tt)*)) => { [$($body)*] }`
4. Use an AST coercion helper if the parser does not accept `tt` substitutions in the output position

## To Recognise:
1. A macro with rules that pass `$($body:tt)*` or similar through recursive calls
2. Tokens are appended to the body in each step: `($($body)* new_token,)`
3. A final rule converts the accumulated tokens into a complete syntax element
4. The `->` arrow convention separating input from accumulated output

# Context & Application

The source demonstrates the problem with a naive approach to building an array initialiser. The naive version would expand like: `[e, init_array!(@accum 2, e)]` then `[e, e, init_array!(@accum 1, e)]` -- but each intermediate step is an incomplete array expression, which Rust forbids. Push-down accumulation avoids this by keeping the partial result inside a `tt` group where it is not parsed until the final step.

Push-down accumulation is "frequently used as part of incremental TT munchers, as it allows arbitrarily complex intermediate results to be constructed."

# Examples

**Example 1** (Ch. 3, "Push-down Accumulation"): Array initialiser that clones an expression N times:

```rust
macro_rules! init_array {
    (@accum (0, $_e:expr) -> ($($body:tt)*))
        => {init_array!(@as_expr [$($body)*])};
    (@accum (1, $e:expr) -> ($($body:tt)*))
        => {init_array!(@accum (0, $e) -> ($($body)* $e,))};
    (@accum (2, $e:expr) -> ($($body:tt)*))
        => {init_array!(@accum (1, $e) -> ($($body)* $e,))};
    (@accum (3, $e:expr) -> ($($body:tt)*))
        => {init_array!(@accum (2, $e) -> ($($body)* $e,))};
    (@as_expr $e:expr) => {$e};
    [$e:expr; $n:tt] => {
        {
            let e = $e;
            init_array!(@accum ($n, e.clone()) -> ())
        }
    };
}

let strings: [String; 3] = init_array![String::from("hi!"); 3];
// Expansion trace:
// init_array!(@accum (3, e.clone()) -> ())
// init_array!(@accum (2, e.clone()) -> (e.clone(),))
// init_array!(@accum (1, e.clone()) -> (e.clone(), e.clone(),))
// init_array!(@accum (0, e.clone()) -> (e.clone(), e.clone(), e.clone(),))
// init_array!(@as_expr [e.clone(), e.clone(), e.clone(),])
```

**Example 2** (Ch. 4, "Enum Parsing"): The `parse_unitary_variants!` macro accumulates variant names:

```rust
// Accumulating variant names into the output buffer:
(@collect_unitary_variants $fixed:tt,
    ($var:ident $(= $_val:expr)*, $($tail:tt)*) -> ($($var_names:tt)*)
) => {
    parse_unitary_variants! {
        @collect_unitary_variants $fixed,
        ($($tail)*) -> ($($var_names)* $var,)
    }
};
```

# Relationships

## Builds Upon
- **macro-rules** -- the pattern uses recursive `macro_rules!` definitions
- **token-tree** -- `$($body:tt)*` buffers tokens without parsing
- **internal-rules** -- `@accum` and `@as_expr` are internal rule prefixes

## Enables
- **macro-parsing** -- complex parsing macros use accumulation to build their output
- **macro-counting** -- some counting techniques use accumulation to build expressions

## Related
- **tt-muncher** -- TT munchers and push-down accumulation are frequently combined
- **ast-coercion** -- the final accumulated `tt` sequence often needs AST coercion to parse correctly
- **callback-pattern** -- accumulated results may be passed to a callback macro

## Contrasts With
- None explicitly -- the naive alternative (intermediate partial expansions) is simply not possible in Rust

# Common Errors

- **Error**: Trying to accumulate tokens outside of a group, causing them to be parsed prematurely.
  **Correction**: Always wrap the accumulation buffer in a group and capture as `$($body:tt)*`. The tokens inside are not parsed until the final emission step.

- **Error**: Forgetting to include an AST coercion rule when emitting the final accumulated result.
  **Correction**: If the parser rejects the final `tt` substitution, add an `(@as_expr $e:expr) => {$e}` or equivalent coercion rule to force parsing.

# Common Confusions

- **Confusion**: Thinking the `($input) -> ($output)` syntax is special Rust macro syntax.
  **Clarification**: This is purely a convention. The `->` is just a regular token used to visually separate input from output in the macro rules. Any token or arrangement could be used instead.

- **Confusion**: Believing that intermediate macro expansions must be valid Rust syntax.
  **Clarification**: Intermediate steps in push-down accumulation never actually produce syntax -- they only pass tokens around as `tt` sequences inside macro arguments. Only the final rule emits real Rust syntax.

# Source Reference

Chapter 3: Patterns, "Push-down Accumulation" section. The pattern is introduced with the `init_array!` example, contrasted with the naive approach that fails, and a full expansion trace is provided. The section concludes by noting its frequent combination with TT munchers.

# Verification Notes

- Definition source: Direct quotation from "Push-down Accumulation" section, paragraphs 1-3 and concluding paragraph
- Key Properties: Derived from source explanation and the expansion trace
- Confidence rationale: HIGH -- the source thoroughly explains the pattern with a complete trace showing each expansion step
- Uncertainties: None for the definition
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
