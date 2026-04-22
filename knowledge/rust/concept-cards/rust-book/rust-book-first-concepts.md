---
# === CORE IDENTIFICATION ===
concept: First Rust Concepts (via Guessing Game)
slug: rust-book-first-concepts

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: introductory-concepts
tier: foundational

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Programming a Guessing Game"
chapter_number: 2
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust guessing game concepts"
  - "Rust introductory patterns"
  - "let, match, and crates"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-book-overview
extends: []
related:
  - rust-variables-and-mutability
  - rust-ownership
  - cargo-dependencies
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the core concepts introduced in the Rust guessing game tutorial?"
  - "How do let bindings, mutability, and shadowing work in Rust?"
  - "What is the Result type and how does error handling work with expect and match?"
  - "How do you add and use external crates in a Rust project?"
  - "What is the match expression and how does pattern matching work?"
  - "What are associated functions and how are they called?"
  - "How does Rust's type inference and type conversion work?"
---

# Quick Definition

Chapter 2 introduces core Rust concepts through a guessing game: `let` bindings with optional `mut` for mutability, the `String` type and its associated functions, references (`&` and `&mut`), the `Result` enum for error handling (with `Ok`/`Err` variants), `match` expressions for pattern matching, variable shadowing for type conversion, external crate usage via `Cargo.toml`, and `loop`/`break`/`continue` for flow control. These concepts are explored at a high level and treated in depth in subsequent chapters.

# Core Definition

The guessing game tutorial demonstrates Rust's approach to several fundamental programming concepts by building a complete, working program. The key ideas introduced:

**Variables and mutability**: "In Rust, variables are immutable by default" (Ch. 2). To make a variable mutable, add `mut` before the name: `let mut guess = String::new();`. This is a deliberate design choice -- immutability by default encourages safer code.

**Associated functions**: The `::` syntax in `String::new()` "indicates that `new` is an associated function of the `String` type" (Ch. 2). An associated function "is a function that's implemented on a type" rather than on a particular instance.

**References**: "The `&` indicates that this argument is a _reference_, which gives you a way to let multiple parts of your code access one piece of data without needing to copy that data into memory multiple times" (Ch. 2). References, like variables, are immutable by default -- hence `&mut guess` rather than `&guess` when mutation is needed.

**The Result type**: `Result` is "an _enumeration_, often called an _enum_, which is a type that can be in one of multiple possible states" called _variants_. "`Result`'s variants are `Ok` and `Err`" (Ch. 2). The `expect` method crashes on `Err`; `match` enables graceful error handling.

**Match expressions**: "A `match` expression is made up of _arms_. An arm consists of a _pattern_ to match against, and the code that should be run if the value given to `match` fits that arm's pattern" (Ch. 2). Rust evaluates arms in order and executes the first match.

**Shadowing**: "Rust allows us to shadow the previous value of `guess` with a new one. _Shadowing_ lets us reuse the `guess` variable name rather than forcing us to create two unique variables" (Ch. 2). This enables changing a variable's type (e.g., `String` to `u32`) while reusing the name.

# Prerequisites

- **rust-book-overview** -- understanding of Cargo project creation, basic program structure, and `fn main()`

# Key Properties

1. **Immutable by default**: Variables declared with `let` cannot be reassigned; `let mut` enables mutation
2. **String::new()**: Associated functions are called on the type itself using `::`, not on an instance
3. **References avoid copying**: `&` creates a reference; `&mut` creates a mutable reference; both avoid copying data
4. **Result enum**: Functions that can fail return `Result<T, E>` with `Ok(value)` and `Err(error)` variants
5. **expect() panics on error**: Calling `.expect("message")` on an `Err` crashes the program with the given message; on `Ok` it unwraps the value
6. **match for control flow**: Arms are checked in order; the first matching pattern executes; `_` is a catch-all pattern
7. **Shadowing changes types**: `let guess: u32 = guess.trim().parse()...` shadows the `String` `guess` with a `u32` `guess`
8. **External crates**: Added to `[dependencies]` in `Cargo.toml` with semantic version specifiers (e.g., `rand = "0.8.5"`, meaning `^0.8.5`)
9. **Cargo.lock**: Ensures reproducible builds by recording exact dependency versions; `cargo update` refreshes within semver constraints
10. **Prelude**: Rust automatically imports a set of items (the _prelude_) into every program; items not in the prelude require explicit `use` statements

# Construction / Recognition

## Pattern: Handling fallible operations with match:
```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```
This converts `parse()`'s `Result` into either the parsed number or a loop continuation, avoiding a crash on invalid input.

