---
# === CORE IDENTIFICATION ===
concept: Generics, Traits, and Lifetimes
slug: rust-generics-traits-lifetimes

# === CLASSIFICATION ===
category: type-system
subcategory: parametric-polymorphism
tier: intermediate

# === PROVENANCE ===
source: "The Rust Programming Language"
source_slug: rust-book
authors: "Steve Klabnik and Carol Nichols"
chapter: "Generic Types, Traits, and Lifetimes"
chapter_number: 10
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "generic types"
  - "trait bounds"
  - "lifetime annotations"
  - "lifetime elision"
  - "monomorphization"
  - "blanket implementations"
  - "orphan rule"
  - "coherence"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rust-ownership-and-borrowing
  - rust-structs
  - rust-enums-and-pattern-matching
  - rust-error-handling
extends:
  - rust-common-programming-concepts
related:
  - rust-closures-and-iterators
  - rust-smart-pointers
  - rust-trait-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write functions and structs that work with multiple types?"
  - "What are traits and how do I define shared behavior?"
  - "What is the orphan rule and why does it exist?"
  - "How do lifetime annotations prevent dangling references?"
  - "What are the lifetime elision rules?"
  - "What is monomorphization and does it affect runtime performance?"
  - "How do I use trait bounds to constrain generic types?"
  - "What is a blanket implementation?"
  - "When do I need explicit lifetime annotations?"
  - "How do I combine generics, trait bounds, and lifetimes in a single function?"
---

# Quick Definition

Generics let Rust code operate on abstract types, traits define shared behavior across types (similar to interfaces), and lifetimes are a kind of generic that ensures references remain valid. Together they eliminate code duplication while preserving compile-time type safety and memory safety with zero runtime cost.

# Core Definition

Chapter 10 presents the three pillars of Rust's parametric polymorphism system. **Generics** are "abstract stand-ins for concrete types or other properties" that let functions, structs, enums, and methods work with many concrete types. **Traits** define "the functionality a particular type has and can share with other types" and can be used as **trait bounds** "to specify that a generic type can be any type that has certain behavior." **Lifetimes** are "another kind of generic" that "ensure that references are valid as long as we need them to be" (Ch. 10).

The compiler uses **monomorphization** -- "the process of turning generic code into specific code by filling in the concrete types that are used when compiled" -- so that generics impose zero runtime cost. As the source states: "Using generic types won't make your program run any slower than it would with concrete types" (Ch. 10, "Performance of Code Using Generics").

Traits enforce the **orphan rule** (a.k.a. coherence): "We can implement a trait on a type only if either the trait or the type, or both, are local to our crate" (Ch. 10, "Implementing a Trait on a Type"). This prevents conflicting implementations across crates.

Lifetime annotations "don't change how long any of the references live. Rather, they describe the relationships of the lifetimes of multiple references to each other without affecting the lifetimes" (Ch. 10, "Lifetime Annotation Syntax"). The **borrow checker** uses these annotations to verify that all references are valid.

# Prerequisites

- **Ownership and Borrowing** -- lifetimes are an extension of borrowing rules; understanding ownership is essential to grasping why lifetime annotations exist
- **Structs** -- generics and traits are demonstrated extensively on structs; method syntax (`impl`) is the foundation for trait implementations
- **Enums and Pattern Matching** -- `Option<T>` and `Result<T, E>` are key generic enums used throughout the chapter as motivating examples
- **Error Handling** -- `Result<T, E>` from Chapter 9 is used as a concrete example of a generic enum with two type parameters

# Key Properties

