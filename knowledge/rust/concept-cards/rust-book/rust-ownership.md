---
# === CORE IDENTIFICATION ===
concept: Ownership, Borrowing, References, and Slices
slug: rust-ownership

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: memory-management
tier: foundational

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Understanding Ownership"
chapter_number: 4
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rust ownership"
  - "Rust borrowing"
  - "Rust references"
  - "Rust slices"
  - "move semantics"
  - "borrow checker"
  - "Rust memory safety"
  - "Copy trait"
  - "Clone trait"
  - "dangling references"
  - "string slices"
  - "&str"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-variables-and-mutability
  - rust-functions-and-control-flow
extends: []
related:
  - rust-book-first-concepts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is ownership in Rust and what are the three ownership rules?"
  - "What is the difference between the stack and the heap, and why does it matter for ownership?"
  - "What happens when you assign a heap-allocated value to another variable (move vs. copy)?"
  - "What is the difference between move, clone, and copy in Rust?"
  - "What are references and how does borrowing work?"
  - "What are the rules of references in Rust?"
  - "What is a mutable reference and what restrictions does it have?"
  - "How does Rust prevent dangling references?"
  - "What are slices and how do string slices (&str) work?"
  - "What types implement the Copy trait?"
  - "How do ownership and functions interact?"
  - "What is the drop function and when is it called?"
---

# Quick Definition

Ownership is Rust's defining feature for memory safety without garbage collection. Three rules govern it: each value has exactly one owner, there can be only one owner at a time, and the value is dropped when the owner goes out of scope. Assigning heap data to another variable _moves_ it (invalidating the original); stack-only types with `Copy` are duplicated instead. References (`&T` and `&mut T`) allow borrowing without taking ownership, subject to two constraints: you may have either one mutable reference or any number of immutable references (never both), and references must always be valid (no dangling). Slices are references to contiguous subsequences of collections, providing safe views into data without ownership.

# Core Definition

**Ownership** is "a set of rules that govern how a Rust program manages memory" (Ch. 4). Rust uses a third approach beyond garbage collection and manual allocation: "Memory is managed through a system of ownership with a set of rules that the compiler checks. If any of the rules are violated, the program won't compile. None of the features of ownership will slow down your program while it's running."

The three ownership rules are stated explicitly:
1. "Each value in Rust has an _owner_."
2. "There can only be one owner at a time."
3. "When the owner goes out of scope, the value will be dropped." (Ch. 4)

When the owner goes out of scope, "Rust calls a special function for us. This function is called `drop`" (Ch. 4). This is similar to C++'s RAII pattern.

**Move semantics**: When a `String` is assigned to another variable (`let s2 = s1;`), Rust copies the pointer, length, and capacity on the stack but does NOT copy the heap data. Critically, "after the line `let s2 = s1;`, Rust considers `s1` as no longer valid" (Ch. 4). This prevents double-free errors. "Instead of being called a shallow copy, it's known as a _move_." Consequence: "Rust will never automatically create 'deep' copies of your data. Therefore, any _automatic_ copying can be assumed to be inexpensive."

**Clone**: "If we _do_ want to deeply copy the heap data of the `String`, not just the stack data, we can use a common method called `clone`" (Ch. 4). "When you see a call to `clone`, you know that some arbitrary code is being executed and that code may be expensive."

**Copy trait**: Types stored entirely on the stack (known size at compile time) implement `Copy` and are duplicated rather than moved. "If a type implements the `Copy` trait, variables that use it do not move, but rather are trivially copied" (Ch. 4). Copy types include: all integer types, `bool`, all floating-point types, `char`, and tuples containing only `Copy` types. "Rust won't let us annotate a type with `Copy` if the type, or any of its parts, has implemented the `Drop` trait."

**References and borrowing**: "A reference is like a pointer in that it's an address we can follow to access the data stored at that address; that data is owned by some other variable. Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference" (Ch. 4). "We call the action of creating a reference _borrowing_."

The two rules of references:
1. "At any given time, you can have _either_ one mutable reference _or_ any number of immutable references."
2. "References must always be valid." (Ch. 4)

The restriction on mutable references prevents **data races** at compile time. A data race occurs when: "Two or more pointers access the same data at the same time," "At least one of the pointers is being used to write to the data," and "There's no mechanism being used to synchronize access to the data" (Ch. 4).

**Reference scope**: "A reference's scope starts from where it is introduced and continues through the last time that reference is used" (Ch. 4). This means immutable and mutable references can coexist if their usage periods don't overlap.

**Dangling references**: "The compiler guarantees that references will never be dangling references: If you have a reference to some data, the compiler will ensure that the data will not go out of scope before the reference to the data does" (Ch. 4).

**Slices**: "_Slices_ let you reference a contiguous sequence of elements in a collection. A slice is a kind of reference, so it does not have ownership" (Ch. 4). String slices (`&str`) store a pointer to the starting position and a length. "String literals are immutable; `&str` is an immutable reference" -- string literals are themselves slices pointing into the program binary. Idiomatic Rust functions accept `&str` rather than `&String` for maximum flexibility via deref coercions.

# Prerequisites

