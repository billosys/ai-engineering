---
concept: Patterns
slug: rust-patterns
category: language-fundamentals
subcategory: null
tier: intermediate
source: "The Rust Reference"
source_slug: reference
authors: "The Rust Project"
chapter: "Patterns"
chapter_number: 9
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "pattern matching"
  - "destructuring"
  - "refutable patterns"
  - "irrefutable patterns"
  - "binding modes"
  - "or-patterns"
  - "match patterns"
prerequisites:
  - rust-statements-and-expressions
extends: []
related:
  - rust-operator-expressions
contrasts_with: []
answers_questions:
  - "What are all the pattern types in Rust?"
  - "What is the difference between refutable and irrefutable patterns?"
  - "Where can patterns be used in Rust?"
  - "How do binding modes work (move, ref, ref mut)?"
  - "How does the default binding mode interact with references?"
  - "What is the @ operator in patterns?"
  - "How do or-patterns (|) work?"
  - "What are the rules for range patterns?"
  - "How does structural equality apply to constant patterns?"
  - "What changed about binding modes in the 2024 edition?"
---

# Quick Definition

Patterns match values against structures and optionally bind variables to parts of those structures. Rust has twelve pattern types: literal, identifier, wildcard (`_`), rest (`..`), range, reference, struct, tuple struct, tuple, grouped, slice, and path patterns. Patterns appear in `let` bindings, function parameters, `match` arms, `if let`, `while let`, and `for` loops, and are classified as either refutable (may fail to match) or irrefutable (always match).

# Core Definition

Patterns can **destructure** structs, enums, and tuples, breaking values into component pieces using syntax mirroring construction. The wildcard `_` matches a single field without binding; the rest pattern `..` matches all remaining fields.

**Refutability** is the key classificatory property. Irrefutable patterns always match (required in `let`, function parameters, and `for`). Refutable patterns may fail (allowed in `match` arms, `if let`, `while let`). A pattern is irrefutable if it cannot fail to match for any value of its type.

The twelve pattern types:

1. **Literal patterns** match exact values: `1`, `"hello"`, `true`, `-5`. Always refutable.
2. **Identifier patterns** bind matched values to variables: `x`, `mut x`, `ref x`, `x @ subpattern`. Irrefutable unless the `@` subpattern is refutable. Path patterns take precedence -- a name matching a constant in scope is a path pattern, not an identifier pattern.
3. **Wildcard** (`_`) matches anything without binding. Always irrefutable.
4. **Rest** (`..`) matches zero or more remaining elements in tuples, tuple structs, and slices. May appear only once. Always irrefutable.
5. **Range patterns** match scalar values within bounds: `1..=5` (inclusive), `1..5` (exclusive), `1..` (from), `..5` (to exclusive), `..=5` (to inclusive). Must be nonempty. Irrefutable only when spanning the entire type's range (e.g., `0u8..=255u8`). Bounds can be literals, negated literals, or paths to constants.
6. **Reference patterns** (`&pattern`, `&mut pattern`) dereference the matched value. Always irrefutable.
7. **Struct patterns** match by named fields: `Point { x: 0, y }` (shorthand for `y: y`). Must specify all fields unless `..` is used. Refutable when matching an enum with multiple variants.
8. **Tuple struct patterns** match by position: `Some(x)`, `Color(r, g, b)`. Refutable when the path resolves to a multi-variant enum constructor.
9. **Tuple patterns** match tuples by position: `(a, b, c)`. Refutable if any subpattern is refutable.
10. **Grouped patterns** use parentheses for precedence: `&(0..=5)`. Resolve ambiguity between reference and range patterns.
11. **Slice patterns** match arrays and slices: `[first, .., last]`. Irrefutable for arrays when all elements are irrefutable; for slices, only irrefutable in the form `[..]` or with a single `..` rest pattern.
12. **Path patterns** match constants, unit structs, and enum variants: `None`, `CONSTANT`, `MyEnum::Variant`. Irrefutable only when the path refers to a single-variant enum or struct.

**Or-patterns** (`p | q`) match if either subpattern matches. Both sides must bind the same set of variables with compatible types and binding modes. Or-patterns have the lowest precedence among undelimited patterns.