1. **Generic type parameters** are declared in angle brackets (`<T>`) after function names, struct names, enum names, or `impl` keywords
2. **Multiple generic parameters** are supported (e.g., `Point<T, U>`, `Result<T, E>`)
3. **Trait definitions** group method signatures; types implementing a trait must provide all required method bodies
4. **Default implementations** in traits can call other methods in the same trait, even those without defaults
5. **`impl Trait` syntax** is sugar for trait bounds in parameter position (`fn notify(item: &impl Summary)` equals `fn notify<T: Summary>(item: &T)`)
6. **The `+` syntax** combines multiple trait bounds: `impl Summary + Display` or `T: Summary + Display`
7. **`where` clauses** provide cleaner syntax when multiple generic parameters have complex trait bounds
8. **`impl Trait` in return position** lets functions return a type that implements a trait without naming the concrete type (limited to a single concrete return type)
9. **Blanket implementations** implement a trait for any type satisfying trait bounds (e.g., `impl<T: Display> ToString for T`)
10. **Lifetime parameters** use the `'a` syntax after `&` in references: `&'a i32`, `&'a mut i32`
11. **Lifetime elision rules** (three rules) allow the compiler to infer lifetimes in common patterns, reducing annotation burden
12. **`'static` lifetime** denotes references that live for the entire program duration; all string literals are `'static`
13. **Monomorphization** produces specialized code at compile time, yielding zero runtime cost for generics

# Construction / Recognition

## Defining a Generic Function:
```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}
```

## Defining and Implementing a Trait:
```rust
pub trait Summary {
    fn summarize(&self) -> String;
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}
```

## Using Trait Bounds with `where` Clause:
```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
    // ...
}
```

## Adding Lifetime Annotations:
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

## Combining Generics, Traits, and Lifetimes:
```rust
fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() { x } else { y }
}
```

## Recognizing When Lifetime Annotations Are Needed:
1. Apply elision rule 1: each reference parameter gets its own lifetime
2. Apply elision rule 2: if exactly one input lifetime, assign it to all output lifetimes
3. Apply elision rule 3: if a parameter is `&self` or `&mut self`, its lifetime goes to all output lifetimes
4. If ambiguity remains after all three rules, explicit annotations are required

# Context & Application

Chapter 10 is one of the most foundational chapters in the Rust book because generics, traits, and lifetimes pervade virtually all Rust code. Traits are the primary mechanism for polymorphism in Rust, and they underpin closures (`Fn`/`FnMut`/`FnOnce`), iterators (`Iterator`), error handling (`Display`, `Error`), operator overloading, and much more.

**Practical contexts:**
- Writing library APIs that are generic over input types
- Using trait bounds to constrain generic parameters to types with the required behavior
- Annotating lifetimes in structs that hold references or functions that accept and return references
- Using `impl Trait` for ergonomic function signatures and return types
- Publishing crates that respect the orphan rule for trait coherence

**Design impact:** The source emphasizes that "traits and trait bounds let us write code that uses generic type parameters to reduce duplication but also specify to the compiler that we want the generic type to have particular behavior." Unlike dynamically typed languages where method-not-found errors occur at runtime, "Rust moves these errors to compile time" (Ch. 10).

# Examples

**Example 1** (Ch. 10, "In Struct Definitions"): A `Point<T>` struct with a single generic parameter constrains both `x` and `y` to the same type. Using `Point<T, U>` allows different types for `x` and `y`.

**Example 2** (Ch. 10, "Using Default Implementations"): A `Summary` trait with a default `summarize` method that calls a required `summarize_author` method -- implementors only need to define `summarize_author` to get `summarize` for free:
```rust
pub trait Summary {
    fn summarize_author(&self) -> String;
    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}
```

**Example 3** (Ch. 10, Listing 10-15): Conditional method implementation using trait bounds -- `Pair<T>` always has `new`, but only has `cmp_display` when `T: Display + PartialOrd`.

**Example 4** (Ch. 10, "In Function Signatures"): The `longest` function with lifetime `'a` applied to both parameters and the return type, meaning the returned reference's lifetime equals the smaller of the two input lifetimes.

**Example 5** (Ch. 10, Listing 10-24): A struct holding a reference requires a lifetime annotation: `struct ImportantExcerpt<'a> { part: &'a str }`, meaning the struct cannot outlive the reference it holds.

