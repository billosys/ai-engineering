---
concept: Macro Parsing (Enum Parsing)
slug: macro-parsing
category: macro-building-blocks
subcategory: null
tier: advanced
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "04-building-blocks"
chapter_number: 4
pdf_page: null
section: "Enum Parsing"
extraction_confidence: high
aliases:
  - "enum parsing"
  - "parse_unitary_variants"
  - "macro-based parsing"
  - "declarative macro parsing"
prerequisites:
  - macro-rules
  - token-tree
  - tt-muncher
  - push-down-accumulation
  - callback-pattern
  - internal-rules
extends:
  - tt-muncher
related:
  - ast-coercion
  - macro-counting
  - macro-invocation-design
contrasts_with: []
answers_questions:
  - "How do you parse Rust enum definitions inside a macro?"
  - "How do you combine TT munching, push-down accumulation, and callbacks in one macro?"
  - "How do you extract variant names from an enum in a macro?"
  - "How do you handle attributes and initializers when parsing enum variants?"
---

# Quick Definition

Macro parsing is the technique of using an incremental TT muncher with push-down accumulation and callbacks to parse structured Rust syntax (such as enum definitions) inside a `macro_rules!` macro. The source demonstrates this with `parse_unitary_variants!`, which extracts variant names from a unitary enum and passes them to a caller-specified callback macro.

# Core Definition

"This macro shows how you can use an incremental tt muncher and push-down accumulation to parse the variants of an `enum` where all variants are unitary (*i.e.* they have no payload). Upon completion, `parse_unitary_variants!` invokes a callback macro with the list of variants (plus any other arbitrary arguments supplied)."

"This can be modified to also parse `struct` fields, compute tag values for the variants, or even extract the names of *all* variants in an arbitrary `enum`."

The macro combines all the major patterns from Chapters 3 and 4: internal rules (`@collect_unitary_variants`, `@as_expr`, `@as_item`), TT munching (consuming variants one at a time from the body), push-down accumulation (building up the list of variant names in `$($var_names:tt)*`), and callbacks (invoking `$callback!` with the final result).

# Prerequisites

- **macro_rules!** -- the parsing macro is a `macro_rules!` definition
- **Token trees** -- input is captured and processed as `tt` sequences
- **TT muncher** -- variants are consumed one at a time from the enum body
- **Push-down accumulation** -- variant names are accumulated in `($($var_names:tt)*)` 
- **Callback pattern** -- the final result is passed to a caller-specified callback macro
- **Internal rules** -- `@collect_unitary_variants`, `@as_expr`, `@as_item` organise the logic

# Key Properties

1. Entry rule accepts an enum definition and a callback: `(enum $name:ident {$($body:tt)*} => $callback:ident $arg:tt)`
2. The enum body is processed one variant at a time via TT munching
3. Attributes (`#[...]`) on variants are consumed and skipped
4. Variants with optional `= value` initialisers are handled
5. Variants with payloads (tuple or struct) trigger a compile-time error message
6. The final variant list is passed to the callback as `($($var_names),*)`
7. Two exit rules handle expression callbacks (using `@as_expr`) and item callbacks (using `@as_item`)

# Construction / Recognition

## To Construct:
1. Define an entry rule that captures the enum body and a callback: `(enum $name:ident {$($body:tt)*} => $callback:ident $arg:tt)`
2. Normalise the body by appending a trailing comma: `($($body)*,)`
3. Define `@collect_unitary_variants` rules that munch one variant at a time, accumulating names
4. Handle special cases: attributes (skip), initialisers (strip `= val`), payloads (error)
5. Define exit rules that invoke the callback with accumulated names, using AST coercion

## To Recognise:
1. A macro that accepts `enum Name { ... }` as input
2. Internal rules with accumulation buffers (`-> ($($var_names:tt)*)`)
3. Rules that match and skip `#[$_attr:meta]` attributes
4. A callback invocation in the exit rule

# Context & Application

The `parse_unitary_variants!` macro is a reusable building block for deriving functionality from enum definitions. It can be used to auto-generate `FromStr` implementations, iteration over variants, serialisation logic, or any other code that needs to know the list of variant names. The callback mechanism makes it composable: different callers can provide different callbacks for different purposes.

The macro demonstrates a defensive approach to structured input: it explicitly handles attributes, optional initialisers, and payload variants (with an error), rather than relying on a fragile catch-all pattern.

# Examples

**Example 1** (Ch. 4, "Enum Parsing"): The complete `parse_unitary_variants!` macro with usage:

```rust
macro_rules! parse_unitary_variants {
    (@as_expr $e:expr) => {$e};
    (@as_item $($i:item)+) => {$($i)+};

    // Exit rules -- invoke callback with collected variant names.
    (
        @collect_unitary_variants ($callback:ident ( $($args:tt)* )),
        ($(,)*) -> ($($var_names:ident,)*)
    ) => {
        parse_unitary_variants! {
            @as_expr
            $callback!{ $($args)* ($($var_names),*) }
        }
    };

    // Consume an attribute.
    (
        @collect_unitary_variants $fixed:tt,
        (#[$_attr:meta] $($tail:tt)*) -> ($($var_names:tt)*)
    ) => {
        parse_unitary_variants! {
            @collect_unitary_variants $fixed,
            ($($tail)*) -> ($($var_names)*)
        }
    };

    // Handle a variant, optionally with an initialiser.
    (
        @collect_unitary_variants $fixed:tt,
        ($var:ident $(= $_val:expr)*, $($tail:tt)*) -> ($($var_names:tt)*)
    ) => {
        parse_unitary_variants! {
            @collect_unitary_variants $fixed,
            ($($tail)*) -> ($($var_names)* $var,)
        }
    };

    // Abort on variant with a payload.
    (
        @collect_unitary_variants $fixed:tt,
        ($var:ident $_struct:tt, $($tail:tt)*) -> ($($var_names:tt)*)
    ) => {
        const _error: () = "cannot parse unitary variants from enum with non-unitary variants";
    };

    // Entry rule.
    (enum $name:ident {$($body:tt)*} => $callback:ident $arg:tt) => {
        parse_unitary_variants! {
            @collect_unitary_variants
            ($callback $arg), ($($body)*,) -> ()
        }
    };
}

// Usage:
assert_eq!(
    parse_unitary_variants!(
        enum Dummy { A, B, C }
        => stringify(variants:)
    ),
    "variants : ( A , B , C )"
);
```

# Relationships

## Builds Upon
- **tt-muncher** -- variants are consumed incrementally from the enum body
- **push-down-accumulation** -- variant names are accumulated in `-> ($($var_names:tt)*)`
- **callback-pattern** -- the final result is delivered to a caller-specified macro
- **internal-rules** -- `@collect_unitary_variants`, `@as_expr`, `@as_item` organise the logic
- **ast-coercion** -- the callback invocation is wrapped in `@as_expr` or `@as_item`

## Enables
- Derive-like macro functionality for enums (auto-generating impl blocks, match arms, etc.)

## Related
- **macro-invocation-design** -- the entry rule's syntax (`enum Name {...} => callback arg`) illustrates macro API design
- **macro-counting** -- enum counting technique uses a similar approach (creating a hidden enum)

## Contrasts With
- None explicitly -- procedural macros (derive macros) are the alternative approach for parsing Rust syntax

# Common Errors

- **Error**: Forgetting to normalise the enum body by adding a trailing comma.
  **Correction**: The entry rule appends `,` to the body: `($($body)*,)`. Without this, the last variant would not match the `$var:ident ..., $($tail:tt)*` pattern because there would be no comma after it.

- **Error**: Not handling attributes on variants, causing the parser to choke on `#[...]` tokens.
  **Correction**: Include a rule that matches and consumes `#[$_attr:meta]` before continuing to parse the variant.

# Common Confusions

- **Confusion**: Thinking macro-based parsing can handle all Rust syntax as flexibly as procedural macros.
  **Clarification**: `macro_rules!` parsing is limited to what matchers can capture. Complex syntax (generic parameters, where clauses, visibility modifiers with paths) may require increasingly elaborate rules. For very complex parsing needs, procedural macros are more appropriate.

- **Confusion**: Thinking the `TT bundling` of `$fixed:tt` is the same as `$($args:tt)*`.
  **Clarification**: `$fixed:tt` captures the entire callback specification `($callback $arg)` as a single grouped token tree, allowing it to be forwarded as one unit through intermediate rules without destructuring. This is TT bundling -- it simplifies forwarding through rules that do not need to inspect the contents.

# Source Reference

Chapter 4: Building Blocks, "Enum Parsing" section. The complete `parse_unitary_variants!` macro is presented with all rules annotated. The section explicitly identifies the pattern as combining TT munching, push-down accumulation, and callbacks.

# Verification Notes

- Definition source: Direct quotation from "Enum Parsing" section, concluding paragraphs
- Key Properties: Derived from the complete macro source code and its annotations
- Confidence rationale: HIGH -- the source provides the complete, annotated implementation with working test
- Uncertainties: None for the definition
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