- **rust-variables-and-mutability** -- understanding of types, scope, stack-allocated data (scalars, tuples, arrays), and the `String` type
- **rust-functions-and-control-flow** -- understanding of function parameters, return values, and scopes

# Key Properties

1. **Three ownership rules**: (a) each value has one owner, (b) only one owner at a time, (c) value dropped when owner leaves scope
2. **Stack vs. heap**: Fixed-size data lives on the stack (fast, LIFO); dynamic data lives on the heap (requires allocation, accessed via pointers). "The main purpose of ownership is to manage heap data" (Ch. 4)
3. **Move**: Assigning heap data (`String`, etc.) invalidates the source variable. "Any _automatic_ copying can be assumed to be inexpensive"
4. **Clone**: Explicit deep copy of heap data. Visual indicator that potentially expensive work is happening
5. **Copy**: Stack-only types are trivially duplicated on assignment. `Copy` and `Drop` are mutually exclusive
6. **`drop` function**: Called automatically when owner goes out of scope. Reassigning a variable drops the old value immediately
7. **Immutable references** (`&T`): Multiple allowed simultaneously; borrower cannot modify the data
8. **Mutable references** (`&mut T`): Only one allowed at a time; no immutable references may coexist while the mutable reference is active
9. **No dangling**: The compiler ensures referenced data outlives the reference (enforced via lifetimes, covered in Ch. 10)
10. **String slices** (`&str`): Reference to a contiguous range of a `String`, with `[start..end]` syntax. String literals have type `&str`
11. **Array slices** (`&[T]`): Same concept for arrays -- `&a[1..3]` has type `&[i32]`
12. **Idiomatic parameter types**: Functions should accept `&str` instead of `&String` to work with both string slices and `String` references (via deref coercion)
13. **Ownership and functions**: Passing a value to a function moves or copies it (same rules as assignment). Returning a value transfers ownership to the caller

# Construction / Recognition

## Move semantics (heap data):
```rust
let s1 = String::from("hello");
let s2 = s1;       // s1 is MOVED to s2
// println!("{s1}"); // ERROR: value borrowed here after move
println!("{s2}");   // OK: s2 owns the data
```

## Clone (explicit deep copy):
```rust
let s1 = String::from("hello");
let s2 = s1.clone();  // heap data is duplicated
println!("{s1}");      // OK: s1 is still valid
```

## Copy (stack data):
```rust
let x = 5;
let y = x;        // x is COPIED (i32 implements Copy)
println!("{x}");   // OK: x is still valid
```

## References and borrowing:
```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}  // s goes out of scope, but it doesn't own what it refers to -- no drop

let s1 = String::from("hello");
let len = calculate_length(&s1);  // s1 is borrowed, not moved
println!("{s1} has length {len}"); // s1 still valid
```

## Mutable references:
```rust
fn change(some_string: &mut String) {
    some_string.push_str(", world");
}

let mut s = String::from("hello");
change(&mut s);  // s must be declared mut; reference must be &mut
```

## String slices:
```rust
let s = String::from("hello world");
let hello = &s[0..5];    // or &s[..5]
let world = &s[6..11];   // or &s[6..]
let full = &s[..];       // slice of entire string

// Idiomatic function signature:
fn first_word(s: &str) -> &str { /* ... */ }
```

# Context & Application

- **Ownership is Rust's defining feature**: "Ownership is Rust's most unique feature and has deep implications for the rest of the language. It enables Rust to make memory safety guarantees without needing a garbage collector" (Ch. 4)
- **No runtime cost**: All ownership checks happen at compile time. "None of the features of ownership will slow down your program while it's running"
- **Prevents data races**: The mutable reference restriction "allows for mutation but in a very controlled fashion" -- Rust "can prevent data races at compile time" (Ch. 4)
- **Eliminates use-after-free**: Move semantics ensure invalidated variables cannot be used
- **Eliminates double-free**: Only one owner exists, so only one `drop` is called
- **Eliminates dangling pointers**: The compiler ensures references never outlive their data
- **Slices tie references to data**: Unlike returning an index (which can become stale), slices maintain a compile-time connection to the underlying data, preventing stale-index bugs
- **C++ analogy**: The `drop` function pattern is "sometimes called _Resource Acquisition Is Initialization (RAII)_" (Ch. 4)

# Examples

**Example 1** (Ch. 4): Ownership transferred through function calls:
```rust
fn takes_ownership(some_string: String) {
    println!("{some_string}");
}  // some_string is dropped here

fn makes_copy(some_integer: i32) {
    println!("{some_integer}");
}  // some_integer goes out of scope -- nothing special (Copy type)

let s = String::from("hello");
takes_ownership(s);   // s is moved into the function
// s is no longer valid here

let x = 5;
makes_copy(x);        // x is copied into the function
// x is still valid here
```

**Example 2** (Ch. 4): The borrowing rules prevent simultaneous mutable and immutable references:
```rust
let mut s = String::from("hello");
let r1 = &s;      // OK: first immutable reference
let r2 = &s;      // OK: second immutable reference
println!("{r1} and {r2}");
// r1 and r2 are no longer used after this point

let r3 = &mut s;  // OK: mutable reference, but only after r1/r2's last use
println!("{r3}");
```

