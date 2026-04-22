---
concept: Patterns and Matching
slug: rust-patterns-and-matching
category: language-fundamentals
subcategory: control-flow
tier: intermediate
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Patterns and Matching"
chapter_number: 19
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "pattern matching"
  - "destructuring"
  - "refutable patterns"
  - "irrefutable patterns"
  - "match guards"
  - "@ bindings"
  - "pattern syntax"
prerequisites: []
extends: []
related:
  - rust-patterns
contrasts_with: []
answers_questions:
  - "Where can patterns be used in Rust?"
  - "What is the difference between refutable and irrefutable patterns?"
  - "How do you destructure structs, enums, and tuples?"
  - "How do match guards work and what is their precedence with or-patterns?"
  - "What is the difference between _ and a variable name starting with underscore?"
  - "How does the @ operator let you bind and test a value simultaneously?"
  - "How do you ignore remaining fields with .. in patterns?"
  - "Can you nest destructuring patterns across multiple levels?"
  - "Why does if let not check for exhaustiveness?"
  - "How do named variables in match arms shadow outer variables?"
---

# Quick Definition

Patterns are a special syntax in Rust for matching against the structure of types. They appear in six contexts: `match` arms, `let` statements, `if let` expressions, `while let` loops, `for` loops, and function parameters. Patterns are classified as irrefutable (always match, required in `let`/`for`/function parameters) or refutable (may fail to match, used in `match`/`if let`/`while let`). Rust provides a rich pattern syntax including literals, named variables, wildcards (`_`), ranges (`..=`), destructuring of structs/enums/tuples, rest patterns (`..`), or-patterns (`|`), match guards, and `@` bindings.

# Core Definition

**Six places patterns appear:**
1. **`match` arms** -- must be exhaustive; all possibilities covered. `match VALUE { PATTERN => EXPRESSION, ... }`
2. **`let` statements** -- `let PATTERN = EXPRESSION;` (irrefutable only, or use `let...else`)
3. **`if let` expressions** -- can mix `if let`, `else if`, `else if let` chains; not checked for exhaustiveness
4. **`while let` loops** -- loop continues as long as the pattern matches
5. **`for` loops** -- the value after `for` is a pattern (e.g., `for (index, value) in v.iter().enumerate()`)
6. **Function/closure parameters** -- each parameter is a pattern (e.g., `fn foo(&(x, y): &(i32, i32))`)

**Refutability:**
- **Irrefutable patterns** always match (e.g., `x`, `(a, b, c)`). Required in `let`, `for`, and function parameters.
- **Refutable patterns** may fail (e.g., `Some(x)`). Allowed in `match` arms, `if let`, `while let`, `let...else`.
- Using a refutable pattern where irrefutable is required produces a compiler error. Using an irrefutable pattern in `if let` or `let...else` produces a warning.

**Pattern syntax:**
- **Literals**: match exact values (`1`, `"hello"`, `true`)
- **Named variables**: irrefutable, bind any value; variables in `match`/`if let`/`while let` create a new scope and shadow outer variables
- **Multiple patterns**: `|` (or) operator combines alternatives: `1 | 2 | 3 =>`
- **Ranges**: `..=` for inclusive ranges on numeric or char values: `1..=5`, `'a'..='j'`
- **Destructuring**: structs (`Point { x, y }`), enums (matching variant shape), tuples, nested combinations
- **Ignoring values**: `_` ignores entirely (no binding, no ownership transfer); `_x` binds but suppresses unused warnings (still takes ownership); `..` ignores remaining fields/elements
- **Match guards**: `if` condition after pattern in `match` arm; applies to the whole or-pattern (`4 | 5 | 6 if y` means `(4 | 5 | 6) if y`); not checked for exhaustiveness
- **`@` bindings**: `id @ 3..=7` binds the matched value to `id` while also testing the range

# Prerequisites

Understanding of basic Rust types (structs, enums, tuples), ownership, and `match` expressions from earlier chapters.

# Key Properties

