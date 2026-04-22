---
concept: Constructor Idiom
slug: constructor-idiom
category: idiom
subcategory: null
tier: foundational
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Constructors"
extraction_confidence: high
aliases:
  - "constructors"
  - "new() convention"
  - "associated function constructor"
  - "Rust constructor pattern"
prerequisites: []
extends: []
related:
  - default-trait
  - borrowed-types-for-arguments
contrasts_with: []
answers_questions:
  - "How do you create constructors in Rust?"
  - "What is the new() convention in Rust?"
  - "Does Rust have constructors?"
  - "Should I implement both Default and new()?"
  - "What is an associated function in Rust?"
---

# Quick Definition

Rust has no constructors as a language construct. Instead, the convention is to use an associated function named `new` that returns `Self`. Types should typically implement both `new()` and the `Default` trait when a no-argument constructor is reasonable.

# Core Definition

"Rust does not have constructors as a language construct. Instead, the convention is to use an associated function `new` to create an object." (Ch. 1, "Constructors")

"It is common and expected for types to implement both `Default` and an empty `new` constructor. `new` is the constructor convention in Rust, and users expect it to exist, so if it is reasonable for the basic constructor to take no arguments, then it should, even if it is functionally identical to default." (Ch. 1, "Constructors")

"The advantage of implementing or deriving `Default` is that your type can now be used where a `Default` implementation is required, most prominently, any of the `*or_default` functions in the standard library."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Rust has no constructor keyword or special constructor syntax
2. The convention is an associated function named `new` (no `self` parameter)
3. `new` returns `Self` (the type being constructed)
4. Types should implement both `new()` and `Default` when a no-argument constructor makes sense
5. `Default` can be derived with `#[derive(Default)]` if all fields implement `Default`
6. `new` can take parameters; `Default::default()` cannot
7. There can be multiple named constructors (e.g., `new`, `with_capacity`, `from_parts`) but only one `Default` implementation
8. Users expect `new` to exist -- it is part of Rust's API conventions

# Construction / Recognition

## To Implement the Constructor Idiom:
1. Define a `pub struct` with its fields
2. Create an `impl` block for the struct
3. Define `pub fn new(...) -> Self` as an associated function (no `self` parameter)
4. If a zero-argument constructor makes sense, also implement `Default`
5. If all fields implement `Default`, use `#[derive(Default)]` instead of a manual implementation
6. For complex construction with many optional parameters, consider the builder pattern instead

## To Recognize:
1. Look for `impl TypeName { pub fn new(...) -> Self { ... } }`
2. The function should not take `&self` or `&mut self` -- it is an associated function, not a method
3. It should return `Self`, not a reference

# Context & Application

Since Rust has no class-based inheritance or literal constructor syntax, the `new()` convention fills the role that constructors play in other languages. This is purely a convention -- there is nothing special about the name `new` to the compiler. However, the Rust community strongly expects it, and the API Guidelines document it as a standard.

**Typical contexts:**
- Every struct that needs to be instantiated by external code
- Library APIs where construction requires validation or setup
- Any type where direct struct-literal construction is not appropriate (e.g., fields are private)

**API Guidelines reference:** The source links to the Rust API Guidelines item C-COMMON-TRAITS, which recommends implementing both `Default` and `new`.

# Examples

**Example 1** (Ch. 1, "Constructors"): A basic constructor with a parameter:

```rust
/// Time in seconds.
///
/// # Example
///
/// ```
/// let s = Second::new(42);
/// assert_eq!(42, s.value());
/// ```
pub struct Second {
    value: u64,
}

impl Second {
    // Constructs a new instance of [`Second`].
    // Note this is an associated function - no self.
    pub fn new(value: u64) -> Self {
        Self { value }
    }

    /// Returns the value in seconds.
    pub fn value(&self) -> u64 {
        self.value
    }
}
```

**Example 2** (Ch. 1, "Constructors"): Manual `Default` implementation:

```rust
pub struct Second {
    value: u64,
}

impl Second {
    /// Returns the value in seconds.
    pub fn value(&self) -> u64 {
        self.value
    }
}

impl Default for Second {
    fn default() -> Self {
        Self { value: 0 }
    }
}
```

**Example 3** (Ch. 1, "Constructors"): Using `#[derive(Default)]` when all fields implement `Default`:

```rust
#[derive(Default)]
pub struct Second {
    value: u64,
}

impl Second {
    /// Returns the value in seconds.
    pub fn value(&self) -> u64 {
        self.value
    }
}
```

# Relationships

## Builds Upon
- None -- this is a foundational idiom

## Enables
- **default-trait** -- the Default trait provides a standardized default constructor

## Related
- **borrowed-types-for-arguments** -- constructor parameters should follow the borrowed types idiom where appropriate

## Contrasts With
- None explicitly stated (implicitly contrasts with OOP constructors and the builder pattern for complex cases)

# Common Errors

- **Error**: Implementing `Default` but not `new()` for a type that has an obvious zero-argument constructor.
  **Correction**: Implement both. Users expect `new()` to exist even if it is functionally identical to `default()`.

- **Error**: Making the constructor a method (`fn new(&self, ...) -> Self`) instead of an associated function.
  **Correction**: Constructors should be associated functions with no `self` parameter: `fn new(...) -> Self`.

# Common Confusions

- **Confusion**: Thinking `new` is a keyword or has special compiler support in Rust.
  **Clarification**: `new` is purely a naming convention. The compiler treats it as any other associated function. The convention is enforced by community norms and the API Guidelines, not the language.

- **Confusion**: Thinking you must choose between `new()` and `Default`.
  **Clarification**: "It is common and expected for types to implement both." `new()` is for direct construction; `Default` enables generic code (e.g., `Option::unwrap_or_default()`).

# Source Reference

Chapter 1: Idioms, "Constructors" section. Covers the `new()` convention, Default constructors, and `#[derive(Default)]`. See also links to: the Rust Book on associated functions, std::default::Default documentation, std `*or_default` functions, and API Guidelines C-COMMON-TRAITS.

# Verification Notes

- Definition: Direct quotation from the Description subsection
- Key Properties: All from explicit statements in the source
- Examples: All three examples directly from the source with original code
- Confidence: HIGH -- the source provides explicit description with multiple code examples and API Guidelines references
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