**Binding modes** determine whether a matched value is moved, copied, or borrowed. The default binding mode starts as "move". When a non-reference pattern matches a reference value, the compiler automatically dereferences and adjusts the binding mode: shared references set it to `ref`, mutable references set it to `ref mut` (unless already `ref`). This is the ergonomic "match ergonomics" feature. In the 2024 edition, explicit `ref`/`ref mut`/`mut` annotations are only allowed when the default binding mode is "move."

**Constant patterns** require the constant's type to implement `PartialEq` and the value to have recursive structural equality: primitive types always qualify; structs/enums qualify only if `PartialEq` is `#[derive]`d and all fields have structural equality. Float `NaN` values are excluded; `NaN` cannot appear as a constant pattern.

# Prerequisites

- **Statements and expressions** -- patterns appear in `let` statements, `match`/`if`/`while` expressions, and function parameters

# Key Properties

1. Patterns in `let` bindings and function parameters must be irrefutable; patterns in `match` arms, `if let`, and `while let` may be refutable
2. The `@` operator binds the matched value to a variable while also matching a subpattern: `e @ 1..=5` binds the value to `e` if it is in range 1-5
3. Default binding modes provide "match ergonomics": matching `&Some(3)` with `Some(x)` automatically makes `x` a `&i32` (as if `ref x`)
4. In the 2024 edition, explicit `ref`, `ref mut`, and `mut` in patterns are only allowed when the default binding mode is "move" -- the compiler prevents redundant or confusing annotations
5. The rest pattern `..` may only appear once per tuple, tuple struct, or slice pattern
6. Struct patterns support field shorthand: `Point { x, y }` is equivalent to `Point { x: x, y: y }`
7. Or-patterns (`A | B`) require both alternatives to bind the same variable names with compatible types; they have the lowest precedence among undelimited patterns
8. Range patterns are exhaustive (irrefutable) when they cover the entire value range: `0u8..=255u8` or `'\u{0}'..='\u{D7FF}'` paired with `'\u{E000}'..='\u{10FFFF}'` for `char`
9. Path patterns take precedence over identifier patterns in ambiguous single-segment cases -- a name matching a constant in scope becomes a path pattern, not a binding
10. Slice patterns can bind subslices: `[first, rest @ ..]` binds `rest` to the remaining elements

# Construction / Recognition

## To destructure a value:
1. Match the structure's shape: `let Point { x, y } = point;` for structs
2. Use `..` to ignore remaining fields: `let Point { x, .. } = point;`
3. Nest patterns: `let Some(Point { x, .. }) = opt_point else { return; };`

## To use range patterns:
1. Inclusive: `1..=5` matches 1, 2, 3, 4, 5
2. Exclusive: `1..5` matches 1, 2, 3, 4
3. Half-open: `1..` matches 1 and above; `..5` matches below 5; `..=5` matches up to and including 5
4. Bounds can be constants: `TROPOSPHERE_MIN..=TROPOSPHERE_MAX`

## To match ergonomically with references:
1. When matching `&Option<i32>`, write `Some(x)` instead of `&Some(ref x)` -- the compiler adjusts automatically
2. The 2024 edition disallows mixing explicit `ref`/`mut` with auto-adjusted binding modes

# Context & Application

Patterns are one of Rust's most powerful features, enabling concise, type-safe deconstruction of complex data. The `match` expression with patterns replaces both `switch` statements and visitor patterns from other languages. Pattern matching on enums is exhaustive -- the compiler verifies all variants are handled. Binding modes and match ergonomics (introduced in Rust 1.26) significantly reduce boilerplate when matching borrowed values. The 2024 edition tightens the rules further to prevent confusing combinations of explicit and implicit binding mode annotations. Or-patterns enable combining multiple match arms without duplicating the body, and the distributive law means `Enum::A(x) | Enum::B(x)` covers both variants while binding `x` from either.

# Examples

**Example 1** (Ch. 9, "Identifier patterns"): Binding with `@` subpattern:
```rust
let x = 2;
match x {
    e @ 1..=5 => println!("got a range element {}", e),
    _ => println!("anything"),
}
```

