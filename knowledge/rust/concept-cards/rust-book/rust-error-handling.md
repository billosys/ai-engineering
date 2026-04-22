---
concept: Rust Error Handling
slug: rust-error-handling
category: language-fundamentals
subcategory: error-handling
tier: foundational
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "09 - Error Handling"
chapter_number: 9
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "error handling"
  - "panic!"
  - "Result"
  - "Result<T, E>"
  - "unwrap"
  - "expect"
  - "? operator"
  - "error propagation"
  - "recoverable errors"
  - "unrecoverable errors"
  - "custom types for validation"
prerequisites:
  - rust-enums-and-matching
  - rust-module-system
extends: []
related:
  - rust-enums-and-matching
  - rust-collections
contrasts_with: []
answers_questions:
  - "What is the difference between recoverable and unrecoverable errors in Rust?"
  - "When should I use panic! vs. Result?"
  - "How does the ? operator work for error propagation?"
  - "What is the difference between unwrap and expect?"
  - "Can the ? operator be used with Option<T>?"
  - "How do I match on different error kinds?"
  - "Can main return a Result?"
  - "What is unwinding vs. aborting on panic?"
  - "How do I create custom types for validation?"
  - "When is it appropriate to use unwrap or expect in production code?"
  - "How does the ? operator convert between error types?"
---

# Quick Definition

Rust groups errors into two categories: unrecoverable errors handled by the `panic!` macro (which stops execution, unwinds the stack, and cleans up), and recoverable errors handled by the `Result<T, E>` enum (`Ok(T)` for success, `Err(E)` for failure). The `?` operator provides concise error propagation by returning `Err` values early and converting error types via the `From` trait. Rust has no exceptions; the type system enforces error handling at compile time.

# Core Definition

Rust distinguishes **recoverable errors** (file not found, invalid input) from **unrecoverable errors** (index out of bounds, invariant violation). Most languages use exceptions for both; Rust uses `Result<T, E>` for recoverable errors and `panic!` for unrecoverable ones. This distinction is encoded in the type system, not left to convention.

