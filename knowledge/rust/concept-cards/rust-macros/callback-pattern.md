---
concept: Callback Pattern
slug: callback-pattern
category: macro-patterns
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "03-patterns"
chapter_number: 3
pdf_page: null
section: "Callbacks"
extraction_confidence: high
aliases:
  - "macro callback"
  - "callback macro"
  - "macro indirection"
prerequisites:
  - macro-rules
  - token-tree
  - macro-expansion
extends:
  - macro-rules
related:
  - tt-muncher
  - internal-rules
  - macro-invocation-design
contrasts_with:
  - macro-expansion
answers_questions:
  - "How do you pass information from one macro expansion to another?"
  - "Why can't a macro use the output of another macro's expansion directly?"
  - "How do you compose macros that depend on each other's output?"
---

# Quick Definition

The callback pattern passes the name of a macro as an argument to another macro, which then invokes it with computed results. This works around the limitation that macro expansion order prevents one macro from directly using the expansion of another macro as input.

# Core Definition

"Due to the order that macros are expanded in, it is (as of Rust 1.2) impossible to pass information to a macro from the expansion of *another* macro. This can make modularising macros very difficult. An alternative is to use recursion and pass a callback." The pattern works by having a macro accept a callback identifier, compute some result, and then invoke the callback with that result. Using a `tt` repetition, arbitrary arguments can also be forwarded to the callback.

# Prerequisites

- **macro_rules!** -- understanding basic declarative macro definition is required
- **Token trees** -- the callback pattern relies on `tt` repetitions to forward arbitrary arguments
- **Macro expansion** -- understanding expansion order is essential to understanding why the callback pattern is needed

# Key Properties

1. A callback is a macro name (captured as `$callback:ident`) passed as an argument to another macro
2. The receiving macro invokes the callback with computed results using `$callback!(...)`
3. This circumvents the limitation that macro expansion order prevents direct composition
4. Arbitrary additional arguments can be forwarded using `$($args:tt)*` repetitions
5. The pattern enables modularisation of macro logic across multiple macro definitions

# Construction / Recognition

## To Construct:
1. Define the "worker" macro that accepts a callback identifier as a parameter: `($callback:ident) => { ... }`
2. Have the worker macro invoke the callback with the computed result: `$callback!(result_tokens)`
3. Invoke the worker macro, passing the name of the macro that should receive the result

## To Recognise:
1. A macro parameter captured as `$callback:ident` that is later invoked with `!`
2. A macro invocation where one argument is the name of another macro
3. Chains of macro calls where results flow "upward" through callbacks rather than "downward" through nesting

# Context & Application

The callback pattern is needed because `recognise_tree!(expand_to_larch!())` does not work as expected -- the inner macro invocation is not expanded before matching. Instead, the entire `expand_to_larch!()` is treated as tokens to match against, which fails. The callback pattern reverses the flow: `call_with_larch!(recognise_tree)` causes `call_with_larch` to invoke `recognise_tree!(larch)` directly with the result.

This pattern is commonly used in combination with TT munchers and push-down accumulation, where a macro that parses or accumulates a result needs to pass its output to a caller-specified macro for final processing.

# Examples

**Example 1** (Ch. 3, "Callbacks"): Direct composition fails, but callbacks succeed:

```rust
macro_rules! call_with_larch {
    ($callback:ident) => { $callback!(larch) };
}

macro_rules! recognise_tree {
    (larch) => { println!("#1, the Larch.") };
    ($($other:tt)*) => { println!("I don't know; some kind of birch maybe?") };
}

fn main() {
    // This does NOT work -- expand_to_larch!() is not expanded first:
    // recognise_tree!(expand_to_larch!());
    // prints: "I don't know; some kind of birch maybe?"

    // This DOES work via callback:
    call_with_larch!(recognise_tree);
    // prints: "#1, the Larch."
}
```

**Example 2** (Ch. 3, "Callbacks"): Forwarding arbitrary arguments through a callback:

```rust
macro_rules! callback {
    ($callback:ident($($args:tt)*)) => {
        $callback!($($args)*)
    };
}

fn main() {
    callback!(callback(println("Yes, this *was* unnecessary.")));
}
```

# Relationships

## Builds Upon
- **macro-rules** -- the callback pattern is built entirely within the `macro_rules!` system
- **token-tree** -- `tt` repetitions are used to forward arbitrary arguments

## Enables
- **macro-parsing** -- the enum parsing building block uses callbacks to deliver parsed results
- **macro-invocation-design** -- callbacks are a key tool for designing composable macro APIs

## Related
- **tt-muncher** -- TT munchers often use callbacks to deliver their final output
- **push-down-accumulation** -- accumulated results are often passed to a callback at the end
- **internal-rules** -- internal rules provide an alternative to callbacks for intra-macro composition

## Contrasts With
- **Direct macro composition** -- unlike function calls, nested macro invocations do not expand inner-to-outer

# Common Errors

- **Error**: Trying to use `my_macro!(other_macro!())` expecting the inner macro to expand first.
  **Correction**: Macro expansion order does not work like function evaluation. Use the callback pattern: have the inner macro accept `my_macro` as a callback identifier and invoke it with the result.

- **Error**: Capturing the callback as `$callback:expr` instead of `$callback:ident`.
  **Correction**: Macro names must be captured as `ident` since they are identifiers, not expressions. An expression cannot appear before `!` in a macro invocation.

# Common Confusions

- **Confusion**: Thinking callbacks in macros work like closures or function pointers.
  **Clarification**: Macro callbacks are purely a compile-time textual mechanism. The "callback" is just a macro name that gets invoked with tokens -- there is no runtime indirection, no captures, and no type system involvement.

- **Confusion**: Believing that `$callback:ident` limits you to passing only simple tokens.
  **Clarification**: While the callback name itself must be a single identifier, you can forward arbitrarily complex token sequences as arguments using `$($args:tt)*` repetitions.

# Source Reference

Chapter 3: Patterns, "Callbacks" section. The pattern is introduced with the `call_with_larch` / `recognise_tree` example demonstrating why direct composition fails and how callbacks solve the problem. The section also shows argument forwarding with `tt` repetitions.

# Verification Notes

- Definition source: Direct quotation from "Callbacks" section opening paragraphs
- Key Properties: Derived from source examples and explanation
- Confidence rationale: HIGH -- the source explicitly defines the pattern with clear examples and traces the expansion steps
- Uncertainties: None for the definition; the source notes this limitation exists "as of Rust 1.2" which may have evolved
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
