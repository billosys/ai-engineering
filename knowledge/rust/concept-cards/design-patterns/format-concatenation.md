---
concept: String Concatenation with format!
slug: format-concatenation
category: idiom
subcategory: null
tier: intermediate
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Concatenating strings with format!"
extraction_confidence: high
aliases:
  - "concatenating strings with format!"
  - "format macro for strings"
  - "string concatenation idiom"
  - "format! string building"
prerequisites:
  - borrowed-types-for-arguments
extends: []
related:
  - constructor-idiom
contrasts_with: []
answers_questions:
  - "What is the idiomatic way to concatenate strings in Rust?"
  - "Should I use format! or push_str for string concatenation?"
  - "When is format! better than manual string building?"
  - "What are the trade-offs of format! vs push/push_str?"
---

# Quick Definition

Use the `format!` macro for string concatenation, especially when mixing literal and non-literal strings. While `push`, `push_str`, and the `+` operator work, `format!` is usually the most succinct and readable approach.

# Core Definition

"It is possible to build up strings using the `push` and `push_str` methods on a mutable `String`, or using its `+` operator. However, it is often more convenient to use `format!`, especially where there is a mix of literal and non-literal strings." (Ch. 1, "Concatenating strings with format!")

"Using `format!` is usually the most succinct and readable way to combine strings." (Advantages)

"It is usually not the most efficient way to combine strings - a series of `push` operations on a mutable string is usually the most efficient (especially if the string has been pre-allocated to the expected size)." (Disadvantages)

# Prerequisites

- **borrowed-types-for-arguments** -- understanding `&str` vs `String` is essential for knowing when `format!` returns a new `String` from borrowed inputs

# Key Properties

1. `format!` returns a new `String`, allocating on the heap
2. `format!` accepts inline variable names (e.g., `format!("Hello {name}!")`)
3. `format!` is the most readable approach when mixing literals with variables
4. `push` and `push_str` on a mutable `String` are more efficient, especially with pre-allocation
5. The `+` operator also concatenates strings but is less readable for complex cases
6. `format!` uses the same syntax as `println!` but returns the string instead of printing it

# Construction / Recognition

## To Apply This Idiom:
1. When building a string from a mix of literal text and variables, use `format!("literal {variable} more literal")`
2. Avoid manually creating a mutable `String`, calling `.push_str()`, and returning it
3. Use inline variable capture syntax for cleaner code: `format!("Hello {name}!")` instead of `format!("Hello {}!", name)`

## When to Use Alternatives:
1. If building a string in a hot loop or performance-critical path, prefer pre-allocated `String` with `push`/`push_str`
2. If only concatenating two strings, the `+` operator may be clearer: `first + &second`

# Context & Application

This is one of the simplest Rust idioms but an important one for code readability. New Rust programmers coming from languages like C or Java may instinctively build strings with manual mutation. The `format!` macro provides a declarative, template-like approach that makes the final string shape immediately visible.

**Typical contexts:**
- Building display strings, log messages, error messages
- Constructing file paths or URLs from components
- Any situation combining literal and dynamic text

# Examples

**Example 1** (Ch. 1, "Concatenating strings with format!"): The source shows the contrast between manual building and `format!`:

```rust
fn say_hello(name: &str) -> String {
    // We could construct the result string manually.
    // let mut result = "Hello ".to_owned();
    // result.push_str(name);
    // result.push('!');
    // result

    // But using format! is better.
    format!("Hello {name}!")
}
```

The manual approach requires four lines (create, push, push, return). The `format!` approach is a single, self-documenting expression.

# Relationships

## Builds Upon
- **borrowed-types-for-arguments** -- `format!` naturally works with `&str` arguments

## Enables
- None specifically

## Related
- **constructor-idiom** -- constructors may use `format!` for building derived string fields

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `format!` in a tight loop where performance matters, creating many intermediate allocations.
  **Correction**: Pre-allocate a `String` with `String::with_capacity()` and use `push_str()` for performance-critical string building.

- **Error**: Using the old-style positional syntax `format!("{}", name)` when the variable name is available directly.
  **Correction**: Use inline variable capture: `format!("{name}")` is cleaner (stabilized in Rust 1.58).

# Common Confusions

- **Confusion**: Thinking `format!` is always the best choice for string concatenation.
  **Clarification**: The source explicitly notes that "a series of `push` operations on a mutable string is usually the most efficient." `format!` optimizes for readability, not performance.

- **Confusion**: Thinking `format!` is as expensive as formatted I/O in other languages.
  **Clarification**: `format!` is a compile-time macro that generates efficient formatting code. The cost is primarily the heap allocation for the new `String`, not the formatting itself.

# Source Reference

Chapter 1: Idioms, "Concatenating strings with format!" section. The section is concise, covering Description, Example, Advantages, and Disadvantages.

# Verification Notes

- Definition: Direct quotation from the Description subsection
- Advantages/Disadvantages: Direct quotations from the source
- Example: Directly from the source with original code and comments
- Confidence: HIGH -- the source provides an explicit description with a clear code example
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set