1. `match` expressions must be exhaustive -- the compiler enforces that all possible values are covered
2. `if let` does not check for exhaustiveness, unlike `match`, which can lead to missed logic bugs
3. Named variables inside `match` arms shadow outer variables of the same name -- the inner `y` in `Some(y)` is a new binding, not the outer `y`
4. `_` does not bind and does not take ownership; `_s` does bind and takes ownership (important for types that don't implement `Copy`)
5. `..` ignores remaining fields in a struct or elements in a tuple; it must be unambiguous (can only appear once in a tuple pattern)
6. Match guards apply to all alternatives in an or-pattern: `4 | 5 | 6 if y` is `(4 | 5 | 6) if y`, not `4 | 5 | (6 if y)`
7. `@` bindings let you both test a value against a pattern and capture it: `id @ 3..=7` binds the value to `id` if it falls in that range
8. Ranges in patterns (`..=`) work only with numeric and `char` values because the compiler must verify the range is not empty
9. Struct destructuring supports field shorthand: `Point { x, y }` is equivalent to `Point { x: x, y: y }`
10. Nested destructuring works across multiple levels: you can match `Message::ChangeColor(Color::Rgb(r, g, b))` in a single pattern

# Construction / Recognition

## To destructure a struct:
1. Name the struct and use `{ }` with field names: `let Point { x, y } = point;`
2. Match specific field values: `Point { x, y: 0 }` matches when `y` is 0
3. Ignore remaining fields: `Point { x, .. }` extracts only `x`

## To use match guards for complex conditions:
1. Write the pattern: `Some(x)`
2. Add an `if` condition: `Some(x) if x % 2 == 0`
3. Access outer variables in the guard: `Some(n) if n == y` (where `y` is from the outer scope)

## To bind while testing with @:
1. Place `variable @` before a subpattern: `id @ 3..=7`
2. Both the binding and the test happen in one pattern
3. Without `@`, a plain range `3..=7` matches but does not expose the value

# Context & Application

Chapter 19 serves as the comprehensive pattern reference for The Rust Programming Language. It consolidates all pattern syntax introduced piecemeal in earlier chapters (match in Ch 6, if let in Ch 6, for in Ch 3) and adds advanced syntax (match guards, @ bindings, nested destructuring). The chapter emphasizes two key design decisions: Rust's exhaustiveness checking makes `match` safer than switch statements in other languages, and the refutable/irrefutable distinction is enforced at compile time to prevent runtime failures.

The distinction between `_` and `_x` is a subtle but important ownership consideration: `_` truly ignores the value (no ownership transfer), while `_x` binds it (taking ownership). This matters when the value has a destructor or is a non-Copy type.

Match guards extend the expressiveness of patterns beyond what structural matching alone can express, at the cost of losing exhaustiveness checking. The guard's precedence with or-patterns (applying to all alternatives) is a common source of confusion.

# Examples

**Example 1** (Ch. 19, "Destructuring Structs"): Struct field shorthand and literal matching:
```rust
struct Point { x: i32, y: i32 }
let p = Point { x: 0, y: 7 };
match p {
    Point { x, y: 0 } => println!("On the x axis at {x}"),
    Point { x: 0, y } => println!("On the y axis at {y}"),
    Point { x, y } => println!("On neither axis: ({x}, {y})"),
}
```

**Example 2** (Ch. 19, "Match Guards"): Guard applies to entire or-pattern:
```rust
let x = 4;
let y = false;
match x {
    4 | 5 | 6 if y => println!("yes"),  // (4|5|6) if y
    _ => println!("no"),
}
// Prints "no" because y is false for ALL of 4, 5, and 6
```

**Example 3** (Ch. 19, "@ Bindings"): Bind a value while testing a range:
```rust
enum Message { Hello { id: i32 } }
let msg = Message::Hello { id: 5 };
match msg {
    Message::Hello { id: id_variable @ 3..=7 } => {
        println!("Found an id in range: {id_variable}");
    }
    Message::Hello { id: 10..=12 } => println!("In another range"),
    Message::Hello { id } => println!("Some other id: {id}"),
}
```

**Example 4** (Ch. 19, "_ vs _x"): Ownership difference:
```rust
let s = Some(String::from("Hello"));
// if let Some(_s) = s { ... }  // _s takes ownership, s is moved
if let Some(_) = s { /* _ does NOT take ownership */ }
println!("{s:?}"); // s is still valid
```

# Relationships

## Builds Upon
(none -- this chapter is a reference consolidation of pattern syntax introduced throughout the book)

## Enables
- **rust-advanced-features** -- Ch 20 uses patterns in macro definitions where macro patterns mirror value patterns

## Related
- **rust-patterns** -- The Rust Reference's formal specification of all twelve pattern types with binding mode rules

## Contrasts With
(none)

# Common Errors

- **Error**: Using a refutable pattern in a `let` binding: `let Some(x) = option_value;`.
  **Correction**: Use `let Some(x) = option_value else { return; };` (let...else with a diverging block) or use `if let Some(x) = option_value { ... }`.

- **Error**: Using `..` twice in a tuple pattern: `(.., second, ..)`.
  **Correction**: Rust cannot determine which elements to ignore. Restructure the pattern to use `..` only once, with the position unambiguous.

- **Error**: Expecting a match guard to apply only to the last alternative in an or-pattern: writing `4 | 5 | 6 if y` and expecting only `6 if y`.
  **Correction**: The guard applies to the entire or-pattern: `(4 | 5 | 6) if y`. This is by design.

# Common Confusions

- **Confusion**: Thinking `_x` and `_` behave identically in patterns.
  **Clarification**: `_x` still binds and takes ownership (important for non-Copy types). `_` never binds and never takes ownership. For `let _s = some_string;`, the string is moved into `_s`; for `let _ = some_string;`, no move occurs.

- **Confusion**: Expecting named variables in `match` arms to refer to outer variables of the same name.
  **Clarification**: Match arms create a new scope. `Some(y)` in a match arm introduces a new `y` that shadows any outer `y`. To compare against the outer variable, use a match guard: `Some(n) if n == y`.

- **Confusion**: Thinking `if let` chains check for exhaustiveness like `match`.
  **Clarification**: `if let` does not require covering all cases. The compiler will not warn about missing patterns. Use `match` when exhaustiveness is important.

# Source Reference

Chapter 19 of The Rust Programming Language (1039 lines): "Patterns and Matching." Three sections: "All the Places Patterns Can Be Used" (match arms, let, if let, while let, for, function parameters), "Refutability" (irrefutable vs refutable, let...else), "Pattern Syntax" (literals, named variables, multiple patterns, ranges, destructuring structs/enums/tuples/nested, ignoring values with _/`_x`/.., match guards, @ bindings).

# Verification Notes

- Definition source: Directly extracted from Chapter 19 of The Rust Programming Language
- Key Properties: All derived from explicit examples and explanations in the source text
- Confidence rationale: HIGH -- authoritative book by the Rust team with concrete code examples for every pattern type
- Uncertainties: None -- this chapter is a stable reference covering well-established language features
- Cross-reference status: rust-patterns (The Rust Reference) covers the same topic with formal specification detail