**Example 2** (Ch. 9, "Binding modes"): Automatic reference binding (match ergonomics):
```rust
let x: &Option<i32> = &Some(3);
if let Some(y) = x {
    // y was automatically converted to &i32 (as if `ref y`)
}
```

**Example 3** (Ch. 9, "Slice patterns"): Matching slices with rest patterns:
```rust
let words = vec!["a", "b", "c"];
match &words[..] {
    [] => println!("empty"),
    [one] => println!("single: {}", one),
    [head, tail @ ..] => println!("head={} tail={:?}", head, tail),
}
```

**Example 4** (Ch. 9, "Destructuring"): Destructuring an enum with field shorthand:
```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    ChangeColor(u8, u8, u8),
}
match message {
    Message::Quit => println!("Quit"),
    Message::Move { x, y: 0 } => println!("move {} horizontally", x),
    Message::Move { .. } => println!("other move"),
    Message::ChangeColor { 0: red, 1: green, 2: _ } => {
        println!("red: {}, green: {}", red, green);
    }
}
```

# Relationships

## Builds Upon
- **rust-statements-and-expressions** -- patterns are used in `let` statements, `match`/`if let`/`while let` expressions, and function/closure parameters

## Enables
- None explicitly

## Related
- **rust-operator-expressions** -- destructuring assignment uses pattern-like syntax on the left side of `=`

## Contrasts With
- None explicitly

# Common Errors

- **Error**: Using a refutable pattern in a `let` binding without `else`: `let Some(x) = opt;`.
  **Correction**: Use `let Some(x) = opt else { return; };` (with a diverging else block) or use `if let Some(x) = opt { ... }`.

- **Error**: Forgetting that a single-segment identifier matching a constant in scope becomes a path pattern, not a binding: `match x { MY_CONST => ... }` matches the constant's value, not any value.
  **Correction**: If you want to bind the value to a variable, choose a name that does not shadow a constant. If you want to match the constant, this is correct behavior -- just be aware of it.

- **Error**: Writing `[1.., _]` in a slice pattern -- `RangeFromPattern` is not allowed as a top-level subpattern in slice patterns.
  **Correction**: Enclose the range in parentheses if needed, or restructure the match.

# Common Confusions

- **Confusion**: Thinking `_` and `..` are interchangeable in patterns.
  **Clarification**: `_` matches and ignores a single field or element. `..` matches zero or more remaining fields/elements and may only appear once. In `Point { x: _, .. }`, the `_` ignores one field and `..` ignores the rest.

- **Confusion**: Thinking `ref` in a pattern means the same as `&` in a pattern.
  **Clarification**: `ref x` binds `x` as a reference to the matched value (creating a borrow). `&x` is a reference pattern that dereferences the matched value (destructuring a reference). They work in opposite directions: `ref` creates a reference from a value; `&` matches an existing reference.

- **Confusion**: Expecting `match` to fall through like C's `switch`.
  **Clarification**: Rust `match` arms do not fall through. Each arm is independent. Use or-patterns (`A | B => ...`) to handle multiple patterns with the same body.

# Source Reference

Chapter 9 of The Rust Reference: "Patterns" (1071 lines). Covers all twelve pattern types (literal, identifier, wildcard, rest, range, reference, struct, tuple struct, tuple, grouped, slice, path), or-patterns, destructuring, refutability, binding modes with 2024 edition changes, and constant pattern structural equality requirements.

# Verification Notes

- Definition source: Directly from Chapter 9 of The Rust Reference, covering the complete pattern type taxonomy
- Key Properties: All derived from explicit rule identifiers (r[patterns.refutable], r[patterns.ident.binding], r[patterns.range], r[patterns.const.structural-equality], r[patterns.or])
- Confidence rationale: HIGH -- authoritative language reference with formal grammar productions and precise semantics
- Uncertainties: The 2024 edition binding mode restrictions (r[patterns.ident.binding.mode-limitations.edition2024]) are relatively new and may see refinement
- Cross-reference status: rust-statements-and-expressions and rust-operator-expressions are companion cards in this extraction set
