---
concept: Rust Structs
slug: rust-structs
category: language-fundamentals
subcategory: data-types
tier: foundational
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "05 - Using Structs to Structure Related Data"
chapter_number: 5
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "structs"
  - "struct definition"
  - "methods"
  - "associated functions"
  - "tuple structs"
  - "unit-like structs"
  - "impl blocks"
  - "field init shorthand"
  - "struct update syntax"
prerequisites:
  - rust-ownership
extends: []
related:
  - rust-enums-and-matching
  - rust-module-system
contrasts_with: []
answers_questions:
  - "How do I define and instantiate a struct in Rust?"
  - "What are tuple structs and unit-like structs?"
  - "How do I define methods on a struct?"
  - "What are associated functions and how do they differ from methods?"
  - "What is the field init shorthand?"
  - "What is struct update syntax and how does it interact with ownership?"
  - "What is automatic referencing and dereferencing for method calls?"
  - "How do I derive Debug for a struct?"
  - "Can a struct have multiple impl blocks?"
  - "How does ownership work with struct data?"
---

# Quick Definition

A struct is a custom data type that lets you package together and name multiple related values that make up a meaningful group. Rust supports three kinds of structs: classic structs with named fields, tuple structs with positional fields, and unit-like structs with no fields. Methods and associated functions are defined in `impl` blocks, where methods take `self` as their first parameter and associated functions (like constructors) do not.

# Core Definition

A **struct** (structure) is defined with the `struct` keyword followed by a name and curly braces containing named, typed fields. Instances are created by specifying concrete values for each field using `key: value` syntax; fields may appear in any order. The entire instance must be mutable if any field needs mutation -- Rust does not allow marking individual fields as mutable.

The **field init shorthand** allows omitting the field name when a variable with the same name provides the value (e.g., writing `email` instead of `email: email`). **Struct update syntax** (`..other_instance`) fills remaining fields from another instance of the same type; this uses `=` (assignment/move semantics), so fields of non-Copy types are moved and the source instance may become partially or fully invalid.

**Tuple structs** have the struct keyword, a name, and parenthesized types but no named fields. They create distinct types even when their field types match (e.g., `Color(i32, i32, i32)` and `Point(i32, i32, i32)` are different types). Fields are accessed by index (`.0`, `.1`, etc.) and tuple structs can be destructured by naming the type.

**Unit-like structs** have no fields at all and behave like the unit type `()`. They are useful for implementing traits on types that carry no data.

Structs that hold references require **lifetime annotations** (covered in Chapter 10). Without lifetimes, storing references like `&str` in struct fields causes a compiler error (`E0106: missing lifetime specifier`). The common approach for beginners is to use owned types like `String` instead.

**Methods** are functions defined in an `impl` block whose first parameter is `self` (short for `self: Self`). The `self` parameter can be `&self` (immutable borrow), `&mut self` (mutable borrow), or `self` (taking ownership). Rust has **automatic referencing and dereferencing**: when calling `object.method()`, Rust automatically adds `&`, `&mut`, or `*` so that `object` matches the method signature. This works because methods have a clear receiver type.

**Associated functions** are all functions in an `impl` block; those without `self` are not methods and are called using `::` syntax (e.g., `Rectangle::square(3)`). They are commonly used as constructors. A struct may have **multiple `impl` blocks**, which is valid syntax and becomes useful with generic types and traits.

The `#[derive(Debug)]` attribute opts a struct into the `Debug` trait, enabling use with `{:?}` (compact) and `{:#?}` (pretty-printed) format specifiers in `println!`. The `dbg!` macro takes ownership of an expression, prints file/line plus the debug-formatted value to stderr, and returns ownership.

# Prerequisites

- **Ownership and borrowing** (Ch. 4): Struct update syntax moves data; methods borrow `self`. Understanding move semantics and the Copy trait is essential for knowing when a source struct remains valid after update syntax.

# Key Properties

1. Struct field order in the definition does not matter; instances can specify fields in any order
2. The entire instance must be declared `mut` to change any field; per-field mutability is not supported
3. Field init shorthand: when variable name matches field name, omit the field name
4. Struct update syntax (`..instance`) must come last in the struct literal and moves non-Copy fields
5. Each tuple struct definition creates a unique type, even if field types are identical to another tuple struct
6. Tuple structs can be destructured: `let Point(x, y, z) = origin;`
7. Unit-like structs have no fields and no curly braces or parentheses -- just a semicolon
8. Methods can share the name of a field; parentheses distinguish method calls from field access
9. Automatic referencing and dereferencing: Rust infers `&`, `&mut`, or `*` on the receiver of method calls
10. Associated functions without `self` are called with `::` syntax and are commonly used as constructors

# Construction / Recognition

## Defining and Instantiating Structs

1. Use `struct Name { field: Type, ... }` to define a struct with named fields
2. Create instances with `Name { field: value, ... }` -- order does not matter
3. Use dot notation (`instance.field`) to access or mutate fields (if instance is `mut`)
4. Use field init shorthand when parameter/variable names match field names
5. Use `..other` at the end of a struct literal to fill remaining fields from another instance

