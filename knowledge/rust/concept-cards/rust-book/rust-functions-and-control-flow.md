---
# === CORE IDENTIFICATION ===
concept: Functions, Statements, Expressions, and Control Flow
slug: rust-functions-and-control-flow

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: functions-and-flow
tier: foundational

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Common Programming Concepts"
chapter_number: 3
pdf_page: null
section: "Functions; Comments; Control Flow"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust functions"
  - "Rust control flow"
  - "statements vs expressions"
  - "Rust loops"
  - "Rust if expressions"
  - "loop labels"
  - "implicit return"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-variables-and-mutability
extends: []
related:
  - rust-book-first-concepts
  - rust-ownership
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are functions defined and called in Rust?"
  - "What is the difference between statements and expressions in Rust?"
  - "How do function return values work in Rust?"
  - "How do if expressions work in Rust, and how do they differ from if statements in other languages?"
  - "What are the three kinds of loops in Rust?"
  - "How do loop labels work for nested loops?"
  - "Can loops return values in Rust?"
  - "Why is Rust called an expression-based language?"
---

# Quick Definition

Rust functions are declared with `fn`, use snake_case naming, require type annotations on all parameters, and declare return types with `->`. Rust is an expression-based language: statements perform actions without returning values, while expressions evaluate to values. The last expression in a function body (without a semicolon) is implicitly returned. Control flow uses `if` expressions (not statements -- they can return values), and three loop types: `loop` (infinite, can return values via `break`), `while` (conditional), and `for` (iteration over collections, the most commonly used).

# Core Definition

**Functions**: "We define a function in Rust by entering `fn` followed by a function name and a set of parentheses" (Ch. 3). Rust uses snake_case for function and variable names. "Rust doesn't care where you define your functions, only that they're defined somewhere in a scope that can be seen by the caller." In function signatures, "you _must_ declare the type of each parameter" -- this deliberate design decision means "the compiler almost never needs you to use them elsewhere in the code to figure out what type you mean."

**Statements vs. expressions**: "Rust is an expression-based language, this is an important distinction to understand" (Ch. 3). Statements "are instructions that perform some action and do not return a value." Expressions "evaluate to a resultant value." Key consequence: `let y = 6;` is a statement, so `let x = (let y = 6);` is invalid -- unlike C and Ruby where assignment returns a value. Critically, "expressions do not include ending semicolons. If you add a semicolon to the end of an expression, you turn it into a statement, and it will then not return a value."

**Function return values**: "The return value of the function is synonymous with the value of the final expression in the block of the body of a function" (Ch. 3). Return types are declared after `->`. The `return` keyword is available for early returns, "but most functions return the last expression implicitly."

**if expressions**: "Because `if` is an expression, we can use it on the right side of a `let` statement" (Ch. 3). Unlike many languages, "Rust will not automatically try to convert non-Boolean types to a Boolean. You must be explicit and always provide `if` with a Boolean as its condition." When used in a `let` statement, all arms must return the same type.

**Loops**: Rust has three kinds: `loop` (infinite until `break`), `while` (conditional), and `for` (collection iteration). `loop` can return values via `break value;`. Loop labels (e.g., `'counting_up`) disambiguate `break`/`continue` in nested loops. "The safety and conciseness of `for` loops make them the most commonly used loop construct in Rust" (Ch. 3).

# Prerequisites

- **rust-variables-and-mutability** -- understanding of types, `let` bindings, and basic Rust syntax

# Key Properties

1. **`fn` declaration**: `fn name(param: Type) -> ReturnType { body }` -- parameters require type annotations; return type declared with `->`
2. **Statements don't return values**: `let y = 6;` is a statement. `let x = (let y = 6);` is a compile error -- assignments don't return values in Rust
3. **Expressions do return values**: Math operations, function calls, macro calls, and block scopes `{ ... }` are all expressions
4. **Semicolons transform expressions to statements**: Adding `;` to a function's final expression changes the return from the computed value to `()` (unit), causing a type mismatch error
5. **Implicit return**: The last expression (without `;`) in a function body is the return value; `return` is for early exits
6. **`if` is an expression**: `let number = if condition { 5 } else { 6 };` -- arms must have the same type
7. **`if` requires `bool`**: No truthy/falsy conversions -- `if 3 { ... }` is a compile error
8. **`loop` returns values**: `let result = loop { break counter * 2; };`
9. **Loop labels**: `'label: loop { ... break 'label; }` -- labels must start with a single quote; `break` and `continue` default to the innermost loop
10. **`for` is preferred**: Safer than `while` with index (no off-by-one errors) and often more efficient (no bounds checking at each iteration)
11. **Comments**: `//` for line comments; Rust also has documentation comments (covered in Ch. 14)

# Construction / Recognition

## Function with return value (expression-based):
```rust
fn plus_one(x: i32) -> i32 {
    x + 1    // no semicolon: this is an expression, returned implicitly
}
```
Adding a semicolon (`x + 1;`) turns it into a statement returning `()`, causing: "mismatched types -- expected `i32`, found `()`".

## Block expressions:
```rust
let y = {
    let x = 3;
    x + 1    // no semicolon: block evaluates to 4
};
// y is 4
```

