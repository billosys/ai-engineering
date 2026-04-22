---
# === CORE IDENTIFICATION ===
concept: Variables, Mutability, and Data Types
slug: rust-variables-and-mutability

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables-and-types
tier: foundational

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Common Programming Concepts"
chapter_number: 3
pdf_page: null
section: "Variables and Mutability; Data Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust variables"
  - "Rust mutability"
  - "Rust constants"
  - "Rust shadowing"
  - "Rust data types"
  - "Rust scalar types"
  - "Rust compound types"
  - "let bindings"
  - "Rust tuples"
  - "Rust arrays"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-book-overview
extends: []
related:
  - rust-book-first-concepts
  - rust-ownership
  - rust-functions-and-control-flow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do variables and mutability work in Rust?"
  - "What is the difference between immutable variables, mutable variables, and constants?"
  - "What is shadowing and how does it differ from mutability?"
  - "What scalar types does Rust provide?"
  - "What are tuples and arrays in Rust and how do they differ?"
  - "How does Rust handle integer overflow?"
  - "What is the unit type in Rust?"
  - "How does Rust's static type system work with type inference?"
---

# Quick Definition

Rust variables are immutable by default; adding `mut` enables mutation. Constants (`const`) are always immutable, require type annotations, and must be set to constant expressions. Shadowing allows re-declaring a variable with `let`, enabling type changes. Rust is statically typed with two categories of data types: scalar (integers, floats, booleans, characters) and compound (tuples, arrays). The compiler can usually infer types from context, but type annotations are required when multiple types are possible.

# Core Definition

**Variables and mutability**: "By default, variables are immutable. This is one of many nudges Rust gives you to write your code in a way that takes advantage of the safety and easy concurrency that Rust offers" (Ch. 3). The keyword `mut` before a variable name makes it mutable: "Adding `mut` also conveys intent to future readers of the code by indicating that other parts of the code will be changing this variable's value."

**Constants**: "Constants aren't just immutable by default -- they're always immutable" (Ch. 3). Three key differences from immutable variables: (1) `mut` cannot be used with constants, (2) the type must always be annotated, and (3) constants may only be set to constant expressions, not runtime-computed values. Constants use `SCREAMING_SNAKE_CASE` naming convention and are "valid for the entire time a program runs, within the scope in which they were declared."

**Shadowing**: "You can declare a new variable with the same name as a previous variable" (Ch. 3). The new variable "overshadows the first, taking any uses of the variable name to itself." Shadowing differs from `mut` in two ways: (1) reassigning without `let` produces a compile error, ensuring intentionality, and (2) "because we're effectively creating a new variable when we use the `let` keyword again, we can change the type of the value but reuse the same name."

**Static typing**: "Rust is a _statically typed_ language, which means that it must know the types of all variables at compile time" (Ch. 3). The compiler usually infers types, but annotations are required when multiple types are possible (e.g., `let guess: u32 = "42".parse().expect("Not a number!");`).

# Prerequisites

- **rust-book-overview** -- basic program structure, `fn main()`, and the `let` keyword

# Key Properties