## Defining Methods and Associated Functions

1. Open an `impl Name { }` block for the struct
2. Define methods with `fn method_name(&self, ...)` as the first parameter
3. Use `&self` for read-only access, `&mut self` for mutation, or `self` to consume the instance
4. Define associated functions (constructors) without `self` -- call them with `Name::function()`
5. The `Self` keyword inside `impl` blocks is an alias for the type being implemented

# Context & Application

Structs are one of the two building blocks (along with enums) for creating custom types in Rust. They are the primary way to group related data with named fields, analogous to objects' data attributes in object-oriented languages. The `impl` block system keeps all behavior associated with a type in one location, improving code organization.

Structs interact deeply with ownership: struct update syntax moves data just like assignment, and methods choose their ownership relationship with `self` via `&self`, `&mut self`, or `self`. The derive mechanism (e.g., `#[derive(Debug)]`) provides automatic trait implementations that cover common needs like printing for debugging.

Unlike C/C++, Rust has no `->` operator for calling methods on pointers. Automatic referencing and dereferencing eliminates this need: Rust figures out whether a method reads, mutates, or consumes the receiver and adjusts the call automatically.

# Examples

**Example 1** (Sec. 5.1): Field init shorthand and struct update syntax:
```rust
fn build_user(email: String, username: String) -> User {
    User {
        email,      // field init shorthand
        username,   // field init shorthand
        active: true,
        sign_in_count: 1,
    }
}
let user2 = User {
    email: String::from("another@example.com"),
    ..user1  // moves user1.username into user2; user1 partially invalidated
};
```

**Example 2** (Sec. 5.3): Method and associated function:
```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn square(size: u32) -> Self {
        Self { width: size, height: size }
    }
}
let sq = Rectangle::square(3);   // associated function
println!("Area: {}", sq.area()); // method call
```

**Example 3** (Sec. 5.2): Debugging with derive and dbg!:
```rust
#[derive(Debug)]
struct Rectangle { width: u32, height: u32 }

let scale = 2;
let rect1 = Rectangle {
    width: dbg!(30 * scale),  // prints to stderr, returns value
    height: 50,
};
dbg!(&rect1);  // pass reference to avoid moving rect1
```

# Relationships

## Builds Upon
- **Ownership** (Ch. 4) -- struct update syntax uses move semantics; method signatures declare borrowing relationships

## Enables
- **rust-enums-and-matching** -- enums are the other building block for custom types; enum variants can hold struct-like data
- **rust-module-system** -- struct fields have individual privacy controlled by `pub`

## Related
- **rust-enums-and-matching** -- enums can hold data like structs but model "one of many" rather than "all of these"
- **rust-module-system** -- `pub` controls which struct fields are visible outside the module

## Contrasts With
(none)

# Common Errors

- **Error**: Trying to mark individual struct fields as mutable.
  **Correction**: Rust requires the entire instance to be `mut`. You cannot have a mix of mutable and immutable fields on a single instance.

- **Error**: Using a struct instance after struct update syntax moved a non-Copy field.
  **Correction**: Struct update syntax moves data for non-Copy types. If only Copy fields (like `bool`, `u64`) are filled via `..`, the source remains valid. If a `String` or other non-Copy field is moved, the source instance (or at least that field) becomes invalid.

- **Error**: Trying to print a struct with `{}` (Display) instead of `{:?}` (Debug).
  **Correction**: Structs do not implement `Display` by default. Add `#[derive(Debug)]` and use `{:?}` or `{:#?}` for debug output.

# Common Confusions

- **Confusion**: Thinking `dbg!` works like `println!` and prints to stdout.
  **Clarification**: `dbg!` prints to stderr, takes ownership (so pass `&` if you need the value later), and returns the value. `println!` prints to stdout and takes references.

- **Confusion**: Assuming associated functions and methods are the same thing.
  **Clarification**: All functions in an `impl` block are associated functions. Only those with `self` as the first parameter are methods. Non-method associated functions use `::` syntax (e.g., `String::from`), not dot notation.

- **Confusion**: Thinking tuple structs with the same field types are interchangeable.
  **Clarification**: Each tuple struct definition creates a distinct type. `Color(i32, i32, i32)` and `Point(i32, i32, i32)` are completely different types and cannot be used interchangeably, even though their fields have the same types.

# Source Reference

Chapter 5: Using Structs to Structure Related Data. Section 5.1: Defining and Instantiating Structs (field init shorthand, struct update syntax, tuple structs, unit-like structs, ownership of struct data). Section 5.2: An Example Program Using Structs (refactoring from tuples to structs, derived traits, Debug, dbg!). Section 5.3: Methods (method syntax, automatic referencing and dereferencing, methods with parameters, associated functions, multiple impl blocks).

# Verification Notes

- Definition source: Direct synthesis from Chapter 5 source (851 lines)
- Key Properties: All items directly stated in the source text
- Confidence rationale: HIGH -- the chapter provides explicit, comprehensive coverage of all struct features
- Uncertainties: None; this is foundational, well-defined material
- Cross-reference status: Related slugs reference cards in this rust-book extraction set
