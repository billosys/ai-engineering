---
concept: Rust Enums and Pattern Matching
slug: rust-enums-and-matching
category: language-fundamentals
subcategory: data-types
tier: foundational
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "06 - Enums and Pattern Matching"
chapter_number: 6
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "enums"
  - "enum variants"
  - "pattern matching"
  - "match expression"
  - "Option enum"
  - "if let"
  - "let else"
  - "exhaustive matching"
prerequisites:
  - rust-structs
extends: []
related:
  - rust-structs
  - rust-error-handling
  - rust-collections
contrasts_with: []
answers_questions:
  - "How do I define enums in Rust?"
  - "How can enum variants hold data?"
  - "What is the Option<T> enum and why does Rust have no null?"
  - "How does the match expression work?"
  - "What does it mean that match is exhaustive?"
  - "What are catch-all patterns and the _ placeholder?"
  - "When should I use if let instead of match?"
  - "What is let...else and how does it differ from if let?"
  - "Can enums have methods?"
  - "How do match arms bind to values inside enum variants?"
---

# Quick Definition

Enums allow defining a type by enumerating its possible variants, where each variant can optionally hold different types and amounts of data. The `match` expression provides exhaustive pattern matching against enum variants, and the `Option<T>` enum replaces null with a type-safe representation of presence or absence. The `if let` and `let...else` constructs offer concise alternatives to `match` when only one pattern is of interest.

# Core Definition

An **enum** (enumeration) is defined with the `enum` keyword and lists named variants. Variants are namespaced under the enum identifier and accessed with `::` syntax (e.g., `IpAddrKind::V4`). Unlike structs that carry "all of these" fields, enums model "one of a set of possible values."

Enum variants can hold data directly, eliminating the need for a separate struct:
- No data: `Quit`
- Named fields (struct-like): `Move { x: i32, y: i32 }`
- Positional data (tuple-like): `Write(String)`
- Multiple positional values: `ChangeColor(i32, i32, i32)`

Each variant name also becomes a **constructor function** that returns an instance of the enum type. Enums can have **methods** defined in `impl` blocks, just like structs.

**`Option<T>`** is Rust's replacement for null. Defined as `enum Option<T> { None, Some(T) }`, it encodes the concept of a value being present or absent. It is in the prelude along with its variants `Some` and `None`. Because `Option<T>` and `T` are different types, the compiler forces you to handle the `None` case before using the inner value, preventing null-pointer errors at compile time. You must convert an `Option<T>` to a `T` (via `match`, `unwrap`, `if let`, etc.) before performing `T` operations.

The **`match`** expression compares a value against a series of patterns and executes the code for the first matching arm. Each arm consists of a pattern, the `=>` separator, and an expression (or block). The match expression is itself an expression -- the resultant value of the matching arm is the value of the entire `match`. Match arms can **bind to values** inside enum variants, extracting the inner data.

Matches in Rust are **exhaustive**: every possible value must be covered, or the code will not compile. The compiler checks this and reports which patterns are missing. The **catch-all pattern** (a variable name like `other`) matches any remaining values and binds the value. The **`_` placeholder** matches any value without binding it, signaling that the value is intentionally unused. Catch-all arms must come last.

**`if let`** is syntactic sugar for a `match` that handles one pattern and ignores the rest, reducing boilerplate when only one variant matters. It sacrifices exhaustive checking for conciseness. An optional `else` clause handles all non-matching values.

**`let...else`** takes a pattern on the left and an expression on the right. If the pattern matches, the extracted value is bound in the outer scope. If it does not match, the `else` arm must diverge (return, break, continue, or panic), keeping the main function body on the "happy path."

# Prerequisites

- **Structs** (Ch. 5): Enums are the complement to structs for creating custom types. Understanding struct-like syntax helps with named-field variants.

# Key Properties

1. Enum variants are namespaced under the enum name and accessed with `::` syntax
2. Each variant can hold different types and amounts of associated data
3. Variant names act as constructor functions for the enum type
4. Enums can have methods defined in `impl` blocks, just like structs
5. `Option<T>` is in the prelude; `Some` and `None` can be used without the `Option::` prefix
6. `Option<T>` and `T` are different types; you cannot use an `Option<T>` as if it were a `T`
7. `match` is exhaustive: all possible values must be covered or the code will not compile
8. Match arms are evaluated in order; the first matching pattern executes
9. Match arms can bind to the parts of values that match the pattern, extracting inner data
10. The `_` placeholder matches any value without binding it; catch-all arms must be last
11. `if let` sacrifices exhaustive checking for conciseness when only one pattern matters
12. `let...else` binds matched values in the outer scope; the else arm must diverge

# Construction / Recognition

## Defining and Using Enums

1. Use `enum Name { Variant1, Variant2(Type), ... }` to define an enum
2. Create instances with `Name::Variant(data)` -- the variant name is a constructor
3. Use `impl Name { }` to define methods on an enum
4. Use `Option<T>` for values that may be absent -- prefer `Some(value)` and `None` over null-like patterns

## Pattern Matching