1. **Immutable by default**: `let x = 5;` creates an immutable binding; `let mut x = 5;` creates a mutable one
2. **Constants**: `const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;` -- always immutable, type required, constant expression only, valid for program lifetime within their scope
3. **Shadowing**: `let x = x + 1;` creates a new variable, allowing type changes; scoped to blocks (inner shadowing ends when the scope ends)
4. **Four scalar types**: integers (`i8`/`u8` through `i128`/`u128` plus `isize`/`usize`), floating-point (`f32`, `f64`), boolean (`bool`), and character (`char`, 4 bytes, Unicode scalar value)
5. **Integer defaults**: `i32` is the default integer type; `f64` is the default float type
6. **Integer literal forms**: decimal (`98_222`), hex (`0xff`), octal (`0o77`), binary (`0b1111_0000`), byte (`b'A'`); underscores are visual separators
7. **Integer overflow**: Debug mode panics; release mode wraps (two's complement). Explicit methods: `wrapping_*`, `checked_*`, `overflowing_*`, `saturating_*`
8. **Tuples**: Fixed-length, mixed-type compound; destructured with patterns (`let (x, y, z) = tup;`) or indexed with `.` (`tup.0`). The empty tuple `()` is the _unit_ type
9. **Arrays**: Fixed-length, same-type compound; stack-allocated. Declared as `[i32; 5]` or initialized with `[3; 5]` (five 3s). Bounds-checked at runtime -- invalid access panics
10. **`char` is 4 bytes**: Represents a Unicode scalar value (`U+0000` to `U+D7FF` and `U+E000` to `U+10FFFF`), not just ASCII

# Construction / Recognition

## Variables and Constants:
```rust
let x = 5;                     // immutable variable
let mut y = 5;                 // mutable variable
const MAX_POINTS: u32 = 100;   // constant (type annotation required)
```

## Shadowing with Type Change:
```rust
let spaces = "   ";            // spaces is &str
let spaces = spaces.len();     // spaces is now usize -- type changed via shadowing
```
Using `mut` instead would fail: "we're not allowed to mutate a variable's type" (Ch. 3).

## Compound Types:
```rust
// Tuple: mixed types, fixed length
let tup: (i32, f64, u8) = (500, 6.4, 1);
let (x, y, z) = tup;          // destructuring
let five_hundred = tup.0;     // index access

// Array: same type, fixed length, stack-allocated
let a: [i32; 5] = [1, 2, 3, 4, 5];
let a = [3; 5];               // [3, 3, 3, 3, 3]
let first = a[0];             // index access (bounds-checked)
```

# Context & Application

- **Immutability by default** supports Rust's safety and concurrency goals -- when a value is declared immutable, the compiler guarantees it does not change, making code easier to reason about
- **Shadowing** is commonly used for type conversions (e.g., parsing a string input into a number) without inventing new variable names like `guess_str` and `guess_num`
- **Arrays vs. vectors**: Arrays are for fixed-size, stack-allocated data; vectors (covered in Ch. 8) are heap-allocated and growable. "If you're unsure whether to use an array or a vector, chances are you should use a vector" (Ch. 3)
- **`isize`/`usize`**: Architecture-dependent integer types (32 or 64 bits). "The primary situation in which you'd use `isize` or `usize` is when indexing some sort of collection" (Ch. 3)
- **Memory safety via bounds checking**: Invalid array access panics at runtime rather than allowing undefined behavior -- "Rust protects you against this kind of error by immediately exiting instead of allowing the memory access" (Ch. 3)

# Examples

**Example 1** (Ch. 3): Compile-time error from reassigning an immutable variable:
```rust
let x = 5;
x = 6;  // ERROR: cannot assign twice to immutable variable `x`
```

**Example 2** (Ch. 3): Shadowing with inner scope:
```rust
let x = 5;
let x = x + 1;           // x is 6
{
    let x = x * 2;       // x is 12 inside this scope
    println!("{x}");      // prints 12
}
println!("{x}");          // prints 6 -- inner shadowing ended
```

**Example 3** (Ch. 3): Integer overflow handling methods:
```rust
// wrapping_*: wrap around on overflow
// checked_*: return None on overflow
// overflowing_*: return (value, bool) indicating overflow
// saturating_*: clamp to min/max value
```

**Example 4** (Ch. 3): Runtime panic on invalid array access:
```rust
let a = [1, 2, 3, 4, 5];
let index = 10;
let element = a[index];  // PANICS: index out of bounds: the len is 5 but the index is 10
```

# Relationships

## Builds Upon
- **rust-book-overview** -- introduces `let`, `fn main()`, semicolons

## Enables
- **rust-ownership** -- ownership rules build directly on understanding of variable binding, scope, and stack vs. heap data
- **rust-functions-and-control-flow** -- functions use these types as parameters and return values

## Related
- **rust-book-first-concepts** -- introduces `let`, `mut`, and shadowing in the guessing game context

## Contrasts With
- None within this source

# Common Errors

- **Error**: Trying to reassign an immutable variable without `let`.
  **Correction**: Either add `mut` to the original declaration, or use `let` to shadow the variable with a new value.

- **Error**: Using `mut` and expecting to change a variable's type.
  **Correction**: "We're not allowed to mutate a variable's type" (Ch. 3). Use shadowing with `let` instead.

- **Error**: Relying on integer overflow wrapping behavior in release mode.
  **Correction**: "Relying on integer overflow's wrapping behavior is considered an error" (Ch. 3). Use explicit methods (`wrapping_add`, `checked_add`, etc.) to handle overflow intentionally.

- **Error**: Accessing an array index beyond its length.
  **Correction**: Rust panics at runtime on out-of-bounds access. Use bounds checking or iterate with `for` loops to avoid index errors.

# Common Confusions

- **Confusion**: Immutable variables and constants are the same thing.
  **Clarification**: Three differences: (1) constants cannot use `mut`, (2) constants require type annotations, (3) constants can only be set to constant expressions. Also, constants can be declared in global scope; variables cannot.

- **Confusion**: Shadowing is just reassignment.
  **Clarification**: Shadowing creates a brand-new variable. It allows type changes, and the shadowed variable is not affected by the new one (inner-scope shadowing reverts when the scope ends). Reassignment (`=` without `let`) is only allowed on `mut` variables and cannot change the type.

- **Confusion**: `char` and `u8` are the same (both hold "a character").
  **Clarification**: `char` is 4 bytes and holds a Unicode scalar value. `u8` is 1 byte. String bytes and characters are different concepts -- "your human intuition for what a 'character' is may not match up with what a `char` is in Rust" (Ch. 3).

# Source Reference

Chapter 3, sections "Variables and Mutability" and "Data Types" (approximately 600 lines of the 1315-line chapter). Covers immutability, `mut`, constants, shadowing, scalar types (integers with all sizes, floats, bool, char), compound types (tuples with destructuring and indexing, arrays with initialization and bounds checking), integer overflow behavior, and the unit type.

# Verification Notes

- Definition source: Direct quotes from Chapter 3 sections on variables and data types
- Key Properties: All 10 items directly supported by source text
- Confidence rationale: HIGH -- canonical source with explicit, detailed exposition of each concept
- Uncertainties: None
- Cross-reference status: Related slugs reference cards within this extraction set