## Pattern: Using external crates:
1. Add to `Cargo.toml`: `rand = "0.8.5"` under `[dependencies]`
2. Bring trait into scope: `use rand::Rng;`
3. Use the functionality: `rand::thread_rng().gen_range(1..=100)`

## Pattern: Type conversion via shadowing:
```rust
let guess = String::new();       // guess is a String
let guess: u32 = guess.trim().parse().expect("Not a number!");  // guess is now u32
```

# Context & Application

- **Error handling strategy**: The progression from `expect()` (crash on error) to `match` on `Result` (graceful handling) introduces Rust's philosophy of making error handling explicit and unavoidable
- **Crate ecosystem**: The tutorial demonstrates that Rust's standard library is intentionally small; external crates (from Crates.io) provide additional functionality like random number generation
- **Type safety**: Comparing a `String` to a number produces a compile-time error -- Rust's strong typing prevents category errors that other languages might silently handle
- **Trait usage preview**: `use rand::Rng;` introduces the concept that traits must be in scope to call their methods, foreshadowing Chapter 10's full treatment

# Examples

**Example 1** (Ch. 2): Reading user input with error handling:
```rust
use std::io;

let mut guess = String::new();
io::stdin()
    .read_line(&mut guess)
    .expect("Failed to read line");
```

**Example 2** (Ch. 2): Comparison using match with the Ordering enum:
```rust
use std::cmp::Ordering;

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Too small!"),
    Ordering::Greater => println!("Too big!"),
    Ordering::Equal => {
        println!("You win!");
        break;
    }
}
```

**Example 3** (Ch. 2): The `println!` macro with placeholders:
```rust
let x = 5;
let y = 10;
println!("x = {x} and y + 2 = {}", y + 2);
// prints: x = 5 and y + 2 = 12
```

# Relationships

## Builds Upon
- **rust-book-overview** -- Cargo project creation, `fn main()`, `println!`, semicolons

## Enables
- **rust-variables-and-mutability** -- Ch. 3 covers variables, mutability, and shadowing in full detail
- **rust-data-types** -- Ch. 3 covers all scalar and compound types
- **rust-ownership** -- references (`&`, `&mut`) are covered thoroughly in Ch. 4

## Related
- **cargo-dependencies** -- Cargo Guide's detailed treatment of dependency management introduced here
- **rust-variables-and-mutability** -- full treatment of `let`, `mut`, constants, shadowing

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting to make a variable mutable before passing it as `&mut` to `read_line`.
  **Correction**: Declare with `let mut guess` -- both the variable and the reference must be mutable.

- **Error**: Not handling the `Result` returned by `read_line` or `parse`.
  **Correction**: Rust warns if you ignore a `Result`. Use `.expect()` for quick prototyping or `match` for proper error handling.

- **Error**: Comparing a `String` directly to a number type.
  **Correction**: Convert types first. Use `parse()` to convert strings to numbers, with a type annotation to tell Rust which numeric type to use.

# Common Confusions

- **Confusion**: Shadowing and mutation are the same thing.
  **Clarification**: `mut` allows changing a variable's value but not its type. Shadowing (re-declaring with `let`) creates a new variable that can have a different type. After shadowing, the original variable is inaccessible.

- **Confusion**: `expect()` is the proper way to handle errors in production code.
  **Clarification**: `expect()` causes a panic (crash) on error. It is useful for prototyping and cases where failure is truly unrecoverable. For graceful error handling, use `match` on the `Result` variants. Chapter 9 covers error handling in depth.

- **Confusion**: The `_` in `Err(_)` means the error is discarded.
  **Clarification**: `_` is a catch-all pattern that matches any value. In `Err(_)`, it means "match any error regardless of its contents." The error information is indeed not bound to a variable, but the pattern still matches.

# Source Reference

Chapter 2: Programming a Guessing Game (951 lines). A project chapter that introduces `let`, `mut`, `String`, references, `Result` enum, `match` expressions, `loop`/`break`/`continue`, shadowing, type annotations, external crate usage, `Cargo.toml` dependencies, `Cargo.lock`, and the `use` statement. Concepts are introduced at a high level with forward references to later chapters.

# Verification Notes

- Definition source: Direct quotes from Chapter 2, with key concepts quoted verbatim
- Key Properties: All 10 items directly supported by Chapter 2 source text
- Confidence rationale: HIGH -- canonical source material; concepts are clearly defined even though this is a tutorial chapter
- Uncertainties: None -- the tutorial introduces concepts explicitly
- Cross-reference status: Related slugs reference cards in this extraction set and the cargo-guide set