**`panic!`** stops program execution. By default, it **unwinds** the stack (walks back, cleaning up each frame's data). Setting `panic = 'abort'` in `Cargo.toml` switches to immediate abort without cleanup, producing smaller binaries. Use `RUST_BACKTRACE=1` to display the call stack when a panic occurs. Panics can originate from explicit `panic!()` calls or from operations like out-of-bounds vector indexing.

**`Result<T, E>`** is an enum: `Ok(T)` holds a success value, `Err(E)` holds an error value. Both `Result` and its variants are in the prelude. Handle with `match`, closures (`unwrap_or_else`), or shortcuts. **`unwrap()`** returns the `Ok` value or panics on `Err`. **`expect(msg)`** does the same but includes a custom panic message -- preferred in production code because it provides context. For matching on specific error kinds, use methods like `.kind()` on `io::Error` to get an `io::ErrorKind` enum value.

**Error propagation** is the pattern of returning errors to the caller rather than handling them locally. The **`?` operator** placed after a `Result` expression returns the `Ok` value if successful, or returns early from the function with the `Err` value if not. Crucially, `?` calls the `From` trait's `from()` function on the error, automatically converting the received error type into the function's return error type. This allows a function returning `Result<T, OurError>` to use `?` on operations returning different error types, provided `From<TheirError> for OurError` is implemented.

The `?` operator also works with **`Option<T>`**: it returns `None` early from a function returning `Option`, or extracts the `Some` value. You cannot mix `?` on `Result` and `Option` in the same function; use `.ok()` or `.ok_or()` to convert between them.

**`main` can return `Result<(), Box<dyn Error>>`**, allowing the use of `?` in the main function. `Box<dyn Error>` is a trait object meaning "any kind of error." When `main` returns `Ok(())`, the executable exits with code 0; when it returns `Err`, it exits with a nonzero code.

**Guidelines for panic vs. Result**: Return `Result` as the default for functions that might fail. Use `panic!` in examples, prototypes, and tests. Use `expect` when you have logic proving an `Ok` is guaranteed but the compiler cannot verify it (e.g., parsing a hardcoded valid string). Panic when your code reaches a **bad state** -- a broken assumption, guarantee, contract, or invariant -- especially when continuing could be insecure or harmful. When failure is expected (malformed input, rate limits), return `Result`.

**Custom types for validation**: Instead of repeating range checks throughout code, create a type (like `Guess`) whose constructor validates the input and panics on invalid values. The private field plus public getter pattern ensures that instances are always valid, and function signatures can declare the constraint (accepting `Guess` instead of `i32`). This leverages the type system to enforce invariants at compile time.

# Prerequisites

- **Enums and matching** (Ch. 6): `Result<T, E>` is an enum; `match` and `if let` are the primary ways to handle it. `Option<T>` patterns also apply.
- **Module system** (Ch. 7): Custom validation types use modules and privacy to enforce invariants (private fields, public getters).

# Key Properties

1. Rust has no exceptions; it uses `Result<T, E>` for recoverable errors and `panic!` for unrecoverable ones
2. `panic!` unwinds by default; set `panic = 'abort'` in `Cargo.toml` for immediate abort
3. `RUST_BACKTRACE=1` shows the call stack on panic; debug symbols must be enabled
4. `Result<T, E>`, `Ok`, and `Err` are in the prelude; no import needed
5. `unwrap()` panics on `Err` with a generic message; `expect(msg)` panics with a custom message
6. `expect` is preferred over `unwrap` in production because it provides context for debugging
7. The `?` operator returns `Ok` values and propagates `Err` values early from the function
8. `?` calls `From::from()` on the error, converting it to the function's return error type
9. `?` can only be used in functions returning `Result`, `Option`, or types implementing `FromResidual`
10. `?` works on `Option<T>` (returns `None` early); you cannot mix `?` on `Result` and `Option` in one function
11. `main` can return `Result<(), Box<dyn Error>>` to use `?` at the top level
12. Return `Result` by default; use `panic!` for bugs, broken invariants, and bad states
13. Custom validation types (private field + `new()` that panics on invalid input + getter) enforce invariants through the type system

# Construction / Recognition

## Handling Unrecoverable Errors

1. Call `panic!("message")` to halt execution with a message
2. Set `RUST_BACKTRACE=1` to see the full call stack
3. Add `panic = 'abort'` to `[profile.release]` in `Cargo.toml` for smaller binaries
4. Read backtraces from the top until you see your own files

## Handling Recoverable Errors with Result

1. Use `match` on a `Result` to handle `Ok(value)` and `Err(error)` separately
2. Match on `error.kind()` (for `io::Error`) to handle specific error variants differently
3. Use `.unwrap()` for quick prototyping; switch to `.expect("reason")` for production code
4. Use `unwrap_or_else(|e| { ... })` for inline error-handling closures

## Propagating Errors with ?

1. Append `?` after a `Result` expression to propagate errors: `File::open("file.txt")?`
2. Chain calls after `?`: `File::open("file.txt")?.read_to_string(&mut s)?`
3. Implement `From<SourceError> for TargetError` to enable automatic error conversion with `?`
4. Use `?` with `Option<T>` in functions that return `Option`
5. Return `Result<(), Box<dyn Error>>` from `main` to use `?` at the top level

## Creating Custom Validation Types

1. Define a struct with a private field in a module: `pub struct Guess { value: i32 }`
2. Implement `pub fn new(value: i32) -> Guess` that panics on invalid input
3. Implement `pub fn value(&self) -> i32` as a getter (no direct field access from outside)
4. Use `Guess` in function signatures to guarantee valid values without repeated checks

# Context & Application

Rust's error handling is one of its most distinctive features. By splitting errors into recoverable (`Result`) and unrecoverable (`panic!`) categories and encoding the distinction in the type system, Rust forces programmers to make explicit decisions about error handling at every call site. This eliminates several classes of bugs: uncaught exceptions, forgotten error checks, and null-related failures.

The `?` operator is syntactic sugar that makes error propagation almost as concise as exceptions but with full type safety. Its automatic `From` conversion means libraries can define their own error types and still compose cleanly with other libraries' errors.

The custom-type-for-validation pattern (the `Guess` example) is a fundamental Rust idiom: use the type system to make invalid states unrepresentable. Rather than checking preconditions at every use site, you validate once at construction time and let the type carry the guarantee. This pattern scales to complex domain validation and is a cornerstone of Rust's approach to correctness.

Error handling works hand-in-hand with `Option<T>` from Chapter 6: both are enums that force explicit handling, both work with `match` and `?`, and both use the same mental model of "handle all possible cases."

# Examples

**Example 1** (Sec. 9.2): Matching on specific error kinds:
```rust
use std::fs::File;
use std::io::ErrorKind;

let greeting_file = match File::open("hello.txt") {
    Ok(file) => file,
    Err(error) => match error.kind() {
        ErrorKind::NotFound => match File::create("hello.txt") {
            Ok(fc) => fc,
            Err(e) => panic!("Problem creating the file: {e:?}"),
        },
        other_error => panic!("Problem opening the file: {other_error:?}"),
    },
};
```

**Example 2** (Sec. 9.2): Error propagation with the ? operator:
```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}

// Even shorter:
fn read_username_from_file_short() -> Result<String, io::Error> {
    let mut username = String::new();
    File::open("hello.txt")?.read_to_string(&mut username)?;
    Ok(username)
}

// Shortest:
fn read_username_from_file_shortest() -> Result<String, io::Error> {
    std::fs::read_to_string("hello.txt")
}
```

**Example 3** (Sec. 9.3): Custom validation type:
```rust
pub struct Guess {
    value: i32,  // private field
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Guess value must be between 1 and 100, got {value}.");
        }
        Guess { value }
    }

    pub fn value(&self) -> i32 {
        self.value
    }
}
```

# Relationships

## Builds Upon
- **rust-enums-and-matching** -- `Result<T, E>` is an enum; `match` is the primary handling mechanism; `Option<T>` patterns directly transfer
- **rust-module-system** -- custom validation types use module privacy (private fields, public constructors)

## Enables
- All subsequent chapters use error handling patterns extensively; `Result` and `?` are pervasive in idiomatic Rust

## Related
- **rust-enums-and-matching** -- `Result` and `Option` are both enums handled with `match`; `?` works on both
- **rust-collections** -- collection access methods return `Option`; vector indexing panics on out-of-bounds (an unrecoverable error)

## Contrasts With
(none)

# Common Errors

- **Error**: Using `unwrap()` throughout production code, causing unhelpful panic messages.
  **Correction**: Use `expect("reason why this should succeed")` instead -- it provides context in the panic message that aids debugging. Better yet, propagate with `?` and let callers decide.

- **Error**: Using `?` in a function that returns `()` instead of `Result` or `Option`.
  **Correction**: The `?` operator can only be used in functions whose return type is compatible with the value `?` is applied to. Change the return type to `Result<(), ErrorType>` or handle the error with `match`.

- **Error**: Mixing `?` on `Result` and `?` on `Option` in the same function.
  **Correction**: A function must return `Result` to use `?` on `Result`, or `Option` to use `?` on `Option`. Convert between them with `.ok()` (Result to Option) or `.ok_or(err)` / `.ok_or_else(|| err)` (Option to Result).

# Common Confusions

- **Confusion**: Thinking `panic!` is like throwing an exception that can be caught.
  **Clarification**: `panic!` is for unrecoverable errors. It unwinds the stack and terminates the thread (or the program, if in the main thread). While `std::panic::catch_unwind` exists, it is not designed for general control flow. Recoverable errors should use `Result`.

- **Confusion**: Believing the `?` operator is just shorthand for `.unwrap()`.
  **Clarification**: `?` does not panic. It returns early from the function with an `Err` value, allowing the caller to handle it. Additionally, `?` performs automatic error type conversion via the `From` trait, which `unwrap` does not.

- **Confusion**: Thinking `expect` and `unwrap` are always bad practice.
  **Clarification**: `expect` is appropriate when you have additional information that guarantees success (e.g., parsing a hardcoded valid string). In tests, `unwrap`/`expect` are fine because test failure via panic is the desired behavior. The guideline is: use `Result` propagation for errors that callers should handle; use `expect` when failure indicates a bug.

# Source Reference

Chapter 9: Error Handling. Section 9.1: Unrecoverable Errors with panic! (unwinding vs. aborting, RUST_BACKTRACE, buffer overread prevention). Section 9.2: Recoverable Errors with Result (match on Result, matching different errors, unwrap/expect shortcuts, error propagation, the ? operator, ? with Option, main returning Result). Section 9.3: To panic! or Not to panic! (examples/prototypes/tests, guidelines for error handling, bad states and contracts, custom types for validation).

# Verification Notes

- Definition source: Direct synthesis from Chapter 9 source (988 lines)
- Key Properties: All items directly stated in the source text
- Confidence rationale: HIGH -- the chapter provides explicit, comprehensive coverage of all error handling features
- Uncertainties: None; this is foundational, well-defined material
- Cross-reference status: Related slugs reference cards in this rust-book extraction set
