---
concept: AST Coercion
slug: ast-coercion
category: macro-building-blocks
subcategory: null
tier: intermediate
source: "The Little Book of Rust Macros"
source_slug: rust-macros
authors: "Daniel Keep et al."
chapter: "04-building-blocks"
chapter_number: 4
pdf_page: null
section: "AST Coercion"
extraction_confidence: high
aliases:
  - "as_expr"
  - "as_item"
  - "macro coercion"
  - "tt coercion"
  - "AST forcing"
prerequisites:
  - macro-rules
  - token-tree
  - fragment-specifier
  - macro-expansion
extends:
  - macro-rules
related:
  - push-down-accumulation
  - internal-rules
  - macro-parsing
contrasts_with: []
answers_questions:
  - "Why does the parser reject my macro expansion even though the tokens are valid?"
  - "What are as_expr!, as_item!, as_pat!, and as_stmt! macros for?"
  - "How do you force tt tokens to be parsed as a specific grammar construct?"
  - "Why does the Rust parser give up on tt substitutions?"
---

# Quick Definition

AST coercion macros (`as_expr!`, `as_item!`, `as_pat!`, `as_stmt!`) are trivial helper macros that force the Rust parser to interpret a sequence of `tt` tokens as a specific grammar construct. They are necessary because the parser often fails to parse substituted `tt` tokens correctly, even when the tokens form valid syntax.

# Core Definition

"The Rust parser is not very robust in the face of `tt` substitutions. Problems can arise when the parser is expecting a particular grammar construct and *instead* finds a lump of substituted `tt` tokens. Rather than attempt to parse them, it will often just *give up*. In these cases, it is necessary to employ an AST coercion."

"These coercions are often used with push-down accumulation macros in order to get the parser to treat the final `tt` sequence as a particular kind of grammar construct."

"Note that this specific set of macros is determined by what macros are allowed to expand to, *not* what they are able to capture."

# Prerequisites

- **macro_rules!** -- AST coercion macros are defined using `macro_rules!`
- **Token trees** -- the problem arises specifically with `tt` substitutions
- **Fragment specifiers** -- each coercion macro uses a specific fragment specifier (`expr`, `item`, `pat`, `stmt`)
- **Macro expansion** -- understanding how the parser processes macro output is essential

# Key Properties

1. Each coercion macro is trivially simple: `macro_rules! as_expr { ($e:expr) => {$e} }`
2. They work by forcing the parser to re-parse the `tt` sequence through a specific fragment specifier
3. The available coercions are limited to what macros can expand to: `expr`, `item`, `pat`, `stmt`
4. There is no `as_ty!` macro because macros cannot appear in type position
5. Coercion macros are often embedded as internal rules (e.g., `@as_expr`) rather than defined separately
6. The input and output are identical -- the macro's only purpose is to trigger the parser

# Construction / Recognition

## To Construct:
1. Define a minimal macro for the target grammar construct: `macro_rules! as_expr { ($e:expr) => {$e} }`
2. Wrap problematic `tt` sequences in the coercion: `as_expr!(my_tt_tokens)`
3. Alternatively, embed as an internal rule: `(@as_expr $e:expr) => {$e};`

## To Recognise:
1. A macro named `as_expr`, `as_item`, `as_pat`, or `as_stmt` (or `@as_*` internal rules)
2. A macro whose body is simply `{$e}` or `{$i}` -- it passes through its input unchanged
3. Usage wrapping the output of push-down accumulation or other `tt`-producing patterns

# Context & Application

AST coercion is a necessary workaround for a parser limitation. When a push-down accumulation macro finishes building up a sequence of `tt` tokens and emits them, the parser may not recognise the tokens as valid syntax even though they are. Wrapping the emission in `as_expr!(...)` forces the parser to treat the tokens as an expression, resolving the ambiguity.

This pattern is so common that it appears in nearly every non-trivial macro that uses push-down accumulation. In the `init_array!` example from Chapter 3, the `@as_expr` internal rule serves exactly this purpose. The enum parsing example in Chapter 4 uses both `@as_expr` and `@as_item` coercions depending on whether the callback expects expression or item output.

