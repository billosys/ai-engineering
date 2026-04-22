---
concept: The Default Trait
slug: default-trait
category: idiom
subcategory: null
tier: foundational
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "The Default Trait"
extraction_confidence: high
aliases:
  - "Default trait"
  - "std::default::Default"
  - "#[derive(Default)]"
  - "default constructor trait"
  - "default values pattern"
prerequisites:
  - constructor-idiom
extends:
  - constructor-idiom
related:
  - borrowed-types-for-arguments
  - collections-as-smart-pointers
contrasts_with: []
answers_questions:
  - "What is the Default trait in Rust?"
  - "When should I implement Default?"
  - "How do I use derive(Default)?"
  - "What is the difference between new() and Default?"
  - "How does partial struct initialization with Default work?"
---

# Quick Definition

The `Default` trait provides a standardized way to create a type's default value. Unlike `new()`, which is a naming convention specific to each type, `Default` is a trait that enables generic programming -- any code that needs "a default value of type T" can require `T: Default`.

# Core Definition

"Many types in Rust have a constructor. However, this is *specific* to the type; Rust cannot abstract over 'everything that has a `new()` method'. To allow this, the `Default` trait was conceived, which can be used with containers and other generic types (e.g. see `Option::unwrap_or_default()`). Notably, some containers already implement it where applicable." (Ch. 1, "The Default Trait")

"Not only do one-element containers like `Cow`, `Box` or `Arc` implement `Default` for contained `Default` types, one can automatically `#[derive(Default)]` for structs whose fields all implement it, so the more types implement `Default`, the more useful it becomes."

"On the other hand, constructors can take multiple arguments, while the `default()` method does not. There can even be multiple constructors with different names, but there can only be one `Default` implementation per type."

# Prerequisites

- **constructor-idiom** -- the Default trait is an abstraction over the concept of constructors; understanding why Rust uses `new()` motivates why `Default` exists as a trait

# Key Properties

1. `Default` is a trait in `std::default` with a single method: `fn default() -> Self`
2. `Default::default()` takes no arguments -- it always produces the same default value
3. `#[derive(Default)]` automatically implements `Default` if all fields implement it
4. `Option` defaults to `None`, `Vec` to empty, `String` to empty, `bool` to `false`, numeric types to `0`, `Duration` to zero
5. `Cow`, `Box`, and `Arc` implement `Default` when their contained type does
6. There can only be one `Default` implementation per type, but multiple named constructors
7. `Default` enables the struct update syntax: `MyStruct { field: value, ..Default::default() }`
8. The more types implement `Default`, the more broadly useful the trait becomes (network effect)

# Construction / Recognition

## To Implement Default:
1. If all fields implement `Default`, add `#[derive(Default)]` to the struct
2. Otherwise, write a manual `impl Default for MyType { fn default() -> Self { ... } }`
3. Ensure the default value is sensible -- it should represent the most common or safest starting configuration

## To Use Default for Partial Initialization:
1. Set the fields you care about explicitly
2. Use `..Default::default()` for the rest:
   ```rust
   let conf = MyConfiguration {
       check: true,
       ..Default::default()
   };
   ```

## To Use in Generic Code:
1. Add `T: Default` as a trait bound
2. Call `T::default()` or use methods like `Option::unwrap_or_default()`

# Context & Application

The `Default` trait bridges the gap between Rust's lack of constructors and the need for generic "give me a default" functionality. In languages with constructors, a default constructor (no arguments) serves this role. In Rust, `Default` provides the same capability as a trait, enabling it to work in generic contexts.

**Typical contexts:**
- Configuration structs where most fields have sensible defaults
- Generic containers that need to create default values for their elements
- The `*or_default()` family of standard library methods
- Struct update syntax for partial initialization
- Any `#[derive]` chain where `Default` is expected (often alongside `Debug`, `Clone`, `PartialEq`)

# Examples

**Example 1** (Ch. 1, "The Default Trait"): A configuration struct using `#[derive(Default)]` and partial initialization:

```rust
use std::{path::PathBuf, time::Duration};

// note that we can simply auto-derive Default here.
#[derive(Default, Debug, PartialEq)]
struct MyConfiguration {
    // Option defaults to None
    output: Option<PathBuf>,
    // Vecs default to empty vector
    search_path: Vec<PathBuf>,
    // Duration defaults to zero time
    timeout: Duration,
    // bool defaults to false
    check: bool,
}

impl MyConfiguration {
    // add setters here
}

fn main() {
    // construct a new instance with default values
    let mut conf = MyConfiguration::default();
    // do something with conf here
    conf.check = true;
    println!("conf = {conf:#?}");

    // partial initialization with default values, creates the same instance
    let conf1 = MyConfiguration {
        check: true,
        ..Default::default()
    };
    assert_eq!(conf, conf1);
}
```

The example demonstrates that `Option<PathBuf>` defaults to `None`, `Vec<PathBuf>` to empty, `Duration` to zero, and `bool` to `false`. It also shows the struct update syntax `..Default::default()` for partial initialization.

# Relationships

## Builds Upon
- **constructor-idiom** -- `Default` is the trait-based abstraction of the constructor convention

## Enables
- Generic programming with default values (e.g., `T: Default` bounds)
- The `*or_default()` standard library family

## Related
- **borrowed-types-for-arguments** -- another foundational API design idiom
- **collections-as-smart-pointers** -- collections like `Vec` implement `Default`

## Contrasts With
- None explicitly stated (implicitly contrasts with `new()` which can take arguments and have multiple variants)

# Common Errors

- **Error**: Implementing `Default` with a value that is not truly the "default" but rather a specific configuration.
  **Correction**: `Default` should represent the most neutral, zero-cost, or safest starting point. Use named constructors for specific configurations.

- **Error**: Forgetting to derive `Default` and then being unable to use the type with `*or_default()` methods or in generic contexts.
  **Correction**: Derive `Default` for any struct where all fields implement it and a sensible default exists.

# Common Confusions

- **Confusion**: Thinking `Default` replaces the need for `new()`.
  **Clarification**: `Default` and `new()` serve different purposes. `new()` is the conventional constructor that may take arguments. `Default` is a trait for generic code. Both should be implemented when a no-argument constructor is reasonable.

- **Confusion**: Thinking `#[derive(Default)]` works for enums automatically.
  **Clarification**: For enums, `#[derive(Default)]` requires annotating one variant with `#[default]` (stabilized in Rust 1.62). Without this annotation, you must implement `Default` manually.

# Source Reference

Chapter 1: Idioms, "The Default Trait" section. See also linked resources: the constructor idiom, the `Default` trait documentation, `Option::unwrap_or_default()`, and the `derive(new)` crate.

# Verification Notes

- Definition: Direct quotation from the Description subsection
- Key Properties: All from explicit statements in the source, with standard library defaults verified
- Example: Directly from the source with original code and comments
- Confidence: HIGH -- the source provides explicit description with a detailed code example
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