**Example 3** (Ch. 4): Slices prevent stale-index bugs:
```rust
let mut s = String::from("hello world");
let word = first_word(&s);  // word is an immutable reference (&str)
// s.clear();               // ERROR: cannot borrow s as mutable
//                          // because it's also borrowed as immutable (by word)
println!("the first word is: {word}");
```
"Not only has Rust made our API easier to use, but it has also eliminated an entire class of errors at compile time!" (Ch. 4).

**Example 4** (Ch. 4): Scope and immediate drop on reassignment:
```rust
let mut s = String::from("hello");
s = String::from("ahoy");
// The original "hello" String is dropped immediately when replaced
println!("{s}, world!");  // prints: ahoy, world!
```

# Relationships

## Builds Upon
- **rust-variables-and-mutability** -- variable binding, scope, stack vs. heap (arrays vs. vectors), `String` type
- **rust-functions-and-control-flow** -- function parameters and return values as mechanisms for ownership transfer

## Enables
- **Structs and methods** (Ch. 5) -- struct fields are subject to ownership rules; methods borrow `self` or take ownership
- **Enums** (Ch. 6) -- enum variants can hold owned data or references
- **Generics, traits, and lifetimes** (Ch. 10) -- lifetimes are the mechanism underlying "references must always be valid"
- **Smart pointers** (Ch. 15) -- `Box`, `Rc`, `RefCell` build on ownership to enable patterns like shared ownership and interior mutability
- **Concurrency** (Ch. 16) -- ownership rules prevent data races, enabling "fearless concurrency"

## Related
- **rust-book-first-concepts** -- introduces `&` references and `&mut` references in the guessing game

## Contrasts With
- None within this source (though implicitly contrasts with GC-based languages and manual memory management in C/C++)

# Common Errors

- **Error**: Using a variable after it has been moved.
  **Correction**: Either clone the value before the move, restructure code to use references, or accept that the original variable is no longer valid.

- **Error**: Trying to have both a mutable reference and an immutable reference active at the same time.
  **Correction**: Ensure immutable references are last used before the mutable reference is created. "A reference's scope starts from where it is introduced and continues through the last time that reference is used" (Ch. 4).

- **Error**: Returning a reference to a locally-created value (dangling reference).
  **Correction**: Return the owned value directly instead of a reference. The compiler error message will say: "this function's return type contains a borrowed value, but there is no value for it to be borrowed from" (Ch. 4).

- **Error**: Creating two mutable references to the same data in the same scope.
  **Correction**: Use separate scopes (curly brackets) to ensure the first mutable borrow ends before the second begins.

- **Error**: Modifying a `String` while a slice (`&str`) into it is still in use.
  **Correction**: The slice is an immutable borrow, so mutation (which requires mutable borrow) is not allowed until the slice is no longer used. This is by design: it prevents stale references.

# Common Confusions

- **Confusion**: Move is the same as shallow copy.
  **Clarification**: A move copies the stack data (pointer, length, capacity) like a shallow copy, but it also _invalidates the source variable_. "Instead of being called a shallow copy, it's known as a _move_" (Ch. 4). A shallow copy in other languages leaves both variables valid; Rust does not.

- **Confusion**: All types are moved on assignment.
  **Clarification**: Types implementing `Copy` (all scalars, `bool`, `char`, and tuples of `Copy` types) are trivially duplicated, not moved. "There's no difference between deep and shallow copying here" (Ch. 4).

- **Confusion**: References are the same as pointers.
  **Clarification**: "A reference is like a pointer... Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference" (Ch. 4). References carry compile-time safety guarantees that raw pointers do not.

- **Confusion**: `&String` and `&str` are interchangeable in function signatures.
  **Clarification**: `&str` is more general -- it accepts both string slices and `String` references (via deref coercion). "Defining a function to take a string slice instead of a reference to a `String` makes our API more general and useful without losing any functionality" (Ch. 4).

- **Confusion**: The borrow checker is purely about lifetime scoping.
  **Clarification**: The borrow checker enforces two distinct rules: (1) mutual exclusivity of mutable and immutable references, and (2) that references don't outlive their data. Both rules work together to prevent data races and use-after-free bugs.

# Source Reference

Chapter 4: Understanding Ownership (1138 lines). Three sections: "What Is Ownership?" (covers stack/heap, ownership rules, scope, `String` type, memory allocation, move/clone/copy, ownership with functions, return values), "References and Borrowing" (covers immutable/mutable references, borrowing rules, data race prevention, dangling references), and "The Slice Type" (covers string slices, `&str` type, string literals as slices, array slices, and idiomatic function signatures).

# Verification Notes

- Definition source: All three ownership rules and both reference rules quoted verbatim from Chapter 4
- Key Properties: All 13 items directly supported by explicit source text
- Confidence rationale: HIGH -- this is the canonical source for Rust's defining feature, with thorough and explicit treatment
- Uncertainties: None -- ownership is comprehensively covered
- Cross-reference status: Related slugs reference cards within this extraction set; forward references to chapters 5, 6, 10, 15, 16 noted in Relationships