# Examples

**Example 1** (Ch. 4, "AST Coercion"): The standard set of coercion macros:

```rust
macro_rules! as_expr { ($e:expr) => {$e} }
macro_rules! as_item { ($i:item) => {$i} }
macro_rules! as_pat  { ($p:pat) =>  {$p} }
macro_rules! as_stmt { ($s:stmt) => {$s} }

as_item!{struct Dummy;}

fn main() {
    as_stmt!(let as_pat!(_) = as_expr!(42));
}
```

**Example 2** (Ch. 3, "Visibility"): Using `as_item!` to coerce generated `impl` blocks:

```rust
macro_rules! newtype_new {
    (struct $name:ident($t:ty);) => { newtype_new! { () struct $name($t); } };
    (pub struct $name:ident($t:ty);) => { newtype_new! { (pub) struct $name($t); } };

    (($($vis:tt)*) struct $name:ident($t:ty);) => {
        as_item! {
            impl $name {
                $($vis)* fn new(value: $t) -> Self {
                    $name(value)
                }
            }
        }
    };
}

macro_rules! as_item { ($i:item) => {$i} }
```

**Example 3** (Ch. 3, "Push-down Accumulation"): AST coercion as an internal rule:

```rust
macro_rules! init_array {
    (@accum (0, $_e:expr) -> ($($body:tt)*))
        => {init_array!(@as_expr [$($body)*])};
    // ...
    (@as_expr $e:expr) => {$e};
}
```

# Relationships

## Builds Upon
- **macro-rules** -- coercion macros are `macro_rules!` definitions
- **token-tree** -- the problem is specific to `tt` substitutions
- **fragment-specifier** -- each coercion uses a specific fragment specifier to force parsing

## Enables
- **push-down-accumulation** -- accumulation patterns almost always need AST coercion for final output
- **macro-parsing** -- parsed and reconstructed syntax often requires coercion

## Related
- **internal-rules** -- coercion macros are frequently embedded as `@as_expr` internal rules

## Contrasts With
- None explicitly -- coercion is a workaround, not an alternative to another pattern

# Common Errors

- **Error**: Omitting AST coercion and getting unexpected parser errors from correct-looking macro output.
  **Correction**: When macro output comes from `tt` substitution (especially from push-down accumulation), wrap it in the appropriate coercion macro: `as_expr!`, `as_item!`, etc.

- **Error**: Trying to define `as_ty!` for type coercion.
  **Correction**: Macros cannot expand in type position (as of Rust 1.2 / issue #27245), so an `as_ty!` coercion macro is not possible.

# Common Confusions

- **Confusion**: Thinking AST coercion macros transform or modify their input.
  **Clarification**: They are pure pass-through. The input and output are identical tokens. The only effect is on the parser: the fragment specifier in the matcher forces the parser to interpret the tokens as a specific grammar construct.

- **Confusion**: Thinking you always need AST coercion when using `tt` tokens.
  **Clarification**: AST coercion is only needed when the parser fails to parse substituted `tt` sequences. In many contexts, `tt` substitutions parse correctly without coercion. You only need it when you observe parser errors on otherwise valid token sequences.

# Source Reference

Chapter 4: Building Blocks, "AST Coercion" section. The four standard coercion macros are defined and the parser limitation is explained. The pattern is also referenced in Chapter 3's "Visibility" and "Push-down Accumulation" sections. See also the "Enum Parsing" section in Chapter 4 where both `@as_expr` and `@as_item` are used.

# Verification Notes

- Definition source: Direct quotation from "AST Coercion" section, paragraphs 1-2
- Key Properties: Derived from source explanation, examples, and footnote about `as_ty!`
- Confidence rationale: HIGH -- the source clearly defines the problem and solution with concrete examples
- Uncertainties: The type position limitation (issue #27245) may have been resolved in newer Rust versions
- Cross-reference status: All slugs reference cards in this extraction set or Agent A/B sets
