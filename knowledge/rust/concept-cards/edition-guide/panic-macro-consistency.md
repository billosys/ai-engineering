---
concept: Panic Macro Consistency
slug: panic-macro-consistency
category: edition-2021
subcategory: null
tier: advanced
source: "Rust Edition Guide"
source_slug: edition-guide
authors: "The Rust Project"
chapter: "04-rust-2021"
chapter_number: 4
pdf_page: null
section: "Panic macro consistency"
extraction_confidence: high
aliases:
  - "panic format string"
  - "non_fmt_panics"
  - "panic 2021"
prerequisites:
  - rust-2021-edition
extends: []
related:
  - edition-migration
contrasts_with: []
answers_questions:
  - "How does panic!() behave differently in Rust 2021?"
  - "Why can't I use panic!(variable) in Rust 2021?"
  - "What is panic_any?"
  - "What is the non_fmt_panics lint?"
  - "Are core::panic! and std::panic! the same in Rust 2021?"
---

# Quick Definition

In Rust 2021, `panic!()` always processes its first argument as a format string (like `println!()`), making it consistent across `core` and `std`. This means `panic!("{")` is no longer valid (must escape as `{{`), `panic!(variable)` is no longer valid (must use `panic!("{}", variable)` or `std::panic::panic_any(variable)`), and `panic!("{}") ` is an error (missing format argument). The same changes apply to `assert!(expr, ..)`.

# Core Definition

"The new `panic!()` macro will no longer accept arbitrary expressions as the only argument. It will, just like `println!()`, always process the first argument as format string. Since `panic!()` will no longer accept arbitrary payloads, `panic_any()` will be the only way to panic with something other than a formatted string." (Edition Guide, Ch. 4: Rust 2021, "Panic macro consistency")

In Rust 2018, `panic!()` only used string formatting when invoked with more than one argument. With a single argument, it accepted anything -- including non-strings like `panic!(123)`, which produced the unhelpful message `panicked at 'Box<Any>'`.

# Prerequisites

- **Rust 2021 Edition** (`rust-2021-edition`) -- the panic macro behavior change is part of the 2021 edition

# Key Properties

1. `panic!()` always processes the first argument as a format string in Rust 2021
2. `panic!("{}", 1)` works in all editions (panics with message "1")
3. `panic!("{}")` was OK in Rust 2018 (panicked with literal "{}") but is an error in 2021 (missing argument)
4. `panic!(variable)` is an error in Rust 2021 (first argument must be a string literal)
5. `panic!(123)` is no longer accepted (use `std::panic::panic_any(123)`)
6. `std::panic::panic_any()` is the replacement for non-string panic payloads
7. `core::panic!()` and `std::panic!()` are identical in Rust 2021 (previously had historical differences)
8. The same changes apply to `assert!(expr, ..)`
9. The `non_fmt_panics` lint has been a default warning since Rust 1.50
10. This change prepares for implicit format arguments (`panic!("hello {name}")`)

# Construction / Recognition

## To Migrate Panic Calls:
1. Run `cargo fix --edition` to automatically migrate
2. For `panic!(MyStruct)`: change to `std::panic::panic_any(MyStruct)` (note: function, not macro)
3. For `panic!("Some curlies: {}")`: change to `panic!("{}", "Some curlies: {}")` or `panic!("Some curlies: {{}}")`
4. For `panic!(variable)`: change to `panic!("{}", variable)` to use `Display`, or `std::panic::panic_any(variable)` for raw payloads

## To Identify Affected Code:
1. Look for `panic!()` with a single non-literal argument
2. Look for `panic!()` with string literals containing unescaped `{` or `}` but no format arguments
3. Look for `panic!()` with non-string arguments like integers
4. Check for the `non_fmt_panics` lint warning

# Context & Application

The inconsistency in `panic!()` was a historical artifact. When invoked with multiple arguments, `panic!()` used `format_args!()` for string formatting. With a single argument, it treated the argument as an opaque value. This led to confusing behavior: `panic!("{}")` silently used the literal string "{}" as the panic message, and `panic!(123)` produced an opaque `Box<Any>` payload.

This became especially problematic with the stabilization of implicit format arguments, where `println!("hello {name}")` is shorthand for `println!("hello {}", name)`. Without the 2021 change, `panic!("hello {name}")` would not interpolate `name` -- it would panic with the literal string "hello {name}".

The unification of `core::panic!()` and `std::panic!()` also eliminates a subtle source of bugs when toggling `#![no_std]`.

# Examples

**Example 1** (Behavioral differences across editions, "Details" section):

```rust
// Rust 2018:
panic!("{}", 1);  // Ok, panics with message "1"
panic!("{}");     // Ok, panics with message "{}" (literal string)

let a = "{";
println!(a);      // Error: first argument must be a format string literal
panic!(a);        // Ok in 2018: panic doesn't care about the format

// Rust 2021:
panic!("{}", 1);  // Ok, panics with message "1"
panic!("{}");     // Error: missing argument for format string
panic!(a);        // Error: must be a string literal
```

**Example 2** (Migrating non-string payloads, "Migration" section):

```rust
// Rust 2018:
panic!(MyStruct);    // Worked but produced unhelpful "Box<Any>" message

// Rust 2021:
std::panic::panic_any(MyStruct);  // Explicit function for non-string payloads
```

**Example 3** (Escaping curly braces, "Migration" section):

```rust
// Rust 2018:
panic!("Some curlies: {}");  // Ok, literal string

// Rust 2021 -- two options:
panic!("{}", "Some curlies: {}");    // Pass as format argument
panic!("Some curlies: {{}}");        // Escape the braces
```

# Relationships

## Builds Upon
- **rust-2021-edition** -- panic macro consistency is part of the 2021 edition

## Enables
- No downstream concepts directly (but enables future implicit format arguments in panic)

## Related
- **edition-migration** -- `cargo fix --edition` handles the migration

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Using `panic!(my_error)` where `my_error` is a variable, not a string literal.
  **Correction**: Use `panic!("{}", my_error)` to format using `Display`, or `std::panic::panic_any(my_error)` if you need to pass a non-string payload that can be caught with `catch_unwind`.

- **Error**: Writing `panic!("Value: {}")` intending the literal string "Value: {}" as the message.
  **Correction**: Escape the braces: `panic!("Value: {{}}")` or pass as an argument: `panic!("{}", "Value: {}")`.

# Common Confusions

- **Confusion**: Thinking `std::panic::panic_any()` is a macro.
  **Clarification**: `panic_any()` is a function, not a macro. This is noted explicitly in the migration guidance.

- **Confusion**: Thinking `core::panic!()` and `std::panic!()` were always identical.
  **Clarification**: Before Rust 2021, there were "some historical differences between those two, which can be noticeable when switching `#![no_std]` on or off." They are unified in Rust 2021.

- **Confusion**: Thinking only `panic!()` is affected.
  **Clarification**: "The same applies to `assert!(expr, ..)`. " The format string consistency applies to `assert!` as well.

# Source Reference

Chapter 4: Rust 2021, "Panic macro consistency" section. References RFC 3007 ("panic plan") and RFC 2795 (implicit format arguments). The `non_fmt_panics` lint has been a default warning since Rust 1.50.

# Verification Notes

- Definition source: Direct quotation from "Panic macro consistency" section, "Details" subsection
- Key Properties: All from explicit statements in the source
- Confidence rationale: HIGH -- the source provides clear before/after examples and comprehensive migration guidance
- Uncertainties: None
- Cross-reference status: All slugs reference cards in this extraction set or Agent A's set