**Example 6** (Ch. 10, "Lifetime Elision"): The `first_word` function compiles without lifetime annotations because elision rules 1 and 2 resolve all lifetimes: one input reference parameter gets `'a`, and since it's the only input lifetime, the output gets `'a` too.

# Relationships

## Builds Upon
- **Ownership and Borrowing** -- lifetimes formalize borrowing rules for complex reference patterns
- **Structs** -- generic structs and trait implementations extend struct capabilities
- **Enums** -- `Option<T>` and `Result<T, E>` are motivating examples of generic enums

## Enables
- **Closures and Iterators** -- closure traits (`Fn`, `FnMut`, `FnOnce`) and the `Iterator` trait are built on the trait system
- **Smart Pointers** -- `Deref`, `Drop`, and other traits define smart pointer behavior
- **Trait Objects** -- dynamic dispatch builds on traits for runtime polymorphism
- **Error Handling patterns** -- custom error types implement `Display` and `Error` traits

## Related
- **Common Programming Concepts** -- basic types and functions that generics abstract over
- **Testing** -- test assertions require `PartialEq` and `Debug` traits (derivable)

## Contrasts With
- None within this source; conceptually contrasts with dynamic typing approaches where method dispatch is resolved at runtime

# Common Errors

- **Error**: Forgetting to declare `T` after `impl` when implementing methods on a generic struct, writing `impl Point<T>` instead of `impl<T> Point<T>`.
  **Correction**: Always declare the generic type parameter after `impl` so the compiler knows `T` is generic, not a concrete type.

- **Error**: Trying to use `impl Trait` in return position when the function might return different concrete types (e.g., returning either `NewsArticle` or `SocialPost`).
  **Correction**: `impl Trait` in return position only works for a single concrete return type. Use trait objects (`Box<dyn Trait>`) for multiple return types.

- **Error**: Attempting to return a reference to a value created inside a function, even with lifetime annotations.
  **Correction**: Lifetime parameters cannot extend a value's lifetime. Return an owned type instead when the value is created locally.

- **Error**: Omitting lifetime annotations on struct fields that hold references.
  **Correction**: Every reference in a struct definition requires a lifetime annotation declared on the struct.

# Common Confusions

- **Confusion**: Thinking lifetime annotations change how long references live.
  **Clarification**: Annotations only describe relationships between lifetimes; they do not extend or shorten any reference's actual scope.

- **Confusion**: Believing generics have runtime overhead because the code seems more abstract.
  **Clarification**: Monomorphization generates specialized code at compile time, so generic code runs exactly as fast as hand-written concrete code.

- **Confusion**: Conflating `impl Trait` syntax with trait objects (`dyn Trait`).
  **Clarification**: `impl Trait` is resolved at compile time (static dispatch, monomorphized), while `dyn Trait` uses dynamic dispatch at runtime. `impl Trait` in return position is limited to a single concrete type.

- **Confusion**: Thinking the orphan rule is an arbitrary restriction rather than a coherence guarantee.
  **Clarification**: Without the orphan rule, two crates could implement the same trait for the same type, and the compiler would have no way to determine which implementation to use.

- **Confusion**: Believing `'static` means the reference is immutable or special.
  **Clarification**: `'static` simply means the reference is valid for the entire program duration. All string literals have this lifetime because they are stored in the program binary.

# Source Reference

Chapter 10: Generic Types, Traits, and Lifetimes. Sections: "Removing Duplication by Extracting a Function," "Generic Data Types" (in functions, structs, enums, methods; performance), "Defining Shared Behavior with Traits" (defining, implementing, defaults, trait bounds, `where` clauses, returning impl Trait, blanket implementations), "Validating References with Lifetimes" (dangling references, borrow checker, annotation syntax, function signatures, struct definitions, elision rules, method definitions, `'static`), and "Generic Type Parameters, Trait Bounds, and Lifetimes Together." No page numbers (online documentation source).

# Verification Notes

- Core definitions: directly adapted from Ch. 10 introductory paragraphs and section openings
- Monomorphization description: quoted from "Performance of Code Using Generics" section
- Orphan rule: quoted from "Implementing a Trait on a Type" section
- Lifetime annotation semantics: quoted from "Lifetime Annotation Syntax" section
- Lifetime elision rules: three rules enumerated directly from source text
- Confidence: HIGH -- Ch. 10 provides extensive explicit definitions, worked examples, and compiler error demonstrations for every concept
- Cross-references: all slug references correspond to planned or existing concept cards
- Uncertainties: None; all concepts have explicit definitions in the source