## if as expression in let:
```rust
let condition = true;
let number = if condition { 5 } else { 6 };
```

## Loop with return value and label:
```rust
let result = 'outer: loop {
    let mut count = 0;
    loop {
        count += 1;
        if count == 10 {
            break 'outer count * 2;  // breaks outer loop, returns 20
        }
    }
};
```

## for loop with Range:
```rust
for number in (1..4).rev() {
    println!("{number}!");
}
// prints: 3! 2! 1!
```

# Context & Application

- **Expression-based design** makes Rust code compact: `if`/`else` and blocks can produce values directly, reducing the need for temporary variables
- **Mandatory type annotations on parameters** enable better compiler error messages and make function interfaces self-documenting
- **`for` loops over iterators** are both safer (no bounds errors) and often faster (compiler can eliminate bounds checks) than manual indexing with `while`
- **`loop` with `break value`** is useful for retry patterns: "retry an operation you know might fail, such as checking whether a thread has completed its job" (Ch. 3)
- **Semicolon sensitivity** is a common source of confusion for newcomers but reinforces the expression/statement distinction that permeates Rust

# Examples

**Example 1** (Ch. 3): A function that is purely an expression:
```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();
    println!("The value of x is: {x}");  // prints: The value of x is: 5
}
```
"That's a perfectly valid function in Rust" -- the body is just the number `5`, an expression.

**Example 2** (Ch. 3): Multiple parameters with different types:
```rust
fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

**Example 3** (Ch. 3): `else if` chains and the `match` alternative:
```rust
let number = 6;
if number % 4 == 0 {
    println!("divisible by 4");
} else if number % 3 == 0 {
    println!("divisible by 3");    // this prints
} else if number % 2 == 0 {
    println!("divisible by 2");    // NOT reached, even though 6 % 2 == 0
} else {
    println!("not divisible by 4, 3, or 2");
}
```
"Rust only executes the block for the first `true` condition." "Using too many `else if` expressions can clutter your code... Chapter 6 describes a powerful Rust branching construct called `match`" (Ch. 3).

**Example 4** (Ch. 3): Loop label for nested loops:
```rust
'counting_up: loop {
    // inner loop
    loop {
        if condition { break; }              // breaks inner loop only
        if other_condition { break 'counting_up; }  // breaks outer loop
    }
}
```

# Relationships

## Builds Upon
- **rust-variables-and-mutability** -- types used in function signatures and return values

## Enables
- **rust-ownership** -- ownership transfer through function parameters and return values is a core topic in Ch. 4
- **rust-book-first-concepts** -- the guessing game uses `loop`, `break`, `continue`, `match`, and functions

## Related
- **rust-book-first-concepts** -- the guessing game tutorial introduces `loop`/`break`/`continue` and `match` in practice

## Contrasts With
- None within this source

# Common Errors

- **Error**: Adding a semicolon to the final expression in a function, changing the return type to `()`.
  **Correction**: Remove the trailing semicolon. The compiler will suggest this: "consider removing this semicolon" (Ch. 3).

- **Error**: Using `if` with a non-boolean condition (e.g., `if number { ... }`).
  **Correction**: "Rust will not automatically try to convert non-Boolean types to a Boolean" (Ch. 3). Write `if number != 0 { ... }` instead.

- **Error**: `if`/`else` arms returning different types when used in a `let` binding.
  **Correction**: "Variables must have a single type, and Rust needs to know definitively at compile time what type the `number` variable is" (Ch. 3). Both arms must return the same type.

- **Error**: Using `while` with manual index to iterate over an array, then changing the array size without updating the loop bound.
  **Correction**: Use a `for` loop instead: `for element in a { ... }`. This eliminates the chance of index-related bugs.

# Common Confusions

- **Confusion**: `let y = 6` is an expression in Rust (as it is in C/Ruby).
  **Clarification**: In Rust, `let y = 6;` is a statement and does not return a value. You cannot write `x = y = 6` in Rust. The `6` itself is an expression, but the `let` binding is a statement.

- **Confusion**: `return` is required to return values from functions.
  **Clarification**: Most Rust functions use implicit return -- the last expression (without `;`) in the body is returned. `return` is for early exits only.

- **Confusion**: `loop` and `while true` are equivalent.
  **Clarification**: While both can run infinitely, `loop` has additional capabilities: it can return values via `break value`, and the compiler understands that `loop` always runs at least once, which affects type inference and flow analysis.

# Source Reference

Chapter 3, sections "Functions," "Comments," and "Control Flow" (approximately 700 lines of the 1315-line chapter). Covers function declaration and parameters, the statement/expression distinction, implicit returns, `if`/`else if`/`else` as expressions, `loop` with `break` values and labels, `while` loops, `for` loops with iterators and ranges, and `//` comments.

# Verification Notes

- Definition source: Direct quotes from Chapter 3 sections on functions and control flow
- Key Properties: All 11 items directly supported by source text
- Confidence rationale: HIGH -- canonical source with clear exposition and worked examples
- Uncertainties: None
- Cross-reference status: All related slugs reference cards within this extraction set
