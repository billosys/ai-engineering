---
concept: Builder Pattern
slug: builder-pattern
category: creational-pattern
subcategory: null
tier: foundational
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "02-design-patterns"
chapter_number: 2
pdf_page: null
section: "Builder"
extraction_confidence: high
aliases:
  - "builder"
  - "builder helper"
  - "FooBuilder pattern"
prerequisites:
  - newtype-pattern
extends: []
related:
  - command-pattern
  - strategy-pattern
contrasts_with: []
answers_questions:
  - "How do I construct complex objects with many optional fields in Rust?"
  - "How do I avoid having many constructors for one type?"
  - "What replaces function overloading for constructors in Rust?"
---

# Quick Definition

The Builder pattern constructs an object through calls to a separate builder helper, allowing step-by-step configuration before producing the final value. It replaces the need for multiple constructors or function overloading, which Rust does not support.

# Core Definition

The Builder pattern uses a separate builder type to accumulate configuration and then produce the target object via a `build()` method. The source describes it as: "Construct an object with calls to a builder helper." Builder methods typically take and return the builder (by value or mutable reference), enabling method chaining. A convenience `builder()` method on the target type helps users discover the builder. (Ch. 2, "Builder")

# Prerequisites

- **newtype-pattern** -- understanding struct construction and type wrappers helps motivate why a separate builder type is useful for managing complex construction

# Key Properties

1. A separate builder struct accumulates configuration state before constructing the target
2. Builder methods take and return the builder, enabling fluent method chaining (e.g., `FooBuilder::new().name("x".into()).build()`)
3. The builder can derive `Default` so that unset fields use sensible defaults
4. A `build()` method consumes (or borrows) the builder to produce the final object
5. The target type can provide a `fn builder() -> FooBuilder` method to aid discoverability
6. If `build()` takes `&self` rather than `self`, the builder can serve as a template for constructing many instances
7. The pattern compensates for Rust's lack of function overloading and default parameter values

# Construction / Recognition

## To Implement the Builder Pattern:
1. Define the target struct with its full set of fields
2. Define a corresponding builder struct (often `TargetBuilder`) with the same or optional versions of those fields
3. Implement `Default` for the builder if appropriate
4. Implement builder methods that set individual fields and return `self` (or `&mut self`)
5. Implement a `build()` method that constructs and returns the target
6. Optionally add a `Target::builder()` associated function that returns a default builder

## To Recognize the Pattern:
1. A separate struct whose sole purpose is configuring and producing another struct
2. Method chaining on the builder type
3. A terminal `build()` method that produces the target

# Context & Application

This pattern is seen more frequently in Rust than in many other languages because Rust lacks overloading and default values for function parameters. Since you can only have a single method with a given name, having multiple constructors is less ergonomic in Rust than in C++, Java, or others.

The pattern is often used where the builder object is useful in its own right, not merely as a temporary construction aid. The source cites `std::process::Command` as a builder for `Child` (a process), where the `T`/`TBuilder` naming convention is not used.

Taking and returning the builder as a mutable reference (rather than by value) is often more ergonomic and efficient. The borrow checker makes this work naturally, allowing both incremental construction and one-liner chaining styles.

# Examples

**Example 1** (Ch. 2, "Builder" -- Example): The source shows a `Foo`/`FooBuilder` pair where `FooBuilder` derives `Default`, provides a `new()` constructor and a `name()` method that returns `FooBuilder` by value, and a `build()` method that produces `Foo`. Usage: `FooBuilder::new().name(String::from("Y")).build()`.

**Example 2** (Ch. 2, "Builder" -- Discussion): The source shows the mutable-reference variant: `let mut fb = FooBuilder::new(); fb.a(); fb.b(); let f = fb.build();` as well as `FooBuilder::new().a().b().build()`. Both styles work when builder methods take and return `&mut self`.

# Relationships

## Builds Upon
- **newtype-pattern** -- builders often wrap the same fields as the target type

## Enables
- Complex configuration APIs (e.g., `std::process::Command`)
- Backwards-compatible API evolution (new fields can be added to the builder without breaking existing callers)

## Related
- **command-pattern** -- `std::process::Command` is both a builder and a command
- **strategy-pattern** -- both patterns separate concerns; strategy separates behavior, builder separates construction

## Contrasts With
- Direct struct construction (simpler but inflexible for many fields or defaults)
- Constructor functions (limited to a single signature per name in Rust)

# Common Errors

- **Error**: Making the builder's `build()` method fallible without returning `Result`.
  **Correction**: If construction can fail (e.g., required fields not set), return `Result<Target, Error>` from `build()`.

- **Error**: Forgetting to provide a discoverability method like `Target::builder()`.
  **Correction**: Add `pub fn builder() -> TargetBuilder` to the target type so IDE autocompletion helps users find the builder.

# Common Confusions

- **Confusion**: Thinking the builder must always consume itself on `build()`.
  **Clarification**: The source notes that if you can avoid consuming the builder, "that is an advantage. It means we can use the FooBuilder as a template for constructing many Foos."

- **Confusion**: Assuming the builder and target must follow the `T`/`TBuilder` naming convention.
  **Clarification**: The source notes that `std::process::Command` is a builder for `Child` and does not use this convention. The naming should reflect the API's semantics.

# Source Reference

Chapter 2: Design Patterns, "Builder" section (Creational Patterns). Includes a full code example with `Foo`/`FooBuilder`, a discussion of Rust-specific motivation (no overloading, no default parameters), and references to `std::process::Command`, the `derive_builder` crate, and the Wikipedia article on the Builder pattern.

# Verification Notes

- Definition source: Direct from "Description" subsection opening line; elaborated from "Motivation" and "Discussion"
- Key Properties: Derived from the code example and discussion text
- Confidence rationale: HIGH -- the source provides a complete code example, detailed motivation, advantages/disadvantages, and discussion
- Uncertainties: None
- Cross-reference status: `command-pattern`, `strategy-pattern`, `newtype-pattern` are from Agent 3's extraction set