1. Write `match value { pattern => expression, ... }` to match against enum variants
2. Each arm: pattern `=>` expression, separated by commas
3. Use curly braces for multi-line arm bodies (the trailing comma is then optional)
4. Bind inner values with variable names in patterns: `Some(i) => i + 1`
5. Cover all variants or use a catch-all (`other` or `_`) as the last arm
6. Use `if let Pattern = expr { body }` when only one variant needs handling
7. Use `let Pattern = expr else { diverge };` to stay on the happy path

# Context & Application

Enums and `match` are central to idiomatic Rust. The `Option<T>` enum eliminates null from the language, shifting null-related bugs from runtime crashes to compile-time errors. This design was a deliberate response to Tony Hoare's "billion-dollar mistake" of null references.

The combination of enums with data and exhaustive `match` enables a powerful pattern: define all possible states as variants, then let the compiler ensure every state is handled. This is fundamental to Rust's error handling (the `Result<T, E>` enum in Chapter 9), state machines, command processing, and protocol design.

The `if let` and `let...else` constructs recognize that full `match` is sometimes verbose when only one variant matters. `let...else` is particularly valuable for early-return patterns in functions, keeping the main logic un-nested.

# Examples

**Example 1** (Sec. 6.1): Enum with data and methods:
```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
impl Message {
    fn call(&self) {
        // method body uses self
    }
}
let m = Message::Write(String::from("hello"));
m.call();
```

**Example 2** (Sec. 6.2): Match with value binding:
```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}
let five = Some(5);
let six = plus_one(five);    // Some(6)
let none = plus_one(None);   // None
```

**Example 3** (Sec. 6.3): if let and let...else:
```rust
// if let: concise single-pattern match
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}

// let...else: happy path with early return
fn describe(coin: &Coin) -> String {
    let Coin::Quarter(state) = coin else {
        return String::from("Not a quarter");
    };
    // state is bound here on the happy path
    format!("Quarter from {state:?}")
}
```

# Relationships

## Builds Upon
- **rust-structs** -- enums are the complement to structs; enum variants can contain struct-like data

## Enables
- **rust-error-handling** -- `Result<T, E>` is an enum; `match` and `?` are the primary ways to handle errors
- **rust-collections** -- `Option<T>` is returned by collection access methods like `Vec::get`

## Related
- **rust-structs** -- both are building blocks for custom types; enums model "one of" while structs model "all of"
- **rust-error-handling** -- `Result` uses the same enum/match pattern as `Option`
- **rust-collections** -- vectors can store multiple types using an enum

## Contrasts With
(none)

# Common Errors

- **Error**: Forgetting to handle all enum variants in a `match` (non-exhaustive match).
  **Correction**: Rust requires exhaustive matching. Add the missing variant arm or use a catch-all pattern (`_` or a variable name) as the last arm.

- **Error**: Trying to use an `Option<T>` value directly as a `T` (e.g., adding `Option<i8>` to `i8`).
  **Correction**: `Option<T>` and `T` are different types. You must extract the value first using `match`, `if let`, `unwrap()`, `expect()`, or other `Option` methods.

- **Error**: Placing the catch-all arm before other specific arms in a `match`.
  **Correction**: Patterns are evaluated in order. A catch-all must come last; otherwise, subsequent arms are unreachable and Rust will warn.

# Common Confusions

- **Confusion**: Thinking Rust has null like other languages.
  **Clarification**: Rust has no null. The `Option<T>` enum (`Some(T)` / `None`) encodes the concept of presence or absence. Because `Option<T>` is a different type from `T`, the compiler forces explicit handling of the `None` case, preventing null-related bugs at compile time.

- **Confusion**: Assuming `if let` and `match` are interchangeable in all cases.
  **Clarification**: `if let` is sugar for a `match` with one pattern plus a wildcard. It sacrifices exhaustive checking -- if you add new variants to an enum later, `match` will force you to handle them but `if let` will silently ignore them.

- **Confusion**: Conflating `if let` with `let...else`.
  **Clarification**: `if let` runs code when the pattern matches (inside the `if` body). `let...else` binds the matched value in the outer scope and requires the `else` arm to diverge (return/break/panic). `let...else` keeps the happy path un-nested; `if let` nests the happy path inside a block.

# Source Reference

Chapter 6: Enums and Pattern Matching. Section 6.1: Defining an Enum (enum values, data in variants, Option<T>, Rust's rejection of null). Section 6.2: The match Control Flow Construct (match arms, patterns binding values, matching Option<T>, exhaustive matching, catch-all and _ placeholder). Section 6.3: Concise Control Flow with if let and let...else (if let syntax, else clause, let...else for happy-path flow).

# Verification Notes

- Definition source: Direct synthesis from Chapter 6 source (765 lines)
- Key Properties: All items directly stated in the source text
- Confidence rationale: HIGH -- the chapter provides explicit, complete coverage of enums, Option, match, if let, and let...else
- Uncertainties: None; this is foundational, well-defined material
- Cross-reference status: Related slugs reference cards in this rust-book extraction set
